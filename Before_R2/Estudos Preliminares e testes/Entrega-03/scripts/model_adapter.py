"""Thin, provider-agnostic adapter for Structured-Outputs-constrained LLM
calls. Only OpenAIAdapter is implemented this round (OPENAI_API_KEY is the
only provider key present in this environment, per METHODOLOGY discipline
in ../CHANGELOG_v4.md). ClaudeAdapter/GeminiAdapter are stubs so adding a
provider later is a config/adapter addition, not an architecture rewrite.

Every adapter must expose the same interface:

    call(system_prompt: str, user_prompt: str, schema: dict,
         model: str, reasoning_effort: str | None) -> AdapterResult

A DryRunAdapter is provided for testing the orchestration pipeline
(context assembly, schema validation, logging, consistency checking)
WITHOUT spending any API budget or requiring MODEL_SELECTION_PROTOCOL.md's
prerequisites to be satisfied yet. Use --dry-run on run_stage.py to select
it. Real provider calls must never be made until that checklist is
complete (see ../MODEL_SELECTION_PROTOCOL.md).
"""
import json
import os
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class AdapterResult:
    raw_response_text: str
    parsed_json: dict
    model_provider: str
    model_id: str
    model_snapshot: Optional[str]
    reasoning_effort: Optional[str]
    usage: dict = field(default_factory=dict)  # e.g. {"input_tokens":.., "output_tokens":..}


class BaseAdapter:
    provider_name = "base"

    def call(self, system_prompt: str, user_prompt: str, schema: dict,
              model: str, reasoning_effort: Optional[str] = None) -> AdapterResult:
        raise NotImplementedError


class OpenAIAdapter(BaseAdapter):
    provider_name = "openai"

    def __init__(self):
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise RuntimeError(
                "OPENAI_API_KEY not set. This must be present in the "
                "environment before any real call - see "
                "MODEL_SELECTION_PROTOCOL.md prerequisites."
            )
        import openai  # imported lazily so dry-run mode never requires it
        self._client = openai.OpenAI(api_key=api_key)

    def call(self, system_prompt: str, user_prompt: str, schema: dict,
              model: str, reasoning_effort: Optional[str] = None) -> AdapterResult:
        """Uses the Responses API with a json_schema response format.
        NOTE: the exact parameter names/shape for 'reasoning_effort' and for
        pinning a snapshot must be confirmed against the currently
        installed `openai` SDK's docs (2.32.0 at time of writing) before
        real use - the SDK's method signatures can change across versions
        and the model id itself (e.g. resolving to a specific snapshot)
        must be confirmed by the user per MODEL_SELECTION_PROTOCOL.md.
        This method deliberately raises until that confirmation exists,
        to avoid a silently-wrong first real call.
        """
        raise NotImplementedError(
            "OpenAIAdapter.call() is intentionally not wired to a live "
            "request yet. Before implementing the final request shape, "
            "confirm against the installed `openai` SDK's current API "
            "surface: (1) the exact structured-output parameter (e.g. "
            "response_format={'type':'json_schema',...} vs a dedicated "
            "'text.format' field - this has changed across OpenAI SDK "
            "versions), (2) how to pass a pinned model snapshot string, "
            "and (3) how 'reasoning_effort' is exposed for the chosen "
            "model family. Use DryRunAdapter to test everything else in "
            "the pipeline first."
        )


class ClaudeAdapter(BaseAdapter):
    provider_name = "anthropic"

    def __init__(self):
        raise NotImplementedError(
            "Deferred: no ANTHROPIC_API_KEY present in this environment. "
            "See ../CHANGELOG_v4.md 'what was explicitly not done'."
        )

    def call(self, *args, **kwargs):
        raise NotImplementedError


class GeminiAdapter(BaseAdapter):
    provider_name = "google"

    def __init__(self):
        raise NotImplementedError(
            "Deferred: no Google/Gemini API key present in this "
            "environment. See ../CHANGELOG_v4.md 'what was explicitly not done'."
        )

    def call(self, *args, **kwargs):
        raise NotImplementedError


class DryRunAdapter(BaseAdapter):
    """Returns a schema-valid placeholder response without any network
    call. Used to test context assembly, schema validation, consistency
    checking and logging end-to-end before real API spend is authorized."""
    provider_name = "dry_run"

    def call(self, system_prompt: str, user_prompt: str, schema: dict,
              model: str = "dry-run-model", reasoning_effort: Optional[str] = None) -> AdapterResult:
        placeholder = _placeholder_for_schema(schema)
        return AdapterResult(
            raw_response_text=json.dumps(placeholder),
            parsed_json=placeholder,
            model_provider=self.provider_name,
            model_id=model,
            model_snapshot="dry-run-snapshot",
            reasoning_effort=reasoning_effort,
            usage={"input_tokens": len(system_prompt.split()) + len(user_prompt.split()),
                   "output_tokens": len(json.dumps(placeholder).split())},
        )


def _placeholder_for_schema(schema: dict) -> dict:
    """Generates a minimal but schema-shaped placeholder for dry-run
    testing. Not a real model response - values are deliberately generic
    UNK/abstention-style so a dry run never looks like a real finding."""
    inner = schema.get("schema", schema)
    props = inner.get("properties", {})
    out = {}
    for key, spec in props.items():
        out[key] = _placeholder_for_property(spec, inner)
    return out


def _placeholder_for_property(spec: dict, root_schema: dict):
    if "$ref" in spec:
        resolved = _resolve_ref(spec["$ref"], root_schema)
        return _placeholder_for_property(resolved, root_schema)
    t = spec.get("type")
    if "enum" in spec:
        enum = spec["enum"]
        for v in ("UNK", "UNCLEAR", "NA", "insufficient_evidence"):
            if v in enum:
                return v
        return enum[0]
    if t == "object":
        return {k: _placeholder_for_property(v, root_schema)
                for k, v in spec.get("properties", {}).items()}
    if t == "array":
        return []
    if t == "boolean":
        return False
    if t == "string" or (isinstance(t, list) and "string" in t):
        return "DRY_RUN_PLACEHOLDER"
    if isinstance(t, list) and "null" in t:
        return None
    return None


def _resolve_ref(ref: str, root_schema: dict):
    # only supports local "#/$defs/Name" pointers, merged in by run_stage.py
    assert ref.startswith("#/$defs/")
    name = ref.split("/")[-1]
    defs = root_schema.get("$defs", {})
    if name not in defs:
        raise KeyError(f"$ref {ref} not found - did run_stage.py merge common_defs.schema.json?")
    return defs[name]


ADAPTERS = {
    "openai": OpenAIAdapter,
    "anthropic": ClaudeAdapter,
    "google": GeminiAdapter,
    "dry_run": DryRunAdapter,
}


def get_adapter(provider: str) -> BaseAdapter:
    if provider not in ADAPTERS:
        raise ValueError(f"Unknown provider '{provider}'. Known: {list(ADAPTERS)}")
    return ADAPTERS[provider]()
