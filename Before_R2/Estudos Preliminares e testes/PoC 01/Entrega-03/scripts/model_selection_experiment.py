"""Orchestrates the Tier 0 (tuning, free, existing candidates) and Tier 1
(held-out, scored) model selection experiment per
../MODEL_SELECTION_PROTOCOL.md.

Tier 0 usage (reads reference/data/candidate_adjudications_v3.csv):
    python model_selection_experiment.py --tier 0 --provider dry_run

Tier 1 usage (reads a user-prepared CSV of new, hand-adjudicated candidates
in the same column format - see MODEL_SELECTION_PROTOCOL.md for how these
must be produced BEFORE running this):
    python model_selection_experiment.py --tier 1 --provider dry_run \\
        --tier1-file ../data/tier1_human_adjudications.csv

Real provider runs (--provider openai) use the live adapter only after
MODEL_SELECTION_PROTOCOL.md's prerequisites checklist is complete. Use
--provider dry_run to validate orchestration without cost.
"""
import argparse
import csv
import json
import re
from pathlib import Path

import context_package
import run_stage
from consistency_check import check_consistency

ROOT = Path(__file__).resolve().parent.parent
REFERENCE_DATA = ROOT / "reference" / "data"
DATA_DIR = ROOT / "data"

CELEX_TO_SLUG = {
    "32022L2464": "csrd",
    "32010R0066": "ecolabel",
    "32019R2089": "climate_benchmarks",
    "32018R2067": "ets_verification",
}

ANCHOR_EXPECTATIONS = {
    "CAND-03": "negative",
    "CAND-06": "negative",
    "CAND-07": "conditional",
}

N_CONSISTENCY_RUNS = 3


def extract_article_token(article_field: str) -> str:
    m = re.search(r"Article\s?\d+[a-z]?", article_field)
    if not m:
        raise ValueError(f"Could not extract an 'Article N' token from '{article_field}'")
    return m.group(0)


def load_candidates(csv_path: Path) -> list:
    with csv_path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f))


def run_b1_b2_for_candidate(cand: dict, provider: str, model: str) -> dict:
    candidate_id = cand["candidate_id"]
    slug = CELEX_TO_SLUG.get(cand["source_celex"])
    if slug is None:
        raise ValueError(f"Unknown source_celex '{cand['source_celex']}' for {candidate_id}")
    article_token = extract_article_token(cand["article"])

    pkg = context_package.build_package(slug, article_token)
    b1_values = {
        "CANDIDATE_ID": candidate_id,
        "SOURCE_ACT_TITLE": slug,
        "SOURCE_CELEX": cand["source_celex"],
        "ARTICLE": article_token,
        "FULL_ARTICLE_TEXT": pkg["full_text"],
        "CROSS_REFERENCED_TEXT": "",
        "KNOWN_CROSS_ACT_TEXT": "",
    }

    b1_records = []
    for _ in range(N_CONSISTENCY_RUNS):
        b1_records.append(run_stage.run_once("b1", candidate_id, provider, model,
                                               b1_values, None, estimate_only=False))
    b1_latest = b1_records[-1]

    b2_values = dict(b1_values)
    b2_values["STAGE_B1_OUTPUT_JSON"] = json.dumps(b1_latest["output"], ensure_ascii=False)

    b2_records = []
    for _ in range(N_CONSISTENCY_RUNS):
        b2_records.append(run_stage.run_once("b2", candidate_id, provider, model,
                                               b2_values, None, estimate_only=False))

    consistency = check_consistency("b2", candidate_id,
                                     [{"stage": "b2", "unit_id": candidate_id, **r}
                                      for r in b2_records])

    return {
        "candidate_id": candidate_id,
        "ai_relational_test_result": b2_records[-1]["output"]["relational_test_result"],
        "ai_R_actor": b2_records[-1]["output"]["R_actor"],
        "ai_I_actor": b2_records[-1]["output"]["I_actor"],
        "ai_T_actor": b2_records[-1]["output"]["T_actor"],
        "ai_primary_mechanism": b2_records[-1]["output"]["primary_mechanism"],
        "consistency": consistency,
        "human_relational_test_result": cand.get("relational_test_result"),
    }


