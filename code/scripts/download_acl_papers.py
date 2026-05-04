"""
Download main-conference papers from ACL Anthology venues.

Targets only the primary proceedings volume (e.g., acl-long, emnlp-main, naacl-long)
and skips findings, workshops, and short papers.

Usage:
    python scripts/download_acl_papers.py --venue acl --year 2024
    python scripts/download_acl_papers.py --venue emnlp --year 2024
    python scripts/download_acl_papers.py --venue naacl --year 2024
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from bs4 import BeautifulSoup
from tqdm.auto import tqdm

ROOT = Path(__file__).resolve().parent.parent

VOLUME_MAP = {
    "acl": "{year}.acl-long",
    "emnlp": "{year}.emnlp-main",
    "naacl": "{year}.naacl-long",
}

BASE_URL = "https://aclanthology.org"


def _list_papers(venue: str, year: int) -> list[dict]:
    vol_id = VOLUME_MAP[venue].format(year=year)
    vol_url = f"{BASE_URL}/volumes/{vol_id}/"
    print(f"Fetching: {vol_url}")

    r = requests.get(vol_url, timeout=30)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")

    pdf_pattern = re.compile(
        rf"https://aclanthology\.org/({re.escape(vol_id)}\.(\d+))\.pdf"
    )

    papers = []
    seen = set()
    for a in soup.find_all("a", href=True):
        m = pdf_pattern.match(a["href"])
        if not m or m.group(1) in seen:
            continue
        paper_id = m.group(1)
        num = int(m.group(2))
        if num == 0:
            continue
        seen.add(paper_id)

        strong = a.find_previous("strong")
        title = strong.get_text(strip=True) if strong else paper_id

        papers.append({
            "name": title,
            "url": a["href"],
            "paper_id": paper_id,
        })

    return papers


def _download_one(paper: dict, out_dir: Path) -> tuple[str, bool, str]:
    safe_name = re.sub(r"[^\w\s-]", "", paper["name"])[:120].strip()
    safe_name = re.sub(r"\s+", "_", safe_name)
    filepath = out_dir / f"{safe_name}.pdf"
    paper["path"] = str(filepath)

    if filepath.exists() and filepath.stat().st_size > 1000:
        return paper["name"], True, "exists"

    try:
        r = requests.get(paper["url"], timeout=60)
        r.raise_for_status()
        filepath.write_bytes(r.content)
        return paper["name"], True, "ok"
    except Exception as e:
        return paper["name"], False, str(e)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--venue", required=True, choices=["acl", "emnlp", "naacl"])
    parser.add_argument("--year", required=True, type=int)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()

    out_dir = ROOT / "data" / f"{args.venue}_{args.year}_papers"
    out_dir.mkdir(parents=True, exist_ok=True)
    json_path = ROOT / "data" / f"{args.venue}_{args.year}_papers.json"

    print(f"Listing papers for {args.venue.upper()} {args.year}...")
    papers = _list_papers(args.venue, args.year)
    print(f"Found {len(papers)} papers")

    if not papers:
        print("No papers found. Exiting.")
        return

    ok, fail = 0, 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(_download_one, p, out_dir): p for p in papers}
        for fut in tqdm(as_completed(futures), total=len(futures), unit="paper", desc="Downloading"):
            name, success, msg = fut.result()
            if success:
                ok += 1
            else:
                fail += 1
                tqdm.write(f"FAIL: {name[:60]}: {msg}")

    json_path.write_text(json.dumps(papers, indent=2, ensure_ascii=False))
    print(f"\nDone: {ok} downloaded, {fail} failed")
    print(f"Metadata: {json_path}")
    print(f"PDFs: {out_dir}")


if __name__ == "__main__":
    main()
