from __future__ import annotations

"""Independent source-bounded R2 coding; no R1, RA, or prior-run inputs."""

import hashlib
import json
from pathlib import Path


OUT = Path(__file__).resolve().parent
INPUT = OUT / "R2_coding_input.json"
CORPUS = OUT.parents[1] / "02_corpus" / "act.md"
RAW_OUTPUT = OUT / "R2_output_raw.json"


# Each entry was independently reconstructed from the R2 packet and canonical
# corpus. Any candidate not in an explicit category below is a screened item
# without a source-bounded focal regulatory relation and is recorded as such.
DIRECT = {
    "CAND2-8EA8F480D39C": ("Commission", ["sectors of the economy", "key stakeholders"], ["facilitate", "bring together"], ["sector-specific climate dialogues, partnerships and voluntary roadmaps"], "coordination", "The Commission directly facilitates dialogue with sectors and stakeholders; no third actor performs a mediating regulatory function."),
    "CAND2-E5D1DF913444": ("Union", ["Member States", "European Parliament", "Council", "Commission"], ["take necessary measures"], ["achievement of the Union climate-neutrality objective"], "none_or_direct", "Named Union and Member State actors are assigned direct action; no distinct intermediary is stated."),
    "CAND2-4DBCD3C10267": ("Union", ["Member States"], ["invite establishment"], ["national climate advisory body"], "standard_setting", "The recital directly invites Member States to establish a body; the future body is not treated as an intermediary for this focal relation."),
    "CAND2-9F08E9BCE44A": ("Union", ["Commission", "Member States"], ["adopt"], ["Union and national adaptation strategies"], "standard_setting", "The recital describes direct institutional strategy roles and no actor mediating between regulator and target."),
    "CAND2-5BDA0309AE37": ("Union", ["Member States", "European Parliament", "Council", "Commission"], ["take into account"], ["listed climate, social, scientific and economic considerations"], "standard_setting", "The listed considerations directly guide named institutions and Member States."),
    "CAND2-8856CE9D84FD": ("Commission", ["Member States"], ["assess", "issue recommendations"], ["collective progress and national measures"], "monitoring_supervision", "The Commission assesses progress and national measures directly, and may issue recommendations to a Member State."),
    "CAND2-AB84F16B6A72": ("Union", ["EEA"], ["assist"], ["Commission assessments"], "none_or_direct", "The recital directly assigns assistance by the EEA; it does not state a mediated regulator-target relationship."),
    "CAND2-DAF9214798E0": ("Commission", ["all parts of society", "stakeholders"], ["engage"], ["action toward a climate-neutral and climate-resilient society"], "coordination", "The Commission directly engages societal actors; the European Climate Pact is an instrument, not an actor coded as I."),
    "CAND2-F6BA2D3327F5": ("Union", ["Member States"], ["align"], ["reporting and assessment sequence with Member State reporting requirements"], "reporting", "The reporting architecture concerns Member State reporting requirements directly, without a third actor."),
    "CAND2-DC2080A516E3": ("Union", ["relevant Union institutions", "Member States"], ["take necessary measures"], ["collective achievement of climate neutrality"], "none_or_direct", "Article 2(2) imposes a direct obligation on named institutional actors."),
    "CAND2-6E01B3D59579": ("Union", ["relevant Union institutions", "Member States"], ["prioritise", "enhance"], ["emission reductions and removals in implementing the 2030 target"], "standard_setting", "The binding climate target guides direct implementation by named actors."),
    "CAND2-28D96C4EB989": ("Commission", ["European Parliament", "Council"], ["report"], ["foreseen outcome of legislative procedures"], "reporting", "The Commission may report directly to Parliament and Council; procedures are objects, not targets or intermediaries."),
    "CAND2-69F07555AEAE": ("Union", ["relevant Union institutions", "Member States"], ["ensure"], ["continuous progress in enhancing adaptation"], "none_or_direct", "The provision creates a direct obligation without a third actor."),
    "CAND2-107690E984ED": ("Union", ["relevant Union institutions", "Member States"], ["ensure", "identify shortcomings"], ["coherent adaptation policies"], "standard_setting", "The direct obligation is imposed on Union institutions and Member States; consultation with civil society does not establish I."),
    "CAND2-8AC97A3A1797": ("Union", ["Member States"], ["adopt", "implement", "update", "include"], ["national adaptation strategies, plans and updated reporting information"], "reporting", "Member States are directly required to conduct strategy and reporting activity."),
    "CAND2-EDD56D7845D3": ("Commission", ["Member States"], ["assess"], ["collective Member State progress"], "monitoring_supervision", "The Commission directly assesses collective Member State progress."),
    "CAND2-EC26B7CB9612": ("Commission", ["Member States"], ["assess", "submit conclusions"], ["collective adaptation progress and assessment conclusions"], "monitoring_supervision", "The focal assessment concerns Member State progress and is performed by the Commission."),
    "CAND2-610B079BEC92": ("Commission", ["Member States"], ["assess"], ["national measures"], "monitoring_supervision", "Article 7(1) assigns a direct Commission assessment of national measures."),
    "CAND2-EC28D6A68B17": ("Commission", ["Member States"], ["assess"], ["consistency of national measures"], "monitoring_supervision", "The point defines the object of the direct Commission assessment."),
    "CAND2-D441FFCD4FC3": ("Commission", ["Member States"], ["assess", "submit conclusions"], ["consistency of national adaptation measures"], "monitoring_supervision", "The point specifies the adaptation component of the Commission's direct assessment."),
    "CAND2-66E1F84E584B": ("Commission", ["Member State"], ["issue recommendations", "make publicly available"], ["Member State measures and recommendations"], "enforcement_support", "The Commission may issue recommendations directly to the Member State."),
    "CAND2-9E16D8A0E046": ("Union", ["Member State concerned"], ["notify"], ["how recommendations will be taken into account"], "reporting", "The Member State is directly required to notify the Commission; the notification is an object."),
    "CAND2-295D4FBD3131": ("Union", ["Member State concerned"], ["set out", "provide reasoning"], ["treatment of recommendations in a progress report"], "reporting", "The Member State is directly required to report and provide reasoning."),
    "CAND2-DCD349D8BCA7": ("Commission", ["social partners", "academia", "business community", "citizens", "civil society"], ["engage", "facilitate"], ["inclusive process, exchange of best practice and identification of actions"], "coordination", "The Commission directly engages the listed societal actors."),
    "CAND2-04BA3CF9F1E9": ("Commission", ["citizens", "social partners", "stakeholders"], ["engage", "foster dialogue", "diffuse information"], ["dialogue and science-based information"], "information_transmission", "The Commission uses instruments to engage named actors directly; the instrument is not I."),
    "CAND2-8D92B13ED7AE": ("Commission", ["sectors of the economy", "relevant stakeholders"], ["engage", "monitor", "facilitate", "share"], ["voluntary roadmaps, dialogue and best practice"], "coordination", "Roadmaps and dialogue are objects/processes; the Commission directly engages sectors and stakeholders."),
    "CAND2-3E6642A72EB3": ("Commission", ["European Parliament", "Council"], ["submit report"], ["report on operation of the Regulation and assessments"], "reporting", "The Commission submits the report directly to Parliament and Council."),
    "CAND2-4366F1CEFAE0": ("Union", ["members of the Advisory Board"], ["set membership requirements"], ["composition, eligibility criteria and independence"], "standard_setting", "The provision directly sets institutional membership requirements."),
    "CAND2-2A5446CEC717": ("Management Board", ["members of the Advisory Board"], ["designate", "select"], ["appointment of Advisory Board members"], "standard_setting", "The Management Board directly selects and designates Advisory Board members."),
    "CAND2-A95EB0288DC5": ("Union", ["members of the Advisory Board"], ["set independence and governance requirements"], ["independence, chairperson election and rules of procedure"], "standard_setting", "The provision directly regulates the status and governance of Advisory Board members."),
    "CAND2-CC0ABB8E0765": ("Advisory Board", ["Management Board", "Executive Director"], ["consult", "inform"], ["annual work programme and its implementation"], "information_transmission", "The Advisory Board communicates and consults directly with named institutional recipients."),
    "CAND2-4463F3ADEC6D": ("Union", ["Member State"], ["require establishment"], ["multilevel climate and energy dialogue"], "coordination", "The amended provision directly requires each Member State to establish a dialogue."),
    "CAND2-290564FC113D": ("Union", ["Member State"], ["prepare", "submit", "update"], ["long-term strategy"], "reporting", "The amended provision directly requires each Member State to prepare and submit its strategy."),
    "CAND2-84FD60C2FE3B": ("Commission", ["European Parliament", "Council"], ["report", "submit proposals"], ["review report on operation and progress"], "reporting", "The amended Article 45 establishes direct reporting to Parliament and Council."),
}

