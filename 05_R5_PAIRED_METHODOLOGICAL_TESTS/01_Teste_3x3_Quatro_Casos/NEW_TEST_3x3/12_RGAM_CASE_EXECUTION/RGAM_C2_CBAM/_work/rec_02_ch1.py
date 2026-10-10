from rgam_lib import *

# =============== ARTICLE 1 ===============
st("st.A1P1", "A1.P1", "scope",
   "The Regulation establishes the CBAM to address greenhouse gas emissions embedded in Annex I goods on importation into the customs territory of the Union, to prevent carbon leakage.",
   "to address greenhouse gas emissions embedded in the goods listed in Annex I on their importation into the customs territory of the Union in order to prevent the risk of carbon leakage")
st("st.A1P2", "A1.P2", "external_referencing",
   "The CBAM complements the EU ETS established under Directive 2003/87/EC by applying an equivalent set of rules to imports of the goods referred to in Article 2.",
   "The CBAM complements the system for greenhouse gas emission allowance trading within the Union established under Directive 2003/87/EC")
st("st.A1P3", "A1.P3", "external_referencing",
   "The CBAM is set to replace the mechanisms under Directive 2003/87/EC that prevent carbon leakage, by reflecting the extent to which EU ETS allowances are allocated free of charge under Article 10a of that Directive.",
   "The CBAM is set to replace the mechanisms established under Directive 2003/87/EC to prevent the risk of carbon leakage")
ext("ext.DIR87_GEN", "st.A1P2;st.A1P3;st.A7P7;st.A35P7", "A1.P2;A1.P3;A7.P7.sub2;A35.P7.sub2", "Directive 2003/87/EC (EU ETS), including Article 10a (free allocation of allowances)", "legal_instrument",
    "other (the CBAM is stated to complement and to replace mechanisms of that Directive; scope-relation statement)", dependents="",
    dep_kind="qualifies", constitutive="N",
    effect="Statement of relation between the CBAM and another legal system; no relation of W depends on its content for constitution. Content of Directive 2003/87/EC is not part of W.")

# =============== ARTICLE 2 ===============
st("st.A2P1", "A2.P1", "scope",
   "The Regulation applies to Annex I goods originating in a third country (or processed products from them under inward processing) when imported into the customs territory.",
   "This Regulation applies to goods listed in Annex I originating in a third country")
st("st.A2P2", "A2.P2", "scope",
   "The Regulation also applies to Annex I goods brought to an artificial island or fixed or floating structure on the continental shelf or in the exclusive economic zone of a Member State adjacent to the customs territory.",
   "This Regulation also applies to goods listed in Annex I to this Regulation originating in a third country")
st("st.A2P2S2", "A2.P2.sub2", "assignment_bearing",
   "The Commission shall adopt implementing acts on detailed conditions for applying the CBAM to goods brought to offshore structures, under the examination procedure of Article 29(2).",
   "The Commission shall adopt implementing acts laying down detailed conditions for the application of the CBAM to such goods")
st("st.A2P3", "A2.P3;A2.P3.pta;A2.P3.ptb;A2.P3.ptc", "scope",
   "By derogation from paragraphs 1 and 2 the Regulation does not apply to (a) goods under a negligible-value threshold per consignment, (b) goods in travellers' personal luggage under a negligible-value threshold, (c) goods moved or used in military activities.",
   "By way of derogation from paragraphs 1 and 2, this Regulation shall not apply to:")
st("st.A2P4", "A2.P4;ANX3.pt1.P1;ANX3.pt1.pt-1;ANX3.pt1.pt-2;ANX3.pt1.pt-3;ANX3.pt1.pt-4;ANX3.pt1.P2;ANX3.pt1.pt-5;ANX3.pt1.pt-6;ANX3.pt1.pt-7;ANX3.pt1.pt-8;ANX3.pt1.pt-9",
   "scope",
   "By derogation the Regulation does not apply to goods originating in the third countries and territories listed in point 1 of Annex III (four countries and five territories as enumerated there).",
   "this Regulation shall not apply to goods originating in the third countries and territories listed in point 1 of Annex III")
