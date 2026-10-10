from rgam_lib import *

# =============== ARTICLE 5 ===============
st("st.A5P1", "A5.P1", "relation_bearing",
   "Any importer established in a Member State shall, before importing goods, apply for the status of authorised CBAM declarant; where it appoints an indirect customs representative who agrees to act as authorised CBAM declarant, that representative submits the application.",
   "Any importer established in a Member State shall, prior to importing goods into the customs territory of the Union, apply for the status of authorised CBAM declarant")
st("st.A5P2", "A5.P2", "relation_bearing",
   "Where an importer is not established in a Member State, the indirect customs representative shall submit the application for an authorisation.",
   "Where an importer is not established in a Member State, the indirect customs representative shall submit the application for an authorisation.")
st("st.A5P3", "A5.P3", "procedural",
   "The application for an authorisation shall be submitted via the CBAM registry established in accordance with Article 14.",
   "The application for an authorisation shall be submitted via the CBAM registry established in accordance with Article 14.")
st("st.A5P4", "A5.P4;A5.P4.sub2", "position_defining",
   "Where import transmission capacity for electricity is allocated through explicit capacity allocation, the person to whom capacity has been allocated and who nominates it is regarded as an authorised CBAM declarant in the Member State where it declared the importation; the competent authority of the Member State where the customs declaration was lodged registers that person in the CBAM registry.",
   "shall, for the purposes of this Regulation, be regarded as an authorised CBAM declarant in the Member State where the person has declared the importation of electricity in the customs declaration")
st("st.A5P5", "A5.P5;A5.P5.pta;A5.P5.ptb;A5.P5.ptc;A5.P5.ptd;A5.P5.pte;A5.P5.ptf;A5.P5.ptg;A5.P5.pth", "procedural",
   "The application shall include name and contact details, EORI number, main economic activity, a tax-authority certification of no outstanding recovery order, a declaration of honour on infringements, information on financial and operational capacity (with supporting documents if the competent authority so decides on a risk assessment), estimated import value and volume, and details of persons on whose behalf the applicant acts.",
   "The application for an authorisation shall include the following information about the applicant:")
st("st.A5P6", "A5.P6", "assignment_bearing",
   "The applicant may withdraw its application at any time.",
   "The applicant may withdraw its application at any time.")
st("st.A5P7", "A5.P7", "relation_bearing",
   "The authorised CBAM declarant shall inform the competent authority without delay, via the CBAM registry, of any change to the information provided under paragraph 5 that may influence the grant decision or the content of the authorisation.",
   "The authorised CBAM declarant shall inform without delay the competent authority, via the CBAM registry, of any changes to the information provided under paragraph 5 of this Article")
st("st.A5P8", "A5.P8", "assignment_bearing",
   "The Commission is empowered to adopt implementing acts on communications between applicant, competent authority and Commission, the application format and procedures, the competent authority's procedure and deadlines, and the identification of authorised CBAM declarants for electricity imports, under the examination procedure of Article 29(2).",
   "The Commission is empowered to adopt implementing acts on communications between the applicant, the competent authority and the Commission")

qr("qr.A5_APPLY", "st.A5P1;st.A5P2;st.A5P3;st.A5P5", "A5.P1;A5.P2;A5.P3;A5.P5;A5.P5.pta;A5.P5.ptb;A5.P5.ptc;A5.P5.ptd;A5.P5.pte;A5.P5.ptf;A5.P5.ptg;A5.P5.pth;A5.P7;A17.P1",
   "pd.APPL", "pd.CA", "delegation_authorization", "applicant -> competent authority",
   "apply for the status of authorised CBAM declarant before importing goods, submitting via the CBAM registry the information listed in Article 5(5)",
   "authorisation status of authorised CBAM declarant", "authorization_designation*", "obligation",
   "Any importer established in a Member State shall, prior to importing goods into the customs territory of the Union, apply for the status of authorised CBAM declarant",
   gdir="competent authority -> applicant (grant or refusal of the authorisation; see Article 17)",
   tnote="residual function tag (authorization_designation*); the origin position 'applicant' is a role of an importer or, where Article 5(1)-(2) so provides, of its indirect customs representative",
   mech="application lodged through the CBAM registry; competent authority may require supporting documents on the basis of a risk assessment (A5(5)(f))", instr="pd.REGISTRY",
   cond="importer established in a Member State: before importing; where an indirect customs representative is appointed and agrees, it submits the application (A5(1)); where the importer is not established in a Member State the indirect customs representative submits it (A5(2))",
   deriv="derived", drule="The counterparty (competent authority) is identified by explicit cross-reference: A5.P7 refers to the competent authority and to the decision under Article 17; A17.P1 provides that the competent authority of the Member State in which the applicant is established decides on applications submitted in accordance with Article 5; the registry channel is A5.P3.",
   authattr="applicant must apply (binding); the competent authority holds the decisional power under Article 17", discattr="competent authority may require supporting documents on the basis of a risk assessment (A5(5)(f)); otherwise criteria are fixed",
   deps="pd.APPL;pd.CA;pd.REGISTRY", gap="Establishment of the CBAM registry (N2 duty of the Commission, Article 14) and designation of the competent authority (N2, Article 11) are not evidenced; both are expectations, not gates.",
   unc="unc.UCC_ICR", iunits="A17.P1")
