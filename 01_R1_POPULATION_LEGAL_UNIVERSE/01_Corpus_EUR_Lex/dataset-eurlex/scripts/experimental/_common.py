"""Shared, state-guarded utilities for the future experimental pipeline."""

from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[2]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest().upper()


def _yaml_scalar(text: str, key: str) -> str | None:
    match = re.search(rf"^\s*{re.escape(key)}:\s*([^#\r\n]+)", text, re.MULTILINE)
    return match.group(1).strip().strip("'\"") if match else None


def assert_reference_locked(root: Path = ROOT) -> None:
    """Fail closed until the authorized reference-lock state exists."""
    project = (root / "config" / "project.yaml").read_text(encoding="utf-8")
    experiment = (root / "config" / "experiment.yaml").read_text(encoding="utf-8")
    project_status = re.search(r"(?m)^  status:\s*([^\s#]+)", project)
    reference_locked_match = re.search(r"(?m)^reference:\s*\n\s+locked:\s*([^\s#]+)", project)
    reference_locked = reference_locked_match.group(1).strip().strip("'\"") if reference_locked_match else None
    if (project_status.group(1) if project_status else None) != "reference_locked" or reference_locked != "true":
        raise RuntimeError("REFERENCE_NOT_LOCKED")
    experiment_status = re.search(r"(?m)^  status:\s*([^\s#]+)", experiment)
    if (experiment_status.group(1) if experiment_status else None) != "not_started":
        benchmark = root / "03_human" / "reference_benchmark.json"
        if not benchmark.exists():
            raise RuntimeError("REFERENCE_NOT_LOCKED")


def load_records(path: Path) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        records = payload
    elif isinstance(payload, dict):
        for key in ("records", "items", "candidates", "relations"):
            if isinstance(payload.get(key), list):
                records = payload[key]
                break
        else:
            records = [payload]
    else:
        raise ValueError("JSON input must be an object or array")
    if not all(isinstance(item, dict) for item in records):
        raise ValueError("Every record must be a JSON object")
    return records


def _norm(value: Any) -> str:
    if value is None:
        return ""
    return re.sub(r"\s+", " ", str(value).strip().casefold())


def location_key(record: dict[str, Any]) -> tuple[str, ...]:
    location = record.get("location") or record.get("source_location") or {}
    return tuple(_norm(location.get(field)) for field in ("article", "paragraph", "point", "subparagraph", "recital"))


def record_key(record: dict[str, Any]) -> tuple[str, ...]:
    location = location_key(record)
    if any(location):
        # Experimental outputs do not receive reference candidate IDs. Location
        # is therefore the cross-source key when structural coordinates exist.
        return ("location",) + location
    candidate_id = _norm(record.get("candidate_id"))
    if candidate_id:
        return ("candidate_id", candidate_id)
    # relation_id is only a last-resort key for malformed/locationless records.
    return ("relation_id", _norm(record.get("relation_id")))


def is_reference_positive(record: dict[str, Any]) -> bool:
    return _norm(record.get("relational_result")) == "positive"


def is_experimental_positive(record: dict[str, Any]) -> bool:
    return _norm(record.get("decision")) == "intermediated"


def derived_relational_result(record: dict[str, Any]) -> str:
    return {
        "intermediated": "positive",
        "direct": "negative",
        "uncertain": "conditional",
        "not_supported": "insufficient_evidence",
    }.get(_norm(record.get("decision")), "insufficient_evidence")


def safe_divide(numerator: int | float, denominator: int | float) -> float:
    return numerator / denominator if denominator else 0.0


def classification_metrics(reference: Iterable[dict[str, Any]], experimental: Iterable[dict[str, Any]]) -> dict[str, float | int]:
    reference_keys = {record_key(item) for item in reference if is_reference_positive(item)}
    experimental_keys = {record_key(item) for item in experimental if is_experimental_positive(item)}
    tp = len(reference_keys & experimental_keys)
    fp = len(experimental_keys - reference_keys)
    fn = len(reference_keys - experimental_keys)
    precision = safe_divide(tp, tp + fp)
    recall = safe_divide(tp, tp + fn)
    f1 = safe_divide(2 * precision * recall, precision + recall)
    return {"TP": tp, "FP": fp, "FN": fn, "precision": precision, "recall": recall, "F1": f1}


def normalized_values(value: Any) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, list):
        output: set[str] = set()
        for item in value:
            output.add(_norm(item.get("label") if isinstance(item, dict) else item))
        return {item for item in output if item}
    if isinstance(value, dict):
        return {_norm(value.get("label"))} if value.get("label") else set()
    return {_norm(value)} if _norm(value) else set()


def compare_fields(reference: dict[str, Any], experimental: dict[str, Any]) -> dict[str, Any]:
    output: dict[str, Any] = {
        "reference_key": record_key(reference),
        "experimental_key": record_key(experimental),
        "relational_result_agreement": _norm(reference.get("relational_result")) == derived_relational_result(experimental),
    }
    for field in ("R", "I", "T"):
        output[f"{field}_agreement"] = normalized_values(reference.get(field)) == normalized_values(experimental.get(field))
    output["mechanism_agreement"] = _norm(reference.get("primary_mechanism")) == _norm(experimental.get("mechanism"))
    return output


def build_comparison(reference: list[dict[str, Any]], experimental: list[dict[str, Any]]) -> dict[str, Any]:
    ref_by_key = {record_key(item): item for item in reference}
    exp_by_key = {record_key(item): item for item in experimental}
    rows = []
    for key in sorted(set(ref_by_key) | set(exp_by_key)):
        ref_item = ref_by_key.get(key)
        exp_item = exp_by_key.get(key)
        row: dict[str, Any] = {"key": key, "reference_present": ref_item is not None, "experimental_present": exp_item is not None}
        row["reference_positive"] = bool(ref_item and is_reference_positive(ref_item))
        row["experimental_positive"] = bool(exp_item and is_experimental_positive(exp_item))
        if ref_item and exp_item:
            row.update(compare_fields(ref_item, exp_item))
        rows.append(row)
    return {"metrics": classification_metrics(reference, experimental), "rows": rows}


def error_taxonomy(comparison: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    for row in comparison.get("rows", []):
        key = "|".join(row.get("key", []))
        if row.get("reference_positive") and not row.get("experimental_positive"):
            errors.append({"key": key, "category": "omission"})
        elif row.get("experimental_positive") and not row.get("reference_positive"):
            errors.append({"key": key, "category": "over-inclusion"})
        elif row.get("reference_positive") and row.get("experimental_positive"):
            for field, category in (("R_agreement", "regulator_error"), ("I_agreement", "intermediary_error"), ("T_agreement", "target_error"), ("mechanism_agreement", "mechanism_error")):
                if row.get(field) is False:
                    errors.append({"key": key, "category": category})
            if row.get("relational_result_agreement") is False:
                errors.append({"key": key, "category": "category_error"})
    return errors
