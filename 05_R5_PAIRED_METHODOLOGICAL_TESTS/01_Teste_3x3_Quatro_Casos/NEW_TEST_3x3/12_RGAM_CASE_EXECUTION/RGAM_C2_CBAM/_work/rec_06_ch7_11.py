from rgam_lib import *

# =============== ARTICLE 28 ===============
st("st.A28P1", "A28.P1;A28.P2", "relation_bearing",
   "The power to adopt delegated acts is conferred on the Commission under the conditions of Article 28; the power referred to in Articles 2(10), 2(11), 18(3), 20(6) and 27(6) is conferred for five years from 17 May 2023, tacitly extended for periods of identical duration unless the European Parliament or the Council opposes the extension not later than three months before the end of each period; the Commission draws up a report on the delegation not later than nine months before the end of the five-year period.",
   "The power to adopt delegated acts is conferred on the Commission subject to the conditions laid down in this Article.")
st("st.A28P3", "A28.P3;A28.P4", "relation_bearing",
   "The delegation of power may be revoked at any time by the European Parliament or by the Council; a decision to revoke ends the delegation, takes effect the day after its publication in the Official Journal or at a later date specified, and does not affect the validity of any delegated act already in force.",
   "may be revoked at any time by the European Parliament or by the Council")
st("st.A28P5", "A28.P5", "relation_bearing",
   "Before adopting a delegated act the Commission shall consult experts designated by each Member State in accordance with the principles of the Inter-institutional Agreement of 13 April 2016 on Better Law-Making.",
   "Before adopting a delegated act, the Commission shall consult experts designated by each Member State")
st("st.A28P6", "A28.P6", "relation_bearing",
   "As soon as it adopts a delegated act the Commission shall notify it simultaneously to the European Parliament and to the Council.",
   "the Commission shall notify it simultaneously to the European Parliament and to the Council")
st("st.A28P7", "A28.P7", "relation_bearing",
   "A delegated act enters into force only if no objection has been expressed by the European Parliament or by the Council within two months of notification, or if both inform the Commission before the expiry of that period that they will not object; the period is extended by two months at the initiative of the European Parliament or the Council.",
   "shall enter into force only if no objection has been expressed either by the European Parliament or by the Council within a period of two months of notification of that act")
qr("qr.A28_CONFER", "st.A28P1;st.A28P3", "A28.P1;A28.P2;A28.P3", "pd.EP", "pd.COM", "delegation_authorization", "European Parliament and Council -> Commission",
   "confer on the Commission the power to adopt the delegated acts referred to in Articles 2(10), 2(11), 18(3), 20(6) and 27(6) for a period of five years from 17 May 2023, tacitly extended for periods of identical duration unless the European Parliament or the Council opposes the extension not later than three months before the end of each period",
   "power to adopt delegated acts", "rule_making_standard_setting", "competence",
   "The power to adopt delegated acts referred to in Articles 2(10), 2(11), 18(3), 20(6) and 27(6) shall be conferred on the Commission for a period of five years from 17 May 2023.",
   extra="pd.COUNCIL", tnote="n-ary: the European Parliament and the Council are the grantors identified through their opposition (A28(2)) and revocation (A28(3)) powers; the conferral clause itself is passive",
   mech="conferral of delegated power for a renewable five-year period", instr="INS-TYPE: delegated act",
   cond="acts referred to in Articles 2(10), 2(11), 18(3), 20(6) and 27(6); five-year period from 17 May 2023; tacit extension unless opposed",
   deriv="derived", drule="A28.P1 and A28.P2 confer the power on the Commission passively; the grantors are identified by A28.P2 (opposition to extension by the European Parliament or the Council) and A28.P3 (revocation by the European Parliament or the Council).",
   authattr="the power is conferred subject to conditions, revocable by the European Parliament or the Council", discattr="extension is tacit unless opposed", deps="pd.EP;pd.COUNCIL;pd.COM",
   unc="unc.A28_PASSIVE")
qr("qr.A28_REVOKE", "st.A28P3", "A28.P3;A28.P4", "pd.EP", "pd.COM", "authority_control", "European Parliament or Council -> Commission",
   "revoke the delegation of power referred to in Articles 2(10), 2(11), 18(3), 20(6) and 27(6) at any time, by a decision that takes effect the day after its publication in the Official Journal or at a later date specified and does not affect the validity of delegated acts already in force",
   "revocation of the delegation of power", "rule_making_standard_setting", "competence",
   "The delegation of power referred to in Articles 2(10), 2(11), 18(3), 20(6) and 27(6) may be revoked at any time by the European Parliament or by the Council.",
   extra="pd.COUNCIL", tnote="n-ary: the power is held by the European Parliament or by the Council, each acting alone",
   mech="revocation decision published in the Official Journal", instr="INS-TYPE: decision to revoke", cond="at any time",
   authattr="each of the European Parliament and the Council may revoke unilaterally", discattr="no ground required for revocation", deps="pd.EP;pd.COUNCIL;pd.COM")
qr("qr.A28_CONSULT", "st.A28P5", "A28.P5", "pd.COM", "pd.MSEXPERTS", "representation_participation", "Commission -> experts designated by each Member State",
   "consult experts designated by each Member State, in accordance with the principles of the Inter-institutional Agreement of 13 April 2016 on Better Law-Making, before adopting a delegated act",
   "preparation of delegated acts", "cooperation_coordination*", "obligation",
   "Before adopting a delegated act, the Commission shall consult experts designated by each Member State",
   tnote="residual function tag; consultation", mech="expert consultation", instr="INS-TYPE: consultation", cond="before adopting a delegated act",
   authattr="consultation is mandatory; its effect on the content of the act is not stated", discattr="the Commission's treatment of expert input is not stated", deps="pd.COM;pd.MSEXPERTS",
   ext="ext.IIA_BLM", unc="unc.CONSULT_EFFECT")
qr("qr.A28_NOTIFY", "st.A28P6", "A28.P6", "pd.COM", "pd.EP", "information_reporting", "Commission -> European Parliament and Council",
   "notify a delegated act simultaneously to the European Parliament and to the Council as soon as it is adopted", "delegated acts", "information_provision", "obligation",
   "the Commission shall notify it simultaneously to the European Parliament and to the Council",
   extra="pd.COUNCIL", mech="notification", cond="as soon as a delegated act is adopted", acls="INFO", asuff="sufficient",
   authattr="the notification starts the objection period (A28(7))", discattr="none stated", deps="pd.COM;pd.EP;pd.COUNCIL")
