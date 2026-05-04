#!/usr/bin/env python3
"""Download conference papers from proceedings sites or OpenReview.

Supported sources:
  - proceedings.iclr.cc / proceedings.neurips.cc  (direct scrape)
  - proceedings.mlr.press (PMLR volumes, for ICML/AISTATS/etc.)
  - OpenReview API (fallback when formal proceedings unavailable)

Usage:
  python scripts/download_papers.py --conference iclr --year 2025
  python scripts/download_papers.py --conference icml --year 2025
  python scripts/download_papers.py --conference iclr --year 2025 --metadata-only
"""
from __future__ import annotations

import argparse
import json
import re
import time
from pathlib import Path
from typing import List, Tuple

import requests
from bs4 import BeautifulSoup
from tqdm.auto import tqdm

DATA_ROOT = Path(__file__).resolve().parent.parent / "data"
SLEEP = 0.25


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.ASCII)
    return re.sub(r"[-\s]+", "_", text.strip())[:120]


# ── proceedings.{conf}.cc scraper (ICLR, NeurIPS) ──────────────

def list_proceedings_cc(conf: str, year: int) -> List[Tuple[str, str]]:
    base = f"https://proceedings.{conf}.cc/paper_files/paper/{year}"
    page = BeautifulSoup(
        requests.get(base, timeout=30).text, "html.parser"
    )
    pairs = []
    for a in page.select("a"):
        href = a.get("href", "")
        if f"/paper/{year}/hash/" in href and "-Abstract-" in href:
            title = a.text.strip()
            pdf = (
                f"https://proceedings.{conf}.cc"
                + href.replace("/hash/", "/file/")
                      .replace("-Abstract-", "-Paper-")
                      .replace(".html", ".pdf")
            )
            pairs.append((title, pdf))
    return pairs


# ── PMLR scraper (ICML, AISTATS, etc.) ─────────────────────────

def pmlr_volume_for(conf: str, year: int) -> int | None:
    idx = requests.get("https://proceedings.mlr.press/", timeout=30).text
    soup = BeautifulSoup(idx, "html.parser")
    patt_conf = re.compile(conf, re.I)
    patt_year = re.compile(str(year))
    for li in soup.select("ul.list-unstyled > li"):
        a = li.find("a", href=True)
        if not a:
            continue
        if patt_conf.search(a.text) and patt_year.search(a.text):
            m = re.search(r"/v(\d+)/?$", a["href"])
            if m:
                return int(m.group(1))
    return None


def list_pmlr(conf: str, year: int) -> List[Tuple[str, str]]:
    vol = pmlr_volume_for(conf, year)
    if vol is None:
        return []
    base = f"https://proceedings.mlr.press/v{vol}"
    idx = BeautifulSoup(
        requests.get(base, timeout=30).text, "html.parser"
    )
    pairs = []
    for div in idx.select("div.paper"):
        title_el = div.select_one("p.title")
        pdf_el = div.select_one("p.links a[href$='.pdf']")
        if title_el and pdf_el:
            pairs.append((title_el.text.strip(), pdf_el["href"]))
    return pairs


# ── OpenReview scraper (fallback) ───────────────────────────────