st("st.A2P5", "A2.P5", "external_referencing",
   "Origin of imported goods is determined by the non-preferential origin rules of Article 59 of Regulation (EU) No 952/2013.",
   "Imported goods shall be considered as originating in third countries in accordance with the rules for non-preferential origin as referred to in Article 59 of Regulation (EU) No 952/2013")
st("st.A2P6", "A2.P6;A2.P6.pta;A2.P6.ptb", "procedural",
   "Third countries and territories are to be listed in point 1 of Annex III where they fulfil both conditions: the EU ETS applies to them or an agreement fully links ETS systems, and the carbon price paid in the country of origin is effectively charged without rebates beyond those applied in the EU ETS.",
   "Third countries and territories shall be listed in point 1 of Annex III where they fulfil all the following conditions:")
st("st.A2P7", "A2.P7;A2.P7.pta;A2.P7.ptb;A2.P7.ptc;A2.P7.ptd;A2.P7.pte;A2.P7.ptf", "scope",
   "Electricity imports from a third country or territory whose electricity market is integrated with the Union market through market coupling, and for which no technical solution exists to apply the CBAM, are exempt provided that the Commission has assessed fulfilment of six cumulative conditions (agreement with the Union, equivalent domestic legislation, roadmap, climate-neutrality commitment, demonstrated progress and carbon pricing by 1 January 2030, system preventing indirect imports).",
   "such importation of electricity from that country or territory shall be exempt from the application of the CBAM, provided that the Commission has assessed that all of the following conditions have been fulfilled in accordance with paragraph 8")
st("st.A2P8", "A2.P8;A2.P7.ptc", "relation_bearing",
   "A third country or territory fulfilling the paragraph 7 conditions is to be listed in point 2 of Annex III and shall submit two reports on fulfilment (by 1 July 2025 and 31 December 2027); by 31 December 2025 and 1 July 2028 the Commission shall assess, on the basis of the roadmap and the reports, whether the third country continues to fulfil the conditions.",
   "shall submit two reports on the fulfilment of those conditions, the first report by 1 July 2025 and the second by 31 December 2027")
st("st.A2P9", "A2.P9;A2.P9.pta;A2.P9.ptb;A2.P9.ptc", "procedural",
   "A third country or territory listed in point 2 of Annex III shall be removed from that list where the Commission has reasons to consider progress insufficient or action incompatible with Union climate and environmental legislation, where the country supports new high-emission generation capacity, or where electricity-export-driven emissions rose by at least 5 % compared with 1 January 2026.",
   "shall be removed from that list where one or more of the following conditions applies:")
st("st.A2P10", "A2.P10", "relation_bearing",
   "The Commission is empowered to adopt delegated acts under Article 28 laying down requirements and procedures for third countries removed from point 2 of Annex III, and, where market coupling remains incompatible, may decide to exclude them from Union market coupling and require explicit capacity allocation at the border.",
   "the Commission may decide to exclude those third countries or territories from Union market coupling and require explicit capacity allocation at the border between the Union and those third countries or territories")
st("st.A2P11", "A2.P11;ANX3.pt2.P1", "relation_bearing",
   "The Commission is empowered to adopt delegated acts under Article 28 to amend the lists of third countries and territories in points 1 or 2 of Annex III by adding or removing a country or territory, depending on whether the conditions of paragraphs 6, 7 or 9 are fulfilled; point 2 of Annex III is a placeholder for countries to be added or removed under Article 2(11).",
   "to amend the lists of third countries or territories listed in point 1 or 2 of Annex III by adding or removing a third country or territory")
st("st.A2P12", "A2.P12", "relation_bearing",
   "The Union may conclude agreements with third countries or territories with a view to taking into account carbon pricing mechanisms in such countries or territories for the purposes of the application of Article 9.",
   "The Union may conclude agreements with third countries or territories with a view to taking into account carbon pricing mechanisms")
