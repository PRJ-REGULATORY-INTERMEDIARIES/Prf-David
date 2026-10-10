from __future__ import annotations

import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "outputs"
OUTPUT.mkdir(exist_ok=True)

CASE_INFO = {
    "case_01": {"celex": "32021R1119", "title": "Regulation (EU) 2021/1119 — European Climate Law"},
    "case_02": {"celex": "32023R0956", "title": "Regulation (EU) 2023/956 — Carbon Border Adjustment Mechanism"},
    "case_03": {"celex": "32023R1115", "title": "Regulation (EU) 2023/1115 — Deforestation-Free Products Regulation"},
}


def labels(value):
    return [] if not value else [item.get("label", "") for item in value]


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"))


def norm(value):
    return re.sub(r"\s+", " ", value).strip()


def proposal_path(case_id):
    return ROOT / "cases" / case_id / "primary_coding" / "CLAUDE_CODING_PROPOSAL.json"


# status, Luna confidence, Luna relation type, rationale, field overrides
REVIEWS = {
    "case_01-rel-001": ("ACCEPT", "high", "direct", "The Commission's periodic assessment of collective Member-State progress is an operative R–T supervisory relation in Article 6. Member States are an actor class, while progress and consistency are objects. No third actor performs a demonstrated mediating function in this provision.", {}),
    "case_01-rel-002": ("ACCEPT", "high", "direct", "Article 7 expressly links the Commission's assessment and recommendations to the concerned Member State, followed by the Member State's notification and report-back. The cited text supports a direct relation; documents submitted under the cross-referenced Regulation are not needed to establish the direct R–T architecture.", {}),
    "case_01-rel-003": ("ACCEPT", "medium", "intermediated", "Article 8(4) imposes a specific duty on the EEA to assist in preparing the very Article 6 and 7 assessments through which the Commission supervises Member States. This is legally integrated analytical input, not merely a general advisory mention. The limited detail about the EEA's precise work supports medium confidence but does not defeat the intermediary role.", {}),
    "case_01-rel-004": ("QUESTION", "low", "uncertain", "Article 8(3)(b) makes reports of the EEA, Advisory Board and JRC one of several bases for Commission assessments, but does not assign the latter two a specific duty to perform a mediating function. The passage can support institutionally integrated information supply, yet it can also be read as scientific source material. Researcher attention is required; do not treat every listed report source as an intermediary.", {}),
    "case_01-rel-005": ("REVISE", "medium", "direct", "The direct classification is supportable: Article 10 assigns the Commission engagement and monitoring duties toward sectors that choose to prepare roadmaps. However, the quoted evidence omits the operative third sentence on facilitating dialogue and sharing best practice, even though those actions are included in the Claude fields. The final record should quote the complete paragraph or narrow the action field. Voluntary status does not by itself erase the expressly assigned regulatory/coordination relation.", {"action": ["engage with sectors preparing indicative voluntary roadmaps", "monitor the development of such roadmaps", "facilitate dialogue at Union level", "share best practice among relevant stakeholders"]}),
    "case_01-rel-006": ("ACCEPT", "high", "direct", "The amended text reproduced through Article 13(6)(a) directly requires each Member State to prepare and submit its long-term strategy to the Commission. The strategy is the object and Member States are the target actors; no intermediary is present.", {}),
    "case_01-rel-007": ("ACCEPT", "low", "uncertain", "The Article 5(4) obligation is real, but the recipient of the reports under Article 19(1) of Regulation (EU) 2018/1999 is not reproduced in the frozen corpus. The unresolved R and external-context flag correctly prevent a forced direct or intermediated classification.", {}),

    "case_02-rel-001": ("ACCEPT", "high", "intermediated", "Article 8(1) expressly requires verification by an accredited verifier, and Article 6(2)(d) makes the verification report part of the declaration reviewed under Article 19. The verifier's independent verification operationally mediates the Commission/competent-authority oversight of the declarant. The internal CBAM provisions are sufficient for this relation; external accreditation texts are not needed for the classification itself.", {}),
    "case_02-rel-002": ("ACCEPT", "high", "intermediated", "Article 10(5)(b) requires third-country operators to ensure verification, while Article 10(6)-(7) links the retained and disclosed verified information to the declarant's Article 8 compliance and Article 19 review. The accredited verifier is a distinct functionally integrated intermediary.", {}),
    "case_02-rel-003": ("REVISE", "medium", "intermediated", "The independent person certifies the information contained in the carbon-price documentation; the text does not say that the person certifies its own independence. Correct the action field to describe certification of the information/documentation. The certification still mediates the declarant's claim reviewed by the Commission or competent authority, although its qualification regime is thinner than Article 18's verifier regime.", {"action": ["certify the information contained in the carbon-price documentation"]}),
    "case_02-rel-004": ("QUESTION", "low", "uncertain", "Articles 25(2)-(4) and 19(3) clearly establish customs data collection and transmission into Commission/competent-authority oversight. The remaining boundary is whether customs is an I in an R–I–T chain or a co-regulator performing a parallel customs-control function. The record also bundles customs-to-Commission transmission with Commission-to-authority communication. Researcher review should decide whether the active checks are sufficient for intermediation under the production rule.", {"relation_type": "uncertain", "mechanism": "information_transmission"}),
    "case_02-rel-005": ("QUESTION", "low", "uncertain", "Article 33 creates a real customs notice/data-transmission chain, but the importer's reporting duty is separately direct to the Commission under Article 35(1). The quoted provision does not clearly make customs a regulator-mediated actor between the Commission and importer; it may be a notice and data conduit. Retain as a material boundary case rather than accepting the intermediated label.", {"relation_type": "uncertain", "mechanism": "information_transmission"}),
    "case_02-rel-006": ("QUESTION", "low", "uncertain", "Article 27(5) says only that the Commission may be assisted by competent and customs authorities. It supplies no task, output or function by which either authority mediates the Commission's investigation toward a target. The uncertainty is genuine because the assistance could involve regulatory checks, but the frozen text cannot specify that function.", {}),
    "case_02-rel-007": ("ACCEPT", "high", "direct", "Article 17 directly assigns the authorization decision to the competent authority and makes the applicant the target. The consultation with other authorities is parallel co-regulator input, not a distinct intermediary relation in this row.", {}),
    "case_02-rel-008": ("ACCEPT", "high", "direct", "Article 25(1) directly assigns customs authorities the border-control decision against persons other than authorised declarants. Customs is R here, not an intermediary; importation is the object and the person class is T.", {}),
    "case_02-rel-009": ("ACCEPT", "high", "direct", "Article 6(1)-(2) establishes the declarant's direct duty to submit the annual declaration through the CBAM registry. The registry is an instrument, not a third actor, and the separate verifier relation is not duplicated here.", {}),
    "case_02-rel-010": ("ACCEPT", "medium", "direct", "The Commission is empowered by Article 7(7) to specify the calculation methods that declarants and third-country operators must apply under Annex IV. The implementing acts are absent, so the detailed methodology is externally incomplete, but the direct standard-setting relation and its classification are textually established.", {}),
    "case_02-rel-011": ("ACCEPT", "medium", "direct", "Article 8(3) and Article 18(1) directly authorize Commission implementing acts concerning verifier qualifications and verification principles. The verifier is T in this distinct relation, not I; the absent future instruments do not undermine the current delegation.", {}),
    "case_02-rel-012": ("ACCEPT", "high", "direct", "Article 18(2) directly authorizes a national accreditation body to accredit a person as verifier on the stated capacity test. The external definition of the body is not necessary to establish the operative relationship reproduced in the act.", {}),
    "case_02-rel-013": ("REVISE", "medium", "direct", "The direct relationship exists, but the row materially bundles two different targets and functions: Commission registration of third-country operators/installations and Commission assignment/closure of declarant accounts. The adjudicator should split these into separate rows because R–T and action/object change, while retaining this Claude row as the auditable bundled proposal.", {}),
    "case_02-rel-014": ("ACCEPT", "high", "direct", "Article 12 directly assigns the Commission assistance and coordination function toward competent authorities. Those authorities are T in this relation; their role as R in other rows does not create an intermediary here.", {}),
    "case_02-rel-015": ("REVISE", "medium", "intermediated", "Article 15(1)-(2) creates a sequential chain: the Commission performs risk-based controls, then competent authorities conduct further investigations to correct identified irregularities. In this relation the competent authority can be coded as I between the Commission (R) and the declarant (T), because its downstream investigative function is expressly triggered by Commission findings. This differs from treating two co-regulators as a single direct R.", {"R": ["European Commission"], "I": ["competent authority"], "T": ["authorised CBAM declarant"], "action": ["carry out Commission risk-based controls", "inform competent authority of irregularities", "carry out further investigations to correct irregularities"], "mediating_function": ["conduct further investigations and correction activity triggered by Commission-identified irregularities"], "mechanism": "enforcement_support", "relation_type": "intermediated"}),
    "case_02-rel-016": ("ACCEPT", "high", "direct", "Article 19 directly gives the Commission oversight and review functions, with the competent authority also empowered to review in its own right. The accredited verifier's reports are inputs to this direct review and are already captured in the distinct verification relation.", {}),
    "case_02-rel-017": ("ACCEPT", "high", "direct", "Articles 20-24 describe direct administration of certificates by Member States and the Commission toward authorised declarants. The common platform is an instrument jointly managed by regulators, not a third actor mediating a separate regulatory relationship.", {}),
    "case_02-rel-018": ("ACCEPT", "high", "direct", "Article 26 directly assigns the competent authority penalty and payment-enforcement powers against the listed target classes. No distinct intermediary is identified.", {}),
    "case_02-rel-019": ("ACCEPT", "high", "direct", "Article 27 directly assigns Commission monitoring, investigation and anti-circumvention amendment powers. The possible assistance and notifications are separate boundary candidates and do not alter this direct relation.", {}),
    "case_02-rel-020": ("ACCEPT", "medium", "direct", "Article 2(6)-(9) and Annex III make countries or territories the subjects of Commission assessment and listing/removal decisions. They are institutional targets in this relation, not merely geographic objects; the unusual target class warrants medium confidence.", {}),
    "case_02-rel-021": ("ACCEPT", "high", "direct", "Article 35(1) directly requires the importer or indirect customs representative to submit the transitional report to the Commission. The customs representative is the obligated T where Article 32 applies, not an intermediary in the reporting relation.", {}),
    "case_02-rel-022": ("REVISE", "medium", "intermediated", "Article 35(3)-(5) explicitly sequences Commission identification and communication, competent-authority correction/penalty action, and importer or representative consequences. Reconstructing the Commission as R, the competent authority as I, and the importer/representative as T captures the legally integrated enforcement handoff; the Claude row incorrectly treats the whole chain as direct with both authorities in R.", {"R": ["European Commission"], "I": ["competent authority"], "T": ["importer", "indirect customs representative"], "action": ["identify incomplete, incorrect or missing reports", "communicate information and reasons to the competent authority", "initiate correction procedure", "notify and impose penalty on the importer or indirect customs representative"], "mediating_function": ["apply Commission-detected reporting deficiencies through correction and penalty procedures directed at the importer or representative"], "mechanism": "enforcement_support", "relation_type": "intermediated"}),

    "case_03-rel-001": ("ACCEPT", "high", "direct", "Articles 16, 18 and 19 directly assign competent authorities risk-based checks of operators and traders. The listed documents, systems and products are objects of checking; operators and traders are the targets. No separate intermediary is demonstrated in this checking power.", {}),
    "case_03-rel-002": ("ACCEPT", "high", "direct", "Articles 17, 23-25 directly assign competent authorities interim measures, corrective action and penalties toward operators and traders. The enforcement powers are not mediated by a third actor in this row.", {}),
    "case_03-rel-003": ("ACCEPT", "high", "intermediated", "Article 26 distinguishes competent authorities' compliance determination from customs authorities' border controls based on the due-diligence statement status. Customs therefore performs a legally integrated delegated border function toward products of operators/traders, supporting the intermediated classification even though customs is also a regulator in its own domain.", {}),
    "case_03-rel-004": ("QUESTION", "low", "uncertain", "The information system performs registration, risk-identification and communication functions, but Article 33 describes the system as an instrument and assigns the Commission establishment, maintenance, rules and access functions. It is not clear that the Commission itself, rather than the system, is the third actor performing the mediating function. Keep the system-mediated architecture visible, but require researcher resolution of the actor-versus-instrument boundary.", {"relation_type": "uncertain", "I": ["European Commission (through the information system it establishes and maintains under Article 33)"], "mechanism": "information_transmission"}),
    "case_03-rel-005": ("ACCEPT", "high", "direct", "Article 29 directly assigns the Commission the country-classification assessment and notifications. Member States and third countries are institutional target classes; risk category is the object. Optional information sources do not create additional intermediaries here.", {}),
    "case_03-rel-006": ("ACCEPT", "medium", "intermediated", "Articles 2(31) and 31 establish a formal substantiated-concern channel: a distinct person submits an objectively supported claim, the competent authority must assess it and report follow-up, and the channel is tied to investigation and access to justice. This is a legally integrated reporting trigger, not mere advice, although its private and episodic character warrants medium confidence.", {}),
    "case_03-rel-007": ("ACCEPT", "high", "direct", "Articles 4(5) and 5(5) directly require operators and SME traders to inform competent authorities of new non-compliance risk. The reporting party is itself the regulated target, so no third-party intermediary exists.", {}),
    "case_03-rel-008": ("REJECT", "high", "not_supported", "Article 12(3)-(4) requires public annual reporting, but the operative text identifies no regulator as R and addresses the report to the public generally. The obligation is real, yet the proposed R–I–T relationship is not adequately supported. Reclassify the relationship as not_supported for this construct rather than leave it as an unresolved regulator relation.", {"R": [], "I": [], "relation_type": "not_supported", "mechanism": "none_or_direct"}),
    "case_03-rel-009": ("ACCEPT", "high", "direct", "Article 22 directly requires Member States to make application information available to the Commission and public, after which Commission services publish an overview. The Commission's compilation is its own downstream act, not a third intermediary.", {}),
    "case_03-rel-010": ("REVISE", "high", "direct", "The operative relation supported by Article 25(3) is Member States' direct notification of final judgments and penalties to the Commission. The Commission's publication is transparency toward the public, not a demonstrated intermediary function between the sanctioning authority and the already-sanctioned operators/traders. Correct R to the Commission, remove the proposed I, set T to Member States, and retain judgments/penalties as the object.", {"R": ["European Commission"], "I": [], "T": ["Member States"], "action": ["receive notification of final judgments and penalties"], "object": ["final judgments and penalties imposed for infringements"], "mediating_function": [], "mechanism": "reporting", "relation_type": "direct"}),
}

