from rgam_lib import *

# =============== ANNEX I / II (scope lists) ===============
st("st.ANX1", "ANX1.pt1;ANX1.pt2;ANX1.TBL1;ANX1.TBL2;ANX1.TBL3;ANX1.TBL4;ANX1.TBL5;ANX1.TBL6", "scope",
   "Annex I fixes, by Combined Nomenclature codes under Regulation (EEC) No 2658/87, the goods to which the Regulation applies (cement, electricity, fertilisers, iron and steel, aluminium, hydrogen) and the greenhouse gases relating to each good.",
   "For the purpose of the identification of goods, this Regulation shall apply to goods falling under the Combined Nomenclature")
st("st.ANX2", "ANX2.TBL1;ANX2.TBL2;ANX2.TBL3", "scope",
   "Annex II lists the goods (iron and steel, aluminium, hydrogen) for which only direct emissions are taken into account under Article 7(1).",
   "Chemicals :: CN code | Greenhouse gas ;; 2804 10 00 – Hydrogen | Carbon dioxide")
ext("ext.REG2658", "st.ANX1", "ANX1.pt1", "Council Regulation (EEC) No 2658/87 (tariff and statistical nomenclature and Common Customs Tariff; Combined Nomenclature codes)", "legal_instrument",
    "defines_term", dependents="st.ANX1", dep_kind="specifies", constitutive="Y",
    effect="The CN codes that identify the goods in Annex I are those under the external Regulation; the legal identity of each listed code is undetermined within W beyond the text of Annex I.")
unc("unc.ANX_TABLE_GEOMETRY", "SOURCE_AMBIGUITY", "", "ANX1.TBL4;ANX2.TBL1",
    "The iron and steel tables of Annexes I and II are rendered in the source file with duplicated and merged cell content (the same CN list reappears inside the table), so the table geometry is not faithfully represented as text.",
    "The unit text is kept exactly as parsed from the frozen file; no statement relies on the geometry; the scope statement is coded at the level of the goods category.", "Scope claims about individual CN codes in these two tables are limited to the parsed text.")

# =============== ANNEX IV ===============
st("st.ANX4METH", "ANX4.pt1.P1;ANX4.pt1.pta;ANX4.pt1.ptb;ANX4.pt1.ptc;ANX4.pt1.ptd;ANX4.pt1.pte;ANX4.pt1.ptf;ANX4.pt1.ptg;ANX4.pt2.P1;ANX4.pt2.P3;ANX4.pt2.TBL1;ANX4.pt2.P4;ANX4.pt2.P6;ANX4.pt2.TBL2;ANX4.pt3.P1;ANX4.pt3.P3;ANX4.pt3.TBL3;ANX4.pt3.P5;ANX4.pt3.TBL4;ANX4.pt4.1.P1;ANX4.pt4.2.P1;ANX4.pt4.2.P2;ANX4.pt4.2.1.P1;ANX4.pt4.2.2.P1;ANX4.pt4.2.2.P2;ANX4.pt4.3.P1",
   "procedural",
   "Annex IV states the calculation methods for embedded emissions: definitions; actual specific embedded emissions for simple goods (direct and, where applicable, indirect emissions) and complex goods (attributed emissions and precursors); default values for goods other than electricity (average emission intensity of each exporting country plus a mark-up), for imported electricity (specific and alternative values) and for embedded indirect emissions.",
   "For determining the specific actual embedded emissions of simple goods produced in a given installation, direct and, where applicable, indirect emissions shall be accounted for.")
st("st.ANX4_GUIDANCE", "ANX4.pt4.P1", "assignment_bearing",
   "The Commission shall publish guidance for the approach taken to correct for waste gases or greenhouse gases used as process input before collecting the data required to determine default values; default values are revised periodically through implementing acts under Article 7(7).",
   "The Commission shall publish guidance for the approach taken to correct for waste gases or greenhouse gases used as process input")
st("st.ANX4_3C", "ANX4.pt4.3.P2", "relation_bearing",
   "Where a third country or a group of third countries demonstrates to the Commission, on the basis of reliable data, that the average electricity mix emission factor or the CO2 emission factor of price-setting sources is lower than the default value for indirect emissions, an alternative default value based on that factor shall be established for it.",
   "Where a third country, or a group of third countries, demonstrates to the Commission, on the basis of reliable data")
