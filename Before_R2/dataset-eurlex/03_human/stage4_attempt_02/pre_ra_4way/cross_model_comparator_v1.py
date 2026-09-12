#!/usr/bin/env python3
"""Build the derived, non-adjudicative four-way pre-RA comparison.

This comparator is intentionally independent of validate_reference_logic.py.
It never imports or modifies that validator and writes only inside pre_ra_4way/.
"""

from __future__ import annotations

import copy
import csv
import hashlib
import json
import math
import re
import unicodedata
from collections import Counter, OrderedDict
from datetime import date
from pathlib import Path
from typing import Any, Iterable


VERSION = "1.0.0"
PROTOCOL_VERSION = "1.0.0"
METHODOLOGY_VERSION = "1.1.0"
HERE = Path(__file__).resolve().parent
STAGE = HERE.parent
ROOT = HERE.parents[2]

CONDITIONS = ("condition_A", "condition_B", "condition_C", "condition_D", "condition_E")
SHORT_CONDITIONS = ("A", "B", "C", "D", "E")

CODERS: OrderedDict[str, Path] = OrderedDict(
    [
        ("Terra-R1", STAGE / "R1_output.json"),
        ("Terra-R2", STAGE / "R2_output.json"),
        ("Claude-R1", STAGE / "claude_replication_01" / "Claude_R1_output.json"),
        ("Claude-R2", STAGE / "claude_replication_01" / "Claude_R2_output.json"),
    ]
)

PREFIX = {
    "Terra-R1": "terra_r1",
    "Terra-R2": "terra_r2",
    "Claude-R1": "claude_r1",
    "Claude-R2": "claude_r2",
}

PAIRS = (
    ("Terra-R1", "Terra-R2"),
    ("Claude-R1", "Claude-R2"),
    ("Terra-R1", "Claude-R1"),
    ("Terra-R1", "Claude-R2"),
    ("Terra-R2", "Claude-R1"),
    ("Terra-R2", "Claude-R2"),
)

# Recorded before derived artifacts were created. These are integrity controls,
# not substantive results.
PROTECTED_SHA256 = {
    "02_corpus/act.md": "b24a02ea241ca631b606660bb48bb5a2222b29f849c4e4552fb99f871b2e8fd4",
    "methodology/v1.1.0/codebook.md": "c160e153907a786c04070cb09f6e9baa11de709a4432a5f89ebe375a8a7eb472",
    "methodology/v1.1.0/experimental_output_schema.json": "aaa0c351836120cadef86d051ef8d950675577afbabefd5ac5d3931f33ae875c",
    "methodology/v1.1.0/methodology_manifest.yaml": "4bb92019f932a836707d81d087503b60913b3770cdc3881b05fc0662d036fb00",
    "methodology/v1.1.0/reference_coding_schema.json": "abbc4325a5e749cf31836fb24314c27ed22061d6e6539fb435fce8236d5ad2ec",
    "methodology/v1.1.0/strings.yaml": "242c288db010320619a0cdb58c38cb73c6be8aa499497ccfae7bfbfc33f34305",
    "03_human/stage4_attempt_02/R1_output_raw.json": "af443a0f98307a9d989816c5f0e15d4aa009553174eb470753f4134cb6640f29",
    "03_human/stage4_attempt_02/R1_output.json": "af443a0f98307a9d989816c5f0e15d4aa009553174eb470753f4134cb6640f29",
    "03_human/stage4_attempt_02/R2_output_raw.json": "18855b2053447d061be3c1fcfae9ebdbd579620d922a6394223f57b0f21ad2f6",
    "03_human/stage4_attempt_02/R2_output.json": "18855b2053447d061be3c1fcfae9ebdbd579620d922a6394223f57b0f21ad2f6",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_R1_output_raw.json": "f997f3d763836887d858528e78ac3753be9fb0dfe23bfd0fa0bf885ea4870daa",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_R1_output.json": "86cf2af470fad31165efd0af8ac1cb02fa77c20b6bacad265a40601d5611e2e5",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_R2_output_raw.json": "e9cecdb87207a636d94b54e5e86e4d099986bac77fcb6428844b2631a5844df5",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_R2_output.json": "cfea747db3441279cb4293092a7cc9435434bb967880ae0f5404e1b401f5a06e",
    "03_human/stage4_attempt_02/validate_reference_logic.py": "b502413da838f1b447ab67b49fe073ab0a1d6a076fe86a9298d9d4a021ff998d",
    "03_human/stage4_attempt_02/candidate_reconstruction.json": "38416b70f9337ad66dbd6c6d41d280d18ad9e5694e0cacb0c938c5833b1aff55",
    "03_human/stage4_attempt_02/R1_coding_input.json": "813b984c5e80aa03c98bc4399f40644c7d802eedd45f55a2d7a9a787a82d0b38",
    "03_human/stage4_attempt_02/R2_coding_input.json": "813b984c5e80aa03c98bc4399f40644c7d802eedd45f55a2d7a9a787a82d0b38",
}

