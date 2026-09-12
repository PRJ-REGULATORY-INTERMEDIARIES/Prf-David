"""Assembles the "legal-context package" for Stage B1/B2: the FULL article
(all paragraphs under one carrier article heading), not just the single
paragraph that triggered Stage A screening.

Extends (reuses the same BeautifulSoup parsing logic as) screening_v3.py's
carrier_article tracking - does not reimplement it from scratch.

Cross-act references known to matter for this corpus (the concrete case:
RIT-007 depends on Article 14 of Regulation (EC) No 765/2008, and on
Directive 2006/43/EC's independence regime referenced from the CSRD) are
served from a small local registry (KNOWN_CROSS_ACT_REFS below) so the
context-escape-hatch loop isn't immediately triggered by gaps already known
from the human v3 coding round. New/unanticipated references still go
through scripts/context_request_loop.py.

Usage (dry-run friendly - no network calls, reads already-collected HTML):
    python context_package.py <slug> "<Article label substring>"
"""
import re
import sys
import unicodedata
from pathlib import Path

from bs4 import BeautifulSoup

REFERENCE_DIR = Path(__file__).resolve().parent.parent / "reference" / "data"
RAW_HTML_DIR = REFERENCE_DIR / "raw_html"

ARTICLE_CLASS = "oj-ti-art"
SUBTITLE_CLASS = "oj-sti-art"
BODY_CLASSES = {"oj-normal", "oj-sti-art"}

SLUG_TO_FILE = {
    "csrd": "csrd_raw.html",
    "ecolabel": "ecolabel_raw.html",
    "climate_benchmarks": "climate_benchmarks_raw.html",
    "ets_verification": "ets_verification_raw.html",
}

# Registry of cross-act text known (from the human v3 coding round) to be
# needed for specific candidates. Populated by hand as gaps are found -
# this is deliberately small and explicit, not an automated crawler.
# Structure: {act_label: {"celex": ..., "note": ..., "text": ...}}
KNOWN_CROSS_ACT_REFS = {
    "Regulation (EC) No 765/2008, Article 14": {
        "celex": "32008R0765",
        "note": (
            "Not yet fetched into this registry. RIT-007's human coding "
            "relied on a quotation already present in "
            "../../Entrega-02/CODEBOOK.md's certification anchor examples: "
            "'The body recognised under Article 14 of Regulation (EC) No "
            "765/2008 shall publish and communicate the outcome of the peer "
            "evaluation of a national accreditation [body].' Fetch the full "
            "article via collect.py before running Tier 0/1 units that need "
            "it, and update this registry entry's 'text' field."
        ),
        "text": None,
    },
    "Directive 2006/43/EC (independence regime for statutory auditors)": {
        "celex": "32006L0043",
        "note": (
            "Referenced by CSRD Art. 27a (RIT-001/RIT-002). Not yet fetched "
            "into this registry - fetch via collect.py before relying on "
            "the escape hatch not triggering for this reference."
        ),
        "text": None,
    },
}


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text)
    text = text.replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def extract_full_article(slug: str, article_label_substring: str) -> dict:
    """Returns all paragraphs under the first article whose oj-ti-art text
    contains article_label_substring (e.g. 'Article 27a', 'Article 9').
    Mirrors screening_v3.py's traversal, but collects every paragraph for
    the matched article instead of only ones with a lexical hit."""
    html_path = RAW_HTML_DIR / SLUG_TO_FILE[slug]
    if not html_path.exists():
        raise FileNotFoundError(
            f"{html_path} not found. Copy from ../Entrega-02/data/raw_html/ "
            "or run collect.py for this act."
        )
    soup = BeautifulSoup(html_path.read_text(encoding="utf-8"), "html.parser")

    paragraphs = []
    current_article = None
    capturing = False
    matched_article_label = None

    for p in soup.find_all("p"):
        classes = set(p.get("class") or [])
        text = normalize(p.get_text())
        if not text:
            continue

        if ARTICLE_CLASS in classes:
            if capturing:
                break  # reached the next article - stop
            current_article = text
            if article_label_substring in text:
                capturing = True
                matched_article_label = text
                paragraphs.append(text)
            continue

        if capturing and (classes & BODY_CLASSES):
            paragraphs.append(text)

    if not capturing:
        raise ValueError(
            f"No article matching '{article_label_substring}' found in {slug}."
        )

    return {
        "slug": slug,
        "article_label": matched_article_label,
        "full_text": "\n".join(paragraphs),
        "paragraph_count": len(paragraphs),
    }


def find_same_act_cross_references(full_text: str, article_label_substring: str) -> list:
    """Detects 'Article N' mentions in the extracted text that are NOT the
    matched article itself - candidates for auto-resolution within the same
    HTML file. Returns a de-duplicated list of referenced article labels
    (resolution left to the caller, since a mention is not always load-bearing)."""
    mentions = set(re.findall(r"Article\s?\d+[a-z]?", full_text))
    mentions.discard(article_label_substring)
    return sorted(mentions)


def build_package(slug: str, article_label_substring: str) -> dict:
    core = extract_full_article(slug, article_label_substring)
    cross_refs = find_same_act_cross_references(core["full_text"], article_label_substring)
    return {
        **core,
        "same_act_cross_reference_candidates": cross_refs,
        "known_cross_act_refs_available": {
            k: (v["text"] is not None) for k, v in KNOWN_CROSS_ACT_REFS.items()
        },
    }


def main() -> None:
    if len(sys.argv) != 3:
        print('Uso: python context_package.py <slug> "<Article label substring>"')
        raise SystemExit(1)
    slug, article_label = sys.argv[1], sys.argv[2]
    pkg = build_package(slug, article_label)
    print(f"Matched: {pkg['article_label']} ({pkg['paragraph_count']} paragraphs)")
    print(f"Same-act cross-reference candidates: {pkg['same_act_cross_reference_candidates']}")
    print(f"Known cross-act refs available: {pkg['known_cross_act_refs_available']}")
    print("--- full_text preview (first 500 chars) ---")
    print(pkg["full_text"][:500])


if __name__ == "__main__":
    main()
