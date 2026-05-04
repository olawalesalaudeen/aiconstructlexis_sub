"""
Screen papers for LLM relevance using Together AI Batch Inference.

Steps:
  1. Extract text from PDFs in parallel (pymupdf + multiprocessing)
  2. Build a JSONL file with one chat-completion request per paper
  3. Upload to Together, create a batch job
  4. Poll until completion
  5. Download results and merge back into the paper list JSON

Usage:
    python scripts/batch_screen_papers.py \
        --input  data/iclr_2025_papers.json \
        --output data/iclr_2025_papers.json \
        --model  openai/gpt-oss-120b
"""
from __future__ import annotations

import argparse
import json
import multiprocessing as mp
import os
import re
import sys
import time
from pathlib import Path

from tqdm.auto import tqdm

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from misc.logging_config import setup_logging, get_logger
from misc.prompts import SCREENING_PAPERS_PROMPT

setup_logging(run_name="batch_screen_papers")
logger = get_logger(__name__)

CONFERENCE_PAGE_LIMITS: dict[str, int] = {
    "neurips": 10,
    "iclr": 11,
    "icml": 10,
    "acl": 10,
    "emnlp": 10,
    "naacl": 10,
}
DEFAULT_PAGE_LIMIT = 12


def _detect_conference(input_path: str) -> str:
    p = input_path.lower()
    for conf in CONFERENCE_PAGE_LIMITS:
        if conf in p:
            return conf
    return ""


def _extract_one(args: tuple[int, str, int]) -> tuple[int, str]:
    """Extract main body text from a single PDF. Runs in worker process."""
    idx, pdf_path, max_pages = args
    if not Path(pdf_path).exists():
        return idx, ""
    try:
        import pymupdf
        doc = pymupdf.open(pdf_path)
        n = min(max_pages, len(doc))
        text = "\n".join(doc[i].get_text() for i in range(n))
        doc.close()
    except Exception:
        return idx, ""

    m = re.search(r'\n\s*(References|REFERENCES|Bibliography)\s*\n', text)
    if m:
        text = text[:m.start()]
    return idx, text


