from __future__ import annotations

import csv
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OLD = ROOT / "03_human" / "stage4_attempt_01" / "candidate_universe.csv"
NEW = ROOT / "03_human" / "stage4_attempt_02" / "candidate_reconstruction.json"
OUT = Path(__file__).resolve().parent / "candidate_transition_audit.csv"


# This is a reconstruction audit only. It must never read the attempt-01
# coding outputs (R/I/T, results, evidence, or confidence).
ALLOWED_TRANSITIONS = {
    "retained",
    "hierarchically_remapped",
    "absorbed_into_new_candidate",
    "explicitly_excluded_after_reconstruction",
    "unmatched_requires_review",
    "newly_reconstructed",
}


# These are explicit, text-and-structure-only decisions. They are deliberately
# not a fallback for unmatched rows: an old row not listed here remains for
# review, rather than being silently treated as excluded.
EXPLICIT_EXCLUSIONS: dict[str, tuple[str, str]] = {
    "CAND-0008": ("non_relational_objective", "Recital 10 states a general contribution objective and contains no focal regulatory relation after reconstruction."),
    "CAND-0009": ("context_only", "Recital 11 supplies sectoral-policy background rather than a focal regulatory relation."),
    "CAND-0016": ("context_only", "Recital 21 records prior institutional conclusions and legal-allocation context, not a focal relation."),
    "CAND-0018": ("non_relational_objective", "Recital 23 describes ecosystem functions and policy objectives without a focal regulatory relation."),
    "CAND-0022": ("context_only", "Recital 28 provides budgetary-contribution context rather than a standalone regulatory relation."),
    "CAND-0023": ("non_relational_objective", "Recital 29 states a subsidy-phase-out objective without a focal regulatory relation."),
    "CAND-0034": ("enacting_clause", "The enacting formula does not establish a focal regulatory relation."),
    "CAND-0035": ("non_relational_objective", "Article 1 is a framework-and-scope clause, not a focal regulatory relation."),
    "CAND-0036": ("non_relational_objective", "Article 1(a) states an objective/scope element, not a focal regulatory relation."),
    "CAND-0037": ("non_relational_objective", "Article 2(1) is a target-setting clause, not a focal regulatory relation."),
    "CAND-0053": ("non_relational_objective", "Article 4(c) is a factor for a future target proposal, not a focal regulatory relation."),
    "CAND-0054": ("non_relational_objective", "Article 4(i) is an environmental-effectiveness factor, not a focal regulatory relation."),
    "CAND-0055": ("context_only", "Article 4(m) identifies existing information as a review factor, without a focal regulatory relation."),
    "CAND-0057": ("context_only", "Article 4(7) is a general review clause whose external developments are context only for this reconstruction."),
    "CAND-0077": ("context_only", "Article 7(3)(c) states a complementarity condition for recommendations, not a standalone focal relation."),
    "CAND-0098": ("context_only", "Article 13(4) is an amending instruction that inserts an information item; it is not a standalone focal relation in this reconstruction."),
    "CAND-0104": ("context_only", "Article 13(10) is an annex-amendment instruction whose listed policy information is context only here."),
    "CAND-0106": ("enacting_clause", "Article 14 is an entry-into-force clause and does not establish a focal regulatory relation."),
}


# A chapeau can be remapped to its reconstructed children even where the child
# lines occur immediately after, rather than inside, the old chapeau's span.
# These mappings were checked from IDs, locations, excerpts, and hierarchy only.
SPECIAL_TRANSITIONS: dict[str, tuple[str, list[str], str, str]] = {
    "CAND-0031": (
        "newly_reconstructed",
        ["CAND2-DAF9214798E0"],
        "lost_structural_unit_reconstructed",
        "Recital 38 is a complete Commission-to-society engagement unit that was absent from the first hierarchy-aware reconstruction and has now been reconstructed from its canonical span.",
    ),
    "CAND-0040": (
        "hierarchically_remapped",
        ["CAND2-DDC9A9630321", "CAND2-D6ED62ADF0C5", "CAND2-6EA7E563363E", "CAND2-021AD4B3CF48"],
        "chapeau_absorbed_by_children",
        "Article 3(2) chapeau is represented by its reconstructed child points (a), (b), (c), and (e).",
    ),
    "CAND-0064": (
        "absorbed_into_new_candidate",
        ["CAND2-EDD56D7845D3"],
        "contextual_child_absorbed_by_parent",
        "Article 6(1)(a) is retained as an assessment object within the reconstructed Article 6(1) Commission-assessment unit.",
    ),
    "CAND-0066": (
        "newly_reconstructed",
        ["CAND2-7811F95526B7"],
        "lost_structural_unit_reconstructed",
        "Article 6(2) is a complete Commission-review unit whose two listed review objects must remain available with their common hierarchical context.",
    ),
    "CAND-0067": (
        "absorbed_into_new_candidate",
        ["CAND2-7811F95526B7"],
        "contextual_child_absorbed_by_parent",
        "Article 6(2)(a) is one review object within the newly reconstructed Article 6(2) Commission-review unit.",
    ),
    "CAND-0074": (
        "hierarchically_remapped",
        ["CAND2-9E16D8A0E046", "CAND2-295D4FBD3131"],
        "chapeau_absorbed_by_children",
        "Article 7(3) chapeau is represented by its reconstructed child points (a) and (b).",
    ),
}


