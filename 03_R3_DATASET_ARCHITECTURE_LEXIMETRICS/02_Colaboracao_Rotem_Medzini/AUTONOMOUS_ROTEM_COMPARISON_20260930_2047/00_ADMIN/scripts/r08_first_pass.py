"""R08 — FIRST PASS (MODEL_CODED by the executing agent) under CODING_INSTRUCTIONS_FROZEN.md.

Parent values are an INTERPRETIVE_APPLICATION of the revised codebook (not Rotem's coding).
TEXT_SPAN values are extracted programmatically from the frozen provision packs via (start, end) markers,
so every span is an exact substring of its provision (asserted).
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, write_csv  # noqa: E402

PACKS = RUN_ROOT / "07_CASE_SELECTION/case_texts"
PROV = {}
for f in sorted(PACKS.glob("CASE_0*_PROVISIONS.md")):
    txt = f.read_text(encoding="utf-8")
    for m in re.finditer(r"(?ms)^## (\S+)\n\n(.*?)(?=^## |\Z)", txt):
        PROV[m.group(1)] = m.group(2).strip()


def _rx(s):
    # whitespace-tolerant pattern; returns the exact substring as it appears in the pack
    return r"\s+".join(re.escape(w) for w in s.split())


def span(pid, start, end=None):
    t = PROV[pid]
    m = re.search(_rx(start), t)
    assert m, f"start not found in {pid}: {start[:60]}"
    if end is None:
        s = m.group(0)
    else:
        m2 = re.compile(_rx(end)).search(t, m.start())
        assert m2, f"end not found in {pid}: {end[:60]}"
        s = t[m.start():m2.end()]
    assert s in t
    return s


EV = []
NS = "NOT_SPECIFIED"
NAF = "NOT_A_FUNCTION_OF_THE_INTERMEDIARY"


def ev(parent, pid, start, end=None, actor=NS, action="", addressee=NS, obj="", reg=NS, inter=NS, target=NS, role="ACTOR",
       modality="OBLIGATION", trigger="NONE", effect="NONE", fn=NAF, mech="N/A", basis="TEXTUAL", rationale="", conf="HIGH"):
    n = sum(1 for e in EV if e["PARENT_ID"] == parent) + 1
    EV.append(dict(EVENT_ID=f"{parent}-E{n:02d}", PARENT_ID=parent, SOURCE_PROVISION_ID=pid, TEXT_SPAN=span(pid, start, end),
                   ACTOR=actor, ACTION=action, ACTION_ADDRESSEE=addressee, OBJECT=obj, REGULATOR_ACTOR=reg, INTERMEDIARY_ACTOR=inter,
                   TARGET_ACTOR=target, INTERMEDIARY_ROLE_IN_EVENT=role, NORMATIVE_MODALITY=modality, TRIGGER_CONDITION=trigger,
                   LEGAL_EFFECT=effect, FUNCTION_CODE=fn, MECHANISM_CODE=mech, INFERENCE_BASIS=basis, RATIONALE=rationale,
                   CONFIDENCE=conf, REVIEW_STATUS="MODEL_CODED"))


# ---------------- CASE_01 — 32004R0874 ----------------
A = "32004R0874:"
# Independent auditor
ev("P01_AUD", A + "A12(5)", "The auditor shall be appointed by the Registry after consulting the Commission.", actor="Registry", action="shall appoint (passive: 'shall be appointed by')",
   addressee=NS, obj="the auditor", reg="Commission (consulted)", inter="the auditor", role="OBJECT", rationale="Appointment of the intermediary by the Registry = recognition/selection event; split from the consultation (rule 1).")
ev("P01_AUD", A + "A12(5)", "after consulting the Commission", actor="Registry", action="shall consult (before appointment)", addressee="Commission", obj="appointment of the auditor",
   reg="Commission", inter="the auditor", role="OBJECT", trigger="before appointment of the auditor", rationale="Distinct directional action Registry→Commission (consultation), split per rule 1 (cf. H_015).")
ev("P01_AUD", A + "A12(5)", "At the end of the phased registration an independent audit shall be performed at the expense of the Registry", actor="the auditor (inferred; passive voice)",
   action="shall perform an independent audit", obj="operational and technical administration of the phased registration period by the Registry (purpose sentence)", inter="the auditor", target="Registry",
   trigger="At the end of the phased registration", effect="audit performed at the expense of the Registry (cost borne by the audited entity)", fn="auditing", mech="Assurance", basis="INFERENTIAL",
   rationale="Agent omitted (passive); 'The auditor' in the next sentence and the purpose sentence identify actor and object within the same provision. Identified as an audit → auditing; confirming sound administration also verifies conformity (assurance). No mechanism family for auditing; Assurance used.", conf="MEDIUM")
ev("P01_AUD", A + "A12(5)", "shall report its findings to the Commission", actor="the auditor (grammatical subject: 'an independent audit')", action="shall report its findings",
   addressee="Commission", obj="audit findings", reg="Commission", inter="the auditor", target="Registry", fn="auditing", mech="Assurance", basis="INFERENTIAL",
   rationale="Transmission of the audit result to the regulator is the reporting component of the audit; the revised codebook treats reporting as an obligation of the intermediary (¶85), the function remains auditing.", conf="MEDIUM")
# Validation agents
ev("P01_VAL", A + "A13", "Validation agents shall be legal persons established within the territory of the Community.", None, actor=NS, action="shall be (eligibility condition)", obj="legal form and establishment of validation agents",
   inter="Validation agents", role="OBJECT", modality="DEFINITION_OR_STATUS", effect="eligibility condition for acting as validation agent", rationale="Regulation of the intermediary (eligibility); not a function.")
ev("P01_VAL", A + "A13", "The Registry shall select the validation agents", "ensuring the widest possible geographical diversity.", actor="Registry", action="shall select", obj="validation agents",
   inter="validation agents", role="OBJECT", rationale="Selection of the intermediary by the Registry (a non-public body) under procedural criteria: recognition event.")
ev("P01_VAL", A + "A13", "The Registry shall require the validation agent to execute the validation in an objective, transparent and non-discriminatory manner.", actor="Registry", action="shall require",
   addressee="the validation agent", obj="manner of executing validation", inter="the validation agent", role="ADDRESSEE", rationale="Registry imposes procedural requirements on the intermediary (regulation of the intermediary).")
ev("P01_VAL", A + "A13", "Member States shall provide for validation concerning the names mentioned in Article 10(3).", actor="Member States", action="shall provide for validation", obj="validation of names under Article 10(3)",
   reg="Member States", role="NOT_PRESENT", rationale="Parallel validation channel under Member State responsibility; validation agents not mentioned; recorded because it adds a national regulator to the validation function.", conf="MEDIUM")
ev("P01_VAL", A + "A13", "the Member States shall send to the Commission", "for verification.", actor="Member States", action="shall send", addressee="Commission",
   obj="addresses to which documentary evidence is to be sent for verification", reg="Member States; Commission", role="NOT_PRESENT", trigger="within two months following entry into force of this Regulation")
ev("P01_VAL", A + "A13", "The Commission shall notify the Registry of these addresses.", actor="Commission", action="shall notify", addressee="Registry", obj="addresses for verification of Article 10(3) names",
   reg="Commission", role="NOT_PRESENT")
ev("P01_VAL", A + "A13", "The Registry shall publish information about the validation agents at its website.", actor="Registry", action="shall publish", addressee="public (website)",
   obj="information about the validation agents", inter="validation agents", role="OBJECT")
ev("P01_VAL", A + "A14", "The Registry, upon receipt of the application, shall block the domain name in question until validation has taken place", actor="Registry", action="shall block",
   obj="the domain name applied for", target="applicant", role="NOT_PRESENT", trigger="upon receipt of the application; until validation has taken place or the documentation deadline passes",
   effect="domain name blocked pending validation", rationale="Registry action conditioned on the intermediary's validation output.", conf="MEDIUM")
ev("P01_VAL", A + "A14", "Every applicant shall submit documentary evidence that shows that he or she is the holder of the prior right claimed on the name in question.", actor="applicant", action="shall submit",
   addressee="a validation agent indicated by the Registry (next sentence)", obj="documentary evidence of the prior right", inter="validation agent", target="applicant", role="ADDRESSEE",
   rationale="Direct applicant→validation agent edge (cf. H_016); addressee stated in the immediately following sentence.")
ev("P01_VAL", A + "A14", "The documentary evidence shall be submitted to a validation agent indicated by the Registry.", actor="Registry", action="indicates (participial clause)", addressee="applicant",
   obj="the competent validation agent", inter="a validation agent", target="applicant", role="OBJECT", modality="DEFINITION_OR_STATUS", basis="INFERENTIAL",
   rationale="Separate Registry→applicant relation (indication of the agent) kept distinct from the applicant's submission duty (H_016).", conf="MEDIUM")
ev("P01_VAL", A + "A14", "If the documentary evidence has not been received by this deadline, the application for the domain name shall be rejected.", actor=NS, action="shall be rejected",
   obj="the application", target="applicant", role="NOT_PRESENT", trigger="If the documentary evidence has not been received by this deadline", effect="rejection of the application",
   rationale="Legal effect; actor not specified (passive). Not recast as an actor edge (rule 5).")
ev("P01_VAL", A + "A14", "Validation agents shall time-stamp documentary evidence upon receipt.", actor="Validation agents", action="shall time-stamp", obj="documentary evidence", inter="Validation agents",
   target="applicant", trigger="upon receipt", rationale="Procedural duty on the intermediary (revised codebook obligations: procedural compliance / recordkeeping); not itself a regulatory function.", conf="MEDIUM")
ev("P01_VAL", A + "A14", "Validation agents shall examine applications for any particular domain name in the order in which the application was received at the Registry.", actor="Validation agents",
   action="shall examine (in order of receipt)", obj="applications", inter="Validation agents", target="applicant", rationale="Ordering rule (procedural compliance).", conf="MEDIUM")
ev("P01_VAL", A + "A14", "The relevant validation agent shall examine whether the applicant", "has prior rights on the name.", actor="The relevant validation agent", action="shall examine whether",
   obj="whether the applicant first in line has prior rights on the name", inter="The relevant validation agent", target="applicant", fn="assurance", mech="Assurance",
   rationale="Verification of a claimed legal entitlement against documentary evidence = assessing conformity with regulatory requirements.")
ev("P01_VAL", A + "A14", "If the documentary evidence has not been received in time or if the validation agent finds that the documentary evidence does not substantiate a prior right, he shall notify the Registry of this.",
   actor="validation agent", action="shall notify", addressee="Registry", obj="negative validation result", inter="validation agent", target="applicant",
   trigger="If the documentary evidence has not been received in time or if the validation agent finds that the documentary evidence does not substantiate a prior right", fn="assurance", mech="Assurance",
   rationale="Communication of the verification outcome to the decision-maker; transmission is a component of the assurance function (reporting = obligation under ¶85).", conf="MEDIUM")
ev("P01_VAL", A + "A14", "If the validation agent finds that prior rights exist regarding the application for a particular domain name that is first in line, he shall notify the Registry accordingly.",
   actor="validation agent", action="shall notify", addressee="Registry", obj="positive validation result", inter="validation agent", target="applicant",
   trigger="If the validation agent finds that prior rights exist", fn="assurance", mech="Assurance", conf="MEDIUM")
ev("P01_VAL", A + "A14", "The Registry shall register the domain name, on the first come first served basis, if it finds that the applicant has demonstrated a prior right", actor="Registry", action="shall register",
   obj="the domain name", target="applicant", role="NOT_PRESENT", trigger="if it finds that the applicant has demonstrated a prior right", effect="registration of the domain name",
   rationale="Decision remains with the Registry; the intermediary's finding is an input (assurance output → registry decision).")
# ADR providers
ev("P01_ADR", A + "A22(5)", "The complaints and the responses to those complaints must be submitted to an ADR provider chosen by the complainant", actor="complainant (inferred; passive)", action="must submit",
   addressee="ADR provider", obj="complaint", inter="ADR provider", role="ADDRESSEE", basis="INFERENTIAL", rationale="Split complaint/response submissions (H_017); complainant inferred as submitter of the complaint.", conf="MEDIUM")
ev("P01_ADR", A + "A22(5)", "The complaints and the responses to those complaints must be submitted to an ADR provider chosen by the complainant", actor="respondent (inferred; passive)", action="must submit",
   addressee="ADR provider", obj="response to the complaint", inter="ADR provider", role="ADDRESSEE", basis="INFERENTIAL", conf="MEDIUM")
ev("P01_ADR", A + "A22(5)", "an ADR provider chosen by the complainant from the list referred to in the first paragraph of Article 23", actor="complainant", action="chooses", obj="ADR provider (from the Registry's list)",
   inter="ADR provider", role="OBJECT", modality="DEFINITION_OR_STATUS", rationale="Selection of the specific provider by the user, within a list set by the Registry (A23(1)).")
ev("P01_ADR", A + "A22(6)", "the ADR provider shall inform the Registry of the identity of the complainant and the domain name involved", actor="the ADR provider", action="shall inform", addressee="Registry",
   obj="identity of the complainant and the domain name involved", inter="the ADR provider", trigger="As soon as a request for ADR is properly filed with the ADR provider and the appropriate fee is paid",
   fn="dispute_resolution", mech="Dispute resolution", rationale="Procedural transmission to the Registry within the dispute-resolution function; triggers the Registry's suspension.", conf="MEDIUM")
ev("P01_ADR", A + "A22(6)", "The Registry shall suspend the domain name involved from cancellation or transfer until the dispute resolution proceedings or subsequent legal proceedings are complete", actor="Registry",
   action="shall suspend", obj="the domain name involved (from cancellation or transfer)", role="NOT_PRESENT", trigger="after being informed of a properly filed request (preceding sentence)",
   effect="domain name frozen pending proceedings", rationale="Registry action triggered by the intermediary's notification; legal effect kept on the Registry's action.", conf="MEDIUM")
ev("P01_ADR", A + "A22(7)", "The ADR provider shall examine the complaint for compliance with its rules of procedure", "Regulation (EC) No 733/2002", actor="The ADR provider", action="shall examine",
   obj="the complaint (compliance with procedural rules and Regulations 874/2004 and 733/2002)", inter="The ADR provider", fn="complaint_handling", mech="Complaint handling",
   rationale="Receiving and assessing a complaint for admissibility = complaint handling (¶82); the later panel decision is dispute resolution.", conf="MEDIUM")
ev("P01_ADR", A + "A22(7)", "shall forward the complaint to the respondent within five working days following receipt of the fees to be paid by the complainant", actor="The ADR provider", action="shall forward",
   addressee="the respondent", obj="the complaint", inter="The ADR provider", target="respondent (domain name holder or Registry)", trigger="unless non-compliance is established", fn="complaint_handling",
   mech="Complaint handling", conf="MEDIUM")
ev("P01_ADR", A + "A23(1)", "The Registry may select ADR providers, who shall be reputable bodies with appropriate expertise in an objective, transparent and non-discriminatory manner.", actor="Registry",
   action="may select", obj="ADR providers", inter="ADR providers", role="OBJECT", modality="PERMISSION", rationale="Selection (recognition) of the intermediary by a non-public body; permissive.")
ev("P01_ADR", A + "A23(1)", "A list of the ADR providers shall be published on the Registry's website.", actor="Registry (inferred: 'Registry's website')", action="shall publish", addressee="public",
   obj="list of ADR providers", inter="ADR providers", role="OBJECT", basis="INFERENTIAL", conf="MEDIUM")

# ---------------- CASE_02 — 31989L0336 ----------------
B = "31989L0336:"
ev("P02_CB", B + "A10(2)", "the manufacturer or his authorized representative established within the Community shall hold at the disposal of the relevant competent authorities", "a technical construction file.",
   actor="the manufacturer or his authorized representative", action="shall hold at the disposal of", addressee="the relevant competent authorities", obj="technical construction file",
   reg="competent authorities", target="manufacturer", role="NOT_PRESENT",
   trigger="In the case of apparatus for which the manufacturer has not applied, or has applied only in part, the standards referred to in Article 7 (1) or failing such standards")
ev("P02_CB", B + "A10(2)", "include a technical report or certificate, one or other obtained from a competent body", actor="manufacturer (obtains; inferred)", action="[shall] obtain (file shall include)",
   addressee="a competent body", obj="technical report or certificate", inter="a competent body", target="manufacturer", role="ACTOR", fn="assurance", mech="Assurance", basis="INFERENTIAL",
   rationale="The competent body issues the report/certificate that the file must contain; the act presupposes, but does not impose as a duty, the body's assurance activity.", conf="MEDIUM")
ev("P02_CB", B + "A10(2)", "Member States shall presume, subject to the provisions of this paragraph, that such apparatus meets the protection requirements referred to in Article 4.", actor="Member States",
   action="shall presume", obj="conformity of the apparatus with the protection requirements", reg="Member States", target="manufacturer", role="NOT_PRESENT", effect="presumption of conformity",
   rationale="Legal effect attached to the certified file; not an actor edge with the competent body.")
ev("P02_NB", B + "A10(4)", "once the manufacturer or his authorized representative established within the Community has obtained an EC type-examination certificate concerning this apparatus issued by one of the notified bodies",
   actor="the manufacturer or his authorized representative", action="has obtained", addressee="one of the notified bodies", obj="EC type-examination certificate", inter="notified bodies",
   target="manufacturer", role="ACTOR", trigger="for apparatus covered by Article 2 (2) of Directive 86/361/EEC", fn="assurance", mech="Assurance",
   rationale="Certificate issued by the notified body is the condition for certifying conformity: assurance by the intermediary.")
ev("P02_NB", B + "A10(6)", "Each Member State shall notify the Commission and the other Member States of the competent authorities referred to in this Article and of the bodies responsible for issuing the EC type-examination certificates referred to in paragraphs 4 and 5.",
   actor="Each Member State", action="shall notify", addressee="the Commission and the other Member States", obj="competent authorities and bodies responsible for EC type-examination certificates",
   reg="Member States; Commission", inter="notified bodies", role="OBJECT", rationale="Notification is addressed to the Commission and the other Member States, not to the bodies (cf. H_006, H_011).")
ev("P02_NB", B + "A10(6)", "The Commission shall publish a list of those authorities and bodies, for information purposes", "shall ensure that the list is updated.", actor="The Commission",
   action="shall publish; shall ensure updating", addressee="public (Official Journal)", obj="list of authorities and bodies", reg="Commission", inter="notified bodies", role="OBJECT",
   effect="publication 'for information purposes' (no constitutive effect stated)")
ev("P02_NB", B + "A10(6)", "Member States shall apply the criteria listed in Annex II for the assessment of the bodies to be notified.", actor="Member States", action="shall apply criteria for the assessment of",
   obj="bodies to be notified", reg="Member States", inter="bodies to be notified", role="OBJECT", rationale="Vetting of the intermediary against Annex II before notification.")
ev("P02_NB", B + "A10(6)", "Bodies which comply with the assessment criteria fixed by the relevant harmonized standards shall be presumed to comply with the aforementioned criteria.", actor=NS,
   action="shall be presumed to comply", obj="compliance of bodies with Annex II criteria", inter="Bodies", role="OBJECT", modality="DEFINITION_OR_STATUS", effect="presumption of compliance with Annex II")
ev("P02_NB", B + "A10(6)", "A Member State which has notified a body must withdraw approval if it finds that the body no longer meets the criteria listed in Annex II.", actor="A Member State which has notified a body",
   action="must withdraw approval", obj="approval of the body", reg="Member State", inter="the body", role="OBJECT", trigger="if it finds that the body no longer meets the criteria listed in Annex II",
   effect="withdrawal of approval")
ev("P02_NB", B + "A10(6)", "It shall forthwith inform the Commission and the other Member States thereof.", actor="Member State (that withdrew approval)", action="shall inform", addressee="the Commission and the other Member States",
   obj="withdrawal of approval", reg="Member State; Commission", inter="the body", role="OBJECT", trigger="after withdrawal of approval")
ev("P02_NB", B + "ANNEX_II", "The bodies designated by the Member States must fulfil the following minimum conditions:", actor="The bodies designated by the Member States", action="must fulfil",
   obj="minimum conditions (points 1-5)", reg="Member States", inter="The bodies designated by the Member States", role="ACTOR", modality="OBLIGATION",
   rationale="Requirements on the intermediary itself (regulation of the intermediary).")
ev("P02_NB", B + "ANNEX_II", "independence, in carrying out the tests, preparing the reports, issuing the certificates and performing the verification function provided for in this Directive", actor="staff and technical personnel of the bodies",
   action="[must be] independent in carrying out", obj="tests, reports, certificates and the verification function", inter="bodies", role="ACTOR", modality="OBLIGATION",
   rationale="Independence requirement; it also evidences the bodies' assurance tasks (tests, reports, certificates, verification).", conf="MEDIUM")
ev("P02_NB", B + "ANNEX_II", "5. possession of civil liability insurance unless such liability is covered by the State under national law.", actor="The bodies designated by the Member States (chapeau)",
   action="[must possess]", obj="civil liability insurance", inter="bodies", role="ACTOR", trigger="unless such liability is covered by the State under national law", basis="INFERENTIAL",
   rationale="Condition on the notified body; the insurer is not named and performs no stated action.", conf="MEDIUM")
ev("P02_NB", B + "ANNEX_II", "Fulfilment of the conditions under points 1 and 2 shall be verified at intervals by the competent authorities of the Member States.", actor="the competent authorities of the Member States",
   action="shall verify at intervals", obj="fulfilment of conditions 1 and 2 by the bodies", reg="competent authorities of the Member States", inter="bodies", role="OBJECT",
   rationale="Ongoing supervision of the intermediary by public authorities (only points 1 and 2; not insurance).")
ev("P02_INS", B + "ANNEX_II", "5. possession of civil liability insurance unless such liability is covered by the State under national law.", actor="The bodies designated by the Member States (chapeau)",
   action="[must possess]", addressee=NS, obj="civil liability insurance", inter="NOT_SPECIFIED (insurer not named)", target="notified bodies", role="NOT_PRESENT",
   trigger="unless such liability is covered by the State under national law", fn=NAF, mech="N/A", basis="INFERENTIAL",
   rationale="The only textual trace of the insurer: an obligation on the bodies. Under REV ¶28 this necessarily relies on an insurance provider (structural reliance); the text assigns no action, addressee or regulatory function to the insurer.", conf="HIGH")

# ---------------- CASE_03 — 31991L0263 ----------------
C = "31991L0263:"
ev("P03_NB", C + "A10(1)", "Member States shall notify to the Commission the bodies established in the Community", "pertaining to the procedures referred to in Article 9.", actor="Member States", action="shall notify",
   addressee="the Commission", obj="designated bodies and their identifying symbols", reg="Member States; Commission", inter="the bodies", role="OBJECT")
ev("P03_NB", C + "A10(1)", "Member States shall apply the minimum criteria, set out in Annex V, for the designation of such bodies.", actor="Member States", action="shall apply minimum criteria for the designation of",
   obj="such bodies", reg="Member States", inter="such bodies", role="OBJECT", rationale="Vetting before designation.")
ev("P03_NB", C + "A10(1)", "Bodies that satisfy the criteria fixed by the relevant harmonized standards shall be presumed to satisfy the criteria set out in Annex V.", modality="DEFINITION_OR_STATUS",
   action="shall be presumed to satisfy", obj="Annex V criteria", inter="Bodies", role="OBJECT", effect="presumption of compliance with Annex V")
ev("P03_NB", C + "A10(4)", "A Member State has designated a notified body or a test laboratory under paragraph 1 or 2 shall annul the designation if the notified body or the test laboratory no longer meets the relevant cirteria for designation.",
   actor="A Member State [which] has designated", action="shall annul the designation", obj="designation of the notified body", reg="Member State", inter="notified body", role="OBJECT",
   trigger="if the notified body or the test laboratory no longer meets the relevant cirteria for designation", effect="annulment of designation")
ev("P03_NB", C + "A10(4)", "Where a Member State or the Commission considers that a notified body or a test laboratory designated by a Member State does not meet the relevant criteria the matter shall be brought before the Committee referred to in Article 13",
   actor=NS, action="shall be brought before", addressee="the Committee referred to in Article 13", obj="compliance of the notified body with designation criteria", reg="Member State; Commission; Committee",
   inter="notified body", role="OBJECT", trigger="Where a Member State or the Commission considers that a notified body ... does not meet the relevant criteria", basis="TEXTUAL")
ev("P03_NB", C + "A10(4)", "in the light of the Committee's opinion the Commission shall inform the Member State concerned of any changes needed if that notified body or test laboratory is to retain its recognized status.",
   actor="the Commission", action="shall inform", addressee="the Member State concerned", obj="changes needed for the body to retain recognized status", reg="Commission", inter="notified body", role="OBJECT",
   trigger="in the light of the Committee's opinion", effect="retention of recognized status conditional on changes")
ev("P03_NB", C + "ANNEX_III(3.1)", "The manufacturer shall lodge an application for assessment of his quality system with a notified body of his choice, for the products concerned.", actor="The manufacturer",
   action="shall lodge an application", addressee="a notified body of his choice", obj="assessment of his quality system", inter="notified body", target="manufacturer", role="ADDRESSEE",
   rationale="Target selects and addresses the intermediary (selection by the regulated entity).")
ev("P03_NB", C + "ANNEX_III(3.3)", "The notified body shall assess the quality system to determine whether it satisfies the requirements referred to in point 3.2.", actor="The notified body", action="shall assess",
   obj="the manufacturer's quality system (against point 3.2)", inter="The notified body", target="manufacturer", fn="assurance", mech="Assurance", rationale="Assessment against stated requirements = assurance (consistent with H_012/H_013).")
ev("P03_NB", C + "ANNEX_III(3.3)", "It shall presume conformity with these requirements in respect of quality systems that implement the relevant harmonized standard", actor="The notified body", action="shall presume conformity",
   obj="quality systems implementing the harmonized standard", inter="The notified body", target="manufacturer", modality="OBLIGATION", effect="presumption of conformity", fn="assurance", mech="Assurance", conf="MEDIUM")
ev("P03_NB", C + "ANNEX_III(3.3)", "The auditing team shall have at least one member with experience of evaluation in the product technology concerned. The evaluation procedure shall include an inspection visit to the manufacturer's premises.",
   actor="The auditing team (of the notified body)", action="shall include an inspection visit", addressee="manufacturer (premises)", obj="evaluation procedure / inspection visit", inter="notified body", target="manufacturer",
   fn="assurance", mech="Assurance", rationale="Composition and method of the assessment. The text uses 'auditing team' and 'evaluation procedure' inside the assessment of point 3.3; under REV ¶82 'auditing' = 'identified or structured as an audit', so auditing is a defensible alternative. Kept assurance (assessment procedure; H_014 distinguishes it from the periodic audits of point 4).", conf="LOW")
ev("P03_NB", C + "ANNEX_III(3.3)", "The decision shall be notified to the manufacturer. The notification shall contain the conclusions of the examination and the reasoned assessment decision.", actor="notified body (inferred; passive)",
   action="shall notify", addressee="the manufacturer", obj="reasoned assessment decision", inter="notified body", target="manufacturer", fn="assurance", mech="Assurance", basis="INFERENTIAL", conf="MEDIUM")
ev("P03_NB", C + "ANNEX_III(3.4)", "The manufacturer or his authorized representative shall keep the notified body that has approved the quality system informed of any intended updating of the quality system.",
   actor="The manufacturer or his authorized representative", action="shall keep informed", addressee="the notified body that has approved the quality system", obj="intended updating of the quality system",
   inter="the notified body", target="manufacturer", role="ADDRESSEE", rationale="Transmission of regulatory information from target to intermediary.")
ev("P03_NB", C + "ANNEX_III(3.4)", "The notified body shall evaluate the modifications proposed and decide whether the amended quality system will still satisfy the requirements referred to in point 3.2. or whether a re-assessment is required.",
   actor="The notified body", action="shall evaluate and decide", obj="proposed modifications of the quality system", inter="The notified body", target="manufacturer", trigger="upon notification of intended updating (preceding sentence)",
   fn="assurance", mech="Assurance", rationale="'Evaluate' in the text = conformity assessment of changes (assurance); REV has no 'evaluation' function.", conf="HIGH")
ev("P03_NB", C + "ANNEX_III(3.4)", "It shall notify its decision to the manufacturer.", actor="The notified body", action="shall notify", addressee="the manufacturer", obj="decision on the amended quality system",
   inter="The notified body", target="manufacturer", fn="assurance", mech="Assurance")
ev("P03_NB", C + "ANNEX_III(4)", "4.Surveillance under the responsibility of the notified body", "approved quality system.", actor="the notified body (heading)", action="[surveillance] to make sure",
   obj="fulfilment by the manufacturer of the obligations arising out of the approved quality system", inter="the notified body", target="manufacturer", modality="DEFINITION_OR_STATUS", fn="monitoring", mech="Monitoring",
   rationale="Purpose clause of continuing surveillance = systematic tracking of compliance (monitoring).")
ev("P03_NB", C + "ANNEX_III(4)", "4.2.The manufacturer shall allow the notified body access for inspection purpose", "shall provide it with all necessary information", actor="The manufacturer", action="shall allow access; shall provide information",
   addressee="the notified body", obj="locations of manufacture, inspection, testing and storage; necessary information", inter="the notified body", target="manufacturer", role="ADDRESSEE",
   rationale="Target→intermediary information and access duty.")
ev("P03_NB", C + "ANNEX_III(4)", "4.3.The notified body shall carry out audits at reasonable intervals to make sure that the manufacturer maintains and applies the quality system", actor="The notified body",
   action="shall carry out audits at reasonable intervals", obj="maintenance and application of the quality system", inter="The notified body", target="manufacturer", fn="auditing", mech="Monitoring",
   rationale="Expressly identified as audits (REV ¶82: auditing = 'identified or structured as an audit'); periodic, so mechanism Monitoring (no auditing family exists).")
ev("P03_NB", C + "ANNEX_III(4)", "and shall provide an audit report to the manufacturer", actor="The notified body", action="shall provide", addressee="the manufacturer", obj="audit report", inter="The notified body",
   target="manufacturer", fn="auditing", mech="Monitoring", rationale="The audit report goes to the audited manufacturer; no addressee among public authorities in this point.")
ev("P03_NB", C + "ANNEX_III(4)", "4.4.Additionally, the notified body may pay unexpected visits to the manufacturer.", actor="the notified body", action="may pay unexpected visits", addressee="the manufacturer",
   inter="the notified body", target="manufacturer", modality="PERMISSION", fn="monitoring", mech="Monitoring")
ev("P03_NB", C + "ANNEX_III(4)", "During such visits the notified body may carry out, or cause to be carried out, tests to verify that the quality system is functionning correctly, if necessary.", actor="the notified body",
   action="may carry out, or cause to be carried out, tests", obj="correct functioning of the quality system", inter="the notified body", target="manufacturer", modality="PERMISSION", trigger="During such visits; if necessary",
   fn="monitoring", mech="Monitoring", rationale="Verification tests within surveillance visits; assurance is a defensible alternative.", conf="MEDIUM")
ev("P03_NB", C + "ANNEX_III(4)", "The notified body shall provide the manufacturer with a visit report and, if a test has taken place, with a report.", actor="The notified body", action="shall provide",
   addressee="the manufacturer", obj="visit report; test report", inter="The notified body", target="manufacturer", trigger="if a test has taken place (test report)", fn="monitoring", mech="Monitoring")
ev("P03_NB", C + "A10(2)", "Notified bodies shall apply the criteria fixed by the appropriate parts of the", "for the designation of such laboratories.", actor="Notified bodies", action="shall apply criteria for the designation of",
   obj="test laboratories", inter="Notified bodies", target="test laboratories", fn="assurance", mech="Assurance",
   rationale="Secondary intermediation: notified bodies apply designation criteria to another intermediary (REV ¶31 'secondary'; orientation intermediary-facing).", conf="MEDIUM")
ev("P03_NB", C + "ANNEX_V(6)", "6.The notified body must take out liability insurance unless its liability is assumed by the State in accordance with national law, or the Member State itself is directly responsible.",
   actor="The notified body", action="must take out", obj="liability insurance", inter="The notified body", role="ACTOR",
   trigger="unless its liability is assumed by the State in accordance with national law, or the Member State itself is directly responsible", rationale="Requirement on the intermediary (liability_financial_cover).")
ev("P03_TL", C + "A10(2)", "2. Member States shall inform the Commission of test laboratories established in the Community which they have designated for carrying out tests pertaining to the procedures referred to in Article 9.",
   actor="Member States", action="shall inform", addressee="the Commission", obj="designated test laboratories", reg="Member States; Commission", inter="test laboratories", role="OBJECT",
   rationale="'inform' is directed to the Commission, not to the laboratories; 'designated' qualifies the laboratories (H_011).")
ev("P03_TL", C + "A10(2)", "Notified bodies shall apply the criteria fixed by the appropriate parts of the", "for the designation of such laboratories.", actor="Notified bodies", action="shall apply criteria for the designation of",
   obj="test laboratories", inter="such laboratories", role="OBJECT", rationale="Designation criteria for the laboratories are applied by another intermediary (notified bodies).", conf="MEDIUM")
ev("P03_TL", C + "A10(4)", "A Member State has designated a notified body or a test laboratory under paragraph 1 or 2 shall annul the designation if the notified body or the test laboratory no longer meets the relevant cirteria for designation.",
   actor="A Member State [which] has designated", action="shall annul the designation", obj="designation of the test laboratory", reg="Member State", inter="test laboratory", role="OBJECT",
   trigger="if ... the test laboratory no longer meets the relevant cirteria for designation", effect="annulment of designation")
ev("P03_INS", C + "ANNEX_V(6)", "6.The notified body must take out liability insurance unless its liability is assumed by the State in accordance with national law, or the Member State itself is directly responsible.",
   actor="The notified body", action="must take out", obj="liability insurance", inter="NOT_SPECIFIED (insurer not named)", target="notified body", role="NOT_PRESENT",
   trigger="unless its liability is assumed by the State in accordance with national law, or the Member State itself is directly responsible", basis="INFERENTIAL",
   rationale="Only textual trace of the insurer; identification would rest on REV ¶28 necessary reliance.")

# ---------------- CASE_04 — 31986L0361 ----------------
D = "31986L0361:"
ev("P04_LAB", D + "A2(8)", "'approved testing laboratory' means a laboratory the conformity of which with the accreditation system", "for conducting conformity tests on terminal equipment;",
   actor="the appropriate Member State or a body recognized as competent by that State", action="has verified (conformity with accreditation system); approves", obj="the laboratory",
   reg="Member State; body recognized as competent by that State", inter="approved testing laboratory", role="OBJECT", modality="DEFINITION_OR_STATUS",
   effect="status of 'approved testing laboratory'", rationale="Definition embeds the recognition pathway: verification against an accreditation system, then approval (vetting).")
ev("P04_LAB", D + "A7(2)", "Member States shall send the Commission a list of the laboratories which they have approved", "with the common conformity specifications.", actor="Member States", action="shall send",
   addressee="the Commission", obj="list of approved laboratories", reg="Member States; Commission", inter="the laboratories", role="OBJECT")
ev("P04_LAB", D + "A7(2)", "They shall regularly submit a report on the activities of these laboratories in the field covered by this Directive.", actor="Member States", action="shall regularly submit",
   addressee="NOT_SPECIFIED (the Commission by context)", obj="report on the activities of the laboratories", reg="Member States", inter="these laboratories", role="OBJECT", basis="INFERENTIAL",
   rationale="Monitoring of the intermediaries by the regulator; addressee omitted in this sentence.", conf="MEDIUM")
ev("P04_LAB", D + "A7(2)", "Such lists and reports shall be transmitted to the Committee referred to in Article 5 for information.", action="shall be transmitted", addressee="the Committee referred to in Article 5",
   obj="lists and reports on laboratories", inter="laboratories", role="OBJECT", effect="for information only")
ev("P04_LAB", D + "A7(3)", "For the purposes of Article 6, the certificate of conformity issued by the approved laboratory which has carried out the tests must be accompanied by the data obtained from the measurements performed during the conformity tests",
   actor="the approved laboratory which has carried out the tests (issuer)", action="[issues certificate; certificate] must be accompanied by", obj="certificate of conformity with measurement data",
   inter="the approved laboratory", target="NOT_SPECIFIED (equipment applicant not named)", trigger="For the purposes of Article 6", fn="assurance", mech="Assurance",
   rationale="The laboratory tests and certifies conformity (assurance); content requirements for its output.")
ev("P04_LAB", D + "A8(1)", "1. A Member State may, after examining the common conformity specification and the test results, suspend recognition of a certificate of conformity issued for the purpose of type approval:",
   actor="A Member State", action="may suspend recognition", obj="certificate of conformity (output of the intermediary)", reg="Member State", inter="approved laboratory (issuer, implicit)", role="OBJECT",
   modality="PERMISSION", trigger="(a) shortcomings in applying the common conformity specification; (b) the specification fails to meet the essential requirements", effect="suspension of recognition of the certificate",
   basis="INFERENTIAL", rationale="The certificate is the laboratory's output (Art 7(3)); the laboratory itself is not named here.", conf="MEDIUM")
ev("P04_LAB", D + "A8(1)", "If it exercises this option, the Member State concerned shall immediately inform the Commission and the other Member States, stating the reasons for its decision.", actor="the Member State concerned",
   action="shall immediately inform", addressee="the Commission and the other Member States", obj="decision to suspend and its reasons", reg="Member State; Commission", role="NOT_PRESENT",
   trigger="If it exercises this option")
ev("P04_LAB", D + "A8(3)", "3. If the reasons given for the Member State's decision are as described in paragraph 1 (a), the Commission shall immediately consult the Member States concerned.", actor="the Commission",
   action="shall immediately consult", addressee="the Member States concerned", reg="Commission", role="NOT_PRESENT", trigger="If the reasons given for the Member State's decision are as described in paragraph 1 (a)")
ev("P04_LAB", D + "A8(3)", "If no agreement is reached without four weeks, the Commission shall seek the opinion of one of the approved laboratories notified in accordance with Article 7 which is based outside the territory of the Member States concerned.",
   actor="the Commission", action="shall seek the opinion of", addressee="one of the approved laboratories ... based outside the territory of the Member States concerned", obj="opinion on the disputed suspension",
   reg="Commission", inter="approved laboratory", role="ADDRESSEE", trigger="If no agreement is reached without four weeks [and reasons under paragraph 1 (a)]",
   rationale="Mandatory ('shall') but doubly conditional involvement of the intermediary (derived conditional position, cf. H_002). The PILOT_03 summary 'may seek' is not supported by the text.")
ev("P04_LAB", D + "A8(3)", "The Commission shall communicate the opinion of this laboratory to all the Member States", actor="approved laboratory (gives opinion; inferred from 'the opinion of this laboratory')",
   action="[gives] opinion", addressee="the Commission", obj="opinion on the disputed certificate/test results", reg="Commission", inter="this laboratory", role="ACTOR",
   trigger="when consulted under the conditions above", fn="assurance", mech="Assurance", basis="INFERENTIAL",
   rationale="The laboratory's opinion is presupposed. It is an expert technical assessment (closest REV function: assurance); the laboratory does not resolve the dispute (the Commission formulates recommendations). REV has no 'evaluation/advice' function.", conf="LOW")
ev("P04_LAB", D + "A8(3)", "The Commission shall communicate the opinion of this laboratory to all the Member States", actor="The Commission", action="shall communicate", addressee="all the Member States",
   obj="the opinion of this laboratory", reg="Commission", inter="this laboratory", role="OBJECT", rationale="Transmission of the intermediary's output by the regulator.")
ev("P04_LAB", D + "A8(3)", "which may submit their comments to it within a period of one month", actor="Member States", action="may submit comments", addressee="the Commission", obj="comments on the laboratory's opinion",
   reg="Member States; Commission", role="NOT_PRESENT", modality="PERMISSION", trigger="within a period of one month")
ev("P04_LAB", D + "A8(3)", "After taking note of any such comments the Commission shall, if necessary, formulate appropriate recommendations or opinions.", actor="the Commission", action="shall formulate (if necessary)",
   obj="recommendations or opinions", reg="Commission", role="NOT_PRESENT", trigger="if necessary; after taking note of comments", rationale="Decision power stays with the Commission.")
ev("P04_LAB", D + "A8(3)", "If in preparing its opinion a laboratory consulted unavoidably incurs expenditure, which may if necessary include additional tests, the Commission will defray that expenditure on production of documentary evidence.",
   actor="the Commission", action="will defray", addressee="a laboratory consulted", obj="expenditure incurred in preparing the opinion", reg="Commission", inter="a laboratory consulted", role="BENEFICIARY",
   trigger="If in preparing its opinion a laboratory consulted unavoidably incurs expenditure; on production of documentary evidence", effect="reimbursement of the laboratory")
ev("P04_LAB", D + "A8(3)", "If, however, further to an opinion a decision to suspend recognition of a certificate of conformity is not maintained, the Member State which took it shall reimburse the Commission",
   actor="the Member State which took it", action="shall reimburse", addressee="the Commission", reg="Member State; Commission", role="NOT_PRESENT",
   trigger="If, however, further to an opinion a decision to suspend recognition of a certificate of conformity is not maintained", effect="cost shifting to the Member State")

# ---------------- CASE_05 — 32022R2065 Art 37 + 42(4) ----------------
E = "32022R2065:"
ev("P05_AUD", E + "A37(1)", "Providers of very large online platforms and of very large online search engines shall be subject, at their own expense and at least once a year, to independent audits to assess compliance with the following:",
   actor="NOT_SPECIFIED (passive: 'shall be subject … to independent audits')", action="shall be subject to independent audits to assess compliance", obj="compliance with Chapter III obligations and code/crisis-protocol commitments (points (a)-(b))",
   inter="organisations carrying out the audits (named in 37(2)-(3))", target="Providers of very large online platforms and of very large online search engines", role="ACTOR",
   effect="audit at the providers' own expense; at least once a year", fn="auditing", mech="Assurance", basis="INFERENTIAL",
   rationale="Audit agent unnamed in 37(1); identified as 'organisations carrying out the audits' in 37(2)-(3). Purpose = assess compliance (assurance); identified as audit (auditing).", conf="MEDIUM")
ev("P05_AUD", E + "A37(2)", "Providers of very large online platforms and of very large online search engines shall afford the organisations carrying out the audits", "by answering oral or written questions.",
   actor="Providers of very large online platforms and of very large online search engines", action="shall afford cooperation and assistance; give access; answer questions",
   addressee="the organisations carrying out the audits", obj="cooperation, access to data and premises, answers", inter="the organisations carrying out the audits", target="Providers of VLOPs/VLOSEs", role="ADDRESSEE",
   rationale="Target→intermediary access and information duty.")
ev("P05_AUD", E + "A37(2)", "They shall refrain from hampering, unduly influencing or undermining the performance of the audit.", actor="Providers of VLOPs/VLOSEs", action="shall refrain from hampering, unduly influencing or undermining",
   obj="performance of the audit", inter="auditors", target="Providers of VLOPs/VLOSEs", role="OBJECT", modality="PROHIBITION")
ev("P05_AUD", E + "A37(2)", "Such audits shall ensure an adequate level of confidentiality and professional secrecy", "including after the termination of the audits.", actor="Such audits (the auditing organisations, inferred)",
   action="shall ensure confidentiality and professional secrecy", obj="information obtained from providers and third parties", inter="auditing organisations", role="ACTOR", basis="INFERENTIAL",
   rationale="Requirement on the intermediary (Confidentiality obligation, REV ¶85).", conf="MEDIUM")
ev("P05_AUD", E + "A37(2)", "Where necessary for the purpose of the transparency reporting pursuant to Article 42(4), the audit report and the audit implementation report referred to in paragraphs 4 and 6 of this Article shall be accompanied with versions that do not contain any information that could reasonably be considered to be confidential.",
   action="shall be accompanied with non-confidential versions", obj="audit report and audit implementation report", inter="auditing organisations (report author, implicit)", role="OBJECT",
   trigger="Where necessary for the purpose of the transparency reporting pursuant to Article 42(4)", basis="INFERENTIAL", rationale="Actor not specified (passive).", conf="MEDIUM")
ev("P05_AUD", E + "A37(3)", "3. Audits performed pursuant to paragraph 1 shall be performed by organisations which:", actor=NS, action="shall be performed by organisations which [meet conditions (a)-(c)]",
   obj="independence, no conflicts of interest, expertise, objectivity and professional ethics", inter="organisations", role="OBJECT", modality="DEFINITION_OR_STATUS",
   effect="eligibility conditions for audit organisations", rationale="Eligibility requirements on the intermediary; no approval or selection procedure by an authority is stated (selection left to the provider).")
ev("P05_AUD", E + "A37(4)", "Providers of very large online platforms and of very large online search engines shall ensure that the organisations that perform the audits establish an audit report for each audit.",
   actor="Providers of very large online platforms and of very large online search engines", action="shall ensure", addressee="the organisations that perform the audits", obj="establishment of an audit report for each audit",
   inter="the organisations that perform the audits", target="Providers of VLOPs/VLOSEs", role="ADDRESSEE", rationale="The duty to ensure the report exists is placed on the audited target.")
ev("P05_AUD", E + "A37(4)", "the organisations that perform the audits establish an audit report for each audit", actor="the organisations that perform the audits", action="establish an audit report",
   obj="audit report", inter="the organisations that perform the audits", target="Providers of VLOPs/VLOSEs", modality="OBLIGATION", fn="auditing", mech="Assurance",
   rationale="Report-writing by the intermediary; the obligation is formally addressed to the provider ('shall ensure').", conf="MEDIUM")
ev("P05_AUD", E + "A37(4)", "an audit opinion on whether the provider of the very large online platform or of the very large online search engine subject to the audit complied with the obligations and with the commitments referred to in paragraph 1, namely ‘positive’, ‘positive with comments’ or ‘negative’;",
   actor="audit organisation (report author, inferred)", action="[states] an audit opinion", obj="compliance of the provider with obligations and commitments", inter="audit organisation", target="the provider ... subject to the audit",
   modality="OBLIGATION", fn="assurance", mech="Assurance", basis="INFERENTIAL", rationale="Formal attestation of compliance (positive / with comments / negative) = assurance.", conf="HIGH")
ev("P05_AUD", E + "A37(4)", "where the audit opinion is not ‘positive’, operational recommendations on specific measures to achieve compliance and the recommended timeframe to achieve compliance.",
   actor="audit organisation (report author, inferred)", action="[includes] operational recommendations", addressee="the provider", obj="specific measures and timeframe to achieve compliance", inter="audit organisation",
   target="the provider", trigger="where the audit opinion is not ‘positive’", fn="auditing", mech="Assurance", basis="INFERENTIAL",
   rationale="Recommendations are part of the audit report; internal_compliance is a defensible alternative (support for implementation of requirements).", conf="LOW")
ev("P05_AUD", E + "A37(5)", "Where the organisation performing the audit was unable to audit certain specific elements or to express an audit opinion based on its investigations", "could not be audited.",
   actor="the organisation performing the audit (report author)", action="[report shall include] explanation", obj="circumstances and reasons why elements could not be audited", inter="the organisation performing the audit",
   trigger="Where the organisation performing the audit was unable to audit certain specific elements or to express an audit opinion", fn="auditing", mech="Assurance", basis="INFERENTIAL", conf="MEDIUM")
ev("P05_AUD", E + "A37(6)", "Providers of very large online platforms or of very large online search engines receiving an audit report that is not ‘positive’ shall take due account of the operational recommendations addressed to them",
   actor="audit organisation (inferred: report delivered to the provider)", action="[delivers] audit report", addressee="Providers of VLOPs/VLOSEs", obj="audit report", inter="audit organisation", target="Providers of VLOPs/VLOSEs",
   fn="auditing", mech="Assurance", basis="INFERENTIAL", rationale="'receiving an audit report' presupposes delivery to the provider; the act never states delivery by the auditor to a public authority.", conf="MEDIUM")
ev("P05_AUD", E + "A37(6)", "They shall, within one month from receiving those recommendations, adopt an audit implementation report setting out those measures.", actor="Providers of VLOPs/VLOSEs", action="shall adopt",
   obj="audit implementation report", inter="audit organisation (source of the recommendations)", target="Providers of VLOPs/VLOSEs", role="OBJECT",
   trigger="receiving an audit report that is not ‘positive’; within one month", effect="duty to justify non-implementation and alternative measures (next sentence)",
   rationale="Conditional follow-up duty of the target triggered by the intermediary's negative/qualified opinion.")
ev("P05_AUD", E + "A37(7)", "The Commission is empowered to adopt delegated acts in accordance with Article 87 to supplement this Regulation by laying down the necessary rules for the performance of the audits pursuant to this Article",
   actor="The Commission", action="is empowered to adopt delegated acts", obj="rules on procedural steps, methodologies and reporting templates for the audits", reg="Commission", inter="auditing organisations", role="OBJECT",
   modality="PERMISSION", rationale="Regulator sets rules for the intermediary's procedure.")
ev("P05_AUD", E + "A42(4)", "Providers of very large online platforms or of very large online search engines shall transmit to the Digital Services Coordinator of establishment and the Commission, without undue delay upon completion",
   actor="Providers of VLOPs/VLOSEs", action="shall transmit", addressee="the Digital Services Coordinator of establishment and the Commission", obj="audit report (Art 37(4)) and audit implementation report (Art 37(6)), with risk-assessment and mitigation reports",
   reg="Digital Services Coordinator of establishment; Commission", inter="audit organisation (author of the audit report)", target="Providers of VLOPs/VLOSEs", role="OBJECT", trigger="without undue delay upon completion",
   rationale="The intermediary's output reaches the regulators through the target: R ← T ← I. No direct auditor→regulator edge exists in the text.")
ev("P05_AUD", E + "A42(4)", "make publicly available at the latest three months after the receipt of each audit report pursuant to Article 37(4)", actor="Providers of VLOPs/VLOSEs", action="shall make publicly available",
   addressee="public", obj="the documents listed in points (a)-(e), including the audit report", inter="audit organisation (author)", target="Providers of VLOPs/VLOSEs", role="OBJECT",
   trigger="at the latest three months after the receipt of each audit report")

# ---------------- CASE_06 — 32022R2065 Art 22 ----------------
ev("P06_TF", E + "A22(1)", "Providers of online platforms shall take the necessary technical and organisational measures to ensure that notices submitted by trusted flaggers", "are given priority and are processed and decided upon without undue delay.",
   actor="Providers of online platforms", action="shall take measures to ensure priority processing", obj="notices submitted by trusted flaggers", inter="trusted flaggers", target="Providers of online platforms", role="BENEFICIARY",
   trigger="acting within their designated area of expertise", effect="priority treatment of trusted flaggers' notices", rationale="Obligation on the target; the intermediary is the beneficiary of the priority rule.")
ev("P06_TF", E + "A22(1)", "notices submitted by trusted flaggers, acting within their designated area of expertise, through the mechanisms referred to in Article 16", actor="trusted flaggers", action="submit notices",
   addressee="Providers of online platforms (via the Article 16 notice mechanisms)", obj="notices of allegedly illegal content", inter="trusted flaggers", target="Providers of online platforms", modality="OTHER",
   trigger="acting within their designated area of expertise", fn="monitoring", mech="Monitoring", basis="INFERENTIAL",
   rationale="Submitting notices is presupposed (participial clause), not imposed. Detecting and notifying illegal content (cf. 22(2)(a)) = tracking risks/conduct → monitoring; the core activity is transmission of information to the target. REV has no 'reporting/flagging' function (calibration item).", conf="LOW")
ev("P06_TF", E + "A22(2)", "The status of ‘trusted flagger’ under this Regulation shall be awarded, upon application by any entity, by the Digital Services Coordinator of the Member State in which the applicant is established",
   actor="the Digital Services Coordinator of the Member State in which the applicant is established", action="shall award", addressee="the applicant entity", obj="status of ‘trusted flagger’",
   reg="Digital Services Coordinator", inter="trusted flagger (applicant)", role="OBJECT", trigger="upon application by any entity; applicant has demonstrated conditions (a)-(c)",
   effect="acquisition of trusted flagger status", rationale="Recognition by a public authority after demonstration of conditions = vetting.")
ev("P06_TF", E + "A22(2)", "it has particular expertise and competence for the purposes of detecting, identifying and notifying illegal content;", actor="applicant", action="has [demonstrated] expertise and competence",
   obj="detecting, identifying and notifying illegal content", inter="trusted flagger", role="OBJECT", modality="DEFINITION_OR_STATUS", effect="condition for the status",
   rationale="Condition of recognition; also states the activity profile (detect, identify, notify).")
ev("P06_TF", E + "A22(3)", "Trusted flaggers shall publish, at least once a year easily comprehensible and detailed reports on notices submitted in accordance with Article 16 during the relevant period.",
   actor="Trusted flaggers", action="shall publish", addressee="public", obj="reports on notices (by provider, type of content, action taken by the provider)", inter="Trusted flaggers", target="providers of hosting services (identity listed)",
   trigger="at least once a year", rationale="Transparency/reporting obligation on the intermediary (REV ¶85: transparency_disclosure / reporting).")
ev("P06_TF", E + "A22(3)", "Trusted flaggers shall send those reports to the awarding Digital Services Coordinator, and shall make them publicly available.", actor="Trusted flaggers", action="shall send",
   addressee="the awarding Digital Services Coordinator", obj="reports on notices, including the action taken by providers", reg="awarding Digital Services Coordinator", inter="Trusted flaggers",
   target="providers of hosting services (whose actions are reported)", fn="monitoring", mech="Monitoring",
   rationale="Transmission to the oversight body of information that includes the targets' responses. Under the unrevised definition this is monitoring ('…transmitting information to an oversight body'); under REV it is primarily a reporting/notification obligation. Kept as a calibration item.", conf="LOW")
ev("P06_TF", E + "A22(4)", "Digital Services Coordinators shall communicate to the Commission and the Board the names, addresses and email addresses of the entities to which they have awarded the status of the trusted flagger",
   actor="Digital Services Coordinators", action="shall communicate", addressee="the Commission and the Board", obj="identity of entities awarded (or suspended/revoked) trusted flagger status",
   reg="Digital Services Coordinators; Commission; Board", inter="trusted flaggers", role="OBJECT")
ev("P06_TF", E + "A22(5)", "The Commission shall publish the information referred to in paragraph 4 in a publicly available database", "shall keep the database up to date.", actor="The Commission",
   action="shall publish and keep up to date", addressee="public", obj="database of trusted flaggers", reg="Commission", inter="trusted flaggers", role="OBJECT")
ev("P06_TF", E + "A22(6)", "it shall communicate that information to the Digital Services Coordinator that awarded the status of trusted flagger to the entity concerned, providing the necessary explanations and supporting documents.",
   actor="provider of online platforms", action="shall communicate", addressee="the Digital Services Coordinator that awarded the status", obj="information on insufficiently precise, inaccurate or inadequately substantiated notices",
   reg="awarding Digital Services Coordinator", inter="the entity concerned (trusted flagger)", target="provider of online platforms", role="OBJECT",
   trigger="Where a provider of online platforms has information indicating that a trusted flagger has submitted a significant number of insufficiently precise, inaccurate or inadequately substantiated notices",
   rationale="Target reports on the intermediary to the regulator: the intermediary is the object of oversight.")
ev("P06_TF", E + "A22(6)", "the status of trusted flagger shall be suspended during the period of the investigation", actor="NOT_SPECIFIED (passive)", action="shall be suspended", obj="trusted flagger status",
   reg="Digital Services Coordinator (forms the triggering view)", inter="trusted flagger", role="OBJECT",
   trigger="Upon receiving the information from the provider of online platforms, and if the Digital Services Coordinator considers that there are legitimate reasons to open an investigation",
   effect="suspension of status during investigation", rationale="Legal effect; the suspending actor is not named.")
ev("P06_TF", E + "A22(7)", "The Digital Services Coordinator that awarded the status of trusted flagger to an entity shall revoke that status if it determines", "no longer meets the conditions set out in paragraph 2.",
   actor="The Digital Services Coordinator that awarded the status", action="shall revoke", obj="trusted flagger status", reg="awarding Digital Services Coordinator", inter="the entity", role="OBJECT",
   trigger="if it determines, following an investigation ..., that the entity no longer meets the conditions set out in paragraph 2", effect="revocation of status")
ev("P06_TF", E + "A22(7)", "Before revoking that status, the Digital Services Coordinator shall afford the entity an opportunity to react to the findings of its investigation and its intention to revoke the entity’s status as trusted flagger.",
   actor="the Digital Services Coordinator", action="shall afford an opportunity to react", addressee="the entity", obj="findings and intended revocation", reg="Digital Services Coordinator",
   inter="the entity", role="ADDRESSEE", trigger="Before revoking that status")
ev("P06_TF", E + "A22(8)", "The Commission, after consulting the Board, shall, where necessary, issue guidelines to assist providers of online platforms and Digital Services Coordinators in the application of paragraphs 2, 6 and 7.",
   actor="The Commission", action="shall issue guidelines (where necessary)", addressee="providers of online platforms and Digital Services Coordinators", obj="application of paragraphs 2, 6 and 7",
   reg="Commission; Board", inter="trusted flaggers", target="providers of online platforms", role="OBJECT", trigger="where necessary; after consulting the Board")

# ---------------- PARENTS (INTERPRETIVE_APPLICATION of the revised codebook) ----------------
FN = ["F_CODE_CREATION", "F_ASSURANCE", "F_MONITORING", "F_REGISTRY_ADMINISTRATION", "F_INTERNAL_COMPLIANCE", "F_DISPUTE_RESOLUTION", "F_COMPLAINT_HANDLING", "F_AUDITING", "F_INSURANCE_RISK_UNDERWRITING", "F_ENFORCEMENT"]


def flags(*yes):
    return {f: ("Yes" if f in yes else "No") for f in FN}


P = [
 dict(PARENT_ID="P01_AUD", CASE_ID="CASE_01", ACT_ID="32004R0874", INTERMEDIARY_NAME="Independent auditor (phased registration audit)", INTERMEDIARY_QUALIFIES="YES",
      QUALIFICATION_RATIONALE="A12(5) assigns an independent audit of the Registry's administration of phased registration and reporting of findings to the Commission.", RELEVANT_PROVISIONS="32004R0874:A12(5)",
      INTERMEDIARY_INVOLVEMENT="Required", ORIENTATION="bidirectional", REGULATOR_CONTEXT="EU_public", TARGET_CONTEXT="service_provider", **flags("F_ASSURANCE", "F_AUDITING"), MECHANISM_FAMILY="Assurance",
      RECOGNITION_PATHWAY="Designation", FUNCTION_DESCRIPTION="Audits the Registry's operational and technical administration of phased registration and reports findings to the Commission.",
      IDENTIFICATION_BASIS_TEST="DIRECT_ASSIGNMENT"),
 dict(PARENT_ID="P01_VAL", CASE_ID="CASE_01", ACT_ID="32004R0874", INTERMEDIARY_NAME="Validation agents", INTERMEDIARY_QUALIFIES="YES",
      QUALIFICATION_RATIONALE="A14 assigns examination of documentary evidence of prior rights and notification of the result to the Registry; A13 governs selection.", RELEVANT_PROVISIONS="32004R0874:A13; 32004R0874:A14",
      INTERMEDIARY_INVOLVEMENT="Required", ORIENTATION="bidirectional", REGULATOR_CONTEXT="hybrid_public_private; national_public", TARGET_CONTEXT="individual; public_body", **flags("F_ASSURANCE"),
      MECHANISM_FAMILY="Assurance", RECOGNITION_PATHWAY="Designation", FUNCTION_DESCRIPTION="Verify whether domain-name applicants hold the claimed prior rights and notify the Registry of positive or negative findings.",
      IDENTIFICATION_BASIS_TEST="DIRECT_ASSIGNMENT; LEGAL_RECOGNITION"),
 dict(PARENT_ID="P01_ADR", CASE_ID="CASE_01", ACT_ID="32004R0874", INTERMEDIARY_NAME="ADR providers", INTERMEDIARY_QUALIFIES="YES",
      QUALIFICATION_RATIONALE="A22(5)-(7) and A23(1): providers receive and examine complaints, forward them, inform the Registry; selected by the Registry.", RELEVANT_PROVISIONS="32004R0874:A22(5); 32004R0874:A22(6); 32004R0874:A22(7); 32004R0874:A23(1)",
      INTERMEDIARY_INVOLVEMENT="Conditional", ORIENTATION="bidirectional", REGULATOR_CONTEXT="hybrid_public_private", TARGET_CONTEXT="individual", **flags("F_DISPUTE_RESOLUTION", "F_COMPLAINT_HANDLING"),
      MECHANISM_FAMILY="Dispute resolution", RECOGNITION_PATHWAY="Designation", FUNCTION_DESCRIPTION="Receive, examine and forward complaints on domain names, inform the Registry, and administer the ADR procedure.",
      IDENTIFICATION_BASIS_TEST="DIRECT_ASSIGNMENT; LEGAL_RECOGNITION"),
 dict(PARENT_ID="P02_CB", CASE_ID="CASE_02", ACT_ID="31989L0336", INTERMEDIARY_NAME="Competent bodies", INTERMEDIARY_QUALIFIES="YES",
      QUALIFICATION_RATIONALE="A10(2) requires the technical construction file to include a technical report or certificate obtained from a competent body (reliance on a named third-party assurance provider).", RELEVANT_PROVISIONS="31989L0336:A10(2)",
      INTERMEDIARY_INVOLVEMENT="Conditional", ORIENTATION="target-facing", REGULATOR_CONTEXT="national_public", TARGET_CONTEXT="product_economic_operator", **flags("F_ASSURANCE"), MECHANISM_FAMILY="Assurance",
      RECOGNITION_PATHWAY="None", FUNCTION_DESCRIPTION="Provide technical reports or certificates for manufacturers' technical construction files where standards were not (fully) applied.",
      IDENTIFICATION_BASIS_TEST="STRUCTURAL_RELIANCE; DIRECT_ASSIGNMENT"),
 dict(PARENT_ID="P02_NB", CASE_ID="CASE_02", ACT_ID="31989L0336", INTERMEDIARY_NAME="Notified bodies", INTERMEDIARY_QUALIFIES="YES",
      QUALIFICATION_RATIONALE="A10(4)-(6), Annex II: bodies issue EC type-examination certificates; assessed against Annex II and notified by Member States.", RELEVANT_PROVISIONS="31989L0336:A10(4); 31989L0336:A10(6); 31989L0336:ANNEX_II",
      INTERMEDIARY_INVOLVEMENT="Conditional", ORIENTATION="target-facing", REGULATOR_CONTEXT="national_public; EU_public", TARGET_CONTEXT="product_economic_operator", **flags("F_ASSURANCE"), MECHANISM_FAMILY="Assurance",
      RECOGNITION_PATHWAY="Vetting", FUNCTION_DESCRIPTION="Issue EC type-examination certificates for specified apparatus.", IDENTIFICATION_BASIS_TEST="LEGAL_RECOGNITION; DIRECT_ASSIGNMENT"),
 dict(PARENT_ID="P02_INS", CASE_ID="CASE_02", ACT_ID="31989L0336", INTERMEDIARY_NAME="Insurance providers (civil liability insurance)", INTERMEDIARY_QUALIFIES="YES",
      QUALIFICATION_RATIONALE="Applying REV ¶28 literally: Annex II point 5 requires designated bodies to possess civil liability insurance, which necessarily relies on an insurance provider although none is named. No action or function is assigned to the insurer in the text (see child layer).",
      RELEVANT_PROVISIONS="31989L0336:ANNEX_II", INTERMEDIARY_INVOLVEMENT="Conditional", ORIENTATION="intermediary-facing", REGULATOR_CONTEXT="national_public", TARGET_CONTEXT="regulatory_intermediary",
      **flags("F_INSURANCE_RISK_UNDERWRITING"), MECHANISM_FAMILY="Insurance / risk underwriting", RECOGNITION_PATHWAY="None",
      FUNCTION_DESCRIPTION="Provide the civil liability cover that notified bodies must possess, unless liability is covered by the State.", IDENTIFICATION_BASIS_TEST="STRUCTURAL_RELIANCE"),
 dict(PARENT_ID="P03_NB", CASE_ID="CASE_03", ACT_ID="31991L0263", INTERMEDIARY_NAME="Notified bodies", INTERMEDIARY_QUALIFIES="YES",
      QUALIFICATION_RATIONALE="A10(1),(4); Annex III 3.1-4.4; Annex V(6): designated bodies assess quality systems, carry out surveillance and periodic audits; apply designation criteria to laboratories.",
      RELEVANT_PROVISIONS="31991L0263:A10(1); 31991L0263:A10(2); 31991L0263:A10(4); 31991L0263:ANNEX_III(3.1); 31991L0263:ANNEX_III(3.3); 31991L0263:ANNEX_III(3.4); 31991L0263:ANNEX_III(4); 31991L0263:ANNEX_V(6)",
      INTERMEDIARY_INVOLVEMENT="Required", ORIENTATION="target-facing; intermediary-facing", REGULATOR_CONTEXT="national_public; EU_public", TARGET_CONTEXT="product_economic_operator; regulatory_intermediary",
      **flags("F_ASSURANCE", "F_MONITORING", "F_AUDITING"), MECHANISM_FAMILY="Assurance; Monitoring", RECOGNITION_PATHWAY="Vetting",
      FUNCTION_DESCRIPTION="Assess and approve manufacturers' quality systems, evaluate modifications, carry out surveillance, periodic audits and unannounced visits; apply designation criteria to test laboratories.",
      IDENTIFICATION_BASIS_TEST="LEGAL_RECOGNITION; DIRECT_ASSIGNMENT"),
 dict(PARENT_ID="P03_TL", CASE_ID="CASE_03", ACT_ID="31991L0263", INTERMEDIARY_NAME="Test laboratories", INTERMEDIARY_QUALIFIES="YES",
      QUALIFICATION_RATIONALE="A10(2): laboratories designated by Member States for carrying out tests pertaining to the conformity procedures; designation subject to criteria applied by notified bodies.", RELEVANT_PROVISIONS="31991L0263:A10(2); 31991L0263:A10(4)",
      INTERMEDIARY_INVOLVEMENT="Not specified", ORIENTATION="target-facing", REGULATOR_CONTEXT="national_public", TARGET_CONTEXT="product_economic_operator", **flags("F_ASSURANCE"), MECHANISM_FAMILY="Assurance",
      RECOGNITION_PATHWAY="Designation", FUNCTION_DESCRIPTION="Carry out tests pertaining to the conformity procedures for which they are designated.", IDENTIFICATION_BASIS_TEST="LEGAL_RECOGNITION"),
 dict(PARENT_ID="P03_INS", CASE_ID="CASE_03", ACT_ID="31991L0263", INTERMEDIARY_NAME="Insurance providers (liability insurance)", INTERMEDIARY_QUALIFIES="YES",
      QUALIFICATION_RATIONALE="Applying REV ¶28 literally to Annex V point 6 (notified body must take out liability insurance); insurer not named and assigned no action.", RELEVANT_PROVISIONS="31991L0263:ANNEX_V(6)",
      INTERMEDIARY_INVOLVEMENT="Conditional", ORIENTATION="intermediary-facing", REGULATOR_CONTEXT="national_public", TARGET_CONTEXT="regulatory_intermediary", **flags("F_INSURANCE_RISK_UNDERWRITING"),
      MECHANISM_FAMILY="Insurance / risk underwriting", RECOGNITION_PATHWAY="None", FUNCTION_DESCRIPTION="Provide liability cover to notified bodies unless liability is assumed by the State.", IDENTIFICATION_BASIS_TEST="STRUCTURAL_RELIANCE"),
 dict(PARENT_ID="P04_LAB", CASE_ID="CASE_04", ACT_ID="31986L0361", INTERMEDIARY_NAME="Approved testing laboratories", INTERMEDIARY_QUALIFIES="YES",
      QUALIFICATION_RATIONALE="A2(8), A7(2)-(3), A8(3): accredited/approved laboratories issue certificates of conformity with test data and give opinions when consulted by the Commission in disputes.", RELEVANT_PROVISIONS="31986L0361:A2(8); 31986L0361:A7(2); 31986L0361:A7(3); 31986L0361:A8(3)",
      INTERMEDIARY_INVOLVEMENT="Required; Conditional", ORIENTATION="bidirectional", REGULATOR_CONTEXT="national_public; EU_public", TARGET_CONTEXT="product_economic_operator; public_body", **flags("F_ASSURANCE"),
      MECHANISM_FAMILY="Assurance", RECOGNITION_PATHWAY="Vetting", FUNCTION_DESCRIPTION="Carry out conformity tests and issue certificates with measurement data; when consulted under Article 8(3), give an opinion on a disputed suspension.",
      IDENTIFICATION_BASIS_TEST="LEGAL_RECOGNITION; DIRECT_ASSIGNMENT"),
 dict(PARENT_ID="P05_AUD", CASE_ID="CASE_05", ACT_ID="32022R2065", INTERMEDIARY_NAME="Organisations performing independent audits", INTERMEDIARY_QUALIFIES="YES",
      QUALIFICATION_RATIONALE="A37(1)-(5): independent organisations audit VLOP/VLOSE compliance and establish an audit report with an audit opinion and recommendations.", RELEVANT_PROVISIONS="32022R2065:A37(1); 32022R2065:A37(2); 32022R2065:A37(3); 32022R2065:A37(4); 32022R2065:A37(5); 32022R2065:A37(6); 32022R2065:A37(7); 32022R2065:A42(4)",
      INTERMEDIARY_INVOLVEMENT="Required", ORIENTATION="target-facing", REGULATOR_CONTEXT="EU_public; national_public", TARGET_CONTEXT="platform_provider; service_provider", **flags("F_ASSURANCE", "F_AUDITING"),
      MECHANISM_FAMILY="Assurance", RECOGNITION_PATHWAY="None", FUNCTION_DESCRIPTION="Audit VLOP/VLOSE compliance at least annually and issue an audit report with an opinion and, where not positive, operational recommendations.",
      IDENTIFICATION_BASIS_TEST="DIRECT_ASSIGNMENT"),
 dict(PARENT_ID="P06_TF", CASE_ID="CASE_06", ACT_ID="32022R2065", INTERMEDIARY_NAME="Trusted flaggers", INTERMEDIARY_QUALIFIES="YES",
      QUALIFICATION_RATIONALE="A22: entities with recognised expertise in detecting, identifying and notifying illegal content, whose notices platforms must prioritise; status awarded and revocable by the DSC; reporting duties to the DSC.",
      RELEVANT_PROVISIONS="32022R2065:A22(1); 32022R2065:A22(2); 32022R2065:A22(3); 32022R2065:A22(4); 32022R2065:A22(5); 32022R2065:A22(6); 32022R2065:A22(7); 32022R2065:A22(8)",
      INTERMEDIARY_INVOLVEMENT="Optional", ORIENTATION="bidirectional", REGULATOR_CONTEXT="national_public; EU_public", TARGET_CONTEXT="platform_provider", **flags("F_MONITORING"), MECHANISM_FAMILY="Monitoring",
      RECOGNITION_PATHWAY="Vetting", FUNCTION_DESCRIPTION="Detect and notify illegal content to online platforms (priority notices) and report annually on notices to the awarding DSC and the public.",
      IDENTIFICATION_BASIS_TEST="LEGAL_RECOGNITION"),
]
for p in P:
    p["PASS_ID"] = "FIRST_PASS"

PH = ["PARENT_ID", "CASE_ID", "ACT_ID", "INTERMEDIARY_NAME", "INTERMEDIARY_QUALIFIES", "QUALIFICATION_RATIONALE", "RELEVANT_PROVISIONS", "INTERMEDIARY_INVOLVEMENT", "ORIENTATION", "REGULATOR_CONTEXT",
      "TARGET_CONTEXT"] + FN + ["MECHANISM_FAMILY", "RECOGNITION_PATHWAY", "FUNCTION_DESCRIPTION", "IDENTIFICATION_BASIS_TEST", "PASS_ID"]
CH = ["EVENT_ID", "PARENT_ID", "SOURCE_PROVISION_ID", "TEXT_SPAN", "ACTOR", "ACTION", "ACTION_ADDRESSEE", "OBJECT", "REGULATOR_ACTOR", "INTERMEDIARY_ACTOR", "TARGET_ACTOR",
      "INTERMEDIARY_ROLE_IN_EVENT", "NORMATIVE_MODALITY", "TRIGGER_CONDITION", "LEGAL_EFFECT", "FUNCTION_CODE", "MECHANISM_CODE", "INFERENCE_BASIS", "RATIONALE", "CONFIDENCE", "REVIEW_STATUS"]
OUT = RUN_ROOT / "08_DUAL_CODING/first_pass"
write_csv(OUT / "PARENT_FIRST_PASS.csv", PH, P)
write_csv(OUT / "CHILD_FIRST_PASS.csv", CH, EV)
from collections import Counter  # noqa: E402
print(len(P), "parents;", len(EV), "events;", Counter(e["PARENT_ID"] for e in EV))