na("na.A5P4_DEEM", "st.A5P4", "A5.P4", "pd.ELECNOM", "be regarded, for the purposes of the Regulation, as an authorised CBAM declarant in the Member State where the importation of electricity is declared",
   "status of authorised CBAM declarant for electricity imports under explicit capacity allocation", "authorization_designation*", "declaratory",
   "shall, for the purposes of this Regulation, be regarded as an authorised CBAM declarant in the Member State where the person has declared the importation of electricity in the customs declaration",
   mech="deeming of status by operation of the provision", instr="INS-TYPE: status of authorised CBAM declarant",
   cond="transmission capacity for import of electricity allocated through explicit capacity allocation; the person has nominated that capacity for import; derogation from paragraph 1",
   nt="AMBIGUOUS", eff="status of authorised CBAM declarant (deemed) for the person concerned, as stated; whether this is N1 direct constitution of a status or a deeming outside N1-N4 is not resolved",
   notc="does not constitute the person as an entity; does not state who the status is owed to", deriv="direct", deps="pd.ELECNOM;pd.ACD",
   epi="documented", unc="unc.NT_DEEMING", hq="hq.NORMTYPE_BUNDLE")
qr("qr.A5P4_REG", "st.A5P4", "A5.P4.sub2", "pd.CA", "pd.ELECNOM", "delegation_authorization", "competent authority -> person regarded as authorised CBAM declarant",
   "register the person in the CBAM registry", "registration of the deemed authorised CBAM declarant for electricity imports", "authorization_designation*", "obligation",
   "The competent authority of the Member State in which the customs declaration has been lodged shall register the person in the CBAM registry.",
   tnote="residual function tag; registration rather than a grant decision", mech="registration in the CBAM registry", instr="pd.REGISTRY",
   cond="the person is regarded as authorised CBAM declarant under A5(4) first subparagraph",
   authattr="competent authority registers (ministerial); no discretion stated", discattr="none stated", deps="pd.CA;pd.ELECNOM;pd.REGISTRY",
   gap="Existence of the registry is an expectation (Article 14 N2).")
na("na.A5P6_WITHDRAW", "st.A5P6", "A5.P6", "pd.APPL", "withdraw its application for the status of authorised CBAM declarant", "application for an authorisation", "implementation", "permission",
   "The applicant may withdraw its application at any time.", cond="at any time", cp="", cps="NONE_IDENTIFIABLE", nt="N3",
   eff="competence of the applicant to withdraw its application", notc="the provision names no addressee of the withdrawal; no counterparty is created", deriv="direct", deps="pd.APPL")
qr("qr.A5P7_CHANGE", "st.A5P7", "A5.P7", "pd.ACD", "pd.CA", "information_reporting", "authorised CBAM declarant -> competent authority",
   "inform without delay, via the CBAM registry, of changes to the information provided under Article 5(5) that occurred after the grant decision and that may influence it or the content of the authorisation",
   "changes to application information", "information_provision", "obligation",
   "The authorised CBAM declarant shall inform without delay the competent authority, via the CBAM registry, of any changes to the information provided under paragraph 5 of this Article",
   mech="notification through the CBAM registry", instr="pd.REGISTRY", cond="changes occurred after the decision granting the status under Article 17 and may influence that decision or the authorisation's content",
   authattr="binding duty on the authorised CBAM declarant", discattr="none stated", acls="INFO", asuff="sufficient", deps="pd.ACD;pd.CA;pd.REGISTRY",
   gap="Establishment of the CBAM registry is not evidenced (expectation).")
na("na.A5P8_IMPL", "st.A5P8", "A5.P8", "pd.COM", "adopt implementing acts on communications between applicant, competent authority and Commission, the standard format of the application and procedures to submit it via the CBAM registry, the competent authority's procedure and deadlines, and rules for identification of authorised CBAM declarants for electricity imports",
   "implementing acts on application for an authorisation", "rule_making_standard_setting", "competence",
   "The Commission is empowered to adopt implementing acts on communications between the applicant, the competent authority and the Commission",
   mech="implementing act under the examination procedure (Article 29(2))", instr="INS-TYPE: implementing act", nt="N3",
   eff="competence of the Commission to adopt implementing acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM")

# =============== ARTICLE 6 ===============
st("st.A6P1", "A6.P1", "assignment_bearing",
   "By 31 May each year (first for 2026 in 2027) each authorised CBAM declarant shall use the CBAM registry to submit a CBAM declaration for the preceding calendar year.",
   "each authorised CBAM declarant shall use the CBAM registry referred to in Article 14 to submit a CBAM declaration for the preceding calendar year")
st("st.A6P2", "A6.P2;A6.P2.pta;A6.P2.ptb;A6.P2.ptc;A6.P2.ptd", "procedural",
   "The CBAM declaration shall contain the total quantity of each type of goods imported, the total embedded emissions (calculated under Article 7 and verified under Article 8), the total number of CBAM certificates to be surrendered (after reduction for carbon price paid and adjustment for free allocation) and copies of verification reports.",
   "The CBAM declaration shall contain the following information:")
st("st.A6P3", "A6.P3", "assignment_bearing",
   "Where processed products from inward processing are imported, the authorised CBAM declarant shall report in the declaration the emissions embedded in the goods placed under inward processing, even if the processed products are not Annex I goods; also for returned goods under Article 205 of Regulation (EU) No 952/2013.",
   "the authorised CBAM declarant shall report in the CBAM declaration the emissions embedded in the goods that were placed under the inward processing procedure")
st("st.A6P4", "A6.P4", "assignment_bearing",
   "Where imported Annex I goods are processed products from outward processing, the authorised CBAM declarant shall report only the emissions of the processing operation outside the customs territory.",
   "the authorised CBAM declarant shall report in the CBAM declaration only the emissions of the processing operation undertaken outside the customs territory of the Union")
st("st.A6P5", "A6.P5", "assignment_bearing",
   "Where imported goods are returned goods under Article 203 of Regulation (EU) No 952/2013, the authorised CBAM declarant shall report separately 'zero' total embedded emissions for them.",
   "shall report separately, in the CBAM declaration, ‘zero’ for the total embedded emissions corresponding to those goods")
