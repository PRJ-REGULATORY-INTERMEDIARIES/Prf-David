# Batch 02 — Chapter III (Articles 12–23). Convention (DECISION_RULES v1.1): origin = obligor; counterpart = right-holder/addressee.
CTRL, DS = "controller", "data subject"
COMM = pd("European Commission", "position_type", "A12.P8", note="Institution constituted by the Treaties, not by the GDPR; no external reference is made to the Treaties in the unit.")
SA_T = "supervisory authority"

def rt(u, rtype, obj, fn, mod, cond="", note="", deriv="direct", unres="", flag="", origin=CTRL, cp=DS, acc="", ext_dep=""):
    return qr(u, origin, cp, rtype, obj, fn, mod, cond=cond, deriv=deriv, type_note=note, unresolved=unres, flag=flag, acc=acc, ext=ext_dep)

# Article 12
q = [rt("A12.P1", "information/reporting", "information (Arts 13–14), communications (Arts 15–22, 34) in concise, transparent, intelligible form", "information provision", "obligation", note="modalities of communication")]
screen("A12.P1", "Yes", "relation-bearing", qr=q)
q = [rt("A12.P2", "beneficiary/protective", "facilitation of exercise of rights under Arts 15–22; no refusal to act except where unable to identify", "implementation (facilitation)", "obligation", cond="refusal allowed only if the controller demonstrates it cannot identify the data subject (Art.11(2))")]
screen("A12.P2", "Yes", "relation-bearing", qr=q)
q = [rt("A12.P3", "information/reporting", "information on action taken on a request under Arts 15–22", "information provision", "obligation", cond="without undue delay; within one month; extendable by two months with reasons")]
screen("A12.P3", "Yes", "relation-bearing", qr=q)
q = [rt("A12.P4", "information/reporting", "reasons for not acting on a request and information on the possibility of lodging a complaint with a supervisory authority and seeking a judicial remedy", "information provision", "obligation", cond="controller does not take action; at the latest within one month",
        note="points the data subject to Arts 77–79 (remedies); the information duty is the relation here, the remedies are separate relations (Chapter VIII)")]
screen("A12.P4", "Yes", "relation-bearing", qr=q, note="Information duty that refers to complaint and judicial remedy; the remedy relations are extracted at Arts 77–79.")
q = [rt("A12.P5", "authority/control", "right of the controller to charge a reasonable fee or refuse to act on manifestly unfounded or excessive requests", "implementation (private-party competence)", "permission", cond="requests manifestly unfounded or excessive; controller bears the burden of demonstrating this",
        note="a private-party competence toward the data subject conferred by the Regulation; typed 'authority/control' provisionally; free of charge otherwise", flag="type-uncertain")]
screen("A12.P5", "Yes", "relation-bearing", qr=q, note="Free of charge by default; conditional permission to charge or refuse; burden of demonstration on the controller.")
q = [rt("A12.P6", "information/reporting", "request for additional information to confirm identity", "information provision (request)", "permission", cond="reasonable doubts concerning identity")]
screen("A12.P6", "Yes", "relation-bearing", qr=q)
q = [rt("A12.P7", "information/reporting", "combination of information with standardised machine-readable icons", "information provision", "permission", cond="information under Arts 13 and 14")]
screen("A12.P7", "Yes", "relation-bearing", qr=q, note="Icons: permission; content set by delegated act (P8).")
n = na("A12.P8", "European Commission", "adopt delegated acts under Art.92 to determine the information presented by icons and the procedures for providing standardised icons", "icons and procedures", "rule-making (delegated)", "competence", cond="in accordance with Article 92", cp_status="none", note="Delegation of rule-making to the Commission; the controlling conditions (revocation, objection) are in Art.92 and relate the Commission to the European Parliament and the Council.")
screen("A12.P8", "Yes", "operative-assignment (delegated competence)", na=[n], pos=[COMM], status="Extracted", note="Delegated rule-making competence; the supervisory relation is extracted at Art.92.")