ext("ext.UCC_ORIGIN", "st.A2P1;st.A2P2;st.A2P5;st.A3DEF_IMPORTATION", "A2.P1;A2.P2;A2.P5;A3.P0.pt4;A3.P0.pt6", "Regulation (EU) No 952/2013 (Union Customs Code): Art. 256 (inward processing), Art. 59 (non-preferential origin), Art. 201 (release for free circulation), Art. 4 (customs territory of the Union)",
    "legal_instrument", "defines_term", dependents="st.A2P1;st.A2P2;st.A2P5;st.A3DEF_IMPORTATION;cl.NECESSARY_STAGE", dep_kind="specifies", constitutive="Y",
    effect="Scope claims about 'importation', 'customs territory of the Union', origin determination and inward processing rest on definitions in Regulation (EU) No 952/2013; those definitions are outside W and unresolved. Scope-related claims are limited to the wording of W.")
ext("ext.REG1186", "st.A2P3", "A2.P3.pta;A2.P3.ptb", "Council Regulation (EC) No 1186/2009, Art. 23 (value of goods of negligible value)", "legal_instrument",
    "supplies_rule_or_standard", dependents="st.A2P3;cl.NECESSARY_STAGE", dep_kind="specifies", constitutive="Y",
    effect="The numerical threshold of the de minimis derogation in Article 2(3)(a) and (b) is the value specified in the external provision; the threshold is undetermined within W.")
ext("ext.DELREG2446", "st.A2P3;st.A3DEF_GEO", "A2.P3.ptc;A3.P0.pt10", "Commission Delegated Regulation (EU) 2015/2446, Art. 1 points (48) (intrinsic value) and (49) (military activities)", "legal_instrument",
    "defines_term", dependents="st.A2P3;cl.NECESSARY_STAGE", dep_kind="specifies", constitutive="Y",
    effect="The notions 'intrinsic value' and 'military activities' used in the Article 2(3) derogations are defined in the external provision; undetermined within W.")

na("na.A2P2S2", "st.A2P2S2", "A2.P2.sub2", "pd.COM", "adopt implementing acts laying down detailed conditions for the application of the CBAM to goods brought to offshore structures (equivalents of importation and release for free circulation, CBAM declaration procedures, customs controls)",
   "implementing acts on offshore application of the CBAM", "rule_making_standard_setting", "obligation",
   "The Commission shall adopt implementing acts laying down detailed conditions for the application of the CBAM to such goods",
   mech="implementing act adopted under the examination procedure referred to in Article 29(2)", instr="INS-TYPE: implementing act",
   cond="goods brought to an artificial island, fixed or floating structure, or other structure on the continental shelf or in the EEZ of a Member State adjacent to the customs territory (Article 2(2))",
   nt="N0", eff="duty of the Commission to adopt implementing acts", notc="does not constitute any CBAM-specific entity; the content of the acts is not in W",
   deriv="direct", deps="pd.COM", unc="")

qr("qr.A2P8_REPORT", "st.A2P8", "A2.P8;A2.P7;A2.P7.ptc", "pd.3C", "pd.COM", "information_reporting", "third country or territory -> Commission",
   "submit two reports on fulfilment of the paragraph 7 conditions (first by 1 July 2025, second by 31 December 2027)", "reports on fulfilment of the electricity-exemption conditions",
   "information_provision", "obligation",
   "shall submit two reports on the fulfilment of those conditions, the first report by 1 July 2025 and the second by 31 December 2027",
   extra="", cond="third country or territory fulfils all conditions of Article 2(7) and is listed in point 2 of Annex III",
   deriv="derived", drule="Reporting party and recipient: A2.P8 first sentence names the third country as reporter; the recipient is the Commission by A2.P8 second sentence (assessment 'on the basis of ... the reports received from the third country') and A2.P7(c) (roadmap submitted to the Commission).",
   authattr="reporting obligation binding on the listed third country as a condition of continued exemption", discattr="none stated",
   acls="INFO", asuff="sufficient", deps="pd.3C;pd.COM", gap="No evidence of any third country's listing in point 2 of Annex III (the point is a placeholder); relation is constituted as a norm but no instance is evidenced.",
   unc="unc.A2P8_STATE")
