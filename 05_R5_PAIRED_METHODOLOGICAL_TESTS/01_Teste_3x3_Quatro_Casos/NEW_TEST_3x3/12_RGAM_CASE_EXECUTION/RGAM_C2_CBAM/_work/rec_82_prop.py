from rgam_lib import *

# Property families F1-F5: the mapping of the ten dimensions to families is not stated in the allowed sources (RGAM-DR-24 only says "five families F1-F5");
# provisional assignment by listing order of the ten dimensions (pairs), positional properties placed in F5; logged as a protocol gap (HQ-GAP).
FAM = {"centralization": "F1", "directness and intermediation": "F1", "public-private allocation": "F2", "self-regulatory autonomy": "F2",
       "vertical distribution": "F3", "decision-centre plurality": "F3", "relational depth": "F4", "functional allocation": "F4",
       "discretion distribution": "F5", "accountability structure": "F5", "necessary stage": "F5", "substitutability": "F5"}
AGG_SC = "Value stated for this S only; no aggregation to a larger scale is made here (values per S are reported before any summary); no scalar, composite or threshold."


def P(key, name, btype, bearer, scale, value, rule, support, status, agg=AGG_SC, path="", cdep="N", cref="", count="", rival="", hq="hq.GAP_BUNDLE"):
    return prop(key, name, FAM[name], btype, bearer, scale, value, rule, support, status, path=path, agg=agg, cdep=cdep, cref=cref, count=count,
                fallacy="Y", rival=rival, hq=hq)

P("prop.CENT_AUTH", "centralization", "SUBCONFIGURATION", "sc.AUTH", "sc.AUTH (function: authorisation of declarants)",
  "Binding status decisions (grant, refusal, guarantee requirement, revocation) rest with the competent authority of the Member State where the applicant is established; the Commission administers the registry accounts and is a consulted party. Decisions are decentralised to Member State level; account administration is central.",
  "Read the origin position of each decision relation of the S (qr.A17_GRANT, qr.A17_REFUSE, qr.A17_GUARANTEE, qr.A17_REVOKE) and of the account relations (qr.A16_ACCOUNT, qr.A16_ACCESS, qr.A16_CLOSE); no counting.",
  "qr.A17_GRANT;qr.A17_REFUSE;qr.A17_GUARANTEE;qr.A17_REVOKE;qr.A16_ACCOUNT;qr.A16_ACCESS;qr.A16_CLOSE;qr.A17_CONSULT", "asserted",
  rival="Reading the Commission's consultation and account roles as co-decision would move the S towards a shared decision centre; the text states consultation only.", hq="hq.GAP_BUNDLE")
P("prop.CENT_CERT", "centralization", "SUBCONFIGURATION", "sc.CERTMKT", "sc.CERTMKT (function: certificate lifecycle)",
  "Price calculation and publication, platform establishment and management, registry recording and cancellation are assigned to the Commission; sale and repurchase are obligations of the Member State where the declarant is established, executed through the Commission-run platform. Central infrastructure; decentralised commercial counterparty.",
  "Read the origin positions of qr.A20_SELL, qr.A23_REPURCHASE (Member State) and qr.A20_REGSALE, qr.A23_COMBEHALF, qr.A24_CANCEL (Commission) and of na.A21_PRICE, na.A21_PUBLISH, na.A20_PLATFORM.",
  "qr.A20_SELL;qr.A20_REGSALE;qr.A23_REPURCHASE;qr.A23_COMBEHALF;qr.A24_CANCEL;na.A21_PRICE;na.A21_PUBLISH;na.A20_PLATFORM", "asserted")
P("prop.CENT_ENFORCE", "centralization", "SUBCONFIGURATION", "sc.ENFORCE", "sc.ENFORCE (function: review, determination and sanction)",
  "The Commission sets risk factors, reviews declarations and produces an indicative preliminary calculation; the competent authority holds the definitive determination, notification and penalty decisions; Member States communicate penalty decisions to the Commission and register payment in the CBAM registry.",
  "Read the origin positions and the 'indicative / without prejudice' wording of qr.A19_REVIEW, qr.A19_PRELIM, qr.A19_DECIDE, qr.A26_IMPOSE_ACD, qr.A26_COMM.",
  "qr.A19_REVIEW;qr.A19_PRELIM;qr.A19_DECIDE;qr.A26_IMPOSE_ACD;qr.A26_COMM;na.A19_RISK", "asserted")
