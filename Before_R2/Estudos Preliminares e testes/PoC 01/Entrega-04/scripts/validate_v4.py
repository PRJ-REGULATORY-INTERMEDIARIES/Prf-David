"""Acceptance checks for the Entrega-04 package."""
from __future__ import annotations

import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

import jsonschema

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
V3_DATA = ROOT.parent / "Entrega-02" / "data"
SCHEMA_FILES = {
    "a2": "stage_a2_candidate_detection.schema.json",
    "b1": "stage_b1_architecture.schema.json",
    "b2": "stage_b2_rit_adjudication.schema.json",
    "c": "stage_c_attributes.schema.json",
}


def read_csv(path: Path) -> list[dict]:
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def check(condition: bool, message: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {message}")
    else:
        failures.append(message)
        print(f"FAIL: {message}")


def validate_manifest(failures: list[str]) -> None:
    manifest = read_csv(DATA / "CELEX_MANIFEST_v4.csv")
    check(len(manifest) == 5, "manifest contains exactly five acts", failures)
    required = {"base_celex", "version_celex", "eli", "act_title", "act_type", "document_date",
                "entry_into_force", "legal_status", "consolidated_version", "retrieval_date",
                "language", "source_url", "sha256", "file_name"}
    check(bool(manifest) and required.issubset(manifest[0]),
          "manifest contains the required CELEX/version fields", failures)
    check(len({row["base_celex"] for row in manifest}) == 5, "base CELEX values are unique", failures)
    check(len({row["version_celex"] for row in manifest}) == 5, "version CELEX values are unique", failures)
    check(all(row["base_celex"] == row["version_celex"] for row in manifest),
          "version identifiers are not counted as additional acts", failures)
    for row in manifest:
        path = ROOT / row["relative_path"].replace("/", "\\")
        exists = path.exists()
        check(exists and path.stat().st_size > 0, f"{row['celex']} HTML exists and is non-empty", failures)
        if exists:
            digest = hashlib.sha256(path.read_bytes()).hexdigest()
            check(digest == row["sha256"], f"{row['celex']} hash matches manifest", failures)


def validate_screening(failures: list[str]) -> None:
    current = read_csv(DATA / "screening_hits_v4.csv")
    historical = read_csv(V3_DATA / "screening_hits_v3.csv")
    expected = {"32022L2464", "32010R0066", "32019R2089", "32018R2067", "32020R0852"}
    actual = {row["source_celex"] for row in current}
    check(actual == expected, "screening identifies exactly the five required CELEX acts", failures)
    old_celex = expected - {"32020R0852"}
    counts = Counter(row["source_celex"] for row in current)
    old_counts = Counter(row["source_celex"] for row in historical)
    check(all(counts[c] == old_counts[c] for c in old_celex), "four-act screening counts regress exactly", failures)
    check(counts["32020R0852"] > 0, "Taxonomy Regulation contributes non-empty screening output", failures)
    required = {"screening_id", "source_celex", "article", "paragraph", "recital", "provision_type",
                "candidate_mechanism", "semantic_role", "entity_form", "matched_pattern",
                "screening_confidence", "evidence_text"}
    check(required.issubset(current[0]), "A1 rows contain provision, semantic-role and entity-form fields", failures)


def validate_datasets(failures: list[str]) -> None:
    actors = read_csv(DATA / "actors_v4.csv")
    actor_ids = {row["actor_id"] for row in actors}
    candidates = read_csv(DATA / "candidate_adjudications_v4.csv")
    relationships = read_csv(DATA / "rit_relationships_v4.csv")
    check(len(candidates) == 30, "candidate v4 contains the 10 regression rows plus 20 held-out rows", failures)
    check(sum(row["human_review_status"] == "PENDING_HUMAN" for row in candidates) == 20,
          "all 20 new candidates remain pending human adjudication", failures)
    check(len(relationships) == 7, "relationship v4 preserves the seven human-validated relationships", failures)
    for row in relationships:
        role_ids = [row["R_actor_id"], row["I_actor_id"], row["T_actor_id"]]
        check(all(role_ids), f"{row['relationship_id']} has R, I and T", failures)
        check(len(set(role_ids)) == 3, f"{row['relationship_id']} R/I/T are pairwise distinct", failures)
        check(all(actor_id in actor_ids for actor_id in role_ids), f"{row['relationship_id']} actor FKs are valid", failures)
        check(row["verbatim_evidence"].strip() != "", f"{row['relationship_id']} has literal evidence", failures)
        check(row["intermediary_present"] == "1", f"{row['relationship_id']} is a positive relationship", failures)
    completed = [row for row in candidates if row["human_review_status"] != "PENDING_HUMAN"]
    check(all(row["intermediary_present"] == "1" for row in relationships),
          "negative/conditional cases are absent from positive relationships", failures)
    check(all(row["ai_assisted"] == "0" for row in completed), "no AI proposal was promoted into v4 authoritative rows", failures)
    check(all(row.get("human_approved") == "1" for row in relationships),
          "all authoritative relationships carry explicit human approval", failures)
    check(not any("autonomy_index" in row or "accountability_index" in row for row in relationships),
          "deferred autonomy/accountability indices are not presented as measured", failures)


def validate_ai_log(failures: list[str]) -> None:
    path = DATA / "ai_runs_v4.jsonl"
    check(path.exists(), "AI execution log exists", failures)
    if not path.exists():
        return
    common = json.loads((ROOT / "schemas" / "common_defs.schema.json").read_text(encoding="utf-8"))
    schemas = {}
    for stage, filename in SCHEMA_FILES.items():
        schema = json.loads((ROOT / "schemas" / filename).read_text(encoding="utf-8"))
        inner = schema.get("schema", schema)
        inner.setdefault("$defs", {}).update(common["$defs"])
        schemas[stage] = inner
    records = []
    with path.open(encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, 1):
            record = json.loads(line)
            records.append(record)
            required_metadata = {"run_id", "provider", "model_id", "model_snapshot",
                                 "reasoning_setting", "prompt_version", "schema_version",
                                 "timestamp", "input_hash", "output_hash", "cost_estimate"}
            check(required_metadata.issubset(record),
                  f"AI log line {line_number} has call-level provenance", failures)
            if record.get("stage") == "a2":
                check(record.get("output", {}).get("ai_run_ref") == record.get("run_id"),
                      f"AI log line {line_number} links A2 output to run_id", failures)
            try:
                jsonschema.validate(record["output"], schemas[record["stage"]])
            except Exception as exc:  # report all invalid outputs, not just the first
                failures.append(f"AI log line {line_number} failed {record['stage']} schema: {exc}")
    check(len(records) == (20 * 9 + 7 * 3), "dry-run log contains 201 stage calls", failures)
    check(not any(record["model_provider"] != "dry_run" for record in records),
          "current AI log is explicitly dry-run only", failures)
    print("PASS: every AI log record was checked against its stage schema")


def validate_auxiliary(failures: list[str]) -> None:
    expected = {
        "semantic_candidates_v4.csv": 20,
        "relationship_mechanisms_v4.csv": 7,
        "human_review_v4.csv": 47,
        "validation_sample_v4.csv": 20,
        "challenge_sample_v4.csv": 4,
        "ai_runs_v4.csv": 201,
    }
    for name, minimum in expected.items():
        path = DATA / name
        check(path.exists(), f"auxiliary output {name} exists", failures)
        if path.exists():
            rows = read_csv(path)
            check(len(rows) == minimum, f"{name} contains the expected {minimum} rows", failures)
    if (DATA / "semantic_candidates_v4.csv").exists():
        rows = read_csv(DATA / "semantic_candidates_v4.csv")
        check(all(row.get("output_status") == "DRY_RUN_ONLY" for row in rows),
              "semantic candidates are explicitly marked dry-run only", failures)


def main() -> None:
    failures: list[str] = []
    validate_manifest(failures)
    validate_screening(failures)
    validate_datasets(failures)
    validate_ai_log(failures)
    validate_auxiliary(failures)
    if failures:
        print(f"\n{len(failures)} acceptance check(s) failed.")
        raise SystemExit(1)
    print("\nAll Entrega-04 acceptance checks passed.")


if __name__ == "__main__":
    main()