qr("qr.A2P8_ASSESS", "st.A2P8", "A2.P8;A2.P7", "pd.COM", "pd.3C", "oversight_supervision", "Commission -> third country or territory",
   "assess, by 31 December 2025 and by 1 July 2028, whether the third country or territory continues to fulfil the paragraph 7 conditions", "continued fulfilment of exemption conditions",
   "monitoring", "obligation",
   "By 31 December 2025 and by 1 July 2028, the Commission shall assess, in particular on the basis of the roadmap referred to in paragraph 7, point (c), and the reports received from the third country or territory",
   mech="assessment on the basis of roadmap and reports", instr="INS-TYPE: report; roadmap",
   cond="third country or territory listed in point 2 of Annex III",
   authattr="Commission holds the assessing role; outcome conditions the exemption (A2(7)) and feeds removal (A2(9))", discattr="Commission assessment of 'sufficient progress' (A2(9)(a)) is evaluative; thresholds only partly specified",
   acls="NONE", asuff="NA", deps="pd.COM;pd.3C", gap="Existence of any listed third country is not evidenced in W.", unc="unc.A2P8_STATE;unc.XREF_BUNDLE", hq="hq.XREF_BUNDLE")
qr("qr.A2P10_DEL", "st.A2P10;st.A2P11", "A2.P10;A2.P11", "pd.COM", "pd.3C", "authority_control", "Commission -> third country or territory",
   "adopt, by delegated act, requirements and procedures for third countries removed from the Annex III point 2 list and, where market coupling remains incompatible, decide to exclude them from Union market coupling and require explicit capacity allocation",
   "application of the CBAM to electricity from third countries removed from the electricity exemption list", "authorization_designation*", "competence",
   "to ensure the application of this Regulation to those countries or territories with regard to electricity",
   tnote="residual function tag (authorization_designation*) used for list-amendment decisions; nearest relation type authority_control",
   mech="delegated act (Article 28); decision to exclude from market coupling", instr="INS-TYPE: delegated act",
   cond="the third country or territory has been removed from point 2 of Annex III (A2(9)); market coupling remains incompatible with the application of the Regulation",
   deriv="derived", drule="Third-country counterpart and Commission competence stated in A2.P10; the removal premise comes from A2.P9 and the list-amendment power from A2.P11 (internal cross-references resolved within W).",
   authattr="Commission may decide (discretion) to exclude from market coupling and impose explicit capacity allocation", discattr="'may decide': discretionary; no criteria beyond incompatibility with application of the Regulation",
   deps="pd.COM;pd.3C", ext="ext.REG2015_1222", gap="Union market coupling is governed by an external instrument; its legal mechanism for exclusion is not in W.",
   unc="unc.A2P10_EXT", hq="hq.EXTDEP_MARKETCOUPLING", iunits="A2.P9;A2.P11")
