"""
Batch extraction using Together AI's batch API with two aggregation modes:

  majority_vote  - keep entities/relationships appearing in >= ceil(N/2) trials
  union          - keep ALL entities/relationships from any trial (threshold=1),
                   then let downstream aggregation deduplicate

Phase 1: Submit N_TRIALS entity-extraction requests per paper as a single batch.
Phase 2: After entity consolidation, submit N_TRIALS relationship requests per paper.

Usage:
    python scripts/batch_majority_vote.py \
        --papers_url outputs/experiments/inputs/paper_list_20_llm_for_extraction.json \
        --model "deepseek-ai/DeepSeek-V3.1" \
        --temperature 0.6 \
        --n_trials 3 \
        --mode majority_vote \
        --sandbox outputs/sandbox_batch_mv

    python scripts/batch_majority_vote.py \
        --papers_url outputs/experiments/inputs/paper_list_20_llm_for_extraction.json \
        --model "deepseek-ai/DeepSeek-V3.1" \
        --temperature 0.6 \
        --n_trials 3 \
        --mode union \
        --sandbox outputs/sandbox_batch_union
"""

import argparse
import json
import os
import random
import re
import sys
import tempfile
import time
from pathlib import Path
from threading import Lock, Semaphore

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from misc.logging_config import setup_logging, get_logger

setup_logging(run_name="batch_mv")
logger = get_logger(__name__)

# ---------------------------------------------------------------------------
# Rate limiting & retry helpers
# ---------------------------------------------------------------------------

# (max_requests_per_minute, max_concurrent_requests)
# Together Tier 4 = 4,500 RPM; OpenAI Tier 5 = 10,000 RPM;
# Google Tier 1 = 300 RPM (Flash), Tier 2 = 2,000 RPM.
# Values below use ~80% of tier cap as safety margin.
PROVIDER_LIMITS = {
    "together": (3600, 15),
    "google":   (120, 8),
    "openai":   (8000, 30),
}

_FAILED_SENTINEL = "__FAILED__"


class _RateLimiter:
    """Lightweight sliding-window RPM limiter + concurrency semaphore."""

    def __init__(self, max_rpm: int = 60, max_concurrent: int = 4):
        self.max_rpm = max_rpm
        self.max_concurrent = max_concurrent
        self._sem = Semaphore(max_concurrent)
        self._timestamps: list[float] = []
        self._lock = Lock()

    def acquire(self):
        self._sem.acquire()
        sleep_time = 0.0
        with self._lock:
            now = time.time()
            self._timestamps = [
                t for t in self._timestamps if now - t < 60
            ]
            if len(self._timestamps) >= self.max_rpm:
                sleep_time = (
                    60 - (now - self._timestamps[0])
                    + random.uniform(1, 3)
                )
        if sleep_time > 0:
            logger.info(
                "Rate limit: sleeping %.1fs", sleep_time,
            )
            time.sleep(sleep_time)
        with self._lock:
            self._timestamps.append(time.time())

    def release(self):
        self._sem.release()


def _is_retryable(exc: Exception) -> bool:
    """Check if an API error is transient and worth retrying."""
    status = getattr(exc, "status_code", None)
    if status in (429, 500, 502, 503, 529):
        return True
    name = type(exc).__name__
    return name in ("APITimeoutError", "APIConnectionError", "Timeout", "ConnectionError")


def load_papers(path: str):
    with open(path) as f:
        papers = json.load(f)
    # Filter to LLM-flagged papers and deduplicate by (name, path).
    # Duplicates can sneak in from scraping (e.g., truncated titles like "A"/"E"),
    # and OpenAI's batch API rejects the whole batch on duplicate custom_ids.
    seen = set()
    out = []
    n_dupes = 0
    for p in papers:
        if not p.get("is_LLM_paper", False):
            continue
        key = (p.get("name", ""), p.get("path", ""))
        if key in seen:
            n_dupes += 1
            continue
        seen.add(key)
        out.append(p)
    if n_dupes:
        logger.warning(
            "load_papers: dropped %d duplicate (name, path) entries from %s",
            n_dupes, path,
        )
    return out


