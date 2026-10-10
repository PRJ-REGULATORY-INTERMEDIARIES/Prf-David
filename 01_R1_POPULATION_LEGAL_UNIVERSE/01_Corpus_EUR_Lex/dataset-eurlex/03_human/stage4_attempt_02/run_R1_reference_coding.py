from __future__ import annotations

"""Independent, source-bounded R1 reference coding for stage4_attempt_02.

Reads only the authorized R1 input packet. The substantive decision table was
constructed from the authorized corpus-bound focal excerpts and contexts. It
does not read R2, RA, attempt 1, strings, or experimental artifacts.
"""

import hashlib
import json
from pathlib import Path


OUT = Path(__file__).resolve().parent
INPUT = OUT / "R1_coding_input.json"
RAW_OUTPUT = OUT / "R1_output_raw.json"


NOT_CANDIDATES = {
    "CAND2-C4E87D5066C6", "CAND2-0E374F1C7A4C", "CAND2-F9C7B65B0C4D",
    "CAND2-5E4EA665A85E", "CAND2-EACA0173738F", "CAND2-CDF54AB06415",
    "CAND2-5AAF170024C6", "CAND2-1317278CFFD8", "CAND2-EF7DEB27D98C",
    "CAND2-37CE75C181B6", "CAND2-F5D039301252", "CAND2-7D237A86714A",
    "CAND2-3373C2B0AA49", "CAND2-558133B800C4", "CAND2-8EAE E41F1080".replace(" ", ""),
    "CAND2-2B14782F89D9", "CAND2-71E7A98F944E", "CAND2-DDC9A9630321",
    "CAND2-D6ED62ADF0C5", "CAND2-6EA7E563363E", "CAND2-021AD4B3CF48",
    "CAND2-082F5C3C3784", "CAND2-81FF544AFB12", "CAND2-D64B4FFA6C04",
    "CAND2-5891C83730AB", "CAND2-8207DD57CAB1", "CAND2-A1B35C3F8A0A",
    "CAND2-815A1BF3717E", "CAND2-4A3243C9112E", "CAND2-7811F95526B7",
    "CAND2-5E47A052C0DF", "CAND2-90DBC4512D0E", "CAND2-A8BB17B8CD32",
    "CAND2-937128584EE2", "CAND2-958BB6289A36", "CAND2-4F0C4C78A5A5",
    "CAND2-465FC96778A7", "CAND2-C5168282A9CE", "CAND2-8607C66ECE11",
    "CAND2-E000728831B2", "CAND2-CBC911FFFEDF", "CAND2-431D6B0BD7E3",
    "CAND2-90DA767B29FC", "CAND2-CC0ABB8E0765", "CAND2-474D6A7B8FCA",
    "CAND2-78725C040A77", "CAND2-8D7D5ED06FD0", "CAND2-E269DC5EED3A",
    "CAND2-06C85DCA5897", "CAND2-A3E2EAA5D77D", "CAND2-D6FFF8586396",
    "CAND2-0235CD5AC705",
}