qr("qr.A2P11_LIST", "st.A2P11;st.A2P6;st.A2P9", "A2.P11;A2.P6;A2.P9;A2.P7;ANX3.pt2.P1", "pd.COM", "pd.3C", "authority_control", "Commission -> third country or territory",
   "adopt delegated acts to add or remove a third country or territory in point 1 or 2 of Annex III depending on fulfilment of the conditions of paragraphs 6, 7 or 9", "listing of third countries and territories determining exclusion from the scope of the Regulation",
   "authorization_designation*", "competence",
   "to amend the lists of third countries or territories listed in point 1 or 2 of Annex III by adding or removing a third country or territory, depending on whether the conditions set out in paragraph 6, 7 or 9 of this Article are fulfilled",
   tnote="residual function tag (authorization_designation*): listing decision; nearest relation type authority_control; the third country is the subject of the decision, not a co-actor",
   mech="delegated act (Article 28)", instr="INS-TYPE: delegated act; Annex III lists",
   cond="conditions of Article 2(6), 2(7) or 2(9) fulfilled in respect of that third country or territory",
   deriv="derived", drule="Commission power and condition cross-references in A2.P11; condition content in A2.P6, A2.P7, A2.P9; the lists themselves are Annex III points 1 and 2 (units resolved within W).",
   authattr="Commission holds exclusive power to amend the lists by delegated act", discattr="conditions fixed in A2.P6/P7/P9; partly evaluative (A2.P9(a))",
   deps="pd.COM;pd.3C", gap="Point 2 of Annex III is a placeholder (no third country listed); point 1 lists countries/territories by name.",
   unc="unc.A2P8_STATE", iunits="A2.P6;A2.P7;A2.P9;ANX3.pt1.P1;ANX3.pt1.P2;ANX3.pt2.P1")
qr("qr.A2P12_AGREE", "st.A2P12", "A2.P12", "pd.UNION", "pd.3C", "contractual_exchange", "Union -> third countries or territories",
   "conclude agreements taking into account carbon pricing mechanisms of third countries or territories for the purposes of Article 9", "agreements on recognition of carbon pricing",
   "cooperation_coordination*", "permission",
   "The Union may conclude agreements with third countries or territories with a view to taking into account carbon pricing mechanisms in such countries or territories for the purposes of the application of Article 9.",
   tnote="residual function tag; contractual_exchange used for treaty-making competence",
   mech="international agreement", instr="INS-TYPE: agreement",
   authattr="permissive competence of the Union", discattr="discretionary ('may')", deps="pd.UNION;pd.3C", gap="No agreement is evidenced in W.")
ext("ext.REG2015_1222", "st.A2P10", "A2.P10;A3.P0.pt11", "Commission Regulation (EU) 2015/1222 (capacity allocation and congestion management), as referred to in the definition of 'market coupling'", "legal_instrument",
    "defines_term", dependents="qr.A2P10_DEL", dep_kind="specifies", constitutive="Y",
    effect="The legal mechanism of 'Union market coupling', from which the Commission may exclude third countries, is defined by reference to the external Regulation; the relation is recorded as stated in W but its operative content is undetermined.")

# =============== ARTICLE 3 (definitions; GAP-07) ===============
st("st.A3DEF_GOODS", "A3.P0;A3.P0.pt1;A3.P0.pt2", "definitional",
   "'Goods' means goods listed in Annex I and 'greenhouse gases' means the gases specified in Annex I for each listed good.",
   "‘goods’ means goods listed in Annex I")
st("st.A3DEF_EMISS", "A3.P0.pt3;A3.P0.pt21;A3.P0.pt22;A3.P0.pt23;A3.P0.pt26;A3.P0.pt27;A3.P0.pt28;A3.P0.pt29;A3.P0.pt34", "definitional",
   "Definitions of emissions, direct, indirect and embedded emissions, tonne of CO2e, production processes, default value, actual emissions and carbon price, with embedded and actual emissions calculated under Annex IV.",
   "‘embedded emissions’ means direct emissions released during the production of goods and indirect emissions from the production of electricity that is consumed during the production processes")
st("st.A3DEF_IMPORTATION", "A3.P0.pt4;A3.P0.pt6", "external_referencing",
   "'Importation' means release for free circulation as provided for in Article 201 of Regulation (EU) No 952/2013 and 'customs territory of the Union' means the territory defined in Article 4 of that Regulation.",
   "‘importation’ means release for free circulation as provided for in Article 201 of Regulation (EU) No 952/2013")