INSUFFICIENT = {
    "CAND2-71E7A98F944E": "The Advisory Board is described as a point of reference, but the excerpt does not identify an actor-target regulatory relation.",
    "CAND2-D6ED62ADF0C5": "Scientific advice and reports are described, but no recipient actor or target relationship is identified in the focal unit.",
    "CAND2-4A3243C9112E": "The Commission must adopt guidelines, but the focal text does not identify an actor subject to the guidelines.",
    "CAND2-7811F95526B7": "The Commission reviews Union measures, but measures are objects and no actor can be coded as T from the supplied text.",
    "CAND2-4F0C4C78A5A5": "The point identifies information submitted and reported, but does not identify its submitting actor in the focal unit.",
    "CAND2-465FC96778A7": "The point identifies reports as assessment inputs but does not establish a regulatory relationship with their institutional sources.",
    "CAND2-8D7D5ED06FD0": "The amended text requires implementation but does not identify the actor bound by the inserted provision in the supplied focal context.",
}

POSITIVE = {
    "CAND2-11BF388480EA": ("Member State", "national climate advisory body", ["relevant national authorities"], ["establish", "provide expert scientific advice"], ["national climate advisory body; expert scientific advice on climate policy"], "information_transmission", "The Member State establishes the advisory body, which provides expert advice to relevant national authorities as prescribed by that Member State."),
    "CAND2-88A2261C68DE": ("Commission", "EEA", ["Member States"], ["assist", "prepare assessments"], ["assessments under Articles 6 and 7"], "monitoring_supervision", "Article 8(4) requires EEA assistance in Commission assessments; the same-act assessment provisions identify Member State progress and measures as the assessed target."),
}