# r, targets, action, object, primary mechanism, interpretive note
DIRECT = {
    "CAND2-8EA8F480D39C": ("Commission", ["sectors of the economy", "key stakeholders"], ["facilitate"], ["sector-specific climate dialogues and partnerships; voluntary roadmaps"], "coordination", "The recital gives the Commission a direct facilitation role toward sectors and stakeholders; no distinct mediating actor is identified."),
    "CAND2-04C304F4BA49": ("Union", ["Member States"], ["ensure contribution"], ["contribution to the global response to climate change"], "standard_setting", "The Regulation is described as directly ensuring Union and Member State contribution; no third actor mediates the relation."),
    "CAND2-DD20E29F5EEE": ("Union", ["Member States"], ["guide"], ["Union and Member State climate actions by stated principles"], "standard_setting", "The stated principles guide Member State and Union actions directly, without a distinct intermediary."),
    "CAND2-E5D1DF913444": ("Union", ["Member States", "European Parliament", "Council", "Commission"], ["take necessary measures"], ["collective achievement of the climate-neutrality objective"], "none_or_direct", "The recital assigns direct action to named Union and Member State actors; it identifies no intermediary."),
    "CAND2-4DBCD3C10267": ("Union", ["Member States"], ["invite establishment"], ["national climate advisory body"], "standard_setting", "The recital directly invites Member States to establish a national advisory body; the body is the object of establishment, not the intermediary in this focal relation."),
    "CAND2-9F08E9BCE44A": ("Union", ["Commission", "Member States"], ["adopt"], ["Union adaptation strategy; national adaptation strategies and plans"], "standard_setting", "The recital describes direct strategy-adoption roles for the Commission and Member States; no third actor mediates them."),
    "CAND2-5BDA0309AE37": ("Union", ["Member States", "European Parliament", "Council", "Commission"], ["take into account"], ["listed social, scientific, environmental and economic considerations"], "standard_setting", "The recital sets direct considerations for named institutions and Member States without an intermediary."),
    "CAND2-8856CE9D84FD": ("Commission", ["Member States"], ["assess", "issue recommendations"], ["collective progress and national measures"], "monitoring_supervision", "The Commission assesses Member State progress and may issue recommendations directly to a Member State; no intermediary is identified."),
    "CAND2-AB84F16B6A72": ("Union", ["EEA"], ["assist"], ["preparation of Commission assessments"], "none_or_direct", "The recital assigns the EEA a direct assistance duty concerning Commission assessments; no R-I-T mediation is textually established."),
    "CAND2-DAF9214798E0": ("Commission", ["all parts of society", "stakeholders"], ["engage"], ["action toward a climate-neutral and climate-resilient society"], "coordination", "The Commission is to engage societal actors directly; the European Climate Pact is named as a route, not as an actor performing mediation."),
    "CAND2-F6BA2D3327F5": ("Union", ["Member States"], ["align"], ["reporting and assessment sequence with Member State information and reporting requirements"], "reporting", "The recital directly aligns reporting architecture with Member State reporting requirements; it identifies no third actor."),
    "CAND2-DC2080A516E3": ("Union", ["relevant Union institutions", "Member States"], ["take necessary measures"], ["collective achievement of the climate-neutrality objective"], "none_or_direct", "Article 2(2) addresses named institutional actors directly and supplies no separate intermediary."),
    "CAND2-11BF388480EA": ("Union", ["Member States"], ["invite establishment"], ["national climate advisory body"], "standard_setting", "The provision directly invites each Member State to establish a body; that future body is not coded as a mediator here."),
    "CAND2-6E01B3D59579": ("Union", ["relevant Union institutions", "Member States"], ["prioritise", "enhance"], ["emission reductions and removals in implementing the 2030 target"], "standard_setting", "The binding target directs implementation by named institutional actors without a third actor."),
    "CAND2-28D96C4EB989": ("Commission", ["European Parliament", "Council"], ["report"], ["foreseen outcome of legislative procedures"], "reporting", "The Commission may report directly to Parliament and Council; legislative procedures are objects, not targets or intermediaries."),
    "CAND2-69F07555AEAE": ("Union", ["relevant Union institutions", "Member States"], ["ensure"], ["continuous progress in adaptation"], "none_or_direct", "Article 5(1) creates a direct obligation for named institutional actors without an intermediary."),
    "CAND2-107690E984ED": ("Union", ["relevant Union institutions", "Member States"], ["ensure", "consult"], ["coherent adaptation policies; identification of shortcomings"], "standard_setting", "The core obligation is directly imposed on Union institutions and Member States; civil society is consulted, not established as a mediator between regulator and target."),
    "CAND2-8AC97A3A1797": ("Union", ["Member States"], ["adopt", "implement", "update", "include"], ["national adaptation strategies and plans; updated information in reports"], "reporting", "Article 5(4) directly regulates Member State strategy and reporting conduct, with no third actor."),
    "CAND2-EDD56D7845D3": ("Commission", ["Member States"], ["assess"], ["collective progress toward the climate-neutrality objective"], "monitoring_supervision", "The Commission assesses collective Member State progress directly; the cross-reference does not establish an intermediary in the supplied text."),
    "CAND2-EC26B7CB9612": ("Commission", ["Member States"], ["assess", "submit conclusions"], ["collective progress on adaptation; assessment conclusions"], "monitoring_supervision", "The focal assessment concerns Member State progress and is performed directly by the Commission."),
    "CAND2-610B079BEC92": ("Commission", ["Member States"], ["assess"], ["national measures"], "monitoring_supervision", "Article 7(1) assigns a direct Commission assessment of national measures."),
    "CAND2-EC28D6A68B17": ("Commission", ["Member States"], ["assess"], ["consistency of national measures"], "monitoring_supervision", "The point specifies the object of the Commission's direct assessment of Member State measures."),
    "CAND2-D441FFCD4FC3": ("Commission", ["Member States"], ["assess", "submit conclusions"], ["consistency of national adaptation measures; assessment conclusions"], "monitoring_supervision", "The point supplies the adaptation object for a direct Commission assessment of national measures."),
    "CAND2-66E1F84E584B": ("Commission", ["Member State"], ["issue recommendations", "make publicly available"], ["Member State measures and recommendations"], "enforcement_support", "The Commission may issue recommendations directly to the Member State; public availability does not create a mediating actor."),
    "CAND2-9E16D8A0E046": ("Union", ["Member State concerned"], ["notify"], ["how recommendations will be taken into account"], "reporting", "The Regulation directly requires the Member State to notify the Commission; the notification is an object, not an intermediary."),
    "CAND2-295D4FBD3131": ("Union", ["Member State concerned"], ["set out", "provide reasoning"], ["treatment of recommendations in the progress report"], "reporting", "The Regulation directly requires reporting and reasoning by the Member State, without a third actor."),
    "CAND2-88A2261C68DE": ("Union", ["EEA"], ["assist"], ["preparation of Commission assessments"], "none_or_direct", "Article 8(4) assigns the EEA a direct assistance duty; no target-regulation relationship mediated by the EEA is specified."),
    "CAND2-DCD349D8BCA7": ("Commission", ["social partners", "academia", "business community", "citizens", "civil society"], ["engage", "facilitate"], ["inclusive process, exchange of best practice and identification of actions"], "coordination", "Article 9(1) creates direct Commission engagement with named societal actors; consultations and dialogues are instruments, not actors."),
    "CAND2-04BA3CF9F1E9": ("Commission", ["citizens", "social partners", "stakeholders"], ["engage", "foster dialogue", "diffuse information"], ["dialogue and science-based information"], "information_transmission", "Article 9(2) directly engages named actors; the European Climate Pact is an instrument rather than a distinct mediating actor."),
    "CAND2-8D92B13ED7AE": ("Commission", ["sectors of the economy", "relevant stakeholders"], ["engage", "monitor", "facilitate", "share"], ["voluntary roadmaps, dialogue and best practice"], "coordination", "Article 10 directly connects the Commission with sectors and stakeholders; roadmaps are objects of monitoring, not T or I."),
    "CAND2-3E6642A72EB3": ("Commission", ["European Parliament", "Council"], ["submit report"], ["report on operation of the Regulation and assessment conclusions"], "reporting", "Article 11 establishes direct Commission reporting to Parliament and Council."),
    "CAND2-4366F1CEFAE0": ("Union", ["members of the Advisory Board"], ["set composition and criteria"], ["Advisory Board membership and eligibility criteria"], "standard_setting", "The provision directly sets institutional membership requirements; the criteria are objects rather than actors."),
    "CAND2-2A5446CEC717": ("Management Board", ["members of the Advisory Board"], ["designate", "select"], ["appointment of Advisory Board members"], "standard_setting", "The Management Board exercises a direct appointment and selection function over Advisory Board members."),
    "CAND2-A95EB0288DC5": ("Union", ["members of the Advisory Board"], ["require independent appointment", "set internal governance"], ["independence, chairperson election and rules of procedure"], "standard_setting", "The provision directly regulates the status and internal governance of Advisory Board members."),
    "CAND2-4463F3ADEC6D": ("Union", ["Member State"], ["require establishment"], ["multilevel climate and energy dialogue"], "coordination", "The amended provision directly requires each Member State to establish a dialogue; participating groups are not a separate mediator in this focal relation."),
    "CAND2-290564FC113D": ("Union", ["Member State"], ["prepare", "submit", "update"], ["long-term strategy"], "reporting", "The amended provision directly requires each Member State to prepare and submit its strategy to the Commission."),
    "CAND2-84FD60C2FE3B": ("Commission", ["European Parliament", "Council"], ["report", "accompany with proposals"], ["review report on operation and progress"], "reporting", "The amended Article 45 establishes direct Commission reporting to Parliament and Council."),
}


