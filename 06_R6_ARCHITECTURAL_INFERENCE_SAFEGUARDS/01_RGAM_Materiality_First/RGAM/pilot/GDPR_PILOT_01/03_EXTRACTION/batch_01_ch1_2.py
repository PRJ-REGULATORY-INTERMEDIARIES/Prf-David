# Batch 01 — Chapters I–II (Articles 1–11). Machine-generated, provisional (DECISION_RULES v1.0).
# ---- positions / devices defined in Chapter I
pd("controller", "position_type", "A4.P0.pt7", note="Role defined functionally ('determines the purposes and means'), not constituted as an office; criteria for nomination may be set by Union or Member State law (Art.4(7)).")
pd("processor", "position_type", "A4.P0.pt8", note="Role defined functionally ('processes on behalf of the controller').")
pd("data subject", "position_type", "A4.P0.pt1", note="Identified or identifiable natural person; category defined in the definition of 'personal data'.")
pd("recipient", "position_type", "A4.P0.pt9", note="Category; public authorities receiving data in a particular inquiry under Union/Member State law are not 'recipients'.")
pd("third party", "position_type", "A4.P0.pt10", note="Residual category.")
pd("representative (of controller/processor in the Union)", "position_type", "A4.P0.pt17", note="Designated in writing by the controller or processor pursuant to Art.27; instance created by the designation, not by the Regulation.")
pd("supervisory authority", "position_type", "A4.P0.pt21", ntype="N2 (referenced; establishing obligation in Art.51)", mult="one or more per Member State (Art.51(1)) — to be checked at Art.51", note="Defined as an 'independent public authority which is established by a Member State pursuant to Article 51'. The Regulation does not itself constitute any national authority (N2, see Art.51). No national instance created.")
pd("supervisory authority concerned", "position_type", "A4.P0.pt22", note="Relational category (establishment of controller/processor; affected data subjects; complaint lodged) — role assigned by facts, not by designation.")
pd("main establishment", "position_type", "A4.P0.pt16", note="Locational/organizational category used to allocate competence (Art.56); not an institution.")
pd("binding corporate rules", "device", "A4.P0.pt20", note="Defined as data protection policies adhered to by a controller/processor within a group; approval by supervisory authority is regulated in Art.47. Device status to be assessed at Art.47 (DEV threshold).", flag="DEV-threshold")
pd("international organisation", "position_type", "A4.P0.pt26", note="Category used for transfers (Chapter V).")
ext("A2.P2.ptb", "Treaty on European Union, Title V, Chapter 2 (common foreign and security policy)", "legal_instrument", "defines_scope_exclusion", "scope", "Scope boundary only; no governance relation taken from it.")
ext("A2.P3", "Regulation (EC) No 45/2001", "legal_instrument", "applies_to_Union_institutions_bodies", "constitutes_other_regime", "Processing by Union institutions is governed elsewhere; the European Data Protection Supervisor (established by that instrument) is not constituted by the GDPR.")
ext("A2.P4", "Directive 2000/31/EC (Arts 12–15)", "legal_instrument", "without_prejudice", "scope", "No relation taken.")
ext("A4.P0.pt25", "Directive (EU) 2015/1535, Art.1(1)(b)", "legal_instrument", "defines_term", "defines_term", "Definition only.")
ext("A2.P2.ptd", "(unnamed) rules on 'competent authorities' for criminal-law purposes", "other_normative", "defines_scope_exclusion", "scope", "Excluded regime not named in the provision; no content imported.")

# ---- Article 1
screen("A1.P1", "No", "purpose/scope-context", status="Not applicable", note="Statement of subject-matter; no position, assignment or relation.")
screen("A1.P2", "No", "purpose/scope-context", status="Not applicable", note="Statement of protected interests; no position.")
n = na("A1.P3", "(not stated — passive; Union and Member State legal orders implied)", "not restrict or prohibit free movement of personal data within the Union for reasons connected with protection", "free movement of personal data", "rule-making/limitation of legislation (implied)", "prohibition", counterpart="", cp_status="none", deriv="direct", note="Subject is not named. Not attributed to any position.", flag="subject-unstated")
screen("A1.P3", "Uncertain", "norm-without-named-subject", na=[n], status="Extracted", note="Prohibition with no named addressee; kept as NA with unstated subject.")

# ---- Article 2, 3 (scope)
screen("A2.P1", "No", "scope-context", status="Not applicable", note="Material scope.")
screen("A2.P2", "No", "scope-context", ext=["EXT-001", "EXT-005"], status="Not applicable", note="Exclusions from scope; external references recorded without expansion.")
n = na("A2.P3", "(not stated — Union legislator implied)", "adapt Regulation (EC) 45/2001 and other Union legal acts to the principles and rules of this Regulation, in accordance with Art.98", "Union legal acts on processing by Union institutions", "rule-making/adaptation", "obligation", cp_status="none", cond="in accordance with Article 98", note="Addressee not named; see Art.98 (Commission proposals).", flag="subject-unstated")
screen("A2.P3", "Uncertain", "norm-without-named-subject; scope", na=[n], ext=["EXT-002"], status="Extracted", note="Adaptation duty with unstated subject; link to Art.98.")
screen("A2.P4", "No", "scope-context", ext=["EXT-003"], status="Not applicable", note="Without-prejudice clause.")
screen("A3.P1", "No", "scope-context", status="Not applicable", note="Territorial scope.")
screen("A3.P2", "No", "scope-context", status="Not applicable", note="Territorial scope (extraterritorial application).")
screen("A3.P3", "No", "scope-context", status="Not applicable", note="Territorial scope (public international law).")

