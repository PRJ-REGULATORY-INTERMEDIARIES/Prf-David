# Batch 03 — Chapter IV, Sections 1–3 (Articles 24–36).
CTRL, PROC, DS, SA = "controller", "processor", "data subject", "supervisory authority"
def rt(u, origin, cp, rtype, obj, fn, mod, cond="", note="", deriv="direct", unres="", flag="", acc="", ext_dep="", dep=""):
    return qr(u, origin, cp, rtype, obj, fn, mod, cond=cond, deriv=deriv, type_note=note, unresolved=unres, flag=flag, acc=acc, ext=ext_dep, dep=dep)

BOARD = pd("European Data Protection Board", "position_type", "A35.P4", ntype="N1 (Art.68(1)) — to be checked at Art.68", note="Referred to in Art.35(4) as 'the Board referred to in Article 68'.")
DPO = pd("data protection officer", "position_type", "A35.P2", ntype="N2-designation (Art.37(1)) — to be checked at Arts 37–39", note="Office specified at type level; instances are designated by controllers/processors.")
JC = pd("joint controllers (category)", "position_type", "A26.P1", note="Two or more controllers jointly determining purposes and means; role arises by fact, 'shall be joint controllers'.")
CODE = pd("approved code of conduct (Art.40)", "device", "A24.P3;A28.P5;A32.P3;A35.P8", note="Scheme regulated in Arts 40–41; device status assessed in Section 5.", flag="DEV-threshold")
CERT = pd("approved certification mechanism (Art.42)", "device", "A24.P3;A25.P3;A28.P5;A32.P3", note="Scheme regulated in Arts 42–43; device status assessed in Section 5.", flag="DEV-threshold")
SCC = pd("standard contractual clauses (Art.28(7)-(8))", "device", "A28.P6;A28.P7;A28.P8", note="Instrument adopted by the Commission or by a supervisory authority; typed characteristic of the controller–processor contract unless a distinct scheme is shown.", flag="DEV-threshold")
CM = pd("consistency mechanism (Art.63)", "device", "A35.P6;A28.P8", note="Procedure among supervisory authorities, the Board and the Commission, regulated in Arts 63–67 (Chapter VII); referenced here.", flag="DEV-threshold")

# Art 24
n = na("A24.P1", CTRL, "implement appropriate technical and organisational measures to ensure and be able to demonstrate that processing complies; review and update them", "compliance measures", "implementation", "obligation", cond="taking into account nature, scope, context, purposes and risks")
screen("A24.P1", "Yes", "operative-assignment", na=[n], status="Extracted", note="Core responsibility of the controller (self-regulatory implementation); demonstration duty without identified forum here.")
n = na("A24.P2", CTRL, "include data protection policies among the measures", "data protection policies", "implementation", "obligation", cond="where proportionate in relation to processing activities")
screen("A24.P2", "Yes", "operative-assignment", na=[n], status="Extracted")
n = na("A24.P3", CTRL, "use adherence to approved codes of conduct (Art.40) or approved certification mechanisms (Art.42) as an element to demonstrate compliance", "demonstration of compliance", "information provision (demonstration)", "permission", cp_status="none", dep="approved code of conduct (Art.40); approved certification mechanism (Art.42)", note="Dependency on devices regulated in Section 5; the permission does not itself identify to whom compliance is demonstrated.")
screen("A24.P3", "Yes", "operative-assignment; device-referencing", na=[n], status="Extracted", note="Link between the controller's demonstration duty and Arts 40/42 (candidate cross-section coupling for S).")

# Art 25
n = na("A25.P1", CTRL, "implement appropriate technical and organisational measures (e.g. pseudonymisation) designed to implement data-protection principles and integrate safeguards, at the time of determining the means and of processing", "data protection by design", "implementation", "obligation", cond="state of the art, cost, nature, scope, context, purposes, risks")
screen("A25.P1", "Yes", "operative-assignment", na=[n], status="Extracted")
n = na("A25.P2", CTRL, "ensure by default that only necessary personal data are processed (amount, extent, storage period, accessibility)", "data protection by default", "implementation", "obligation")
screen("A25.P2", "Yes", "operative-assignment", na=[n], status="Extracted")
n = na("A25.P3", CTRL, "use an approved certification mechanism (Art.42) as an element to demonstrate compliance with Art.25(1)-(2)", "demonstration of compliance", "information provision (demonstration)", "permission", dep="approved certification mechanism (Art.42)")
screen("A25.P3", "Yes", "operative-assignment; device-referencing", na=[n], status="Extracted")