st("st.ANX4_IMPLACT", "ANX4.pt4.3.P3;ANX4.pt4.3.pt-1;ANX4.pt4.3.pt-2", "assignment_bearing",
   "The Commission shall adopt, no later than 30 June 2025, an implementing act pursuant to Article 7(7) specifying which calculation method for default values of indirect emissions applies, on the basis of the most appropriate way to achieve the prevention of carbon leakage and the environmental integrity of the CBAM.",
   "The Commission shall adopt, no later than 30 June 2025, an implementing act pursuant to Article 7(7)")
st("st.ANX4_ELEC", "ANX4.pt5.P1;ANX4.pt5.pta;ANX4.pt5.ptb;ANX4.pt5.ptc;ANX4.pt5.ptd;ANX4.pt5.pte;ANX4.pt5.P2", "procedural",
   "An authorised CBAM declarant may apply actual embedded emissions instead of default values for imported electricity if five cumulative criteria are met (power purchase agreement with a third-country producer; connection or absence of congestion; emissions not above 550 g CO2 per kWh; firm nomination of interconnection capacity by all responsible transmission system operators for the same period of at most one hour; certification by an accredited verifier receiving at least monthly interim reports).",
   "An authorised CBAM declarant may apply actual embedded emissions instead of default values for the calculation referred to in Article 7(3) if the following cumulative criteria are met:")
st("st.ANX4_IND", "ANX4.pt6.P1", "procedural",
   "An authorised CBAM declarant may apply actual embedded emissions instead of default values for indirect emissions if it can demonstrate a direct technical link between the installation and the electricity generation source or if the operator has concluded a power purchase agreement with a third-country producer for an equivalent amount of electricity.",
   "An authorised CBAM declarant may apply actual embedded emissions instead of default values for the calculation referred to in Article 7(4)")
st("st.ANX4_REGION", "ANX4.pt7.P1;ANX4.pt7.P2", "procedural",
   "Default values can be adapted to particular areas and regions within third countries where specific characteristics prevail; declarants for goods originating in a third country, group of countries or region who demonstrate on reliable data that region-specific adaptations are lower than the default values determined by the Commission may use those adaptations.",
   "Default values can be adapted to particular areas and regions within third countries where specific characteristics prevail in terms of objective emission factors.")
na("na.ANX4_GUIDANCE", "st.ANX4_GUIDANCE", "ANX4.pt4.P1", "pd.COM", "publish guidance for the approach taken to correct for waste gases or greenhouse gases used as process input, before collecting the data required to determine the relevant default values for each type of goods listed in Annex I",
   "guidance on correction for waste gases", "information_provision", "obligation",
   "The Commission shall publish guidance for the approach taken to correct for waste gases or greenhouse gases used as process input",
   mech="guidance", instr="INS-TYPE: guidance", cond="before collecting the data required to determine the relevant default values", nt="N0",
   eff="duty of the Commission to publish guidance", notc="no addressee named; no counterparty created", deriv="direct", deps="pd.COM")
na("na.ANX4_IMPLACT", "st.ANX4_IMPLACT", "ANX4.pt4.3.P3;ANX4.pt4.3.pt-1;ANX4.pt4.3.pt-2", "pd.COM", "adopt, no later than 30 June 2025, an implementing act pursuant to Article 7(7) to further specify which of the calculation methods for default values of indirect emissions applies",
   "implementing act on default values for indirect emissions", "rule_making_standard_setting", "obligation",
   "The Commission shall adopt, no later than 30 June 2025, an implementing act pursuant to Article 7(7)",
   mech="implementing act under the examination procedure (Article 7(7) and Article 29(2))", instr="INS-TYPE: implementing act",
   cond="no later than 30 June 2025; the method is to be determined on the basis of the most appropriate way to achieve the prevention of carbon leakage and ensuring the environmental integrity of the CBAM", nt="N0",
   eff="duty of the Commission to adopt an implementing act by a stated date", notc="adoption of the act is not evidenced in W and is not assessed (layer X); the deadline precedes the 2026-01-01 reference date", deriv="direct", deps="pd.COM",
   epi="documented", unc="unc.ANX4_DEADLINE")