CONDITIONAL = {
    "CAND2-27E84BD23730": {
        "R": "Commission",
        "I": "Energy Union Committee",
        "action": ["adopt implementing acts", "set out structure, format, technical details and process"],
        "object": ["information and methodology for reporting on the phasing out of energy subsidies"],
        "mechanism": "standard_setting",
        "note": "The Committee expressly assists the Commission, establishing a third actor and an assisting function, but the supplied text identifies no actor that can responsibly be coded as T; information and methodology remain objects.",
    }
}


def actor(label: str, role: str) -> dict[str, object]:
    return {"label": label, "role": role, "evidence_refs": ["E1"]}


def location(source: dict[str, object]) -> dict[str, object]:
    return {key: source.get(key) for key in ("celex", "article", "paragraph", "point", "subparagraph", "recital")}


def evidence(item: dict[str, object]) -> list[dict[str, object]]:
    source = item["source_location"]
    container = f"Article {source['article']}" if source.get("article") else f"Recital {source['recital']}"
    point = f", paragraph {source['paragraph']}" if source.get("paragraph") else ""
    point += f", point ({source['point']})" if source.get("point") else ""
    lines = f", lines {source['line_start']}-{source['line_end']}"
    return [{
        "evidence_id": "E1",
        "location": container + point + lines,
        "quote": item["focal_excerpt"],
        "evidence_role": "relationship",
        "observability": "DIRECT",
        "supports": ["screening_status", "R", "I", "T", "action", "object", "relational_test", "primary_mechanism"],
    }]


