from __future__ import annotations

import json
import re
from typing import Iterable


CONDITIONS = ("condition_A", "condition_B", "condition_C", "condition_D", "condition_E")
VALID = {"YES", "NO", "UNCLEAR"}


def _actor_signature(value) -> tuple:
    if not value:
        return ()
    return tuple(sorted((item.get("label"), item.get("role")) for item in value))


def _text_signature(value) -> tuple:
    if not value:
        return ()
    return tuple(sorted(re.sub(r"\s+", " ", str(item)).strip().casefold() for item in value))


def substantive_signature(record: dict) -> tuple:
    """Return only substantive fields; ignore notes, wording, order and metadata."""
    conditions = tuple(record["relational_test"][name]["result"] for name in CONDITIONS)
    return (
        record.get("screening_status"),
        _actor_signature(record.get("R")),
        _actor_signature(record.get("I")),
        _actor_signature(record.get("T")),
        conditions,
        record.get("relational_result"),
        record.get("primary_mechanism"),
        _text_signature(record.get("action")),
        _text_signature(record.get("object")),
        _text_signature(record.get("mediating_function")),
        _text_signature(record.get("secondary_mechanisms")),
    )


def expected_relational_result(record: dict) -> str:
    results = {name: record["relational_test"][name]["result"] for name in CONDITIONS}
    if all(value == "YES" for value in results.values()):
        return "positive"
    if any(results[name] == "NO" for name in ("condition_A", "condition_B", "condition_C", "condition_D")):
        return "negative"
    if results["condition_E"] == "NO":
        return "insufficient_evidence"
    if any(value == "UNCLEAR" for value in results.values()):
        return "conditional"
    raise ValueError("Unreachable condition combination")


def validate_relational_logic(record: dict) -> None:
    test = record["relational_test"]
    for name in CONDITIONS:
        result = test[name]["result"]
        if result not in VALID:
            raise ValueError(f"Invalid {name}: {result}")
        if not test[name]["evidence_refs"]:
            raise ValueError(f"Missing evidence refs for {name}")
    expected = expected_relational_result(record)
    if record["relational_result"] != expected:
        raise ValueError(
            f"{record['candidate_id']}: relational_result={record['relational_result']} "
            f"is incompatible with A-E; expected {expected}"
        )
    if record["relational_result"] == "positive" and not all(record[key] for key in ("R", "I", "T")):
        raise ValueError(f"{record['candidate_id']}: positive requires R, I and T")
    if record["relational_result"] == "positive" and record["screening_status"] in {"not_candidate", "insufficient_evidence"}:
        raise ValueError(f"{record['candidate_id']}: positive cannot have exclusion/insufficient screening status")
    if record["screening_status"] == "direct_relationship" and record["I"] not in (None, []):
        raise ValueError(f"{record['candidate_id']}: direct relationship cannot contain I")
    if test["condition_C"]["result"] == "YES" and not record["I"]:
        raise ValueError(f"{record['candidate_id']}: C=YES requires I")
    if test["condition_D"]["result"] == "YES" and not record["I"]:
        raise ValueError(f"{record['candidate_id']}: D=YES requires I")


def human_review_triggers(r1: Iterable[dict], r2: Iterable[dict], ra: Iterable[dict], audit_ids: set[str]) -> set[str]:
    selected = set(audit_ids)
    r1_by_id = {record["candidate_id"]: record for record in r1}
    r2_by_id = {record["candidate_id"]: record for record in r2}
    ra_by_id = {record["candidate_id"]: record for record in ra}
    for candidate_id in r1_by_id.keys() | r2_by_id.keys() | ra_by_id.keys():
        records = [x for x in (r1_by_id.get(candidate_id), r2_by_id.get(candidate_id), ra_by_id.get(candidate_id)) if x]
        if any(record.get("I") not in (None, []) for record in records):
            selected.add(candidate_id)
        if any(record["relational_test"][key]["result"] == "YES" for record in records for key in ("condition_C", "condition_D")):
            selected.add(candidate_id)
        if r1_by_id.get(candidate_id) and r2_by_id.get(candidate_id):
            if substantive_signature(r1_by_id[candidate_id]) != substantive_signature(r2_by_id[candidate_id]):
                selected.add(candidate_id)
        if any(record.get("confidence") == "low" for record in records):
            selected.add(candidate_id)
    return selected


def run_abstract_tests() -> None:
    def record(results: dict, result: str, r=True, i=True, t=True):
        return {
            "candidate_id": "ABSTRACT",
            "relational_test": {key: {"result": value, "evidence_refs": ["e1"]} for key, value in results.items()},
            "relational_result": result,
            "R": [{}] if r else None,
            "I": [{}] if i else None,
            "T": [{}] if t else None,
            "screening_status": "candidate",
        }
    validate_relational_logic(record(dict.fromkeys(CONDITIONS, "YES"), "positive"))
    validate_relational_logic(record({"condition_A": "YES", "condition_B": "YES", "condition_C": "NO", "condition_D": "NO", "condition_E": "YES"}, "negative", i=False))
    validate_relational_logic(record({"condition_A": "YES", "condition_B": "UNCLEAR", "condition_C": "NO", "condition_D": "NO", "condition_E": "YES"}, "negative", i=False, t=False))
    invalid = record(dict.fromkeys(CONDITIONS, "YES"), "negative")
    try:
        validate_relational_logic(invalid)
    except ValueError:
        pass
    else:
        raise AssertionError("incompatible positive/negative record was not rejected")
    same_a = record({"condition_A": "YES", "condition_B": "YES", "condition_C": "NO", "condition_D": "NO", "condition_E": "YES"}, "negative", i=False)
    same_b = json.loads(json.dumps(same_a))
    same_b["notes"] = ["different wording"]
    same_b["evidence_items"] = [{"evidence_id": "other"}]
    assert substantive_signature(same_a) == substantive_signature(same_b)
    different = json.loads(json.dumps(same_a))
    different["relational_test"]["condition_C"]["result"] = "YES"
    different["I"] = [{}]
    assert substantive_signature(same_a) != substantive_signature(different)
    low_r1 = json.loads(json.dumps(same_a))
    low_r1["confidence"] = "low"
    selected = human_review_triggers([low_r1], [same_a], [], set())
    assert "ABSTRACT" in selected
    print("REFERENCE_LOGIC_ABSTRACT_TESTS_OK")


if __name__ == "__main__":
    run_abstract_tests()