qr("qr.ANX4_3C", "st.ANX4_3C", "ANX4.pt4.3.P2", "pd.3C", "pd.COM", "information_reporting", "third country or group of third countries -> Commission",
   "demonstrate to the Commission, on the basis of reliable data, that the average electricity mix emission factor or the CO2 emission factor of price-setting sources is lower than the default value for indirect emissions, whereupon an alternative default value based on that factor shall be established for the country or group of countries",
   "demonstration of a lower emission factor", "information_provision", "permission",
   "Where a third country, or a group of third countries, demonstrates to the Commission, on the basis of reliable data",
   tnote="the establishment of the alternative default value is stated passively ('shall be established'); the Commission is the recipient of the demonstration and the only default-value setter named in Annex IV",
   mech="demonstration on reliable data", instr="INS-TYPE: reliable data", cond="the average electricity mix emission factor or CO2 emission factor of price-setting sources is lower than the default value for indirect emissions",
   acls="INFO", asuff="sufficient", authattr="permissive for the third country; the Commission's decision on the alternative value is not described as discretionary or bound", discattr="not determinable within W",
   deps="pd.3C;pd.COM", unc="unc.ANX4_PASSIVE")
na("na.ANX4_ELEC_ACTUAL", "st.ANX4_ELEC;st.A7P3", "ANX4.pt5.P1;ANX4.pt5.pta;ANX4.pt5.ptb;ANX4.pt5.ptc;ANX4.pt5.ptd;ANX4.pt5.pte;ANX4.pt5.P2;A7.P3", "pd.ACD",
   "apply actual embedded emissions instead of default values for imported electricity if the cumulative criteria of Annex IV point 5 are met", "actual embedded emissions of imported electricity",
   "implementation", "permission",
   "An authorised CBAM declarant may apply actual embedded emissions instead of default values for the calculation referred to in Article 7(3) if the following cumulative criteria are met:",
   mech="demonstration of five cumulative criteria", instr="INS-TYPE: power purchase agreement; verifier certification",
   cond="five cumulative criteria: power purchase agreement with a third-country producer; connection or absence of congestion; emissions not above 550 grammes of CO2 per kWh; firm nomination of interconnection capacity; certification by an accredited verifier", nt="N3",
   eff="permission of the authorised CBAM declarant to apply actual embedded emissions", notc="the addressee of the demonstration is not named; transmission system operators are mentioned as nominating parties, not as counterparties",
   deriv="derived", drule="A7.P3 allows actual emissions for electricity where the declarant demonstrates that 'the criteria ... listed in point 5 of Annex IV' are met; point 5 lists them (internal cross-reference).",
   deps="pd.ACD", unc="unc.ANX4_ELEC_ADDRESSEE")
qr("qr.ANX4_ELEC_CERT", "st.ANX4_ELEC;st.A7P3", "ANX4.pt5.pte;A7.P3", "pd.ACD", "pd.VERIF", "verification_assurance", "authorised CBAM declarant -> accredited verifier",
   "obtain, as one of the cumulative criteria for applying actual embedded emissions to imported electricity, certification by an accredited verifier that the criteria are fulfilled, the verifier receiving at least monthly interim reports demonstrating how the criteria are fulfilled",
   "certification of fulfilment of the electricity actual-emission criteria", "verification_assurance", "obligation",
   "the fulfilment of the above criteria is certified by an accredited verifier, who shall receive at least monthly interim reports demonstrating how those criteria are fulfilled",
   gdir="accredited verifier -> authorised CBAM declarant's claim (certification)",
   tnote="origin is assigned to the declarant that must meet the criterion; the provision is passive on who supplies the interim reports (see HQ-DIRECTION)", mech="verifier certification; monthly interim reports",
   instr="INS-TYPE: certification; interim report", cond="the declarant applies actual embedded emissions to imported electricity (Article 7(3))", deriv="derived",
   drule="A7.P3 makes the declarant demonstrate that the Annex IV point 5 criteria are met; criterion (e) requires certification by an accredited verifier, who receives interim reports.",
   authattr="the certification is a condition of the declarant's permission to use actual emissions", discattr="verifier's judgement on fulfilment", deps="pd.ACD;pd.VERIF",
   unc="unc.A9_DIRECTION", hq="hq.DIRECTION_A9", ext="ext.REG2018_2067", gap="Accredited-verifier status depends on external accreditation; no verifier is evidenced.")
na("na.ANX4_IND_ACTUAL", "st.ANX4_IND;st.A7P4", "ANX4.pt6.P1;A7.P4", "pd.ACD", "apply actual embedded emissions instead of default values for indirect emissions if it can demonstrate a direct technical link between the installation and the electricity generation source, or that the installation operator has a power purchase agreement with a third-country producer for an equivalent amount of electricity",
   "actual embedded indirect emissions", "implementation", "permission",
   "An authorised CBAM declarant may apply actual embedded emissions instead of default values for the calculation referred to in Article 7(4)",
   mech="demonstration of a direct technical link or a power purchase agreement", instr="INS-TYPE: power purchase agreement", cond="demonstration of a direct technical link, or a power purchase agreement for an equivalent amount of electricity", nt="N3",
   eff="permission of the authorised CBAM declarant to apply actual embedded emissions", notc="the addressee of the demonstration is not named; no counterparty created",
   deriv="derived", drule="A7.P4 allows actual indirect emissions where the declarant demonstrates that 'the criteria ... listed in point 6 of Annex IV' are met; point 6 lists them (internal cross-reference).", deps="pd.ACD", unc="unc.ANX4_ELEC_ADDRESSEE")