def list_openreview(conf: str, year: int) -> List[Tuple[str, str]]:
    """Use OpenReview API v2 to list accepted papers."""
    import openreview

    venue_map = {
        "icml": f"ICML.cc/{year}/Conference",
        "iclr": f"ICLR.cc/{year}/Conference",
        "neurips": f"NeurIPS.cc/{year}/Conference",
    }
    venue_id = venue_map.get(conf.lower())
    if not venue_id:
        raise ValueError(
            f"Unknown conference '{conf}' for OpenReview. "
            f"Supported: {list(venue_map.keys())}"
        )

    client = openreview.api.OpenReviewClient(
        baseurl="https://api2.openreview.net"
    )

    submissions = client.get_all_notes(
        invitation=f"{venue_id}/-/Submission",
        details="directReplies",
    )
    print(f"  OpenReview: fetched {len(submissions)} submissions")

    accepted = []
    for note in submissions:
        decisions = [
            r for r in (note.details.get("directReplies") or [])
            if "Decision" in (r.get("invitation") or "")
            or "acceptance" in (r.get("invitation") or "").lower()
        ]
        is_accepted = False
        for d in decisions:
            content = d.get("content", {})
            dec_val = content.get("decision", {})
            if isinstance(dec_val, dict):
                dec_val = dec_val.get("value", "")
            if isinstance(dec_val, str) and "accept" in dec_val.lower():
                is_accepted = True
                break

        if not is_accepted:
            venueid = (note.content or {}).get("venueid", {})
            if isinstance(venueid, dict):
                venueid = venueid.get("value", "")
            if isinstance(venueid, str) and "accept" in venueid.lower():
                is_accepted = True

        if not is_accepted:
            venue = (note.content or {}).get("venue", {})
            if isinstance(venue, dict):
                venue = venue.get("value", "")
            if isinstance(venue, str) and (
                "accept" in venue.lower()
                or f"{conf.upper()} {year}" in venue
            ):
                is_accepted = True

        if is_accepted:
            title_field = (note.content or {}).get("title", {})
            if isinstance(title_field, dict):
                title = title_field.get("value", "Untitled")
            else:
                title = str(title_field) if title_field else "Untitled"
            pdf_url = f"https://openreview.net/pdf?id={note.id}"
            accepted.append((title, pdf_url))

    return accepted


# ── main ────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Download conference paper PDFs and create metadata JSON"
    )
    parser.add_argument(
        "--conference", required=True,
        help="neurips, iclr, icml, etc."
    )
    parser.add_argument("--year", type=int, required=True)
    parser.add_argument(
        "--metadata-only", action="store_true",
        help="Create JSON index only, skip PDF download"
    )
    parser.add_argument(
        "--source", choices=["auto", "proceedings", "pmlr", "openreview"],
        default="auto",
        help="Force a specific source (default: auto-detect)"
    )
    args = parser.parse_args()

    conf = args.conference.lower()
    year = args.year
    dest_dir = DATA_ROOT / f"{conf}_{year}_papers"
    dest_dir.mkdir(parents=True, exist_ok=True)
    meta_path = DATA_ROOT / f"{conf}_{year}_papers.json"

    # Resolve paper listing
    papers: List[Tuple[str, str]] = []

    if args.source == "auto":
        if conf in {"neurips", "iclr"}:
            print(f"Trying proceedings.{conf}.cc ...")
            papers = list_proceedings_cc(conf, year)
        if not papers and conf not in {"neurips", "iclr"}:
            print("Trying PMLR ...")
            papers = list_pmlr(conf, year)
        if not papers:
            print("Falling back to OpenReview API ...")
            papers = list_openreview(conf, year)
    elif args.source == "proceedings":
        papers = list_proceedings_cc(conf, year)
    elif args.source == "pmlr":
        papers = list_pmlr(conf, year)
    elif args.source == "openreview":
        papers = list_openreview(conf, year)

    if not papers:
        print(f"ERROR: No papers found for {conf.upper()} {year}")
        return

    print(f"Found {len(papers)} papers for {conf.upper()} {year}")

    # Build metadata
    meta = []
    for title, pdf_url in papers:
        pdf_path = dest_dir / f"{slugify(title)}.pdf"
        meta.append({
            "name": title,
            "url": pdf_url,
            "path": str(pdf_path),
        })

    meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
    print(f"Metadata JSON -> {meta_path}  ({len(meta)} entries)")

    if args.metadata_only:
        print("--metadata-only: skipping PDF download")
        return

    # Download PDFs
    skipped = 0
    failed = 0
    for title, pdf_url in tqdm(papers, unit="paper", desc="Downloading"):
        pdf_path = dest_dir / f"{slugify(title)}.pdf"
        if pdf_path.exists() and pdf_path.stat().st_size > 1000:
            skipped += 1
            continue
        try:
            with requests.get(pdf_url, stream=True, timeout=60) as r:
                r.raise_for_status()
                with open(pdf_path, "wb") as f:
                    for chunk in r.iter_content(8192):
                        f.write(chunk)
        except Exception as e:
            print(f"\n  FAIL {title[:60]}: {e}")
            failed += 1
        time.sleep(SLEEP)

    print(
        f"\nDone! {len(papers)} total, "
        f"{skipped} already existed, {failed} failed"
    )
    print(f"PDFs -> {dest_dir}")


if __name__ == "__main__":
    main()