st("st.A6P6", "A6.P6", "assignment_bearing",
   "The Commission is empowered to adopt implementing acts on the format of the CBAM declaration, the procedure for submitting it via the CBAM registry and the arrangements for surrendering CBAM certificates, under the examination procedure of Article 29(2).",
   "The Commission is empowered to adopt implementing acts concerning the standard format of the CBAM declaration")
na("na.A6_DECL", "st.A6P1;st.A6P2", "A6.P1;A6.P2;A6.P2.pta;A6.P2.ptb;A6.P2.ptc;A6.P2.ptd", "pd.ACD",
   "submit a CBAM declaration for the preceding calendar year by 31 May of each year, via the CBAM registry, containing the total quantity of imported goods, the total embedded emissions, the number of CBAM certificates to be surrendered and copies of verification reports",
   "CBAM declaration", "information_provision", "obligation",
   "each authorised CBAM declarant shall use the CBAM registry referred to in Article 14 to submit a CBAM declaration for the preceding calendar year",
   mech="electronic declaration via the CBAM registry", instr="pd.REGISTRY",
   cond="by 31 May of each year, for the first time in 2027 for the year 2026", cp="", cps="NONE_IDENTIFIABLE", nt="N0",
   eff="duty of the authorised CBAM declarant to submit a declaration",
   notc="the provision does not name the recipient of the declaration; no counterparty is created (later provisions assign review of declarations, see Articles 19 and 22)",
   deriv="direct", deps="pd.ACD;pd.REGISTRY", unc="unc.A6_RECIPIENT")
na("na.A6P3_INWARD", "st.A6P3", "A6.P3", "pd.ACD", "report the emissions embedded in goods placed under the inward processing procedure that resulted in the imported processed products, including where those products are not Annex I goods or are returned goods",
   "reporting scope for inward-processing products", "information_provision", "obligation",
   "the authorised CBAM declarant shall report in the CBAM declaration the emissions embedded in the goods that were placed under the inward processing procedure",
   mech="declaration content rule", instr="INS-TYPE: CBAM declaration", cond="processed products resulting from an inward processing procedure under Article 256 of Regulation (EU) No 952/2013 are imported",
   nt="N0", eff="duty specifying declaration content", notc="no counterparty identified", deriv="direct", deps="pd.ACD", unc="unc.A6_RECIPIENT")
na("na.A6P4_OUTWARD", "st.A6P4", "A6.P4", "pd.ACD", "report only the emissions of the processing operation undertaken outside the customs territory of the Union for outward-processing products",
   "reporting scope for outward-processing products", "information_provision", "obligation",
   "the authorised CBAM declarant shall report in the CBAM declaration only the emissions of the processing operation undertaken outside the customs territory of the Union",
   mech="declaration content rule", instr="INS-TYPE: CBAM declaration", cond="imported Annex I goods are processed products from an outward processing procedure under Article 259 of Regulation (EU) No 952/2013",
   nt="N0", eff="duty specifying declaration content", notc="no counterparty identified", deriv="direct", deps="pd.ACD", unc="unc.A6_RECIPIENT")
na("na.A6P5_RETURNED", "st.A6P5", "A6.P5", "pd.ACD", "report separately 'zero' total embedded emissions for returned goods",
   "reporting scope for returned goods", "information_provision", "obligation",
   "shall report separately, in the CBAM declaration, ‘zero’ for the total embedded emissions corresponding to those goods",
   mech="declaration content rule", instr="INS-TYPE: CBAM declaration", cond="imported goods are returned goods as referred to in Article 203 of Regulation (EU) No 952/2013",
   nt="N0", eff="duty specifying declaration content", notc="no counterparty identified", deriv="direct", deps="pd.ACD", unc="unc.A6_RECIPIENT")
na("na.A6P6_IMPL", "st.A6P6", "A6.P6", "pd.COM", "adopt implementing acts on the standard format of the CBAM declaration, the procedure for submitting it via the CBAM registry and the arrangements for surrendering CBAM certificates",
   "implementing acts on the CBAM declaration", "rule_making_standard_setting", "competence",
   "The Commission is empowered to adopt implementing acts concerning the standard format of the CBAM declaration",
   mech="implementing act under the examination procedure (Article 29(2))", instr="INS-TYPE: implementing act", nt="N3",
   eff="competence of the Commission to adopt implementing acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM")
ext("ext.UCC_PROCESSING", "st.A6P3;st.A6P4;st.A6P5", "A6.P3;A6.P4;A6.P5;A34.P1;A34.P2;A34.P2.pta;A34.P2.ptb", "Regulation (EU) No 952/2013 (Union Customs Code): Art. 256 (inward processing), Art. 205 (returned goods), Art. 259 (outward processing), Art. 203 (returned goods)", "legal_instrument",
    "defines_term", dependents="na.A6P3_INWARD;na.A6P4_OUTWARD;na.A6P5_RETURNED", dep_kind="conditions", constitutive="Y",
    effect="The customs procedures that trigger the special reporting rules are defined externally; the applicability conditions of these duties are undetermined within W.")

# =============== ARTICLE 7 ===============
st("st.A7P1", "A7.P1", "procedural",
   "Embedded emissions in goods are calculated pursuant to the methods in Annex IV; for Annex II goods only direct emissions are calculated and taken into account.",
   "Embedded emissions in goods shall be calculated pursuant to the methods set out in Annex IV.")
st("st.A7P2", "A7.P2", "procedural",
   "Embedded emissions in goods other than electricity are based on actual emissions (Annex IV points 2 and 3), or on default values (point 4.1) where actual emissions cannot be adequately determined and for indirect emissions.",
   "Embedded emissions in goods other than electricity shall be determined based on the actual emissions")
