"""Build the blind four-way RA package for stage4_attempt_02.

Reads the four validated reference codings, applies RA_blinding_spec.yaml, assigns a
cryptographically random Coder A/B/C/D permutation drawn from the operating-system
CSPRNG, and writes:

  ra_4way/RA_blind_input.json                      (RA-accessible, blind)
  ra_4way_private/RA_4way_identity_mapping.yaml    (researcher-controlled, NOT for RA)

The mapping is never printed. The only stdout is BLIND_RA_PACKAGE_READY.

Source outputs are opened read-only and are never modified.
"""

from __future__ import annotations

import json
import re
import secrets
import unicodedata
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent          # stage4_attempt_02
ROOT = BASE.parent.parent                              # dataset-eurlex
OUT_DIR = BASE / "ra_4way"
PRIVATE_DIR = BASE / "ra_4way_private"

CODING_INPUT = BASE / "R1_coding_input.json"
ALIASES = BASE / "pre_ra_4way" / "actor_label_aliases.yaml"

# The four validated codings. Order here is the *file* order, never the blind order.
SOURCES = [
    BASE / "R1_output.json",
    BASE / "R2_output.json",
    BASE / "claude_replication_01" / "Claude_R1_output.json",
    BASE / "claude_replication_01" / "Claude_R2_output.json",
]

CONDITIONS = ("condition_A", "condition_B", "condition_C", "condition_D", "condition_E")

# Fields preserved per proposal, per RA_blinding_spec.yaml.
PRESERVED = (
    "screening_status",
    "R", "I", "T",
    "condition_A", "condition_B", "condition_C", "condition_D", "condition_E",
    "relational_result",
    "primary_mechanism",
    "confidence",
)


def load_aliases() -> dict[str, str]:
    """Parse the flat `aliases:` block of actor_label_aliases.yaml without a YAML dep."""
    text = ALIASES.read_text(encoding="utf-8")
    out: dict[str, str] = {}
    in_block = False
    for line in text.splitlines():
        if line.startswith("aliases:"):
            in_block = True
            continue
        if in_block:
            if line and not line.startswith((" ", "\t")):
                break
            m = re.match(r'\s+"(.+?)"\s*:\s*"(.+?)"\s*$', line)
            if m:
                out[normalize_label(m.group(1))] = m.group(2)
    return out


def normalize_label(value: str) -> str:
    """NFKC, quote/dash normalization, casefold, trim, whitespace collapse,
    trailing trivial punctuation removal. No fuzzy matching, no entity resolution."""
    s = unicodedata.normalize("NFKC", str(value))
    s = s.replace("‘", "'").replace("’", "'")
    s = s.replace("“", '"').replace("”", '"')
    s = re.sub(r"[‐-―−]", "-", s)
    s = s.casefold()
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"[.,;:]+$", "", s).strip()
    return s


def normalized_label_set(actor_list, aliases: dict[str, str]) -> list[str] | None:
    """Normalized, alias-resolved, sorted, de-duplicated actor *labels* only.

    actor.role is dropped entirely: the blinding spec forbids it, and structural
    placement (R / I / T) already carries the role information."""
    if actor_list is None:
        return None
    labels = set()
    for actor in actor_list:
        norm = normalize_label(actor.get("label", ""))
        if not norm:
            continue
        labels.add(normalize_label(aliases.get(norm, norm)))
    return sorted(labels)


def build_proposal(record: dict, aliases: dict[str, str]) -> dict:
    test = record["relational_test"]
    return {
        "screening_status": record["screening_status"],
        "R": normalized_label_set(record.get("R"), aliases),
        "I": normalized_label_set(record.get("I"), aliases),
        "T": normalized_label_set(record.get("T"), aliases),
        "condition_A": test["condition_A"]["result"],
        "condition_B": test["condition_B"]["result"],
        "condition_C": test["condition_C"]["result"],
        "condition_D": test["condition_D"]["result"],
        "condition_E": test["condition_E"]["result"],
        "relational_result": record["relational_result"],
        "primary_mechanism": record["primary_mechanism"],
        "confidence": record["confidence"],
    }


def main() -> None:
    aliases = load_aliases()

    candidates = json.loads(CODING_INPUT.read_text(encoding="utf-8"))
    candidate_order = [c["candidate_id"] for c in candidates]
    candidate_by_id = {c["candidate_id"]: c for c in candidates}

    codings = []
    for path in SOURCES:
        records = json.loads(path.read_text(encoding="utf-8"))
        by_id = {r["candidate_id"]: r for r in records}
        if sorted(by_id) != sorted(candidate_order):
            raise SystemExit(f"candidate universe mismatch in {path.name}")
        codings.append((path, by_id))

    # Cryptographically secure permutation of the four codings onto Coder A-D.
    labels = ["Coder A", "Coder B", "Coder C", "Coder D"]
    indices = list(range(4))
    permutation: list[int] = []
    while indices:
        permutation.append(indices.pop(secrets.randbelow(len(indices))))
    # permutation[k] = index into SOURCES that receives labels[k]

    blind = []
    for cid in candidate_order:
        cand = candidate_by_id[cid]
        entry = {
            "candidate_id": cid,
            "source_location": cand["source_location"],
            "focal_excerpt": cand["focal_excerpt"],
            "parent_context": cand["parent_context"],
            "same_act_context_refs": cand["same_act_context_refs"],
            "candidate_origin": cand.get("candidate_origin"),
            "proposals": {},
        }
        for label, src_index in zip(labels, permutation):
            entry["proposals"][label] = build_proposal(codings[src_index][1][cid], aliases)
        blind.append(entry)

    package = {
        "package": "RA_blind_input",
        "protocol_version": "1.0.0",
        "blinding_spec_version": "1.0.0",
        "methodology_version": "1.1.0",
        "celex": "32021R1119",
        "candidate_count": len(blind),
        "coders_presented": labels,
        "notice": (
            "The four proposals are independent replicas presented in a cryptographically "
            "randomized order. No proposal is a reference or ground truth. Provider, model, "
            "family, replicate order and execution metadata are not present in this package "
            "and must not be inferred. Agreement counts are features of the proposals only "
            "and are never a truth rule."
        ),
        "candidates": blind,
    }

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    PRIVATE_DIR.mkdir(parents=True, exist_ok=True)
    (OUT_DIR / "RA_blind_input.json").write_text(
        json.dumps(package, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    mapping_lines = [
        "mapping: RA_4way_identity_mapping",
        "status: researcher_controlled",
        "accessible_to_RA: false",
        "generation_method: os_csprng_random_permutation",
        "protocol_version: 1.0.0",
        "assignments:",
    ]
    for label, src_index in zip(labels, permutation):
        rel = SOURCES[src_index].relative_to(ROOT).as_posix()
        mapping_lines.append(f'  "{label}": "{rel}"')
    mapping_lines.append("")
    (PRIVATE_DIR / "RA_4way_identity_mapping.yaml").write_text(
        "\n".join(mapping_lines), encoding="utf-8"
    )

    print("BLIND_RA_PACKAGE_READY")


if __name__ == "__main__":
    main()