st("st.A3DEF_ETS", "A3.P0.pt5;A3.P0.pt33", "external_referencing",
   "'EU ETS' and 'EU ETS allowance' are defined by reference to Directive 2003/87/EC (activities listed in its Annex I other than aviation; Article 3 point (a)).",
   "‘EU ETS’ means the system for greenhouse gas emissions allowance trading within the Union in respect of activities listed in Annex I to Directive 2003/87/EC other than aviation activities")
st("st.A3DEF_3C", "A3.P0.pt7", "definitional",
   "'Third country' means a country or territory outside the customs territory of the Union.",
   "‘third country’ means a country or territory outside the customs territory of the Union")
st("st.A3DEF_CA", "A3.P0.pt13", "position_defining",
   "'Competent authority' means the authority designated by each Member State in accordance with Article 11.",
   "the authority designated by each Member State in accordance with Article 11")
st("st.A3DEF_CUST", "A3.P0.pt14", "position_defining",
   "'Customs authorities' means the customs administrations of Member States as defined in Article 5, point (1), of Regulation (EU) No 952/2013.",
   "the customs administrations of Member States as defined in Article 5, point (1), of Regulation (EU) No 952/2013")
st("st.A3DEF_IMP", "A3.P0.pt15;A3.P0.pt16", "position_defining",
   "'Importer' means the person lodging a customs declaration for release for free circulation in its own name and on its own behalf or, where an indirect customs representative lodges it, the person on whose behalf it is lodged; 'customs declarant' is defined by reference to Article 5 point (15) of Regulation (EU) No 952/2013.",
   "‘importer’ means either the person lodging a customs declaration for release for free circulation of goods in its own name and on its own behalf")
st("st.A3DEF_ACD", "A3.P0.pt17", "position_defining",
   "'Authorised CBAM declarant' means a person authorised by a competent authority in accordance with Article 17.",
   "‘authorised CBAM declarant’ means a person authorised by a competent authority in accordance with Article 17")
st("st.A3DEF_PERSON", "A3.P0.pt18;A3.P0.pt19;A3.P0.pt19.pta;A3.P0.pt19.ptb;A3.P0.pt20", "definitional",
   "Definitions of 'person', 'established in a Member State' and the EORI number (assigned by the customs authority under Article 9 of Regulation (EU) No 952/2013).",
   "‘person’ means a natural person, a legal person or any association of persons which is not a legal person but which is recognised under Union or national law as having the capacity to perform legal acts")
st("st.A3DEF_CERT", "A3.P0.pt24;A3.P0.pt25", "definitional",
   "'CBAM certificate' means a certificate in electronic format corresponding to one tonne of CO2e of embedded emissions in goods; 'surrender' means offsetting of CBAM certificates against the declared embedded emissions or those that should have been declared.",
   "‘CBAM certificate’ means a certificate in electronic format corresponding to one tonne of CO2e of embedded emissions in goods")
st("st.A3DEF_OPER", "A3.P0.pt30;A3.P0.pt31", "position_defining",
   "'Installation' means a stationary technical unit where a production process is carried out; 'operator' means any person who operates or controls an installation in a third country.",
   "‘operator’ means any person who operates or controls an installation in a third country")
st("st.A3DEF_NAB", "A3.P0.pt32", "position_defining",
   "'National accreditation body' means a national accreditation body appointed by each Member State pursuant to Article 4(1) of Regulation (EC) No 765/2008.",
   "a national accreditation body as appointed by each Member State pursuant to Article 4(1) of Regulation (EC) No 765/2008")
st("st.A3DEF_GEO", "A3.P0.pt8;A3.P0.pt9;A3.P0.pt10", "external_referencing",
   "'Continental shelf', 'exclusive economic zone' and 'intrinsic value' are defined by reference to the UN Convention on the Law of the Sea (Articles 76, 55) and Delegated Regulation (EU) 2015/2446 (Article 1 point (48)).",
   "‘continental shelf’ means a continental shelf as defined in Article 76 of the United Nations Convention on the Law of the Sea")
