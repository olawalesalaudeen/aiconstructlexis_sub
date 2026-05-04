"""
Apply canonical-level majority vote to RELATIONSHIPS (in addition to entities).

For each (canonical_source, canonical_target, type) edge, look across all
3 models per paper and keep the edge for that paper only when ≥k models
extracted some surface variant of the same canonical edge.

This corrects the same bug for relationships that we corrected for entities:
the original raw-string MV was at extraction time and surface variants
caused most edges to fail MV. With canonical-MV, an edge passes if 2/3
models concur after harmonization.

Usage:
    python scripts/joint_canonical_mv_relationships.py \
        --joint network_data/joint_neurips24_iclr25/joint_network_merged.json \
        --confs neurips24:network_data/neurips24/trials \
                iclr25:network_data/iclr25/trials \
        --models gemini25pro gpt54mini qwen35_397b \
        --threshold 2
"""
import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, Tuple


def _norm(s: str) -> str:
    s = (s or "").strip().lower()
    for ch in "-_/": s = s.replace(ch, " ")
    return " ".join(s.split())


# Symmetric relationship types — A→B and B→A are the same edge
SYMMETRIC_TYPES = {"related", "correlates"}


def _bucket_key(src: str, tgt: str, rtype: str) -> Tuple[str, str, str]:
    if rtype in SYMMETRIC_TYPES:
        a, b = sorted([src, tgt])
        return (a, b, rtype)
    return (src, tgt, rtype)


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--joint", required=True)
    p.add_argument("--confs", nargs="+", required=True, help="conf:trials_dir")
    p.add_argument("--models", nargs="+", required=True)
    p.add_argument("--threshold", type=int, default=2)
    args = p.parse_args()

    with open(args.joint) as f:
        net = json.load(f)

    # Build name_mapping (lowercased and normalized)
    nm = {}
    nm_norm = {}
    for et in ("constructs", "measurements", "behaviors"):
        for g in net.get(et, []) or []:
            c = (g.get("canonical_name") or "").strip()
            if not c: continue
            nm[c.lower()] = c
            nm_norm[_norm(c)] = c
            for orig in g.get("original_names", []) or []:
                if orig:
                    nm[orig.lower()] = c
                    nm_norm[_norm(orig)] = c
    for orig, canon in (net.get("name_mapping") or {}).items():
        if orig and canon:
            nm.setdefault(orig.lower(), canon)
            nm_norm.setdefault(_norm(orig), canon)

    def resolve(s: str):
        s = s.strip()
        return nm.get(s.lower()) or nm_norm.get(_norm(s))

    # Build canonical edge ledger from per-model raw rel trials:
    # (canon_src, canon_tgt, type) -> conf -> paper -> set(models)
    edge_ledger: Dict[Tuple[str, str, str], Dict[str, Dict[str, set]]] = \
        defaultdict(lambda: defaultdict(lambda: defaultdict(set)))

    for conf_spec in args.confs:
        conf, trials_dir = conf_spec.split(":", 1)
        for model in args.models:
            path = Path(trials_dir) / model / "relationship_trials.json"
            if not path.is_file():
                print(f"WARNING: missing {path}", file=sys.stderr); continue
            with open(path) as f:
                trials = json.load(f)
            for paper, paper_trials in trials.items():
                seen_in_paper: set = set()
                for trial_rels in paper_trials:
                    if not isinstance(trial_rels, list):
                        continue
                    for r in trial_rels:
                        if not isinstance(r, dict): continue
                        src = r.get("source", "")
                        tgt = r.get("target", "")
                        rtype = (r.get("type") or "").strip().lower()
                        c_src = resolve(src)
                        c_tgt = resolve(tgt)
                        if not (c_src and c_tgt and rtype): continue
                        # Drop self-loops
                        if c_src == c_tgt: continue
                        # Symmetric types: bucket key sorts endpoints
                        key = _bucket_key(c_src, c_tgt, rtype)
                        if (key, paper) in seen_in_paper: continue
                        seen_in_paper.add((key, paper))
                        edge_ledger[key][conf][paper].add(model)

    # Cross-check: only keep edges where ≥threshold models agree per paper
    new_rels = []
    n_total_canonical_edges = len(edge_ledger)
    for (src, tgt, rtype), conf_papers in edge_ledger.items():
        valid_papers = []
        pbc: Dict[str, list] = {}
        for conf, papers in conf_papers.items():
            for paper, models in papers.items():
                if len(models) >= args.threshold:
                    valid_papers.append({"conference": conf, "paper": paper})
                    pbc.setdefault(conf, []).append(paper)
        if not valid_papers:
            continue
        # Look up evidence from existing rels (best-effort)
        # We just produce a fresh edge here
        new_rels.append({
            "source": src,
            "target": tgt,
            "type": rtype,
            "papers": valid_papers,
            "papers_by_conference": pbc,
            "paper_count": len(valid_papers),
            "paper_count_by_conference": {c: len(ps) for c, ps in pbc.items()},
        })

    # Carry over evidence from old rels into new ones (matched by (src,tgt,type))
    old = {(r["source"], r["target"], r["type"].lower()): r
           for r in (net.get("relationships") or [])}
    for r in new_rels:
        k = (r["source"], r["target"], r["type"])
        if k in old:
            ev = old[k].get("evidence") or []
            r["evidence"] = ev

    new_rels.sort(key=lambda r: -r["paper_count"])

    print(f"Canonical edges (any single extraction): {n_total_canonical_edges}")
    print(f"After canonical-MV (≥{args.threshold} models per paper): {len(new_rels)}")

    net["relationships"] = new_rels
    with open(args.joint, "w") as f:
        json.dump(net, f, indent=2)
    print(f"Wrote {args.joint}")


if __name__ == "__main__":
    main()