# Articles 13–14 (information duties)
q = [rt("A13.P1", "information/reporting", "identity and contact details of the controller and its representative; DPO contact; purposes and legal basis; legitimate interests; recipients; intended third-country transfers and safeguards", "information provision", "obligation", cond="personal data collected from the data subject; at the time of obtaining the data")]
screen("A13.P1", "Yes", "relation-bearing", qr=q, note="Points (a)-(f) inventoried; references to the representative, DPO and the Commission's adequacy decisions are mentions inside the content of the information (not relations of the controller with those positions).")
q = [rt("A13.P2", "information/reporting", "storage period; existence of rights; right to withdraw consent; right to lodge a complaint with a supervisory authority; statutory/contractual requirement; automated decision-making", "information provision", "obligation", cond="in addition to 13(1); at the time of obtaining the data")]
screen("A13.P2", "Yes", "relation-bearing", qr=q)
q = [rt("A13.P3", "information/reporting", "information on another purpose before further processing", "information provision", "obligation", cond="intended further processing for another purpose")]
screen("A13.P3", "Yes", "relation-bearing", qr=q)
screen("A13.P4", "No", "exception", status="Not applicable", note="Disapplies 13(1)-(3) where the data subject already has the information; modifies the condition of the existing relations (recorded in their conditions note only).")
q = [rt("A14.P1", "information/reporting", "identity and contact details; DPO; purposes; categories of data; recipients; intended third-country transfers", "information provision", "obligation", cond="personal data not obtained from the data subject")]
screen("A14.P1", "Yes", "relation-bearing", qr=q)
q = [rt("A14.P2", "information/reporting", "storage period; legitimate interests; rights; complaint right; source of the data; automated decision-making", "information provision", "obligation", cond="in addition to 14(1)")]
screen("A14.P2", "Yes", "relation-bearing", qr=q)
q = [rt("A14.P3", "information/reporting", "timing of information (within one month; at first communication; at first disclosure)", "information provision", "obligation", cond="timing alternatives (a)-(c)")]
screen("A14.P3", "Yes", "relation-bearing", qr=q)
q = [rt("A14.P4", "information/reporting", "information on another purpose before further processing", "information provision", "obligation", cond="intended further processing")]
screen("A14.P4", "Yes", "relation-bearing", qr=q)
screen("A14.P5", "No", "exception", status="Not applicable", note="Exceptions (already informed; impossible/disproportionate effort — with a duty to make information public; Union/Member State law; professional secrecy). Modifies conditions of Art.14(1)-(4).")