def extract_text(pdf_path: str, max_pages: int = 0) -> str:
    from src.utils import extract_text_from_pdf
    text = extract_text_from_pdf(pdf_path, max_pages=max_pages) or ""
    if len(text) > 500_000:
        text = text[:500_000] + "\n\n[... text truncated ...]"
    return text


def parse_json_response(raw: str) -> dict:
    raw = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
    fence = re.search(r"^```(?:json)?\s*\n(.*?)\n```\s*$", raw, re.DOTALL)
    if fence:
        raw = fence.group(1).strip()
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        from utils.json import clean_messy_string, clean_to_dict
        parsed = clean_to_dict(clean_messy_string(raw))
        if isinstance(parsed, str):
            try:
                parsed = json.loads(parsed)
            except json.JSONDecodeError:
                parsed = clean_to_dict(clean_messy_string(parsed))
        return parsed if isinstance(parsed, dict) else {"error": "Parse failed"}


def _is_reasoning_model(model: str) -> bool:
    """Check if a model is a reasoning/thinking model that doesn't accept temperature."""
    m = model.lower()
    # OpenAI reasoning models: o3, o4-mini (but NOT gpt-5.4, gpt-5.4-mini etc.)
    if any(m.startswith(p) for p in ("o3", "o4")):
        return True
    # gpt-5 (exact) is reasoning, but gpt-5.4/gpt-5.4-mini are not
    if m == "gpt-5" or m == "gpt-5-mini":
        return True
    # Together thinking models
    if "thinking" in m or "-r1" in m:
        return True
    return False


def _token_limit_key(model: str) -> str:
    """Return the correct token limit parameter name for this model.
    OpenAI reasoning/frontier models (o3, o4-mini, gpt-5*) need 'max_completion_tokens';
    others use 'max_tokens'."""
    m = model.lower()
    if any(m.startswith(p) for p in ("o3", "o4", "gpt-5", "gpt-4.1")):
        return "max_completion_tokens"
    return "max_tokens"


def build_entity_jsonl(papers, paper_texts, model, temperature, n_trials):
    """Build JSONL lines for entity extraction: papers × n_trials."""
    from misc.prompts import EXTRACT_ENTITIES_PROMPT

    tok_key = _token_limit_key(model)
    reasoning = _is_reasoning_model(model)
    lines = []
    for paper in papers:
        name = paper["name"]
        text = paper_texts[name]
        if not text.strip():
            continue
        user_content = f"{EXTRACT_ENTITIES_PROMPT}\n\n---\nPaper text (extracted from PDF):\n\n{text}"
        for trial in range(n_trials):
            custom_id = json.dumps({"paper": name, "trial": trial, "phase": "entities"})
            body = {
                "model": model,
                "messages": [
                    {"role": "system", "content": "Respond with valid JSON only. Extract entities (constructs, measurements, behaviors) — no relationships."},
                    {"role": "user", "content": user_content},
                ],
                tok_key: 16384,
            }
            if not reasoning:
                body["temperature"] = temperature
            line = {
                "custom_id": custom_id,
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": body,
            }
            lines.append(json.dumps(line, ensure_ascii=False))
    return lines


def build_relationship_jsonl(papers, paper_texts, voted_entities, model, temperature, n_trials):
    """Build JSONL lines for relationship extraction using voted entities."""
    from misc.prompts import EXTRACT_RELATIONSHIPS_PROMPT

    tok_key = _token_limit_key(model)
    reasoning = _is_reasoning_model(model)
    lines = []
    for paper in papers:
        name = paper["name"]
        text = paper_texts[name]
        if not text.strip():
            continue
        entities = voted_entities.get(name)
        if not entities:
            continue

        entity_names = {
            "constructs": [c.get("name", "") for c in entities.get("constructs", [])],
            "measurements": [m.get("name", "") for m in entities.get("measurements", [])],
            "behaviors": [b.get("name", "") for b in entities.get("behaviors", [])],
        }
        entities_json_str = json.dumps(entity_names, indent=2, ensure_ascii=False)
        rel_prompt = EXTRACT_RELATIONSHIPS_PROMPT.format(entities_json=entities_json_str)
        user_content = f"{rel_prompt}\n\n---\nPaper text (extracted from PDF):\n\n{text}"

        for trial in range(n_trials):
            custom_id = json.dumps({"paper": name, "trial": trial, "phase": "relationships"})
            body = {
                "model": model,
                "messages": [
                    {"role": "system", "content": "Respond with valid JSON only. Extract relationships between the provided entities."},
                    {"role": "user", "content": user_content},
                ],
                tok_key: 16384,
            }
            if not reasoning:
                body["temperature"] = temperature
            line = {
                "custom_id": custom_id,
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": body,
            }
            lines.append(json.dumps(line, ensure_ascii=False))
    return lines