qr("qr.A28_OBJECT", "st.A28P7", "A28.P7;A28.P6", "pd.EP", "pd.COM", "oversight_supervision", "European Parliament or Council -> Commission",
   "object to a delegated act within two months of notification (extended by two months at the initiative of the European Parliament or the Council), the act entering into force only if no objection is expressed or both inform the Commission before expiry that they will not object",
   "control of delegated acts", "rule_making_standard_setting", "competence",
   "shall enter into force only if no objection has been expressed either by the European Parliament or by the Council within a period of two months of notification of that act",
   extra="pd.COUNCIL", tnote="n-ary: objection by either institution prevents entry into force; function recorded as rule-making control", mech="objection within a notification period",
   instr="INS-TYPE: delegated act", cond="delegated act adopted pursuant to Articles 2(10), 2(11), 18(3), 20(6) or 27(6); within two months of notification, extendable by two months",
   authattr="either the European Parliament or the Council can block entry into force of a delegated act", discattr="no ground required for objection", deps="pd.EP;pd.COUNCIL;pd.COM", iunits="A28.P6")
na("na.A28_REPORT", "st.A28P1", "A28.P2", "pd.COM", "draw up a report in respect of the delegation of power not later than nine months before the end of the five-year period", "report on the delegation of power",
   "information_provision", "obligation", "The Commission shall draw up a report in respect of the delegation of power not later than nine months before the end of the five-year period.",
   mech="report", cond="not later than nine months before the end of the five-year period", nt="N0", eff="duty of the Commission to draw up a report on the delegation",
   notc="the provision names no recipient of the report; no counterparty is created", deriv="direct", deps="pd.COM")
ext("ext.IIA_BLM", "st.A28P5", "A28.P5", "Inter-institutional Agreement of 13 April 2016 on Better Law-Making (principles governing consultation of Member State experts)", "other_normative",
    "supplies_rule_or_standard", dependents="qr.A28_CONSULT", dep_kind="specifies", constitutive="N",
    effect="Principles that the consultation is to follow; the Agreement is not part of W and no relation of W depends on it for constitution.")

# =============== ARTICLE 29 ===============
st("st.A29P1", "A29.P1", "relation_bearing",
   "The Commission shall be assisted by the CBAM Committee, a committee within the meaning of Regulation (EU) No 182/2011.",
   "The Commission shall be assisted by the CBAM Committee.")
st("st.A29P2", "A29.P2", "external_referencing",
   "Where reference is made to this paragraph, Article 5 of Regulation (EU) No 182/2011 shall apply.",
   "Where reference is made to this paragraph, Article 5 of Regulation (EU) No 182/2011 shall apply.")
qr("qr.A29_ASSIST", "st.A29P1;st.A29P2", "A29.P1;A29.P2", "pd.COM", "pd.CBAMCOM", "representation_participation", "Commission -> CBAM Committee",
   "be assisted by the CBAM Committee in the adoption of implementing acts under the examination procedure referred to in Article 29(2), to which Article 5 of Regulation (EU) No 182/2011 applies",
   "adoption of implementing acts", "cooperation_coordination*", "obligation",
   "The Commission shall be assisted by the CBAM Committee.",
   tnote="nearest of the ten types: the committee participates in the Commission's implementing procedure; the substance of the examination procedure (control over the Commission's draft acts) lies in the external Regulation (EU) No 182/2011 and is not in W; residual function tag",
   mech="examination procedure under Article 5 of Regulation (EU) No 182/2011", instr="INS-TYPE: implementing act (procedure)",
   cond="where reference is made to Article 29(2), as in each provision empowering the Commission to adopt implementing acts under 'the examination procedure referred to in Article 29(2)'",
   deriv="derived", drule="A29.P1 states the assistance; A29.P2 provides that Article 5 of Regulation (EU) No 182/2011 applies where reference is made to it; the invoking provisions are the empowerments that refer to 'the examination procedure referred to in Article 29(2)' (internal cross-references resolved within W).",
   authattr="the Committee's decisional weight over the Commission's implementing acts is defined by the external Regulation and is not in W", discattr="not determinable within W",
   deps="pd.COM;pd.CBAMCOM", ext="ext.REG182", hq="hq.EXTDEP_COMITOLOGY", unc="unc.NT_COMMITTEE",
   iunits="A2.P2.sub2;A5.P8;A6.P6;A7.P7.sub2;A8.P3.sub2;A9.P4;A14.P6;A17.P10.sub2;A18.P1;A21.P3;A25.P6;A31.P2;A35.P7.sub2",
   gap="The control exercised through the examination procedure is external to W; the relation is recorded as stated in W.")
ext("ext.REG182", "st.A29P1;st.A29P2", "A29.P1;A29.P2", "Regulation (EU) No 182/2011 (mechanisms for control by the Member States of the Commission's exercise of implementing powers), including Article 5 (examination procedure)", "legal_instrument",
    "supplies_rule_or_standard", dependents="qr.A29_ASSIST;pd.CBAMCOM", dep_kind="constitutes", constitutive="Y",
    effect="The legal effect of the CBAM Committee's involvement (examination procedure) is defined by the external Regulation; claims about the committee's control over the Commission's implementing acts are undetermined within W and are limited to the statement that the Commission is assisted by the committee.")

# =============== ARTICLE 30 ===============
st("st.A30P1", "A30.P1", "assignment_bearing",
   "The Commission, in consultation with relevant stakeholders, shall collect the information necessary for extending the scope of the Regulation as indicated in paragraph 2(a) and for developing methods of calculating embedded emissions based on environmental footprint methods.",
   "The Commission, in consultation with relevant stakeholders, shall collect the information necessary with a view to extending the scope of this Regulation")
st("st.A30P2", "A30.P2;A30.P2.sub2;A30.P2.pta;A30.P2.pta.pti;A30.P2.pta.ptii;A30.P2.pta.ptiii;A30.P2.pta.ptiv;A30.P2.ptb;A30.P2.ptc;A30.P2.ptd;A30.P2.pte;A30.P2.ptf;A30.P2.ptg", "relation_bearing",
   "Before the end of the transitional period the Commission shall present a report to the European Parliament and to the Council on the application of the Regulation, assessing possible extensions of scope (indirect emissions of Annex II goods, transport, other goods at risk of carbon leakage, other precursors), criteria and a timetable ending in 2030 for including goods, technical requirements, international progress, the governance system including administrative costs, effects on developing countries and least developed countries, and the methodology for indirect emissions.",
   "Before the end of the transitional period referred to in Article 32, the Commission shall present a report to the European Parliament and to the Council on the application of this Regulation.")
