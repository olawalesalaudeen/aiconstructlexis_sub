"""
LLM cross-conference merge pass for the joint nomological network.

Takes the joint network (built by build_joint_network.py) and runs the
existing MERGE_GROUPS_PROMPT on each entity type to catch SEMANTIC
duplicates that have different surface forms across conferences (e.g.
NeurIPS "Factuality" and ICLR "Factuality and faithfulness"). Smart-batches
related items together so the LLM sees the full family at once.

Joint metadata (papers_by_conference, characterizations, original_nodes) is
unioned across merged groups.

Usage:
    python scripts/joint_llm_merge.py \
        --input  network_data/joint_neurips24_iclr25/joint_network.json \
        --output network_data/joint_neurips24_iclr25/joint_network_merged.json \
        --provider google --model gemini-2.5-pro --batch-size 500
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from misc import prompts  # noqa: E402
from scripts.cluster_for_batching import make_batches  # noqa: E402
from scripts.llm_aggregator import call_llm_for_aggregation  # noqa: E402


def _slim(g: Dict[str, Any]) -> Dict[str, Any]:
    out = {"canonical_name": g.get("canonical_name", "")}
    onames = g.get("original_names") or []
    if onames:
        out["original_names"] = onames
    cd = (g.get("canonical_definition") or "").strip()
    if cd:
        out["canonical_definition"] = cd
    return out


def _decode_id_groups(result: Any, groups: List[Dict[str, Any]]) -> Dict[int, str]:
    """Return id -> canonical_name mapping from MERGE_GROUPS_PROMPT response."""
    if not isinstance(result, dict):
        return {}
    grp_dict = result.get("groups")
    if not isinstance(grp_dict, dict):
        return {}
    out: Dict[int, str] = {}
    seen: set = set()
    for canon, ids in grp_dict.items():
        if not isinstance(ids, list):
            continue
        for raw in ids:
            try:
                idx = int(raw)
            except (ValueError, TypeError):
                continue
            if 0 <= idx < len(groups) and idx not in seen:
                out[idx] = canon
                seen.add(idx)
    # ungrouped — keep original canonical_name
    for raw in (result.get("ungrouped") or []):
        try:
            idx = int(raw)
        except (ValueError, TypeError):
            continue
        if 0 <= idx < len(groups) and idx not in seen:
            out[idx] = groups[idx].get("canonical_name", "")
            seen.add(idx)
    # missing IDs default to their own name (treated as singleton group)
    for i in range(len(groups)):
        if i not in seen:
            out[i] = groups[i].get("canonical_name", "")
    return out


def _merge_groups_joint(winner: Dict[str, Any], loser: Dict[str, Any]) -> None:
    """Merge joint-network metadata from `loser` into `winner` in place."""
    # original_names
    wn = set(winner.get("original_names") or [])
    for n in loser.get("original_names") or []:
        if n not in wn:
            winner.setdefault("original_names", []).append(n)
            wn.add(n)
    # papers_by_conference
    wpbc = winner.setdefault("papers_by_conference", {})
    for conf, ps in (loser.get("papers_by_conference") or {}).items():
        ex = set(wpbc.setdefault(conf, []))
        for p in ps:
            if p not in ex:
                wpbc[conf].append(p)
                ex.add(p)
    # original_nodes
    wnodes = winner.setdefault("original_nodes", {})
    for k, v in (loser.get("original_nodes") or {}).items():
        if k not in wnodes:
            wnodes[k] = v
    # source_snippets_evidence
    wsse = winner.setdefault("source_snippets_evidence", [])
    wset = {json.dumps(s, sort_keys=True) if isinstance(s, dict) else str(s) for s in wsse}
    for s in loser.get("source_snippets_evidence") or []:
        sig = json.dumps(s, sort_keys=True) if isinstance(s, dict) else str(s)
        if sig not in wset:
            wsse.append(s)
            wset.add(sig)
    # characterizations
    wchars = winner.setdefault("characterizations", {})
    for conf, ch in (loser.get("characterizations") or {}).items():
        if conf not in wchars:
            wchars[conf] = ch
    if not winner.get("characterization") and loser.get("characterization"):
        winner["characterization"] = loser["characterization"]


def _apply_id_to_canon(groups: List[Dict[str, Any]],
                       id_to_canon: Dict[int, str]) -> List[Dict[str, Any]]:
    """Group input groups by their assigned canonical name and merge metadata."""
    by_canon: Dict[str, List[int]] = {}
    for i, c in id_to_canon.items():
        by_canon.setdefault(c, []).append(i)
    out: List[Dict[str, Any]] = []
    for canon, idxs in by_canon.items():
        # Pick the seed: the input group with highest paper_count
        winner_idx = max(idxs, key=lambda i: groups[i].get("paper_count", 0))
        winner = dict(groups[winner_idx])
        winner["canonical_name"] = canon  # use the LLM-chosen canonical name
        for j in idxs:
            if j == winner_idx:
                continue
            _merge_groups_joint(winner, groups[j])
        # Recompute aggregate paper info
        pbc = winner.get("papers_by_conference", {})
        winner["paper_count_by_conference"] = {c: len(ps) for c, ps in pbc.items()}
        all_papers = [{"conference": c, "paper": p} for c, ps in pbc.items() for p in ps]
        winner["papers"] = all_papers
        winner["paper_count"] = len(all_papers)
        out.append(winner)
    return out


def merge_one_type(groups: List[Dict[str, Any]], node_type: str,
                   provider: str, model: str, batch_size: int) -> List[Dict[str, Any]]:
    """Run the LLM merge pass on one entity type using smart batching."""
    print(f"\n=== Merging {node_type} (start: {len(groups)}) ===")
    if len(groups) <= 1:
        return groups
    names = [g.get("canonical_name", "") for g in groups]
    batch_idx_lists = make_batches(names, batch_size=batch_size)
    print(f"  Smart-clustered into {len(batch_idx_lists)} batches "
          f"(target size {batch_size})")

    # We accumulate id→canonical assignments across batches
    full_id_to_canon: Dict[int, str] = {}

    for bnum, idxs in enumerate(batch_idx_lists, 1):
        batch_groups = [groups[i] for i in idxs]
        slim_groups = [{"id": j, **_slim(g)} for j, g in enumerate(batch_groups)]
        groups_json = json.dumps(slim_groups, indent=2)
        prompt = prompts.MERGE_GROUPS_PROMPT.format(
            node_type=node_type, groups_json=groups_json,
        )
        for attempt in range(3):
            try:
                result = call_llm_for_aggregation(prompt, provider, model)
                break
            except Exception as e:
                print(f"    batch {bnum}/{len(batch_idx_lists)} attempt {attempt+1}: {e}")
                if attempt == 2:
                    result = None
                else:
                    time.sleep(5 * (attempt + 1))
        if result is None:
            # Fallback: keep groups as-is
            for j, idx in enumerate(idxs):
                full_id_to_canon[idx] = groups[idx].get("canonical_name", "")
            continue
        # Parse string fences
        if isinstance(result, str):
            text = result.strip()
            fence = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
            if fence:
                text = fence.group(1).strip()
            try:
                result = json.loads(text)
            except json.JSONDecodeError:
                try:
                    from json_repair import repair_json
                    result = repair_json(text, return_objects=True)
                except Exception:
                    result = {}
        local_map = _decode_id_groups(result, batch_groups)
        coverage = sum(1 for v in local_map.values() if v)
        print(f"  batch {bnum}/{len(batch_idx_lists)}: {len(set(local_map.values()))} groups "
              f"from {len(batch_groups)} input ({coverage}/{len(batch_groups)} covered)")
        for j, idx in enumerate(idxs):
            full_id_to_canon[idx] = local_map.get(j, batch_groups[j].get("canonical_name", ""))

    # Apply the per-batch decisions to original groups
    merged = _apply_id_to_canon(groups, full_id_to_canon)
    print(f"  After per-batch merges: {len(merged)} groups")

    # Cross-batch pass: now merge groups whose canonical_names match (post LLM)
    # via the same id_to_canon flow on the post-merge list
    if len(merged) <= batch_size:
        # Single global pass
        slim_groups = [{"id": j, **_slim(g)} for j, g in enumerate(merged)]
        groups_json = json.dumps(slim_groups, indent=2)
        prompt = prompts.MERGE_GROUPS_PROMPT.format(
            node_type=node_type, groups_json=groups_json,
        )
        try:
            result = call_llm_for_aggregation(prompt, provider, model)
            if isinstance(result, str):
                text = result.strip()
                fence = re.search(r"```(?:json)?\s*\n?(.*?)\n?```", text, re.DOTALL)
                if fence:
                    text = fence.group(1).strip()
                try:
                    result = json.loads(text)
                except json.JSONDecodeError:
                    try:
                        from json_repair import repair_json
                        result = repair_json(text, return_objects=True)
                    except Exception:
                        result = {}
            local_map = _decode_id_groups(result, merged)
            merged = _apply_id_to_canon(merged, local_map)
            print(f"  After cross-batch global merge: {len(merged)} groups")
        except Exception as e:
            print(f"  cross-batch merge failed: {e}")

    return merged


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--provider", default="google")
    parser.add_argument("--model", default="gemini-2.5-pro")
    parser.add_argument("--batch-size", type=int, default=500)
    parser.add_argument("--types", nargs="+",
                        default=["constructs", "measurements", "behaviors"])
    args = parser.parse_args()

    with open(args.input) as f:
        net = json.load(f)
    print(f"Loaded {args.input}")
    for et in ("constructs", "measurements", "behaviors"):
        print(f"  {et}: {len(net.get(et, []))}")
    print(f"  relationships: {len(net.get('relationships', []))}")

    for et in args.types:
        net[et] = merge_one_type(
            net.get(et, []) or [], et,
            args.provider, args.model, args.batch_size,
        )

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(net, f, indent=2)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