def test(a: str, b: str, c: str, d: str, e: str = "YES") -> dict[str, object]:
    return {
        "condition_A": {"result": a, "evidence_refs": ["E1"]},
        "condition_B": {"result": b, "evidence_refs": ["E1"]},
        "condition_C": {"result": c, "evidence_refs": ["E1"]},
        "condition_D": {"result": d, "evidence_refs": ["E1"]},
        "condition_E": {"result": e, "evidence_refs": ["E1"]},
    }


def common(item: dict[str, object]) -> dict[str, object]:
    rule_source = [actor("This Regulation", "rule_source")] if item["source_location"].get("article") else []
    return {
        "candidate_id": item["candidate_id"],
        "candidate_origin": item["candidate_origin"],
        "source_location": location(item["source_location"]),
        "is_regulatory_act": True,
        "regulatory_act_type": "EU Regulation",
        "rule_source": rule_source,
        "standard_setter": [],
        "direct_regulator": [],
        "oversight_authority": [],
        "enforcement_authority": [],
        "instrument": [],
        "procedure": [],
        "secondary_mechanisms": [],
        "evidence_items": evidence(item),
        "additional_context_required": [],
        "notes": ["Raw independent R1 coding; source-bounded to the authorized corpus context."],
    }


def record_not_candidate(item: dict[str, object]) -> dict[str, object]:
    record = common(item)
    record.update({
        "screening_status": "not_candidate",
        "R": None,
        "I": None,
        "T": None,
        "action": [],
        "object": [],
        "mediating_function": [],
        "relational_test": test("NO", "NO", "NO", "NO"),
        "relational_result": "negative",
        "primary_mechanism": "none_or_direct",
        "confidence": "high",
        "interpretive_note": "The focal excerpt does not establish a source-bounded regulatory relationship with identifiable R and actor-target T. Mentioned information, goals, actors, processes or external instruments are not recoded as relational roles.",
    })
    return record