st("st.A30P3", "A30.P3", "relation_bearing",
   "At least one year before the end of the transitional period the Commission shall present a report to the European Parliament and to the Council identifying products further down the value chain of the Annex I goods that it recommends for inclusion, developing a methodology based on relevance in terms of cumulated greenhouse gas emissions and risk of carbon leakage.",
   "At least one year before the end of the transitional period, the Commission shall present a report to the European Parliament and to the Council")
st("st.A30P4", "A30.P4", "relation_bearing",
   "The reports of paragraphs 2 and 3 shall, where appropriate, be accompanied by a legislative proposal by the end of the transitional period, including a detailed impact assessment.",
   "The reports referred to in paragraphs 2 and 3 shall, where appropriate, be accompanied by a legislative proposal by the end of the transitional period")
st("st.A30P5", "A30.P5", "relation_bearing",
   "Every two years from the end of the transitional period, as part of its annual report to the European Parliament and to the Council under Article 10(5) of Directive 2003/87/EC, the Commission shall assess the effectiveness of the CBAM in addressing the carbon leakage risk of Union goods exported to third countries without the EU ETS or similar carbon pricing and, where the report concludes there is such a risk, shall where appropriate present a legislative proposal.",
   "the Commission shall assess the effectiveness of the CBAM in addressing the carbon leakage risk of goods produced in the Union for export to third countries")
st("st.A30P6", "A30.P6;A30.P6.sub2;A30.P6.pta;A30.P6.pta.pti;A30.P6.pta.ptii;A30.P6.pta.ptiii;A30.P6.pta.ptiv;A30.P6.pta.ptv;A30.P6.pta.ptvi;A30.P6.pta.ptvii;A30.P6.ptb;A30.P6.ptb.pti;A30.P6.ptb.ptii;A30.P6.ptb.ptiii;A30.P6.ptb.ptiv;A30.P6.ptc;A30.P6.ptd", "relation_bearing",
   "The Commission shall monitor the functioning of the CBAM and, before 1 January 2028 and every two years thereafter, present a report to the European Parliament and to the Council on the application of the Regulation containing at least an assessment of the CBAM's impacts (carbon leakage including exports, covered sectors, internal market, inflation and commodity prices, user industries, international trade including resource shuffling, least developed countries), an assessment of the governance system including the implementation and administration of the authorisation of CBAM declarants by Member States, the scope, circumvention and the application of penalties in Member States, results of investigations and penalties imposed, and aggregated information on emission intensity per country of origin.",
   "Before 1 January 2028, as well as every two years thereafter, the Commission shall present a report to the European Parliament and to the Council")
st("st.A30P7", "A30.P7", "relation_bearing",
   "Where an unforeseeable, exceptional and unprovoked event outside the control of one or more third countries has destructive consequences on their economic and industrial infrastructure, the Commission shall assess the situation and submit to the European Parliament and the Council a report, accompanied where appropriate by a legislative proposal to amend the Regulation by setting out necessary provisional measures.",
   "the Commission shall assess the situation and submit to the European Parliament and to the Council a report")
st("st.A30P8", "A30.P8", "external_referencing",
   "From the end of the transitional period, as part of the annual reporting under Article 41 of Regulation (EU) 2021/947, the Commission shall evaluate and report on how the financing under that Regulation has contributed to the decarbonisation of the manufacturing industry in least developed countries.",
   "the Commission shall evaluate and report on how the financing under that Regulation has contributed to the decarbonisation of the manufacturing industry in LDCs")
na("na.A30_COLLECT", "st.A30P1", "A30.P1", "pd.COM", "collect, in consultation with relevant stakeholders, the information necessary for extending the scope of the Regulation and for developing methods of calculating embedded emissions based on environmental footprint methods",
   "information for extending scope and for new calculation methods", "monitoring", "obligation",
   "The Commission, in consultation with relevant stakeholders, shall collect the information necessary with a view to extending the scope of this Regulation",
   mech="information collection; consultation of 'relevant stakeholders'", cond="", nt="N0", eff="duty of the Commission to collect information",
   notc="'relevant stakeholders' is not a defined category or position; no counterparty is created", deriv="direct", deps="pd.COM", unc="unc.A30_STAKEHOLDERS")
qr("qr.A30_REPORT2", "st.A30P2", "A30.P2;A30.P2.sub2;A30.P2.pta;A30.P2.pta.pti;A30.P2.pta.ptii;A30.P2.pta.ptiii;A30.P2.pta.ptiv;A30.P2.ptb;A30.P2.ptc;A30.P2.ptd;A30.P2.pte;A30.P2.ptf;A30.P2.ptg", "pd.COM", "pd.EP", "information_reporting", "Commission -> European Parliament and Council",
   "present, before the end of the transitional period, a report on the application of the Regulation containing an assessment of possible extensions of scope, criteria for including goods with a timetable ending in 2030, technical requirements, international progress, the governance system including administrative costs, effects on developing and least developed countries, and the methodology for indirect emissions",
   "report on the application of the Regulation", "information_provision", "obligation",
   "Before the end of the transitional period referred to in Article 32, the Commission shall present a report to the European Parliament and to the Council on the application of this Regulation.",
   extra="pd.COUNCIL", mech="report", instr="INS-TYPE: report", cond="before the end of the transitional period referred to in Article 32", acls="INFO", asuff="sufficient",
   authattr="the Commission reports; the recipients' assessment or sanction capacity is not stated in W", discattr="the Commission determines the content within the listed topics",
   deps="pd.COM;pd.EP;pd.COUNCIL", gap="Reporting addressed to the legislators; no forum capacity is stated, so no accountability class beyond INFO is evidenced.")
qr("qr.A30_REPORT3", "st.A30P3", "A30.P3", "pd.COM", "pd.EP", "information_reporting", "Commission -> European Parliament and Council",
   "present, at least one year before the end of the transitional period, a report identifying products further down the value chain of the Annex I goods recommended for inclusion, on the basis of a methodology developed in a timely manner and based on relevance in terms of cumulated greenhouse gas emissions and risk of carbon leakage",
   "report on downstream products", "information_provision", "obligation",
   "At least one year before the end of the transitional period, the Commission shall present a report to the European Parliament and to the Council",
   extra="pd.COUNCIL", mech="report", instr="INS-TYPE: report", cond="at least one year before the end of the transitional period", acls="INFO", asuff="sufficient",
   authattr="the Commission reports and recommends", discattr="the Commission develops the methodology", deps="pd.COM;pd.EP;pd.COUNCIL")