st("st.A7P3", "A7.P3", "procedural",
   "Embedded emissions in imported electricity are determined by default values (Annex IV point 4.2) unless the authorised CBAM declarant demonstrates that the actual-emission criteria of Annex IV point 5 are met.",
   "unless the authorised CBAM declarant demonstrates that the criteria to determine the embedded emissions based on the actual emissions listed in point 5 of Annex IV are met")
st("st.A7P4", "A7.P4", "procedural",
   "Embedded indirect emissions are calculated by the method of Annex IV point 4.3 and the implementing acts under paragraph 7, unless the authorised CBAM declarant demonstrates that the criteria of Annex IV point 6 are met.",
   "Embedded indirect emissions shall be calculated in accordance with the method set out in point 4.3 of Annex IV")
st("st.A7P5", "A7.P5;A7.P6", "assignment_bearing",
   "The authorised CBAM declarant shall keep records of the information required to calculate embedded emissions (Annex V), sufficiently detailed to enable accredited verifiers to verify and the Commission and the competent authority to review the CBAM declaration, until the end of the fourth year after the year in which the declaration was or should have been submitted.",
   "The authorised CBAM declarant shall keep records of the information required to calculate the embedded emissions in accordance with the requirements laid down in Annex V.")
st("st.A7P7", "A7.P7;A7.P7.pta;A7.P7.ptb;A7.P7.sub2", "assignment_bearing",
   "The Commission is empowered to adopt implementing acts on the application of the Annex IV calculation methods (system boundaries, precursors, emission factors, default values and their verification; simple and complex goods; conditions for inadequate actual emissions; evidence for actual electricity emissions) and on indirect-emission methods; default values may be adapted to areas, regions or countries; acts build on existing legislation for EU ETS installations, in particular Implementing Regulation (EU) 2018/2066, Implementing Regulation (EU) 2018/2067 and Delegated Regulation (EU) 2019/331; examination procedure of Article 29(2).",
   "The Commission is empowered to adopt implementing acts concerning:")
na("na.A7_METHOD", "st.A6P2;st.A7P1;st.A7P2;st.A7P3;st.A7P4;st.ANX4METH", "A6.P2.ptb;A7.P1;A7.P2;A7.P3;A7.P4", "pd.ACD",
   "determine the embedded emissions of declared goods in accordance with Annex IV: on actual emissions for goods other than electricity, on default values where actual emissions cannot be adequately determined and for indirect emissions, on default values for imported electricity unless the actual-emission criteria are demonstrated",
   "embedded emissions of declared goods", "information_provision", "obligation",
   "Embedded emissions in goods shall be calculated pursuant to the methods set out in Annex IV.",
   mech="calculation by the Annex IV methods; default values; demonstration of criteria", instr="INS-TYPE: calculation method (Annex IV); default value",
   cond="actual emissions cannot be adequately determined, and indirect emissions: default values (A7(2)); electricity: default unless the Annex IV point 5 criteria are demonstrated (A7(3)); indirect emissions: Annex IV point 4.3 unless the point 6 criteria are demonstrated (A7(4))",
   nt="N0", eff="duty on the authorised CBAM declarant to determine embedded emissions by the stated methods", notc="the provisions of Article 7(1)-(4) are impersonal; the obligated position is identified through Article 6(2)(b)",
   deriv="derived", drule="A7.P1-P4 state the calculation rules impersonally; A6.P2 point (b) requires the CBAM declaration of the authorised CBAM declarant to contain total embedded emissions 'calculated in accordance with Article 7'; the subject is therefore the authorised CBAM declarant.",
   deps="pd.ACD", iunits="ANX4.pt1;ANX4.pt2;ANX4.pt3;ANX4.pt4;ANX4.pt5;ANX4.pt6;ANX4.pt7")
na("na.A7_RECORDS", "st.A7P5;st.ANX5REC", "A7.P5;A7.P6;ANX5.pt1;ANX5.pt1.pt1;ANX5.pt1.pt1.pta;ANX5.pt1.pt1.ptb;ANX5.pt1.pt2;ANX5.pt1.pt2.pta;ANX5.pt1.pt2.ptb;ANX5.pt1.pt2.ptc;ANX5.pt2.P1;ANX5.pt2.pta;ANX5.pt2.ptb;ANX5.pt2.ptc;ANX5.pt2.ptd", "pd.ACD",
   "keep records of the information required to calculate embedded emissions (Annex V minimum data), including the verifier's report, until the end of the fourth year after the year in which the CBAM declaration was or should have been submitted",
   "records of calculation information", "information_provision", "obligation",
   "The authorised CBAM declarant shall keep records of the information required to calculate the embedded emissions in accordance with the requirements laid down in Annex V.",
   mech="record-keeping in line with Annex V; retention period", instr="INS-TYPE: records; verification report", cond="records sufficiently detailed to enable verifiers accredited pursuant to Article 18 to verify and the Commission and the competent authority to review the declaration (purposive clause)",
   nt="N0", eff="duty of the authorised CBAM declarant to keep records",
   notc="the provision names verifiers, the Commission and the competent authority as those whom the records are to enable, not as addressees of a communication; no counterparty is created",
   deriv="direct", deps="pd.ACD", unc="unc.A7P5_PURPOSIVE")
na("na.A7P7_IMPL", "st.A7P7", "A7.P7;A7.P7.pta;A7.P7.ptb;A7.P7.sub2", "pd.COM",
   "adopt implementing acts on the application of the Annex IV calculation methods, default values, evidence for actual electricity emissions and indirect-emission methods, building on existing EU ETS monitoring and verification legislation",
   "implementing acts on calculation methods", "rule_making_standard_setting", "competence",
   "The Commission is empowered to adopt implementing acts concerning:",
   mech="implementing act under the examination procedure (Article 29(2)); may provide for adaptation of default values to areas, regions or countries", instr="INS-TYPE: implementing act",
   nt="N3", eff="competence of the Commission to adopt implementing acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM", unc="unc.XREF_BUNDLE", hq="hq.XREF_BUNDLE")
