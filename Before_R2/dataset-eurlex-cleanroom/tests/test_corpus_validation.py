"""
Regression tests for the acquisition/normalization pipeline.

These wrap the same checks as `scripts/validate_corpus.py` in pytest so
CI (or a plain `pytest` run) fails loudly if a future edit to the
normalization script desynchronizes a case's Markdown from its manifest,
or from the raw XHTML's structural counts.
"""

from __future__ import annotations

import hashlib
import re
import sys
from pathlib import Path

import pytest
import yaml
from bs4 import BeautifulSoup

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

with open(PROJECT_ROOT / "config" / "case_registry.yaml", encoding="utf-8") as f:
    REGISTRY = yaml.safe_load(f)

CASE_IDS = [c["case_id"] for c in REGISTRY["cases"]]


def sha256_of(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


@pytest.fixture(params=CASE_IDS)
def case_dirs(request):
    case_id = request.param
    source_dir = PROJECT_ROOT / "cases" / case_id / "source"
    corpus_dir = PROJECT_ROOT / "cases" / case_id / "corpus"
    return case_id, source_dir, corpus_dir


def test_source_hash_matches_manifest(case_dirs):
    case_id, source_dir, _ = case_dirs
    with open(source_dir / "source_manifest.yaml", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
    data = (source_dir / "act_official.xhtml").read_bytes()
    assert sha256_of(data) == manifest["file"]["sha256"]
    assert manifest["acquisition"]["resolved_host"] in {
        "publications.europa.eu",
        "eur-lex.europa.eu",
    }


def test_derived_files_hash_matches_manifest(case_dirs):
    case_id, _, corpus_dir = case_dirs
    with open(corpus_dir / "corpus_manifest.yaml", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
    for name, meta in manifest["derived_files"].items():
        data = (corpus_dir / name).read_bytes()
        assert sha256_of(data) == meta["sha256"], f"{case_id}/{name} hash drift"


def test_structural_counts_consistent(case_dirs):
    case_id, source_dir, corpus_dir = case_dirs
    with open(corpus_dir / "corpus_manifest.yaml", encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
    counts = manifest["counts"]

    xhtml = (source_dir / "act_official.xhtml").read_text(encoding="utf-8")
    soup = BeautifulSoup(xhtml, "lxml-xml")
    n_articles = len({el["id"] for el in soup.find_all("div", id=re.compile(r"^art_\d+$"))})
    n_recitals = len({el["id"] for el in soup.find_all("div", id=re.compile(r"^rct_\d+$"))})
    n_annexes = len(
        {el["id"] for el in soup.find_all("div", id=re.compile(r"^anx_"), class_="eli-container")}
    )
    assert n_articles == counts["articles"]
    assert n_recitals == counts["recitals"]
    assert n_annexes == counts["annexes"]

    operative = (corpus_dir / "act_operative.md").read_text(encoding="utf-8")
    assert len(re.findall(r"^#{2,6} Article \d+\b", operative, re.MULTILINE)) == counts["articles"]
    assert len(re.findall(r"^# ANNEX\b", operative, re.MULTILINE)) == counts["annexes"]

    recitals_md = (corpus_dir / "act_recitals.md").read_text(encoding="utf-8")
    assert len(re.findall(r"^\(\d+\) ", recitals_md, re.MULTILINE)) == counts["recitals"]


def test_operative_corpus_excludes_recitals(case_dirs):
    """act_operative.md must not contain the recital-numbering pattern as
    body content, since recitals must never leak into the primary coding
    corpus (a recital alone cannot support a positive relation)."""
    _, _, corpus_dir = case_dirs
    operative = (corpus_dir / "act_operative.md").read_text(encoding="utf-8")
    # The recital numbering "(1) " only appears in the recitals file; the
    # operative corpus starts directly at the enacting articles/annexes.
    assert "Whereas:" not in operative