# ---- Article 4 (definitions)
n1 = na("A4.P0.pt7", "Union or Member State law (legislator not named)", "provide for the controller or the specific criteria for its nomination", "controller", "authorization/designation", "permission", cond="where the purposes and means of processing are determined by Union or Member State law", cp_status="none", note="Competence-type permission of the Union/Member State legislator; the Regulation is the source, the legislator is not a position of the text.", flag="subject-unstated")
screen("A4.P0", "Yes", "position-defining; definitional-context", na=[n1], pos=["PD-001", "PD-002", "PD-003", "PD-004", "PD-005", "PD-006", "PD-007", "PD-008", "PD-009", "PD-010", "PD-011"], ext=["EXT-004"], status="Extracted",
       note="26 point-definitions inventoried automatically. Position-type/device candidates extracted: pts 1,7,8,9,10,16,17,20,21,22,26. Definitions of data categories, processing, consent, breach, profiling etc. are definitional context only (no assignment). Pt.24 'relevant and reasoned objection' is a procedural concept used in Arts 60–65 (see Chapter VII).")

# ---- Article 5
screen("A5.P1", "No", "substantive-conduct-rule", status="Not applicable", note="Six principles stated passively ('Personal data shall be...'); no position is the subject until Art.5(2). Attribution to the controller is derived from 5(2).")
n = na("A5.P2", "controller", "be responsible for, and be able to demonstrate compliance with, Art.5(1) ('accountability')", "compliance with processing principles", "implementation; compliance demonstration", "obligation", cp_status="none", note="The text labels this 'accountability'. No forum is identified in this unit; demonstration-to-whom is not stated (supervisory authorities' powers appear in Chapter VI). Classification under DR-10: IND (assertion of accountability; forum not identifiable here).", flag="accountability-label")
screen("A5.P2", "Yes", "operative-assignment", na=[n], status="Extracted", note="Assignment to controller; textual label 'accountability' without identifiable forum -> accountability class IND here.")

# ---- Article 6
screen("A6.P1", "No", "substantive-conduct-rule", status="Not applicable", note="Conditions for lawful processing (a)-(f). Points (c),(e) refer to a legal obligation or official authority vested in the controller — context for 6(3).")
n = na("A6.P2", "Member States", "maintain or introduce more specific provisions to adapt the application of the Regulation for processing under points (c) and (e) of Art.6(1)", "specific requirements for processing", "rule-making (specification)", "competence", cond="limited to processing for compliance with legal obligation / public-interest task; see also Chapter IX", cp_status="none", note="Permission/competence conferred on Member States by the Regulation; origin (Union legislature) is the enacting act, not a text position.")
screen("A6.P2", "Yes", "operative-assignment (competence)", na=[n], status="Extracted", note="Specification clause: delegation-like competence to Member States.")
n = na("A6.P3", "(not stated — Union or Member State legislator implied)", "lay down the basis for processing under points (c) and (e) of Art.6(1) by Union law or Member State law; the law must meet an objective of public interest and be proportionate", "legal basis of processing", "rule-making", "obligation", cond="applies to processing under 6(1)(c),(e)", cp_status="none", note="Passive 'shall be laid down by'; the legal basis may contain specific adapting provisions. Legislator not a named position.", flag="subject-unstated")
screen("A6.P3", "Uncertain", "norm-without-named-subject", na=[n], status="Extracted", note="Requirement of a legal basis in Union or Member State law.")
n = na("A6.P4", "controller", "take into account, inter alia, the criteria in points (a)-(e) when ascertaining the compatibility of a further purpose", "compatibility assessment of further processing", "implementation (assessment)", "obligation", cond="further processing not based on consent or on a Union/Member State law that is a necessary and proportionate measure under Art.23(1)", cp_status="none")
screen("A6.P4", "Yes", "operative-assignment", na=[n], status="Extracted", note="Controller's own assessment duty; no counterpart or forum.")