na("na.ANX4_REGION", "st.ANX4_REGION", "ANX4.pt7.P2;ANX4.pt7.P1", "pd.ACD", "use region-specific adaptations of default values where it can demonstrate on reliable data that they are lower than the default values determined by the Commission",
   "region-specific default values", "implementation", "permission",
   "Where declarants for goods originating in a third country, a group of third countries or a region within a third country can demonstrate, on the basis of reliable data",
   mech="demonstration on reliable data", instr="INS-TYPE: reliable data", cond="goods originate in a third country, a group of third countries or a region; alternative region-specific adaptations are lower than the default values determined by the Commission", nt="N3",
   eff="permission of declarants to use region-specific adaptations", notc="the addressee of the demonstration is not named; the Annex uses the plural 'declarants' without a defined position other than the authorised CBAM declarant (assumed from the Annex's context)",
   deriv="direct", deps="pd.ACD", unc="unc.ANX4_ELEC_ADDRESSEE")

# =============== ANNEX V ===============
st("st.ANX5REC", "ANX5.pt1;ANX5.pt1.pt1;ANX5.pt1.pt1.pta;ANX5.pt1.pt1.ptb;ANX5.pt1.pt2;ANX5.pt1.pt2.pta;ANX5.pt1.pt2.ptb;ANX5.pt1.pt2.ptc;ANX5.pt2.P1;ANX5.pt2.pta;ANX5.pt2.ptb;ANX5.pt2.ptc;ANX5.pt2.ptd", "procedural",
   "Annex V specifies the minimum data to be kept by the authorised CBAM declarant: identifying data (name, CBAM account number), data on imported goods (type and quantity, country of origin, actual emissions or default values) and, where emissions are determined on actual emissions, installation identification, operator contact information, verification reports and specific embedded emissions.",
   "MINIMUM DATA TO BE KEPT BY AN AUTHORISED CBAM DECLARANT FOR IMPORTED GOODS:")

# =============== ANNEX VI ===============
st("st.ANX6P1", "ANX6.pt1.P1;ANX6.pt1.pta;ANX6.pt1.ptb;ANX6.pt1.ptc;ANX6.pt1.ptd;ANX6.pt1.ptd.sub2", "assignment_bearing",
   "Verification principles: verifiers shall carry out verifications with professional scepticism; declared emissions are considered verified only if the verifier finds with reasonable assurance that the report is free of material misstatements and non-conformities; installation visits are mandatory except where waiver criteria are met; materiality is judged against thresholds set by implementing acts under Article 8(3) or, where none exist, by expert judgement.",
   "verifiers shall carry out verifications with an attitude of professional scepticism")
st("st.ANX6P2", "ANX6.pt2.P1;ANX6.pt2.pta;ANX6.pt2.ptb;ANX6.pt2.ptc;ANX6.pt2.ptd;ANX6.pt2.pte;ANX6.pt2.ptf;ANX6.pt2.ptg;ANX6.pt2.pth;ANX6.pt2.pti;ANX6.pt2.ptj;ANX6.pt2.ptk;ANX6.pt2.ptk.pti;ANX6.pt2.ptk.ptii;ANX6.pt2.ptk.ptiii;ANX6.pt2.ptl;ANX6.pt2.ptm;ANX6.pt2.ptn", "assignment_bearing",
   "The verifier shall prepare a verification report establishing the embedded emissions of the goods and specifying all issues relevant to the work carried out, including at least: installations and operator contact information, reporting period, verifier name and accreditation, installation visits, quantities, direct emissions, attribution, flows not associated with the goods, data for complex goods, the verifier's statement of reasonable assurance, and material misstatements and non-conformities found and corrected.",
   "The verifier shall prepare a verification report establishing the embedded emissions of the goods")