P("prop.CENT_LIFECYCLE", "centralization", "ARCHITECTURE", "arch.LIFECYCLE", "arch.LIFECYCLE over sc.AUTH, sc.CERTMKT, sc.ENFORCE",
  "Differentiated by function: central (Commission) for information infrastructure, accounts, price, platform and review input; Member State level for binding decisions. The arrangement is not summarised as 'centralised' or 'decentralised' (an arrangement strongly central in one function and decentralised in another is not described by one label).",
  "Qualitative juxtaposition of PROP CENT_AUTH, CENT_CERT and CENT_ENFORCE.", "qr.A17_GRANT;qr.A19_DECIDE;qr.A19_PRELIM;qr.A20_REGSALE;qr.A16_ACCOUNT", "asserted",
  agg="Values per S are reported first (PROP CENT_AUTH, CENT_CERT, CENT_ENFORCE); the whole-level statement is a qualitative juxtaposition by function; no composite, index or threshold; ecological and atomistic fallacies checked (the whole-level statement is not pushed down to every S).")
P("prop.PLURALITY_AUTH", "decision-centre plurality", "SUBCONFIGURATION", "sc.AUTH", "sc.AUTH",
  "Plural decision centres by structure: each Member State designates its own competent authority and the competent authority of the Member State where the applicant is established decides (A11(1), A17(1)). The number of decision centres is not stated.",
  "Read the multiplicity of qr.A11_DESIG ('each Member State') and the allocation rule of qr.A17_GRANT.", "qr.A11_DESIG;qr.A17_GRANT", "asserted",
  count="undetermined: legal multiplicity 'each Member State' (number of Member States not stated in W); no designation of a competent authority is evidenced (PT-7)")
P("prop.PLURALITY_DELEG", "decision-centre plurality", "SUBCONFIGURATION", "sc.DELEG", "sc.DELEG (delegated acts only)",
  "For delegated acts two institutions, the European Parliament and the Council, each hold an independent power to object or to revoke the delegation. The effect of the CBAM Committee's involvement in implementing acts is external to W and is not included in this value.",
  "Read the holders of the powers in qr.A28_OBJECT and qr.A28_REVOKE.", "qr.A28_OBJECT;qr.A28_REVOKE;qr.A28_CONFER", "asserted")
P("prop.DIRECT_AUTH", "directness and intermediation", "SUBCONFIGURATION", "sc.AUTH", "sc.AUTH",
  "Importers established in a Member State apply directly; an importer not established in a Member State can apply only through an indirect customs representative (A5(2)); an established importer may appoint one (A5(1)). Intermediation is therefore mandatory for non-established importers and optional for established ones.",
  "Read the conditions of qr.A5_APPLY and its origin position; the representative's constitution is external (flagged).", "qr.A5_APPLY", "asserted",
  rival="The status and powers of the indirect customs representative are constituted by an external Regulation; the intermediation is stated in W but its legal content is undetermined.")
P("prop.DIRECT_VERIF", "directness and intermediation", "SUBCONFIGURATION", "sc.VERIF", "sc.VERIF",
  "Declarants and operators must go through an accredited verifier to have declared or determined embedded emissions verified (A8(1), A10(5)(b)); accreditation is conferred through a national accreditation body (A18(2)). The verification function is intermediated by third parties between the obliged parties and the authorities.",
  "Read qr.A8_ENSURE, qr.A10_VERIFY and qr.A18_ACCREDIT; the verifier relations are down-coded for a constitutive external dependency (flagged).", "qr.A8_ENSURE;qr.A10_VERIFY;qr.A18_ACCREDIT", "asserted")
P("prop.PUBPRIV_VERIF", "public-private allocation", "SUBCONFIGURATION", "sc.VERIF", "sc.VERIF",
  "Verification and accreditation are allocated to accredited persons and to national accreditation bodies; W does not state whether those are public or private entities, so the allocation along the public-private axis is not determinable within W.",
  "No relation or position record states the public or private character of the verifier or of the accreditation body.", "qr.A18_ACCREDIT;qr.A8_ENSURE;pd.VERIF;pd.NAB", "undetermined",
  count="undetermined: no evidenced instance and no stated legal multiplicity (PT-7)")