def lines_from_old(value: str) -> tuple[int, int]:
    match = re.search(r"lines (\d+)-(\d+)", value)
    if not match:
        raise ValueError(f"Missing line range: {value}")
    return int(match.group(1)), int(match.group(2))


def overlap(a_start: int, a_end: int, b_start: int, b_end: int) -> int:
    return max(0, min(a_end, b_end) - max(a_start, b_start) + 1)


def section(value: str) -> str:
    match = re.match(r"(Article \d+|Recital \d+)", value)
    return match.group(1) if match else value.split(",", 1)[0]


def new_section(location: dict[str, object]) -> str:
    if location.get("article") is not None:
        return f"Article {location['article']}"
    return f"Recital {location['recital']}"


def locations(new_rows: list[dict[str, object]]) -> str:
    return " | ".join(json.dumps(row["source_location"], ensure_ascii=False) for row in new_rows)


def excerpts(new_rows: list[dict[str, object]]) -> str:
    return "\n---\n".join(str(row["focal_excerpt"]) for row in new_rows)


def audit_row(old: dict[str, object] | None, destinations: list[dict[str, object]], transition: str, reason_code: str, reason: str) -> dict[str, str]:
    if transition not in ALLOWED_TRANSITIONS:
        raise ValueError(f"Unsupported transition: {transition}")
    destination_ids = [str(row["candidate_id"]) for row in destinations]
    absorbed_by = destination_ids[0] if transition == "absorbed_into_new_candidate" else ""
    if transition == "absorbed_into_new_candidate" and len(destination_ids) != 1:
        raise ValueError("An absorbed row must have exactly one absorbing candidate")
    return {
        "attempt_01_candidate_id": "" if old is None else str(old["candidate_id"]),
        "attempt_02_candidate_id": ";".join(destination_ids),
        "destination_candidate_ids": ";".join(destination_ids),
        "absorbed_by_candidate_id": absorbed_by,
        "transition": transition,
        "attempt_01_location": "" if old is None else str(old["source_location"]),
        "attempt_02_location": locations(destinations) if destinations else "",
        "attempt_01_excerpt": "" if old is None else str(old["excerpt"]),
        "attempt_02_focal_excerpt": excerpts(destinations) if destinations else "",
        "reason_code": reason_code,
        "reason": reason,
        "coding_fields_reused": "none",
    }


def mapped_row(old: dict[str, object], destinations: list[dict[str, object]], transition: str, reason_code: str, reason: str) -> dict[str, str]:
    if not destinations:
        raise ValueError(f"Mapped row without destination: {old['candidate_id']}")
    return audit_row(old, destinations, transition, reason_code, reason)


