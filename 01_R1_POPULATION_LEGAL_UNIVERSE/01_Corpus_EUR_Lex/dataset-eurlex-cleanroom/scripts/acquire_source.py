#!/usr/bin/env python3
"""
Source acquisition for dataset-eurlex-cleanroom.

Downloads the official Official Journal XHTML rendition of each act listed
in config/case_registry.yaml directly from the EUR-Lex / Publications
Office CELLAR repository (content negotiation on the CELEX identifier),
and writes act_official.xhtml + source_manifest.yaml per case.

Refuses to proceed if the resolved response is not an official EUR-Lex /
Publications Office XHTML document (per project rule: "Stop if acquisition
is not from the official EUR-Lex source.").
"""

from __future__ import annotations

import hashlib
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

import yaml

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = PROJECT_ROOT / "config" / "case_registry.yaml"

ALLOWED_HOSTS = {"publications.europa.eu", "eur-lex.europa.eu"}
ENDPOINT_PATTERN = "http://publications.europa.eu/resource/celex/{celex}"
REQUEST_HEADERS = {
    "Accept": "application/xhtml+xml",
    "Accept-Language": "eng",
    "User-Agent": "dataset-eurlex-cleanroom/1.0 (academic research; official-source acquisition)",
}


def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_registry() -> dict:
    with open(REGISTRY_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def acquire_case(case: dict) -> dict:
    celex = case["celex"]
    case_id = case["case_id"]
    url = ENDPOINT_PATTERN.format(celex=celex)

    req = urllib.request.Request(url, headers=REQUEST_HEADERS)
    opener = urllib.request.build_opener()  # follows redirects by default

    with opener.open(req, timeout=60) as resp:
        resolved_url = resp.geturl()
        content_type = resp.headers.get("Content-Type", "")
        body = resp.read()
        status = resp.status

    resolved_host = urlparse(resolved_url).netloc

    if resolved_host not in ALLOWED_HOSTS:
        raise RuntimeError(
            f"[STOP] {case_id}: resolved host '{resolved_host}' is not an "
            f"official EUR-Lex / Publications Office host. Acquisition aborted."
        )
    if "xhtml" not in content_type.lower():
        raise RuntimeError(
            f"[STOP] {case_id}: resolved content-type '{content_type}' is not "
            f"XHTML. Acquisition aborted (official-source rule)."
        )
    if status != 200:
        raise RuntimeError(f"[STOP] {case_id}: HTTP status {status}. Acquisition aborted.")

    case_dir = PROJECT_ROOT / "cases" / case_id / "source"
    case_dir.mkdir(parents=True, exist_ok=True)

    out_file = case_dir / "act_official.xhtml"
    out_file.write_bytes(body)

    digest = sha256_of(body)
    acquired_at = datetime.now(timezone.utc).isoformat(timespec="seconds")

    manifest = {
        "case_id": case_id,
        "celex": celex,
        "official_title": case["official_title"],
        "language": case["language"],
        "acquisition": {
            "requested_url": url,
            "resolved_url": resolved_url,
            "resolved_host": resolved_host,
            "content_type": content_type,
            "http_status": status,
            "acquisition_timestamp_utc": acquired_at,
            "request_headers": REQUEST_HEADERS,
        },
        "file": {
            "name": "act_official.xhtml",
            "byte_size": len(body),
            "sha256": digest,
        },
        "source_authority": "EUR-Lex / Publications Office of the European Union (CELLAR)",
        "acquisition_method": "content_negotiation_on_celex_identifier",
    }

    manifest_file = case_dir / "source_manifest.yaml"
    with open(manifest_file, "w", encoding="utf-8") as f:
        yaml.safe_dump(manifest, f, sort_keys=False, allow_unicode=True)

    return manifest


def main() -> int:
    registry = load_registry()
    results = []
    for case in registry["cases"]:
        print(f"Acquiring {case['case_id']} ({case['celex']}) ...")
        try:
            manifest = acquire_case(case)
        except Exception as exc:  # noqa: BLE001 - top-level acquisition guard
            print(str(exc), file=sys.stderr)
            return 1
        print(
            f"  OK  bytes={manifest['file']['byte_size']}  "
            f"sha256={manifest['file']['sha256']}"
        )
        print(f"  resolved -> {manifest['acquisition']['resolved_url']}")
        results.append(manifest)

    print("\nAll sources acquired from official EUR-Lex / Publications Office CELLAR.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