EVIDENCE_OVERRIDES = {
    "case_01-rel-005": "The Commission shall engage with sectors of the economy within the Union that choose to prepare indicative voluntary roadmaps towards achieving the climate-neutrality objective set out in Article 2(1). The Commission shall monitor the development of such roadmaps. Its engagement shall involve the facilitation of dialogue at Union level, and the sharing of best practice among relevant stakeholders.",
}


ADDITIONS = [
    {
        "case_id": "case_02", "relation_id": "LUNA-ADD-001", "source_location": "Article 27(4)-(5)",
        "evidence_quote": "A Member State or any party that has been affected by, or has benefited from, any of the situations referred to in paragraph 2 may notify the Commission if it is confronted with practices of circumvention. Interested parties other than directly affected or benefited parties, such as environmental organisations and non-governmental organisations, which find concrete evidence of practices of circumvention may also notify the Commission.",
        "contextual_basis": "Article 27(4)-(5) creates a formal notification channel that can trigger a Commission investigation when the claim meets the Article 27(5) data and reasons requirements. The target actor behind the circumvention practice is not identified with sufficient precision in the cited text.",
        "R": ["European Commission"], "I": ["Member State or affected, benefited or interested party submitting a circumvention notification"], "T": [],
        "action": ["notify the Commission of practices of circumvention", "provide reasons and relevant data and statistics"],
        "object": ["claim and supporting data concerning practices of circumvention"], "mediating_function": ["formal third-party reporting that may trigger a Commission investigation"],
        "mechanism": "reporting", "relation_type": "uncertain", "confidence": "low", "external_context_required": False,
        "rationale": "This material reporting trigger is absent from the Claude matrix. It is more institutionally specified than a bare voluntary tip because Article 27(5) makes a compliant notification a basis for mandatory Commission investigation. However, Article 27 does not clearly identify the actor or class investigated as T; the text speaks primarily of practices. The row is therefore added as a researcher-facing uncertain candidate, without inventing a target actor.",
    },
    {
        "case_id": "case_03", "relation_id": "LUNA-ADD-002", "source_location": "Article 9(2); Article 10(4); Article 11(3)",
        "evidence_quote": "The operator shall make available to the competent authorities upon request the information, documents and data collected under this Article.",
        "contextual_basis": "Articles 9(2), 10(4) and 11(3) create a direct information-production and availability chain from operators to competent authorities for due-diligence records, risk assessments and mitigation decisions.",
        "R": ["competent authorities"], "I": [], "T": ["operators"],
        "action": ["make available information, documents and data upon request", "make risk assessments and risk-mitigation decisions available upon request"],
        "object": ["due-diligence information, documents and data", "risk assessments", "risk-mitigation decisions"], "mediating_function": [],
        "mechanism": "reporting", "relation_type": "direct", "confidence": "high", "external_context_required": False,
        "rationale": "Article 9(2) is a clear direct reporting/production obligation omitted from the Claude proposal, and Articles 10(4) and 11(3) extend the same authority-facing availability architecture to risk assessments and mitigation decisions. The operator is T; the information and decisions are objects, not targets.",
    },
    {
        "case_id": "case_03", "relation_id": "LUNA-ADD-003", "source_location": "Article 4(6); Article 5(6)",
        "evidence_quote": "Operators shall offer all necessary assistance to the competent authorities to facilitate the carrying out of the checks under Article 18, including access to premises and the making available of documentation and records.",
        "contextual_basis": "Articles 4(6) and 5(6) directly require operators and traders to support competent-authority checks through access and document/record availability.",
        "R": ["competent authorities"], "I": [], "T": ["operators", "traders"],
        "action": ["offer necessary assistance to facilitate checks", "provide access to premises and documentation and records"],
        "object": ["premises", "documentation and records needed for checks"], "mediating_function": [],
        "mechanism": "enforcement_support", "relation_type": "direct", "confidence": "high", "external_context_required": False,
        "rationale": "This is a material direct compliance-support obligation omitted from the Claude matrix. It is not an intermediary relation: the regulated operators/traders themselves assist the competent authorities, and no distinct third actor is present.",
    },
    {
        "case_id": "case_03", "relation_id": "LUNA-ADD-004", "source_location": "Article 5(4)",
        "evidence_quote": "SME traders shall keep the information referred to in paragraph 3 for at least five years from the date of the making available on the market and shall provide that information to the competent authorities upon request.",
        "contextual_basis": "Article 5(4) establishes a separate direct reporting/production obligation for SME traders, distinct from the operator information duties in Article 9 and the check powers in Article 18.",
        "R": ["competent authorities"], "I": [], "T": ["SME traders"],
        "action": ["provide retained supply-chain information to competent authorities upon request"],
        "object": ["information identifying suppliers, recipients and due-diligence statement references"], "mediating_function": [],
        "mechanism": "reporting", "relation_type": "direct", "confidence": "high", "external_context_required": False,
        "rationale": "Article 5(4) is a clear direct competent-authority reporting obligation not represented by Claude's ten rows. It is included because the targeted recall pass specifically required review of reporting chains; the retained information is the object and SME traders are T.",
    },
]


