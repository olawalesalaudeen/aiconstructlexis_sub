"""
Build a JOINT nomological network from two or more already-harmonized
conference networks.

Steps:
  1. Load each input harmonized network (post-canonical-MV).
  2. UNION at canonical name: when the same canonical_name appears in both,
     merge papers / original_names / original_nodes / source_snippets /
     characterizations across conferences. Track per-conference paper counts
     in `papers_by_conference`.
  3. UNION relationships: dedupe by (canonical_source, canonical_target,
     type), unioning evidence + papers across conferences.
  4. Deterministic post-merge for residual surface variants
     (case/hyphen/plural/synonym-verb that escape the per-conference passes).
  5. (Optional) LLM cross-conference merge pass — left as a separate step
     in cluster-batched LLM merge, run via the existing aggregator API.

Usage:
    python scripts/build_joint_network.py \
        --inputs neurips24:network_data/neurips24/harmonized_network_characterized.json \
                 iclr25:network_data/iclr25/harmonized_network_characterized.json \
        --output network_data/joint_neurips24_iclr25/joint_network.json
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))


def _norm_key(name: str) -> str:
    """Lowercased, trimmed key for first-pass union by canonical name."""
    return (name or "").strip().lower()


def merge_group_into(target: Dict[str, Any], source: Dict[str, Any], conf: str) -> None:
    """Merge one group's metadata into another, prefixing papers with conf tag."""
    # original_names
    tn = set(target.setdefault("original_names", []))
    for n in source.get("original_names", []) or []:
        if n and n not in tn:
            target["original_names"].append(n)
            tn.add(n)
    # original_nodes (dict of original_name -> {definition, papers})
    on = target.setdefault("original_nodes", {})
    for k, v in (source.get("original_nodes") or {}).items():
        if k not in on:
            on[k] = {"definition": v.get("definition", ""),
                     "papers": [(conf, p) for p in (v.get("papers") or [])]}
        else:
            existing = {tuple(p) if isinstance(p, list) else p
                        for p in on[k].get("papers") or []}
            for p in v.get("papers") or []:
                tag = (conf, p)
                if tag not in existing:
                    on[k].setdefault("papers", []).append(tag)
                    existing.add(tag)
    # source_snippets_evidence
    sse = target.setdefault("source_snippets_evidence", [])
    sse_set = {json.dumps(s, sort_keys=True) if isinstance(s, dict) else str(s) for s in sse}
    for s in source.get("source_snippets_evidence") or []:
        sig = json.dumps(s, sort_keys=True) if isinstance(s, dict) else str(s)
        if sig not in sse_set:
            sse.append(s)
            sse_set.add(sig)
    # papers — store as (conf, paper) tuples in a hidden per-conference dict
    pbc = target.setdefault("papers_by_conference", {})
    pbc.setdefault(conf, [])
    existing_pbc = set(pbc[conf])
    for p in source.get("papers") or []:
        if p not in existing_pbc:
            pbc[conf].append(p)
            existing_pbc.add(p)
    # characterization — keep per-conference field if multiple; primary = first non-empty
    char = (source.get("characterization") or "").strip()
    if char:
        chars = target.setdefault("characterizations", {})
        chars[conf] = char
        # Promote to top-level "characterization" if not set
        if not target.get("characterization"):
            target["characterization"] = char
    # canonical_definition: prefer non-empty
    if not target.get("canonical_definition") and source.get("canonical_definition"):
        target["canonical_definition"] = source["canonical_definition"]


def build_joint_entities(inputs: List[Tuple[str, Dict[str, Any]]]) -> Dict[str, List[Dict[str, Any]]]:
    out = {"constructs": [], "measurements": [], "behaviors": []}
    for etype in out:
        by_key: Dict[str, Dict[str, Any]] = {}
        for conf, net in inputs:
            for g in net.get(etype, []) or []:
                canon = (g.get("canonical_name") or "").strip()
                if not canon:
                    continue
                key = _norm_key(canon)
                if key not in by_key:
                    new_g = {
                        "canonical_name": canon,
                        "original_names": [],
                        "original_nodes": {},
                        "source_snippets_evidence": [],
                        "papers_by_conference": {},
                    }
                    by_key[key] = new_g
                merge_group_into(by_key[key], g, conf)
        # Compute aggregate paper counts and flatten papers list (with conf tag)
        groups = []
        for g in by_key.values():
            pbc = g.get("papers_by_conference", {})
            all_papers = []
            for conf, papers in pbc.items():
                for p in papers:
                    all_papers.append({"conference": conf, "paper": p})
            g["papers"] = all_papers
            g["paper_count"] = len(all_papers)
            g["paper_count_by_conference"] = {c: len(ps) for c, ps in pbc.items()}
            groups.append(g)
        out[etype] = groups
    return out