# Articles 15–22 (rights)
q = [rt("A15.P1", "beneficiary/protective", "right of access: confirmation of processing, access to data and information (purposes, categories, recipients, storage, rights, complaint right, source, automated decision-making)", "information provision", "entitlement", note="entitlement of the data subject against the controller")]
screen("A15.P1", "Yes", "relation-bearing", qr=q)
q = [rt("A15.P2", "beneficiary/protective", "right to be informed of the appropriate safeguards under Art.46 for transfers to third countries", "information provision", "entitlement", cond="transfer to a third country or international organisation")]
screen("A15.P2", "Yes", "relation-bearing", qr=q, note="Art.46 safeguards referred to (internal cross-reference).")
q = [rt("A15.P3", "beneficiary/protective", "copy of the personal data; fee for further copies; electronic form", "information provision", "obligation", cond="further copies: reasonable fee based on administrative costs")]
screen("A15.P3", "Yes", "relation-bearing", qr=q)
screen("A15.P4", "No", "limitation", status="Not applicable", note="Right to a copy must not adversely affect others' rights; no position or assignment.")
q = [rt("A16.P0", "beneficiary/protective", "right to rectification of inaccurate data and completion of incomplete data", "remediation", "entitlement", cond="without undue delay")]
screen("A16.P0", "Yes", "relation-bearing", qr=q)
q = [rt("A17.P1", "beneficiary/protective", "right to erasure and controller's obligation to erase on listed grounds", "remediation", "entitlement", cond="one of grounds (a)-(f) applies")]
screen("A17.P1", "Yes", "relation-bearing", qr=q)
q = [rt("A17.P2", "information/reporting", "reasonable steps to inform other controllers processing public data that the data subject requested erasure of links/copies", "information provision", "obligation", cond="controller made data public and must erase; taking account of available technology and cost", cp="controllers processing the same personal data (other controllers)", note="counterpart is a category (other controllers), not the data subject", deriv="direct")]
screen("A17.P2", "Yes", "relation-bearing", qr=q, note="Relation controller -> other controllers (information); first controller-to-controller relation in Chapter III.")
screen("A17.P3", "No", "exception", status="Not applicable", note="Exceptions to 17(1)-(2) (freedom of expression; legal obligation; public health; archiving; legal claims).")
q = [rt("A18.P1", "beneficiary/protective", "right to restriction of processing", "remediation", "entitlement", cond="one of grounds (a)-(d)")]
screen("A18.P1", "Yes", "relation-bearing", qr=q)
screen("A18.P2", "No", "substantive-conduct-rule", status="Not applicable", note="Limits on further processing of restricted data (passive).")
q = [rt("A18.P3", "information/reporting", "information to the data subject before the restriction is lifted", "information provision", "obligation")]
screen("A18.P3", "Yes", "relation-bearing", qr=q)
q = [rt("A19.P0", "information/reporting", "communication of rectification/erasure/restriction to each recipient to whom data were disclosed; information to the data subject about those recipients on request", "information provision", "obligation", cond="unless impossible or disproportionate effort; information about recipients only if the data subject requests it", cp="recipient", note="two relations in one unit: controller -> recipient (communication) and controller -> data subject (information on request)")]
q.append(rt("A19.P0", "information/reporting", "information to the data subject about the recipients", "information provision", "obligation", cond="data subject requests it"))
screen("A19.P0", "Yes", "relation-bearing", qr=q)
q = [rt("A20.P1", "beneficiary/protective", "right to receive data in a structured, commonly used, machine-readable format and to transmit them to another controller without hindrance", "implementation", "entitlement", cond="processing based on consent or contract; carried out by automated means")]
screen("A20.P1", "Yes", "relation-bearing", qr=q, note="Also mentions 'another controller' (Art.20(1)); relation to the other controller is not stated beyond non-hindrance.")
q = [rt("A20.P2", "beneficiary/protective", "right to have data transmitted directly from one controller to another", "implementation", "entitlement", cond="where technically feasible")]
screen("A20.P2", "Yes", "relation-bearing", qr=q)
screen("A20.P3", "No", "limitation", status="Not applicable", note="Disapplies the right for public-interest tasks / official authority.")
screen("A20.P4", "No", "limitation", status="Not applicable", note="Protects rights of others.")
q = [rt("A21.P1", "beneficiary/protective", "right to object to processing based on Art.6(1)(e)/(f); controller must stop unless it demonstrates compelling legitimate grounds", "remediation", "entitlement", cond="grounds relating to the data subject's particular situation")]
screen("A21.P1", "Yes", "relation-bearing", qr=q)
q = [rt("A21.P2", "beneficiary/protective", "right to object to direct marketing", "remediation", "entitlement", cond="direct marketing")]
screen("A21.P2", "Yes", "relation-bearing", qr=q)
screen("A21.P3", "No", "consequence-of-objection", status="Not applicable", note="Passive consequence of 21(2) (data no longer processed); same relation as QR for 21(2).")
q = [rt("A21.P4", "information/reporting", "explicit presentation of the rights to object clearly and separately", "information provision", "obligation", cond="at the latest at first communication")]
screen("A21.P4", "Yes", "relation-bearing", qr=q)
screen("A21.P5", "Uncertain", "permission-for-data-subject", status="Hold", note="Data subject may exercise the right to object by automated means using technical specifications (information society services; notwithstanding Directive 2002/58/EC). Recorded as an external reference only.")
ext("A21.P5", "Directive 2002/58/EC", "legal_instrument", "notwithstanding_clause", "specifies", "No relation imported; unit left on Hold because the permission has no identifiable counterpart in the unit.")
q = [rt("A21.P6", "beneficiary/protective", "right to object to processing for research/statistical purposes", "remediation", "entitlement", cond="processing for scientific or historical research or statistical purposes; unless necessary for a public-interest task")]
screen("A21.P6", "Yes", "relation-bearing", qr=q)
q = [rt("A22.P1", "beneficiary/protective", "right not to be subject to a decision based solely on automated processing, including profiling, with legal or similarly significant effects", "remediation", "entitlement", cond="solely automated decision with legal/similarly significant effects")]
screen("A22.P1", "Yes", "relation-bearing", qr=q)
screen("A22.P2", "No", "exception", status="Not applicable", note="Exceptions (contract; authorised by law; explicit consent).")
q = [rt("A22.P3", "beneficiary/protective", "safeguards: right to obtain human intervention, to express a point of view and to contest the decision", "implementation (safeguard)", "obligation", cond="decisions under 22(2)(a) and (c)")]
screen("A22.P3", "Yes", "relation-bearing", qr=q)
screen("A22.P4", "No", "substantive-conduct-rule", status="Not applicable", note="Restricts reliance on special categories; passive.")
n = na("A23.P1", "Union or Member State law (legislator not named)", "restrict by legislative measure the scope of the obligations and rights in Arts 12–22 and 34 (and Art.5 insofar as corresponding)", "scope of data-subject rights and controller/processor obligations", "rule-making (restriction)", "competence", cond="restriction respects the essence of fundamental rights and is a necessary and proportionate measure to safeguard the objectives (a)-(j)", cp_status="none", note="Competence conferred by the Regulation on Union/Member State legislation; legislator not a named position.", flag="subject-unstated")
n2 = na("A23.P2", "Union or Member State law (legislator not named)", "contain specific provisions where relevant as to purposes, categories of data, scope, safeguards, controllers, storage periods, risks and the right to be informed about the restriction", "content of restricting legislative measures", "rule-making (conditions on restriction)", "obligation", cond="legislative measure referred to in 23(1)", cp_status="none", flag="subject-unstated")
screen("A23.P1", "Yes", "operative-assignment (competence)", na=[n], status="Extracted", note="Restriction clause: competence of Union/Member State legislators over data-subject rights (limits on the entitlements of Arts 12–22).")
screen("A23.P2", "Yes", "operative-assignment", na=[n2], status="Extracted", note="Conditions on restricting measures.")
