"""
Deterministic post-process pass to catch residual surface-variant duplicates
that the LLM harmonization missed. Operates on a harmonized_network.json,
collapses pairs/triples whose canonical names differ only by:
  - case / hyphenation / whitespace / punctuation
  - filler suffix singular vs plural ("X ability" / "X abilities" / "X capability"
    / "X capabilities" / "X capacity" / "X skill" / "X skills" /
    "X proficiency" / "X performance")
  - simple plural (s/es/ies)
  - synonym verbs ("X comprehension" / "X awareness" / "X understanding";
    "X recognition" / "X identification")
  - morphological variants ("Logical" ≡ "Logic", "Numerical" ≡ "Numeric",
    "Mathematical" ≡ "Math")
  - equivalent modality prefixes ("Multi-modal" / "Multimodal" / "Cross-modal")

When several canonicals collapse to one normalized form, the canonical with
the highest paper_count wins (ties broken by shorter name). The other groups'
metadata (papers, original_names, original_nodes, snippets, definitions) are
unioned into the winner.

After collapsing entities, the name_mapping is rebuilt and relationships
re-aggregated against the updated mapping.

Usage:
    python scripts/post_merge_residuals.py \
        --harmonized network_data/iclr25/harmonized_network.json \
        --simplified network_data/iclr25/inputs/simplified_multi_model_mv3.json
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

_UNICODE_HYPHENS = "\u2010\u2011\u2012\u2013\u2014\u2015\u2212"

_FILLER_SUFFIXES = (
    " abilities", " ability",
    " capabilities", " capability",
    " capacities", " capacity",
    " skills", " skill",
    " proficiencies", " proficiency",
    " performance",
    # Generic instrument/dataset suffixes
    " benchmark", " benchmarks",
    " dataset", " datasets",
    " evaluation", " evaluations",
    " judge", " judgment",
    " framework",
    " task", " tasks",
)

_SYNONYM_VERBS = [
    ("comprehension", "understanding"),
    ("awareness", "understanding"),
    ("identification", "recognition"),
]

_MORPHOLOGY = [
    ("logical", "logic"),
    ("numerical", "numeric"),
    ("mathematical", "math"),
    ("multi modal", "multimodal"),
    ("cross modal", "multimodal"),
    ("x modal", "multimodal"),
    ("vision language", "vision language"),  # noop — keeps as-is
    ("visio linguistic", "vision language"),
    ("visual linguistic", "vision language"),
]


def normalize(name: str) -> str:
    if not name:
        return ""
    s = name.strip().lower()
    for uh in _UNICODE_HYPHENS:
        s = s.replace(uh, "-")
    # Strip parenthetical acronyms / qualifiers: "BIG-Bench Hard (BBH)" → "BIG-Bench Hard"
    s = re.sub(r"\s*\([^)]*\)\s*", " ", s)
    for ch in "-_/":
        s = s.replace(ch, " ")
    s = "".join(c if (c.isalnum() or c.isspace()) else " " for c in s)
    s = " ".join(s.split())
    # Strip trailing filler suffixes — repeat in case of stacked suffixes like
    # "X benchmark dataset" → "X benchmark" → "X"
    changed = True
    while changed:
        changed = False
        for suf in _FILLER_SUFFIXES:
            if s.endswith(suf):
                s = s[: -len(suf)].rstrip()
                changed = True
                break
    # Synonym verbs (per-word substitution at boundaries)
    for src, dst in _SYNONYM_VERBS:
        s = re.sub(rf'\b{re.escape(src)}\b', dst, s)
    # Morphological variants (multi-word ones first to avoid overlap)
    for src, dst in sorted(_MORPHOLOGY, key=lambda x: -len(x[0])):
        s = re.sub(rf'\b{re.escape(src)}\b', dst, s)
    # Simple plural — applied to the LAST word only so we don't break "across"→"acros"
    parts = s.split()
    if parts:
        last = parts[-1]
        if last.endswith("ies") and len(last) > 3:
            parts[-1] = last[:-3] + "y"
        elif last.endswith("ses") and len(last) > 3:
            parts[-1] = last[:-2]
        elif last.endswith("s") and not last.endswith("ss") and len(last) > 1:
            parts[-1] = last[:-1]
        s = " ".join(parts)
    # Drop stopwords ("to", "of", "the", ...). Keep single-character tokens
    # (digits, acronym pieces) since they may carry meaning like "Llama Guard 2".
    _STOP = {"a", "an", "the", "of", "to", "for", "in", "on", "with", "by",
             "and", "or", "as"}
    parts = [p for p in s.split() if p not in _STOP]
    s = " ".join(parts)
    # Sort tokens to catch word-order swaps ("refusal answer" ≡ "answer refusal")
    # ONLY when token count is ≤ 3 AND none of the tokens look like a domain
    # qualifier ("medical", "visual", "audio", etc.) that would change meaning.
    # For safety we only fold word order on 2-token names.
    if len(parts) == 2:
        s = " ".join(sorted(parts))
    return " ".join(s.split())


def _union_into(winner: Dict[str, Any], loser: Dict[str, Any]) -> None:
    """Merge loser's metadata into winner in-place."""
    # original_names
    wn = set(winner.get("original_names") or [])
    for n in loser.get("original_names") or []:
        if n not in wn:
            winner.setdefault("original_names", []).append(n)
            wn.add(n)
    # papers
    wp = set(winner.get("papers") or [])
    for p in loser.get("papers") or []:
        if p not in wp:
            winner.setdefault("papers", []).append(p)
            wp.add(p)
    winner["paper_count"] = len(winner.get("papers") or [])
    # original_nodes
    wn_nodes = winner.setdefault("original_nodes", {})
    for k, v in (loser.get("original_nodes") or {}).items():
        if k not in wn_nodes:
            wn_nodes[k] = v
        else:
            # Merge papers under this original_node too
            existing_papers = set(wn_nodes[k].get("papers") or [])
            for p in v.get("papers") or []:
                if p not in existing_papers:
                    wn_nodes[k].setdefault("papers", []).append(p)
                    existing_papers.add(p)
    # source_snippets_evidence
    we = winner.setdefault("source_snippets_evidence", [])
    we_set = {json.dumps(s, sort_keys=True) if isinstance(s, dict) else s for s in we}
    for s in loser.get("source_snippets_evidence") or []:
        sig = json.dumps(s, sort_keys=True) if isinstance(s, dict) else s
        if sig not in we_set:
            we.append(s)
            we_set.add(sig)