st("st.A3DEF_MC", "A3.P0.pt11;A3.P0.pt12", "external_referencing",
   "'Market coupling' is the allocation of transmission capacity through a Union system matching orders and allocating cross-zonal capacities as set out in Regulation (EU) 2015/1222; 'explicit capacity allocation' is the allocation of cross-border transmission capacity separate from electricity trade.",
   "‘market coupling’ means the allocation of transmission capacity through a Union system which simultaneously matches orders and allocates cross-zonal capacities as set out in Regulation (EU) 2015/1222")
ext("ext.UNCLOS", "st.A3DEF_GEO", "A3.P0.pt8;A3.P0.pt9", "United Nations Convention on the Law of the Sea, Articles 76 (continental shelf) and 55 (exclusive economic zone)", "legal_instrument",
    "defines_term", dependents="", dep_kind="specifies", constitutive="N",
    effect="Defines geographic notions used in the Article 2(2) scope extension; no governance relation of W depends on it.")
ext("ext.UCC_PERSONS", "st.A3DEF_CUST;st.A3DEF_IMP;st.A5P1;st.A32;st.A17P1", "A3.P0.pt14;A3.P0.pt15;A3.P0.pt16;A3.P0.pt20;A5.P1;A32.P0;A17.P2.ptd", "Regulation (EU) No 952/2013 (Union Customs Code): Art. 5 points (1) and (15) (customs administrations; declarant), Art. 9 (EORI number), Art. 18 (indirect customs representative)", "legal_instrument",
    "defines_term", dependents="pd.CUST;pd.IMP;pd.ICR", dep_kind="constitutes", constitutive="Y",
    effect="The identity and powers of the 'customs authorities', 'customs declarant' and 'indirect customs representative' as legal positions are constituted outside W; their existence is undetermined within W and relations referencing them are limited to the text of W.")
ext("ext.DIR87_DEF", "st.A3DEF_ETS", "A3.P0.pt5;A3.P0.pt33", "Directive 2003/87/EC, Annex I (activities) and Article 3 point (a) (allowance)", "legal_instrument",
    "defines_term", dependents="", dep_kind="specifies", constitutive="N",
    effect="Defines 'EU ETS' and 'EU ETS allowance'; the price mechanism of Article 21 uses the allowance auction price (see separate EXT); no relation depends on these definitions for constitution.")
ext("ext.REG765_NAB", "st.A3DEF_NAB", "A3.P0.pt32;A18.P2", "Regulation (EC) No 765/2008, Art. 4(1) (appointment of national accreditation bodies)", "legal_instrument",
    "constitutes_position", dependents="pd.NAB", dep_kind="constitutes", constitutive="Y",
    effect="The position 'national accreditation body' is constituted by the external appointment; its existence and powers outside Article 18(2) are undetermined within W.")

# =============== ARTICLE 4 ===============
st("st.A4", "A4.P0", "assignment_bearing",
   "Goods shall be imported into the customs territory of the Union only by an authorised CBAM declarant.",
   "Goods shall be imported into the customs territory of the Union only by an authorised CBAM declarant.")
na("na.A4_PROHIB", "st.A4", "A4.P0", "pd.OTHERPERSON", "import goods into the customs territory of the Union", "goods subject to the Regulation", "enforcement", "prohibition",
   "Goods shall be imported into the customs territory of the Union only by an authorised CBAM declarant.",
   mech="reservation of importation to persons holding the authorised-declarant status", instr="INS-TYPE: status of authorised CBAM declarant",
   cond="", cp="authorised CBAM declarant (the only permitted importer)", cps="IN_PROVISION", nt="N0",
   eff="constraint on persons other than authorised CBAM declarants: importation is reserved to authorised CBAM declarants", notc="does not itself constitute any sanction or enforcement body",
   constraint="Y", deriv="direct", drule="",
   deps="pd.ACD", unc="unc.A4_CONVERSE")
