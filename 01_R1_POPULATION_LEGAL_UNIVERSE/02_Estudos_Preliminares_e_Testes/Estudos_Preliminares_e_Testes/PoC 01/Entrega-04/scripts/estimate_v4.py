"""Estimate v4 AI spend using the assembled prompts and published prices."""
from __future__ import annotations

import csv
import json
from pathlib import Path

import context_package_v4 as context_package
import run_stage

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"


def approx_tokens(text: str) -> int:
    return int(len(text.split()) * 1.3)


def call_input(stage: str, values: dict) -> int:
    system, template = run_stage.load_prompts(stage)
    user = run_stage.fill_template(template, values)
    return approx_tokens(system) + approx_tokens(user)


def main() -> None:
    with (DATA / "audit_sample_v4.csv").open(encoding="utf-8") as handle:
        sample = list(csv.DictReader(handle))
    calls = []
    for row in sample:
        package = context_package.build_package({
            "32010R0066": "ecolabel", "32018R2067": "ets_verification",
            "32019R2089": "climate_benchmarks", "32020R0852": "taxonomy",
            "32022L2464": "csrd",
        }[row["source_celex"]], row["article"])
        base = {
            "CANDIDATE_ID": row["audit_sample_id"], "SOURCE_ACT_TITLE": row["source_celex"],
            "SOURCE_CELEX": row["source_celex"], "ARTICLE": package["article_token"],
            "FULL_ARTICLE_TEXT": package["full_text"], "CROSS_REFERENCED_TEXT": "",
            "KNOWN_CROSS_ACT_TEXT": "", "PROVISION_ID": row["audit_sample_id"],
            "PROVISION_TEXT": row["evidence_text"],
        }
        calls.extend([("a2", call_input("a2", base))])
        calls.extend([("b1", call_input("b1", base)), ("b2", call_input("b2", {**base, "STAGE_B1_OUTPUT_JSON": "{}"}))])
    with (DATA / "rit_relationships_v4.csv").open(encoding="utf-8") as handle:
        relationships = list(csv.DictReader(handle))
    for row in relationships:
        package = context_package.build_package({
            "32022L2464": "csrd", "32010R0066": "ecolabel", "32018R2067": "ets_verification",
        }[row["source_act"]], row["article"])
        values = {
            "RELATIONSHIP_ID": row["relationship_id"],
            "RELATIONSHIP_TEXT": package["full_text"],
            "R_ACTOR": row["R_actor_id"], "I_ACTOR": row["I_actor_id"], "T_ACTOR": row["T_actor_id"],
            "REQUESTED_FIXED_FIELDS": "all fixed v3 attributes",
            "REQUESTED_DEFERRED_FIELDS": "conflict_of_interest_rule, reporting_to_regulator, accreditation",
            "FIELD_DEFINITIONS_EXCERPT": "DATA_DICTIONARY_v3 definitions",
        }
        calls.append(("c", call_input("c", values)))
    input_tokens = sum(tokens for _, tokens in calls) * 3
    output_tokens = len(calls) * 600 * 3
    result = {
        "model": "gpt-5.6-terra",
        "calls": len(calls) * 3,
        "approx_input_tokens": input_tokens,
        "approx_output_tokens": output_tokens,
        "published_price_usd_per_million": {"input": 2.0, "output": 12.0},
        "approx_cost_usd": round(input_tokens / 1_000_000 * 2 + output_tokens / 1_000_000 * 12, 4),
        "price_note": "Published OpenAI documentation price; account dashboard remains authoritative.",
        "method_note": "1.3 tokens per whitespace word and 600 output tokens per structured call; conservative planning proxy, not an invoice.",
    }
    (DATA / "api_cost_estimate_v4.json").write_text(json.dumps(result, indent=2), encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