# Art 26 joint controllers
q = [rt("A26.P1", CTRL, "other joint controllers", "contractual/exchange", "arrangement determining respective responsibilities (rights of data subjects; information duties); may designate a contact point for data subjects", "implementation (allocation of responsibilities)", "obligation", cond="unless and in so far as responsibilities are determined by Union or Member State law", note="peer relation among joint controllers by 'arrangement' (typed characteristic; INS-TYPE)")]
screen("A26.P1", "Yes", "relation-bearing", qr=q, pos=[JC], status="Extracted", note="Allocation of responsibilities by arrangement between controllers; fallback to Union/Member State law.")
q = [rt("A26.P2", CTRL, DS, "information/reporting", "essence of the arrangement made available to the data subject; arrangement to reflect roles vis-à-vis data subjects", "information provision", "obligation")]
screen("A26.P2", "Yes", "relation-bearing", qr=q, status="Extracted")
q = [rt("A26.P3", CTRL, DS, "beneficiary/protective", "data subject may exercise rights against each of the joint controllers irrespective of the arrangement", "remediation (rights exercise)", "entitlement", cond="irrespective of the terms of the arrangement", note="makes the arrangement non-binding on the data subject")]
screen("A26.P3", "Yes", "relation-bearing", qr=q, status="Extracted")

# Art 27 representative
n = na("A27.P1", "controller or processor not established in the Union", "designate in writing a representative in the Union", "representative", "authorization/designation", "obligation", cond="Art.3(2) applies", ntype="N2-designation", note="Obligation to designate an office-holder at type level; the representative position is specified in Arts 4(17), 27; the instance arises by the designation, not by the Regulation.", flag="N2-designation")
screen("A27.P1", "Yes", "operative-assignment; position-defining", na=[n], status="Extracted", note="Designation duty (see HQ on N2 vs designation).")
screen("A27.P2", "No", "exception", status="Not applicable", note="Exceptions from the designation duty (occasional processing; public authority or body).")
n = na("A27.P3", "representative", "be established in one of the Member States where the data subjects are", "location of representative", "implementation condition", "obligation", cond="data subjects whose data are processed in relation to the offering of goods/services or monitoring", cp_status="none")
screen("A27.P3", "Yes", "operative-assignment", na=[n], status="Extracted")
q = [rt("A27.P4", CTRL + " or " + PROC, "representative", "delegation/authorization", "mandate to be addressed in addition to or instead of the controller/processor on all issues related to processing", "representation/participation", "obligation", cond="for ensuring compliance", note="gov-direction: controller/processor mandates representative"),
     rt("A27.P4", "representative", SA + " and data subjects (as addressees)", "representation/participation", "being addressed by supervisory authorities and data subjects on all processing issues", "representation", "obligation", note="representative as addressee of SAs and data subjects (counterparts named as 'in particular'; not exhaustive)")]
screen("A27.P4", "Yes", "relation-bearing", qr=q, status="Extracted", note="Representative mediates between non-Union controllers/processors and supervisory authorities/data subjects.")
screen("A27.P5", "No", "limitation", status="Not applicable", note="Designation is without prejudice to legal actions against the controller/processor.")