ext("ext.REG2018_2066", "st.A7P7", "A7.P7.sub2", "Commission Implementing Regulation (EU) 2018/2066 (monitoring and reporting of greenhouse gas emissions under Directive 2003/87/EC)", "legal_instrument",
    "supplies_rule_or_standard", dependents="na.A7P7_IMPL", dep_kind="specifies", constitutive="N",
    effect="Existing legislation on which the implementing acts under Article 7(7) are to build; its content is not in W; no relation of W depends on it for constitution.")
ext("ext.DELREG2019_331", "st.A7P7", "A7.P7.sub2", "Commission Delegated Regulation (EU) 2019/331 (transitional Union-wide rules for harmonised free allocation under Article 10a of Directive 2003/87/EC)", "legal_instrument",
    "supplies_rule_or_standard", dependents="na.A7P7_IMPL", dep_kind="specifies", constitutive="N",
    effect="Existing legislation on which the implementing acts under Article 7(7) are to build; no relation of W depends on it for constitution.")

# =============== ARTICLE 8 ===============
st("st.A8P1", "A8.P1", "relation_bearing",
   "The authorised CBAM declarant shall ensure that the total embedded emissions declared in the CBAM declaration are verified by a verifier accredited pursuant to Article 18, based on the verification principles of Annex VI.",
   "The authorised CBAM declarant shall ensure that the total embedded emissions declared in the CBAM declaration submitted pursuant to Article 6 are verified by a verifier accredited pursuant to Article 18")
st("st.A8P2", "A8.P2", "relation_bearing",
   "For goods produced in installations in a third country registered under Article 10, the authorised CBAM declarant may choose to use verified information disclosed to it under Article 10(7) to fulfil the verification obligation of paragraph 1.",
   "the authorised CBAM declarant may choose to use verified information disclosed to it in accordance with Article 10(7) to fulfil the obligation referred to in paragraph 1 of this Article")
st("st.A8P3", "A8.P3;A8.P3.pta;A8.P3.ptb;A8.P3.ptc;A8.P3.sub2", "assignment_bearing",
   "The Commission is empowered to adopt implementing acts on the application of the Annex VI verification principles (waiver of the installation visit, materiality thresholds, supporting documentation and format), seeking equivalence and coherence with Implementing Regulation (EU) 2018/2067, under the examination procedure of Article 29(2).",
   "The Commission is empowered to adopt implementing acts for the application of the verification principles set out in Annex VI as regards:")
qr("qr.A8_ENSURE", "st.A8P1", "A8.P1;A6.P2.ptb", "pd.ACD", "pd.VERIF", "verification_assurance", "authorised CBAM declarant -> accredited verifier",
   "ensure that the total embedded emissions declared in the CBAM declaration are verified by an accredited verifier on the basis of the Annex VI verification principles",
   "declared embedded emissions", "verification_assurance", "obligation",
   "The authorised CBAM declarant shall ensure that the total embedded emissions declared in the CBAM declaration submitted pursuant to Article 6 are verified by a verifier accredited pursuant to Article 18",
   gdir="accredited verifier -> authorised CBAM declarant (assurance on the declared emissions)",
   tnote="textual direction follows the obligor (the declarant must ensure verification); governance direction is the verifier's assurance work towards the declarant's declaration",
   mech="third-party verification under Annex VI principles; verification report", instr="INS-TYPE: verification report (Annex VI)",
   cond="total embedded emissions declared in the CBAM declaration submitted pursuant to Article 6",
   authattr="binding duty on the authorised CBAM declarant; verifier's capacity set by accreditation (Article 18)", discattr="verifier judgment: materiality thresholds (Annex VI) and expert judgement where no threshold is set",
   deps="pd.ACD;pd.VERIF", gap="Accredited-verifier status depends on external accreditation (Implementing Regulation (EU) 2018/2067, Article 18); no verifier instance is evidenced.",
   unc="unc.A8_DIRECTION", ext="ext.REG2018_2067", iunits="")
qr("qr.A8_USE", "st.A8P2;st.A10P7", "A8.P2;A10.P7", "pd.ACD", "pd.OPER", "verification_assurance", "authorised CBAM declarant -> operator (as source of verified information)",
   "choose to use verified information disclosed by the operator of a registered installation to fulfil the verification obligation of Article 8(1)",
   "verified embedded-emission information disclosed by an operator", "verification_assurance", "permission",
   "the authorised CBAM declarant may choose to use verified information disclosed to it in accordance with Article 10(7) to fulfil the obligation referred to in paragraph 1 of this Article",
   mech="use of operator-verified information in place of own verification arrangement", instr="INS-TYPE: verification report",
   cond="goods produced in installations in a third country registered in accordance with Article 10; information disclosed under Article 10(7)",
   deriv="derived", drule="A8.P2 names the declarant's choice and refers to information disclosed under A10.P7; A10.P7 second sentence states the declarant's entitlement to use the disclosed information in order to fulfil the obligation of Article 8; the operator is the discloser identified in A10.P7.",
   authattr="permission of the declarant; no operator obligation to disclose (A10(7) 'may')", discattr="declarant choice", deps="pd.ACD;pd.OPER",
   gap="Registration of any operator in the CBAM registry (Article 10) is not evidenced in W.")
na("na.A8P3_IMPL", "st.A8P3", "A8.P3;A8.P3.pta;A8.P3.ptb;A8.P3.ptc;A8.P3.sub2", "pd.COM",
   "adopt implementing acts on the application of the Annex VI verification principles (waiver of installation visit, materiality thresholds, supporting documentation and format), seeking equivalence and coherence with the procedures of Implementing Regulation (EU) 2018/2067",
   "implementing acts on verification", "rule_making_standard_setting", "competence",
   "The Commission is empowered to adopt implementing acts for the application of the verification principles set out in Annex VI as regards:",
   mech="implementing act under the examination procedure (Article 29(2))", instr="INS-TYPE: implementing act",
   nt="N3", eff="competence of the Commission to adopt implementing acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM", ext="")