def build_joint_relationships(inputs: List[Tuple[str, Dict[str, Any]]]) -> List[Dict[str, Any]]:
    by_key: Dict[Tuple[str, str, str], Dict[str, Any]] = {}
    for conf, net in inputs:
        for r in net.get("relationships", []) or []:
            src = (r.get("source") or "").strip()
            tgt = (r.get("target") or "").strip()
            rtype = (r.get("type") or "").strip().lower()
            if not src or not tgt or not rtype:
                continue
            key = (_norm_key(src), _norm_key(tgt), rtype)
            if key not in by_key:
                by_key[key] = {
                    "source": src,
                    "target": tgt,
                    "type": rtype,
                    "evidence": [],
                    "papers": [],
                    "papers_by_conference": {},
                    "paper_count": 0,
                }
            tgt_rel = by_key[key]
            # Prefer longer, more specific display name
            if len(src) > len(tgt_rel["source"]):
                tgt_rel["source"] = src
            if len(tgt) > len(tgt_rel["target"]):
                tgt_rel["target"] = tgt
            ev_set = set(tgt_rel.get("evidence") or [])
            for e in r.get("evidence") or []:
                if e and e not in ev_set:
                    tgt_rel["evidence"].append(e)
                    ev_set.add(e)
            pbc = tgt_rel.setdefault("papers_by_conference", {})
            pbc.setdefault(conf, [])
            ex = set(pbc[conf])
            # Per-conf rels may have papers as either list[str] or
            # list[{"conference":..,"paper":..}] (after rel canonical-MV).
            for p in r.get("papers") or []:
                if isinstance(p, dict):
                    p_name = p.get("paper")
                else:
                    p_name = p
                if p_name and p_name not in ex:
                    pbc[conf].append(p_name)
                    ex.add(p_name)
                    tgt_rel["papers"].append({"conference": conf, "paper": p_name})
                    tgt_rel["paper_count"] += 1
    rels = list(by_key.values())
    rels.sort(key=lambda r: (-r["paper_count"], r["source"], r["target"]))
    return rels