def run_sequential(client, jsonl_lines: list, description: str, max_workers: int = 5,
                   provider: str = "together", max_retries: int = 3,
                   base_delay: float = 2.0) -> list:
    """Run requests with rate limiting, retries, and failure tracking.

    Args:
        client: API client (Together, OpenAI, or Google-via-OpenAI).
        jsonl_lines: List of JSON-encoded request strings.
        description: Label for logging.
        max_workers: Max concurrent threads (capped to provider limit).
        provider: Provider name for rate limit lookup ("together", "google", "openai").
        max_retries: Number of attempts per request before giving up.
        base_delay: Base seconds for exponential backoff (delay = base * 2^attempt + jitter).
    """
    import concurrent.futures

    total = len(jsonl_lines)
    rpm, max_conc = PROVIDER_LIMITS.get(provider, (60, 4))
    max_workers = min(max_workers, max_conc)
    rate_limiter = _RateLimiter(max_rpm=rpm, max_concurrent=max_conc)
    failed: list[int] = []
    failed_lock = Lock()

    def _call_one(idx_line):
        idx, line_str = idx_line
        req = json.loads(line_str)
        custom_id = req["custom_id"]
        body = req["body"]

        last_exc = None
        for attempt in range(max_retries):
            rate_limiter.acquire()
            try:
                resp = client.chat.completions.create(**body)
                content = resp.choices[0].message.content if resp.choices else ""
                return {
                    "custom_id": custom_id,
                    "response": {
                        "body": {
                            "choices": [{"message": {"content": content}}]
                        }
                    },
                }
            except Exception as e:
                last_exc = e
                if _is_retryable(e) and attempt < max_retries - 1:
                    delay = min(base_delay * (2 ** attempt) + random.uniform(0, 1), 60.0)
                    logger.warning("Request %d/%d retry %d/%d (%s): %s (sleep %.1fs)",
                                   idx + 1, total, attempt + 1, max_retries - 1,
                                   custom_id[:40], e, delay)
                    time.sleep(delay)
                else:
                    break
            finally:
                rate_limiter.release()

        # All retries exhausted or non-retryable error
        logger.error("Request %d/%d FAILED after %d attempts (%s): %s",
                     idx + 1, total, max_retries, custom_id[:40], last_exc)
        with failed_lock:
            failed.append(idx)
        return {
            "custom_id": custom_id,
            "response": {"body": {"choices": [{"message": {"content": _FAILED_SENTINEL}}]}},
        }

    logger.info("Running %d requests (workers=%d, rpm=%d, provider=%s) for: %s",
                total, max_workers, rpm, provider, description)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        results = list(executor.map(_call_one, enumerate(jsonl_lines)))
    logger.info("Completed %d/%d requests (%d failed) for: %s",
                len(results), total, len(failed), description)
    return results


def submit_batch(client, jsonl_lines: list, description: str, provider: str = "together") -> str:
    """Write JSONL to temp file, upload, and create batch job. Returns job ID.

    Works with Together, OpenAI, and Google (via OpenAI-compat endpoint).
    """
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False, encoding="utf-8")
    for line in jsonl_lines:
        tmp.write(line + "\n")
    tmp.close()
    logger.info("Uploading %d requests from %s (%s, provider=%s)", len(jsonl_lines), tmp.name, description, provider)

    try:
        if provider == "together":
            file_resp = client.files.upload(file=Path(tmp.name), purpose="batch-api", check=False)
            file_id = file_resp.id
        else:
            # OpenAI and Google (via OpenAI-compat) use client.files.create
            with open(tmp.name, "rb") as f:
                file_resp = client.files.create(file=f, purpose="batch")
            file_id = file_resp.id
        logger.info("Uploaded file: %s", file_id)

        batch_resp = client.batches.create(
            input_file_id=file_id,
            endpoint="/v1/chat/completions",
            completion_window="24h",
        )
        # Together wraps in .job, OpenAI/Google don't
        job_id = getattr(getattr(batch_resp, 'job', None), 'id', None) or batch_resp.id
        logger.info("Batch job created: %s", job_id)
        if getattr(batch_resp, 'warning', None):
            logger.warning("Batch warning: %s", batch_resp.warning)
    finally:
        os.unlink(tmp.name)

    return job_id