ext("ext.REG2018_2067", "st.A8P3;st.A18P1", "A8.P3.sub2;A18.P1;A7.P7.sub2", "Commission Implementing Regulation (EU) 2018/2067 (verification of data and accreditation of verifiers under Directive 2003/87/EC), including its Annex I (groups of activities)", "legal_instrument",
    "constitutes_position", dependents="pd.VERIF;qr.A8_ENSURE", dep_kind="constitutes", constitutive="Y",
    effect="The status of 'accredited verifier' for the purposes of this Regulation arises from accreditation under the external Regulation (A18.P1); verifier existence, qualifications and the accreditation process are undetermined within W; claims about the verification relation are limited to W's text.")

# =============== ARTICLE 9 ===============
st("st.A9P1", "A9.P1", "assignment_bearing",
   "An authorised CBAM declarant may claim in the CBAM declaration a reduction in the number of CBAM certificates to be surrendered for the carbon price paid in the country of origin, only if the carbon price was effectively paid, taking into account any rebate or other compensation.",
   "An authorised CBAM declarant may claim in the CBAM declaration a reduction in the number of CBAM certificates to be surrendered")
st("st.A9P2", "A9.P2;A9.P3", "relation_bearing",
   "The authorised CBAM declarant shall keep records of the documentation demonstrating that the declared embedded emissions were subject to a carbon price effectively paid in the country of origin (including rebate evidence and proof of payment), the information to be certified by a person independent from the declarant and from the authorities of the country of origin, until the end of the fourth year after the year of the declaration.",
   "The authorised CBAM declarant shall keep records of the documentation required to demonstrate that the declared embedded emissions were subject to a carbon price in the country of origin")
st("st.A9P4", "A9.P4", "assignment_bearing",
   "The Commission is empowered to adopt implementing acts on the conversion of the yearly average carbon price effectively paid into a reduction of certificates, evidence of payment, examples of rebates, qualifications and independence of the independent person, under the examination procedure of Article 29(2).",
   "The Commission is empowered to adopt implementing acts concerning the conversion of the yearly average carbon price effectively paid")
na("na.A9_REDUCTION", "st.A9P1", "A9.P1", "pd.ACD", "claim in the CBAM declaration a reduction in the number of CBAM certificates to be surrendered for the carbon price effectively paid in the country of origin for the declared embedded emissions",
   "reduction in certificates for carbon price paid abroad", "implementation", "permission",
   "An authorised CBAM declarant may claim in the CBAM declaration a reduction in the number of CBAM certificates to be surrendered",
   mech="claim within the CBAM declaration", instr="INS-TYPE: CBAM declaration",
   cond="the reduction may be claimed only if the carbon price has been effectively paid in the country of origin; any rebate or compensation that would have reduced that price is taken into account",
   nt="N3", eff="competence/permission of the authorised CBAM declarant to claim the reduction", notc="the provision names no addressee of the claim", deriv="direct", deps="pd.ACD", unc="unc.A6_RECIPIENT")
na("na.A9_RECORDS", "st.A9P2", "A9.P2;A9.P3", "pd.ACD", "keep records of the documentation demonstrating that the declared embedded emissions were subject to a carbon price effectively paid in the country of origin, evidence of rebates and of actual payment, until the end of the fourth year after the year of the declaration",
   "records on carbon price paid abroad", "information_provision", "obligation",
   "The authorised CBAM declarant shall keep records of the documentation required to demonstrate that the declared embedded emissions were subject to a carbon price in the country of origin of the goods that has been effectively paid",
   mech="record-keeping; independent certification of the documentation", instr="INS-TYPE: records; certified documentation",
   cond="retention until the end of the fourth year after the year during which the CBAM declaration has been or should have been submitted",
   nt="N0", eff="duty of the authorised CBAM declarant to keep records", notc="no counterparty created for the record-keeping itself", deriv="direct", deps="pd.ACD")
qr("qr.A9_CERT", "st.A9P2", "A9.P2", "pd.ACD", "pd.INDEP", "verification_assurance", "authorised CBAM declarant -> independent person (certifier)",
   "have the information in the carbon-price documentation certified by a person independent from the authorised CBAM declarant and from the authorities of the country of origin, whose name and contact information appear on the documentation",
   "carbon-price documentation", "verification_assurance", "obligation",
   "The information contained in that documentation shall be certified by a person that is independent from the authorised CBAM declarant and from the authorities of the country of origin.",
   gdir="independent person -> documentation of the authorised CBAM declarant (certification)",
   tnote="the sentence is passive: the obligor to obtain certification is not stated; origin is assigned to the paragraph's grammatical subject (the declarant)",
   mech="independent certification", instr="INS-TYPE: certified documentation", cond="documentation demonstrating carbon price effectively paid (Article 9(1)-(2))",
   authattr="certification by an independent third party; qualifications and independence conditions to be set by implementing acts (A9(4))", discattr="none stated",
   deps="pd.ACD;pd.INDEP", unc="unc.A9_DIRECTION", hq="hq.DIRECTION_A9", gap="No independent person is identified; type-level position only.")
na("na.A9P4_IMPL", "st.A9P4", "A9.P4", "pd.COM", "adopt implementing acts on the conversion of the yearly average carbon price effectively paid into a certificate reduction, evidence of payment, examples of rebates, and the qualifications and independence of the independent person",
   "implementing acts on carbon price reduction", "rule_making_standard_setting", "competence",
   "The Commission is empowered to adopt implementing acts concerning the conversion of the yearly average carbon price effectively paid",
   mech="implementing act under the examination procedure (Article 29(2))", instr="INS-TYPE: implementing act", nt="N3",
   eff="competence of the Commission to adopt implementing acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM")

