"""Bounded (max 1 round) resolution of a model's context_escape_hatch
request. If the model still requests context after one augmented re-run,
the unit is routed to human_review_required=1 - no recursive/unbounded
resolution in this pass (per AI_CODING_PROTOCOL.md).

This module resolves requests only against:
  (a) context_package.py's KNOWN_CROSS_ACT_REFS registry (pre-fetched text
      for references already known to matter from the human v3 coding
      round), or
  (b) same-act cross-references resolvable from already-downloaded HTML.
It does NOT autonomously fetch new acts from the network - if the
requested source isn't already known/local, that itself is logged and the
unit goes to human review (a human decides whether it's worth running
collect.py for a new act).
"""
import json
from pathlib import Path

from context_package import KNOWN_CROSS_ACT_REFS, build_package
import run_stage

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


def try_resolve(requested_source: str, slug: str, article_label: str) -> dict:
    """Attempt to resolve one context request. Returns a dict with
    'resolved' (bool) and, if resolved, 'text' to append to the package."""
    for ref_label, ref_data in KNOWN_CROSS_ACT_REFS.items():
        if ref_label.lower() in requested_source.lower() or requested_source.lower() in ref_label.lower():
            if ref_data["text"] is not None:
                return {"resolved": True, "text": ref_data["text"], "source": ref_label}
            return {
                "resolved": False,
                "reason": f"Known reference '{ref_label}' registered but text not yet fetched. {ref_data['note']}",
            }

    try:
        pkg = build_package(slug, article_label)
        cross_ref_candidates = pkg["same_act_cross_reference_candidates"]
        for candidate in cross_ref_candidates:
            if candidate.lower() in requested_source.lower():
                resolved_pkg = build_package(slug, candidate)
                return {"resolved": True, "text": resolved_pkg["full_text"], "source": candidate}
    except (FileNotFoundError, ValueError):
        pass

    return {"resolved": False, "reason": "Not found in known cross-act registry or same-act cross-references."}


def run_with_context_loop(stage: str, unit_id: str, provider: str, model: str,
                            template_values: dict, slug: str, article_label: str,
                            reasoning_effort: str | None = None) -> dict:
    """Runs a stage once; if the model requests additional context, attempts
    one resolution and re-runs once; otherwise routes to human review."""
    record = run_stage.run_once(stage, unit_id, provider, model, template_values,
                                  reasoning_effort, estimate_only=False)
    escape = record["output"].get("context_escape_hatch", {})

    if not escape.get("additional_context_required"):
        return {"final_record": record, "context_rounds_used": 0, "human_review_required": False}

    requested = escape.get("requested_source") or ""
    resolution = try_resolve(requested, slug, article_label)

    if not resolution["resolved"]:
        _route_to_human_review(stage, unit_id,
                                 f"Requested context '{requested}' could not be resolved: {resolution.get('reason')}")
        return {"final_record": record, "context_rounds_used": 0, "human_review_required": True,
                "unresolved_request": requested}

    augmented_values = dict(template_values)
    key = "KNOWN_CROSS_ACT_TEXT" if stage in ("b1", "b2") else None
    if key:
        augmented_values[key] = (augmented_values.get(key, "") or "") + "\n\n" + resolution["text"]

    second_record = run_stage.run_once(stage, unit_id, provider, model, augmented_values,
                                         reasoning_effort, estimate_only=False)
    second_escape = second_record["output"].get("context_escape_hatch", {})

    if second_escape.get("additional_context_required"):
        _route_to_human_review(
            stage, unit_id,
            f"Model requested context again after 1 resolved round "
            f"(2nd request: '{second_escape.get('requested_source')}') - bound reached."
        )
        return {"final_record": second_record, "context_rounds_used": 1, "human_review_required": True}

    return {"final_record": second_record, "context_rounds_used": 1, "human_review_required": False}


def _route_to_human_review(stage: str, unit_id: str, reason: str) -> None:
    queue_path = DATA_DIR / "human_review_queue_v1.csv"
    is_new = not queue_path.exists()
    DATA_DIR.mkdir(exist_ok=True)
    with queue_path.open("a", encoding="utf-8") as f:
        if is_new:
            f.write("stage,unit_id,reason,disagreements_json\n")
        f.write(f'{stage},{unit_id},"{reason}",""\n')