# ---- Article 7
n = na("A7.P1", "controller", "be able to demonstrate that the data subject has consented", "consent evidence", "information provision (demonstration)", "obligation", cond="where processing is based on consent", counterpart="data subject (as the person whose consent is concerned; not a recipient of the demonstration)", cp_status="category-affected-not-recipient")
screen("A7.P1", "Yes", "operative-assignment", na=[n], status="Extracted", note="Demonstration duty; the party to whom the demonstration is owed is not identified.")
q = qr("A7.P2", "controller", "data subject", "information/reporting", "request for consent", "information provision", "obligation", cond="written declaration also concerning other matters", type_note="presentation duty; also beneficiary/protective effect")
screen("A7.P2", "Yes", "relation-bearing", qr=[q], status="Extracted", note="Information duty owed to the data subject. Second sentence: non-binding of infringing parts of a declaration (effect on a legal act, no position).")
q = qr("A7.P3", "controller", "data subject", "beneficiary/protective", "right to withdraw consent (entitlement of counterpart)", "participation/control", "entitlement", deriv="derived", unresolved="obligor (controller) derived from Art.7(1); direction per convention of DECISION_RULES v1.1 (origin = obligor; the first draft had data subject -> controller)")
q2 = qr("A7.P3", "controller", "data subject", "information/reporting", "information on right to withdraw", "information provision", "obligation")
screen("A7.P3", "Yes", "relation-bearing", qr=[q, q2], status="Extracted", note="Entitlement of the data subject (counterpart controller derived) and information duty of the controller.")
screen("A7.P4", "No", "substantive-conduct-rule", status="Not applicable", note="Criterion for assessing 'freely given' consent; no position assignment (assessor not named).")

# ---- Article 8
pd("holder of parental responsibility", "position_type", "A8.P1", note="Category in whose consent/authorization the processing of a child's data depends.")
n = na("A8.P1", "Member States", "provide by law for a lower age (not below 13) for a child's consent in relation to information society services", "age of consent", "rule-making (specification)", "competence", cond="not below 13 years", cp_status="none")
n2 = na("A8.P1", "holder of parental responsibility", "give or authorise consent for a child below 16", "child's consent", "authorization", "competence", cond="child below the age of 16 (or lower national age); offer of information society services directly to a child; Art.6(1)(a) applies", counterpart="controller (implied)", cp_status="implied", deriv="derived", note="Authorization power of a third position; link to the controller derived from the context of consent-based processing.")
screen("A8.P1", "Yes", "operative-assignment (competence); position-referencing", na=[n, n2], pos=["PD-012"], status="Extracted", note="Member State competence to lower the age; role of the holder of parental responsibility.")
n = na("A8.P2", "controller", "make reasonable efforts to verify that consent is given or authorised by the holder of parental responsibility, taking available technology into account", "verification of parental authorization", "verification/assurance (self-performed)", "obligation", counterpart="holder of parental responsibility", cp_status="identified (object of verification, not recipient)")
screen("A8.P2", "Yes", "operative-assignment", na=[n], status="Extracted", note="Controller verification duty (self-verification).")
screen("A8.P3", "No", "scope-context", status="Not applicable", note="Preserves national contract law.")

# ---- Article 9
screen("A9.P1", "No", "substantive-conduct-rule", status="Not applicable", note="Prohibition on processing special categories, stated passively.")
screen("A9.P2", "No", "substantive-conduct-rule (exceptions)", status="Not applicable", note="Ten exceptions; several rely on 'Union or Member State law' as a basis (points b,g,h,i,j) — context for Member State competence in 9(4).")
screen("A9.P3", "No", "substantive-conduct-rule", status="Not applicable", note="Professional-secrecy condition; refers to 'national competent bodies' as sources of secrecy rules (unspecified).")
n = na("A9.P4", "Member States", "maintain or introduce further conditions, including limitations, for processing genetic, biometric or health data", "further conditions on special-category processing", "rule-making (specification)", "competence", cp_status="none")
screen("A9.P4", "Yes", "operative-assignment (competence)", na=[n], status="Extracted", note="Member State competence (second specification clause).")

# ---- Article 10
pd("official authority (controlling processing of criminal-conviction data)", "position_type", "A10.P0", note="'Control of official authority' is a condition on processing; no institution is named or constituted.")
n = na("A10.P0", "(processing subject: controller implied)", "process data on criminal convictions/offences only under the control of official authority or when authorised by Union or Member State law with safeguards; keep any comprehensive register of criminal convictions only under the control of official authority", "processing of criminal-conviction data; comprehensive register", "implementation/oversight condition", "obligation", cp_status="none", note="A register is referred to (not constituted). 'Official authority' is a category, not an identified body; no relation to a named position.", flag="subject-unstated")
screen("A10.P0", "Uncertain", "norm-with-position-reference", na=[n], pos=["PD-013"], status="Extracted", note="Condition of control by official authority: counterpart category unspecific; no QR made.")

# ---- Article 11
n = na("A11.P1", "controller", "is not obliged to maintain, acquire or process additional information to identify the data subject for the sole purpose of complying", "identification information", "implementation (limitation of duty)", "exemption (negative obligation)", cond="purposes do not or no longer require identification", cp_status="none")
q = qr("A11.P2", "controller", "data subject", "information/reporting", "notice of non-identification", "information provision", "obligation", cond="controller able to demonstrate inability to identify; 'if possible'")
screen("A11.P1", "Yes", "operative-assignment", na=[n], status="Extracted", note="Limitation of the controller's duty.")
screen("A11.P2", "Yes", "relation-bearing", qr=[q], status="Extracted", note="Information to data subject; conditional exemption of Arts 15–20 (effect on rights, see Chapter III).")
