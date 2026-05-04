"""
Drop single-paper entities (and their relationships) from a harmonized network.

This produces a noise-filtered version that retains only entities with at
least N papers (default N=2). The original harmonized file is left untouched;
output is written to a new file (default: same name with '.multi-paper' before
the extension).

This is intended to run BEFORE joining a conference's network with others, so
the joint network only has cross-validated concepts.

Usage:
    python scripts/filter_single_paper.py \
        --input  network_data/iclr25/harmonized_network_characterized.json \
        --output network_data/iclr25/harmonized_network.multi-paper.json \
        --min-papers 2
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True)
    p.add_argument("--output", default=None)
    p.add_argument("--min-papers", type=int, default=2,
                   help="Drop entities with paper_count < min-papers (default: 2)")
    args = p.parse_args()

    in_path = Path(args.input)
    out_path = Path(args.output) if args.output else \
        in_path.with_name(in_path.stem + ".multi-paper" + in_path.suffix)

    with open(in_path) as f:
        net = json.load(f)

    print(f"Loaded {in_path}")
    threshold = args.min_papers

    # Filter entities
    kept_canon: set = set()
    for et in ("constructs", "measurements", "behaviors"):
        items = net.get(et, []) or []
        kept = [g for g in items if g.get("paper_count", 0) >= threshold]
        net[et] = kept
        for g in kept:
            kept_canon.add(g.get("canonical_name", ""))
        dropped = len(items) - len(kept)
        print(f"  {et}: {len(items)} → {len(kept)}  (dropped {dropped} with paper_count<{threshold})")

    # Filter relationships — keep only those whose endpoints survive
    rels = net.get("relationships", []) or []
    kept_rels = [r for r in rels
                 if r.get("source") in kept_canon and r.get("target") in kept_canon]
    print(f"  relationships: {len(rels)} → {len(kept_rels)}  "
          f"(kept those with both endpoints surviving)")
    net["relationships"] = kept_rels

    # Rebuild name mapping (drop entries pointing to filtered entities)
    nm = {}
    for et in ("constructs", "measurements", "behaviors"):
        for g in net[et]:
            c = g.get("canonical_name", "").strip()
            if not c: continue
            nm[c] = c
            for orig in g.get("original_names", []) or []:
                if orig: nm[orig] = c
    net["name_mapping"] = nm

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(net, f, indent=2)
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