def main():
    parser = argparse.ArgumentParser(description="Batch screen papers for LLM relevance")
    parser.add_argument("--input", required=True, help="Paper list JSON")
    parser.add_argument("--output", required=True, help="Output JSON")
    parser.add_argument("--model", default="openai/gpt-oss-120b")
    parser.add_argument("--conference", default="auto")
    parser.add_argument("--poll-interval", type=int, default=60, help="Seconds between polls")
    parser.add_argument("--workers", type=int, default=0,
                        help="Extraction workers (0=all CPUs)")
    args = parser.parse_args()

    from together import Together
    client = Together(api_key=os.environ.get("TOGETHER_API_KEY"))

    with open(args.input) as f:
        papers = json.load(f)
    logger.info("Loaded %d papers from %s", len(papers), args.input)

    conf = args.conference if args.conference != "auto" else _detect_conference(args.input)
    max_pages = CONFERENCE_PAGE_LIMITS.get(conf, DEFAULT_PAGE_LIMIT)
    logger.info("Conference: %s — extracting first %d pages per paper", conf or "unknown", max_pages)

    todo_indices = [i for i, p in enumerate(papers)
                    if "is_LLM_paper" not in p or "screen_error" in p]
    already = len(papers) - len(todo_indices)
    logger.info("Already screened: %d, remaining: %d", already, len(todo_indices))

    if not todo_indices:
        llm_count = sum(1 for p in papers if p.get("is_LLM_paper"))
        logger.info("All done. %d/%d are LLM papers.", llm_count, len(papers))
        return

    # Step 1: Parallel text extraction with pymupdf
    n_workers = args.workers or mp.cpu_count()
    logger.info("Extracting text with %d workers (pymupdf)...", n_workers)

    extract_args = [(i, papers[i]["path"], max_pages) for i in todo_indices]

    texts: dict[int, str] = {}
    with mp.Pool(n_workers) as pool:
        for idx, text in tqdm(
            pool.imap_unordered(_extract_one, extract_args, chunksize=32),
            total=len(extract_args),
            desc="Extracting text",
            unit="paper",
        ):
            texts[idx] = text

    # Step 2: Build JSONL
    jsonl_path = Path(args.output).with_suffix(".batch_requests.jsonl")
    logger.info("Building JSONL at %s", jsonl_path)

    id_map: dict[str, int] = {}
    empty_count = 0

    with open(jsonl_path, "w") as f:
        for i in todo_indices:
            text = texts.get(i, "")
            if not text.strip():
                papers[i]["is_LLM_paper"] = False
                papers[i]["screen_note"] = "empty_pdf"
                empty_count += 1
                continue

            custom_id = f"paper_{i}"
            id_map[custom_id] = i

            request = {
                "custom_id": custom_id,
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": {
                    "model": args.model,
                    "messages": [
                        {"role": "user", "content": SCREENING_PAPERS_PROMPT + text}
                    ],
                    "max_tokens": 512,
                    "temperature": 0,
                },
            }
            f.write(json.dumps(request) + "\n")

    logger.info("Built %d requests (%d empty PDFs skipped)", len(id_map), empty_count)

    if not id_map:
        logger.info("No papers to screen. Writing output.")
        Path(args.output).write_text(json.dumps(papers, indent=2, ensure_ascii=False))
        return

    # Step 3: Split JSONL if > 95 MB (Together limit is 100 MB)
    size_mb = jsonl_path.stat().st_size / 1e6
    if size_mb > 95:
        all_lines = jsonl_path.read_text().strip().split("\n")
        mid = len(all_lines) // 2
        part1 = jsonl_path.with_suffix(".part1.jsonl")
        part2 = jsonl_path.with_suffix(".part2.jsonl")
        part1.write_text("\n".join(all_lines[:mid]) + "\n")
        part2.write_text("\n".join(all_lines[mid:]) + "\n")
        jsonl_parts = [part1, part2]
        logger.info("Split %.1fMB JSONL into 2 parts (%d + %d lines)", size_mb, mid, len(all_lines) - mid)
    else:
        jsonl_parts = [jsonl_path]

    # Step 4: Upload & create batch jobs for each part
    batch_ids = []
    for part_path in jsonl_parts:
        logger.info("Uploading %s (%.1fMB)...", part_path.name, part_path.stat().st_size / 1e6)
        file_resp = client.files.upload(file=str(part_path), purpose="batch-api", check=False)
        file_id = file_resp.id
        logger.info("Uploaded file: %s", file_id)

        batch = client.batches.create(
            input_file_id=file_id,
            endpoint="/v1/chat/completions",
            model_id=args.model,
        )
        bid = batch.job.id if hasattr(batch, 'job') else batch.id
        batch_ids.append(bid)
        logger.info("Batch job created: %s", bid)

    # Step 5: Poll all batch jobs until completion
    logger.info("Polling %d batch job(s) (interval=%ds)...", len(batch_ids), args.poll_interval)
    completed_statuses = {}
    while len(completed_statuses) < len(batch_ids):
        for bid in batch_ids:
            if bid in completed_statuses:
                continue
            status = client.batches.retrieve(bid)
            state = status.status
            progress = getattr(status, "progress", None) or 0
            logger.info("Batch %s: status=%s progress=%.1f%%", bid, state, progress)

            if state in ("COMPLETED", "completed"):
                completed_statuses[bid] = status
            elif state.upper() in ("FAILED", "EXPIRED", "CANCELLED"):
                error = getattr(status, "error", "unknown")
                logger.error("Batch job %s %s: %s", bid, state, error)
                sys.exit(1)

        if len(completed_statuses) < len(batch_ids):
            time.sleep(args.poll_interval)

    # Step 6: Download and parse results from all batch jobs
    all_result_text = []
    for bid in batch_ids:
        output_file_id = completed_statuses[bid].output_file_id
        logger.info("Downloading results from %s (batch %s)...", output_file_id, bid)
        result_resp = client.files.content(output_file_id)
        result_text = result_resp.text if hasattr(result_resp, 'text') else result_resp.read().decode()
        all_result_text.append(result_text)

    combined_result = "\n".join(all_result_text)
    results_path = Path(args.output).with_suffix(".batch_results.jsonl")
    results_path.write_text(combined_result)
    logger.info("Results saved to %s", results_path)
    result_text = combined_result

    successes = 0
    errors = 0
    for line in result_text.strip().split("\n"):
        if not line.strip():
            continue
        result = json.loads(line)
        custom_id = result["custom_id"]
        idx = id_map.get(custom_id)
        if idx is None:
            continue

        if result.get("error"):
            papers[idx]["is_LLM_paper"] = False
            papers[idx]["screen_error"] = str(result["error"])
            errors += 1
        else:
            body = result.get("response", {}).get("body", {})
            choices = body.get("choices", [])
            if choices:
                answer = (choices[0].get("message", {}).get("content", "") or "").strip().lower()
                papers[idx]["is_LLM_paper"] = answer.startswith("yes")
                successes += 1
            else:
                papers[idx]["is_LLM_paper"] = False
                papers[idx]["screen_error"] = "no_choices"
                errors += 1

    logger.info("Parsed results: %d successes, %d errors", successes, errors)

    llm_count = sum(1 for p in papers if p.get("is_LLM_paper"))
    Path(args.output).write_text(json.dumps(papers, indent=2, ensure_ascii=False))
    logger.info("Output: %d/%d LLM papers. Written to %s", llm_count, len(papers), args.output)


if __name__ == "__main__":
    main()