def collapse(groups: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], int]:
    """Collapse groups whose canonical_name normalizes to the same form."""
    by_norm: Dict[str, List[int]] = defaultdict(list)
    for i, g in enumerate(groups):
        c = g.get("canonical_name", "")
        if c:
            by_norm[normalize(c)].append(i)

    keep: set = set()
    merged_count = 0
    out: List[Dict[str, Any]] = []
    consumed: set = set()
    for norm_key, idx_list in by_norm.items():
        if len(idx_list) == 1:
            keep.add(idx_list[0])
        else:
            # Pick winner: highest paper_count; tiebreak shorter canonical
            winner_idx = max(
                idx_list,
                key=lambda i: (
                    groups[i].get("paper_count", 0),
                    -len(groups[i].get("canonical_name", "")),
                ),
            )
            winner = dict(groups[winner_idx])  # shallow copy
            for i in idx_list:
                if i == winner_idx:
                    continue
                _union_into(winner, groups[i])
                merged_count += 1
                consumed.add(i)
            out.append(winner)
            consumed.add(winner_idx)
    # Add the singletons
    for i, g in enumerate(groups):
        if i in keep and i not in consumed:
            out.append(g)
    return out, merged_count


def rebuild_name_mapping(network: Dict[str, Any]) -> Dict[str, str]:
    nm: Dict[str, str] = {}
    for etype in ("constructs", "measurements", "behaviors"):
        for g in network.get(etype, []) or []:
            c = g.get("canonical_name", "")
            if not c:
                continue
            nm[c] = c
            for orig in g.get("original_names") or []:
                if orig:
                    nm[orig] = c
    return nm


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--harmonized", required=True)
    parser.add_argument("--simplified", default=None,
                        help="If provided, re-aggregate relationships against the new mapping")
    args = parser.parse_args()

    with open(args.harmonized) as f:
        net = json.load(f)

    print(f"Before:")
    for et in ("constructs", "measurements", "behaviors"):
        print(f"  {et}: {len(net.get(et, []))}")
    print(f"  relationships: {len(net.get('relationships', []))}")

    print("\nCollapsing residual surface-variant duplicates...")
    total_merged = 0
    for et in ("constructs", "measurements", "behaviors"):
        items = net.get(et, []) or []
        if not items:
            continue
        before = len(items)
        net[et], merged = collapse(items)
        after = len(net[et])
        total_merged += merged
        if merged > 0:
            print(f"  {et}: {before} → {after} (-{merged})")
        else:
            print(f"  {et}: {before} (no residual duplicates)")

    print(f"\nTotal residual merges: {total_merged}")

    # Rebuild name mapping
    net["name_mapping"] = rebuild_name_mapping(net)
    print(f"Rebuilt name_mapping: {len(net['name_mapping'])} entries")

    with open(args.harmonized, "w") as f:
        json.dump(net, f, indent=2)
    print(f"\nWrote {args.harmonized}")

    # Re-aggregate relationships if requested
    if args.simplified:
        print("\nRe-aggregating relationships against updated mapping...")
        from scripts.aggregate_relationships_deterministic import (
            aggregate as agg_rels,
        )
        with open(args.simplified) as f:
            simp = json.load(f)
        with open(args.harmonized) as f:
            net = json.load(f)
        aggregated, stats = agg_rels(simp, net)
        net["relationships"] = aggregated
        with open(args.harmonized, "w") as f:
            json.dump(net, f, indent=2)
        print(f"  Raw rels: {stats['n_raw']}  →  Aggregated: {stats['n_aggregated']}")
        print(f"  Unresolved sources: {stats['n_unresolved_src']}")
        print(f"  Unresolved targets: {stats['n_unresolved_tgt']}")


if __name__ == "__main__":
    main()