qr("qr.ANX6_PRINC", "st.ANX6P1;st.A8P1", "ANX6.pt1.P1;ANX6.pt1.pta;ANX6.pt1.ptb;ANX6.pt1.ptc;ANX6.pt1.ptd;ANX6.pt1.ptd.sub2;A8.P1;A10.P5.ptb", "pd.VERIF", "pd.ACD", "verification_assurance", "accredited verifier -> authorised CBAM declarant (and operator)",
   "carry out verifications with professional scepticism, regard the total embedded emissions as verified only if the verifier finds with reasonable assurance that the verification report is free of material misstatements and material non-conformities, make installation visits (mandatory except where waiver criteria are met), and judge materiality against thresholds set by implementing acts or, where none are determined, by expert judgement",
   "verification of declared embedded emissions", "verification_assurance", "obligation",
   "verifiers shall carry out verifications with an attitude of professional scepticism",
   extra="pd.OPER", tnote="n-ary: the verified parties are the authorised CBAM declarant (Article 8(1)) and, for registered installations, the operator (Article 10(5)(b))", mech="verification by principles (professional scepticism, reasonable assurance, installation visits, materiality)",
   instr="INS-TYPE: verification report", cond="verification under Article 8 or Article 10(5)(b)", deriv="derived",
   drule="Annex VI states the verifier's duties without naming the verified party; A8.P1 makes the authorised CBAM declarant ensure verification 'based on the verification principles set out in Annex VI' and A10.P5(b) does so for the operator; the verified parties are taken from those cross-references (internal cross-references resolved within W).",
   authattr="verifier's finding determines whether the declared emissions are considered verified", discattr="expert judgement on materiality where no threshold is determined; waiver of installation visits where criteria are met",
   deps="pd.VERIF;pd.ACD;pd.OPER", ext="ext.REG2018_2067", gap="Accredited-verifier status depends on external accreditation; no verifier is evidenced.", unc="unc.A8_DIRECTION")
qr("qr.ANX6_REPORT", "st.ANX6P2;st.A6P2", "ANX6.pt2.P1;ANX6.pt2.pta;ANX6.pt2.ptb;ANX6.pt2.ptc;ANX6.pt2.ptd;ANX6.pt2.pte;ANX6.pt2.ptf;ANX6.pt2.ptg;ANX6.pt2.pth;ANX6.pt2.pti;ANX6.pt2.ptj;ANX6.pt2.ptk;ANX6.pt2.ptk.pti;ANX6.pt2.ptk.ptii;ANX6.pt2.ptk.ptiii;ANX6.pt2.ptl;ANX6.pt2.ptm;ANX6.pt2.ptn;A6.P2.ptd;A8.P1", "pd.VERIF", "pd.ACD", "information_reporting", "accredited verifier -> authorised CBAM declarant (and operator)",
   "prepare a verification report establishing the embedded emissions of the goods and specifying all issues relevant to the work carried out, with at least the information listed in Annex VI point 2",
   "verification report", "verification_assurance", "obligation",
   "The verifier shall prepare a verification report establishing the embedded emissions of the goods",
   extra="pd.OPER", tnote="n-ary: copies of verification reports are included in the declaration of the authorised CBAM declarant (Article 6(2)(d)) and kept by the operator (Article 10(5)(c)); the addressee of the report is not stated in Annex VI itself", mech="verification report",
   instr="INS-TYPE: verification report", cond="verification under Article 8 or Article 10(5)(b)", deriv="derived",
   drule="Annex VI point 2 states the verifier's duty to prepare the report without naming a recipient; A6.P2 point (d) requires the declaration to contain copies of verification reports issued by accredited verifiers, and A8.P1 / A10.P5 tie the verification to the declarant and the operator (internal cross-references resolved within W).",
   acls="INFO", asuff="sufficient", authattr="the report is the verifier's output on which the declaration and the review rely", discattr="content fixed by Annex VI point 2",
   deps="pd.VERIF;pd.ACD;pd.OPER", ext="ext.REG2018_2067", gap="Accredited-verifier status depends on external accreditation; no verifier is evidenced.", unc="unc.A8_DIRECTION")
ext("ext.DIR2019_944", "st.ANX4METH;st.ANX4_ELEC", "ANX4.pt1.ptg;ANX4.pt5.ptd", "Directive (EU) 2019/944, Article 2 point (35) (definition of transmission system operator)", "legal_instrument",
    "defines_term", dependents="", dep_kind="specifies", constitutive="N",
    effect="Defines 'transmission system operator' used in Annex IV; the TSOs appear only as nominating parties inside a criterion and bear no NA or QR in W; no relation depends on the definition for constitution.")