def run_tier0(provider: str, model: str) -> None:
    candidates = load_candidates(REFERENCE_DATA / "candidate_adjudications_v3.csv")
    print(f"Tier 0: running B1+B2 x{N_CONSISTENCY_RUNS} on {len(candidates)} existing candidates "
          f"(provider={provider}, model={model})\n")

    anchor_pass = True
    results = []
    for cand in candidates:
        result = run_b1_b2_for_candidate(cand, provider, model)
        results.append(result)
        cid = result["candidate_id"]
        expected = ANCHOR_EXPECTATIONS.get(cid)
        if expected:
            ok = result["ai_relational_test_result"] == expected
            anchor_pass = anchor_pass and ok
            print(f"  ANCHOR {cid}: expected={expected} got={result['ai_relational_test_result']} "
                  f"{'OK' if ok else 'MISMATCH'}")
        else:
            print(f"  {cid}: ai={result['ai_relational_test_result']} "
                  f"human={result['human_relational_test_result']}")

    print(f"\nTier 0 anchor checks: {'PASS' if anchor_pass else 'FAIL'}")
    print("Reminder: Tier 0 results are for prompt/schema tuning only - NOT a reportable "
          "model-selection score (see MODEL_SELECTION_PROTOCOL.md).")


def run_tier1(provider: str, model: str, tier1_file: Path) -> None:
    if not tier1_file.exists():
        raise FileNotFoundError(
            f"{tier1_file} not found. Tier 1 requires Igor to hand-adjudicate 15-20 NEW "
            "candidates (same column format as candidate_adjudications_v3.csv) BEFORE "
            "this script is run - see MODEL_SELECTION_PROTOCOL.md, Tier 1 sequencing "
            "constraint. This file does not exist yet, meaning that step has not happened."
        )
    candidates = load_candidates(tier1_file)
    print(f"Tier 1: running B1+B2 x{N_CONSISTENCY_RUNS} on {len(candidates)} held-out candidates "
          f"(provider={provider}, model={model})\n")

    scorecard_rows = []
    for cand in candidates:
        result = run_b1_b2_for_candidate(cand, provider, model)
        match = result["ai_relational_test_result"] == result["human_relational_test_result"]
        scorecard_rows.append({
            "candidate_id": result["candidate_id"],
            "ai_verdict": result["ai_relational_test_result"],
            "human_verdict": result["human_relational_test_result"],
            "verdict_match": match,
            "self_consistent": result["consistency"]["status"] == "STABLE",
        })
        print(f"  {result['candidate_id']}: ai={result['ai_relational_test_result']} "
              f"human={result['human_relational_test_result']} "
              f"{'MATCH' if match else 'MISMATCH'} "
              f"[{result['consistency']['status']}]")

    DATA_DIR.mkdir(exist_ok=True)
    scorecard_path = DATA_DIR / "model_selection_scorecard_v1.csv"
    with scorecard_path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["candidate_id", "ai_verdict", "human_verdict",
                                            "verdict_match", "self_consistent"])
        w.writeheader()
        w.writerows(scorecard_rows)

    n = len(scorecard_rows)
    n_match = sum(1 for r in scorecard_rows if r["verdict_match"])
    n_stable = sum(1 for r in scorecard_rows if r["self_consistent"])
    print(f"\nVerdict agreement with human Tier-1 coding: {n_match}/{n} ({n_match/n:.0%})")
    print(f"Self-consistency (3/3 stable): {n_stable}/{n} ({n_stable/n:.0%})")
    print(f"\nScorecard written to {scorecard_path}.")
    print("This is a partial view (relational_test_result agreement + consistency only) - "
          "the full weighted rubric in MODEL_SELECTION_PROTOCOL.md also requires manual "
          "evidence-fidelity review and the adversarial context test, neither of which is "
          "automated here by design (they require human judgment).")
    print("Fill MODEL_SELECTION_RESULTS.md manually from this scorecard plus that review.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tier", required=True, choices=["0", "1"])
    ap.add_argument("--provider", required=True, choices=["openai", "anthropic", "google", "dry_run"])
    ap.add_argument("--model", default="dry-run-model")
    ap.add_argument("--tier1-file", default=str(DATA_DIR / "tier1_human_adjudications.csv"))
    args = ap.parse_args()

    if args.tier == "0":
        run_tier0(args.provider, args.model)
    else:
        run_tier1(args.provider, args.model, Path(args.tier1_file))


if __name__ == "__main__":
    main()
