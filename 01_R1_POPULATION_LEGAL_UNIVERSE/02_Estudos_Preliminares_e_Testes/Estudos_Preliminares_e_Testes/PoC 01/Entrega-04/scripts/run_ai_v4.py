"""Run the v4 AI stages on the held-out sample or in local dry-run mode.

The default is ``dry_run``. Real calls can be enabled explicitly after the
model/account gate is cleared. No function in this file writes to the v4
candidate or relationship CSVs; it only appends provider outputs to the
run log and creates a human-review queue.
"""
from __future__ import annotations

import argparse
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

import context_package_v4 as context_package
import run_stage
from consistency_check import check_consistency

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SAMPLE = DATA / "audit_sample_v4.csv"
RELATIONSHIPS = DATA / "rit_relationships_v4.csv"
ACTORS = DATA / "actors_v4.csv"
CELEX_TO_SLUG = {v: k for k, v in context_package.SLUG_TO_CELEX.items()}
N_RUNS = 3


def load(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def base_values(row: dict, package: dict) -> dict:
    return {
        "CANDIDATE_ID": row.get("candidate_id") or row["audit_sample_id"],
        "SOURCE_ACT_TITLE": row["source_celex"],
        "SOURCE_CELEX": row["source_celex"],
        "ARTICLE": package["article_token"],
        "FULL_ARTICLE_TEXT": package["full_text"],
        "CROSS_REFERENCED_TEXT": "",
        "KNOWN_CROSS_ACT_TEXT": "",
    }


def run_stage_repeated(stage: str, unit_id: str, provider: str, model: str, values: dict) -> tuple[list[dict], dict]:
    records = [run_stage.run_once(stage, unit_id, provider, model, values, None, False)
               for _ in range(N_RUNS)]
    check_records = [{"stage": stage, "unit_id": unit_id, **record} for record in records]
    return records, check_consistency(stage, unit_id, check_records)


def append_review(stage: str, unit_id: str, reason: str) -> None:
    path = DATA / "human_review_v4.csv"
    is_new = not path.exists()
    with path.open("a", newline="", encoding="utf-8") as handle:
        if is_new:
            handle.write("stage,unit_id,reason\n")
        writer = csv.writer(handle)
        writer.writerow([stage, unit_id, reason])


def run_sample(provider: str, model: str, limit: int | None) -> list[dict]:
    rows = load(SAMPLE)
    if limit is not None:
        rows = rows[:limit]
    results = []
    for row in rows:
        slug = CELEX_TO_SLUG[row["source_celex"]]
        package = context_package.build_package(slug, row["article"])
        values = base_values(row, package)
        values["PROVISION_ID"] = row["audit_sample_id"]
        values["PROVISION_TEXT"] = row["evidence_text"]
        _, a2_consistency = run_stage_repeated("a2", row["audit_sample_id"], provider, model, values)

        b1_records, b1_consistency = run_stage_repeated("b1", row["audit_sample_id"], provider, model, values)
        b2_values = dict(values)
        b2_values["STAGE_B1_OUTPUT_JSON"] = json.dumps(b1_records[-1]["output"], ensure_ascii=False)
        b2_records, b2_consistency = run_stage_repeated("b2", row["audit_sample_id"], provider, model, b2_values)

        # All sample units stay in human review until Tier 1 validates a model,
        # even when the three local runs happen to agree.
        append_review("a2", row["audit_sample_id"], "Full human review required; AI layer not validated on Tier 1.")
        append_review("b2", row["audit_sample_id"], "Full human review required; AI layer not validated on Tier 1.")
        results.append({
            "unit_id": row["audit_sample_id"], "source_celex": row["source_celex"],
            "article": package["article_token"], "a2_consistency": a2_consistency,
            "b1_consistency": b1_consistency, "b2_consistency": b2_consistency,
            "provider": provider, "model": model,
        })
        print(f"{row['audit_sample_id']}: A2={a2_consistency['status']} B1={b1_consistency['status']} B2={b2_consistency['status']}")
    return results


def run_c(provider: str, model: str) -> list[dict]:
    relationships = load(RELATIONSHIPS)
    actors = {row["actor_id"]: row["actor_label"] for row in load(ACTORS)}
    results = []
    for row in relationships:
        slug = CELEX_TO_SLUG[row["source_act"]]
        package = context_package.build_package(slug, row["article"])
        values = {
            "RELATIONSHIP_ID": row["relationship_id"],
            "RELATIONSHIP_TEXT": package["full_text"] + "\n\nEvidence row:\n" + row["verbatim_evidence"],
            "R_ACTOR": actors.get(row["R_actor_id"], row["R_actor_id"]),
            "I_ACTOR": actors.get(row["I_actor_id"], row["I_actor_id"]),
            "T_ACTOR": actors.get(row["T_actor_id"], row["T_actor_id"]),
            "REQUESTED_FIXED_FIELDS": "all fixed v3 attributes",
            "REQUESTED_DEFERRED_FIELDS": "conflict_of_interest_rule, reporting_to_regulator, accreditation",
            "FIELD_DEFINITIONS_EXCERPT": "Use DATA_DICTIONARY_v3.md definitions copied into the report; do not infer outcomes or indices.",
        }
        records, consistency = run_stage_repeated("c", row["relationship_id"], provider, model, values)
        append_review("c", row["relationship_id"], "Full human review required; inherited relationship and AI proposal must be checked separately.")
        results.append({"unit_id": row["relationship_id"], "consistency": consistency, "provider": provider, "model": model})
        print(f"{row['relationship_id']}: C={consistency['status']}")
    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--provider", choices=["dry_run", "openai"], default="dry_run")
    parser.add_argument("--model", default="dry-run-model")
    parser.add_argument("--limit", type=int, default=None, help="Only process the first N audit units")
    parser.add_argument("--include-c", action="store_true", help="Run Stage C on the seven inherited positive relationships")
    args = parser.parse_args()
    DATA.mkdir(exist_ok=True)
    sample_results = run_sample(args.provider, args.model, args.limit)
    c_results = run_c(args.provider, args.model) if args.include_c else []
    summary = {
        "run_started_utc": datetime.now(timezone.utc).isoformat(),
        "provider": args.provider, "model": args.model,
        "sample_units": len(sample_results), "stage_c_units": len(c_results),
        "runs_per_unit": N_RUNS,
        "note": "Dry-run outputs are schema smoke tests only and are not substantive findings. Real API run was unavailable if provider=openai returns an account/quota error.",
        "sample": sample_results, "stage_c": c_results,
    }
    (DATA / "ai_execution_summary_v4.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