# =============== ARTICLE 10 ===============
st("st.A10P1", "A10.P1;A10.P2;A10.P2.pta;A10.P2.ptb;A10.P2.ptc;A10.P3", "relation_bearing",
   "The Commission shall, upon request by an operator of an installation in a third country, register the information on that operator and its installation (name and contact, location with coordinates, main economic activity) in the CBAM registry, notify the operator of the registration, which is valid for five years from notification.",
   "The Commission shall, upon request by an operator of an installation located in a third country, register the information on that operator and on its installation in the CBAM registry")
st("st.A10P4", "A10.P4", "relation_bearing",
   "The operator shall inform the Commission without delay of changes in the registered information, and the Commission shall update the CBAM registry.",
   "The operator shall inform the Commission without delay of any changes in the information referred to in paragraph 2 arising after the registration")
st("st.A10P5", "A10.P5;A10.P5.pta;A10.P5.ptb;A10.P5.ptc;A10.P6", "assignment_bearing",
   "The operator shall determine the embedded emissions by type of goods under Annex IV, ensure verification by an accredited verifier under Annex VI, and keep a copy of the verification report and records of calculation information for four years, sufficiently detailed to enable verification and the review of a CBAM declaration of an authorised CBAM declarant to whom the information was disclosed.",
   "determine the embedded emissions calculated in accordance with the methods set out in Annex IV, by type of goods produced at the installation")
st("st.A10P7", "A10.P7", "relation_bearing",
   "An operator may disclose the information on the verification of embedded emissions to an authorised CBAM declarant, which is entitled to use that information to fulfil the obligation of Article 8.",
   "An operator may disclose the information on the verification of embedded emissions referred to in paragraph 5 of this Article to an authorised CBAM declarant.")
st("st.A10P8", "A10.P8", "relation_bearing",
   "The operator may at any time ask to be deregistered; the Commission shall, on request and after notifying the competent authorities, deregister the operator and delete the information unless needed to review submitted CBAM declarations; the Commission may also deregister after giving the operator the possibility to be heard and consulting the competent authorities if the information is no longer accurate; and it informs the competent authorities of deregistrations.",
   "The operator may, at any time, ask to be deregistered from the CBAM registry.")
qr("qr.A10_REGISTER", "st.A10P1", "A10.P1;A10.P2;A10.P2.pta;A10.P2.ptb;A10.P2.ptc", "pd.COM", "pd.OPER", "delegation_authorization", "Commission -> operator",
   "register the information on the operator and on its installation in the CBAM registry upon the operator's request, on the basis of a request containing name, address and contact information, installation location with six-decimal coordinates and main economic activity",
   "registration of operators and installations", "authorization_designation*", "obligation",
   "The Commission shall, upon request by an operator of an installation located in a third country, register the information on that operator and on its installation in the CBAM registry",
   tnote="residual function tag; registration upon request, nearest relation type delegation_authorization",
   mech="registration in the CBAM registry on request", instr="pd.REGISTRY", cond="request by an operator of an installation located in a third country",
   authattr="Commission registers on request; registration confers the possibility to disclose verified information (A10(7))", discattr="none stated for the registration itself",
   deps="pd.COM;pd.OPER;pd.REGISTRY", gap="Establishment of the CBAM registry (Article 14) and any operator's existence are not evidenced.")
qr("qr.A10_NOTIFY", "st.A10P1", "A10.P3", "pd.COM", "pd.OPER", "information_reporting", "Commission -> operator",
   "notify the operator of the registration in the CBAM registry; the registration is valid for five years from notification",
   "notification of registration", "information_provision", "obligation",
   "The Commission shall notify the operator of the registration in the CBAM registry. The registration shall be valid for a period of five years from the date of its notification to the operator of the installation.",
   mech="notification", instr="", cond="registration made under Article 10(1)", acls="INFO", asuff="sufficient",
   authattr="Commission notification fixes the start of the five-year validity", discattr="none stated", deps="pd.COM;pd.OPER;pd.REGISTRY")
qr("qr.A10_CHANGE", "st.A10P4", "A10.P4", "pd.OPER", "pd.COM", "information_reporting", "operator -> Commission",
   "inform the Commission without delay of changes in the registered information", "changes in registered operator and installation information",
   "information_provision", "obligation",
   "The operator shall inform the Commission without delay of any changes in the information referred to in paragraph 2 arising after the registration",
   mech="notification", cond="changes arising after the registration", acls="INFO", asuff="sufficient",
   authattr="binding duty on the operator", discattr="none stated", deps="pd.OPER;pd.COM")
na("na.A10P4_UPDATE", "st.A10P4", "A10.P4", "pd.COM", "update the relevant information in the CBAM registry following the operator's notification of changes", "registered operator and installation information",
   "implementation", "obligation", "and the Commission shall update the relevant information in the CBAM registry",
   mech="registry update", instr="pd.REGISTRY", cond="the operator has informed the Commission of changes", nt="N0",
   eff="duty of the Commission to update the registry", notc="the update is an act on the registry, not a relation with a further party", deriv="direct", deps="pd.COM;pd.REGISTRY")
na("na.A10_OPER_DETERMINE", "st.A10P5", "A10.P5;A10.P5.pta", "pd.OPER", "determine the embedded emissions, calculated in accordance with the methods of Annex IV, by type of goods produced at the registered installation",
   "embedded emissions by type of goods", "information_provision", "obligation",
   "determine the embedded emissions calculated in accordance with the methods set out in Annex IV, by type of goods produced at the installation",
   mech="calculation by the Annex IV methods", instr="INS-TYPE: calculation method (Annex IV)", cond="operator registered under Article 10(1)",
   nt="N0", eff="duty of the operator to determine embedded emissions", notc="no counterparty named in the point", deriv="direct", deps="pd.OPER")