# Art 28 processor
q = [rt("A28.P1", CTRL, PROC, "verification/assurance", "use only processors providing sufficient guarantees for appropriate measures", "verification/assurance (selection)", "obligation", note="controller verifies sufficiency of guarantees before use; verification means not specified in the unit")]
screen("A28.P1", "Yes", "relation-bearing", qr=q, status="Extracted")
q = [rt("A28.P2", CTRL, PROC, "delegation/authorization", "prior specific or general written authorisation of the controller for engaging another processor; information on intended changes; opportunity to object", "authorization", "obligation", cond="general authorisation: processor informs of intended changes", note="gov-direction: controller authorizes processor's sub-processing")]
screen("A28.P2", "Yes", "relation-bearing", qr=q, status="Extracted")
q = [rt("A28.P3", CTRL, PROC, "delegation/authorization", "processing governed by binding contract or other legal act; processor processes only on documented instructions; confidentiality; security measures; sub-processor conditions; assistance with data-subject rights and with Arts 32–36; deletion/return; information and audits", "implementation (delegated)", "obligation", cond="contract or legal act under Union or Member State law; listed stipulations (a)-(h)", note="instrument: contract/legal act (INS-TYPE); stipulations (a)-(h) inventoried; assistance and audit duties extracted separately", dep=""),
     rt("A28.P3", CTRL + " (or auditor mandated by controller)", PROC, "oversight/supervision", "audits including inspections of the processor; information necessary to demonstrate compliance", "monitoring", "obligation", cond="processor must make information available and allow for and contribute to audits (point h)", note="gov-direction: controller (or mandated auditor) audits processor", acc=""),
     rt("A28.P3", PROC, CTRL, "information/reporting", "immediate notice if an instruction infringes the Regulation; information on legal requirement to process otherwise (point a)", "information provision", "obligation", cond="processor is of the opinion an instruction infringes; or Union/Member State law requires processing and does not prohibit informing")]
screen("A28.P3", "Yes", "relation-bearing", qr=q, status="Extracted", note="Eight stipulations (a)-(h) inventoried at point level; one delegation relation, one oversight (audit) relation, one information relation. Union/Member State law as a legal act source is noted (no position).")
q = [rt("A28.P4", PROC, "other processor (sub-processor)", "delegation/authorization", "same data protection obligations imposed by contract or legal act", "implementation (delegated)", "obligation", note="gov-direction: initial processor imposes obligations on sub-processor"),
     rt("A28.P4", PROC, CTRL, "contractual/exchange", "initial processor remains fully liable to the controller for the sub-processor's performance", "remediation (liability allocation)", "obligation", cond="other processor fails to fulfil its data protection obligations", note="liability relation; not coded as accountability (no forum capacity; DR-10)")]
screen("A28.P4", "Yes", "relation-bearing", qr=q, status="Extracted")
n = na("A28.P5", PROC, "use adherence to an approved code of conduct (Art.40) or certification mechanism (Art.42) as an element to demonstrate sufficient guarantees", "demonstration of sufficient guarantees", "information provision (demonstration)", "permission", dep="approved code of conduct (Art.40); approved certification mechanism (Art.42)")
screen("A28.P5", "Yes", "operative-assignment; device-referencing", na=[n], status="Extracted")
n = na("A28.P6", CTRL + " and " + PROC, "base the contract or legal act in whole or in part on standard contractual clauses", "processor contract", "implementation", "permission", dep="standard contractual clauses (Art.28(7)-(8)); certification (Arts 42–43)", note="SCCs may also be part of a certification.")
screen("A28.P6", "Yes", "operative-assignment; device-referencing", na=[n], status="Extracted")
n = na("A28.P7", "European Commission", "lay down standard contractual clauses for the matters in Art.28(3)-(4)", "standard contractual clauses", "rule-making (standard-setting)", "competence", cond="in accordance with the examination procedure referred to in Article 93(2)", ntype="N3-like (competence to adopt an instrument)", dep="Art.93(2) examination procedure (committee) — Chapter X", note="Competence to adopt an instrument; the instrument is constituted only if adopted.")
screen("A28.P7", "Yes", "operative-assignment (competence)", na=[n], pos=[COMM], status="Extracted", note="Commission competence subject to the committee procedure of Art.93(2) (see Chapter X).")
n = na("A28.P8", SA, "adopt standard contractual clauses for the matters in Art.28(3)-(4)", "standard contractual clauses", "rule-making (standard-setting)", "competence", cond="in accordance with the consistency mechanism referred to in Article 63", dep="consistency mechanism (Art.63)", note="Competence conditioned on a procedure involving other authorities and the Board (Chapter VII).")
screen("A28.P8", "Yes", "operative-assignment (competence)", na=[n], status="Extracted", note="Procedural dependency on Art.63.")
screen("A28.P9", "No", "formal-requirement", status="Not applicable", note="Contract/legal act in writing incl. electronic form.")
n = na("A28.P10", PROC, "(status rule) be considered a controller in respect of processing where it infringes the Regulation by determining purposes and means", "role reclassification", "enforcement (status consequence)", "declaratory", cond="processor infringes by determining purposes and means; without prejudice to Arts 82–84", note="Role-reclassification norm: processor position becomes controller position by conduct; cross-reference to liability and penalties.")
screen("A28.P10", "Yes", "operative-assignment (status rule)", na=[n], status="Extracted")

