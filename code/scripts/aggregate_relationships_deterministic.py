"""
Deterministic relationship aggregation — NO LLM CALLS.

Reads:
  - simplified extraction JSON (raw relationships per paper)
  - harmonized_network.json (canonical entity groups)

For each raw relationship:
  1. Look up canonical source name via the harmonized name_mapping
     (original_name -> canonical_name, built from all entity groups).
  2. Same for target.
  3. Apply normalization (case/hyphen/punctuation insensitive) so that minor
     surface variants of names that didn't make it into the mapping still
     resolve to the right canonical.
  4. Bucket by (canonical_source, canonical_target, type) and union evidence
     + papers across raw rows that fall into the same bucket.

Writes the aggregated relationships back into harmonized_network.json.

Usage:
    python scripts/aggregate_relationships_deterministic.py \
        --simplified network_data/iclr25/inputs/simplified_multi_model_mv3.json \
        --harmonized network_data/iclr25/harmonized_network.json
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


_UNICODE_HYPHENS = "\u2010\u2011\u2012\u2013\u2014\u2015\u2212"


def _normalize(name: str) -> str:
    """Aggressive normalization for fuzzy lookup against the canonical map."""
    if not name:
        return ""
    s = name.strip().lower()
    for uh in _UNICODE_HYPHENS:
        s = s.replace(uh, "-")
    for ch in "-_/":
        s = s.replace(ch, " ")
    s = "".join(c if (c.isalnum() or c.isspace()) else " " for c in s)
    s = " ".join(s.split())
    return s


def build_canonical_lookup(network: Dict[str, Any]) -> Dict[str, str]:
    """Build a robust original_name -> canonical_name mapping.

    Combines (in order of precedence):
      - explicit name_mapping field if present
      - canonical_name -> canonical_name identity
      - original_names -> canonical_name from each group
    Each name is also indexed by its normalized form so we can fall back
    when an extracted relationship name doesn't exactly match a stored form.
    """
    lookup: Dict[str, str] = {}
    norm_lookup: Dict[str, str] = {}

    # Explicit mapping (if any)
    for orig, canon in (network.get("name_mapping") or {}).items():
        if orig and canon:
            lookup[orig] = canon
            norm_lookup[_normalize(orig)] = canon

    # From each group
    for etype in ("constructs", "measurements", "behaviors"):
        for g in network.get(etype, []) or []:
            canon = g.get("canonical_name", "")
            if not canon:
                continue
            lookup[canon] = canon
            norm_lookup[_normalize(canon)] = canon
            for orig in g.get("original_names", []) or []:
                if orig:
                    lookup.setdefault(orig, canon)
                    norm_lookup.setdefault(_normalize(orig), canon)

    return {"exact": lookup, "norm": norm_lookup}


def resolve(name: str, lookup: Dict[str, Dict[str, str]]) -> str:
    """Map a raw relationship endpoint name to its canonical, or return as-is."""
    if not name:
        return name
    name = name.strip()
    if name in lookup["exact"]:
        return lookup["exact"][name]
    n = _normalize(name)
    if n in lookup["norm"]:
        return lookup["norm"][n]
    # No match → keep original (will surface as orphan)
    return name


# Symmetric relationship types — (A, B, type) and (B, A, type) refer to the same edge.
# Asymmetric types must keep direction.
SYMMETRIC_TYPES = {"related", "correlates"}


def _bucket_key(src: str, tgt: str, rtype: str) -> Tuple[str, str, str]:
    """Build the dedup key. For symmetric types, sort the endpoints so that
    A→B and B→A map to the same bucket. For asymmetric types, keep direction."""
    if rtype in SYMMETRIC_TYPES:
        a, b = sorted([src, tgt])
        return (a, b, rtype)
    return (src, tgt, rtype)


def aggregate(simplified: Dict[str, Any], network: Dict[str, Any]) -> Tuple[List[Dict[str, Any]], Dict[str, int]]:
    """Aggregate all raw relationships from simplified extraction into canonical
    relationships.

    Dedup behaviour:
      - `related` and `correlates` are treated as symmetric — (A, B) ≡ (B, A)
      - `causes` and `measured_by` keep direction (A→B ≠ B→A)
      - Self-loops (A == B) are dropped
    """
    lookup = build_canonical_lookup(network)

    buckets: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    n_raw = 0
    n_resolved = 0
    n_unresolved_src = 0
    n_unresolved_tgt = 0
    n_self_loops = 0

    for paper_name, paper_data in simplified.items():
        # Skip non-paper entries
        if not isinstance(paper_data, dict):
            continue
        # Schema: paper_data["parsed_text"]["Nomological Network"]["relationships"]
        nn = (paper_data.get("parsed_text") or {}).get("Nomological Network")
        if nn is None:
            nn = paper_data.get("Nomological Network") or paper_data
        if not isinstance(nn, dict):
            continue
        rels = nn.get("relationships") or []
        for rel in rels:
            if not isinstance(rel, dict):
                continue
            n_raw += 1
            src_raw = (rel.get("source") or "").strip()
            tgt_raw = (rel.get("target") or "").strip()
            rtype = (rel.get("type") or "").strip().lower()
            if not src_raw or not tgt_raw or not rtype:
                continue
            src = resolve(src_raw, lookup)
            tgt = resolve(tgt_raw, lookup)
            if src not in lookup["exact"] and _normalize(src) not in lookup["norm"]:
                n_unresolved_src += 1
            if tgt not in lookup["exact"] and _normalize(tgt) not in lookup["norm"]:
                n_unresolved_tgt += 1
            # Drop self-loops
            if src == tgt:
                n_self_loops += 1
                continue
            n_resolved += 1
            key = _bucket_key(src, tgt, rtype)
            if key not in buckets:
                # Use the bucket's chosen ordering (already sorted for symmetric types)
                buckets[key] = {
                    "source": key[0],
                    "target": key[1],
                    "type": rtype,
                    "evidence": [],
                    "papers": [],
                    "paper_count": 0,
                }
            bucket = buckets[key]
            ev = rel.get("evidence")
            if ev:
                if isinstance(ev, list):
                    for e in ev:
                        if e and e not in bucket["evidence"]:
                            bucket["evidence"].append(e)
                elif ev not in bucket["evidence"]:
                    bucket["evidence"].append(ev)
            if paper_name and paper_name not in bucket["papers"]:
                bucket["papers"].append(paper_name)
            bucket["paper_count"] = len(bucket["papers"])

    aggregated = list(buckets.values())
    aggregated.sort(key=lambda r: (-r["paper_count"], r["source"], r["target"]))
    return aggregated, {
        "n_raw": n_raw,
        "n_resolved": n_resolved,
        "n_aggregated": len(aggregated),
        "n_unresolved_src": n_unresolved_src,
        "n_unresolved_tgt": n_unresolved_tgt,
        "n_self_loops_dropped": n_self_loops,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--simplified", required=True)
    parser.add_argument("--harmonized", required=True)
    args = parser.parse_args()

    print(f"Loading {args.simplified}...")
    with open(args.simplified) as f:
        simplified = json.load(f)
    print(f"  {len(simplified)} papers")

    print(f"Loading {args.harmonized}...")
    with open(args.harmonized) as f:
        network = json.load(f)
    print(f"  constructs: {len(network.get('constructs', []))}, "
          f"measurements: {len(network.get('measurements', []))}, "
          f"behaviors: {len(network.get('behaviors', []))}")

    print("\nAggregating relationships deterministically...")
    aggregated, stats = aggregate(simplified, network)

    print(f"\n=== Stats ===")
    print(f"  Raw relationships: {stats['n_raw']}")
    print(f"  After dedup: {stats['n_aggregated']}")
    print(f"  Unresolved source endpoints: {stats['n_unresolved_src']}")
    print(f"  Unresolved target endpoints: {stats['n_unresolved_tgt']}")
    print(f"  Reduction: {stats['n_raw']} -> {stats['n_aggregated']} "
          f"({100*(1-stats['n_aggregated']/max(stats['n_raw'],1)):.1f}%)")

    network["relationships"] = aggregated
    print(f"\nWriting {args.harmonized}...")
    with open(args.harmonized, "w") as f:
        json.dump(network, f, indent=2)
    print("Done.")


if __name__ == "__main__":
    main()