P("prop.SELFREG", "self-regulatory autonomy", "ARCHITECTURE", "arch.WHOLE", "arch.WHOLE (declared corpus)",
  "No rule-making or standard-setting power is conferred on private actors by the text of W; verifiers apply the principles of Annex VI and the thresholds of implementing acts; the claim concerns the declared corpus only.",
  "Absence-dependent: closure statement cl.NO_SELFREG records the review of every record with a rule-making function.", "na.A5P8_IMPL;na.A7P7_IMPL;qr.ANX6_PRINC;qr.A28_CONFER", "asserted",
  agg="Whole-level statement over the declared corpus; per-S values would all state the same absence; no composite.", cdep="Y", cref="cl.NO_SELFREG")
P("prop.VERTICAL_LIFE", "vertical distribution", "ARCHITECTURE", "arch.LIFECYCLE", "arch.LIFECYCLE over sc.AUTH, sc.CERTMKT, sc.ENFORCE",
  "Union level: Commission (registry, accounts, price, platform, review input, cancellation). Member State level: competent authorities (status decisions, determinations, penalties, recovery under national law) and Member States (sale, repurchase). Distribution is by function across the two levels.",
  "Read the origin positions of the relations of the three S by level.", "qr.A16_ACCOUNT;qr.A17_GRANT;qr.A19_DECIDE;qr.A20_SELL;qr.A23_REPURCHASE;qr.A26_IMPOSE_ACD", "asserted",
  agg="Values per S are reported first (PROP CENT_AUTH, CENT_CERT, CENT_ENFORCE); qualitative juxtaposition; no composite.")
P("prop.FUNCALLOC_LIFE", "functional allocation", "ARCHITECTURE", "arch.LIFECYCLE", "arch.LIFECYCLE over sc.AUTH, sc.CERTMKT, sc.ENFORCE",
  "By function: admission (competent authority); account and registry (Commission); price (Commission); sale and repurchase (Member State, through the platform); monitoring and review (Commission and competent authority); definitive determination and penalty (competent authority); recovery (competent authority under national law).",
  "List, for each function value of the relations of the three S, the origin position.", "qr.A17_GRANT;qr.A16_ACCOUNT;na.A21_PRICE;qr.A20_SELL;qr.A19_REVIEW;qr.A19_DECIDE;qr.A26_SECURE", "asserted",
  agg="Values per S are the function lists of the relation records; no composite.")
P("prop.DISC_AUTH", "discretion distribution", "SUBCONFIGURATION", "sc.AUTH", "sc.AUTH",
  "By function x position x relation: grant (competent authority): criteria fixed in A17(2), with an assessment of financial and operational capacity; guarantee (competent authority): amount fixed by a stated formula, equivalence of 'another form of guarantee' judged by the authority; revocation (competent authority): grounds specified, the notion of 'serious or repeated' infringement left to implementing acts; consultation (competent authorities of other Member States, Commission): effect on the deciding authority not stated.",
  "Read the discretion_attribute of the relations of the S.", "qr.A17_GRANT;qr.A17_GUARANTEE;qr.A17_REVOKE;qr.A17_CONSULT", "asserted")
P("prop.DISC_ENFORCE", "discretion distribution", "SUBCONFIGURATION", "sc.ENFORCE", "sc.ENFORCE",
  "Commission: review strategy and audit 'deemed necessary', indicative preliminary calculation; competent authority: determination of the number and whether to act on the preliminary calculation; penalty for declarants fixed by formula, for other persons within three to five times with listed factors; means of recovery left to national law.",
  "Read the discretion_attribute of the relations of the S.", "qr.A19_REVIEW;qr.A19_PRELIM;qr.A19_DECIDE;qr.A26_IMPOSE_ACD;qr.A26_IMPOSE_OTHER;qr.A26_SECURE", "asserted")
P("prop.ACC_ASSERTED", "accountability structure", "SUBCONFIGURATION", "sc.ENFORCE", "sc.ENFORCE",
  "Coded relations are classified INFO (reports, notifications, registrations) or INFO with sufficiency indeterminate where reasons and information on a right to appeal are stated without an identified forum (qr.A19_DECIDE, qr.A26_IMPOSE_ACD, qr.A26_IMPOSE_OTHER); no relation of the S is classified ANSWERABILITY or ACCOUNTABILITY.",
  "Read accountability_class, accountability_sufficiency and accountability_missing_elements of the relations of the S (descriptive tally of coded records, not an absence claim about the law).",
  "qr.A19_DECIDE;qr.A26_IMPOSE_ACD;qr.A26_IMPOSE_OTHER;qr.A19_NOACTION;qr.A22_INFORM", "asserted",
  hq="hq.ACCOUNT_APPEAL")