qr("qr.A30_PROPOSAL", "st.A30P4", "A30.P4;A30.P2;A30.P3", "pd.COM", "pd.EP", "information_reporting", "Commission -> European Parliament and Council",
   "accompany the reports of paragraphs 2 and 3, where appropriate, by a legislative proposal by the end of the transitional period, including a detailed impact assessment, in particular with a view to extending the scope of the Regulation",
   "legislative proposal accompanying the reports", "information_provision", "obligation",
   "The reports referred to in paragraphs 2 and 3 shall, where appropriate, be accompanied by a legislative proposal by the end of the transitional period",
   extra="pd.COUNCIL", tnote="a legislative proposal is an instrument other than a report; recorded under the nearest type with the report relation it accompanies",
   mech="legislative proposal with impact assessment", instr="INS-TYPE: legislative proposal", cond="where appropriate; by the end of the transitional period",
   deriv="derived", drule="A30.P4 refers to the reports of paragraphs 2 and 3, whose addressees are the European Parliament and the Council (A30.P2, A30.P3); the proposal accompanies those reports.",
   acls="INFO", asuff="sufficient", authattr="the Commission proposes where it judges it appropriate", discattr="'where appropriate'; wide discretion", deps="pd.COM;pd.EP;pd.COUNCIL")
qr("qr.A30_REPORT5", "st.A30P5", "A30.P5", "pd.COM", "pd.EP", "information_reporting", "Commission -> European Parliament and Council",
   "assess every two years from the end of the transitional period, as part of its annual report under Article 10(5) of Directive 2003/87/EC, the effectiveness of the CBAM in addressing the carbon leakage risk of goods produced in the Union for export to third countries that do not apply the EU ETS or a similar carbon pricing mechanism, and present where appropriate a legislative proposal",
   "assessment of export carbon leakage", "information_provision", "obligation",
   "the Commission shall assess the effectiveness of the CBAM in addressing the carbon leakage risk of goods produced in the Union for export to third countries",
   extra="pd.COUNCIL", mech="biennial assessment within an external annual report", instr="INS-TYPE: report; legislative proposal", cond="every two years from the end of the transitional period; legislative proposal where the report concludes there is a risk of carbon leakage and where appropriate",
   acls="INFO", asuff="sufficient", authattr="the Commission assesses and proposes", discattr="'where appropriate'", deps="pd.COM;pd.EP;pd.COUNCIL", ext="ext.DIR87_REPORT")
qr("qr.A30_REPORT6", "st.A30P6", "A30.P6;A30.P6.sub2;A30.P6.pta;A30.P6.pta.pti;A30.P6.pta.ptii;A30.P6.pta.ptiii;A30.P6.pta.ptiv;A30.P6.pta.ptv;A30.P6.pta.ptvi;A30.P6.pta.ptvii;A30.P6.ptb;A30.P6.ptb.pti;A30.P6.ptb.ptii;A30.P6.ptb.ptiii;A30.P6.ptb.ptiv;A30.P6.ptc;A30.P6.ptd", "pd.COM", "pd.EP", "information_reporting", "Commission -> European Parliament and Council",
   "present, before 1 January 2028 and every two years thereafter, a report on the application of the Regulation and the functioning of the CBAM, containing at least an assessment of impacts, an assessment of the governance system including the implementation and administration of the authorisation of CBAM declarants by Member States, the scope, circumvention and the application of penalties in Member States, results of investigations and penalties imposed, and aggregated information on emission intensity for each country of origin",
   "report on the application of the Regulation and the functioning of the CBAM", "information_provision", "obligation",
   "Before 1 January 2028, as well as every two years thereafter, the Commission shall present a report to the European Parliament and to the Council",
   extra="pd.COUNCIL", mech="biennial report", instr="INS-TYPE: report", cond="before 1 January 2028 and every two years thereafter", acls="INFO", asuff="sufficient",
   authattr="the Commission reports on the CBAM and on Member States' administration", discattr="the Commission determines the assessment within the listed topics", deps="pd.COM;pd.EP;pd.COUNCIL")
qr("qr.A30_ASSESS_MS", "st.A30P6", "A30.P6.ptb;A30.P6.ptb.pti;A30.P6.ptb.ptiv;A30.P6.sub2", "pd.COM", "pd.MS", "oversight_supervision", "Commission -> Member States (object of the assessment)",
   "assess the implementation and administration of the authorisation of CBAM declarants by Member States and the application of penalties in Member States, as part of the biennial report",
   "Member States' implementation and administration of authorisation and penalties", "monitoring", "obligation",
   "the governance system, including an assessment of the implementation and administration of the authorisation of CBAM declarants by Member States;",
   tnote="the Member States are the object of the Commission's assessment; the output flows to the European Parliament and the Council (see the report relation); no power of the Commission to correct Member State conduct is stated here",
   mech="assessment within the biennial report", instr="INS-TYPE: report", cond="before 1 January 2028 and every two years thereafter",
   authattr="the Commission assesses Member State administration; assessment capacity only, no corrective power stated in this provision", discattr="the Commission determines the assessment",
   deps="pd.COM;pd.MS", unc="unc.A30_ASSESS_MS", iunits="A30.P6")
qr("qr.A30_EXCEPT", "st.A30P7", "A30.P7", "pd.COM", "pd.EP", "information_reporting", "Commission -> European Parliament and Council",
   "assess the situation and submit a report, accompanied where appropriate by a legislative proposal to amend the Regulation setting out the necessary provisional measures, where an unforeseeable, exceptional and unprovoked event has destructive consequences on the economic and industrial infrastructure of third countries subject to the CBAM",
   "report on exceptional circumstances in third countries", "information_provision", "obligation",
   "the Commission shall assess the situation and submit to the European Parliament and to the Council a report",
   extra="pd.COUNCIL", mech="report with legislative proposal", instr="INS-TYPE: report; legislative proposal",
   cond="an unforeseeable, exceptional and unprovoked event outside the control of one or more third countries subject to the CBAM, with destructive consequences on their economic and industrial infrastructure",
   acls="INFO", asuff="sufficient", authattr="the Commission assesses and reports", discattr="'where appropriate' for the legislative proposal", deps="pd.COM;pd.EP;pd.COUNCIL")