CONDITIONAL = {
    "CAND2-27E84BD23730": ("Commission", "Energy Union Committee", ["adopt implementing acts", "set out structure, format and process"], ["information and methodology for reporting on energy-subsidy phase-out"], "standard_setting", "The Committee is expressly an assisting third actor, but the excerpt identifies no actor that can be responsibly coded as T; information and methodology are objects."),
}


def actor(label: str, role: str, refs: list[str] | None = None) -> dict[str, object]:
    return {"label": label, "role": role, "evidence_refs": refs or ["E1"]}


def output_location(source: dict[str, object]) -> dict[str, object]:
    return {name: source.get(name) for name in ("celex", "article", "paragraph", "point", "subparagraph", "recital")}


def basic_evidence(item: dict[str, object]) -> list[dict[str, object]]:
    source = item["source_location"]
    provision = f"Article {source['article']}" if source.get("article") else f"Recital {source['recital']}"
    if source.get("paragraph"):
        provision += f", paragraph {source['paragraph']}"
    if source.get("point"):
        provision += f", point ({source['point']})"
    return [{
        "evidence_id": "E1",
        "location": f"{provision}, lines {source['line_start']}-{source['line_end']}",
        "quote": item["focal_excerpt"],
        "evidence_role": "relationship",
        "observability": "DIRECT",
        "supports": ["screening_status", "R", "I", "T", "action", "object", "relational_test", "primary_mechanism"],
    }]