PROVENANCE_INPUTS = (
    "02_corpus/act.md",
    "methodology/v1.1.0/codebook.md",
    "methodology/v1.1.0/reference_coding_schema.json",
    "03_human/stage4_attempt_02/candidate_reconstruction.json",
    "03_human/stage4_attempt_02/R1_coding_input.json",
    "03_human/stage4_attempt_02/R2_coding_input.json",
    "03_human/stage4_attempt_02/R1_output_raw.json",
    "03_human/stage4_attempt_02/R1_output.json",
    "03_human/stage4_attempt_02/R2_output_raw.json",
    "03_human/stage4_attempt_02/R2_output.json",
    "03_human/stage4_attempt_02/R1_context_manifest.yaml",
    "03_human/stage4_attempt_02/R2_context_manifest.yaml",
    "03_human/stage4_attempt_02/R1_validation_log.md",
    "03_human/stage4_attempt_02/R2_validation_log.md",
    "03_human/stage4_attempt_02/validate_reference_logic.py",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_R1_output_raw.json",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_R1_output.json",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_R2_output_raw.json",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_R2_output.json",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_R1_context_manifest.yaml",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_R2_context_manifest.yaml",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_R1_validation_log.md",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_R2_validation_log.md",
    "03_human/stage4_attempt_02/claude_replication_01/Claude_replication_execution_log.md",
    "03_human/stage4_attempt_02/claude_replication_01/CLAUDE_REPLICATION_MANIFEST.yaml",
    "03_human/stage4_attempt_02/pre_ra_4way/actor_label_aliases.yaml",
)

STATIC_OUTPUTS = (
    "cross_model_comparator_v1.py",
    "actor_label_aliases.yaml",
    "TERRA_EXECUTION_PROVENANCE_NOTE.md",
    "KNOWN_LIMITATIONS_V1_1.md",
    "RA_4WAY_PROTOCOL.md",
    "RA_blinding_spec.yaml",
)

