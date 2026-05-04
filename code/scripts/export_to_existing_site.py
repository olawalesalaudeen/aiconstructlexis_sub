"""
Export joint_v7_merged.json into the EXISTING aiconstructlexis_dev.github.io
data layout (per-entity JSON files under nomological_network_data/), so the
existing site picks up the new data without code changes.

Output layout (matches what's already deployed):
  nomological_network_data/
    index.json
    constructs/<slug>.json
    measurements/<slug>.json
    behaviors_tasks/<slug>.json

Per-entity schema (matches existing files):
  canonical_name, type (singular), canonical_definition, expert_reviewed,
  names[], papers[] (flat list of titles), paper_count, group_ids[],
  definitions[{text, paper}], definition_count,
  relationships[{direction, other_canonical_name, other_type,
                 relationship_type, paper, evidence}],
  relationship_count, incoming_relationship_count, outgoing_relationship_count

Forward-compat extras (ignored by current loader, useful for future versions):
  characterization, papers_by_conference, paper_count_by_conference,
  conferences

Usage:
  python scripts/export_to_existing_site.py \
    --input network_data/joint_progressive/joint_v7_merged.json \
    --site  aiconstructlexis_dev.github.io \
    --backup
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List


SUBDIR = {"constructs": "constructs", "measurements": "measurements", "behaviors": "behaviors_tasks"}
TYPE_SINGULAR = {"constructs": "construct", "measurements": "measurement", "behaviors": "behavior"}
TYPE_PLURAL_FOR_REL = {"constructs": "constructs", "measurements": "measurements", "behaviors": "behaviors_tasks"}


def slugify(name: str) -> str:
    s = (name or "").strip().lower()
    s = re.sub(r"[^a-z0-9]+", "_", s)
    s = re.sub(r"_+", "_", s).strip("_")
    return s or "unknown"


def papers_to_pbc(papers: List[Any]) -> Dict[str, List[str]]:
    out: Dict[str, List[str]] = defaultdict(list)
    seen: Dict[str, set] = defaultdict(set)
    for p in papers or []:
        if isinstance(p, dict):
            conf = p.get("conference") or "_unknown"
            paper = p.get("paper") or ""
        elif isinstance(p, list) and len(p) == 2:
            conf, paper = p
        else:
            conf, paper = "_unknown", str(p)
        if paper and paper not in seen[conf]:
            out[conf].append(paper)
            seen[conf].add(paper)
    return dict(out)


def flat_paper_titles(pbc: Dict[str, List[str]]) -> List[str]:
    """Return de-duplicated flat list of paper titles across conferences."""
    seen, out = set(), []
    for conf in sorted(pbc.keys()):
        for p in pbc[conf]:
            if p not in seen:
                out.append(p)
                seen.add(p)
    return out


def build_definitions(g: Dict[str, Any]) -> List[Dict[str, Any]]:
    """Existing site expects [{text, paper}, ...]."""
    out: List[Dict[str, Any]] = []
    for orig_name, node in (g.get("original_nodes") or {}).items():
        d = (node.get("definition") or "").strip()
        if not d:
            continue
        # Pick the first paper as a stand-in (existing site shows one paper per def)
        first_paper = ""
        for p in (node.get("papers") or []):
            if isinstance(p, dict):
                first_paper = p.get("paper") or ""
            elif isinstance(p, list) and len(p) == 2:
                first_paper = p[1]
            else:
                first_paper = str(p)
            if first_paper:
                break
        out.append({"text": d, "paper": first_paper, "original_name": orig_name})
    return out


def build_entity_record(g: Dict[str, Any], etype: str, rels_by_canon: Dict[str, List[Dict[str, Any]]]) -> Dict[str, Any]:
    canon = (g.get("canonical_name") or "").strip()
    pbc = g.get("papers_by_conference") or papers_to_pbc(g.get("papers") or [])
    paper_count = sum(len(v) for v in pbc.values()) if pbc else g.get("paper_count", 0)
    papers_flat = flat_paper_titles(pbc)

    # canonical_definition = the LLM-synthesized characterization (or fallback)
    canon_def = (g.get("characterization") or "").strip()
    is_placeholder = not canon_def
    if is_placeholder:
        canon_def = (g.get("canonical_definition") or "").strip()
    if not canon_def:
        for _, node in (g.get("original_nodes") or {}).items():
            d = (node.get("definition") or "").strip()
            if d:
                canon_def = d
                break

    # Relationships involving this canonical
    rels_for_node: List[Dict[str, Any]] = []
    in_count = out_count = 0
    for r in rels_by_canon.get(canon, []):
        is_outgoing = r["source"] == canon
        other = r["target"] if is_outgoing else r["source"]
        rel_pbc = r.get("papers_by_conference") or papers_to_pbc(r.get("papers") or [])
        first_paper = ""
        if rel_pbc:
            first_conf = next(iter(rel_pbc))
            ps = rel_pbc[first_conf]
            if ps:
                first_paper = ps[0]
        first_evidence = ""
        for e in (r.get("evidence") or []):
            if isinstance(e, str) and e.strip():
                first_evidence = e.strip()
                break
            if isinstance(e, dict):
                t = (e.get("evidence") or e.get("text") or "").strip()
                if t:
                    first_evidence = t
                    break
        other_type = r.get("_other_type", "")
        rels_for_node.append({
            "direction": "outgoing" if is_outgoing else "incoming",
            "other_canonical_name": other,
            "other_type": other_type,
            "relationship_type": r.get("type", ""),
            "paper": first_paper,
            "evidence": first_evidence,
            # forward-compat extras
            "paper_count": r.get("paper_count", 0),
            "papers_by_conference": rel_pbc,
        })
        if is_outgoing:
            out_count += 1
        else:
            in_count += 1

    return {
        "canonical_name": canon,
        "type": TYPE_SINGULAR[etype],
        "canonical_definition": canon_def,
        "expert_reviewed": False,
        "expert_removed": bool(g.get("expert_removed")),
        "expert_removed_reason": g.get("expert_removed_reason", "") if g.get("expert_removed") else "",
        "names": g.get("original_names") or [canon],
        "papers": papers_flat,
        "paper_count": paper_count,
        "group_ids": [],
        "definitions": build_definitions(g),
        "definition_count": len([d for d in (g.get("original_nodes") or {}).values() if (d.get("definition") or "").strip()]),
        "relationships": rels_for_node,
        "relationship_count": len(rels_for_node),
        "incoming_relationship_count": in_count,
        "outgoing_relationship_count": out_count,
        # Forward-compat fields (ignored by current loader)
        "characterization": "" if is_placeholder else canon_def,
        "characterization_status": "placeholder" if is_placeholder else "llm",
        "papers_by_conference": pbc,
        "paper_count_by_conference": {c: len(v) for c, v in pbc.items()},
        "conferences": sorted(pbc.keys()),
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--input", required=True, help="joint_v*_merged.json or _characterized.json")
    p.add_argument("--site", required=True, help="aiconstructlexis_dev.github.io repo dir")
    p.add_argument("--backup", action="store_true",
                   help="Move existing nomological_network_data/ to .backup-<timestamp>/ before writing")
    args = p.parse_args()

    in_path = Path(args.input)
    site = Path(args.site)
    out_dir = site / "nomological_network_data"

    # Backup existing data dir
    if args.backup and out_dir.exists():
        ts = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup = site / f"nomological_network_data.backup-{ts}"
        shutil.move(str(out_dir), str(backup))
        print(f"Backed up old data to {backup}")

    out_dir.mkdir(parents=True, exist_ok=True)
    for et in SUBDIR:
        d = out_dir / SUBDIR[et]
        if d.exists():
            shutil.rmtree(d)
        d.mkdir(parents=True)

    with open(in_path) as f:
        net = json.load(f)
    print(f"Loaded {in_path}")

    # Build canonical-name → entity-type map (for rel.other_type)
    name_type: Dict[str, str] = {}
    for et in ("constructs", "measurements", "behaviors"):
        for g in net.get(et) or []:
            cn = (g.get("canonical_name") or "").strip()
            if cn:
                name_type[cn] = et

    # Index relationships by canonical name (both endpoints)
    rels_by_canon: Dict[str, List[Dict[str, Any]]] = defaultdict(list)
    for r in net.get("relationships") or []:
        src = (r.get("source") or "").strip()
        tgt = (r.get("target") or "").strip()
        if not src or not tgt:
            continue
        # tag the partner type for both perspectives
        r_for_src = dict(r); r_for_src["_other_type"] = TYPE_PLURAL_FOR_REL.get(name_type.get(tgt, ""), "")
        r_for_tgt = dict(r); r_for_tgt["_other_type"] = TYPE_PLURAL_FOR_REL.get(name_type.get(src, ""), "")
        rels_by_canon[src].append(r_for_src)
        rels_by_canon[tgt].append(r_for_tgt)

    # Write per-entity files
    index = {SUBDIR[et]: [] for et in ("constructs", "measurements", "behaviors")}
    for et in ("constructs", "measurements", "behaviors"):
        for g in (net.get(et) or []):
            rec = build_entity_record(g, et, rels_by_canon)
            slug = slugify(rec["canonical_name"])
            fname = f"{slug}.json"
            with open(out_dir / SUBDIR[et] / fname, "w") as f:
                json.dump(rec, f, indent=2)
            index[SUBDIR[et]].append(fname)
        index[SUBDIR[et]].sort()

    with open(out_dir / "index.json", "w") as f:
        json.dump(index, f, indent=2)

    # Paper-title → URL map (so site can link to PDFs/OpenReview directly
    # instead of falling back to a Google search).
    PAPER_LIST_FILES = [
        "data/iclr_2024_papers.json",
        "data/neurips_2024_papers.json",
        "data/iclr_2025_papers.json",
        "data/naacl_2025_papers.json",
        "data/acl_2025_papers.json",
        "data/icml_2025_papers.json",
        "data/emnlp_2025_papers.json",
    ]
    url_by_title: Dict[str, str] = {}
    repo_root = Path(__file__).resolve().parent.parent
    for f in PAPER_LIST_FILES:
        path = repo_root / f
        if not path.exists():
            continue
        try:
            data = json.load(open(path))
        except Exception:
            continue
        items = list(data.values()) if isinstance(data, dict) else data
        for p in items:
            if not isinstance(p, dict):
                continue
            title = (p.get("name") or p.get("title") or "").strip()
            url = (p.get("url") or p.get("pdf_url") or p.get("openreview_url") or "").strip()
            if title and url and title not in url_by_title:
                url_by_title[title] = url
    url_path = out_dir / "paper_urls.json"
    with open(url_path, "w") as f:
        json.dump(url_by_title, f)
    print(f"  paper_urls.json: {len(url_by_title)} title→URL ({url_path.stat().st_size//1024} KB)")

    # Bundled per-type files for fast site loads (single fetch instead of N).
    # Loader checks for these first and falls back to per-entity if missing.
    for et in ("constructs", "measurements", "behaviors"):
        sub = SUBDIR[et]
        bundle_path = out_dir / f"{sub}.bundle.json"
        records = []
        for fname in index[sub]:
            with open(out_dir / sub / fname) as f:
                records.append(json.load(f))
        with open(bundle_path, "w") as f:
            json.dump(records, f, indent=2)
        print(f"  bundle {sub}.bundle.json: {len(records)} records, {bundle_path.stat().st_size//1024} KB")

    # Graph-only minimal bundle — drops definitions, snippets, papers list,
    # characterization, etc. Network graph only needs name/type/pc/edges, so
    # this is much smaller and renders 5-10× faster.
    graph_nodes = []
    seen_canon = set()
    for et in ("constructs", "measurements", "behaviors"):
        sub = SUBDIR[et]
        sing = TYPE_SINGULAR[et]
        for fname in index[sub]:
            with open(out_dir / sub / fname) as f:
                cfg = json.load(f)
            if cfg.get("expert_removed"):
                continue
            cn = (cfg.get("canonical_name") or "").strip()
            if not cn or cn in seen_canon:
                continue
            seen_canon.add(cn)
            # canonical_definition contains the LLM-synthesized "State of the
            # Field" text — include a trimmed version so graph hovers can show it.
            cd = (cfg.get("canonical_definition") or "").strip()
            graph_nodes.append({
                "name": cn,
                "type": sing,
                "paper_count": cfg.get("paper_count", 0),
                "names": cfg.get("names") or [],
                "definition": cd[:1200],  # cap each tooltip to ~1.2 kB
            })
    # Edges: dedup by (src, tgt, type), restrict to edges where both endpoints
    # are in seen_canon (i.e., not expert_removed).
    graph_edges = []
    seen_edges = set()
    for r in (net.get("relationships") or []):
        s = (r.get("source") or "").strip()
        t = (r.get("target") or "").strip()
        if s not in seen_canon or t not in seen_canon or s == t:
            continue
        rt = (r.get("type") or "").strip()
        key = (s, t, rt)
        if key in seen_edges:
            continue
        seen_edges.add(key)
        graph_edges.append({
            "source": s,
            "target": t,
            "type": rt,
            "paper_count": r.get("paper_count", 0),
        })
    graph_payload = {"nodes": graph_nodes, "edges": graph_edges,
                     "schema_version": 1, "node_count": len(graph_nodes), "edge_count": len(graph_edges)}
    graph_path = out_dir / "graph.bundle.json"
    with open(graph_path, "w") as f:
        json.dump(graph_payload, f, indent=2)
    print(f"  bundle graph.bundle.json: {len(graph_nodes)} nodes, {len(graph_edges)} edges, {graph_path.stat().st_size//1024} KB")

    print(f"Wrote {out_dir}")
    for k, v in index.items():
        print(f"  {k}: {len(v)} files")

    # Sanity: count placeholders
    placeholder_count = 0
    for et in ("constructs", "measurements", "behaviors"):
        for g in (net.get(et) or []):
            if not (g.get("characterization") or "").strip():
                placeholder_count += 1
    print(f"Entities with placeholder canonical_definition (no LLM characterization yet): {placeholder_count}")


if __name__ == "__main__":
    main()
