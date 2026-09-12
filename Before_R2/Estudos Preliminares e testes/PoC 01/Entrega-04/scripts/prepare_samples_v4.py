"""Create a deterministic four-per-act held-out sample for human review.

The file is a review queue, not a claim that the selections have been
adjudicated. Historical v3 candidates are excluded by article token so that
the same provision cannot leak into the held-out evaluation set.
"""
from __future__ import annotations

import csv
import random
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCREENING = ROOT / "data" / "screening_hits_v4.csv"
HISTORICAL = ROOT.parent / "Entrega-02" / "data" / "candidate_adjudications_v3.csv"
OUT = ROOT / "data" / "audit_sample_v4.csv"
SEED = 20260906


def token(value: str) -> str:
    match = re.search(r"Article\s?\d+[a-z]?", value, flags=re.I)
    return match.group(0).lower().replace(" ", "") if match else "PREAMBLE"


def main() -> None:
    with SCREENING.open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    with HISTORICAL.open(encoding="utf-8") as handle:
        historical = list(csv.DictReader(handle))
    excluded = defaultdict(set)
    for row in historical:
        excluded[row["source_celex"]].add(token(row["article"]))

    by_act = defaultdict(list)
    for row in rows:
        row["article_token"] = token(row["article"])
        if row["article_token"] not in excluded[row["source_celex"]]:
            by_act[row["source_celex"]].append(row)

    rng = random.Random(SEED)
    selected = []
    for celex in sorted(by_act):
        candidates = by_act[celex]
        by_article = defaultdict(list)
        for row in candidates:
            by_article[row["article_token"]].append(row)
        article_groups = list(by_article.values())
        rng.shuffle(article_groups)
        chosen = []
        chosen_articles = set()
        # Prefer different articles and a mix of high/low lexical confidence.
        for confidence in ("high", "low"):
            for group in article_groups:
                if any(r["screening_confidence"] == confidence for r in group):
                    row = next(r for r in group if r["screening_confidence"] == confidence)
                    if row["article_token"] not in chosen_articles:
                        chosen.append(row)
                        chosen_articles.add(row["article_token"])
                        break
            if len(chosen) >= 4:
                break
        for group in article_groups:
            if len(chosen) >= 4:
                break
            row = group[0]
            if row["article_token"] not in chosen_articles:
                chosen.append(row)
                chosen_articles.add(row["article_token"])
        if len(chosen) < 4:
            raise RuntimeError(f"Only {len(chosen)} held-out units available for {celex}")
        selected.extend(chosen[:4])

    selected.sort(key=lambda r: (r["source_celex"], r["article_token"], r["screening_id"]))
    fields = ["audit_sample_id", "screening_id", "source_celex", "article", "paragraph", "recital", "article_token",
              "provision_type", "candidate_mechanism", "semantic_role", "entity_form", "screening_confidence",
              "matched_keyword", "evidence_text", "selection_seed", "human_review_status",
              "human_relational_test_result", "human_adjudication_note"]
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for index, row in enumerate(selected, start=1):
            writer.writerow({
                "audit_sample_id": f"AUD-{index:02d}",
                "screening_id": row["screening_id"],
                "source_celex": row["source_celex"],
                "article": row["article"],
                "paragraph": row["paragraph"],
                "recital": row["recital"],
                "article_token": row["article_token"],
                "provision_type": row["provision_type"],
                "candidate_mechanism": row["candidate_mechanism"],
                "semantic_role": row["semantic_role"],
                "entity_form": row["entity_form"],
                "screening_confidence": row["screening_confidence"],
                "matched_keyword": row["matched_keyword"],
                "evidence_text": row["evidence_text"],
                "selection_seed": SEED,
                "human_review_status": "PENDING",
                "human_relational_test_result": "PENDING",
                "human_adjudication_note": "NOT_YET_EXECUTED",
            })
    print(f"Wrote {len(selected)} held-out units to {OUT} using seed {SEED}.")


if __name__ == "__main__":
    main()