# Art 29, 30, 31
n = na("A29.P0", PROC + " and persons acting under the authority of the controller or processor", "not process personal data except on instructions from the controller, unless required by Union or Member State law", "processing on instructions", "implementation (subordination)", "prohibition", cp_status="controller (source of instructions) — identified", cond="unless required by Union or Member State law", counterpart=CTRL)
screen("A29.P0", "Yes", "operative-assignment", na=[n], status="Extracted", note="Instruction relation (controller instructions); the counterpart is named in the unit but only as the source of instructions; kept as NA.")
n = na("A30.P1", CTRL + " and, where applicable, representative", "maintain a record of processing activities containing the points (a)-(g)", "record of processing activities", "information provision (internal record)", "obligation", dep="(record = INS-TYPE; no distinct device)", note="Record is a document held by the controller; not a register constituted by the Regulation.")
n2 = na("A30.P2", PROC + " and, where applicable, representative", "maintain a record of all categories of processing activities carried out on behalf of a controller", "record of processing activities (processor)", "information provision (internal record)", "obligation")
screen("A30.P1", "Yes", "operative-assignment", na=[n], status="Extracted")
screen("A30.P2", "Yes", "operative-assignment", na=[n2], status="Extracted")
screen("A30.P3", "No", "formal-requirement", status="Not applicable", note="Records in writing including electronic form.")
q = [rt("A30.P4", CTRL + " / " + PROC + " / representatives", SA, "information/reporting", "making the record available on request", "information provision", "obligation", cond="on request of the supervisory authority", note="gov-direction: controller/processor → SA (SA may request)")]
screen("A30.P4", "Yes", "relation-bearing", qr=q, status="Extracted")
screen("A30.P5", "No", "exception", status="Not applicable", note="Exemption for enterprises <250 persons unless risk, non-occasional or special categories.")
q = [rt("A31.P0", CTRL + " and " + PROC + " (and representatives)", SA, "oversight/supervision", "cooperation with the supervisory authority in the performance of its tasks", "cooperation/coordination", "obligation", cond="on request", note="gov-direction: SA oversees controller/processor; the unit states the duty of the supervised party")]
screen("A31.P0", "Yes", "relation-bearing", qr=q, status="Extracted")

# Art 32
n = na("A32.P1", CTRL + " and " + PROC, "implement appropriate technical and organisational measures to ensure a level of security appropriate to the risk (a)-(d)", "security of processing", "implementation", "obligation", cond="state of the art, costs, nature, scope, context, purposes, risk")
screen("A32.P1", "Yes", "operative-assignment", na=[n], status="Extracted")
screen("A32.P2", "No", "substantive-conduct-rule", status="Not applicable", note="Criteria for assessing the level of security (passive).")
n = na("A32.P3", CTRL + " and " + PROC, "use adherence to approved code of conduct (Art.40) or certification mechanism (Art.42) as an element to demonstrate compliance with 32(1)", "demonstration of compliance", "information provision (demonstration)", "permission", dep="approved code of conduct (Art.40); approved certification mechanism (Art.42)")
screen("A32.P3", "Yes", "operative-assignment; device-referencing", na=[n], status="Extracted")
n = na("A32.P4", CTRL + " and " + PROC, "take steps to ensure that persons acting under their authority process data only on instructions", "instructed processing", "implementation", "obligation", cond="unless required by Union or Member State law")
screen("A32.P4", "Yes", "operative-assignment", na=[n], status="Extracted")