def deterministic_post_merge(network: Dict[str, Any]) -> Dict[str, Any]:
    """Joint-aware deterministic merge: collapses canonicals whose names
    normalize identically (same surface variants), unioning the joint-network
    metadata structures (papers as {conference, paper} dicts, papers_by_conference,
    characterizations dict, etc.)."""
    from scripts.post_merge_residuals import normalize, rebuild_name_mapping

    for et in ("constructs", "measurements", "behaviors"):
        items = network.get(et, []) or []
        if not items:
            continue
        by_norm: Dict[str, List[int]] = defaultdict(list)
        for i, g in enumerate(items):
            c = g.get("canonical_name", "")
            if c:
                by_norm[normalize(c)].append(i)

        new_items: List[Dict[str, Any]] = []
        merged_count = 0
        for norm_key, idxs in by_norm.items():
            if len(idxs) == 1:
                new_items.append(items[idxs[0]])
                continue
            # Pick winner: highest paper_count, tiebreak shorter name
            winner_idx = max(
                idxs,
                key=lambda i: (
                    items[i].get("paper_count", 0),
                    -len(items[i].get("canonical_name", "")),
                ),
            )
            winner = dict(items[winner_idx])
            for j in idxs:
                if j == winner_idx:
                    continue
                src = items[j]
                # original_names
                wn = set(winner.get("original_names") or [])
                for n in src.get("original_names") or []:
                    if n not in wn:
                        winner.setdefault("original_names", []).append(n)
                        wn.add(n)
                # papers_by_conference
                wpbc = winner.setdefault("papers_by_conference", {})
                for conf, ps in (src.get("papers_by_conference") or {}).items():
                    existing = set(wpbc.setdefault(conf, []))
                    for p in ps:
                        if p not in existing:
                            wpbc[conf].append(p)
                            existing.add(p)
                # original_nodes
                wnodes = winner.setdefault("original_nodes", {})
                for k, v in (src.get("original_nodes") or {}).items():
                    if k not in wnodes:
                        wnodes[k] = v
                # source_snippets_evidence
                wsse = winner.setdefault("source_snippets_evidence", [])
                wset = {json.dumps(s, sort_keys=True) if isinstance(s, dict) else str(s) for s in wsse}
                for s in src.get("source_snippets_evidence") or []:
                    sig = json.dumps(s, sort_keys=True) if isinstance(s, dict) else str(s)
                    if sig not in wset:
                        wsse.append(s)
                        wset.add(sig)
                # characterizations dict
                wchars = winner.setdefault("characterizations", {})
                for conf, ch in (src.get("characterizations") or {}).items():
                    if conf not in wchars:
                        wchars[conf] = ch
                if not winner.get("characterization") and src.get("characterization"):
                    winner["characterization"] = src["characterization"]
                merged_count += 1
            # Recompute aggregate paper info
            pbc = winner.get("papers_by_conference", {})
            winner["paper_count_by_conference"] = {c: len(ps) for c, ps in pbc.items()}
            all_papers = [{"conference": c, "paper": p} for c, ps in pbc.items() for p in ps]
            winner["papers"] = all_papers
            winner["paper_count"] = len(all_papers)
            new_items.append(winner)

        network[et] = new_items
        print(f"  post-merge {et}: {len(items)} → {len(new_items)} (-{merged_count})")

    network["name_mapping"] = rebuild_name_mapping(network)
    return network


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--inputs", nargs="+", required=True,
                        help="conference_label:path/to/harmonized_network_characterized.json")
    parser.add_argument("--output", required=True)
    parser.add_argument("--no-postmerge", action="store_true",
                        help="Skip the deterministic post-merge step")
    args = parser.parse_args()

    inputs: List[Tuple[str, Dict[str, Any]]] = []
    for spec in args.inputs:
        if ":" not in spec:
            print(f"Bad input spec (need conf:path): {spec}", file=sys.stderr)
            sys.exit(1)
        conf, path = spec.split(":", 1)
        with open(path) as f:
            inputs.append((conf, json.load(f)))
        net = inputs[-1][1]
        print(f"Loaded [{conf}] {path}:")
        for et in ("constructs", "measurements", "behaviors"):
            print(f"  {et}: {len(net.get(et, []) or [])}")
        print(f"  relationships: {len(net.get('relationships', []) or [])}")

    print("\nBuilding joint entities...")
    joint = build_joint_entities(inputs)
    for et in ("constructs", "measurements", "behaviors"):
        print(f"  {et}: {len(joint[et])} (after canonical-name union)")

    print("\nBuilding joint relationships...")
    joint_rels = build_joint_relationships(inputs)
    print(f"  relationships: {len(joint_rels)}")

    network: Dict[str, Any] = {
        "metadata": {
            "joint_of": [c for c, _ in inputs],
            "n_conferences": len(inputs),
        },
        "constructs": joint["constructs"],
        "measurements": joint["measurements"],
        "behaviors": joint["behaviors"],
        "relationships": joint_rels,
    }

    # All papers across conferences
    all_papers = []
    for conf, net in inputs:
        for p in net.get("papers", []) or []:
            all_papers.append({"conference": conf, "paper": p})
    network["papers"] = all_papers
    network["paper_count_by_conference"] = {
        conf: len(net.get("papers", []) or []) for conf, net in inputs
    }

    if not args.no_postmerge:
        print("\nRunning deterministic post-merge for surface variants...")
        network = deterministic_post_merge(network)

    # Final summary
    print("\n=== JOINT NETWORK ===")
    for et in ("constructs", "measurements", "behaviors"):
        n = len(network[et])
        n_multi = sum(1 for g in network[et] if g.get("paper_count", 0) >= 2)
        n_cross = sum(1 for g in network[et] if len(g.get("paper_count_by_conference", {})) >= 2)
        print(f"  {et}: {n} total | {n_multi} (≥2 papers) | {n_cross} (in both confs)")
    print(f"  relationships: {len(network['relationships'])}")
    print(f"  papers: {len(network['papers'])}")

    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(network, f, indent=2)
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