HEADERS = [
    "case_id", "celex", "act_title", "relation_id", "source_location", "evidence_quote", "contextual_basis",
    "claude_R", "claude_I", "claude_T", "claude_action", "claude_object", "claude_mediating_function", "claude_mechanism", "claude_relation_type", "claude_confidence",
    "luna_review_status", "luna_proposed_R", "luna_proposed_I", "luna_proposed_T", "luna_proposed_action", "luna_proposed_object", "luna_proposed_mediating_function", "luna_proposed_mechanism", "luna_proposed_relation_type", "luna_confidence", "luna_rationale",
    "external_context_required", "researcher_decision", "researcher_final_R", "researcher_final_I", "researcher_final_T", "researcher_final_relation_type", "researcher_note",
]


def blank_researcher():
    return {key: "" for key in HEADERS if key.startswith("researcher_")}


def make_claude_row(case_id, x):
    status, luna_conf, luna_type, rationale, overrides = REVIEWS[x["relation_id"]]
    luna = {"R": labels(x.get("R")), "I": labels(x.get("I")), "T": labels(x.get("T")), "action": x.get("action", []), "object": x.get("object", []), "mediating_function": x.get("mediating_function", []), "mechanism": x.get("mechanism", "none_or_direct"), "relation_type": x.get("relation_type", "uncertain")}
    luna.update(overrides)
    row = {
        "case_id": case_id, "celex": CASE_INFO[case_id]["celex"], "act_title": CASE_INFO[case_id]["title"], "relation_id": x["relation_id"],
        "source_location": x["source_location"], "evidence_quote": EVIDENCE_OVERRIDES.get(x["relation_id"], x["evidence_quote"]),
        "contextual_basis": f"Current-act context limited to {x['source_location']}; linked provisions are used only where named in the proposal and no outside legal text is imported.",
        "claude_R": compact(labels(x.get("R"))), "claude_I": compact(labels(x.get("I"))), "claude_T": compact(labels(x.get("T"))),
        "claude_action": compact(x.get("action", [])), "claude_object": compact(x.get("object", [])), "claude_mediating_function": compact(x.get("mediating_function", [])),
        "claude_mechanism": x.get("mechanism", ""), "claude_relation_type": x.get("relation_type", ""), "claude_confidence": x.get("confidence", ""),
        "luna_review_status": status, "luna_proposed_R": compact(luna["R"]), "luna_proposed_I": compact(luna["I"]), "luna_proposed_T": compact(luna["T"]),
        "luna_proposed_action": compact(luna["action"]), "luna_proposed_object": compact(luna["object"]), "luna_proposed_mediating_function": compact(luna["mediating_function"]),
        "luna_proposed_mechanism": luna["mechanism"], "luna_proposed_relation_type": luna["relation_type"], "luna_confidence": luna_conf, "luna_rationale": rationale,
        "external_context_required": str(bool(x.get("external_context_required", False))).lower(),
    }
    row.update(blank_researcher())
    return row


