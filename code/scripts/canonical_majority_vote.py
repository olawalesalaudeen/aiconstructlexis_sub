"""
Apply canonical-level majority vote AFTER harmonization.

For each entity (construct/measurement/behavior), we look at the per-model
raw extractions and count how many of the 3 models contributed ANY name that
maps to the same canonical for each paper. A (canonical, paper) pair passes
MV when ≥2 of 3 models contributed.

This corrects a bug in the original pipeline: raw-string MV happened BEFORE
harmonization, so a paper where 3 models said `Reasoning ability` /
`Reasoning capability` / `Reasoning` got dropped (no string had 2 votes)
even though all three were the same concept. After this fix, every
canonical's `paper_count` reflects the true cross-model support.

Usage:
    python scripts/canonical_majority_vote.py \
        --harmonized network_data/iclr25/harmonized_network_characterized.json \
        --trials-dir network_data/iclr25/trials \
        --models gemini25pro gpt54mini qwen35_397b \
        --threshold 2

Writes back to the input file (atomic via tmp file).
"""

import argparse
import json
import os
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Set


def build_name_mapping(network: Dict[str, Any]) -> Dict[str, str]:
    """Build lowercased original_name -> canonical_name mapping from all groups."""
    nm: Dict[str, str] = {}
    for etype in ("constructs", "measurements", "behaviors"):
        for g in network.get(etype, []) or []:
            canon = (g.get("canonical_name") or "").strip()
            if not canon:
                continue
            nm[canon.strip().lower()] = canon
            for orig in g.get("original_names", []) or []:
                if orig:
                    nm[orig.strip().lower()] = canon
    # Also fold in any explicit name_mapping field (post-merge residuals etc.)
    for orig, canon in (network.get("name_mapping") or {}).items():
        if orig and canon:
            nm.setdefault(orig.strip().lower(), canon)
    return nm


def collect_canonical_contributions(
    trials_dir: Path,
    models: list,
    name_mapping: Dict[str, str],
    canon_sets: Dict[str, Set[str]],
) -> Dict[str, Dict[str, Dict[str, Set[str]]]]:
    """For each entity type, build: canonical -> paper -> set(models that contributed).

    canon_sets restricts which canonicals we count per type, so a measurement
    canonical doesn't pollute the construct ledger.
    """
    contributions: Dict[str, Dict[str, Dict[str, Set[str]]]] = {
        "constructs": defaultdict(lambda: defaultdict(set)),
        "measurements": defaultdict(lambda: defaultdict(set)),
        "behaviors": defaultdict(lambda: defaultdict(set)),
    }
    for model in models:
        path = trials_dir / model / "entity_trials.json"
        if not path.is_file():
            print(f"WARNING: missing trials for {model}: {path}", file=sys.stderr)
            continue
        with open(path) as f:
            trials = json.load(f)
        for paper, paper_trials in trials.items():
            for trial in paper_trials:
                if not isinstance(trial, dict):
                    continue
                nn = trial.get("Nomological Network") or trial
                if not isinstance(nn, dict):
                    continue
                for etype in ("constructs", "measurements", "behaviors"):
                    for ent in nn.get(etype, []) or []:
                        if not isinstance(ent, dict):
                            continue
                        raw = (ent.get("name") or "").strip()
                        if not raw:
                            continue
                        canon = name_mapping.get(raw.lower())
                        if canon is None:
                            continue
                        # Only credit it to the entity type that owns this canonical
                        if canon in canon_sets.get(etype, set()):
                            contributions[etype][canon][paper].add(model)
    return contributions


def apply_mv(
    network: Dict[str, Any],
    contributions: Dict[str, Dict[str, Dict[str, Set[str]]]],
    threshold: int,
    drop_zero_papers: bool = False,
) -> Dict[str, Dict[str, int]]:
    """Update each entity's papers and paper_count to reflect canonical MV.

    Returns per-type stats: {etype: {kept, dropped, papers_added, papers_removed}}.
    """
    stats: Dict[str, Dict[str, int]] = {}
    for etype in ("constructs", "measurements", "behaviors"):
        kept_groups = []
        dropped = 0
        papers_added = 0
        papers_removed = 0
        for g in network.get(etype, []) or []:
            canon = (g.get("canonical_name") or "").strip()
            old_papers = set(g.get("papers", []) or [])
            paper_models = contributions[etype].get(canon, {})
            mv_papers = {p for p, ms in paper_models.items() if len(ms) >= threshold}
            if not mv_papers and drop_zero_papers:
                dropped += 1
                continue
            # Compute changes
            papers_added += len(mv_papers - old_papers)
            papers_removed += len(old_papers - mv_papers)
            g["papers"] = sorted(mv_papers)
            g["paper_count"] = len(mv_papers)
            # Stamp diagnostic info
            g["_canonical_mv"] = {
                "threshold": threshold,
                "n_papers_total": len(paper_models),
                "n_papers_mv": len(mv_papers),
            }
            kept_groups.append(g)
        network[etype] = kept_groups
        stats[etype] = {
            "kept": len(kept_groups),
            "dropped": dropped,
            "papers_added": papers_added,
            "papers_removed": papers_removed,
        }
    return stats


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--harmonized", required=True, help="harmonized_network[_characterized].json")
    parser.add_argument("--trials-dir", required=True, help="dir containing per-model trials/")
    parser.add_argument("--models", nargs="+", required=True,
                        help="model labels matching trials/<label>/ directories")
    parser.add_argument("--threshold", type=int, default=2, help="≥k models must contribute")
    parser.add_argument("--drop-zero", action="store_true",
                        help="drop canonicals with zero MV-passing papers")
    args = parser.parse_args()

    h_path = Path(args.harmonized)
    with open(h_path) as f:
        network = json.load(f)

    print(f"Loaded {h_path}")
    for et in ("constructs", "measurements", "behaviors"):
        print(f"  {et}: {len(network.get(et, []))}")

    name_mapping = build_name_mapping(network)
    print(f"Name mapping: {len(name_mapping)} entries")

    canon_sets = {
        et: {(g.get("canonical_name") or "").strip()
             for g in network.get(et, []) or []
             if (g.get("canonical_name") or "").strip()}
        for et in ("constructs", "measurements", "behaviors")
    }

    contributions = collect_canonical_contributions(
        Path(args.trials_dir), args.models, name_mapping, canon_sets,
    )
    print(f"\nApplying canonical MV with threshold={args.threshold}...")
    stats = apply_mv(network, contributions, args.threshold, drop_zero_papers=args.drop_zero)

    for et, s in stats.items():
        print(f"  {et}: kept={s['kept']}, dropped={s['dropped']}, "
              f"papers added={s['papers_added']}, removed={s['papers_removed']}")

    # Atomic write
    tmp = h_path.with_suffix(h_path.suffix + ".tmp")
    with open(tmp, "w") as f:
        json.dump(network, f, indent=2)
    os.replace(tmp, h_path)
    print(f"\nWrote updated {h_path}")


if __name__ == "__main__":
    main()