GENERATED_OUTPUTS = (
    "cross_model_comparison.csv",
    "cross_model_comparison_report.md",
    "pre_ra_4way_validation_log.md",
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8-sig") as handle:
        return json.load(handle)


def write_text(path: Path, value: str) -> None:
    path.write_text(value.rstrip() + "\n", encoding="utf-8", newline="\n")


def normalize_text(value: Any) -> str:
    if value is None:
        return ""
    text = unicodedata.normalize("NFKC", str(value))
    text = text.translate(
        str.maketrans(
            {
                "‘": "'",
                "’": "'",
                "‚": "'",
                "“": '"',
                "”": '"',
                "„": '"',
                "‐": "-",
                "‑": "-",
                "‒": "-",
                "–": "-",
                "—": "-",
                "―": "-",
            }
        )
    )
    text = re.sub(r"\s+", " ", text).strip().casefold()
    text = re.sub(r"[\s\.,;:]+$", "", text)
    return text


def load_aliases(path: Path) -> dict[str, str]:
    """Read only the explicit two-space mappings below `aliases:`.

    This deliberately avoids fuzzy or implicit matching and avoids a PyYAML
    dependency. Quoted YAML scalars are also valid JSON strings.
    """
    aliases: dict[str, str] = {}
    in_aliases = False
    for line in path.read_text(encoding="utf-8-sig").splitlines():
        if line == "aliases:":
            in_aliases = True
            continue
        if in_aliases and not line.startswith("  "):
            break
        if not in_aliases or not line.strip() or line.lstrip().startswith("#"):
            continue
        match = re.fullmatch(r'  ("(?:[^"\\]|\\.)*"):\s+("(?:[^"\\]|\\.)*")', line)
        if not match:
            raise ValueError(f"Unsupported alias line: {line}")
        source = normalize_text(json.loads(match.group(1)))
        target = normalize_text(json.loads(match.group(2)))
        if source in aliases and aliases[source] != target:
            raise ValueError(f"Conflicting alias: {source}")
        aliases[source] = target
    if not aliases:
        raise ValueError("No explicit aliases loaded")
    return aliases


ALIASES = load_aliases(HERE / "actor_label_aliases.yaml")


def normalize_actor_label(label: Any) -> str:
    normalized = normalize_text(label)
    return ALIASES.get(normalized, normalized)


def actor_label_set(value: Any) -> tuple[str, ...]:
    """Return only normalized actor labels; actor.role is intentionally ignored."""
    if not value:
        return ()
    if isinstance(value, dict):
        value = [value]
    labels = {normalize_actor_label(item.get("label")) for item in value if item.get("label")}
    return tuple(sorted(labels))


def condition_vector(record: dict[str, Any]) -> tuple[str, ...]:
    return tuple(record["relational_test"][name]["result"] for name in CONDITIONS)


def substantive_signature(record: dict[str, Any]) -> tuple[Any, ...]:
    """Principal signature requested for four-way comparison.

    Excluded by design: screening_status, actor.role, action, object,
    mediating_function, evidence wording, notes, interpretive_note, confidence,
    and all other free prose or metadata.
    """
    return (
        actor_label_set(record.get("R")),
        actor_label_set(record.get("I")),
        actor_label_set(record.get("T")),
        condition_vector(record),
        record.get("relational_result"),
        record.get("primary_mechanism"),
    )


def all_same(values: Iterable[Any]) -> bool:
    values = list(values)
    return all(value == values[0] for value in values[1:])


def observed_agreement(values_a: list[Any], values_b: list[Any]) -> float:
    if len(values_a) != len(values_b) or not values_a:
        raise ValueError("Agreement requires two non-empty equal-length vectors")
    return sum(a == b for a, b in zip(values_a, values_b)) / len(values_a)


def cohen_kappa(values_a: list[Any], values_b: list[Any]) -> float | None:
    po = observed_agreement(values_a, values_b)
    total = len(values_a)
    count_a = Counter(values_a)
    count_b = Counter(values_b)
    categories = set(count_a) | set(count_b)
    pe = sum((count_a[c] / total) * (count_b[c] / total) for c in categories)
    denominator = 1.0 - pe
    if math.isclose(denominator, 0.0, abs_tol=1e-15):
        return None
    return (po - pe) / denominator


def jaccard(set_a: set[str], set_b: set[str]) -> float:
    union = set_a | set_b
    return 1.0 if not union else len(set_a & set_b) / len(union)


def metric(values_a: list[Any], values_b: list[Any], include_kappa: bool) -> dict[str, Any]:
    result: dict[str, Any] = {"observed_agreement": observed_agreement(values_a, values_b)}
    if include_kappa:
        result["cohen_kappa"] = cohen_kappa(values_a, values_b)
    return result


def make_pair_metrics(
    coder_a: str,
    coder_b: str,
    ids: list[str],
    by_coder: dict[str, dict[str, dict[str, Any]]],
) -> dict[str, Any]:
    records_a = [by_coder[coder_a][candidate_id] for candidate_id in ids]
    records_b = [by_coder[coder_b][candidate_id] for candidate_id in ids]

    def values(records: list[dict[str, Any]], getter) -> list[Any]:
        return [getter(record) for record in records]

    result: dict[str, Any] = {
        "pair": f"{coder_a} × {coder_b}",
        "relational_result": metric(
            values(records_a, lambda r: r["relational_result"]),
            values(records_b, lambda r: r["relational_result"]),
            True,
        ),
        "screening_status": metric(
            values(records_a, lambda r: r["screening_status"]),
            values(records_b, lambda r: r["screening_status"]),
            True,
        ),
    }
    for name, short in zip(CONDITIONS, SHORT_CONDITIONS):
        result[f"condition_{short}"] = metric(
            values(records_a, lambda r, n=name: r["relational_test"][n]["result"]),
            values(records_b, lambda r, n=name: r["relational_test"][n]["result"]),
            True,
        )
    result["conditions_A_E_joint"] = metric(
        values(records_a, condition_vector), values(records_b, condition_vector), True
    )
    for role in ("R", "I", "T"):
        result[role] = metric(
            values(records_a, lambda r, key=role: actor_label_set(r.get(key))),
            values(records_b, lambda r, key=role: actor_label_set(r.get(key))),
            False,
        )
    result["primary_mechanism"] = metric(
        values(records_a, lambda r: r["primary_mechanism"]),
        values(records_b, lambda r: r["primary_mechanism"]),
        True,
    )
    result["substantive_signature"] = metric(
        values(records_a, substantive_signature), values(records_b, substantive_signature), False
    )

    positive_a = {r["candidate_id"] for r in records_a if r["relational_result"] == "positive"}
    positive_b = {r["candidate_id"] for r in records_b if r["relational_result"] == "positive"}
    negative_a = {r["candidate_id"] for r in records_a if r["relational_result"] == "negative"}
    negative_b = {r["candidate_id"] for r in records_b if r["relational_result"] == "negative"}
    d_yes_a = {
        r["candidate_id"]
        for r in records_a
        if r["relational_test"]["condition_D"]["result"] == "YES"
    }
    d_yes_b = {
        r["candidate_id"]
        for r in records_b
        if r["relational_test"]["condition_D"]["result"] == "YES"
    }
    result["positive_sets"] = {
        "coder_a_count": len(positive_a),
        "coder_b_count": len(positive_b),
        "intersection_count": len(positive_a & positive_b),
        "union_count": len(positive_a | positive_b),
        "jaccard": jaccard(positive_a, positive_b),
    }
    result["negative_sets"] = {
        "coder_a_count": len(negative_a),
        "coder_b_count": len(negative_b),
        "intersection_count": len(negative_a & negative_b),
        "union_count": len(negative_a | negative_b),
        "jaccard": jaccard(negative_a, negative_b),
    }
    result["D_yes_sets"] = {
        "coder_a_count": len(d_yes_a),
        "coder_b_count": len(d_yes_b),
        "intersection_count": len(d_yes_a & d_yes_b),
        "union_count": len(d_yes_a | d_yes_b),
        "jaccard": jaccard(d_yes_a, d_yes_b),
    }
    return result


def json_set(value: tuple[str, ...]) -> str:
    return json.dumps(list(value), ensure_ascii=False, separators=(",", ":"))


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def candidate_features(records: list[dict[str, Any]]) -> dict[str, Any]:
    results = [record["relational_result"] for record in records]
    screenings = [record["screening_status"] for record in records]
    role_sets = {role: [actor_label_set(record.get(role)) for record in records] for role in ("R", "I", "T")}
    conditions = [condition_vector(record) for record in records]
    mechanisms = [record["primary_mechanism"] for record in records]
    signatures = [substantive_signature(record) for record in records]
    return {
        "any_positive": "positive" in results,
        "positive_count_4": results.count("positive"),
        "any_conditional": "conditional" in results,
        "any_insufficient": (
            "insufficient_evidence" in results or "insufficient_evidence" in screenings
        ),
        "any_I_present": any(role_sets["I"]),
        "any_C_yes": any(vector[2] == "YES" for vector in conditions),
        "any_D_yes": any(vector[3] == "YES" for vector in conditions),
        "relational_result_unanimous": all_same(results),
        "R_unanimous": all_same(role_sets["R"]),
        "I_unanimous": all_same(role_sets["I"]),
        "T_unanimous": all_same(role_sets["T"]),
        "AE_unanimous": all_same(conditions),
        "primary_mechanism_unanimous": all_same(mechanisms),
        "substantive_disagreement": not all_same(signatures),
        "unanimously_negative": all(result == "negative" for result in results),
    }


def base_gate_reasons(features: dict[str, Any]) -> list[str]:
    reasons: list[str] = []
    if features["any_positive"]:
        reasons.append("rule_1_positive_in_any_replica")
    if features["any_conditional"]:
        reasons.append("rule_2_conditional_in_any_replica")
    if features["any_insufficient"]:
        reasons.append("rule_3_insufficient_evidence_in_any_replica")
    if features["any_D_yes"]:
        reasons.append("rule_4_D_yes_in_any_replica")
    if not features["relational_result_unanimous"]:
        reasons.append("rule_5_relational_result_divergence")
    if not features["I_unanimous"]:
        reasons.append("rule_6_substantive_I_divergence")
    if (
        not features["unanimously_negative"]
        and not (features["R_unanimous"] and features["I_unanimous"] and features["T_unanimous"])
    ):
        reasons.append("rule_7_R_I_T_divergence_non_unanimous_negative")
    return reasons


def choose_audit_sample(
    eligible_ids: list[str], current_validated_hashes: list[str]
) -> tuple[set[str], str]:
    seed_material = f"pre_ra_4way|{PROTOCOL_VERSION}|" + "|".join(current_validated_hashes)
    seed = hashlib.sha256(seed_material.encode("utf-8")).hexdigest()
    if not eligible_ids:
        return set(), seed
    sample_size = min(len(eligible_ids), max(3, math.ceil(0.10 * len(eligible_ids))))
    ranked = sorted(
        eligible_ids,
        key=lambda candidate_id: hashlib.sha256(f"{seed}|{candidate_id}".encode("utf-8")).hexdigest(),
    )
    return set(ranked[:sample_size]), seed


def fmt_fraction(value: float) -> str:
    return f"{value:.3f} ({value * 100:.1f}%)"


def fmt_kappa(value: float | None) -> str:
    return "NA" if value is None else f"{value:.3f}"


def fmt_set(value: tuple[str, ...]) -> str:
    return "∅" if not value else "; ".join(value)


def fmt_location(location: dict[str, Any]) -> str:
    parts: list[str] = []
    if location.get("recital") is not None:
        parts.append(f"Recital {location['recital']}")
    else:
        if location.get("article") is not None:
            parts.append(f"Article {location['article']}")
        if location.get("paragraph") is not None:
            parts.append(f"paragraph {location['paragraph']}")
        if location.get("point") is not None:
            parts.append(f"point {location['point']}")
        if location.get("subparagraph") is not None:
            parts.append(f"subparagraph {location['subparagraph']}")
    if location.get("line_start") is not None:
        line_end = location.get("line_end", location["line_start"])
        suffix = f"line {location['line_start']}" if line_end == location["line_start"] else f"lines {location['line_start']}–{line_end}"
        parts.append(suffix)
    return ", ".join(parts) or canonical_json(location)


def distribution_rows(by_coder: dict[str, dict[str, dict[str, Any]]], ids: list[str]) -> list[tuple[str, list[int]]]:
    rows: list[tuple[str, list[int]]] = []
    for indicator in ("positive", "negative", "conditional", "insufficient_evidence"):
        rows.append(
            (
                indicator,
                [
                    sum(by_coder[coder][cid]["relational_result"] == indicator for cid in ids)
                    for coder in CODERS
                ],
            )
        )
    for confidence in ("high", "medium", "low"):
        rows.append(
            (
                f"confidence={confidence}",
                [sum(by_coder[coder][cid]["confidence"] == confidence for cid in ids) for coder in CODERS],
            )
        )
    rows.extend(
        [
            (
                "I != null",
                [sum(bool(actor_label_set(by_coder[coder][cid].get("I"))) for cid in ids) for coder in CODERS],
            ),
            (
                "C=YES",
                [
                    sum(
                        by_coder[coder][cid]["relational_test"]["condition_C"]["result"] == "YES"
                        for cid in ids
                    )
                    for coder in CODERS
                ],
            ),
            (
                "D=YES",
                [
                    sum(
                        by_coder[coder][cid]["relational_test"]["condition_D"]["result"] == "YES"
                        for cid in ids
                    )
                    for coder in CODERS
                ],
            ),
        ]
    )
    return rows


def render_report(
    ids: list[str],
    inputs_by_id: dict[str, dict[str, Any]],
    by_coder: dict[str, dict[str, dict[str, Any]]],
    pair_metrics: dict[tuple[str, str], dict[str, Any]],
    positive_union: set[str],
    gate_ids: set[str],
    audit_ids: set[str],
    audit_seed: str,
) -> str:
    lines = [
        "# Four-way pre-RA comparison — CELEX 32021R1119",
        "",
        f"Comparator version: {VERSION}. Methodology: locked v{METHODOLOGY_VERSION}. Universe: {len(ids)} frozen candidates.",
        "",
        "This report is strictly descriptive. It treats Terra-R1, Terra-R2, Claude-R1, and Claude-R2 as symmetric independent replicas. It does not adjudicate, choose a winner, execute RA, execute a human gate, or lock a benchmark.",
        "",
        "## Distributions directly recalculated from validated outputs",
        "",
        "| indicador | Terra-R1 | Terra-R2 | Claude-R1 | Claude-R2 |",
        "|---|---:|---:|---:|---:|",
    ]
    for label, values in distribution_rows(by_coder, ids):
        lines.append(f"| {label} | {values[0]} | {values[1]} | {values[2]} | {values[3]} |")

    lines.extend(
        [
            "",
            "`screening_status` is analyzed separately from the principal substantive signature. `I != null` denotes a non-empty normalized I-label set and, under the current validator limitation, is not by itself proof of mediation.",
            "",
            "## Pairwise metrics",
            "",
            "| pair | relational agreement | κ relational | screening agreement | κ screening | A–E joint agreement | R agreement | I agreement | T agreement | mechanism agreement | full substantive signature | positive Jaccard | D=YES Jaccard |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for pair in PAIRS:
        m = pair_metrics[pair]
        lines.append(
            "| {pair} | {rel} | {krel} | {screen} | {kscreen} | {ae} | {r} | {i} | {t} | {mech} | {sig} | {posj:.3f} | {dj:.3f} |".format(
                pair=m["pair"],
                rel=fmt_fraction(m["relational_result"]["observed_agreement"]),
                krel=fmt_kappa(m["relational_result"]["cohen_kappa"]),
                screen=fmt_fraction(m["screening_status"]["observed_agreement"]),
                kscreen=fmt_kappa(m["screening_status"]["cohen_kappa"]),
                ae=fmt_fraction(m["conditions_A_E_joint"]["observed_agreement"]),
                r=fmt_fraction(m["R"]["observed_agreement"]),
                i=fmt_fraction(m["I"]["observed_agreement"]),
                t=fmt_fraction(m["T"]["observed_agreement"]),
                mech=fmt_fraction(m["primary_mechanism"]["observed_agreement"]),
                sig=fmt_fraction(m["substantive_signature"]["observed_agreement"]),
                posj=m["positive_sets"]["jaccard"],
                dj=m["D_yes_sets"]["jaccard"],
            )
        )
    lines.extend(
        [
            "",
            "Cohen's kappa is calculated for nominal scalar/vector categories where meaningful: relational result, screening status, each A–E condition, the joint A–E vector, and primary mechanism. It is not imposed on actor-label sets or the composite signature. `NA` means expected agreement is 1 and kappa is undefined. The strong negative-class imbalance can inflate observed agreement and destabilize kappa, so neither is interpreted alone.",
            "",
            "### Condition-specific agreement and kappa",
            "",
            "| pair | A agreement / κ | B agreement / κ | C agreement / κ | D agreement / κ | E agreement / κ | joint A–E agreement / κ |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for pair in PAIRS:
        m = pair_metrics[pair]
        cells = []
        for short in SHORT_CONDITIONS:
            value = m[f"condition_{short}"]
            cells.append(
                f"{value['observed_agreement']:.3f} / {fmt_kappa(value['cohen_kappa'])}"
            )
        joint = m["conditions_A_E_joint"]
        lines.append(
            f"| {m['pair']} | " + " | ".join(cells) + f" | {joint['observed_agreement']:.3f} / {fmt_kappa(joint['cohen_kappa'])} |"
        )

    lines.extend(
        [
            "",
            "## Within-family stability",
            "",
            "The majority class and rare positives are separated below. Negative-set overlap describes stability of the dominant class; positive-set overlap describes stability of rare affirmative findings.",
            "",
            "| family pair | negatives A/B | negative intersection/union | negative Jaccard | positives A/B | positive intersection/union | positive Jaccard |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for pair in PAIRS[:2]:
        m = pair_metrics[pair]
        n = m["negative_sets"]
        p = m["positive_sets"]
        lines.append(
            f"| {m['pair']} | {n['coder_a_count']}/{n['coder_b_count']} | {n['intersection_count']}/{n['union_count']} | {n['jaccard']:.3f} | {p['coder_a_count']}/{p['coder_b_count']} | {p['intersection_count']}/{p['union_count']} | {p['jaccard']:.3f} |"
        )
    terra = pair_metrics[PAIRS[0]]
    claude = pair_metrics[PAIRS[1]]
    lines.extend(
        [
            "",
            f"For Terra-R1 × Terra-R2, dominant-negative stability is {terra['negative_sets']['jaccard']:.3f} by negative-set Jaccard, while rare-positive stability is {terra['positive_sets']['jaccard']:.3f}. For Claude-R1 × Claude-R2, the corresponding values are {claude['negative_sets']['jaccard']:.3f} and {claude['positive_sets']['jaccard']:.3f}. These are descriptive profiles, not rankings.",
            "",
            "## Cross-family pairs",
            "",
            "| pair | relational agreement / κ | full signature agreement | positives intersection/union | positive Jaccard | D=YES intersection/union | D=YES Jaccard |",
            "|---|---:|---:|---:|---:|---:|---:|",
        ]
    )
    for pair in PAIRS[2:]:
        m = pair_metrics[pair]
        p = m["positive_sets"]
        d = m["D_yes_sets"]
        lines.append(
            f"| {m['pair']} | {m['relational_result']['observed_agreement']:.3f} / {fmt_kappa(m['relational_result']['cohen_kappa'])} | {m['substantive_signature']['observed_agreement']:.3f} | {p['intersection_count']}/{p['union_count']} | {p['jaccard']:.3f} | {d['intersection_count']}/{d['union_count']} | {d['jaccard']:.3f} |"
        )

    lines.extend(
        [
            "",
            "## Empirical union of positive candidates",
            "",
            f"The positive union was recalculated directly from the four validated outputs and contains **{len(positive_union)}** candidates. Every one is marked for the future human gate under rule 1; no ID was hardcoded.",
            "",
        ]
    )
    for candidate_id in ids:
        if candidate_id not in positive_union:
            continue
        packet = inputs_by_id[candidate_id]
        lines.extend(
            [
                f"### {candidate_id}",
                "",
                f"Location: {fmt_location(packet['source_location'])}",
                "",
                f"> {re.sub(r'\s+', ' ', packet['focal_excerpt']).strip()}",
                "",
                "| coder | relational result | R | I | T | A–E | primary mechanism |",
                "|---|---|---|---|---|---|---|",
            ]
        )
        for coder in CODERS:
            record = by_coder[coder][candidate_id]
            ae = "/".join(condition_vector(record))
            lines.append(
                f"| {coder} | {record['relational_result']} | {fmt_set(actor_label_set(record.get('R')))} | {fmt_set(actor_label_set(record.get('I')))} | {fmt_set(actor_label_set(record.get('T')))} | {ae} | {record['primary_mechanism']} |"
            )
        lines.extend(["", "No adjudication is made for this candidate.", ""])

    lines.extend(
        [
            "## Prepared future human-gate queue",
            "",
            f"Rules 1–7 plus the reproducible rule-10 audit sample currently mark **{len(gate_ids)}** candidates. The audit sample contains {len(audit_ids)} candidates selected from otherwise untriggered unanimous negatives. Its SHA-256 ranking seed is `{audit_seed}`. Rules 8–9 depend on a future RA and therefore cannot yet be evaluated. Marking a row is queue preparation only; no human gate was executed.",
            "",
            "## Interpretive boundary",
            "",
            "The full substantive signature excludes screening status and all free prose, including `actor.role`, action, object, evidence wording, notes, interpretive note, and confidence. Explicit actor aliases are auditable in `actor_label_aliases.yaml`; unlisted non-trivial labels remain distinct. Provenance limitations are documented separately and prevent causal attribution of cross-family differences.",
            "",
            "As quatro codificações são réplicas independentes. As diferenças observadas caracterizam perfis distintos de reconstrução e abstenção, não estabelecem superioridade causal de uma família de modelos.",
        ]
    )
    return "\n".join(lines)


def write_csv(
    ids: list[str],
    inputs_by_id: dict[str, dict[str, Any]],
    by_coder: dict[str, dict[str, dict[str, Any]]],
    features_by_id: dict[str, dict[str, Any]],
    reasons_by_id: dict[str, list[str]],
    audit_ids: set[str],
) -> None:
    fields = ["candidate_id", "source_location"]
    for coder in CODERS:
        prefix = PREFIX[coder]
        fields.extend(
            [
                f"{prefix}_screening_status",
                f"{prefix}_R_normalized",
                f"{prefix}_I_normalized",
                f"{prefix}_T_normalized",
                f"{prefix}_A",
                f"{prefix}_B",
                f"{prefix}_C",
                f"{prefix}_D",
                f"{prefix}_E",
                f"{prefix}_relational_result",
                f"{prefix}_primary_mechanism",
                f"{prefix}_confidence",
            ]
        )
    fields.extend(
        [
            "any_positive",
            "positive_count_4",
            "any_conditional",
            "any_insufficient",
            "any_I_present",
            "any_C_yes",
            "any_D_yes",
            "relational_result_unanimous",
            "R_unanimous",
            "I_unanimous",
            "T_unanimous",
            "AE_unanimous",
            "primary_mechanism_unanimous",
            "substantive_disagreement",
            "audit_sample_rule_10",
            "human_gate_trigger",
            "human_gate_reason",
        ]
    )
    with (HERE / "cross_model_comparison.csv").open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        for candidate_id in ids:
            row: dict[str, Any] = {
                "candidate_id": candidate_id,
                "source_location": canonical_json(inputs_by_id[candidate_id]["source_location"]),
            }
            for coder in CODERS:
                prefix = PREFIX[coder]
                record = by_coder[coder][candidate_id]
                row.update(
                    {
                        f"{prefix}_screening_status": record["screening_status"],
                        f"{prefix}_R_normalized": json_set(actor_label_set(record.get("R"))),
                        f"{prefix}_I_normalized": json_set(actor_label_set(record.get("I"))),
                        f"{prefix}_T_normalized": json_set(actor_label_set(record.get("T"))),
                        f"{prefix}_A": condition_vector(record)[0],
                        f"{prefix}_B": condition_vector(record)[1],
                        f"{prefix}_C": condition_vector(record)[2],
                        f"{prefix}_D": condition_vector(record)[3],
                        f"{prefix}_E": condition_vector(record)[4],
                        f"{prefix}_relational_result": record["relational_result"],
                        f"{prefix}_primary_mechanism": record["primary_mechanism"],
                        f"{prefix}_confidence": record["confidence"],
                    }
                )
            features = features_by_id[candidate_id]
            for key in (
                "any_positive",
                "any_conditional",
                "any_insufficient",
                "any_I_present",
                "any_C_yes",
                "any_D_yes",
                "relational_result_unanimous",
                "R_unanimous",
                "I_unanimous",
                "T_unanimous",
                "AE_unanimous",
                "primary_mechanism_unanimous",
                "substantive_disagreement",
            ):
                row[key] = bool_text(features[key])
            row["positive_count_4"] = features["positive_count_4"]
            row["audit_sample_rule_10"] = bool_text(candidate_id in audit_ids)
            row["human_gate_trigger"] = bool_text(bool(reasons_by_id[candidate_id]))
            row["human_gate_reason"] = " | ".join(reasons_by_id[candidate_id])
            writer.writerow(row)


def run_abstract_tests() -> list[str]:
    base = {
        "screening_status": "candidate",
        "R": [{"label": " European Commission. ", "role": "regulator wording A", "evidence_refs": ["e1"]}],
        "I": [{"label": "European Environment Agency (EEA)", "role": "style A", "evidence_refs": ["e1"]}],
        "T": [{"label": "Member States", "role": "target style A", "evidence_refs": ["e1"]}],
        "relational_test": {
            name: {"result": "YES", "evidence_refs": ["e1"]} for name in CONDITIONS
        },
        "relational_result": "positive",
        "primary_mechanism": "monitoring_supervision",
        "action": ["wording A"],
        "object": ["wording A"],
        "mediating_function": ["wording A"],
        "evidence_items": [{"quote": "wording A"}],
        "interpretive_note": "wording A",
        "notes": ["wording A"],
        "confidence": "high",
    }
    stylistic = copy.deepcopy(base)
    stylistic["screening_status"] = "direct_relationship"
    stylistic["R"][0]["label"] = "commission"
    stylistic["R"][0]["role"] = "completely different free prose"
    stylistic["I"][0]["label"] = " EEA "
    stylistic["I"][0]["role"] = "another free-text role"
    stylistic["action"] = ["different action prose"]
    stylistic["object"] = ["different object prose"]
    stylistic["mediating_function"] = ["different function prose"]
    stylistic["evidence_items"] = [{"quote": "different evidence prose"}]
    stylistic["interpretive_note"] = "different note"
    stylistic["notes"] = ["different notes"]
    stylistic["confidence"] = "low"
    assert substantive_signature(base) == substantive_signature(stylistic)

    conceptual = copy.deepcopy(stylistic)
    conceptual["relational_test"]["condition_D"]["result"] = "NO"
    assert substantive_signature(base) != substantive_signature(conceptual)

    actor_difference = copy.deepcopy(stylistic)
    actor_difference["T"][0]["label"] = "Council"
    assert substantive_signature(base) != substantive_signature(actor_difference)

    assert normalize_actor_label("  EUROPEAN   COMMISSION. ") == normalize_actor_label("Commission")
    assert normalize_text("A—B  ‘X’ ") == normalize_text("a-b 'x'")
    return [
        "principal signature ignores actor.role and excluded free-text fields",
        "principal signature ignores screening_status and confidence",
        "explicit aliases and conservative textual normalization collapse wording-only variants",
        "condition and actor-identity changes remain substantive disagreements",
        "no fuzzy matching is implemented",
    ]


def validate_and_write_log(
    ids: list[str],
    input_ids: list[str],
    by_coder: dict[str, dict[str, dict[str, Any]]],
    positive_union: set[str],
    gate_ids: set[str],
    audit_ids: set[str],
    audit_seed: str,
    abstract_checks: list[str],
) -> None:
    current_protected = {rel: sha256_file(ROOT / rel) for rel in PROTECTED_SHA256}
    assert current_protected == PROTECTED_SHA256
    assert len(ids) == 90 and len(set(ids)) == 90
    assert ids == input_ids
    for coder, records in by_coder.items():
        assert len(records) == 90, coder
        assert len(set(records)) == 90, coder
        assert set(records) == set(ids), coder
    with (HERE / "cross_model_comparison.csv").open("r", encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle))
    assert len(rows) == 90
    assert [row["candidate_id"] for row in rows] == ids
    recalculated_union = {
        candidate_id
        for candidate_id in ids
        if any(by_coder[coder][candidate_id]["relational_result"] == "positive" for coder in CODERS)
    }
    assert positive_union == recalculated_union
    forbidden_patterns = (
        "RA_output.json",
        "RA_output_raw.json",
        "human_review.csv",
        "human_gate_output.json",
        "benchmark.json",
    )
    assert not any((HERE / name).exists() for name in forbidden_patterns)
    assert set(HERE.glob("RA_*output*")) == set()

    lines = [
        "# Pre-RA four-way validation log",
        "",
        f"Date (local, date only): {date.today().isoformat()}",
        f"Comparator version: {VERSION}",
        "Status: **PASS**",
        "",
        "## Automated checks",
        "",
        "- PASS — each of the four validated outputs contains exactly 90 unique candidate IDs.",
        "- PASS — all four outputs contain exactly the same 90 IDs as the frozen R1/R2 coding input; no new ID exists.",
        "- PASS — all protected files match the SHA-256 baseline recorded before generation.",
        "- PASS — `cross_model_comparison.csv` contains exactly 90 data rows in frozen-input order.",
        "- PASS — the positive union was recomputed from current validated outputs, not hardcoded.",
        "- PASS — no RA output, human-gate output, or benchmark artifact was created.",
        "- PASS — all files written by this operation are inside `pre_ra_4way/`.",
    ]
    for check in abstract_checks:
        lines.append(f"- PASS — {check}.")
    lines.extend(
        [
            "",
            "## Protected-file SHA-256 verification",
            "",
            "| protected path | expected | observed |",
            "|---|---|---|",
        ]
    )
    for rel in sorted(PROTECTED_SHA256):
        lines.append(f"| `{rel}` | `{PROTECTED_SHA256[rel]}` | `{current_protected[rel]}` |")
    lines.extend(
        [
            "",
            "## Derived selection checks",
            "",
            f"- Positive union count: {len(positive_union)}",
            f"- Positive union IDs (derived): {', '.join(sorted(positive_union))}",
            f"- Current pre-RA human-gate queue count (rules 1–7 plus rule 10): {len(gate_ids)}",
            f"- Rule-10 audit sample count: {len(audit_ids)}",
            f"- Rule-10 audit sample IDs: {', '.join(sorted(audit_ids))}",
            f"- Audit ranking seed: `{audit_seed}`",
            "- RA-dependent rules 8–9: not evaluated because RA does not exist.",
            "",
            "## Explicit non-actions",
            "",
            "RA_NOT_EXECUTED",
            "",
            "HUMAN_GATE_NOT_EXECUTED",
            "",
            "BENCHMARK_NOT_LOCKED",
        ]
    )
    write_text(HERE / "pre_ra_4way_validation_log.md", "\n".join(lines))


def yaml_quote(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def write_manifest() -> None:
    lines = [
        "manifest: PRE_RA_4WAY_MANIFEST",
        f"date: {date.today().isoformat()}",
        "date_precision: day",
        "timestamp_recorded: false",
        "versions:",
        f"  comparator: {VERSION}",
        f"  RA_protocol: {PROTOCOL_VERSION}",
        f"  methodology: {METHODOLOGY_VERSION}",
        "inputs:",
    ]
    for rel in PROVENANCE_INPUTS:
        path = ROOT / rel
        if not path.is_file():
            raise FileNotFoundError(path)
        lines.extend(
            [
                f"  - path: {yaml_quote(rel)}",
                f"    sha256: {sha256_file(path)}",
            ]
        )
    lines.extend(["outputs:"])
    for name in STATIC_OUTPUTS + GENERATED_OUTPUTS:
        path = HERE / name
        if not path.is_file():
            raise FileNotFoundError(path)
        lines.extend(
            [
                f"  - path: {yaml_quote('03_human/stage4_attempt_02/pre_ra_4way/' + name)}",
                f"    sha256: {sha256_file(path)}",
            ]
        )
    lines.extend(
        [
            "  - path: \"03_human/stage4_attempt_02/pre_ra_4way/PRE_RA_4WAY_MANIFEST.yaml\"",
            "    sha256: null",
            "    hash_note: self-hash excluded because a manifest cannot contain its own final cryptographic hash",
            "status: pass",
            "state:",
            "  pre_ra_4way_prepared: true",
            "  cross_model_comparison_complete: true",
            "  RA_started: false",
            "  human_gate_started: false",
            "  benchmark_locked: false",
            "  experiment_started: false",
            "preservation:",
            "  protected_hashes_verified: true",
            "  original_outputs_modified: false",
            "  methodology_v1_1_0_modified: false",
            "  validator_modified: false",
            "limitations:",
            "  - exact Terra execution model/effort is not machine-recorded",
            "  - manifest self-hash must be recorded externally after finalization",
            "  - RA-dependent human-gate rules 8 and 9 remain unevaluable until a future RA exists",
        ]
    )
    write_text(HERE / "PRE_RA_4WAY_MANIFEST.yaml", "\n".join(lines))


def main() -> None:
    # Fail before writing if any protected artifact changed since the baseline.
    observed = {rel: sha256_file(ROOT / rel) for rel in PROTECTED_SHA256}
    if observed != PROTECTED_SHA256:
        changed = [rel for rel in PROTECTED_SHA256 if observed.get(rel) != PROTECTED_SHA256[rel]]
        raise RuntimeError(f"Protected-file hash mismatch: {changed}")

    coding_input = load_json(STAGE / "R1_coding_input.json")
    coding_input_r2 = load_json(STAGE / "R2_coding_input.json")
    input_ids = [record["candidate_id"] for record in coding_input]
    input_ids_r2 = [record["candidate_id"] for record in coding_input_r2]
    if input_ids != input_ids_r2:
        raise RuntimeError("R1/R2 input candidate IDs or order differ")
    ids = input_ids
    inputs_by_id = {record["candidate_id"]: record for record in coding_input}

    loaded = {coder: load_json(path) for coder, path in CODERS.items()}
    by_coder = {
        coder: {record["candidate_id"]: record for record in records}
        for coder, records in loaded.items()
    }
    if any(len(records) != len(by_coder[coder]) for coder, records in loaded.items()):
        raise RuntimeError("Duplicate candidate ID in a coder output")
    if any(set(records) != set(ids) for records in by_coder.values()):
        raise RuntimeError("Coder outputs do not match the frozen candidate universe")

    features_by_id: dict[str, dict[str, Any]] = {}
    reasons_by_id: dict[str, list[str]] = {}
    for candidate_id in ids:
        records = [by_coder[coder][candidate_id] for coder in CODERS]
        features = candidate_features(records)
        features_by_id[candidate_id] = features
        reasons_by_id[candidate_id] = base_gate_reasons(features)

    validated_hashes = [sha256_file(path) for path in CODERS.values()]
    eligible = [
        candidate_id
        for candidate_id in ids
        if features_by_id[candidate_id]["unanimously_negative"] and not reasons_by_id[candidate_id]
    ]
    audit_ids, audit_seed = choose_audit_sample(eligible, validated_hashes)
    for candidate_id in audit_ids:
        reasons_by_id[candidate_id].append("rule_10_random_audit_sample_unanimous_negative")
    gate_ids = {candidate_id for candidate_id in ids if reasons_by_id[candidate_id]}

    positive_union = {
        candidate_id
        for candidate_id in ids
        if any(by_coder[coder][candidate_id]["relational_result"] == "positive" for coder in CODERS)
    }
    pair_metrics = {
        pair: make_pair_metrics(pair[0], pair[1], ids, by_coder) for pair in PAIRS
    }

    write_csv(ids, inputs_by_id, by_coder, features_by_id, reasons_by_id, audit_ids)
    report = render_report(
        ids,
        inputs_by_id,
        by_coder,
        pair_metrics,
        positive_union,
        gate_ids,
        audit_ids,
        audit_seed,
    )
    write_text(HERE / "cross_model_comparison_report.md", report)
    abstract_checks = run_abstract_tests()
    validate_and_write_log(
        ids,
        input_ids_r2,
        by_coder,
        positive_union,
        gate_ids,
        audit_ids,
        audit_seed,
        abstract_checks,
    )
    write_manifest()

    # Final in-process checks after every derived write.
    assert {rel: sha256_file(ROOT / rel) for rel in PROTECTED_SHA256} == PROTECTED_SHA256
    assert (HERE / "PRE_RA_4WAY_MANIFEST.yaml").is_file()
    print(
        json.dumps(
            {
                "status": "PASS",
                "candidates": len(ids),
                "positive_union": len(positive_union),
                "human_gate_queue_pre_RA": len(gate_ids),
                "audit_sample": len(audit_ids),
                "pair_metrics": {metrics["pair"]: metrics for metrics in pair_metrics.values()},
                "RA_started": False,
                "human_gate_started": False,
                "benchmark_locked": False,
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