def make_addition_row(x):
    row = {
        "case_id": x["case_id"], "celex": CASE_INFO[x["case_id"]]["celex"], "act_title": CASE_INFO[x["case_id"]]["title"], "relation_id": x["relation_id"],
        "source_location": x["source_location"], "evidence_quote": x["evidence_quote"], "contextual_basis": x["contextual_basis"],
        "claude_R": "", "claude_I": "", "claude_T": "", "claude_action": "", "claude_object": "", "claude_mediating_function": "", "claude_mechanism": "", "claude_relation_type": "", "claude_confidence": "",
        "luna_review_status": "ADD_MISSING_RELATION", "luna_proposed_R": compact(x["R"]), "luna_proposed_I": compact(x["I"]), "luna_proposed_T": compact(x["T"]),
        "luna_proposed_action": compact(x["action"]), "luna_proposed_object": compact(x["object"]), "luna_proposed_mediating_function": compact(x["mediating_function"]),
        "luna_proposed_mechanism": x["mechanism"], "luna_proposed_relation_type": x["relation_type"], "luna_confidence": x["confidence"], "luna_rationale": x["rationale"],
        "external_context_required": str(x["external_context_required"]).lower(),
    }
    row.update(blank_researcher())
    return row


def validate(rows):
    assert len(rows) == 43, len(rows)
    assert len({row["relation_id"] for row in rows}) == len(rows), "duplicate relation IDs"
    for row in rows:
        for key in ("claude_R", "claude_I", "claude_T", "luna_proposed_R", "luna_proposed_I", "luna_proposed_T"):
            if row[key]:
                assert isinstance(json.loads(row[key]), list), (row["relation_id"], key)
        for key in row:
            if key.startswith("researcher_"):
                assert row[key] == "", (row["relation_id"], key)
        corpus = (ROOT / "cases" / row["case_id"] / "corpus" / "act.md").read_text(encoding="utf-8")
        assert norm(row["evidence_quote"]) in norm(corpus), (row["relation_id"], "evidence not found")


