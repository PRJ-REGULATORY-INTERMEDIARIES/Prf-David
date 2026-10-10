"""Stage A1 lexical screening for all five CELEX acts in Entrega-04.

This is a versioned extension of Entrega-02/scripts/screening_v3.py. The
ontology remains split into actor, mechanism and instrument hits; a lexical
hit is not itself an adjudicated R-I-T relationship.
"""
from __future__ import annotations

import csv
import re
import unicodedata
from pathlib import Path

from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "data"
RAW_DIR = DATA_DIR / "raw_html"

ACTS = {
    "csrd": "32022L2464",
    "ecolabel": "32010R0066",
    "climate_benchmarks": "32019R2089",
    "ets_verification": "32018R2067",
    "taxonomy": "32020R0852",
}

MECHANISM_RULES = {
    "reporting": {
        "anchor": [
            (r"sustainability reporting", "mechanism"),
            (r"sustainability report\b", "instrument"),
            (r"non-financial (report|statement)", "instrument"),
            (r"reporting (obligation|requirement)s?", "mechanism"),
            (r"management report", "instrument"),
            (r"consolidated (management|sustainability) report", "instrument"),
        ],
        "weak": [(r"\bshall report\b", "mechanism"), (r"\bshall disclose\b", "mechanism"),
                 (r"\bshall publish\b", "mechanism"), (r"\breport\b", "instrument")],
        "exclude": [r"shall present a report to the European Parliament",
                     r"report on the application of this (regulation|directive)",
                     r"review (clause|report) (on|of) this (regulation|directive)"],
    },
    "certification": {
        "anchor": [(r"(competent|accredited) bod(y|ies)", "actor"),
                    (r"conformity assessment (body|bodies)", "actor"),
                    (r"independent assurance services provider", "actor"),
                    (r"national accreditation bod(y|ies)", "actor"),
                    (r"certification (body|bodies)", "actor"),
                    (r"certification scheme", "instrument"),
                    (r"accreditation (process|scheme)", "mechanism"),
                    (r"accreditation body", "actor")],
        "weak": [(r"\bcertificat\w*", "mechanism"), (r"\baccreditation\b", "mechanism"),
                 (r"\baccredited\b", "mechanism")],
        "exclude": [],
    },
    "ranking_rating": {
        "anchor": [(r"benchmark administrator", "actor"), (r"benchmark methodology", "instrument"),
                    (r"credit rating agenc(y|ies)", "actor"), (r"rating agenc(y|ies)", "actor"),
                    (r"EU (Climate Transition|Paris-aligned) Benchmark", "instrument")],
        "weak": [(r"\bbenchmark\w*", "instrument"), (r"\brating\b", "instrument"),
                 (r"\branking\b", "mechanism"), (r"\bscore\b", "instrument")],
        "exclude": [r"shall present a report to the European Parliament",
                     r"review (clause|report) (on|of) this (regulation|directive)"],
    },
    "auditing": {
        "anchor": [(r"statutory auditor", "actor"), (r"audit firm", "actor"),
                    (r"(EU ETS )?(lead )?auditor", "actor"), (r"assurance provider", "actor"),
                    (r"assurance (engagement|opinion|services)", "mechanism"),
                    (r"verification (team|body)", "actor"), (r"verification report", "instrument"),
                    (r"accredited verifier", "actor"), (r"quality assurance review", "mechanism")],
        "weak": [(r"\baudit\w*", "mechanism"), (r"\bassurance\b", "mechanism")],
        "exclude": [r"Court of Auditors"],
    },
}

ARTICLE_CLASS = "oj-ti-art"
SUBTITLE_CLASS = "oj-sti-art"
SECTION_CLASSES = {"oj-ti-section-1", "oj-ti-section-2"}
BODY_CLASSES = {"oj-normal", "oj-sti-art"}
AMENDS_PATTERN = re.compile(r"Amendments? to (Directive|Regulation) \(?[A-Z]*\)?\s*[\d/]+", re.I)


