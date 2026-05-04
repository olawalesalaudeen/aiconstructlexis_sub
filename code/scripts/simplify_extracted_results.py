#!/usr/bin/env python3
"""Simplify extracted nomological network JSON to only essential fields.

Preserves the same parsed_text structure that extraction produces (including
"Nomological Network") so aggregators and export work unchanged. Prefers
result.parsed_text when it is already a dict; only re-parses raw_text when
parsed_text is missing or invalid.
"""

import argparse
import ast
import json
import sys
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parent.parent),
)
from misc.logging_config import setup_logging, get_logger, log_counts

setup_logging(run_name="simplify")
logger = get_logger(__name__)


def _strip_markdown_fences(text: str) -> str:
    """Remove ```json ... ``` wrapper if present."""
    s = text.strip()
    if s.startswith("```"):
        lines = s.split("\n")
        if lines[0].startswith("```"):
            lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        s = "\n".join(lines).strip()
    return s


def _parse_raw_fallback(raw_text):
    """Try to parse raw LLM output into a dict. Handles markdown fences."""
    if not raw_text or not isinstance(raw_text, str):
        return {}
    s = _strip_markdown_fences(raw_text)
    if not s:
        return {}
    if not (s.startswith("{") and s.endswith("}")):
        return {}
    try:
        return ast.literal_eval(s)
    except (ValueError, SyntaxError):
        pass
    try:
        return json.loads(s)
    except json.JSONDecodeError:
        try:
            return json.loads(s[:-1])
        except json.JSONDecodeError:
            return {}
    return {}


def simplify_extracted_results(
    input_file: Path, output_file: Path, keep_raw: bool = True
):
    """
    Simplify the extracted JSON to: name, url, path, parsed_text; optionally raw_text.

    - Uses result.parsed_text when it is already a non-empty dict (preserves extraction parsing).
    - Falls back to parsing result.raw_text only when parsed_text is missing or invalid.
    - Downstream expects parsed_text to contain "Nomological Network" with constructs, measurements, behaviors, relationships.
    """
    logger.info("Loading %s", input_file)
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    is_dict = isinstance(data, dict)
    simplified = {}
    skipped = 0

    for key, paper_data in data.items() if is_dict else enumerate(data):
        if not is_dict:
            key = paper_data.get("name", f"paper_{key}")

        result = paper_data.get("result", {})
        parsed_text = result.get("parsed_text")
        raw_text = result.get("raw_text", "")

        # Prefer already-parsed dict from extraction; only re-parse raw_text when needed
        if isinstance(parsed_text, str):
            parsed_text = _parse_raw_fallback(parsed_text) or _parse_raw_fallback(raw_text)
        elif (
            isinstance(parsed_text, dict)
            and parsed_text
            and "error" not in parsed_text
        ):
            pass  # use as-is
        elif isinstance(parsed_text, dict) and parsed_text:
            pass  # use as-is even if it has error key (downstream can skip)
        else:
            parsed_text = _parse_raw_fallback(raw_text)

        if not parsed_text or not isinstance(parsed_text, dict):
            skipped += 1
            continue

        entry = {
            "name": paper_data.get("name", key),
            "url": paper_data.get("url", ""),
            "path": paper_data.get("path", ""),
            "parsed_text": parsed_text,
        }
        if keep_raw and raw_text:
            entry["raw_text"] = raw_text
        simplified[key] = entry

    log_counts(logger, "Simplify results", processed=len(simplified), skipped=skipped)
    logger.info("Writing to %s", output_file)

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(simplified, f, indent=2, ensure_ascii=False)

    size_mb_in = input_file.stat().st_size / 1024 / 1024
    size_mb_out = output_file.stat().st_size / 1024 / 1024
    logger.info(
        "Saved %s  (%.1fMB -> %.1fMB)",
        output_file, size_mb_in, size_mb_out,
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simplify extracted nomological network JSON."
    )
    parser.add_argument(
        "--input",
        "-i",
        required=True,
        help="Input JSON file (extraction output)",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Output JSON file (default: input stem + _simplified.json)",
    )
    parser.add_argument(
        "--no-raw",
        action="store_true",
        help="Omit raw_text in output to reduce file size",
    )
    args = parser.parse_args()

    input_file = Path(args.input)
    if not input_file.exists():
        logger.error("Input file %s does not exist", input_file)
        exit(1)

    output_file = (
        Path(args.output)
        if args.output
        else input_file.with_name(input_file.stem + "_simplified.json")
    )
    simplify_extracted_results(
        input_file, output_file, keep_raw=not args.no_raw
    )
