from __future__ import annotations

"""Resolve the three post-reconstruction audit records using text and structure only.

This utility reads only the canonical corpus, the attempt-02 candidate universe,
and the two non-substantive attempt-02 input packets. It never opens any R1, R2,
or RA coding output from attempt 1, or any substantive coding field.
"""

import csv
import hashlib
import json
import re
from pathlib import Path


OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[1]
CORPUS = ROOT / "02_corpus" / "act.md"
RECONSTRUCTION = OUT / "candidate_reconstruction.json"
RECONSTRUCTION_CSV = OUT / "candidate_reconstruction.csv"
PACKETS = [OUT / "R1_coding_input.json", OUT / "R2_coding_input.json"]
CELEX = "32021R1119"
SKELETON_FIELDS = [
    "candidate_id",
    "candidate_origin",
    "source_location",
    "focal_excerpt",
    "parent_context",
    "same_act_context_refs",
]


def compact(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def candidate_id(line_start: int, line_end: int, excerpt: str) -> str:
    fingerprint = f"{line_start}|{line_end}|{excerpt}".encode("utf-8")
    return "CAND2-" + hashlib.sha256(fingerprint).hexdigest()[:12].upper()


def group_id(basis: str) -> str:
    return "GROUP2-" + hashlib.sha256(basis.encode("utf-8")).hexdigest()[:10].upper()


def make_candidate(
    *,
    group_basis: str,
    article: str | None,
    paragraph: str | None,
    recital: str | None,
    line_start: int,
    line_end: int,
    hierarchy: list[str],
    focal_excerpt: str,
    parent_paragraph: str,
    refs: list[str],
    structural_basis: list[str],
) -> dict[str, object]:
    return {
        "candidate_id": candidate_id(line_start, line_end, focal_excerpt),
        "candidate_origin": "structural",
        "reconstruction_group_id": group_id(group_basis),
        "source_location": {
            "celex": CELEX,
            "article": article,
            "paragraph": paragraph,
            "point": None,
            "subparagraph": None,
            "recital": recital,
            "line_start": line_start,
            "line_end": line_end,
            "hierarchy": hierarchy,
        },
        "focal_excerpt": focal_excerpt,
        "parent_context": {
            "hierarchy": hierarchy,
            "article_heading": "Assessment of Union progress and measures" if article == "6" else None,
            "parent_paragraph": parent_paragraph,
        },
        "same_act_context_refs": refs,
        "lexical_hits": [],
        "structural_reconstruction_basis": structural_basis,
        "substantive_coding_status": "pending_independent_R1_R2_reconstruction",
    }


def packet_skeleton(candidate: dict[str, object]) -> dict[str, object]:
    return {field: candidate[field] for field in SKELETON_FIELDS}


def write_csv(candidates: list[dict[str, object]]) -> None:
    rows = []
    for candidate in candidates:
        rows.append({
            "candidate_id": candidate["candidate_id"],
            "candidate_origin": candidate["candidate_origin"],
            "reconstruction_group_id": candidate["reconstruction_group_id"],
            "source_location": json.dumps(candidate["source_location"], ensure_ascii=False),
            "focal_excerpt": candidate["focal_excerpt"],
            "parent_context": json.dumps(candidate["parent_context"], ensure_ascii=False),
            "same_act_context_refs": "; ".join(candidate["same_act_context_refs"]),
            "lexical_hits": "",
            "structural_reconstruction_basis": "; ".join(candidate["structural_reconstruction_basis"]),
        })
    with RECONSTRUCTION_CSV.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]) if rows else ["candidate_id"])
        writer.writeheader()
        writer.writerows(rows)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def main() -> None:
    lines = CORPUS.read_text(encoding="utf-8").splitlines()
    recital_38 = compact(lines[170])
    article_6_p2_lines = [compact(line) for line in lines[279:282]]
    if not recital_38.startswith("(38) As citizens and communities"):
        raise ValueError("Unexpected canonical location for Recital 38")
    if not article_6_p2_lines[0].startswith("2. By 30 September 2023"):
        raise ValueError("Unexpected canonical location for Article 6(2)")
    if not article_6_p2_lines[1].startswith("- (a) the consistency of Union measures"):
        raise ValueError("Unexpected canonical location for Article 6(2)(a)")
    if not article_6_p2_lines[2].startswith("- (b) the consistency of Union measures"):
        raise ValueError("Unexpected canonical location for Article 6(2)(b)")

    additions = [
        make_candidate(
            group_basis="R38",
            article=None,
            paragraph=None,
            recital="38",
            line_start=171,
            line_end=171,
            hierarchy=["Recital 38"],
            focal_excerpt=recital_38,
            parent_paragraph="",
            refs=[],
            structural_basis=["actor_mentions", "action_mentions"],
        ),
        make_candidate(
            group_basis="A6-P2",
            article="6",
            paragraph="2",
            recital=None,
            line_start=280,
            line_end=282,
            hierarchy=["Article 6", "Assessment of Union progress and measures", "paragraph 2"],
            focal_excerpt=" ".join(article_6_p2_lines),
            parent_paragraph=article_6_p2_lines[0][3:],
            refs=["Article 2(1)", "Article 5"],
            structural_basis=["actor_mentions", "action_mentions", "object_mentions", "same_act_cross_references"],
        ),
    ]

    candidates = json.loads(RECONSTRUCTION.read_text(encoding="utf-8"))
    existing_ids = {str(candidate["candidate_id"]) for candidate in candidates}
    expected_addition_ids = {str(candidate["candidate_id"]) for candidate in additions}
    if len(candidates) not in {88, 90}:
        raise ValueError(f"Unexpected candidate universe size: {len(candidates)}")
    if len(candidates) == 90 and not expected_addition_ids.issubset(existing_ids):
        raise ValueError("90-candidate universe does not contain the expected reconstructed additions")

    base_ids = [str(candidate["candidate_id"]) for candidate in candidates if str(candidate["candidate_id"]) not in expected_addition_ids]
    for packet_path in PACKETS:
        packet = json.loads(packet_path.read_text(encoding="utf-8"))
        if any(list(entry) != SKELETON_FIELDS for entry in packet):
            raise ValueError(f"{packet_path.name} is not a minimal non-substantive input packet")
        if [str(entry["candidate_id"]) for entry in packet if str(entry["candidate_id"]) not in expected_addition_ids] != base_ids:
            raise ValueError(f"{packet_path.name} does not match the existing candidate universe")

    if len(candidates) == 88:
        candidates.extend(additions)
    candidates.sort(key=lambda candidate: (
        int(candidate["source_location"]["line_start"]),
        int(candidate["source_location"]["line_end"]),
        str(candidate["candidate_id"]),
    ))
    if len(candidates) != 90 or len({str(candidate["candidate_id"]) for candidate in candidates}) != 90:
        raise ValueError("Expected exactly 90 unique candidates after reconstruction")

    RECONSTRUCTION.write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    write_csv(candidates)
    skeletons = [packet_skeleton(candidate) for candidate in candidates]
    for packet_path in PACKETS:
        packet_path.write_text(json.dumps(skeletons, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(json.dumps({
        "candidate_count": len(candidates),
        "new_candidate_ids": [candidate["candidate_id"] for candidate in additions],
        "origin_counts": {origin: sum(candidate["candidate_origin"] == origin for candidate in candidates) for origin in ("lexical", "structural", "both")},
        "sha256": {path.name: sha256(path) for path in [RECONSTRUCTION, RECONSTRUCTION_CSV, *PACKETS]},
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
