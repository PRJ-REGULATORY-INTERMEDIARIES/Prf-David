"""Compares 3 independent runs of the same unit+stage (identical input) and
flags disagreement on substantive fields. Per AI_CODING_PROTOCOL.md:
disagreement is NEVER averaged or silently resolved - it routes the unit to
human_review_required=1, with all 3 raw outputs preserved for inspection.

Usage:
    python consistency_check.py --stage b2 --unit-id CAND-01 \\
        --runs-file ../data/model_selection_runs_v1.jsonl
"""
import argparse
import json
from pathlib import Path

# Substantive fields checked per stage - deliberately NOT everything (e.g.
# ai_confidence or evidence wording can vary harmlessly across runs; these
# are the fields whose disagreement actually matters for the coding result).
SUBSTANTIVE_FIELDS = {
    "a2": ["AI_candidate", "candidate_mechanism"],
    "b1": [],  # b1 has no categorical verdict field; consistency checked at b2 instead
    "b2": ["relational_test_result", "R_actor", "I_actor", "T_actor", "primary_mechanism"],
    "c": ["formal_role_present", "regulatory_level", "mode_of_operation"],
}


def normalize_actor_label(value) -> str:
    if value is None:
        return ""
    return " ".join(str(value).lower().split())


def load_runs(runs_file: Path, stage: str, unit_id: str) -> list:
    runs = []
    with runs_file.open(encoding="utf-8") as f:
        for line in f:
            rec = json.loads(line)
            if rec["stage"] == stage and rec["unit_id"] == unit_id:
                runs.append(rec)
    return runs


def compare_field(field: str, values: list):
    if field in ("R_actor", "I_actor", "T_actor"):
        normed = [normalize_actor_label(v) for v in values]
        return len(set(normed)) <= 1, normed
    return len(set(values)) <= 1, values


def check_consistency(stage: str, unit_id: str, runs: list) -> dict:
    if len(runs) < 3:
        return {
            "stage": stage, "unit_id": unit_id, "n_runs": len(runs),
            "status": "INSUFFICIENT_RUNS",
            "human_review_required": True,
            "reason": f"Expected 3 runs, found {len(runs)}. Cannot assess self-consistency.",
        }

    runs = runs[-3:]  # most recent 3, in case of re-runs
    fields = SUBSTANTIVE_FIELDS.get(stage, [])
    disagreements = {}
    for field in fields:
        values = [r["output"].get(field) for r in runs]
        agree, normed = compare_field(field, values)
        if not agree:
            disagreements[field] = normed

    result = {
        "stage": stage,
        "unit_id": unit_id,
        "n_runs": len(runs),
        "fields_checked": fields,
        "status": "STABLE" if not disagreements else "UNSTABLE",
        "human_review_required": bool(disagreements),
        "disagreements": disagreements,
        "output_hashes": [r["output_hash"] for r in runs],
    }
    return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True)
    ap.add_argument("--unit-id", required=True)
    ap.add_argument("--runs-file", required=True)
    args = ap.parse_args()

    runs = load_runs(Path(args.runs_file), args.stage, args.unit_id)
    result = check_consistency(args.stage, args.unit_id, runs)
    print(json.dumps(result, indent=2, ensure_ascii=False))

    if result["human_review_required"]:
        queue_path = Path(args.runs_file).parent / "human_review_queue_v1.csv"
        is_new = not queue_path.exists()
        with queue_path.open("a", encoding="utf-8") as f:
            if is_new:
                f.write("stage,unit_id,reason,disagreements_json\n")
            reason = result.get("reason", "self-consistency check failed")
            f.write(f'{args.stage},{args.unit_id},"{reason}","{json.dumps(result.get("disagreements", {}))}"\n')
        print(f"\n-> routed to {queue_path} (human_review_required=1)")


if __name__ == "__main__":
    main()
