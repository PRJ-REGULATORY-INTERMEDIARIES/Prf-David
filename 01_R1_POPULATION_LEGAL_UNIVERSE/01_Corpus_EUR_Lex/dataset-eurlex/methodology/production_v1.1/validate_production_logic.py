from __future__ import annotations

"""Structural/logical validation for production-v1.1 coding matrix records.

This module intentionally does NOT hard-enforce a mechanical link between the
third_actor_test result pattern and relation_type (e.g. it never requires "all five
dimensions YES => relation_type must be intermediated", nor the reverse). The prior
methodology (v1.1.0, the intensive pilot) enforced `condition_C == YES => I must be
populated` regardless of the mediating-function condition, which produced a documented,
irreducible conflict with the separate rule that a direct relationship must carry no I
(see methodology/v1.1.0/../pre_ra_4way/KNOWN_LIMITATIONS_V1_1.md and every RA_4way
structural-limitation correction). v1.1 deliberately keeps the five-dimension test as a
documented reasoning aid and evidentiary record, not a mechanical trigger, so that a
distinct-but-non-mediating third actor never forces an inconsistent structural state.
"""

import json
from typing import Iterable

VALID_RELATION_TYPES = {"intermediated", "direct", "uncertain", "not_supported"}
VALID_MECHANISMS = {
    "reporting", "verification", "certification", "auditing", "monitoring_supervision",
    "ranking_rating", "standard_setting", "enforcement_support", "coordination",
    "information_transmission", "delegated_implementation", "accreditation",
    "other_mechanism", "none_or_direct",
}
VALID_CONFIDENCE = {"high", "medium", "low", "not_assessed"}
TEST_DIMENSIONS = ("distinction", "function", "regulatory_integration", "evidence", "counterfactual")
VALID_TEST_RESULT = {"YES", "NO", "UNCLEAR"}


def _actor_signature(value) -> tuple:
    if not value:
        return ()
    return tuple(sorted((item.get("label"), item.get("role")) for item in value))


def substantive_signature(record: dict) -> tuple:
    """Comparison signature ignoring free-text role/action/object/mediating_function
    prose and ignoring coder_note, mirroring the same design choice already documented
    for the prior pilot's comparator (KNOWN_LIMITATIONS_V1_1.md, 'free-text actor roles')."""
    labels = lambda arr: tuple(sorted(a.get("label") for a in (arr or [])))
    test = record.get("third_actor_test")
    test_sig = None
    if test:
        test_sig = tuple(test[d]["result"] for d in TEST_DIMENSIONS)
    return (
        record.get("relation_type"),
        labels(record.get("R")),
        labels(record.get("I")),
        labels(record.get("T")),
        record.get("mechanism"),
        test_sig,
        bool(record.get("operative_anchor_location")),
    )


def validate_record(record: dict) -> list[str]:
    """Return a list of human-readable rule violations; empty list means the record
    passes all logical checks this module enforces. Does not replace JSON-Schema
    structural validation against coding_matrix_schema.json -- run both."""
    errors: list[str] = []
    rid = record.get("relation_id", "<no relation_id>")

    rtype = record.get("relation_type")
    if rtype not in VALID_RELATION_TYPES:
        errors.append(f"{rid}: invalid relation_type {rtype!r}")

    if record.get("mechanism") not in VALID_MECHANISMS:
        errors.append(f"{rid}: invalid mechanism {record.get('mechanism')!r}")

    if record.get("confidence") not in VALID_CONFIDENCE:
        errors.append(f"{rid}: invalid confidence {record.get('confidence')!r}")

    # Rule: object != target is not machine-checkable from labels alone; left to review.

    # Rule: operative anchor required for a relation the main matrix treats as settled.
    if rtype in ("intermediated", "direct") and not record.get("operative_anchor_location"):
        errors.append(
            f"{rid}: relation_type={rtype} requires a non-null operative_anchor_location "
            f"(codebook: a positive/direct classification needs an operative-text anchor, "
            f"not a recital alone)"
        )

    # Rule: direct relations carry no I (unchanged from v1.0/v1.1.0 house style).
    if rtype == "direct" and record.get("I"):
        errors.append(f"{rid}: relation_type=direct must not carry a populated I")

    # Rule: intermediated relations require R, I and T all non-empty.
    if rtype == "intermediated":
        for field in ("R", "I", "T"):
            if not record.get(field):
                errors.append(f"{rid}: relation_type=intermediated requires a non-empty {field}")

    # Rule: third_actor_test presence.
    test = record.get("third_actor_test")
    i_populated = bool(record.get("I"))
    if i_populated and not test:
        errors.append(f"{rid}: I is populated but third_actor_test is null")
    if rtype == "intermediated" and not test:
        errors.append(f"{rid}: relation_type=intermediated requires a non-null third_actor_test")
    if test is not None:
        for dim in TEST_DIMENSIONS:
            if dim not in test:
                errors.append(f"{rid}: third_actor_test missing dimension {dim!r}")
                continue
            result = test[dim].get("result")
            if result not in VALID_TEST_RESULT:
                errors.append(f"{rid}: third_actor_test.{dim}.result invalid: {result!r}")
        # Soft consistency note (not an error): counterfactual=NO alongside
        # relation_type=intermediated is a documented tension for reviewer attention,
        # not a structural violation -- substantive judgment stays with the coder.

    return errors


def validate_all(records: Iterable[dict]) -> dict[str, list[str]]:
    out: dict[str, list[str]] = {}
    for record in records:
        errs = validate_record(record)
        if errs:
            out[record.get("relation_id", "<unknown>")] = errs
    return out


def run_abstract_tests() -> None:
    def base(**overrides) -> dict:
        record = {
            "case_id": "case_00", "celex": "00000000", "relation_id": "ABSTRACT",
            "source_location": "Article 1", "evidence_quote": "x",
            "operative_anchor_location": "Article 1", "contextual_support": [],
            "R": [{"label": "R1", "role": "regulator", "evidence_refs": ["e1"]}],
            "I": [], "T": [{"label": "T1", "role": "target", "evidence_refs": ["e1"]}],
            "action": [], "object": [], "mediating_function": [],
            "mechanism": "none_or_direct", "relation_type": "direct",
            "third_actor_test": None, "confidence": "high",
            "external_context_required": False, "coder_note": "",
        }
        record.update(overrides)
        return record

    assert validate_record(base()) == []

    direct_with_i = base(I=[{"label": "X", "role": "third", "evidence_refs": ["e1"]}])
    assert any("third_actor_test is null" in e for e in validate_record(direct_with_i))

    def dim(result="YES"):
        return {"result": result, "note": "abstract"}

    full_test = {d: dim() for d in TEST_DIMENSIONS}
    intermediated = base(
        relation_type="intermediated",
        I=[{"label": "X", "role": "intermediary", "evidence_refs": ["e1"]}],
        third_actor_test=full_test,
    )
    assert validate_record(intermediated) == []

    recital_only_positive = base(operative_anchor_location=None)
    assert any("operative_anchor_location" in e for e in validate_record(recital_only_positive))

    # C=YES/D=NO analogue: a distinct, non-mediating third actor. This must NOT be
    # forced into relation_type=intermediated and must NOT be blocked from staying
    # direct-with-empty-I; it simply is not "I" at all under v1.1's design.
    non_mediating_third_actor_stays_direct = base(
        coder_note="third actor considered and rejected as non-mediating; logged in uncertainties",
    )
    assert validate_record(non_mediating_third_actor_stays_direct) == []

    print("PRODUCTION_V1_1_LOGIC_ABSTRACT_TESTS_OK")


if __name__ == "__main__":
    run_abstract_tests()