def write_csv(path, rows):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADERS, extrasaction="raise")
        writer.writeheader()
        writer.writerows(rows)


def build_note(rows, claude_count):
    by_case = defaultdict(Counter)
    for row in rows:
        by_case[row["case_id"]][row["luna_review_status"]] += 1
    total_types = Counter(row["luna_proposed_relation_type"] for row in rows)
    lines = [
        "# Luna secondary review — three EU green-transition cases", "",
        "This is an independent, source-bounded review of the Claude proposals. It is not the researcher's adjudication and does not use the historical pilot as ground truth. The review used only the three frozen case corpora, the current production codebook and the review instructions.", "",
        "## Per-case counts", "",
        "| Case | Claude proposals | ACCEPT | REVISE | QUESTION | REJECT | ADD_MISSING_RELATION | Luna intermediated / direct / uncertain |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for case_id in CASE_INFO:
        c = by_case[case_id]
        orig = sum(1 for row in rows if row["case_id"] == case_id and row["claude_relation_type"])
        types = Counter(row["luna_proposed_relation_type"] for row in rows if row["case_id"] == case_id)
        lines.append(f"| {case_id} | {orig} | {c['ACCEPT']} | {c['REVISE']} | {c['QUESTION']} | {c['REJECT']} | {c['ADD_MISSING_RELATION']} | {types['intermediated']} / {types['direct']} / {types['uncertain']} |")
    lines += [
        "", f"The review dataset contains {len(rows)} rows: the {claude_count} Claude proposals plus {len(rows) - claude_count} additions. Across all rows, Luna's provisional classifications are **{total_types['intermediated']} intermediated**, **{total_types['direct']} direct**, **{total_types['uncertain']} uncertain**, and **{total_types['not_supported']} not_supported**. The researcher fields remain blank.", "",
        "## Case 01 — European Climate Law", "",
        "The key safeguard is Article 8(4). I ACCEPT the Claude proposal that the EEA is an intermediary because the operative text assigns it a specific duty to assist in preparing the Article 6 and 7 assessments—the very assessment product through which the Commission supervises Member States. This is materially different from Article 8(3)(b), where reports of the Advisory Board and JRC are merely listed among several assessment inputs; that row remains QUESTION because the text does not establish a comparable mediating duty. Article 10 remains a direct relation, but its evidence quote should include the full operative paragraph because Claude's action fields include the final sentence.", "",
        "## Case 02 — CBAM", "",
        "The accredited-verifier chains in Articles 8 and 10 are accepted. The independent-person certification in Article 9 is retained as intermediated but revised so that the person certifies the documentation's information, not its own independence. Customs transmission in Articles 25 and 33 is retained for researcher attention: the text clearly shows active information flow, but it leaves a genuine boundary between intermediary and parallel co-regulator/data conduit. Article 15 and Article 35 are revised to make the Commission → competent authority → declarant/importer enforcement handoff explicit. The country/operator and reporting relations remain direct where the act identifies a direct duty or Commission decision.", "",
        "## Case 03 — Deforestation-Free Products Regulation", "",
        "The customs border chain in Article 26 is accepted as delegated implementation because competent authorities establish compliance while customs authorities execute the border release/suspension consequence. The Article 33 information-system row is QUESTION: the system performs the risk-processing functions, while the Commission establishes and maintains it, so the actor-versus-instrument distinction requires researcher resolution. The substantiated-concerns channel is accepted as a formal reporting intermediary because Article 31 imposes assessment, response and access-to-justice consequences. The public-reporting row is REJECTED as an R–I–T relation and revised to not_supported; Article 25(3) is corrected to a direct Member-State-to-Commission notification relation.", "",
        "## Recall additions and cross-case issues", "",
        "The targeted recall added the Article 27(4)-(5) circumvention-notification channel in CBAM as uncertain because the target actor is not explicit; and three direct Case 03 obligations: operators' information production under Articles 9-11, SME-trader information under Article 5(4), and operator/trader assistance to competent-authority checks under Articles 4(6) and 5(6). I did not add optional scientific inputs, general cooperation clauses, authorised representatives, certification schemes or recital-only initiatives where the act did not demonstrate a distinct regulatory intermediary.", "",
        "Recurring mechanisms are verification/certification, information transmission/reporting, enforcement support and delegated implementation. Recurring conceptual problems are actor-versus-object confusion, treating a system or data conduit as an actor, conflating co-regulators with intermediaries, and treating assistance or optional information sources as mediation. Researcher priority should go first to Case 01 Article 8(4), CBAM customs and enforcement chains, Case 03 Article 33, the substantiated-concerns channel, and the Article 27 addition.", "",
        f"Claude proposals reviewed: {claude_count}.",
    ]
    return "\n".join(lines) + "\n"


def main():
    rows = []
    claude_count = 0
    for case_id in CASE_INFO:
        proposal = json.loads(proposal_path(case_id).read_text(encoding="utf-8"))
        claude_count += len(proposal["relations"])
        for relation in proposal["relations"]:
            assert relation["relation_id"] in REVIEWS, relation["relation_id"]
            rows.append(make_claude_row(case_id, relation))
    assert claude_count == 39, claude_count
    rows.extend(make_addition_row(item) for item in ADDITIONS)
    validate(rows)
    review_path = OUTPUT / "REGULATORY_INTERMEDIARIES_3_CASES_REVIEW.csv"
    write_csv(review_path, rows)
    queue_rows = []
    for row in rows:
        if (
            row["claude_relation_type"] in {"intermediated", "uncertain"}
            or row["luna_proposed_relation_type"] in {"intermediated", "uncertain"}
            or row["luna_review_status"] in {"QUESTION", "REVISE", "ADD_MISSING_RELATION"}
            or (row["luna_review_status"] == "REJECT" and row["claude_relation_type"] == "intermediated")
            or row["external_context_required"] == "true"
        ):
            queue_rows.append(row)
    write_csv(OUTPUT / "RESEARCHER_PRIORITY_REVIEW.csv", queue_rows)
    (OUTPUT / "LUNA_SECONDARY_REVIEW_NOTE.md").write_text(build_note(rows, claude_count), encoding="utf-8")
    counts = Counter(row["luna_review_status"] for row in rows)
    print(json.dumps({
        "claude_rows_reviewed": claude_count, "review_rows": len(rows), "status_counts": counts,
        "luna_relation_types": Counter(row["luna_proposed_relation_type"] for row in rows),
        "priority_queue_rows": len(queue_rows),
        "outputs": [str(review_path), str(OUTPUT / "LUNA_SECONDARY_REVIEW_NOTE.md"), str(OUTPUT / "RESEARCHER_PRIORITY_REVIEW.csv")],
    }, ensure_ascii=False, indent=2, default=dict))


if __name__ == "__main__":
    main()
