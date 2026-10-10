"""Generic per-stage execution: assemble prompt -> call model -> validate
against schema -> log the run. One call = one JSONL record appended to
data/model_selection_runs_v1.jsonl (metadata) with the parsed output
embedded, so a single file is the append-only source of truth for every
call made, dry-run or real.

Usage:
    python run_stage.py --stage b1 --unit-id CAND-01 --provider dry_run
    python run_stage.py --stage b1 --unit-id CAND-01 --provider openai \\
        --model gpt-6-astra --estimate-only

Real provider calls (--provider openai without --estimate-only) will
raise until MODEL_SELECTION_PROTOCOL.md's prerequisites are satisfied and
OpenAIAdapter.call() has been wired up following the note in
model_adapter.py.
"""
import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import jsonschema

from model_adapter import get_adapter

ROOT = Path(__file__).resolve().parent.parent
SCHEMAS_DIR = ROOT / "schemas"
PROMPTS_DIR = ROOT / "prompts"
DATA_DIR = ROOT / "data"

STAGE_SCHEMA_FILES = {
    "a2": "stage_a2_candidate_detection.schema.json",
    "b1": "stage_b1_architecture.schema.json",
    "b2": "stage_b2_rit_adjudication.schema.json",
    "c": "stage_c_attributes.schema.json",
}
STAGE_PROMPT_STEMS = {
    "a2": "stage_a2",
    "b1": "stage_b1",
    "b2": "stage_b2",
    "c": "stage_c",
}

PROMPT_VERSION = "v1"   # bump and note in CHANGELOG_v4.md whenever prompt wording changes
SCHEMA_VERSION = "v1"   # bump and note in CHANGELOG_v4.md whenever a schema file changes

# Placeholder pricing - MUST be confirmed by the user against their OpenAI
# dashboard before being trusted. Deliberately conservative/high so a
# skipped confirmation errs toward overestimating cost, not underestimating.
UNCONFIRMED_PRICE_PER_1K_INPUT_TOKENS_USD = 0.01
UNCONFIRMED_PRICE_PER_1K_OUTPUT_TOKENS_USD = 0.03


def load_schema(stage: str) -> dict:
    common = json.loads((SCHEMAS_DIR / "common_defs.schema.json").read_text(encoding="utf-8"))
    stage_schema = json.loads((SCHEMAS_DIR / STAGE_SCHEMA_FILES[stage]).read_text(encoding="utf-8"))
    inner = stage_schema.get("schema", stage_schema)
    inner.setdefault("$defs", {})
    inner["$defs"].update(common["$defs"])
    return stage_schema


def load_prompts(stage: str) -> tuple[str, str]:
    stem = STAGE_PROMPT_STEMS[stage]
    system = (PROMPTS_DIR / f"{stem}_system.md").read_text(encoding="utf-8")
    guardrails = (PROMPTS_DIR / "shared_guardrail_block.md").read_text(encoding="utf-8")
    system = system.replace("{{SHARED_GUARDRAILS}}", guardrails)
    user_template = (PROMPTS_DIR / f"{stem}_user_template.md").read_text(encoding="utf-8")
    return system, user_template


def fill_template(template: str, values: dict) -> str:
    out = template
    for key, val in values.items():
        out = out.replace("{{" + key + "}}", str(val) if val is not None else "")
    return out


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def estimate_cost(system_prompt: str, user_prompt: str) -> dict:
    # crude word-count-based proxy, NOT a token counter - deliberately
    # conservative (see UNCONFIRMED_PRICE constants above)
    approx_input_tokens = int((len(system_prompt.split()) + len(user_prompt.split())) * 1.3)
    approx_output_tokens = 600  # rough structured-output size guess
    cost = (approx_input_tokens / 1000 * UNCONFIRMED_PRICE_PER_1K_INPUT_TOKENS_USD
            + approx_output_tokens / 1000 * UNCONFIRMED_PRICE_PER_1K_OUTPUT_TOKENS_USD)
    return {
        "approx_input_tokens": approx_input_tokens,
        "approx_output_tokens": approx_output_tokens,
        "approx_cost_usd": round(cost, 4),
        "price_confirmed_by_user": False,
    }


def run_once(stage: str, unit_id: str, provider: str, model: str,
              template_values: dict, reasoning_effort: str | None,
              estimate_only: bool) -> dict:
    schema = load_schema(stage)
    system_prompt, user_template = load_prompts(stage)
    user_prompt = fill_template(user_template, template_values)

    if estimate_only:
        estimate = estimate_cost(system_prompt, user_prompt)
        print(json.dumps({"stage": stage, "unit_id": unit_id, **estimate}, indent=2))
        print("\nNOTE: price constants in this script are UNCONFIRMED placeholders.")
        print("Confirm current OpenAI pricing on your dashboard before proceeding.")
        return estimate

    adapter = get_adapter(provider)
    result = adapter.call(system_prompt, user_prompt, schema, model=model,
                            reasoning_effort=reasoning_effort)

    inner_schema = schema.get("schema", schema)
    jsonschema.validate(instance=result.parsed_json, schema=inner_schema)

    record = {
        "stage": stage,
        "unit_id": unit_id,
        "model_provider": result.model_provider,
        "model_id": result.model_id,
        "model_snapshot": result.model_snapshot,
        "reasoning_effort": result.reasoning_effort,
        "prompt_version": PROMPT_VERSION,
        "schema_version": SCHEMA_VERSION,
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "input_hash": sha256(system_prompt + "\n" + user_prompt),
        "output_hash": sha256(result.raw_response_text),
        "usage": result.usage,
        "output": result.parsed_json,
    }

    DATA_DIR.mkdir(exist_ok=True)
    log_path = DATA_DIR / "model_selection_runs_v1.jsonl"
    with log_path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")

    return record


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stage", required=True, choices=list(STAGE_SCHEMA_FILES))
    ap.add_argument("--unit-id", required=True)
    ap.add_argument("--provider", required=True, choices=["openai", "anthropic", "google", "dry_run"])
    ap.add_argument("--model", default="dry-run-model")
    ap.add_argument("--reasoning-effort", default=None)
    ap.add_argument("--estimate-only", action="store_true")
    ap.add_argument("--template-values-json", default="{}",
                     help="JSON object filling the stage's user prompt template placeholders")
    args = ap.parse_args()

    template_values = json.loads(args.template_values_json)
    record = run_once(args.stage, args.unit_id, args.provider, args.model,
                        template_values, args.reasoning_effort, args.estimate_only)
    if not args.estimate_only:
        print(json.dumps(record, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