def main() -> None:
    old_rows = list(csv.DictReader(OLD.open(encoding="utf-8")))
    new_rows = json.loads(NEW.read_text(encoding="utf-8"))
    old_items = []
    for row in old_rows:
        start, end = lines_from_old(row["source_location"])
        old_items.append({**row, "start": start, "end": end, "section": section(row["source_location"])})
    new_items = []
    for row in new_rows:
        location = row["source_location"]
        new_items.append({**row, "start": int(location["line_start"]), "end": int(location["line_end"]), "section": new_section(location)})
    if len({item["candidate_id"] for item in old_items}) != len(old_items):
        raise ValueError("Attempt-01 candidate IDs are not unique")
    new_by_id = {str(item["candidate_id"]): item for item in new_items}
    if len(new_by_id) != len(new_items):
        raise ValueError("Attempt-02 candidate IDs are not unique")

    used_new: set[str] = set()
    audit_rows: list[dict[str, str]] = []
    unmatched: list[str] = []
    for old in old_items:
        old_id = str(old["candidate_id"])
        if old_id in SPECIAL_TRANSITIONS:
            transition, destination_ids, reason_code, reason = SPECIAL_TRANSITIONS[old_id]
            destinations = [new_by_id[candidate_id] for candidate_id in destination_ids]
            audit_rows.append(mapped_row(old, destinations, transition, reason_code, reason))
            used_new.update(destination_ids)
            continue

        section_candidates = [item for item in new_items if item["section"] == old["section"]]
        exact = [item for item in section_candidates if old["start"] == item["start"] and old["end"] == item["end"]]
        if len(exact) == 1:
            audit_rows.append(mapped_row(old, exact, "retained", "same_span", "The article/recital and complete line span are retained in the reconstructed candidate."))
            used_new.add(str(exact[0]["candidate_id"]))
            continue
        if len(exact) > 1:
            audit_rows.append(mapped_row(old, exact, "hierarchically_remapped", "duplicate_span", "The same old span is represented by multiple reconstructed units and is retained as a hierarchy-aware mapping."))
            used_new.update(str(item["candidate_id"]) for item in exact)
            continue

        children = [item for item in section_candidates if old["start"] <= item["start"] and item["end"] <= old["end"]]
        if len(children) > 1:
            audit_rows.append(mapped_row(old, children, "hierarchically_remapped", "hierarchical_span_resegmentation", "The attempt-01 span is represented by multiple focal child units after hierarchy-aware reconstruction."))
            used_new.update(str(item["candidate_id"]) for item in children)
            continue
        if len(children) == 1:
            audit_rows.append(mapped_row(old, children, "absorbed_into_new_candidate", "duplicate_span", "The attempt-01 parent/introductory span is represented by one focal reconstructed unit."))
            used_new.add(str(children[0]["candidate_id"]))
            continue

        parents = [item for item in section_candidates if item["start"] <= old["start"] and old["end"] <= item["end"]]
        if parents:
            parent = min(parents, key=lambda item: (item["end"] - item["start"], item["start"]))
            audit_rows.append(mapped_row(old, [parent], "absorbed_into_new_candidate", "contextual_child_absorbed_by_parent", "The attempt-01 fragment is context within a single reconstructed parent unit."))
            used_new.add(str(parent["candidate_id"]))
            continue

        overlaps = [item for item in section_candidates if overlap(old["start"], old["end"], item["start"], item["end"]) > 0]
        if overlaps:
            audit_rows.append(mapped_row(old, overlaps, "hierarchically_remapped", "hierarchical_span_resegmentation", "The spans overlap within the same article/recital but have been resegmented by hierarchy-aware reconstruction."))
            used_new.update(str(item["candidate_id"]) for item in overlaps)
            continue

        if old_id in EXPLICIT_EXCLUSIONS:
            reason_code, reason = EXPLICIT_EXCLUSIONS[old_id]
            audit_rows.append(audit_row(old, [], "explicitly_excluded_after_reconstruction", reason_code, reason))
            continue

        unmatched.append(old_id)
        audit_rows.append(audit_row(old, [], "unmatched_requires_review", "no_safe_structural_destination", "No destination or text-and-structure-only exclusion can be established safely; review is required."))

    for new in new_items:
        new_id = str(new["candidate_id"])
        if new_id not in used_new:
            audit_rows.append(audit_row(None, [new], "newly_reconstructed", "newly_reconstructed", "Unit exposed by hierarchy/context reconstruction and not mapped from an attempt-01 candidate; no substantive coding fields reused."))

    old_audit_ids = [row["attempt_01_candidate_id"] for row in audit_rows if row["attempt_01_candidate_id"]]
    if set(old_audit_ids) != {str(item["candidate_id"]) for item in old_items} or len(old_audit_ids) != len(old_items):
        raise ValueError("Every attempt-01 candidate must have exactly one audit outcome")
    for row in audit_rows:
        if row["transition"] == "absorbed_into_new_candidate" and not row["absorbed_by_candidate_id"]:
            raise ValueError("Absorbed candidate lacks absorbed_by_candidate_id")
        if row["transition"] == "explicitly_excluded_after_reconstruction" and row["reason_code"] not in {"enacting_clause", "non_relational_objective", "chapeau_absorbed_by_children", "context_only", "duplicate_span"}:
            raise ValueError("Exclusion lacks a concrete structural reason code")
        if row["coding_fields_reused"] != "none":
            raise ValueError("Audit must not reuse substantive coding fields")

    fields = list(audit_rows[0].keys()) if audit_rows else ["transition"]
    with OUT.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(audit_rows)
    counts: dict[str, int] = {}
    for row in audit_rows:
        counts[row["transition"]] = counts.get(row["transition"], 0) + 1
    print(json.dumps({"attempt_01_candidates": len(old_items), "attempt_02_candidates": len(new_items), "audit_rows": len(audit_rows), "transitions": counts, "unmatched_requires_review": unmatched}, ensure_ascii=False))


if __name__ == "__main__":
    main()