na("na.A30P8_REPORT", "st.A30P8", "A30.P8", "pd.COM", "evaluate and report, from the end of the transitional period and as part of the annual reporting under Article 41 of Regulation (EU) 2021/947, on how the financing under that Regulation has contributed to the decarbonisation of the manufacturing industry in least developed countries",
   "contribution of external financing to decarbonisation in LDCs", "monitoring", "obligation",
   "the Commission shall evaluate and report on how the financing under that Regulation has contributed to the decarbonisation of the manufacturing industry in LDCs",
   mech="evaluation within an external annual reporting", instr="INS-TYPE: report", cond="from the end of the transitional period referred to in Article 32", nt="N0",
   eff="duty of the Commission to evaluate and report", notc="the addressee of the annual reporting under Article 41 of Regulation (EU) 2021/947 is not named in W; no counterparty is created", deriv="direct", deps="pd.COM", ext="ext.REG2021_947")
ext("ext.DIR87_REPORT", "st.A30P5", "A30.P5", "Directive 2003/87/EC, Article 10(5) (annual report to the European Parliament and the Council)", "legal_instrument",
    "supplies_rule_or_standard", dependents="qr.A30_REPORT5", dep_kind="qualifies", constitutive="N",
    effect="The CBAM assessment is delivered as part of an external annual report; the report's addressees stated in A30(5) (European Parliament and Council) do not depend on the external provision for their identification.")
ext("ext.REG2021_947", "st.A30P8", "A30.P8", "Regulation (EU) 2021/947 (Neighbourhood, Development and International Cooperation Instrument - Global Europe), Article 41 (annual reporting)", "legal_instrument",
    "supplies_rule_or_standard", dependents="na.A30P8_REPORT", dep_kind="specifies", constitutive="Y",
    effect="The addressee and form of the annual reporting through which the Commission evaluates are defined by the external Regulation; no counterparty can be identified within W.")
ext("ext.DIR87_ART10B", "st.A30P2", "A30.P2.ptb", "Directive 2003/87/EC, Article 10b (sectors and subsectors at risk of carbon leakage)", "legal_instrument",
    "supplies_rule_or_standard", dependents="qr.A30_REPORT2", dep_kind="specifies", constitutive="N",
    effect="Criterion for identifying goods for inclusion in the report assessment; no relation of W depends on it for constitution.")

# =============== ARTICLE 31 ===============
st("st.A31P1", "A31.P1", "assignment_bearing",
   "The CBAM certificates to be surrendered under Article 22 shall be adjusted to reflect the extent to which EU ETS allowances are allocated free of charge under Article 10a of Directive 2003/87/EC to installations producing, within the Union, the goods listed in Annex I.",
   "The CBAM certificates to be surrendered in accordance with Article 22 of this Regulation shall be adjusted to reflect the extent to which EU ETS allowances are allocated free of charge")
st("st.A31P2", "A31.P2", "assignment_bearing",
   "The Commission is empowered to adopt implementing acts laying down detailed rules for the calculation of the adjustment, by reference to the principles applied in the EU ETS for free allocation, combining the benchmarks into values for the goods concerned and taking into account precursors, under the examination procedure of Article 29(2).",
   "The Commission is empowered to adopt implementing acts laying down detailed rules for the calculation of the adjustment")
na("na.A31_ADJUST", "st.A31P1;st.A6P2", "A31.P1;A6.P2.ptc;A22.P1", "pd.ACD", "have the number of CBAM certificates to be surrendered adjusted to reflect the extent to which EU ETS allowances are allocated free of charge under Article 10a of Directive 2003/87/EC to installations producing Annex I goods within the Union",
   "number of CBAM certificates to be surrendered", "implementation", "obligation",
   "The CBAM certificates to be surrendered in accordance with Article 22 of this Regulation shall be adjusted to reflect the extent to which EU ETS allowances are allocated free of charge",
   mech="adjustment of the surrender number; to be specified by implementing acts", instr="INS-TYPE: adjustment of certificates",
   cond="free allocation of EU ETS allowances under Article 10a of Directive 2003/87/EC to Union installations producing Annex I goods", nt="N0",
   eff="adjustment of the number of certificates to be surrendered", notc="impersonal wording; no counterparty; the extent of free allocation is defined externally",
   deriv="derived", drule="A31.P1 is impersonal; A6.P2 point (c) places the adjustment 'in accordance with Article 31' in the CBAM declaration of the authorised CBAM declarant and A22.P1 places the surrender with the authorised CBAM declarant; the obligated position is therefore the authorised CBAM declarant.",
   deps="pd.ACD", ext="ext.DIR87_FREE", epi="documented", unc="unc.A31_EXT")