P("prop.ACC_ABSENCE", "accountability structure", "ARCHITECTURE", "arch.LIFECYCLE", "arch.LIFECYCLE",
  "The claim that the arrangement contains no actor-forum accountability relation depends on an absence: appeals and judicial control are governed outside W and the committee procedure of the delegation pattern is external; the claim is therefore undetermined.",
  "Absence-dependent: closure test cl.ACCOUNT_ABSENCE returns UNDETERMINED.", "qr.A19_DECIDE;qr.A26_IMPOSE_ACD;qr.A17_REFUSE;qr.A17_REVOKE", "undetermined",
  agg="Whole-level absence claim; no per-S values are generalised.", cdep="Y", cref="cl.ACCOUNT_ABSENCE", hq="hq.ACCOUNT_APPEAL")
P("prop.NECESSARY_STAGE", "necessary stage", "RELATION", "qr.A17_GRANT", "arch.LIFECYCLE",
  "Whether the grant of the status of authorised CBAM declarant is a necessary stage for importing in-scope goods depends on the absence of alternative paths; the derogations (A2(3), A2(4), A2(7), A5(4)) rest on thresholds and definitions in external instruments, so the claim is undetermined.",
  "Positional property (depends on the whole): follow the path application -> grant -> importation (A4, A25(1)); absence of alternative paths tested in cl.NECESSARY_STAGE (UNDETERMINED).",
  "qr.A5_APPLY;qr.A17_GRANT;na.A4_PROHIB;na.A25_PROHIB", "undetermined",
  path="Path step = a relation of types delegation_authorization or authority_control with modality obligation; successive steps are linked by explicit rules (A17(1) 'application ... submitted in accordance with Article 5'; A4 and A25(1) restricting importation to the status); reachability alone is not used.",
  agg="Positional value stated for the relation within ARCH-01 only.", cdep="Y", cref="cl.NECESSARY_STAGE")
P("prop.SUBSTITUTABILITY", "substitutability", "POSITION", "pd.ICR", "sc.AUTH; sc.TRANSITION",
  "Whether the indirect customs representative can substitute the importer as applicant and as reporter, and whether no other substitute exists, depends on the external constitution of the representative and on absence of alternatives; the claim is undetermined.",
  "Positional property: A5(1)-(2) and A32 state the substitution; absence of other substitutes tested in cl.SUBSTITUTABILITY (UNDETERMINED).", "qr.A5_APPLY;na.A32_ICR;qr.A35_REPORT", "undetermined",
  agg="Positional value stated for the position within the two S named; no aggregation.", cdep="Y", cref="cl.SUBSTITUTABILITY")
P("prop.DEPTH_ENFORCE", "relational depth", "SUBCONFIGURATION", "sc.ENFORCE", "sc.ENFORCE (enforcement sequence only)",
  "The enforcement sequence is a chain of explicitly cross-referenced relation steps: Commission review and assessment (qr.A19_REVIEW, qr.A19_ASSESS) -> preliminary calculation to the competent authority (qr.A19_PRELIM) -> determination and request to surrender (qr.A19_DECIDE) -> penalty imposition (qr.A26_IMPOSE_ACD) -> recovery (qr.A26_SECURE) -> communication to the Commission (qr.A26_COMM).",
  "Path-based: follow the explicit references listed under path semantics; no centrality or path-length index is computed.",
  "qr.A19_REVIEW;qr.A19_ASSESS;qr.A19_PRELIM;qr.A19_DECIDE;qr.A26_IMPOSE_ACD;qr.A26_SECURE;qr.A26_COMM", "asserted",
  path="A path step is a QR of type oversight_supervision, information_reporting or authority_control with modality obligation or permission whose condition refers to the preceding step by explicit cross-reference (A19(5) 'taking into account the information submitted by the Commission'; A26(4) 'including in light of the preliminary calculations made by the Commission in accordance with Article 19'; A26(5) 'the due date referred to in paragraph 4, point (d)'); reachability alone is not used.")