# Art 33
q = [rt("A33.P1", CTRL, SA + " (competent under Art.55)", "information/reporting", "notification of a personal data breach", "information provision (notification)", "obligation", cond="within 72 hours where feasible, with reasons if later; unless the breach is unlikely to result in a risk", note="counterpart is the SA competent under Art.55 (competence rule in Chapter VI)", dep="competence rule Art.55")]
screen("A33.P1", "Yes", "relation-bearing", qr=q, status="Extracted", note="Competence of the receiving SA depends on Art.55 (cross-chapter dependency).")
q = [rt("A33.P2", PROC, CTRL, "information/reporting", "notification of a personal data breach to the controller", "information provision (notification)", "obligation", cond="without undue delay after becoming aware")]
screen("A33.P2", "Yes", "relation-bearing", qr=q, status="Extracted")
screen("A33.P3", "No", "content-specification", status="Not applicable", note="Minimum content of the notification (modifies QR of 33(1); recorded in that QR's object).")
screen("A33.P4", "No", "procedural-modality", status="Not applicable", note="Notification in phases.")
q = [rt("A33.P5", CTRL, SA, "oversight/supervision", "documentation of any personal data breaches enabling the supervisory authority to verify compliance", "monitoring (enabling)", "obligation", note="gov-direction: SA verifies controller; the controller documents; the unit does not state that the documentation is transmitted", deriv="derived", unres="relation to SA derived from the purpose clause ('enable the SA to verify')")]
screen("A33.P5", "Yes", "relation-bearing (derived)", qr=q, status="Extracted", note="Derived relation: purpose clause names the SA as verifier; no transmission duty stated.")

# Art 34
q = [rt("A34.P1", CTRL, DS, "information/reporting", "communication of a personal data breach", "information provision (notification)", "obligation", cond="breach likely to result in a high risk; without undue delay")]
screen("A34.P1", "Yes", "relation-bearing", qr=q, status="Extracted")
screen("A34.P2", "No", "content-specification", status="Not applicable", note="Content of the communication.")
screen("A34.P3", "No", "exception", status="Not applicable", note="Exceptions (encryption; subsequent measures; disproportionate effort -> public communication).")
q = [rt("A34.P4", SA, CTRL, "authority/control", "require the controller to communicate the breach to the data subject, or decide that the exceptions in 34(3) are met", "enforcement/oversight (power)", "competence", cond="controller has not already communicated; SA has considered the likelihood of high risk", note="power of the SA over the controller; first SA power in the extraction")]
screen("A34.P4", "Yes", "relation-bearing", qr=q, status="Extracted")

# Art 35 DPIA
n = na("A35.P1", CTRL, "carry out an impact assessment prior to processing likely to result in a high risk", "data protection impact assessment", "implementation (risk assessment)", "obligation", cond="high risk, esp. with new technologies")
screen("A35.P1", "Yes", "operative-assignment", na=[n], status="Extracted")
q = [rt("A35.P2", CTRL, DPO, "representation/participation", "seeking the advice of the data protection officer when carrying out a DPIA", "consultation", "obligation", cond="where a DPO is designated", note="consultation of an internal advisor; gov-direction: controller consults DPO")]
screen("A35.P2", "Yes", "relation-bearing", qr=q, pos=[DPO], status="Extracted")
screen("A35.P3", "No", "content-specification", status="Not applicable", note="Cases in which a DPIA is required (a)-(c).")
n = na("A35.P4", SA, "establish and make public a list of processing operations subject to the DPIA requirement", "list of operations requiring DPIA", "rule-making (standard-setting)/information provision", "obligation", cp_status="none", note="Output artefact (list); INS-TYPE.")
q = [rt("A35.P4", SA, BOARD, "information/reporting", "communication of the DPIA lists", "information provision", "obligation", note="Board referred to in Art.68")]
screen("A35.P4", "Yes", "relation-bearing", na=[n], qr=q, pos=[BOARD], status="Extracted")
n = na("A35.P5", SA, "may establish and make public a list of processing operations for which no DPIA is required", "list of operations not requiring DPIA", "rule-making (standard-setting)", "permission", cp_status="none")
q = [rt("A35.P5", SA, BOARD, "information/reporting", "communication of the lists", "information provision", "obligation")]
screen("A35.P5", "Yes", "relation-bearing", na=[n], qr=q, status="Extracted")
n = na("A35.P6", "competent " + SA, "apply the consistency mechanism (Art.63) before adopting the lists where processing relates to offering goods/services or monitoring in several Member States, or may substantially affect free movement of personal data", "DPIA lists", "cooperation/coordination (procedural)", "obligation", cond="cross-border or free-movement relevance", dep="consistency mechanism (Art.63)", note="Procedural dependency on the consistency mechanism (Chapter VII).")
screen("A35.P6", "Yes", "operative-assignment; procedural-dependency", na=[n], status="Extracted", note="Candidate cross-chapter coupling (IV -> VII).")
screen("A35.P7", "No", "content-specification", status="Not applicable", note="Minimum content of the DPIA.")
n = na("A35.P8", "(assessor of impact — not stated)", "take compliance with approved codes of conduct (Art.40) into due account when assessing impact", "DPIA", "implementation/assessment", "obligation", dep="approved code of conduct (Art.40)", flag="subject-unstated")
screen("A35.P8", "Uncertain", "norm-without-named-subject; device-referencing", na=[n], status="Extracted")
q = [rt("A35.P9", CTRL, DS + " or their representatives", "representation/participation", "seeking the views of data subjects or their representatives on the intended processing", "consultation", "obligation", cond="where appropriate; without prejudice to commercial/public interests or security", note="soft duty ('where appropriate')")]
screen("A35.P9", "Yes", "relation-bearing", qr=q, status="Extracted")
screen("A35.P10", "No", "exception", status="Not applicable", note="Disapplies 35(1)-(7) where a general impact assessment was done in adopting the legal basis, unless Member States deem it necessary (competence recorded in the unit text).")
n = na("A35.P11", CTRL, "carry out a review of whether processing complies with the DPIA, at least when the risk changes", "DPIA review", "monitoring (self)", "obligation", cond="where necessary")
screen("A35.P11", "Yes", "operative-assignment", na=[n], status="Extracted")