def conditions(a: str, b: str, c: str, d: str, e: str, refs: list[str] | None = None) -> dict[str, object]:
    refs = refs or ["E1"]
    return {name: {"result": result, "evidence_refs": refs} for name, result in {
        "condition_A": a, "condition_B": b, "condition_C": c, "condition_D": d, "condition_E": e,
    }.items()}


def common(item: dict[str, object]) -> dict[str, object]:
    article = item["source_location"].get("article")
    return {
        "candidate_id": item["candidate_id"],
        "candidate_origin": item["candidate_origin"],
        "source_location": output_location(item["source_location"]),
        "is_regulatory_act": True,
        "regulatory_act_type": "EU Regulation",
        "rule_source": [actor("This Regulation", "rule_source")] if article else [],
        "standard_setter": [], "direct_regulator": [], "oversight_authority": [], "enforcement_authority": [],
        "instrument": [], "procedure": [], "secondary_mechanisms": [],
        "evidence_items": basic_evidence(item),
        "additional_context_required": [],
        "notes": ["Raw independent R2 coding; only authorized R2 inputs and canonical corpus used."],
    }


def not_candidate(item: dict[str, object]) -> dict[str, object]:
    record = common(item)
    record.update({
        "screening_status": "not_candidate", "R": None, "I": None, "T": None,
        "action": [], "object": [], "mediating_function": [],
        "relational_test": conditions("NO", "NO", "NO", "NO", "YES"),
        "relational_result": "negative", "primary_mechanism": "none_or_direct", "confidence": "high",
        "interpretive_note": "The focal unit is contextual, definitional, evidentiary or an institutional task without a source-bounded focal regulatory relationship with identifiable R and actor-target T.",
    })
    return record


def direct(item: dict[str, object], decision: tuple) -> dict[str, object]:
    regulator, targets, actions, objects, mechanism, note = decision
    record = common(item)
    r = [actor(regulator, "direct_regulator")]
    record.update({
        "screening_status": "direct_relationship", "R": r, "I": None,
        "T": [actor(target, "target") for target in targets],
        "action": actions, "object": objects, "mediating_function": [],
        "relational_test": conditions("YES", "YES", "NO", "NO", "YES"),
        "relational_result": "negative", "primary_mechanism": mechanism,
        "confidence": "medium" if item["source_location"].get("recital") else "high",
        "interpretive_note": note,
    })
    record["direct_regulator"] = r
    if mechanism == "standard_setting": record["standard_setter"] = r
    if mechanism == "monitoring_supervision": record["oversight_authority"] = r
    if mechanism == "enforcement_support": record["enforcement_authority"] = r
    return record


def insufficient(item: dict[str, object], note: str) -> dict[str, object]:
    record = common(item)
    record.update({
        "screening_status": "insufficient_evidence", "R": None, "I": None, "T": None,
        "action": [], "object": [], "mediating_function": [],
        "relational_test": conditions("UNCLEAR", "UNCLEAR", "UNCLEAR", "UNCLEAR", "NO"),
        "relational_result": "insufficient_evidence", "primary_mechanism": "none_or_direct", "confidence": "low",
        "interpretive_note": note,
        "additional_context_required": ["A source-bounded provision identifying the missing actor-target relation would be required."],
    })
    return record


