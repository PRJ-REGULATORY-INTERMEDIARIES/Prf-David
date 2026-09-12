"""Build full-article legal context packages from Entrega-04's local corpus."""
from __future__ import annotations

import re
import unicodedata
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
RAW_DIR = ROOT / "data" / "raw_html"
SLUG_TO_CELEX = {
    "csrd": "32022L2464",
    "ecolabel": "32010R0066",
    "climate_benchmarks": "32019R2089",
    "ets_verification": "32018R2067",
    "taxonomy": "32020R0852",
}
SLUG_TO_FILE = {slug: f"{slug}_raw.html" for slug in SLUG_TO_CELEX}
ARTICLE_CLASS = "oj-ti-art"
BODY_CLASSES = {"oj-normal", "oj-sti-art"}


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def article_token(article_label: str) -> str:
    match = re.search(r"Article\s?\d+[a-z]?", article_label, flags=re.I)
    if not match:
        raise ValueError(f"No article token found in {article_label!r}")
    return match.group(0)


def extract_full_article(slug: str, article_label: str) -> dict:
    path = RAW_DIR / SLUG_TO_FILE[slug]
    if not path.exists():
        raise FileNotFoundError(path)
    target = article_token(article_label) if article_label else "PREAMBLE"
    soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    paragraphs = []
    matched_label = "Preamble" if target == "PREAMBLE" else None
    capturing = target == "PREAMBLE"
    for node in soup.find_all("p"):
        classes = set(node.get("class") or [])
        text = normalize(node.get_text())
        if not text:
            continue
        if ARTICLE_CLASS in classes:
            if capturing:
                if target == "PREAMBLE":
                    break
                break
            if target.lower() in text.lower():
                capturing = True
                matched_label = text
                paragraphs.append(text)
            continue
        if capturing and classes & BODY_CLASSES:
            paragraphs.append(text)
    if not capturing:
        raise ValueError(f"No article matching {target!r} in {slug}")
    full_text = "\n".join(paragraphs)
    refs = sorted(set(re.findall(r"Article\s?\d+[a-z]?", full_text, flags=re.I)) - {target})
    return {
        "slug": slug,
        "celex": SLUG_TO_CELEX[slug],
        "article_token": target,
        "article_label": matched_label,
        "full_text": full_text,
        "paragraph_count": len(paragraphs),
        "same_act_cross_reference_candidates": refs,
    }


def build_package(slug: str, article_label: str) -> dict:
    return extract_full_article(slug, article_label)