def _retry_call(fn, *, op: str, max_retries: int = 6, initial_backoff: float = 5.0):
    """Invoke fn() with exponential backoff on transient network errors."""
    backoff = initial_backoff
    last_exc = None
    for attempt in range(max_retries):
        try:
            return fn()
        except Exception as e:  # noqa: BLE001
            last_exc = e
            msg = str(e).lower()
            # Retry on DNS/socket/transient network errors
            transient = any(k in msg for k in (
                "connection", "nodename", "timeout", "timed out",
                "temporarily unavailable", "broken pipe", "reset by peer",
                "resolving", "resolve", "dns", "ssl", "eof occurred",
            ))
            if not transient and attempt > 0:
                # Non-transient; give up after first try
                raise
            if attempt == max_retries - 1:
                raise
            logger.warning(
                "%s attempt %d/%d failed: %s; sleeping %.1fs and retrying",
                op, attempt + 1, max_retries, str(e)[:120], backoff,
            )
            time.sleep(backoff)
            backoff = min(backoff * 2, 120.0)
    raise last_exc  # type: ignore[misc]


def poll_batch(client, job_id: str, poll_interval: int = 15) -> list:
    """Poll until batch completes, then download and parse results.

    Works with Together, OpenAI, and Google (via OpenAI-compat endpoint).
    Transient network errors during polling/download are retried with backoff.
    """
    while True:
        status = _retry_call(
            lambda: client.batches.retrieve(job_id),
            op=f"batches.retrieve({job_id[:20]})",
        )
        st = status.status
        # Try to get progress info
        done = getattr(status, 'request_counts', None)
        if done:
            completed = getattr(done, 'completed', '?')
            total = getattr(done, 'total', '?')
            failed = getattr(done, 'failed', 0)
            logger.info("Batch %s: status=%s, completed=%s/%s (failed=%s)", job_id, st, completed, total, failed)
        else:
            logger.info("Batch %s: status=%s", job_id, st)

        st_lower = st.lower() if st else ""
        if st_lower == "completed":
            break
        elif st_lower in ("failed", "cancelled", "expired"):
            logger.error("Batch %s ended with status: %s", job_id, st)
            errors = getattr(status, 'errors', None)
            if errors:
                logger.error("Errors: %s", errors)
            return []

        time.sleep(poll_interval)

    output_file_id = status.output_file_id
    if not output_file_id:
        logger.error("No output file for batch %s", job_id)
        return []

    content = _retry_call(
        lambda: client.files.content(output_file_id),
        op=f"files.content({str(output_file_id)[:20]})",
    )
    # Handle different response types across providers
    if isinstance(content, bytes):
        text = content.decode('utf-8')
    elif hasattr(content, 'content') and isinstance(content.content, bytes):
        text = content.content.decode('utf-8')
    elif hasattr(content, 'text') and callable(content.text):
        text = content.text()
    elif hasattr(content, 'text'):
        text = content.text
    elif hasattr(content, 'read'):
        text = content.read().decode('utf-8')
    else:
        text = str(content)

    results = []
    for line in text.strip().split("\n"):
        if line.strip():
            results.append(json.loads(line))
    logger.info("Downloaded %d results from batch %s", len(results), job_id)
    return results