def positive(item: dict[str, object], decision: tuple) -> dict[str, object]:
    regulator, intermediary, targets, actions, objects, mechanism, note = decision
    record = common(item)
    r = [actor(regulator, "direct_regulator")]
    i = [actor(intermediary, "intermediary")]
    refs = ["E1"]
    if item["candidate_id"] == "CAND2-88A2261C68DE":
        record["evidence_items"].append({
            "evidence_id": "E2",
            "location": "Article 6(1)(a), line 276",
            "quote": "the collective progress made by all Member States towards the achievement of the climate-neutrality objective",
            "evidence_role": "relationship",
            "observability": "DIRECT",
            "supports": ["T", "relational_test"],
        })
        refs.append("E2")
    record.update({
        "screening_status": "candidate", "R": r, "I": i,
        "T": [actor(target, "target", refs) for target in targets],
        "action": actions, "object": objects,
        "mediating_function": ["provide expert assistance or advice connecting the regulator's assessment function to the target relation"],
        "relational_test": conditions("YES", "YES", "YES", "YES", "YES", refs),
        "relational_result": "positive", "primary_mechanism": mechanism, "confidence": "medium",
        "interpretive_note": note,
    })
    record["direct_regulator"] = r
    record["oversight_authority"] = r if mechanism == "monitoring_supervision" else []
    return record


def conditional(item: dict[str, object], decision: tuple) -> dict[str, object]:
    regulator, intermediary, actions, objects, mechanism, note = decision
    record = common(item)
    r, i = [actor(regulator, "direct_regulator")], [actor(intermediary, "intermediary")]
    record.update({
        "screening_status": "candidate", "R": r, "I": i, "T": None,
        "action": actions, "object": objects,
        "mediating_function": ["assist the Commission in setting implementing-act requirements"],
        "relational_test": conditions("YES", "UNCLEAR", "YES", "YES", "YES"),
        "relational_result": "conditional", "primary_mechanism": mechanism, "confidence": "low",
        "interpretive_note": note,
        "additional_context_required": ["The regulated actor to whom the specified information or methodology applies is not identified in the supplied text."],
    })
    record["direct_regulator"], record["standard_setter"] = r, r
    return record


def main() -> None:
    corpus = CORPUS.read_text(encoding="utf-8")
    required_context = [
        "responsible for providing expert scientific advice on climate policy to the relevant national authorities",
        "The EEA shall assist the Commission in the preparation of the assessments",
        "the collective progress made by all Member States towards the achievement",
    ]
    if not all(text in corpus for text in required_context):
        raise ValueError("Canonical same-act context required for R2 reconstruction is unavailable")
    inputs = json.loads(INPUT.read_text(encoding="utf-8"))
    categories = [set(DIRECT), set(INSUFFICIENT), set(POSITIVE), set(CONDITIONAL)]
    if any(left & right for index, left in enumerate(categories) for right in categories[index + 1:]):
        raise ValueError("R2 decision categories overlap")
    records = []
    for item in inputs:
        candidate_id = item["candidate_id"]
        if candidate_id in DIRECT:
            records.append(direct(item, DIRECT[candidate_id]))
        elif candidate_id in INSUFFICIENT:
            records.append(insufficient(item, INSUFFICIENT[candidate_id]))
        elif candidate_id in POSITIVE:
            records.append(positive(item, POSITIVE[candidate_id]))
        elif candidate_id in CONDITIONAL:
            records.append(conditional(item, CONDITIONAL[candidate_id]))
        else:
            records.append(not_candidate(item))
    if len(records) != len(inputs) or {record["candidate_id"] for record in records} != {item["candidate_id"] for item in inputs}:
        raise ValueError("R2 output does not cover the authorized packet exactly")
    RAW_OUTPUT.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = {
        "records": len(records),
        "relational_result": {name: sum(record["relational_result"] == name for record in records) for name in ("positive", "negative", "conditional", "insufficient_evidence")},
        "confidence": {name: sum(record["confidence"] == name for record in records) for name in ("high", "medium", "low", "not_assessed")},
        "I_not_null": sum(record["I"] not in (None, []) for record in records),
        "condition_C_yes": sum(record["relational_test"]["condition_C"]["result"] == "YES" for record in records),
        "condition_D_yes": sum(record["relational_test"]["condition_D"]["result"] == "YES" for record in records),
        "raw_sha256": hashlib.sha256(RAW_OUTPUT.read_bytes()).hexdigest().upper(),
    }
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
