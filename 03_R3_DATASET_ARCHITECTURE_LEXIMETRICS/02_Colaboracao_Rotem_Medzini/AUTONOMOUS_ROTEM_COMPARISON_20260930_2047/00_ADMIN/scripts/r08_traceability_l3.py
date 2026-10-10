"""R08/E4 — Traceability test of Rotem's implemented (L3) codes for the selected cases.

For each coded value: documentary anchor in L3, attribution to one intermediary, supporting provision located by this run
in the official text, inferential reconstruction judgment (MODEL_REVIEWED by the executing agent), result class.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from common import RUN_ROOT, write_csv  # noqa: E402

H = ["TRACE_ID", "CASE_ID", "PARENT_IDS", "CODED_VALUE (Rotem L3, verbatim)", "L3_SOURCE", "DOCUMENTARY_ANCHOR_IN_L3", "ATTRIBUTABLE_TO_ONE_INTERMEDIARY_IN_L3",
     "SUPPORTING_PROVISION_FOUND_BY_THIS_RUN (official text)", "INFERENTIAL_RECONSTRUCTION", "RESULT_CLASS", "NOTE"]
R = [
    ("T01", "CASE_01", "P01_*", "Function_assurance = Yes", "CDI row 75", "Relevant provision(s) empty; narrative names Articles 12, 13, 15 inline",
     "NO (row covers 5 intermediaries); narrative: 'validation agents assessed prior-right claims'", "32004R0874:A14 (examination of prior rights)", "YES via narrative + A14",
     "RECONSTRUCTABLE_VIA_NARRATIVE", "Flag attributable only through prose"),
    ("T02", "CASE_01", "P01_*", "Function_auditing = Yes", "CDI row 75", "narrative '(Article 12)'",
     "NO (row-level); narrative: 'an independent auditor reviewed the phased registration process'", "32004R0874:A12(5)", "YES", "RECONSTRUCTABLE_VIA_NARRATIVE", ""),
    ("T03", "CASE_01", "P01_*", "Function_dispute_resolution = Yes", "CDI row 75", "narrative (ADR, panels)",
     "NO (row-level); narrative: 'ADR providers adjudicated abusive registrations'", "32004R0874:A22-A23", "YES", "RECONSTRUCTABLE_VIA_NARRATIVE", ""),
    ("T04", "CASE_01", "P01_*", "Recongnition_pathways = Designation (one value for 5 intermediaries)", "CDI row 75",
     "narrative: Registry accredits registrars; selects validation agents and ADR providers; appoints auditor after consulting the Commission; contracts escrow agent subject to Commission consent", "NO",
     "A4 (accreditation of registrars); A12(5) (appointment); A13 (selection); A15(1) (escrow contract + Commission consent); A23(1) (may select)",
     "PARTIAL: 'Designation' fits appointment/selection, but accreditation of registrars is closer to vetting and the escrow agent is contracted; one value cannot carry five pathways",
     "LEVEL_OF_ANALYSIS_DIFFERENCE (resolved by REV INTERMEDIARY_MAP rows)", "The recognising actor is a private non-profit Registry, whereas the Chart Key defines designation as 'by a public authority'"),
    ("T05", "CASE_01", "P01_*", "Obligation_intensity = Strong", "CDI row 75", "narrative lists requirements (objectivity, expertise, panellist independence)", "NO", "A13, A23",
     "NOT_RECONSTRUCTABLE per intermediary", "LEVEL_OF_ANALYSIS_DIFFERENCE", "Which intermediary bears 'strong' obligations is not stated"),
    ("T06", "CASE_02", "P02_*", "Function_assurance = Yes", "CDI row 14", "no article references", "NO; narrative attributes reports/certificates to competent and notified bodies",
     "31989L0336:A10(2), A10(4)-(5)", "YES", "RECONSTRUCTABLE_VIA_NARRATIVE", ""),
    ("T07", "CASE_02", "P02_INS", "Function_Insurance / risk underwriting = Yes; recognition 'insurance companies: None'", "CDI row 14",
     "narrative: 'Insurance companies provide the required civil-liability coverage, unless liability is assumed by the State'", "YES via narrative (per-actor strings)",
     "31989L0336:ANNEX_II point 5", "YES: the description states the reliance, as Rotem's e-mail says", "RECONSTRUCTABLE_VIA_NARRATIVE (Rotem's claim confirmed)",
     "The identification basis (structural reliance) is recoverable from prose, not from a field"),
    ("T08", "CASE_02", "P02_CB", "Recognition 'Competent and notified bodies: Vetting'", "CDI row 14", "narrative: 'Competent and notified bodies must possess adequate personnel …'", "YES (per-actor string)",
     "31989L0336 Art 2(5): 'competent body' means any body which meets the criteria listed in Annex II and is recognized as such; Annex II",
     "YES, but only from Art 2(5), which was NOT in this run's provision pack", "RECONSTRUCTABLE (full act); our first pass coded 'None' from an incomplete pack",
     "Adversarial finding: omitting a provision from the window caused a false negative on our side (I-022)"),
    ("T09", "CASE_03", "P03_NB", "Function_auditing = No", "CDI row 19",
     "narrative itself: 'Notified bodies conduct … quality-system audits'; self-regulation narrative: 'The notified body will also carry out audits at reasonable intervals'", "NO (row-level)",
     "31991L0263:ANNEX_III(4) point 4.3 'shall carry out audits at reasonable intervals … audit report'",
     "NOT_RECONSTRUCTABLE: description and flag point in opposite directions; under both the UNREV ('systematic and, where applicable, periodic examination') and REV ('identified or structured as an audit') definitions the text supports Yes",
     "SEMANTIC_AMBIGUITY (description–flag inconsistency)", "Calibration question: is a periodic audit within surveillance coded as monitoring rather than auditing?"),
    ("T10", "CASE_03", "P03_NB", "Function_enforcement = Yes", "CDI row 19", "self-regulation narrative: 'the notified body will withdraw if it is established that the equipment does not conform …'",
     "NO (row-level)", "31991L0263 Art 12: '… the notified body shall withdraw the EC type-examination certificate … or the EC quality system approval decision …'",
     "YES via narrative + Art 12 (Art 12 not in this run's pack)", "RECONSTRUCTABLE_VIA_NARRATIVE (Rotem supported); our first pass 'No' = pack-window false negative", "I-022"),
    ("T11", "CASE_03", "P03_*", "Function_monitoring = Yes", "CDI row 19", "narrative: 'product surveillance'", "NO (row-level)", "ANNEX_III(4) (surveillance)", "YES",
     "RECONSTRUCTABLE_VIA_NARRATIVE", ""),
    ("T12", "CASE_04", "P04_LAB", "Recongnition_pathways = Designation", "CDI row 7", "narrative: 'approved by Member States, or by bodies that Member States recognise as competent'",
     "YES (single intermediary)", "31986L0361:A2(8): conformity with the accreditation system verified … and approved",
     "PARTIAL: approval (designation) is reconstructable; the prior verification against an accreditation system (vetting) is dropped",
     "SEMANTIC_AMBIGUITY (staged recognition; REV allows one value and gives no decision rule)", "Our first pass chose Vetting; both readings are supported by the text"),
    ("T13", "CASE_04", "P04_LAB", "Function_assurance = Yes", "CDI row 7", "narrative: 'Assurance'", "YES", "A7(3) (certificate with test data)", "YES", "RECONSTRUCTABLE", ""),
    ("T14", "CASE_05", "P05_AUD", "Primary_function_mechanism = auditing; Recognition None; Recognizer_type regulated_entity", "LoA row 27", "Relevant_articles = '37'",
     "YES (intermediary-level row)", "A37(1)-(6)", "YES (auditing; no approval by an authority; selection on the provider's side implied by the providers' duties)",
     "RECONSTRUCTABLE (row-level article anchor)", ""),
    ("T15", "CASE_05", "P05_AUD", "Position_in_governance_chain = between_regulator_and_target", "LoA row 27", "Relevant_articles = '37' only", "YES",
     "The regulator link exists only through A42(4) (provider transmits the audit report to the DSC and the Commission) and A37(7) (Commission delegated acts); A42 is not in Rotem's article list",
     "PARTIAL: 'between' holds only if Art 42(4) is read in; the text routes the auditor's output R ← T ← I", "EVIDENCE_GAP in the provision list (REV ¶36 requires all provisions needed)",
     "E2 example: the position value hides that the auditor never addresses the regulator"),
    ("T16", "CASE_06", "P06_TF", "Primary_function_mechanism = Reporting; Recognition Vetting; Recognizer national_supervisory_regulator", "LoA row 21", "Relevant_articles = '22'", "YES",
     "A22(1)-(3) (notices; reports to the awarding DSC); A22(2) (award upon demonstrated conditions)", "YES for activity and recognition; 'Reporting' has no REV function label",
     "RECONSTRUCTABLE (activity) / VOCABULARY_GAP (function)", "E5 transmission"),
    ("T17", "CASE_06", "P06_TF", "Position_in_governance_chain = between_regulator_and_target; between_beneficiaries_and_targets", "LoA row 21", "'22'", "YES",
     "Art 22 names no beneficiaries", "PARTIAL: 'beneficiaries' is not anchored in Art 22", "INFERENTIAL (not traceable to the provision list)", ""),
]
write_csv(RUN_ROOT / "08_DUAL_CODING/TRACEABILITY_TEST_ROTEM_L3.csv", H, R)
print(len(R))
