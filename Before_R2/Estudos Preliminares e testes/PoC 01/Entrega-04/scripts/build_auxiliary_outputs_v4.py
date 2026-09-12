"""Materialise the v4 audit, AI-run and discovery-support tables.

These outputs are deliberately downstream of the append-only JSONL run log.
They provide reviewable CSV views without promoting an AI proposal into the
authoritative candidate or relationship tables.
"""
from __future__ import annotations

import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def read_csv(name: str) -> list[dict]:
    with (DATA / name).open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def write_csv(name: str, fields: list[str], rows: list[dict]) -> None:
    with (DATA / name).open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def load_jsonl() -> list[dict]:
    path = DATA / "ai_runs_v4.jsonl"
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def main() -> None:
    sample = read_csv("audit_sample_v4.csv")
    relationships = read_csv("rit_relationships_v4.csv")
    records = load_jsonl()

    # One current A2 view per held-out unit. Dry-run records remain visible,
    # but are explicitly non-substantive and therefore cannot become AI-only
    # discoveries or authoritative candidates.
    a2_by_unit: dict[str, dict] = {}
    for record in records:
        if record["stage"] == "a2":
            a2_by_unit[record["unit_id"]] = record
    semantic_fields = [
        "semantic_candidate_id", "provision_id", "source_celex", "article",
        "paragraph", "recital", "ai_candidate", "candidate_actor", "candidate_function",
        "candidate_mechanism", "ai_evidence", "additional_context_required",
        "requested_legal_source", "reason", "ai_run_ref", "ai_confidence",
        "abstention_reason", "discovery_source", "human_review_status",
        "output_status",
    ]
    semantic_rows = []
    for row in sample:
        record = a2_by_unit[row["audit_sample_id"]]
        output = record["output"]
        semantic_rows.append({
            "semantic_candidate_id": f"SEM-V4-{row['audit_sample_id']}",
            "provision_id": row["audit_sample_id"],
            "source_celex": row["source_celex"],
            "article": row["article"],
            "paragraph": row.get("paragraph", "NA"),
            "recital": row.get("recital", "NA"),
            "ai_candidate": output.get("ai_candidate", "UNK"),
            "candidate_actor": output.get("candidate_actor") or "NA",
            "candidate_function": output.get("candidate_function") or "NA",
            "candidate_mechanism": output.get("candidate_mechanism", "NA"),
            "ai_evidence": output.get("ai_evidence", "NA"),
            "additional_context_required": str(output.get("additional_context_required", False)),
            "requested_legal_source": output.get("requested_legal_source") or "NA",
            "reason": output.get("reason") or "NA",
            "ai_run_ref": record["run_id"],
            "ai_confidence": output.get("ai_confidence", "low"),
            "abstention_reason": output.get("abstention_reason") or "NA",
            "discovery_source": "LEXICAL",
            "human_review_status": "PENDING_HUMAN",
            "output_status": "DRY_RUN_ONLY" if record["provider"] == "dry_run" else "SUBSTANTIVE_PENDING_HUMAN",
        })
    write_csv("semantic_candidates_v4.csv", semantic_fields, semantic_rows)

    ai_fields = [
        "run_id", "stage", "unit_id", "provider", "model_id", "model_snapshot",
        "reasoning_setting", "prompt_version", "schema_version", "timestamp",
        "input_hash", "output_hash", "input_tokens", "output_tokens", "total_tokens",
        "estimated_usd", "output_status", "output_json",
    ]
    ai_rows = []
    for record in records:
        usage = record.get("usage", {})
        cost = record.get("cost_estimate", {})
        ai_rows.append({
            "run_id": record["run_id"], "stage": record["stage"],
            "unit_id": record["unit_id"], "provider": record["provider"],
            "model_id": record["model_id"], "model_snapshot": record["model_snapshot"],
            "reasoning_setting": record.get("reasoning_setting") or "NA",
            "prompt_version": record["prompt_version"], "schema_version": record["schema_version"],
            "timestamp": record["timestamp"], "input_hash": record["input_hash"],
            "output_hash": record["output_hash"], "input_tokens": usage.get("input_tokens", "NA"),
            "output_tokens": usage.get("output_tokens", "NA"), "total_tokens": usage.get("total_tokens", "NA"),
            "estimated_usd": cost.get("estimated_usd") if cost.get("estimated_usd") is not None else "NA",
            "output_status": "DRY_RUN_ONLY" if record["provider"] == "dry_run" else "SUBSTANTIVE_PENDING_HUMAN",
            "output_json": json.dumps(record["output"], ensure_ascii=False, sort_keys=True),
        })
    write_csv("ai_runs_v4.csv", ai_fields, ai_rows)

    mechanism_fields = [
        "relationship_id", "source_celex", "article", "legal_evidence_id",
        "primary_mechanism", "secondary_mechanism", "mechanism_observability",
        "source_delivery", "ai_assisted", "human_approved",
    ]
    mechanism_rows = []
    for row in relationships:
        mechanism_rows.append({
            "relationship_id": row["relationship_id"], "source_celex": row["source_act"],
            "article": row["article"], "legal_evidence_id": row["legal_evidence_id"],
            "primary_mechanism": row["primary_mechanism"],
            "secondary_mechanism": row.get("secondary_mechanism") or "NA",
            "mechanism_observability": "DIRECT",
            "source_delivery": row["source_delivery"], "ai_assisted": row["ai_assisted"],
            "human_approved": row["human_approved"],
        })
    write_csv("relationship_mechanisms_v4.csv", mechanism_fields, mechanism_rows)

    # Rewrite the review queue with explicit missingness and approval fields.
    review_source = DATA / "human_review_v4.csv"
    review_rows = []
    if review_source.exists():
        review_rows = read_csv("human_review_v4.csv")
    review_fields = ["review_id", "stage", "unit_id", "reason", "review_status",
                     "reviewer", "approved", "reviewed_at"]
    normalised_reviews = []
    for index, row in enumerate(review_rows, start=1):
        normalised_reviews.append({
            "review_id": f"REV-V4-{index:03d}", "stage": row.get("stage", "NA"),
            "unit_id": row.get("unit_id", "NA"), "reason": row.get("reason", "NA"),
            "review_status": "PENDING", "reviewer": "NOT_YET_EXECUTED",
            "approved": "0", "reviewed_at": "NOT_YET_EXECUTED",
        })
    write_csv("human_review_v4.csv", review_fields, normalised_reviews)

    validation_fields = list(sample[0]) + ["sample_type", "validation_status"]
    validation_rows = []
    for row in sample:
        validation_rows.append({**row, "sample_type": "HUMAN_REFERENCE_REQUIRED",
                                "validation_status": "PENDING_HUMAN"})
    write_csv("validation_sample_v4.csv", validation_fields, validation_rows)

    challenge_fields = ["challenge_id", "unit_id", "challenge_type", "why_selected",
                        "human_review_status", "ai_status"]
    challenge_rows = [
        {"challenge_id": "CHAL-01", "unit_id": "AUD-03", "challenge_type": "low_confidence_boundary",
         "why_selected": "Tests whether a low-confidence lexical hit is abstained from rather than promoted.",
         "human_review_status": "PENDING_HUMAN", "ai_status": "DRY_RUN_ONLY"},
        {"challenge_id": "CHAL-02", "unit_id": "AUD-09", "challenge_type": "conditional_climate_case",
         "why_selected": "Preserves the CAND-07 climate-benchmarks boundary as conditional pending legal reconstruction.",
         "human_review_status": "PENDING_HUMAN", "ai_status": "DRY_RUN_ONLY"},
        {"challenge_id": "CHAL-03", "unit_id": "AUD-13", "challenge_type": "taxonomy_discriminant",
         "why_selected": "Tests whether Taxonomy signals are treated as exploratory rather than presumed intermediation.",
         "human_review_status": "PENDING_HUMAN", "ai_status": "DRY_RUN_ONLY"},
        {"challenge_id": "CHAL-04", "unit_id": "RIT-007", "challenge_type": "nested_intermediation",
         "why_selected": "Checks the L2 accreditation/verification chain and parent relationship before role assignment.",
         "human_review_status": "PENDING_HUMAN", "ai_status": "DRY_RUN_ONLY"},
    ]
    write_csv("challenge_sample_v4.csv", challenge_fields, challenge_rows)

    discovery_fields = ["category", "count", "status", "interpretation"]
    discovery_rows = [
        {"category": "LEXICAL_ONLY", "count": "20", "status": "OBSERVED_SAMPLE", "interpretation": "All held-out units were selected from A1 hits; no substantive A2 pass was executed."},
        {"category": "BOTH", "count": "0", "status": "NOT_MEASURED", "interpretation": "Requires substantive A2 outputs on the same provision set."},
        {"category": "SEMANTIC_AI_ONLY", "count": "0", "status": "NOT_MEASURED", "interpretation": "Dry-run placeholders cannot establish AI-only discovery."},
        {"category": "HUMAN", "count": "0", "status": "NOT_MEASURED", "interpretation": "No new human discovery adjudication has been completed."},
        {"category": "A1_TOTAL", "count": "1092", "status": "OBSERVED", "interpretation": "Full lexical screening total across the five-act PoC corpus."},
    ]
    write_csv("candidate_discovery_summary_v4.csv", discovery_fields, discovery_rows)
    print("Wrote auxiliary v4 CSV views from the append-only AI log.")


if __name__ == "__main__":
    main()
