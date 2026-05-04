"""
Generate human-readable Markdown configs from per-node JSON config files.

Reads the per-node JSON configs produced by `scripts/export_to_existing_site.py`
(layout: <config-dir>/{constructs,measurements,behaviors_tasks}/<slug>.json)
and the simplified extraction JSON (for paper URLs), then writes one .md file
per node. Production: writes into the `nomological_network_data_readable/`
directory of the deployed site.

Usage:
    python scripts/generate_readable_configs.py \
        --config-dir outputs/sandbox_qwen3_mv/nomological_network_data \
        --extraction 'outputs/sandbox_qwen3_mv/inputs/extraction_*.json' \
        --output-dir outputs/sandbox_qwen3_mv/readable
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Set, Tuple

sys.path.insert(
    0, str(Path(__file__).resolve().parent.parent),
)
from misc.logging_config import setup_logging, get_logger

setup_logging(run_name="readable_configs")
logger = get_logger(__name__)


def load_paper_urls(extraction_paths: List[Path]) -> Dict[str, str]:
    """Build a mapping: paper_title -> URL from extraction JSONs."""
    urls: Dict[str, str] = {}
    for path in extraction_paths:
        if not path.exists():
            continue
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
        for key, val in data.items():
            url = ""
            if isinstance(val, dict):
                url = val.get("url", "")
            if url:
                urls[key] = url
    return urls


def _fmt_type(raw: str) -> str:
    return {
        "construct": "Construct",
        "measurement": "Measurement",
        "behavior_task": "Behavior / Task",
    }.get(raw, raw.replace("_", " ").title())


def _paper_link(title: str, urls: Dict[str, str]) -> str:
    url = urls.get(title, "")
    if url:
        return f"[{title}]({url})"
    return title


def _rel_type_label(t: str) -> str:
    return t if t else "related"


def _collect_all_papers(node: Dict[str, Any]) -> Set[str]:
    """Collect all papers from definitions + relationships."""
    papers: Set[str] = set()
    for p in node.get("papers", []):
        papers.add(p)
    for d in node.get("definitions", []):
        if d.get("paper"):
            papers.add(d["paper"])
    for r in node.get("relationships", []):
        if r.get("paper"):
            papers.add(r["paper"])
        for p in r.get("papers", []):
            papers.add(p)
    return papers


def _merge_relationships(rels: List[Dict[str, Any]], name: str) -> List[Dict[str, Any]]:
    """Merge relationships, deduplicating symmetric 'related' pairs."""
    seen_related: Dict[str, Dict[str, Any]] = {}
    directional: List[Dict[str, Any]] = []

    for r in rels:
        other = r.get("other_canonical_name", "?")
        rtype = _rel_type_label(r.get("relationship_type", ""))
        direction = r.get("direction", "outgoing")
        evidence = r.get("evidence", "")
        papers_list = r.get("papers", [])
        paper_single = r.get("paper", "")
        otype = r.get("other_type", "")

        if rtype == "related":
            pair_key = tuple(sorted([name.lower(), other.lower()]))
            key = f"{pair_key[0]}||{pair_key[1]}"

            if key not in seen_related:
                seen_related[key] = {
                    "other_canonical_name": other,
                    "other_type": otype,
                    "relationship_type": "related",
                    "evidence_list": [],
                    "all_papers": set(),
                }

            entry = seen_related[key]
            if evidence and evidence not in entry["evidence_list"]:
                entry["evidence_list"].append(evidence)
            if paper_single:
                entry["all_papers"].add(paper_single)
            for p in papers_list:
                entry["all_papers"].add(p)
        else:
            directional.append(r)

    merged: List[Dict[str, Any]] = []

    for r in directional:
        merged.append(r)

    for entry in seen_related.values():
        merged.append({
            "other_canonical_name": entry["other_canonical_name"],
            "other_type": entry["other_type"],
            "relationship_type": entry["relationship_type"],
            "evidence_list": entry["evidence_list"],
            "papers": sorted(entry["all_papers"]),
            "_merged": True,
        })

    return merged


def render_node(node: Dict[str, Any], urls: Dict[str, str]) -> str:
    """Render a single node config dict as Markdown."""
    lines: List[str] = []
    name = node.get("canonical_name", "Unnamed")
    ntype = _fmt_type(node.get("type", ""))

    all_papers = _collect_all_papers(node)

    lines.append(f"# {name}")
    lines.append(f"**Type:** {ntype}  ")
    lines.append(f"**Referenced in:** {len(all_papers)} paper{'s' if len(all_papers) != 1 else ''}  ")

    names = node.get("names", [])
    aliases = [n for n in names if n != name]
    if aliases:
        lines.append(f"**Also known as:** {', '.join(aliases)}  ")

    characterization = node.get("characterization", "")
    if characterization:
        lines.append("")
        lines.append("## State of the Field")
        lines.append("")
        lines.append(characterization)

    defs = node.get("definitions", [])
    if defs:
        lines.append("")
        lines.append("## Sources")
        for d in defs:
            text = d.get("text", "")
            paper = d.get("paper", "")
            snippets = d.get("source_snippets", [])
            orig_name = d.get("original_name") or ""

            paper_str = _paper_link(paper, urls) if paper else ""
            header_parts = []
            if paper_str:
                header_parts.append(paper_str)
            if orig_name and orig_name != name:
                header_parts.append(f'(as "{orig_name}")')

            lines.append("")
            if header_parts:
                lines.append(f"**{' '.join(header_parts)}**")
            if text:
                lines.append(f"> {text}")
            if snippets:
                for s in snippets:
                    lines.append(f"> *\"{s}\"*")

    rels = node.get("relationships", [])
    if rels:
        merged = _merge_relationships(rels, name)

        outgoing = [r for r in merged if not r.get("_merged") and r.get("direction") == "outgoing"]
        incoming = [r for r in merged if not r.get("_merged") and r.get("direction") == "incoming"]
        related_merged = [r for r in merged if r.get("_merged")]

        has_any = outgoing or incoming or related_merged
        if has_any:
            lines.append("")
            lines.append("## Relationships")

        if outgoing:
            lines.append("")
            lines.append(f"### {name} →")
            for r in outgoing:
                other = r.get("other_canonical_name", "?")
                otype = r.get("other_type", "").replace("_", " ")
                rtype = _rel_type_label(r.get("relationship_type", ""))
                evidence = r.get("evidence", "")
                papers_list = r.get("papers", [])
                paper_single = r.get("paper", "")

                source_links = []
                if paper_single:
                    source_links.append(_paper_link(paper_single, urls))
                elif papers_list:
                    source_links = [_paper_link(p, urls) for p in papers_list]

                lines.append(f"- **{other}** ({otype}) — *{rtype}*")
                if evidence:
                    lines.append(f"  > {evidence}")
                if source_links:
                    lines.append(f"  - {', '.join(source_links)}")

        if incoming:
            lines.append("")
            lines.append(f"### → {name}")
            for r in incoming:
                other = r.get("other_canonical_name", "?")
                otype = r.get("other_type", "").replace("_", " ")
                rtype = _rel_type_label(r.get("relationship_type", ""))
                evidence = r.get("evidence", "")
                papers_list = r.get("papers", [])
                paper_single = r.get("paper", "")

                source_links = []
                if paper_single:
                    source_links.append(_paper_link(paper_single, urls))
                elif papers_list:
                    source_links = [_paper_link(p, urls) for p in papers_list]

                lines.append(f"- **{other}** ({otype}) — *{rtype}*")
                if evidence:
                    lines.append(f"  > {evidence}")
                if source_links:
                    lines.append(f"  - {', '.join(source_links)}")

        if related_merged:
            lines.append("")
            lines.append("### Associated with")
            for r in related_merged:
                other = r["other_canonical_name"]
                otype = r.get("other_type", "").replace("_", " ")
                evidence_list = r.get("evidence_list", [])
                papers_list = r.get("papers", [])

                source_links = [_paper_link(p, urls) for p in papers_list]

                lines.append(f"- **{other}** ({otype})")
                for ev in evidence_list:
                    lines.append(f"  > {ev}")
                if source_links:
                    lines.append(f"  - {', '.join(source_links)}")

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate human-readable Markdown from per-node JSON configs."
    )
    parser.add_argument(
        "--config-dir", type=Path, required=True,
        help="Directory containing JSON config subdirs (constructs/, measurements/, behaviors_tasks/)",
    )
    parser.add_argument(
        "--extraction", type=str, nargs="+", default=[],
        help="Simplified extraction JSON(s) to pull paper URLs from (supports globs)",
    )
    parser.add_argument(
        "--output-dir", type=Path, required=True,
        help="Output directory for readable .md files",
    )
    args = parser.parse_args()

    import glob as globmod
    extraction_paths: List[Path] = []
    for pattern in args.extraction:
        matches = globmod.glob(str(pattern))
        extraction_paths.extend(Path(m) for m in matches)

    urls = load_paper_urls(extraction_paths)
    logger.info("Loaded URLs for %d papers", len(urls))

    config_dir: Path = args.config_dir
    output_dir: Path = args.output_dir
    total = 0

    for subdir in ("constructs", "measurements", "behaviors_tasks"):
        src = config_dir / subdir
        if not src.exists():
            continue
        dst = output_dir / subdir
        dst.mkdir(parents=True, exist_ok=True)

        for json_file in sorted(src.glob("*.json")):
            with json_file.open("r", encoding="utf-8") as f:
                node = json.load(f)
            md_text = render_node(node, urls)
            md_path = dst / f"{json_file.stem}.md"
            md_path.write_text(md_text, encoding="utf-8")
            total += 1

    logger.info("Generated %d readable Markdown files in %s", total, output_dir)


if __name__ == "__main__":
    main()
