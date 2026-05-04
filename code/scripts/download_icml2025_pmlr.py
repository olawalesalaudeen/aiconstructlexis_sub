"""
One-off ICML 2025 downloader using PMLR Volume 267.

Why this script exists: the generic auto-detect in scripts/download_papers.py
failed to map (icml, 2025) to v267 (the homepage scraper's regex didn't catch
the link text). Rather than redoing the auto-detect heuristic, we hard-code
v267 here. PDFs are hosted on raw.githubusercontent.com (no rate limiting,
unlike OpenReview which throttled the previous attempt).

Output:
- data/icml_2025_papers/<slug>.pdf  for each paper
- data/icml_2025_papers.json        (paper-list metadata: name, url, path)
"""

from __future__ import annotations

import argparse
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from tqdm.auto import tqdm

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PDF_DIR = DATA / "icml_2025_papers"
META_PATH = DATA / "icml_2025_papers.json"

PMLR_VOLUME = 267
PMLR_INDEX_URL = f"https://proceedings.mlr.press/v{PMLR_VOLUME}/"


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.ASCII)
    return re.sub(r"[-\s]+", "_", text.strip())[:120]


def list_pmlr_v267() -> list[tuple[str, str]]:
    """Return [(title, pdf_url), ...] for every paper in PMLR v267."""
    r = requests.get(PMLR_INDEX_URL, timeout=60,
                     headers={"User-Agent": "Mozilla/5.0"})
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    pairs = []
    for div in soup.select("div.paper"):
        title_el = div.select_one("p.title")
        pdf_el = div.select_one("p.links a[href$='.pdf']")
        if not (title_el and pdf_el):
            continue
        title = title_el.get_text(strip=True)
        pdf = pdf_el["href"]
        if not pdf.startswith("http"):
            pdf = f"https://proceedings.mlr.press{pdf}"
        pairs.append((title, pdf))
    return pairs


def download_one(title: str, url: str, dest_dir: Path,
                 session: requests.Session, retries: int = 3) -> tuple[str, str, bool]:
    """Download a single PDF. Returns (title, path_or_error, success)."""
    path = dest_dir / f"{slugify(title)}.pdf"
    if path.exists() and path.stat().st_size > 1024:
        return title, str(path), True
    last_err = ""
    for attempt in range(retries):
        try:
            r = session.get(url, timeout=60, stream=True,
                            headers={"User-Agent": "Mozilla/5.0"})
            r.raise_for_status()
            with open(path, "wb") as f:
                for chunk in r.iter_content(8192):
                    if chunk:
                        f.write(chunk)
            return title, str(path), True
        except Exception as e:
            last_err = str(e)[:200]
            time.sleep(0.5 * (attempt + 1))
    return title, last_err, False


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--metadata-only", action="store_true",
                    help="Skip PDF download; just write JSON.")
    ap.add_argument("--max-workers", type=int, default=12)
    args = ap.parse_args()

    PDF_DIR.mkdir(parents=True, exist_ok=True)

    print(f"Fetching PMLR v{PMLR_VOLUME} index...")
    pairs = list_pmlr_v267()
    print(f"Found {len(pairs)} papers in PMLR v{PMLR_VOLUME}")

    if not args.metadata_only:
        ok = 0
        fail = []
        with requests.Session() as session, \
             ThreadPoolExecutor(max_workers=args.max_workers) as ex:
            futures = {ex.submit(download_one, t, u, PDF_DIR, session): (t, u)
                       for (t, u) in pairs}
            for fut in tqdm(as_completed(futures), total=len(futures),
                            desc="Downloading PDFs"):
                t, info, success = fut.result()
                if success:
                    ok += 1
                else:
                    fail.append((t, info))
        print(f"Downloaded OK: {ok} / {len(pairs)}")
        if fail:
            print(f"Failed: {len(fail)}")
            for t, err in fail[:10]:
                print(f"  - {t[:60]}: {err}")

    # Build metadata file (matches the schema used by other paper_list JSONs)
    meta = []
    for title, url in pairs:
        path = PDF_DIR / f"{slugify(title)}.pdf"
        meta.append({
            "name": title,
            "url": url,
            "path": str(path),
        })
    META_PATH.write_text(json.dumps(meta, indent=2, ensure_ascii=False))
    print(f"Wrote {META_PATH}  ({len(meta)} entries)")


if __name__ == "__main__":
    main()
