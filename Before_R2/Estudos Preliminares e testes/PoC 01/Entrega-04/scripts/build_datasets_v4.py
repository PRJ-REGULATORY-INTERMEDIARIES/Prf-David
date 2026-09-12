"""Build versioned v4 datasets without promoting any AI proposal.

The seven human-confirmed relationships and ten historical adjudications are
copied as a regression baseline. The twenty new held-out units remain
explicitly pending human adjudication; they are never written to the
positive-relationship table merely because a lexical hit exists.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
V3 = ROOT.parent / "Entrega-02" / "data"
DATA = ROOT / "data"


def read(name: str) -> list[dict]:
    with (V3 / name).open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write(name: str, fields: list[str], rows: list[dict]) -> None:
    with (DATA / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def main() -> None:
    historical_candidates = read("candidate_adjudications_v3.csv")
    sample = []
    with (DATA / "audit_sample_v4.csv").open(encoding="utf-8") as handle:
        sample = list(csv.DictReader(handle))

    candidate_fields = [
        "candidate_id", "audit_sample_id", "screening_ids", "source_celex", "article",
        "candidate_actor", "candidate_relationship_description", "relational_test_result",
        "construct_validity", "inclusion_decision", "exclusion_reason",
        "resulting_relationship_id", "coder", "coding_date", "adjudication_note",
        "human_review_status", "ai_assisted", "ai_run_ref", "discovery_source",
    ]
    candidates = []
    for row in historical_candidates:
        candidates.append({
            **row, "audit_sample_id": "NA", "human_review_status": "COMPLETE_FROM_ENTREGA_02",
            "resulting_relationship_id": row["resulting_relationship_id"] or "NA",
            "exclusion_reason": row["exclusion_reason"] or "NA",
            "ai_assisted": "0", "ai_run_ref": "NA", "discovery_source": "LEXICAL",
        })
    for index, row in enumerate(sample, start=1):
        candidates.append({
            "candidate_id": f"CAND-V4-{index:02d}",
            "audit_sample_id": row["audit_sample_id"],
            "screening_ids": row["screening_id"],
            "source_celex": row["source_celex"],
            "article": row["article"],
            "candidate_actor": "PENDING",
            "candidate_relationship_description": "PENDING",
            "relational_test_result": "PENDING",
            "construct_validity": "PENDING",
            "inclusion_decision": "PENDING",
            "exclusion_reason": "NA",
            "resulting_relationship_id": "NA",
            "coder": "NOT_YET_EXECUTED",
            "coding_date": "NOT_YET_EXECUTED",
            "adjudication_note": "Held-out unit; independent human adjudication required before any Tier 1 AI run.",
            "human_review_status": "PENDING_HUMAN",
            "ai_assisted": "0",
            "ai_run_ref": "NA",
            "discovery_source": "LEXICAL",
        })
    write("candidate_adjudications_v4.csv", candidate_fields, candidates)

    actor_fields = ["actor_id", "actor_label", "actor_type_hint",
                    "public_private_hybrid", "jurisdiction", "role_scope"]
    actors = [{
        "actor_id": row["actor_id"], "actor_label": row["actor_label"],
        "actor_type_hint": row["actor_type"],
        "public_private_hybrid": row["public_private_hybrid"],
        "jurisdiction": row["jurisdiction"],
        "role_scope": "relationship-specific inherited reference; not an intrinsic actor type",
    } for row in read("actors_v3.csv")]
    write("actors_v4.csv", actor_fields, actors)

    relationship_fields = list(read("rit_relationships_v3.csv")[0]) + [
        "source_delivery", "ai_assisted", "ai_run_ref",
        "rule_source_id", "standard_setter_id", "direct_regulator_id",
        "oversight_authority_id", "enforcement_authority_id",
        "nested_intermediation_present", "meta_regulatory_relation",
        "interpretation_note", "human_approved",
        "motivation", "centrality", "responsibilization_present",
        "empowerment_present"
    ]
    relationships = []
    for row in read("rit_relationships_v3.csv"):
        clean = {
            key: ("NA" if value in (None, "") and key != "verbatim_evidence" else value)
            for key, value in row.items()
        }
        is_nested = clean["intermediation_level"] == "L2"
        relationships.append({
            **clean,
            "source_delivery": "Entrega-02 human-validated regression baseline",
            "ai_assisted": "0", "ai_run_ref": "NA",
            # These role distinctions are intentionally left unknown in the
            # inherited baseline unless the v3 evidence explicitly supports
            # them. R/I/T labels are relational, not intrinsic actor types.
            "rule_source_id": "UNK",
            "standard_setter_id": "UNK",
            "direct_regulator_id": "UNK",
            "oversight_authority_id": "UNK",
            "enforcement_authority_id": "UNK",
            "nested_intermediation_present": "1" if is_nested else "0",
            "meta_regulatory_relation": "1" if is_nested else "0",
            "interpretation_note": (
                "L2 row has a parent relationship in the inherited v3 chain; "
                "the nested governance interpretation remains bounded to that "
                "documented chain and requires human confirmation in any new run."
                if is_nested else
                "L1 relationship preserved from the inherited human-validated baseline; "
                "no nested governance relation is asserted."
            ),
            "human_approved": "1",
            # These variables are part of the conceptual design but are not
            # observable from the inherited legal rows without a dedicated
            # coding pass. NOE is intentional and prevents a deferred field
            # from being mistaken for a measured attribute.
            "motivation": "NOE",
            "centrality": "NOE",
            "responsibilization_present": "NOE",
            "empowerment_present": "NOE",
        })
    write("rit_relationships_v4.csv", relationship_fields, relationships)
    print(f"candidate_adjudications_v4.csv: {len(candidates)} rows ({len(sample)} pending held-out)")
    print(f"actors_v4.csv: {len(actors)} rows")
    print(f"rit_relationships_v4.csv: {len(relationships)} rows (all regression baseline)")


if __name__ == "__main__":
    main()