qr("qr.A10_VERIFY", "st.A10P5", "A10.P5;A10.P5.ptb", "pd.OPER", "pd.VERIF", "verification_assurance", "operator -> accredited verifier",
   "ensure that the embedded emissions determined are verified in accordance with the Annex VI verification principles by a verifier accredited pursuant to Article 18",
   "operator-determined embedded emissions", "verification_assurance", "obligation",
   "ensure that the embedded emissions referred to in point (a) of this paragraph are verified in accordance with the verification principles set out in Annex VI by a verifier accredited pursuant to Article 18",
   gdir="accredited verifier -> operator's determination of embedded emissions (assurance)", tnote="textual direction follows the obligor (the operator ensures verification)",
   mech="third-party verification under Annex VI principles", instr="INS-TYPE: verification report (Annex VI)", cond="operator registered under Article 10(1)",
   authattr="binding duty on the operator", discattr="verifier judgment under Annex VI", deps="pd.OPER;pd.VERIF", ext="ext.REG2018_2067",
   gap="Accredited-verifier status depends on external accreditation; no verifier instance is evidenced.")
na("na.A10_RECORDS", "st.A10P5", "A10.P5;A10.P5.ptc;A10.P6", "pd.OPER", "keep a copy of the verification report and records of the information required to calculate embedded emissions (Annex V requirements) for four years after the verification, sufficiently detailed to enable verification and the review of the CBAM declaration of an authorised CBAM declarant to whom the information was disclosed",
   "records and verification report", "information_provision", "obligation",
   "keep a copy of the verification report as well as records of the information required to calculate the embedded emissions in goods in accordance with the requirements laid down in Annex V for a period of four years after the verification has been performed",
   mech="record-keeping", instr="INS-TYPE: records; verification report", cond="operator registered under Article 10(1); retention period of four years",
   nt="N0", eff="duty of the operator to keep records", notc="beneficiaries of the detail requirement are named only purposively; no counterparty created", deriv="direct", deps="pd.OPER", unc="unc.A7P5_PURPOSIVE")
qr("qr.A10_DISCLOSE", "st.A10P7", "A10.P7", "pd.OPER", "pd.ACD", "information_reporting", "operator -> authorised CBAM declarant",
   "disclose the information on the verification of embedded emissions to an authorised CBAM declarant, which is entitled to use it to fulfil the obligation of Article 8",
   "verification information on embedded emissions", "information_provision", "permission",
   "An operator may disclose the information on the verification of embedded emissions referred to in paragraph 5 of this Article to an authorised CBAM declarant.",
   mech="voluntary disclosure", instr="INS-TYPE: verification report", cond="operator registered; verification information as referred to in Article 10(5)",
   authattr="permission of the operator (no duty to disclose)", discattr="operator decides whether to disclose", acls="INFO", asuff="sufficient", deps="pd.OPER;pd.ACD",
   gap="No registered operator is evidenced.")
qr("qr.A10_DEREG_REQ", "st.A10P8", "A10.P8", "pd.COM", "pd.OPER", "delegation_authorization", "Commission -> operator",
   "deregister the operator upon its request and delete the information on the operator and installation from the CBAM registry, provided the information is not necessary for the review of submitted CBAM declarations",
   "deregistration of operators", "authorization_designation*", "obligation",
   "The Commission shall, upon such request, and after notifying the competent authorities, deregister the operator and delete the information on that operator and on its installation from the CBAM registry",
   tnote="residual function tag; withdrawal of registration", mech="deregistration on request", instr="pd.REGISTRY",
   cond="the operator asks to be deregistered (A10(8) first sentence); the Commission has notified the competent authorities; the information is not necessary for the review of CBAM declarations already submitted",
   authattr="Commission must deregister on request subject to the review exception", discattr="none stated beyond the review exception", deps="pd.COM;pd.OPER;pd.REGISTRY")
qr("qr.A10_DEREG_INACC", "st.A10P8", "A10.P8", "pd.COM", "pd.OPER", "delegation_authorization", "Commission -> operator",
   "deregister the information on the operator if the Commission finds that it is no longer accurate, after giving the operator the possibility to be heard and consulting the relevant competent authorities",
   "deregistration of operators on inaccuracy", "authorization_designation*", "permission",
   "The Commission may, after having given the operator concerned the possibility to be heard and having consulted with the relevant competent authorities, also deregister the information if the Commission finds that the information on that operator is no longer accurate.",
   tnote="residual function tag; withdrawal of registration at the Commission's initiative", mech="deregistration after hearing and consultation", instr="pd.REGISTRY",
   cond="the Commission finds that the information on the operator is no longer accurate; operator heard; relevant competent authorities consulted",
   authattr="Commission may deregister (discretionary competence)", discattr="'may'; accuracy finding by the Commission", deps="pd.COM;pd.OPER;pd.REGISTRY")
qr("qr.A10_DEREG_CA", "st.A10P8", "A10.P8", "pd.COM", "pd.CA", "information_reporting", "Commission -> competent authorities",
   "notify the competent authorities before deregistering an operator on request, consult the relevant competent authorities before deregistering for inaccuracy, and inform the competent authorities of such deregistrations",
   "deregistration of operators", "cooperation_coordination*", "obligation",
   "The Commission shall inform the competent authorities of such deregistrations.",
   tnote="residual function tag; combines notification, consultation and subsequent information of the competent authorities", mech="notification and consultation", instr="",
   cond="deregistration of an operator under Article 10(8)", acls="INFO", asuff="sufficient", authattr="Commission duty towards competent authorities", discattr="none stated",
   deps="pd.COM;pd.CA", unc="unc.A10_CA_MULTI")
