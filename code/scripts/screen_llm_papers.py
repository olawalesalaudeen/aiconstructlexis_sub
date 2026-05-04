"""
Screen papers for LLM relevance using Gemini 2.5 Flash (batch inference).

Reads a paper list JSON, extracts text from each PDF, sends the screening
prompt to Gemini via the OpenAI-compatible endpoint, and writes back the
JSON with an `is_LLM_paper` boolean flag.

Skips papers that already have `is_LLM_paper` set (for restartability).

Usage:
    python scripts/screen_llm_papers.py \
        --input  data/neurips_2025_papers.json \
        --output data/neurips_2025_papers.json \
        --model  gemini-2.5-flash \
        --max-workers 8
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from threading import Lock

from tqdm.auto import tqdm

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from misc.logging_config import setup_logging, get_logger, log_step, log_counts
from misc.prompts import SCREENING_PAPERS_PROMPT

setup_logging(run_name="screen_papers")
logger = get_logger(__name__)

# Main-text page limits per conference (excludes references & appendix).
# These are the max pages for the main body as defined by each venue's
# submission guidelines.  We add +1 as a buffer for formatting variation.
CONFERENCE_PAGE_LIMITS: dict[str, int] = {
    "neurips": 10,   # 9 content pages + ~1 for title/abstract overflow
    "iclr":    11,   # 10 content pages + 1 buffer
    "icml":    10,   # 9 content pages + 1 buffer
}
DEFAULT_PAGE_LIMIT = 12


def _detect_conference(input_path: str) -> str:
    """Infer conference name from the input file path."""
    p = input_path.lower()
    for conf in CONFERENCE_PAGE_LIMITS:
        if conf in p:
            return conf
    return ""


def _make_client(provider: str):
    """Create an OpenAI-compatible client for the given provider."""
    from openai import OpenAI
    if provider == "google":
        api_key = (
            os.environ.get("GOOGLE_API_KEY")
            or os.environ.get("GEMINI_API_KEY")
        )
        if not api_key:
            raise EnvironmentError(
                "Set GOOGLE_API_KEY or GEMINI_API_KEY"
            )
        return OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
        )
    elif provider == "together":
        api_key = os.environ.get("TOGETHER_API_KEY")
        if not api_key:
            raise EnvironmentError("Set TOGETHER_API_KEY")
        return OpenAI(
            api_key=api_key,
            base_url="https://api.together.xyz/v1",
        )
    elif provider == "openai":
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise EnvironmentError("Set OPENAI_API_KEY")
        return OpenAI(api_key=api_key)
    else:
        raise ValueError(f"Unknown provider: {provider}")


def _extract_main_text(pdf_path: str, max_pages: int) -> str:
    """Extract only the main body text from a PDF.

    Strategy:
      1. Extract text from only the first *max_pages* pages (the main
         paper body per conference guidelines, before appendices).
      2. Within those pages, cut at the "References" section if found.
    This avoids sending appendix / supplementary material to the LLM.
    """
    if not Path(pdf_path).exists():
        return ""

    try:
        from pdfminer.high_level import extract_text
        page_nums = list(range(max_pages))
        text = extract_text(pdf_path, page_numbers=page_nums) or ""
    except Exception:
        try:
            import pymupdf
            doc = pymupdf.open(str(pdf_path))
            pages = [doc[i].get_text() for i in range(min(max_pages, len(doc)))]
            doc.close()
            text = "\n".join(pages)
        except Exception as e:
            logger.debug("PDF extraction failed for %s: %s", pdf_path, e)
            return ""

    return _cut_at_references(text)


def _cut_at_references(text: str) -> str:
    """Truncate text at the 'References' section heading."""
    import re
    # Match common reference section headings on their own line
    match = re.search(
        r'\n\s*(References|REFERENCES|Bibliography)\s*\n',
        text,
    )
    if match:
        text = text[:match.start()]
    return text


def _screen_one(client, paper: dict, model: str,
                rate_timestamps: list, rate_lock: Lock,
                max_rpm: int, max_pages: int = 12) -> dict:
    """Call the LLM to classify one paper. Returns updated paper dict."""
    text = _extract_main_text(paper["path"], max_pages)
    if not text.strip():
        paper["is_LLM_paper"] = False
        paper["screen_note"] = "empty_pdf"
        return paper

    # Sliding-window rate limiting
    sleep_time = 0.0
    with rate_lock:
        now = time.time()
        rate_timestamps[:] = [t for t in rate_timestamps if now - t < 60]
        if len(rate_timestamps) >= max_rpm:
            sleep_time = 60.0 - (now - rate_timestamps[0]) + 0.1
    if sleep_time > 0:
        time.sleep(sleep_time)
    with rate_lock:
        rate_timestamps.append(time.time())

    user_content = SCREENING_PAPERS_PROMPT + text

    max_retries = 3
    for attempt in range(max_retries):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": user_content}],
                # Generous token budget: gpt-oss-style reasoning models emit
                # internal thinking tokens before the final answer. With a
                # tiny budget (e.g. 8) the visible content comes back empty.
                max_tokens=512,
                temperature=0,
            )
            content = resp.choices[0].message.content or ""
            # Strip <think>...</think> blocks that some reasoning models emit
            import re as _re
            content = _re.sub(r"<think>.*?</think>", "", content, flags=_re.DOTALL).strip()
            answer = content.strip().lower()
            paper["is_LLM_paper"] = answer.startswith("yes")
            return paper
        except Exception as e:
            status = getattr(e, "status_code", None)
            retryable = status in (429, 500, 502, 503, 529) or type(e).__name__ in (
                "APITimeoutError", "APIConnectionError", "Timeout", "ConnectionError"
            )
            if retryable and attempt < max_retries - 1:
                delay = min(2.0 * (2 ** attempt) + random.uniform(0, 1), 60.0)
                logger.warning(
                    "Retry %d/%d for %s: %s (sleep %.1fs)",
                    attempt + 1, max_retries - 1,
                    paper["name"][:50], e, delay,
                )
                time.sleep(delay)
            else:
                logger.error("FAILED %s: %s", paper["name"][:60], e)
                paper["is_LLM_paper"] = False
                paper["screen_error"] = str(e)
                return paper

    return paper


def main():
    parser = argparse.ArgumentParser(description="Screen papers for LLM relevance")
    parser.add_argument("--input", required=True, help="Paper list JSON")
    parser.add_argument("--output", required=True, help="Output JSON (can be same as input)")
    parser.add_argument("--provider", default="together",
                        choices=["together", "google", "openai"],
                        help="API provider")
    parser.add_argument("--model", default="openai/gpt-oss-120b",
                        help="Model name")
    parser.add_argument("--max-workers", type=int, default=8)
    parser.add_argument("--max-rpm", type=int, default=3600,
                        help="Max requests per minute")
    parser.add_argument("--save-every", type=int, default=50,
                        help="Checkpoint frequency")
    parser.add_argument(
        "--conference", default="auto",
        help="Conference name (neurips/iclr/icml) for page limits. "
             "'auto' infers from input path.",
    )
    args = parser.parse_args()

    with open(args.input) as f:
        papers = json.load(f)
    logger.info("Loaded %d papers from %s", len(papers), args.input)

    conf = (
        args.conference if args.conference != "auto"
        else _detect_conference(args.input)
    )
    max_pages = CONFERENCE_PAGE_LIMITS.get(conf, DEFAULT_PAGE_LIMIT)
    logger.info(
        "Conference: %s — extracting first %d pages per paper",
        conf or "unknown", max_pages,
    )

    already = [p for p in papers if "is_LLM_paper" in p and "screen_error" not in p]
    todo = [p for p in papers if "is_LLM_paper" not in p or "screen_error" in p]
    logger.info("Already screened: %d, remaining: %d", len(already), len(todo))

    if not todo:
        llm_count = sum(1 for p in papers if p.get("is_LLM_paper"))
        logger.info("All done. %d/%d are LLM papers.", llm_count, len(papers))
        return

    client = _make_client(args.provider)
    rate_timestamps: list[float] = []
    rate_lock = Lock()
    results_lock = Lock()
    completed = list(already)
    output_path = Path(args.output)

    def _save_checkpoint():
        with results_lock:
            all_papers = completed + [p for p in todo if "is_LLM_paper" not in p]
        output_path.write_text(
            json.dumps(all_papers, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )

    with log_step(logger, "screening", total=len(todo), model=args.model):
        with ThreadPoolExecutor(max_workers=args.max_workers) as pool:
            futures = {
                pool.submit(
                    _screen_one, client, p, args.model,
                    rate_timestamps, rate_lock, args.max_rpm,
                    max_pages,
                ): p
                for p in todo
            }
            done_count = 0
            for fut in tqdm(as_completed(futures), total=len(futures),
                            unit="paper", desc="Screening"):
                result = fut.result()
                with results_lock:
                    completed.append(result)
                done_count += 1
                if done_count % args.save_every == 0:
                    _save_checkpoint()
                    logger.info(
                        "Checkpoint: %d/%d done", done_count, len(todo),
                    )

    # Final save — rebuild in original order
    screened_map = {p["name"]: p for p in completed}
    final = [screened_map.get(p["name"], p) for p in papers]
    output_path.write_text(
        json.dumps(final, indent=2, ensure_ascii=False), encoding="utf-8",
    )

    llm_count = sum(1 for p in final if p.get("is_LLM_paper"))
    errors = sum(1 for p in final if "screen_error" in p)
    log_counts(
        logger, "screening_results",
        total=len(final), llm_papers=llm_count, non_llm=len(final) - llm_count,
        errors=errors,
    )
    logger.info("Output written to %s", output_path)


if __name__ == "__main__":
    main()
