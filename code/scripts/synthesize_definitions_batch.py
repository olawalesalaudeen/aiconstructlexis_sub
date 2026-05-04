"""
Synthesize entity characterizations using the Gemini Batch Inference API.

This is the batch-API equivalent of synthesize_definitions.py:
  - 1 entity per LLM request (full attention per entity)
  - All 6500-9000 entity requests submitted as a single batch job
  - Polled until complete, results parsed back into the network

Why batch API instead of synchronous parallel calls?
  - ~50% cost discount versus on-demand pricing
  - No rate-limit / quota concerns at this scale
  - Single submission/polling cycle keeps the orchestration simple

Production parameters (used for joint_v7 characterization):
    --model gemini-2.5-pro
    --min-papers 3            (entities with <3 papers get a deterministic fallback)
    --description characterize-<venue-or-joint-label>

Usage:
    python scripts/synthesize_definitions_batch.py \\
        --input  network_data/joint_neurips24_iclr25/joint_network_merged.json \\
        --output network_data/joint_neurips24_iclr25/joint_network_characterized.json \\
        --model  gemini-2.5-pro \\
        --min-papers 3 \\
        --description characterize-joint
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from misc import prompts  # noqa: E402
from misc.logging_config import setup_logging, get_logger  # noqa: E402
from scripts.batch_majority_vote import (  # noqa: E402
    submit_batch_google,
    poll_batch_google,
    _FAILED_SENTINEL,
)

setup_logging(run_name="characterize_batch")
logger = get_logger(__name__)


# ── Per-entity context builder (matches synthesize_definitions.py) ───────────

def _build_entity_context(
    entity: Dict[str, Any],
    entity_type: str,
    relationships: List[Dict[str, Any]],
) -> Dict[str, Any]:
    """Full per-entity context for the LLM. No truncation: all definitions,
    snippets, and relationships involving this entity are included."""
    name = entity["canonical_name"]

    definitions = []
    for orig_name, node in (entity.get("original_nodes") or {}).items():
        defn = (node.get("definition") or "").strip()
        papers = node.get("papers", []) or []
        if defn:
            definitions.append({
                "original_name": orig_name,
                "definition": defn,
                "papers": papers,
            })

    snippets = entity.get("source_snippets_evidence") or []

    rels = []
    for r in relationships:
        src = r.get("source") or r.get("canonical_source")
        tgt = r.get("target") or r.get("canonical_target")
        if src == name or tgt == name:
            evidence = r.get("evidence") or []
            if not evidence:
                evidence = [
                    ri.get("evidence", "")
                    for ri in (r.get("raw_instances") or [])
                    if ri.get("evidence")
                ]
            rels.append({
                "source": src,
                "target": tgt,
                "type": r.get("type", ""),
                "evidence": evidence,
                "papers": r.get("papers") or [],
            })

    return {
        "canonical_name": name,
        "type": entity_type,
        "definitions": definitions,
        "source_snippets": snippets,
        "relationships": rels,
    }


# ── Build batch JSONL ────────────────────────────────────────────────────────

SYSTEM_PROMPT = (
    "You are a research assistant specializing in academic knowledge synthesis. "
    "Always respond with valid JSON only."
)


def build_jsonl_lines(network: Dict[str, Any], min_papers: int = 1,
                      skip_characterized: bool = True) -> List[str]:
    """Build OpenAI-batch-format JSONL lines, one per entity that needs an LLM call."""
    relationships = network.get("relationships") or []
    lines: List[str] = []
    skipped_fallback = 0
    skipped_existing = 0

    for etype in ("constructs", "measurements", "behaviors"):
        for idx, entity in enumerate(network.get(etype) or []):
            # Skip entities that already have a non-empty characterization (resume)
            if skip_characterized and (entity.get("characterization") or "").strip():
                skipped_existing += 1
                continue
            # Single-paper or below-threshold entities use deterministic fallback
            if entity.get("paper_count", 0) < min_papers:
                fb = ""
                for orig_name, node in (entity.get("original_nodes") or {}).items():
                    d = (node.get("definition") or "").strip()
                    if d:
                        fb = d
                        break
                if not fb:
                    fb = entity.get("canonical_definition", "") or ""
                # Stamp fallback directly onto the entity in the network in
                # memory so we don't need to LLM-call it.
                entity["characterization"] = fb
                skipped_fallback += 1
                continue

            ctx = _build_entity_context(entity, etype, relationships)
            ctx_json = json.dumps([ctx], indent=2)  # prompt expects array-shaped JSON
            user_prompt = prompts.CHARACTERIZE_ENTITIES_PROMPT.format(entities_json=ctx_json)

            custom_id = json.dumps({"etype": etype, "idx": idx,
                                    "name": entity.get("canonical_name", "")})

            req = {
                "custom_id": custom_id,
                "body": {
                    "messages": [
                        {"role": "system", "content": SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt},
                    ],
                    "temperature": 0,
                    "max_tokens": 32768,
                },
            }
            lines.append(json.dumps(req, ensure_ascii=False))

    logger.info(
        "Built %d batch requests; %d used fallback; %d skipped (already characterized)",
        len(lines), skipped_fallback, skipped_existing,
    )
    return lines


# ── Result parsing ───────────────────────────────────────────────────────────

def _extract_text(result: Dict[str, Any]) -> str:
    body = (result.get("response") or {}).get("body", {}) or {}
    choices = body.get("choices") or []
    if not choices:
        return ""
    return choices[0].get("message", {}).get("content", "") or ""


def _parse_json_loose(text: str) -> Any:
    """Strip code fences / think tags, parse JSON; fall back to repair_json."""
    if not text:
        return None
    text = text.strip()
    fence = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
    if fence:
        text = fence.group(1).strip()
    text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        try:
            from json_repair import repair_json
            repaired = repair_json(text, return_objects=True)
            if isinstance(repaired, (dict, list, str)):
                return repaired
        except Exception:
            pass
    return None


def attach_results(network: Dict[str, Any], results: List[Dict[str, Any]]) -> Dict[str, int]:
    """For each batch result, find the matching entity by (etype, idx) and stamp
    the characterization. Returns counts of {ok, parse_failed, missing_target}."""
    stats = {"ok": 0, "parse_failed": 0, "missing_target": 0, "failed_request": 0}

    for r in results:
        custom_id = r.get("custom_id", "")
        try:
            cid = json.loads(custom_id)
        except json.JSONDecodeError:
            cid = {}
        etype = cid.get("etype")
        idx = cid.get("idx")
        canonical_name = cid.get("name", "")
        if etype not in ("constructs", "measurements", "behaviors") or not isinstance(idx, int):
            stats["missing_target"] += 1
            continue

        text = _extract_text(r)
        if text == _FAILED_SENTINEL or not text:
            stats["failed_request"] += 1
            continue

        parsed = _parse_json_loose(text)
        char_text = ""
        if isinstance(parsed, dict):
            # The prompt asks for a single-key {Canonical Name: text} object.
            # Tolerate case differences and accept a "characterization" key fallback.
            if canonical_name and canonical_name in parsed:
                char_text = parsed[canonical_name]
            else:
                # Look for case-insensitive match
                for k, v in parsed.items():
                    if isinstance(v, str) and (k.lower() == canonical_name.lower()
                                              or k.lower() == "characterization"):
                        char_text = v
                        break
                # If there's exactly one string value, take it
                if not char_text:
                    string_values = [v for v in parsed.values() if isinstance(v, str)]
                    if len(string_values) == 1:
                        char_text = string_values[0]
        elif isinstance(parsed, str):
            char_text = parsed

        if not char_text:
            stats["parse_failed"] += 1
            continue

        # Stamp onto the entity
        entities = network.get(etype) or []
        if 0 <= idx < len(entities) and entities[idx].get("canonical_name", "") == canonical_name:
            entities[idx]["characterization"] = char_text
            stats["ok"] += 1
        else:
            stats["missing_target"] += 1

    return stats


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", required=True)
    p.add_argument("--model", default="gemini-2.5-pro",
                   help="LLM model id (production: gemini-2.5-pro)")
    # Production used --min-papers 3 for the joint characterization run.
    p.add_argument("--min-papers", type=int, default=3,
                   help="Entities with paper_count<min get a deterministic fallback (skip LLM). "
                        "Production: 3.")
    p.add_argument("--description", default="characterize-batch",
                   help="Display label for the batch job (e.g. characterize-<venue>)")
    p.add_argument("--resume-job", default=None,
                   help="If supplied, skip submission and poll this existing job name instead")
    p.add_argument("--poll-interval", type=int, default=30,
                   help="Seconds between batch status polls")
    args = p.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    with open(in_path) as f:
        network = json.load(f)
    logger.info("Loaded %s", in_path)
    for et in ("constructs", "measurements", "behaviors"):
        logger.info("  %s: %d", et, len(network.get(et) or []))

    # Build batch lines (this also stamps fallbacks for low-paper entities)
    if args.resume_job:
        logger.info("Resuming existing batch job: %s", args.resume_job)
        results = poll_batch_google(args.resume_job, poll_interval=args.poll_interval)
    else:
        lines = build_jsonl_lines(network, min_papers=args.min_papers)
        if not lines:
            logger.info("Nothing to send to LLM; only fallbacks were applied.")
        else:
            job_name = submit_batch_google(lines, args.description, args.model)
            logger.info("Batch job submitted: %s", job_name)
            # Persist job name in case we need to resume
            job_log = out_path.with_suffix(".batch_job.txt")
            job_log.write_text(job_name)
            logger.info("Wrote job name to %s (use --resume-job to recover)", job_log)
            t0 = time.time()
            results = poll_batch_google(job_name, poll_interval=args.poll_interval)
            logger.info("Batch finished in %.1f min; %d results", (time.time() - t0)/60, len(results))

    # Attach to network
    if not args.resume_job and 'lines' in locals() and not lines:
        results = []
    stats = attach_results(network, results)
    logger.info("Result attach: %s", stats)

    # Final coverage stats
    total_entities = sum(len(network.get(et) or []) for et in ("constructs", "measurements", "behaviors"))
    characterized = sum(
        1 for et in ("constructs", "measurements", "behaviors")
        for e in (network.get(et) or [])
        if e.get("characterization")
    )
    logger.info("Characterized %d / %d (%.1f%%)",
                characterized, total_entities, 100*characterized/max(1, total_entities))

    with open(out_path, "w") as f:
        json.dump(network, f, indent=2)
    logger.info("Wrote %s", out_path)


if __name__ == "__main__":
    main()