def submit_batch_google(jsonl_lines: list, description: str, model: str) -> str:
    """Submit batch via native google.genai SDK. Returns job name (not ID)."""
    from google import genai
    from google.genai import types

    api_key = os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not set")
    client = genai.Client(api_key=api_key)

    # Convert OpenAI-format JSONL lines to Gemini inline requests
    inline_requests = []
    custom_id_map = {}  # index -> custom_id for result mapping

    for idx, line_str in enumerate(jsonl_lines):
        req = json.loads(line_str)
        custom_id = req["custom_id"]
        body = req["body"]
        messages = body.get("messages", [])

        # Combine system + user messages into a single user prompt
        parts = []
        for msg in messages:
            parts.append(msg["content"])
        combined_text = "\n\n".join(parts)

        gen_config = {}
        if "temperature" in body:
            gen_config["temperature"] = body["temperature"]
        max_tok_key = "max_completion_tokens" if "max_completion_tokens" in body else "max_tokens"
        if max_tok_key in body:
            gen_config["max_output_tokens"] = body[max_tok_key]

        inline_req = {
            "key": custom_id,
            "request": {
                "contents": [{"parts": [{"text": combined_text}], "role": "user"}],
            },
        }
        if gen_config:
            inline_req["request"]["generation_config"] = gen_config

        inline_requests.append(inline_req)
        custom_id_map[idx] = custom_id

    logger.info("Submitting %d Google batch requests (%s, model=%s)", len(inline_requests), description, model)

    # Write to temp JSONL file and upload
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".jsonl", delete=False, encoding="utf-8")
    for req in inline_requests:
        tmp.write(json.dumps(req, ensure_ascii=False) + "\n")
    tmp.close()

    try:
        uploaded_file = client.files.upload(
            file=tmp.name,
            config=types.UploadFileConfig(display_name=description, mime_type="jsonl"),
        )
        logger.info("Uploaded file: %s", uploaded_file.name)

        batch_job = client.batches.create(
            model=model,
            src=uploaded_file.name,
            config={"display_name": description},
        )
        job_name = batch_job.name
        logger.info("Google batch job created: %s", job_name)
    finally:
        os.unlink(tmp.name)

    return job_name


def poll_batch_google(job_name: str, poll_interval: int = 30) -> list:
    """Poll Google batch job until complete, convert results to OpenAI-compat format.

    Transient network errors during polling/download are retried with backoff
    so a brief DNS/connection blip doesn't lose the batch results.
    """
    from google import genai

    api_key = os.environ.get("GOOGLE_API_KEY")
    client = genai.Client(api_key=api_key)

    while True:
        batch_job = _retry_call(
            lambda: client.batches.get(name=job_name),
            op=f"google.batches.get({job_name[:20]})",
        )
        state = batch_job.state.name if hasattr(batch_job.state, 'name') else str(batch_job.state)
        logger.info("Google batch %s: state=%s", job_name, state)

        if state == "JOB_STATE_SUCCEEDED":
            break
        elif state in ("JOB_STATE_FAILED", "JOB_STATE_CANCELLED"):
            logger.error("Google batch %s ended with state: %s", job_name, state)
            return []

        time.sleep(poll_interval)

    # Download and convert results to OpenAI-compat format
    results = []

    # Try inline responses first
    dest = batch_job.dest
    if hasattr(dest, 'inlined_responses') and dest.inlined_responses:
        for resp in dest.inlined_responses:
            key = getattr(resp, 'key', '') or ''
            if hasattr(resp, 'response') and resp.response:
                # Extract text from Gemini response
                text = ""
                if hasattr(resp.response, 'text'):
                    text = resp.response.text or ""
                elif hasattr(resp.response, 'candidates') and resp.response.candidates:
                    parts = resp.response.candidates[0].content.parts
                    text = parts[0].text if parts else ""
                results.append({
                    "custom_id": key,
                    "response": {"body": {"choices": [{"message": {"content": text}}]}},
                })
            elif hasattr(resp, 'error') and resp.error:
                logger.warning("Google batch result error for %s: %s", key, resp.error)
                results.append({
                    "custom_id": key,
                    "response": {"body": {"choices": [{"message": {"content": _FAILED_SENTINEL}}]}},
                })
    # Try file-based results
    elif hasattr(dest, 'file_name') and dest.file_name:
        file_content = _retry_call(
            lambda: client.files.download(file=dest.file_name),
            op=f"google.files.download({dest.file_name[:20]})",
        )
        if isinstance(file_content, bytes):
            text = file_content.decode('utf-8')
        else:
            text = str(file_content)
        for line in text.strip().split("\n"):
            if not line.strip():
                continue
            entry = json.loads(line)
            key = entry.get("key", "")
            response = entry.get("response", {})
            # Extract text from Gemini response format
            resp_text = ""
            if isinstance(response, dict):
                candidates = response.get("candidates", [])
                if candidates:
                    parts = candidates[0].get("content", {}).get("parts", [])
                    resp_text = parts[0].get("text", "") if parts else ""
            results.append({
                "custom_id": key,
                "response": {"body": {"choices": [{"message": {"content": resp_text}}]}},
            })

    logger.info("Downloaded %d results from Google batch %s", len(results), job_name)
    return results


