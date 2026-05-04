"""
Apply canonical-level majority vote across multiple conferences' per-model trials.

For the JOINT network: per (entity, conference), check which models extracted
synonyms of that canonical. A (canonical, conference, paper) passes MV when
>= threshold models contributed for that paper.

Usage:
    python scripts/joint_canonical_mv.py \
        --joint network_data/joint_neurips24_iclr25/joint_network_merged.json \
        --confs neurips24:network_data/neurips24/trials \
                iclr25:network_data/iclr25/trials \
        --models gemini25pro gpt54mini qwen35_397b \
        --threshold 2
"""
import argparse, json, sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, Any, List


def build_name_mapping(net: Dict[str, Any]) -> Dict[str, str]:
    nm = {}
    for et in ("constructs", "measurements", "behaviors"):
        for g in net.get(et, []) or []:
            c = (g.get("canonical_name") or "").strip()
            if not c: continue
            nm[c.strip().lower()] = c
            for orig in g.get("original_names", []) or []:
                if orig: nm[orig.strip().lower()] = c
    for orig, canon in (net.get("name_mapping") or {}).items():
        if orig and canon:
            nm.setdefault(orig.strip().lower(), canon)
    return nm


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--joint", required=True)
    parser.add_argument("--confs", nargs="+", required=True,
                        help="conf:trials_dir pairs")
    parser.add_argument("--models", nargs="+", required=True)
    parser.add_argument("--threshold", type=int, default=2)
    args = parser.parse_args()

    with open(args.joint) as f:
        net = json.load(f)
    nm = build_name_mapping(net)
    canon_sets = {
        et: {(g.get("canonical_name") or "").strip()
             for g in net.get(et, []) or []
             if (g.get("canonical_name") or "").strip()}
        for et in ("constructs", "measurements", "behaviors")
    }

    # canonical -> conf -> paper -> set(models)
    contrib: Dict[str, Dict[str, Dict[str, Dict[str, set]]]] = {
        et: defaultdict(lambda: defaultdict(lambda: defaultdict(set)))
        for et in ("constructs", "measurements", "behaviors")
    }

    for conf_spec in args.confs:
        conf, trials_dir = conf_spec.split(":", 1)
        for model in args.models:
            path = Path(trials_dir) / model / "entity_trials.json"
            if not path.is_file():
                print(f"WARNING: missing {path}", file=sys.stderr); continue
            with open(path) as f:
                trials = json.load(f)
            for paper, paper_trials in trials.items():
                for trial in paper_trials:
                    if not isinstance(trial, dict): continue
                    nn = trial.get("Nomological Network") or trial
                    if not isinstance(nn, dict): continue
                    for et in ("constructs", "measurements", "behaviors"):
                        for ent in nn.get(et, []) or []:
                            if not isinstance(ent, dict): continue
                            raw = (ent.get("name") or "").strip()
                            if not raw: continue
                            canon = nm.get(raw.lower())
                            if canon and canon in canon_sets[et]:
                                contrib[et][canon][conf][paper].add(model)

    # Update each entity's papers
    for et in ("constructs", "measurements", "behaviors"):
        new_groups: List[Dict[str, Any]] = []
        dropped = 0
        for g in net[et]:
            canon = (g.get("canonical_name") or "").strip()
            cmap = contrib[et].get(canon, {})
            # MV per (conf, paper)
            valid = []
            pbc: Dict[str, List[str]] = {}
            for conf, papers in cmap.items():
                for paper, models in papers.items():
                    if len(models) >= args.threshold:
                        valid.append({"conference": conf, "paper": paper})
                        pbc.setdefault(conf, []).append(paper)
            if not valid:
                dropped += 1
                continue
            g["papers"] = valid
            g["papers_by_conference"] = pbc
            g["paper_count"] = len(valid)
            g["paper_count_by_conference"] = {c: len(ps) for c, ps in pbc.items()}
            g["_canonical_mv"] = {
                "threshold": args.threshold,
                "n_papers_total": sum(len(p) for p in cmap.values()),
                "n_papers_mv": len(valid),
            }
            new_groups.append(g)
        print(f"{et}: kept={len(new_groups)}, dropped={dropped}")
        net[et] = new_groups

    with open(args.joint, "w") as f:
        json.dump(net, f, indent=2)
    print(f"Wrote {args.joint}")


if __name__ == "__main__":
    main()