na("na.A31P2_IMPL", "st.A31P2", "A31.P2", "pd.COM", "adopt implementing acts laying down detailed rules for the calculation of the adjustment of the number of CBAM certificates for free allocation", "implementing acts on the free-allocation adjustment",
   "rule_making_standard_setting", "competence", "The Commission is empowered to adopt implementing acts laying down detailed rules for the calculation of the adjustment",
   mech="implementing act under the examination procedure (Article 29(2))", instr="INS-TYPE: implementing act", nt="N3", eff="competence of the Commission to adopt implementing acts",
   notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM", ext="ext.DIR87_FREE")
ext("ext.DIR87_FREE", "st.A31P1;st.A1P3", "A31.P1;A31.P2;A1.P3", "Directive 2003/87/EC, Article 10a (free allocation of allowances) and the EU ETS benchmarks and principles applied to Union installations", "legal_instrument",
    "supplies_rule_or_standard", dependents="na.A31_ADJUST;na.A31P2_IMPL", dep_kind="specifies", constitutive="Y",
    effect="The extent of free allocation that determines the adjustment of the number of certificates is defined by the external Directive; the adjustment is undetermined within W.")

# =============== ARTICLES 32-35 (transitional) ===============
st("st.A32", "A32.P0", "assignment_bearing",
   "During the transitional period from 1 October 2023 until 31 December 2025 the obligations of the importer under the Regulation are limited to the reporting obligations of Articles 33, 34 and 35; where the importer is established in a Member State and appoints an indirect customs representative who agrees, the reporting obligations apply to that representative; where the importer is not established in a Member State they apply to the indirect customs representative.",
   "During the transitional period from 1 October 2023 until 31 December 2025, the obligations of the importer under this Regulation shall be limited to the reporting obligations set out in Articles 33, 34 and 35 of this Regulation.")
na("na.A32_LIMIT", "st.A32", "A32.P0", "pd.IMP", "have its obligations under the Regulation limited, during the transitional period from 1 October 2023 until 31 December 2025, to the reporting obligations set out in Articles 33, 34 and 35", "importer's obligations during the transitional period",
   "implementation", "declaratory",
   "During the transitional period from 1 October 2023 until 31 December 2025, the obligations of the importer under this Regulation shall be limited to the reporting obligations set out in Articles 33, 34 and 35 of this Regulation.",
   mech="temporal limitation of obligations", cond="transitional period from 1 October 2023 until 31 December 2025", nt="N0", eff="limits the importer's obligations to reporting during the transitional period",
   notc="does not itself create the reporting obligation (Article 35)", constraint="N", deriv="direct", deps="pd.IMP",
   unc="unc.TRANSITIONAL_TEMPORAL")
na("na.A32_ICR", "st.A32", "A32.P0", "pd.ICR", "bear the reporting obligations of Articles 33, 34 and 35 where the importer is established in a Member State, appoints the indirect customs representative and the representative agrees, or where the importer is not established in a Member State",
   "reporting obligations in the transitional period", "information_provision", "obligation",
   "Where the importer is not established in a Member State, the reporting obligations shall apply to the indirect customs representative.",
   mech="transfer of reporting obligations to the indirect customs representative", cond="transitional period; importer established in a Member State and appoints a representative who agrees, or importer not established in a Member State",
   nt="N0", eff="reporting obligations apply to the indirect customs representative", notc="the addressee of the reporting is identified in Article 35 (the Commission)", deriv="direct", deps="pd.ICR;pd.IMP", ext="ext.UCC_PERSONS",
   unc="unc.TRANSITIONAL_TEMPORAL")
st("st.A33P1", "A33.P1", "relation_bearing",
   "The customs authorities shall inform the importer or, in the situations covered by Article 32, the indirect customs representative of the reporting obligation referred to in Article 35 no later than at the moment of the release of goods for free circulation.",
   "The customs authorities shall inform the importer or, in the situations covered by Article 32, the indirect customs representative of the reporting obligation referred to in Article 35")
st("st.A33P2", "A33.P2", "relation_bearing",
   "The customs authorities shall periodically and automatically communicate to the Commission information on imported goods, including processed products from outward processing: EORI number of the customs declarant and of the importer, eight-digit CN code, quantity, country of origin, date of the customs declaration and customs procedure.",
   "The customs authorities shall periodically and automatically")
st("st.A33P3", "A33.P3", "relation_bearing",
   "The Commission shall communicate the information of paragraph 2 to the competent authorities of the Member States where the customs declarant and, where applicable, the importer are established.",
   "The Commission shall communicate the information referred to in paragraph 2 to the competent authorities of the Member States where the customs declarant and, where applicable, the importer are established.")
qr("qr.A33_INFORM", "st.A33P1", "A33.P1", "pd.CUST", "pd.IMP", "information_reporting", "customs authorities -> importer (or indirect customs representative)",
   "inform the importer or, in the situations covered by Article 32, the indirect customs representative of the reporting obligation referred to in Article 35 no later than at the moment of the release of goods for free circulation",
   "reporting obligation of Article 35", "information_provision", "obligation",
   "The customs authorities shall inform the importer or, in the situations covered by Article 32, the indirect customs representative of the reporting obligation referred to in Article 35",
   extra="pd.ICR", mech="information at release for free circulation", cond="no later than at the moment of the release of goods for free circulation; transitional period", acls="INFO", asuff="sufficient",
   authattr="binding duty on the customs authorities", discattr="none stated", deps="pd.CUST;pd.IMP;pd.ICR", ext="ext.UCC_PERSONS", unc="unc.TRANSITIONAL_TEMPORAL")
qr("qr.A33_COMM", "st.A33P2", "A33.P2", "pd.CUST", "pd.COM", "information_reporting", "customs authorities -> Commission",
   "periodically and automatically communicate to the Commission information on imported goods (EORI number of the customs declarant and of the importer, eight-digit CN code, quantity, country of origin, date of the customs declaration and customs procedure)",
   "information on imported goods", "information_provision", "obligation",
   "The customs authorities shall periodically and automatically",
   mech="automatic communication, in particular by means of the surveillance mechanism established pursuant to Article 56(5) of Regulation (EU) No 952/2013 or by electronic means of data transmission", instr="INS-TYPE: surveillance mechanism (external)",
   cond="goods imported (including processed products resulting from the outward processing procedure)", acls="INFO", asuff="sufficient", authattr="binding duty on the customs authorities", discattr="none stated",
   deps="pd.CUST;pd.COM", ext="ext.UCC_SURVEIL", gap="The surveillance mechanism and the customs authorities' own constitution are external to W.")
qr("qr.A33_COM2CA", "st.A33P3", "A33.P3", "pd.COM", "pd.CA", "information_reporting", "Commission -> competent authorities of the Member States where the customs declarant and the importer are established",
   "communicate the information received from the customs authorities to the competent authorities of the Member States where the customs declarant and, where applicable, the importer are established", "information on imported goods",
   "information_provision", "obligation",
   "The Commission shall communicate the information referred to in paragraph 2 to the competent authorities of the Member States where the customs declarant and, where applicable, the importer are established.",
   mech="communication", cond="information received under Article 33(2)", acls="INFO", asuff="sufficient", authattr="binding duty on the Commission", discattr="none stated",
   deps="pd.COM;pd.CA", gap="No competent authority is evidenced in W.", iunits="A33.P2")
st("st.A34", "A34.P1;A34.P2;A34.P2.pta;A34.P2.ptb", "scope",
   "Where processed products from inward processing are imported the reporting obligation of Article 35 includes information on the goods placed under inward processing, even if the processed products are not listed in Annex I, including returned goods under Article 205 of Regulation (EU) No 952/2013; the reporting obligation does not apply to processed products from outward processing or to returned goods under Article 203 of that Regulation.",
   "the reporting obligation referred to in Article 35 of this Regulation shall include the information on the goods that were placed under the inward processing procedure")
st("st.A35P1", "A35.P1;A35.P2;A35.P2.pta;A35.P2.ptb;A35.P2.ptc;A35.P2.ptd", "relation_bearing",
   "Each importer or, in the situations covered by Article 32, the indirect customs representative, having imported goods during a quarter, shall submit a CBAM report for that quarter to the Commission no later than one month after the end of that quarter, including the total quantity of each type of goods per installation, the actual total embedded emissions, total indirect emissions and the carbon price due in the country of origin.",
   "shall, for that quarter, submit a report (‘CBAM report’) containing information on the goods imported during that quarter, to the Commission, no later than one month after the end of that quarter")
st("st.A35P3", "A35.P3", "relation_bearing",
   "The Commission shall periodically communicate to the relevant competent authorities a list of the importers or indirect customs representatives established in the Member State, with justifications, which it has reasons to believe have failed to submit a CBAM report.",
   "The Commission shall periodically communicate to the relevant competent authorities a list of those importers or indirect customs representatives established in the Member State")
st("st.A35P4", "A35.P4", "relation_bearing",
   "Where the Commission considers a CBAM report incomplete or incorrect it communicates to the competent authority of the Member State where the importer or representative is established the additional information it considers necessary, for indicative purposes and without prejudice to the authority's definitive appreciation; that competent authority initiates the correction procedure and notifies the importer or representative, who submits where appropriate a corrected report to the competent authority and the Commission.",
   "Such information shall be provided for indicative purposes and without prejudice to the definitive appreciation by that competent authority.")
st("st.A35P5", "A35.P5;A35.P5.pta;A35.P5.ptb;A35.P5.ptc;A35.P5.ptd;A35.P5.pte", "relation_bearing",
   "Where the competent authority determines that the importer or representative has not taken the necessary steps to correct a report or failed to submit a report, it shall impose an effective, proportionate and dissuasive penalty, notifying the importer or representative and informing the Commission of the conclusion and reasons, the amount, the due date, the action to pay and the right to appeal.",
   "that competent authority shall impose an effective, proportionate and dissuasive penalty on the importer or, where applicable in accordance with Article 32, the indirect customs representative")
st("st.A35P6", "A35.P6", "relation_bearing",
   "Where the competent authority, after receiving the information from the Commission under Article 35, decides not to take any action, it shall inform the Commission accordingly.",
   "the competent authority shall inform the Commission accordingly")
st("st.A35P7", "A35.P7;A35.P7.pta;A35.P7.ptb;A35.P7.ptc;A35.P7.ptd;A35.P7.pte;A35.P7.sub2", "assignment_bearing",
   "The Commission is empowered to adopt implementing acts on the information to be reported and the format, the indicative range of penalties and criteria for the actual amount, rules on conversion of the carbon price into euro, detailed rules on the Annex IV calculation elements and the format for indirect emissions reporting, under the examination procedure of Article 29(2), applying to goods imported during the transitional period and building on existing legislation for EU ETS installations.",
   "The Commission is empowered to adopt implementing acts concerning:")
qr("qr.A35_REPORT", "st.A35P1", "A35.P1;A35.P2;A35.P2.pta;A35.P2.ptb;A35.P2.ptc;A35.P2.ptd;A32.P0;A34.P1;A34.P2", "pd.IMP", "pd.COM", "information_reporting", "importer (or indirect customs representative) -> Commission",
   "submit, for each quarter in which goods were imported, a CBAM report containing the total quantity of each type of goods per installation, the actual total embedded emissions, the total indirect emissions and the carbon price due in the country of origin, to the Commission no later than one month after the end of the quarter",
   "quarterly CBAM report", "information_provision", "obligation",
   "Each importer or, in the situations covered by Article 32, the indirect customs representative, having imported goods during a given quarter of a calendar year shall",
   extra="pd.ICR", tnote="n-ary: the reporting party is the importer or, in the situations covered by Article 32, the indirect customs representative", mech="quarterly report", instr="INS-TYPE: CBAM report",
   cond="goods imported during a quarter; no later than one month after the end of the quarter; reporting obligations apply during the transitional period (Article 32); special rules for inward processing, outward processing and returned goods (Article 34)",
   authattr="binding reporting duty; the Commission is the recipient", discattr="content fixed by A35(2) and implementing acts", acls="INFO", asuff="sufficient",
   deps="pd.IMP;pd.ICR;pd.COM", ext="ext.UCC_PROCESSING", unc="unc.TRANSITIONAL_TEMPORAL", iunits="A32.P0;A34.P1;A34.P2")
qr("qr.A35_LIST", "st.A35P3", "A35.P3", "pd.COM", "pd.CA", "information_reporting", "Commission -> relevant competent authorities",
   "periodically communicate to the relevant competent authorities a list of importers or indirect customs representatives established in the Member State, with justifications, which it has reasons to believe have failed to comply with the obligation to submit a CBAM report",
   "list of suspected non-reporting importers", "information_provision", "obligation",
   "The Commission shall periodically communicate to the relevant competent authorities a list of those importers or indirect customs representatives established in the Member State",
   mech="list with justifications", instr="INS-TYPE: list", cond="the Commission has reasons to believe that the importer or representative failed to submit a CBAM report", acls="INFO", asuff="sufficient",
   authattr="binding duty on the Commission", discattr="'reasons to believe' judged by the Commission", deps="pd.COM;pd.CA", gap="No competent authority is evidenced in W.", unc="unc.TRANSITIONAL_TEMPORAL")
qr("qr.A35_CORR_COM", "st.A35P4", "A35.P4", "pd.COM", "pd.CA", "information_reporting", "Commission -> competent authority of the Member State where the importer or representative is established",
   "communicate the additional information it considers necessary to complete or correct a CBAM report it considers incomplete or incorrect, for indicative purposes and without prejudice to the definitive appreciation by that competent authority",
   "additional information needed to complete or correct a CBAM report", "information_provision", "obligation",
   "it shall communicate to the competent authority of the Member State where the importer is established",
   mech="communication of additional information (indicative)", cond="the Commission considers that a CBAM report is incomplete or incorrect", acls="INFO", asuff="sufficient",
   authattr="the Commission's input is non-binding on the competent authority (indicative; without prejudice to its definitive appreciation)", discattr="competent authority retains the definitive appreciation",
   deps="pd.COM;pd.CA", gap="No competent authority is evidenced in W.", unc="unc.TRANSITIONAL_TEMPORAL")
qr("qr.A35_CORR_CA", "st.A35P4", "A35.P4", "pd.CA", "pd.IMP", "authority_control", "competent authority -> importer (or indirect customs representative)",
   "initiate the correction procedure and notify the importer or, in the situations covered by Article 32, the indirect customs representative of the additional information necessary to correct the report", "correction of a CBAM report",
   "enforcement", "obligation",
   "That competent authority shall initiate the correction procedure and notify the importer or, in the situations covered by Article 32, the indirect customs representative of the additional information necessary to correct that report.",
   extra="pd.ICR", mech="correction procedure and notification", instr="", cond="the Commission has communicated additional information under Article 35(4)",
   authattr="competent authority runs the correction procedure", discattr="none stated", deps="pd.CA;pd.IMP;pd.ICR", gap="No competent authority is evidenced in W.", unc="unc.TRANSITIONAL_TEMPORAL")
qr("qr.A35_CORR_SUBMIT", "st.A35P4", "A35.P4", "pd.IMP", "pd.CA", "information_reporting", "importer (or indirect customs representative) -> competent authority and Commission",
   "submit, where appropriate, a corrected report to the competent authority concerned and to the Commission", "corrected CBAM report", "information_provision", "obligation",
   "Where appropriate, that importer or that indirect customs representative shall submit a corrected report to the competent authority concerned and to the Commission.",
   extra="pd.ICR;pd.COM", mech="corrected report", instr="INS-TYPE: CBAM report", cond="where appropriate, following the notification of additional information necessary for correction", acls="INFO", asuff="sufficient",
   authattr="binding duty on the importer or representative", discattr="'where appropriate'", deps="pd.IMP;pd.ICR;pd.CA;pd.COM", unc="unc.TRANSITIONAL_TEMPORAL")
qr("qr.A35_PENALTY", "st.A35P5", "A35.P5;A35.P5.pta;A35.P5.ptb;A35.P5.ptc;A35.P5.ptd;A35.P5.pte", "pd.CA", "pd.IMP", "authority_control", "competent authority -> importer (or indirect customs representative)",
   "impose an effective, proportionate and dissuasive penalty where the importer or representative has not taken the necessary steps to correct the CBAM report or has failed to submit a report, and notify the importer or representative of the conclusion and its reasons, the amount, the due date, the action to take to pay and the right to appeal",
   "penalty for failure to report or to correct a report", "enforcement", "obligation",
   "that competent authority shall impose an effective, proportionate and dissuasive penalty on the importer or, where applicable in accordance with Article 32, the indirect customs representative",
   extra="pd.ICR", mech="administrative penalty decision with notification", instr="INS-TYPE: penalty decision",
   cond="the competent authority determines that the importer or representative has not taken the necessary steps to correct the report, or has failed to submit a report",
   authattr="competent authority imposes the penalty (binding decision)", discattr="amount to be guided by an indicative range and criteria set by implementing acts (A35(7)(b)); in W 'effective, proportionate and dissuasive'",
   acls="INFO", asuff="indeterminate", amiss="reasons and the right to appeal are notified but no appeal forum, assessment capacity or consequence is identified in W",
   deps="pd.CA;pd.IMP;pd.ICR", unc="unc.APPEAL_FORUM", hq="hq.ACCOUNT_APPEAL", gap="No competent authority is evidenced in W.", epi="documented")
qr("qr.A35_PENALTY_INFO", "st.A35P5", "A35.P5", "pd.CA", "pd.COM", "information_reporting", "competent authority -> Commission",
   "inform the Commission of the conclusion of non-compliance and its reasons, the amount of the penalty, the date from which it is due, the action to take to pay and the right to appeal", "penalty decisions on reporting",
   "information_provision", "obligation",
   "To that end, the competent authority shall notify the importer or, where applicable in accordance with Article 32, the indirect customs representative and inform the Commission, of the following:",
   mech="communication", cond="the competent authority imposes a penalty under Article 35(5)", acls="INFO", asuff="sufficient", authattr="binding duty on the competent authority", discattr="none stated",
   deps="pd.CA;pd.COM", unc="unc.TRANSITIONAL_TEMPORAL")
qr("qr.A35_NOACT", "st.A35P6", "A35.P6", "pd.CA", "pd.COM", "information_reporting", "competent authority -> Commission",
   "inform the Commission where, after receiving the information from the Commission under Article 35, it decides not to take any action", "decision not to act on Commission information", "information_provision", "obligation",
   "the competent authority shall inform the Commission accordingly",
   mech="communication", cond="the competent authority, after receiving information from the Commission under Article 35, decides not to take any action", acls="INFO", asuff="sufficient",
   authattr="binding duty on the competent authority; no duty to justify the decision is stated", discattr="none stated", deps="pd.CA;pd.COM", unc="unc.TRANSITIONAL_TEMPORAL")
na("na.A35P7_IMPL", "st.A35P7", "A35.P7;A35.P7.pta;A35.P7.ptb;A35.P7.ptc;A35.P7.ptd;A35.P7.pte;A35.P7.sub2", "pd.COM",
   "adopt implementing acts on the information to be reported and the format, the indicative range of penalties and criteria for the actual amount, rules on conversion of the carbon price into euro, detailed rules on the Annex IV calculation elements and the format of the reporting of indirect emissions",
   "implementing acts on the transitional CBAM report", "rule_making_standard_setting", "competence",
   "The Commission is empowered to adopt implementing acts concerning:",
   mech="implementing act under the examination procedure (Article 29(2)); applying to goods imported during the transitional period", instr="INS-TYPE: implementing act", nt="N3",
   eff="competence of the Commission to adopt implementing acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM", unc="unc.TRANSITIONAL_TEMPORAL")

# =============== ARTICLE 36 AND FINAL FORMULAS ===============
st("st.A36", "A36.P1;A36.P2;A36.P2.pta;A36.P2.ptb;FINAL.P1;FINAL.P2", "final_formal",
   "The Regulation enters into force on the day following its publication in the Official Journal and applies from 1 October 2023, with Articles 5, 10, 14, 16 and 17 applying from 31 December 2024 and Article 2(2), Articles 4, 6 to 9, 15 and 19, Article 20(1), (3), (4) and (5), Articles 21 to 27 and Article 31 applying from 1 January 2026; it is binding in its entirety and directly applicable in all Member States; done at Strasbourg on 10 May 2023.",
   "This Regulation shall enter into force on the day following that of its publication in the Official Journal of the European Union.")
