"""Collect the five CELEX acts for PoC 01 and write a reproducibility manifest.

The collector never overwrites Entrega-02/Entrega-03. It stores the exact
EUR-Lex HTML response used by Entrega-04 and records the response hash,
collection timestamp, URL and byte count in both CSV and JSON manifests.
"""
from __future__ import annotations

import csv
import hashlib
import json
import re
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw_html"
DATA_DIR = ROOT / "data"
HEADERS = {"User-Agent": "Mozilla/5.0 (academic research PoC; non-commercial)"}

ACTS = {
    "csrd": {
        "celex": "32022L2464",
        "title": "Directive (EU) 2022/2464 (Corporate Sustainability Reporting Directive)",
        "type": "Directive",
    },
    "ecolabel": {
        "celex": "32010R0066",
        "title": "Regulation (EC) No 66/2010 on the EU Ecolabel",
        "type": "Regulation",
    },
    "climate_benchmarks": {
        "celex": "32019R2089",
        "title": "Regulation (EU) 2019/2089 on climate transition benchmarks and Paris-aligned benchmarks",
        "type": "Regulation",
    },
    "ets_verification": {
        "celex": "32018R2067",
        "title": "Commission Implementing Regulation (EU) 2018/2067 on the verification of data and the accreditation of verifiers",
        "type": "Implementing Regulation",
    },
    "taxonomy": {
        "celex": "32020R0852",
        "title": "Regulation (EU) 2020/852 (Taxonomy Regulation)",
        "type": "Regulation",
    },
}


def fetch(celex: str) -> tuple[str, str]:
    url = f"https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:{celex}"
    response = requests.get(url, headers=HEADERS, timeout=60)
    response.raise_for_status()
    response.encoding = response.encoding or "utf-8"
    return url, response.text


def extract_metadata(html: str, fallback_url: str) -> dict:
    """Extract stable document metadata available in the preserved HTML."""
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(html, "html.parser")
    canonical = soup.find("link", rel="canonical")
    eli = (canonical.get("href") if canonical else fallback_url).removesuffix("/eng")
    title_nodes = soup.select(".eli-main-title .oj-doc-ti")
    date_text = title_nodes[1].get_text(" ", strip=True) if len(title_nodes) > 1 else ""
    date_text = re.sub(r"\s+", " ", date_text.replace("\xa0", " ")).strip()
    match = re.search(r"of\s+(\d{1,2}\s+\w+\s+\d{4})", date_text, flags=re.I)
    document_date = ""
    if match:
        try:
            document_date = datetime.strptime(match.group(1), "%d %B %Y").date().isoformat()
        except ValueError:
            document_date = match.group(1)
    return {
        "eli": eli,
        "document_date": document_date or "NOT_EXTRACTED",
        "entry_into_force": "NOT_EXTRACTED_FROM_HTML_ENDPOINT",
        "legal_status": "NOT_ASSESSED_IN_POC",
        "consolidated_version": "0 (original OJ HTML record)",
        "act_title": " ".join(node.get_text(" ", strip=True) for node in title_nodes),
    }


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    collected_at = datetime.now(timezone.utc).isoformat()
    manifest = []

    for slug, act in ACTS.items():
        url, html = fetch(act["celex"])
        encoded = html.encode("utf-8")
        digest = hashlib.sha256(encoded).hexdigest()
        path = RAW_DIR / f"{slug}_raw.html"
        path.write_bytes(encoded)
        metadata = extract_metadata(html, url)
        row = {
            "slug": slug,
            "celex": act["celex"],
            "base_celex": act["celex"],
            "version_celex": act["celex"],
            "eli": metadata["eli"],
            "title": act["title"],
            "act_title": metadata["act_title"] or act["title"],
            "act_type": act["type"],
            "document_date": metadata["document_date"],
            "entry_into_force": metadata["entry_into_force"],
            "legal_status": metadata["legal_status"],
            "consolidated_version": metadata["consolidated_version"],
            "retrieval_date": collected_at[:10],
            "language": "EN",
            "url": url,
            "source_url": url,
            "version": "EUR-Lex original OJ HTML text served at collection time",
            "collected_at_utc": collected_at,
            "sha256": digest,
            "bytes": len(encoded),
            "file_name": path.name,
            "relative_path": f"data/raw_html/{path.name}",
        }
        manifest.append(row)
        print(f"{slug}: {len(encoded):,} bytes sha256={digest}")
        time.sleep(1)

    fields = list(manifest[0])
    with (DATA_DIR / "CELEX_MANIFEST_v4.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(manifest)
    (DATA_DIR / "CELEX_MANIFEST_v4.json").write_text(
        json.dumps({"manifest_version": "v4", "acts": manifest}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Manifest written for {len(manifest)} CELEX acts.")


if __name__ == "__main__":
    main()