# Art 36
q = [rt("A36.P1", CTRL, SA, "information/reporting", "prior consultation of the supervisory authority", "consultation", "obligation", cond="DPIA indicates a high risk in the absence of mitigation", note="prior consultation gate; whether processing may start before advice is not stated in this unit")]
screen("A36.P1", "Yes", "relation-bearing", qr=q, status="Extracted")
q = [rt("A36.P2", SA, CTRL + " (and processor where applicable)", "information/reporting", "written advice within up to eight weeks (extendable by six weeks)", "interpretation/advice", "obligation", cond="SA is of the opinion the intended processing would infringe the Regulation; periods may be suspended pending requested information", note="advice duty"),
     rt("A36.P2", SA, CTRL + " (and processor where applicable)", "authority/control", "use of any of its powers referred to in Art.58", "enforcement/oversight (power)", "competence", cond="SA is of the opinion that the intended processing would infringe the Regulation", note="cross-reference to Art.58", dep="powers of Art.58")]
screen("A36.P2", "Yes", "relation-bearing", qr=q, status="Extracted", note="Advice duty with deadlines; powers by reference to Art.58 (internal).")
q = [rt("A36.P3", CTRL, SA, "information/reporting", "information to be provided when consulting (responsibilities; purposes and means; measures and safeguards; DPO contact; the DPIA; other requested information)", "information provision", "obligation")]
screen("A36.P3", "Yes", "relation-bearing", qr=q, status="Extracted")
q = [rt("A36.P4", "Member States", SA, "representation/participation", "consultation of the supervisory authority during the preparation of a legislative proposal or regulatory measure relating to processing", "consultation", "obligation", cond="legislative measure to be adopted by a national parliament, or regulatory measure based on it", note="gov-direction: Member States consult SA")]
screen("A36.P4", "Yes", "relation-bearing", qr=q, status="Extracted", note="Link between national rule-making and the SA.")
n = na("A36.P5", "Member State law", "require controllers to consult with and obtain prior authorisation from the supervisory authority for processing for a public-interest task, including social protection and public health", "prior authorisation", "authorization", "permission (competence)", cond="processing for a task carried out in the public interest", cp_status="none", ntype="N3-like (competence to create an authorization relation)", note="Would constitute an optional authorization relation SA<->controller **only if exercised by national law**; no relation is constituted by the GDPR here.", flag="external-dependency")
screen("A36.P5", "Yes", "operative-assignment (competence)", na=[n], ext=[], status="Extracted", note="Optional national-law authorization relation; recorded as NA with external dependency (see EXT).")
ext("A36.P5", "Member State law (national legislation requiring prior authorisation)", "other_normative", "may_constitute_authorization_relation", "constitutes (if exercised)", "No authorization relation is asserted; any such relation exists only if a national law so provides (outside W).")
ext("A28.P7", "Regulation (EU) No 182/2011 (via Art.93(2) of the GDPR)", "legal_instrument", "committee_procedure_referred_to_via_Art.93", "specifies procedure", "Procedure not retrieved; relevant for the Commission's competence in Art.28(7); see Chapter X.")
