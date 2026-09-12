#!/usr/bin/env python3
"""
Validation for dataset-eurlex-cleanroom source acquisition + corpus
normalization.

For each case, checks:
  - act_official.xhtml on disk matches the SHA256 recorded in
    source_manifest.yaml (and that manifest matches corpus_manifest.yaml's
    recorded source hash);
  - each derived corpus file (act_full.md, act_operative.md,
    act_recitals.md) on disk matches the SHA256 recorded in
    corpus_manifest.yaml;
  - the article count independently re-derived from the raw XHTML
    ("art_" eli-subdivision ids) matches the count recorded in
    corpus_manifest.yaml, and matches the number of "Article " headings
    actually present in act_operative.md;
  - the annex count independently re-derived from the raw XHTML
    ("anx_" eli-container ids) matches the count recorded in
    corpus_manifest.yaml and the number of "# ANNEX" headings in
    act_operative.md;
  - the recital count independently re-derived from the raw XHTML
    ("rct_" eli-subdivision ids) matches the count recorded in
    corpus_manifest.yaml and the number of recital paragraphs in
    act_recitals.md.

Exits non-zero if any check fails.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

PROJECT_ROOT = Path(__file__).resolve().parent.parent
REGISTRY_PATH = PROJECT_ROOT / "config" / "case_registry.yaml"

ARTICLE_HEADING_RE = re.compile(r"^#{2,6} Article \d+\b", re.MULTILINE)
ANNEX_HEADING_RE = re.compile(r"^# ANNEX\b", re.MULTILINE)
RECITAL_PARA_RE = re.compile(r"^\(\d+\) ", re.MULTILINE)


def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def check(condition: bool, ok_msg: str, fail_msg: str, errors: list) -> None:
    if condition:
        print(f"  [OK]   {ok_msg}")
    else:
        print(f"  [FAIL] {fail_msg}")
        errors.append(fail_msg)


def validate_case(case: dict, errors: list) -> None:
    case_id = case["case_id"]
    print(f"\nValidating {case_id} ({case['celex']}) ...")

    source_dir = PROJECT_ROOT / "cases" / case_id / "source"
    corpus_dir = PROJECT_ROOT / "cases" / case_id / "corpus"

    xhtml_path = source_dir / "act_official.xhtml"
    with open(source_dir / "source_manifest.yaml", encoding="utf-8") as f:
        source_manifest = yaml.safe_load(f)
    with open(corpus_dir / "corpus_manifest.yaml", encoding="utf-8") as f:
        corpus_manifest = yaml.safe_load(f)

    xhtml_bytes = xhtml_path.read_bytes()
    actual_source_hash = sha256_of(xhtml_bytes)
    recorded_source_hash = source_manifest["file"]["sha256"]
    check(
        actual_source_hash == recorded_source_hash,
        f"act_official.xhtml sha256 matches source_manifest.yaml ({actual_source_hash[:12]}...)",
        f"{case_id}: act_official.xhtml sha256 MISMATCH vs source_manifest.yaml",
        errors,
    )
    check(
        corpus_manifest["source"]["sha256"] == recorded_source_hash,
        "corpus_manifest.yaml source hash matches source_manifest.yaml",
        f"{case_id}: corpus_manifest.yaml source hash does not match source_manifest.yaml",
        errors,
    )

    for name, meta in corpus_manifest["derived_files"].items():
        path = corpus_dir / name
        actual = sha256_of(path.read_bytes())
        check(
            actual == meta["sha256"],
            f"{name} sha256 matches corpus_manifest.yaml",
            f"{case_id}: {name} sha256 MISMATCH vs corpus_manifest.yaml",
            errors,
        )

    soup = BeautifulSoup(xhtml_bytes.decode("utf-8"), "lxml-xml")
    n_articles_raw = len(
        {el["id"] for el in soup.find_all("div", id=re.compile(r"^art_\d+$"))}
    )
    n_recitals_raw = len(
        {el["id"] for el in soup.find_all("div", id=re.compile(r"^rct_\d+$"))}
    )
    n_annexes_raw = len(
        {el["id"] for el in soup.find_all("div", id=re.compile(r"^anx_"), class_="eli-container")}
    )

    counts = corpus_manifest["counts"]
    check(
        n_articles_raw == counts["articles"],
        f"article count consistent: raw XHTML={n_articles_raw} manifest={counts['articles']}",
        f"{case_id}: article count MISMATCH raw XHTML={n_articles_raw} vs manifest={counts['articles']}",
        errors,
    )
    check(
        n_recitals_raw == counts["recitals"],
        f"recital count consistent: raw XHTML={n_recitals_raw} manifest={counts['recitals']}",
        f"{case_id}: recital count MISMATCH raw XHTML={n_recitals_raw} vs manifest={counts['recitals']}",
        errors,
    )
    check(
        n_annexes_raw == counts["annexes"],
        f"annex count consistent: raw XHTML={n_annexes_raw} manifest={counts['annexes']}",
        f"{case_id}: annex count MISMATCH raw XHTML={n_annexes_raw} vs manifest={counts['annexes']}",
        errors,
    )

    operative_text = (corpus_dir / "act_operative.md").read_text(encoding="utf-8")
    n_article_headings = len(ARTICLE_HEADING_RE.findall(operative_text))
    n_annex_headings = len(ANNEX_HEADING_RE.findall(operative_text))
    check(
        n_article_headings == counts["articles"],
        f"act_operative.md contains {n_article_headings} 'Article N' headings, matching manifest",
        f"{case_id}: act_operative.md has {n_article_headings} article headings, expected {counts['articles']}",
        errors,
    )
    check(
        n_annex_headings == counts["annexes"],
        f"act_operative.md contains {n_annex_headings} 'ANNEX' headings, matching manifest",
        f"{case_id}: act_operative.md has {n_annex_headings} annex headings, expected {counts['annexes']}",
        errors,
    )

    recitals_text = (corpus_dir / "act_recitals.md").read_text(encoding="utf-8")
    n_recital_paras = len(RECITAL_PARA_RE.findall(recitals_text))
    check(
        n_recital_paras == counts["recitals"],
        f"act_recitals.md contains {n_recital_paras} numbered recital paragraphs, matching manifest",
        f"{case_id}: act_recitals.md has {n_recital_paras} recital paragraphs, expected {counts['recitals']}",
        errors,
    )

    check(
        source_manifest["acquisition"]["resolved_host"]
        in {"publications.europa.eu", "eur-lex.europa.eu"},
        "acquisition resolved to an official EUR-Lex / Publications Office host",
        f"{case_id}: acquisition did NOT resolve to an official host",
        errors,
    )


def main() -> int:
    with open(REGISTRY_PATH, encoding="utf-8") as f:
        registry = yaml.safe_load(f)

    errors: list = []
    for case in registry["cases"]:
        validate_case(case, errors)

    print("\n" + "=" * 60)
    if errors:
        print(f"VALIDATION FAILED — {len(errors)} error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("VALIDATION PASSED — all cases, all checks.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