def record_direct(item: dict[str, object], decision: tuple) -> dict[str, object]:
    regulator, targets, action, obj, mechanism, note = decision
    record = common(item)
    r_value = [actor(regulator, "direct_regulator")]
    record.update({
        "screening_status": "direct_relationship",
        "R": r_value,
        "I": None,
        "T": [actor(label, "target") for label in targets],
        "action": action,
        "object": obj,
        "mediating_function": [],
        "relational_test": test("YES", "YES", "NO", "NO"),
        "relational_result": "negative",
        "primary_mechanism": mechanism,
        "confidence": "high",
        "interpretive_note": note,
    })
    record["direct_regulator"] = r_value
    if mechanism == "standard_setting":
        record["standard_setter"] = r_value
    if mechanism == "monitoring_supervision":
        record["oversight_authority"] = r_value
    if mechanism == "enforcement_support":
        record["enforcement_authority"] = r_value
    return record


def record_conditional(item: dict[str, object], decision: dict[str, object]) -> dict[str, object]:
    record = common(item)
    r_value = [actor(str(decision["R"]), "direct_regulator")]
    i_value = [actor(str(decision["I"]), "intermediary")]
    record.update({
        "screening_status": "candidate",
        "R": r_value,
        "I": i_value,
        "T": None,
        "action": decision["action"],
        "object": decision["object"],
        "mediating_function": ["assist the Commission in setting implementing-act requirements"],
        "relational_test": test("YES", "UNCLEAR", "YES", "YES"),
        "relational_result": "conditional",
        "primary_mechanism": decision["mechanism"],
        "confidence": "medium",
        "interpretive_note": decision["note"],
    })
    record["direct_regulator"] = r_value
    record["standard_setter"] = r_value
    return record


def main() -> None:
    inputs = json.loads(INPUT.read_text(encoding="utf-8"))
    input_ids = {item["candidate_id"] for item in inputs}
    decision_ids = NOT_CANDIDATES | set(DIRECT) | set(CONDITIONAL)
    if input_ids != decision_ids:
        missing = sorted(input_ids - decision_ids)
        extra = sorted(decision_ids - input_ids)
        raise ValueError(f"Decision coverage mismatch; missing={missing}; extra={extra}")
    if NOT_CANDIDATES & set(DIRECT) or NOT_CANDIDATES & set(CONDITIONAL) or set(DIRECT) & set(CONDITIONAL):
        raise ValueError("Decision categories overlap")
    records = []
    for item in inputs:
        candidate_id = item["candidate_id"]
        if candidate_id in NOT_CANDIDATES:
            records.append(record_not_candidate(item))
        elif candidate_id in DIRECT:
            records.append(record_direct(item, DIRECT[candidate_id]))
        else:
            records.append(record_conditional(item, CONDITIONAL[candidate_id]))
    RAW_OUTPUT.write_text(json.dumps(records, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    summary = {
        "records": len(records),
        "screening_status": {status: sum(record["screening_status"] == status for record in records) for status in ("candidate", "direct_relationship", "not_candidate", "insufficient_evidence")},
        "relational_result": {result: sum(record["relational_result"] == result for record in records) for result in ("positive", "negative", "conditional", "insufficient_evidence")},
        "raw_sha256": hashlib.sha256(RAW_OUTPUT.read_bytes()).hexdigest().upper(),
    }
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