def parse_batch_results(results: list) -> dict:
    """Parse batch results into {custom_id_dict: parsed_response} mapping."""
    parsed = {}
    for r in results:
        custom_id = r.get("custom_id", "")
        try:
            cid = json.loads(custom_id)
        except json.JSONDecodeError:
            cid = {"raw": custom_id}

        resp_body = r.get("response", {}).get("body", {})
        choices = resp_body.get("choices", [])
        if choices:
            content = choices[0].get("message", {}).get("content", "")
        else:
            content = ""

        # Skip failed requests so they don't count as empty trials
        if content == _FAILED_SENTINEL:
            logger.debug("Skipping failed result for %s", custom_id[:60])
            continue

        key = (cid.get("paper", ""), cid.get("trial", 0), cid.get("phase", ""))
        parsed[key] = parse_json_response(content)
    return parsed


def majority_vote_entities(trials_by_paper, n_trials, name_mapping, threshold=None):
    """Vote on entities per paper. Returns {paper_name: {constructs, measurements, behaviors}}.
    threshold=1 gives union; threshold=ceil(N/2) gives majority vote."""
    from collections import Counter

    if threshold is None:
        threshold = (n_trials // 2) + 1
    voted = {}

    for paper_name, trials in trials_by_paper.items():
        paper_result = {}
        for etype in ("constructs", "measurements", "behaviors"):
            canon_counts = Counter()
            canon_to_best = {}
            for trial_parsed in trials:
                nomnet = trial_parsed.get("Nomological Network") or {
                    k: trial_parsed.get(k, []) for k in ("constructs", "measurements", "behaviors")
                }
                entities = nomnet.get(etype, [])
                seen = set()
                for ent in entities:
                    # Defensive: an extractor occasionally returns a bare
                    # string (or other non-dict) instead of an entity object.
                    if isinstance(ent, str):
                        raw = ent.strip()
                    elif isinstance(ent, dict):
                        raw = (ent.get("name", "") or "").strip()
                    else:
                        continue
                    if not raw:
                        continue
                    canon = name_mapping.get(raw.lower(), raw.lower())
                    if canon in seen:
                        continue
                    seen.add(canon)
                    canon_counts[canon] += 1
                    if canon not in canon_to_best or len(json.dumps(ent)) > len(json.dumps(canon_to_best[canon])):
                        canon_to_best[canon] = ent

            kept = [canon_to_best[c] for c, cnt in canon_counts.items() if cnt >= threshold]
            paper_result[etype] = kept
            logger.debug("%s / %s: %d unique, %d voted (threshold=%d)",
                         paper_name[:40], etype, len(canon_counts), len(kept), threshold)

        voted[paper_name] = paper_result
        c, m, b = len(paper_result["constructs"]), len(paper_result["measurements"]), len(paper_result["behaviors"])
        logger.info("[%s] voted entities: C=%d M=%d B=%d", paper_name[:50], c, m, b)

    return voted


def majority_vote_relationships(trials_by_paper, n_trials, name_mapping, threshold=None):
    """Vote on relationships per paper. threshold=1 gives union."""
    from collections import Counter

    if threshold is None:
        threshold = (n_trials // 2) + 1
    voted = {}

    for paper_name, trials in trials_by_paper.items():
        key_counts = Counter()
        key_to_best = {}
        for trial_rels in trials:
            seen = set()
            for rel in trial_rels:
                src = name_mapping.get((rel.get("source", "") or "").strip().lower(),
                                       (rel.get("source", "") or "").strip().lower())
                tgt = name_mapping.get((rel.get("target", "") or "").strip().lower(),
                                       (rel.get("target", "") or "").strip().lower())
                rtype = (rel.get("type", "") or "").strip().lower()
                key = (src, tgt, rtype)
                if key in seen:
                    continue
                seen.add(key)
                key_counts[key] += 1
                if key not in key_to_best or len(str(rel.get("evidence", ""))) > len(str(key_to_best[key].get("evidence", ""))):
                    key_to_best[key] = rel

        kept = [key_to_best[k] for k, cnt in key_counts.items() if cnt >= threshold]
        voted[paper_name] = kept
        logger.info("[%s] voted relationships: %d", paper_name[:50], len(kept))

    return voted


def assemble_output(papers, paper_texts, voted_entities, voted_rels, entity_trials, rel_trials, args):
    """Build the final extraction JSON in the same format as main.py output."""
    results = {}
    for paper in papers:
        name = paper["name"]
        entities = voted_entities.get(name, {"constructs": [], "measurements": [], "behaviors": []})
        rels = voted_rels.get(name, [])

        nn = {
            "constructs": entities.get("constructs", []),
            "measurements": entities.get("measurements", []),
            "behaviors": entities.get("behaviors", []),
            "relationships": rels,
        }

        results[name] = {
            "provider": getattr(args, 'provider', 'together'),
            "model": args.model,
            "title": name,
            "result": {
                "raw_text": "",
                "parsed_text": {
                    "Nomological Network": nn,
                    "Title": name,
                },
            },
            "processed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "attempts": 1,
            "name": paper.get("name", ""),
            "url": paper.get("url", ""),
            "path": paper.get("path", ""),
            "is_LLM_paper": True,
        }

    return results


def main():
    parser = argparse.ArgumentParser(description="Batch extraction via Together AI (majority-vote or union)")
    parser.add_argument("--papers_url", required=True)
    parser.add_argument("--model", default="deepseek-ai/DeepSeek-V3.1")
    parser.add_argument("--temperature", type=float, default=0.6)
    parser.add_argument("--n_trials", type=int, default=3)
    parser.add_argument("--mode", choices=["majority_vote", "union"], default="majority_vote",
                        help="majority_vote: keep entities in >=ceil(N/2) trials; union: keep all")
    parser.add_argument("--sandbox", required=True, help="Output sandbox directory")
    parser.add_argument("--max_papers", type=int, default=0)
    parser.add_argument("--poll_interval", type=int, default=15)
    parser.add_argument("--sequential", action="store_true",
                        help="Use sequential API calls instead of batch API (for models that don't support batch)")
    parser.add_argument("--workers", type=int, default=5,
                        help="Max concurrent workers for sequential mode (default: 5)")
    parser.add_argument("--provider", default="together", choices=["together", "openai", "google"],
                        help="API provider (default: together)")
    args = parser.parse_args()

    vote_threshold = 1 if args.mode == "union" else None  # None → default majority
    logger.info("Mode: %s (vote threshold: %s)", args.mode,
                "1 (keep all)" if vote_threshold == 1 else f"ceil({args.n_trials}/2)")

    sandbox = Path(args.sandbox)
    sandbox.mkdir(parents=True, exist_ok=True)
    (sandbox / "inputs").mkdir(exist_ok=True)
    (sandbox / "trials").mkdir(exist_ok=True)

    # Load papers
    papers = load_papers(args.papers_url)
    if args.max_papers > 0:
        papers = papers[:args.max_papers]
    logger.info("Loaded %d papers", len(papers))

    # Load name mapping
    nm_path = ROOT / "outputs" / "combined_name_mapping.json"
    name_mapping = {}
    if nm_path.exists():
        raw = json.load(open(nm_path))
        name_mapping = {k.strip().lower(): v.strip().lower() for k, v in raw.items() if v.strip()}
        logger.info("Loaded %d name mappings", len(name_mapping))

    # Extract text from all PDFs
    logger.info("Extracting text from %d PDFs...", len(papers))
    paper_texts = {}
    for p in papers:
        pdf_path = p.get("path", "")
        text = extract_text(pdf_path) if pdf_path else ""
        paper_texts[p["name"]] = text
        if not text.strip():
            logger.warning("No text for: %s", p["name"][:60])

    if args.provider == "together":
        from together import Together
        client = Together(api_key=os.environ["TOGETHER_API_KEY"], timeout=600.0)
    elif args.provider == "openai":
        from openai import OpenAI
        client = OpenAI(api_key=os.environ["OPENAI_API_KEY"], timeout=600.0)
        args.sequential = True
    elif args.provider == "google":
        from openai import OpenAI
        client = OpenAI(
            api_key=os.environ["GOOGLE_API_KEY"],
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
            timeout=600.0,
        )
        args.sequential = True

    # ===== PHASE 1: Entity extraction batch =====
    logger.info("=== PHASE 1: Entity extraction (%d papers × %d trials) ===", len(papers), args.n_trials)
    entity_lines = build_entity_jsonl(papers, paper_texts, args.model, args.temperature, args.n_trials)
    logger.info("Built %d entity requests", len(entity_lines))

    if args.sequential:
        entity_results = run_sequential(client, entity_lines, "entity extraction",
                                       max_workers=args.workers, provider=args.provider)
    else:
        entity_job_id = submit_batch(client, entity_lines, "entity extraction")
        entity_results = poll_batch(client, entity_job_id, args.poll_interval)

    # Parse and group by paper
    entity_parsed = parse_batch_results(entity_results)
    entity_trials_by_paper = {}
    for (paper, trial, phase), parsed in entity_parsed.items():
        if phase != "entities":
            continue
        entity_trials_by_paper.setdefault(paper, []).append(parsed)

    # Save raw entity trials
    trials_path = sandbox / "trials" / "entity_trials.json"
    serializable = {p: [t for t in trials] for p, trials in entity_trials_by_paper.items()}
    with open(trials_path, "w") as f:
        json.dump(serializable, f, indent=2, ensure_ascii=False)
    logger.info("Saved entity trials to %s", trials_path)

    # Vote on entities (majority or union depending on mode)
    voted_entities = majority_vote_entities(entity_trials_by_paper, args.n_trials, name_mapping, threshold=vote_threshold)

    # ===== PHASE 2: Relationship extraction batch =====
    logger.info("=== PHASE 2: Relationship extraction ===")
    rel_lines = build_relationship_jsonl(papers, paper_texts, voted_entities, args.model, args.temperature, args.n_trials)
    logger.info("Built %d relationship requests", len(rel_lines))

    if not rel_lines:
        logger.warning("No relationship requests to submit (no voted entities?)")
        voted_rels = {}
        rel_trials_by_paper = {}
    else:
        if args.sequential:
            rel_results = run_sequential(client, rel_lines, "relationship extraction",
                                           max_workers=args.workers, provider=args.provider)
        else:
            rel_job_id = submit_batch(client, rel_lines, "relationship extraction")
            rel_results = poll_batch(client, rel_job_id, args.poll_interval)

        rel_parsed = parse_batch_results(rel_results)
        rel_trials_by_paper = {}
        for (paper, trial, phase), parsed in rel_parsed.items():
            if phase != "relationships":
                continue
            rels = parsed.get("relationships", [])
            rel_trials_by_paper.setdefault(paper, []).append(rels)

        # Save raw relationship trials
        rel_trials_path = sandbox / "trials" / "relationship_trials.json"
        with open(rel_trials_path, "w") as f:
            json.dump(rel_trials_by_paper, f, indent=2, ensure_ascii=False)
        logger.info("Saved relationship trials to %s", rel_trials_path)

        voted_rels = majority_vote_relationships(rel_trials_by_paper, args.n_trials, name_mapping, threshold=vote_threshold)

    # ===== Assemble and save =====
    output = assemble_output(papers, paper_texts, voted_entities, voted_rels,
                             entity_trials_by_paper, rel_trials_by_paper, args)

    mode_tag = "mv" if args.mode == "majority_vote" else "union"
    out_path = sandbox / "inputs" / f"extraction_{args.model.split('/')[-1]}_{mode_tag}{args.n_trials}.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    logger.info("Saved final extraction to %s", out_path)

    # Summary
    total_c = sum(len(v.get("constructs", [])) for v in voted_entities.values())
    total_m = sum(len(v.get("measurements", [])) for v in voted_entities.values())
    total_b = sum(len(v.get("behaviors", [])) for v in voted_entities.values())
    total_r = sum(len(v) for v in voted_rels.values())
    logger.info("=== DONE === C=%d M=%d B=%d R=%d across %d papers", total_c, total_m, total_b, total_r, len(papers))


if __name__ == "__main__":
    main()