def normalize(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).replace("\xa0", " ")
    return re.sub(r"\s+", " ", text).strip()


def classify(mechanism: str, text: str):
    rules = MECHANISM_RULES[mechanism]
    if any(re.search(pattern, text, re.I) for pattern in rules["exclude"]):
        return None
    for pattern, role in rules["anchor"]:
        match = re.search(pattern, text, re.I)
        if match:
            return "high", pattern, role, match.group(0)
    for pattern, role in rules["weak"]:
        match = re.search(pattern, text, re.I)
        if match:
            return "low", pattern, role, match.group(0)
    return None


def infer_entity_form(semantic_role: str, text: str, keyword: str) -> str:
    """Add an orthogonal form hint; it never replaces semantic_role."""
    if semantic_role != "actor":
        return "NA"
    lower = f"{keyword} {text}".lower()
    if re.search(r"\b(committee|board)\b", lower):
        return "committee"
    if re.search(r"\b(auditor|verifier|testing body|assurance provider|certification body|accreditation body)\b", lower):
        return "professional_body"
    if re.search(r"\b(commission|authority)\b", lower):
        return "public_body"
    if re.search(r"\b(administrator|operator|company|undertaking|investor)\b", lower):
        return "private_organization"
    return "other"


def screen_act(slug: str, celex: str, counter: list[int]) -> list[dict]:
    soup = BeautifulSoup((RAW_DIR / f"{slug}_raw.html").read_text(encoding="utf-8"), "html.parser")
    rows = []
    carrier_article = ""
    carrier_section = ""
    amended_act = ""
    paragraph_number = 0
    for paragraph in soup.find_all("p"):
        classes = set(paragraph.get("class") or [])
        text = normalize(paragraph.get_text())
        if not text:
            continue
        if ARTICLE_CLASS in classes:
            carrier_article = text
            continue
        if classes & SECTION_CLASSES:
            carrier_section = text
            continue
        if SUBTITLE_CLASS in classes and AMENDS_PATTERN.search(text):
            amended_act = text
        if not classes & BODY_CLASSES:
            continue
        paragraph_number += 1
        provision_type = "recital" if not carrier_article else "article"
        for mechanism in MECHANISM_RULES:
            result = classify(mechanism, text)
            if not result:
                continue
            confidence, pattern, role, keyword = result
            counter[0] += 1
            rows.append({
                "screening_id": f"SCR-{counter[0]:05d}", "source_celex": celex,
                "amended_act": amended_act, "article": carrier_article,
                "paragraph": str(paragraph_number),
                "recital": f"PREAMBLE-{paragraph_number}" if provision_type == "recital" else "NA",
                "carrier_section": carrier_section, "provision_type": provision_type,
                "candidate_mechanism": mechanism, "semantic_role": role,
                "entity_form": infer_entity_form(role, text, keyword),
                "matched_pattern": pattern, "matched_keyword": keyword,
                "screening_confidence": confidence, "evidence_text": text[:500],
            })
    return rows


def main() -> None:
    all_rows = []
    counter = [0]
    for slug, celex in ACTS.items():
        rows = screen_act(slug, celex, counter)
        all_rows.extend(rows)
        high = sum(row["screening_confidence"] == "high" for row in rows)
        print(f"{slug}: {len(rows)} hits ({high} high, {len(rows) - high} low)")
    fields = ["screening_id", "source_celex", "amended_act", "article", "paragraph", "recital",
              "carrier_section", "provision_type", "candidate_mechanism", "semantic_role",
              "entity_form", "matched_pattern", "matched_keyword", "screening_confidence",
              "evidence_text"]
    output = DATA_DIR / "screening_hits_v4.csv"
    with output.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(all_rows)
    print(f"Total: {len(all_rows)} lines written to {output}")


if __name__ == "__main__":
    main()
