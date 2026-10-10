# Authored external references (EXT): references to sources outside W; no retrieval; source_verification_status fixed not_checked
from reg import *

LI, TS, AA, ON = 'legal_instrument', 'technical_standard', 'administrative_act', 'other_normative'

ext('ext_tfeu_basis', ['s_cit1'], ['CIT1'],
    'Treaty on the Functioning of the European Union, Articles 91(1)(d), 192(1), 194(2) and 322(1)(a) (legal-basis citations in the preamble)',
    LI, 'other', [], 'specifies', 'N',
    'None: citation of the legal basis in a formal preamble element; not an operative reference and not used as a source of any relation.')
ext('ext_tfeu322', ['s_a12'], ['A12.P0'],
    'Treaty on the Functioning of the European Union, Article 322 and the horizontal financial rules adopted pursuant to it', LI,
    'supplies_rule_or_standard', ['na_a12'], 'specifies', 'N',
    'The content of the rules governing direct management is outside W; the duty of the Commission to implement the Fund under direct management is stated in W.')
ext('ext_fr_general', ['s_a12', 's_a11p1b', 's_a19p1', 's_a20p3', 's_a20p9'], ['A12.P0', 'A11.P1', 'A19.P1', 'A20.P3', 'A20.P9'],
    'Regulation (EU, Euratom) 2018/1046 (Financial Regulation): direct management, direct implementation under Article 62(1)(a), individual legal commitment, authorisation of disbursement, payment rules',
    LI, 'supplies_rule_or_standard', ['na_a12', 'qr_agreement', 'qr_paydec', 'qr_prorata', 'qr_transfer_in_use', 'qr_fund'], 'specifies', 'Y',
    'The mechanics of commitment, authorisation and payment are partly defined outside W; claims about them are restricted to what W states (within the declared corpus only); relations dependent on these rules are recorded at documented status where derived.',
    extra_units=['FN16'])
ext('ext_fr_budget', ['s_a10p1a', 's_a10p2', 's_a20p5', 's_a20p7a', 's_a20p10'], ['A10.P1', 'A10.P2', 'A20.P5', 'A20.P7', 'A20.P10'],
    'Regulation (EU, Euratom) 2018/1046, Articles 21(5), 22(2), 116(2), 14(3) and 12(4)(c) (budgetary rules to which W refers or from which it derogates)',
    LI, 'other', ['qr_terminate', 'qr_unused'], 'qualifies', 'N',
    'Derogations and references are recorded as stated; the scope of the derogated rules is outside W (described reference role: derogation or reference to budgetary rules).',
    extra_units=['FN16'])
ext('ext_fr_rights', ['s_a21p2b', 's_a21p2e1', 's_a21p2f'], ['A21.P2.ptb', 'A21.P2.pte', 'A21.P2.ptf'],
    'Regulation (EU, Euratom) 2018/1046, Articles 61 (conflicts of interests), 129(1) (rights of audit and control) and 132 (record keeping)', LI,
    'supplies_rule_or_standard', ['qr_auditauth', 'qr_agree_terms', 'qr_oblig_finrec'], 'specifies', 'Y',
    'The content of the rights exerted by the Commission, OLAF, the Court of Auditors and the EPPO, and of the record-keeping and conflict-of-interests standards, is outside W; claims about the scope of audit and control powers are restricted to the authorisation obligation stated in W.',
    extra_units=['FN16'])
ext('ext_fr_pub', ['s_a23p1b'], ['A23.P1'],
    'Regulation (EU, Euratom) 2018/1046, Article 38(3) (cases in which publication is excluded)', LI, 'supplies_rule_or_standard',
    ['na_publish'], 'qualifies', 'N',
    'The cases excluded from publication are defined outside W; the publication duty is recorded with that condition.', extra_units=['FN16'])
ext('ext_discharge', ['s_a21p3b'], ['A21.P3'],
    'Treaty on the Functioning of the European Union, Article 319 (discharge procedure) and Regulation (EU, Euratom) 2018/1046, Article 247 (integrated financial and accountability reporting; annual management and performance report)',
    LI, 'supplies_rule_or_standard', ['na_report_discharge'], 'conditions', 'Y',
    'The discharge authority, its capacities and the consequences of discharge are not stated in W; no accountability relation toward a discharge authority is admitted; any such claim is undetermined.',
    extra_units=['FN16'])
ext('ext_tfeu311', ['s_a27p4'], ['A27.P4'],
    'Treaty on the Functioning of the European Union, Article 311(3) (own resources)', LI, 'other', ['na_propose2'], 'conditions', 'Y',
    'The norm applies only if revenue from auctioning is established as an own resource under an external act; legal status recorded conditional_on_further_act; the claim is undetermined within W.')
ext('ext_ets_revenue', ['s_a10p1a', 's_a20p9', 's_a19p1'], ['A10.P1', 'A20.P9', 'A19.P1'],
    'Directive 2003/87/EC, Articles 10a(8b), 30d(3) and 30d(4) (auctioning revenue made available to the Fund; annual amounts; assigned revenue)',
    LI, 'supplies_rule_or_standard', ['qr_fund', 'qr_paydec', 'qr_prorata', 'qr_agreement', 'na_a10p3'], 'conditions', 'Y',
    'Availability and amounts of funding for payments rest on external provisions; claims about funding availability are undetermined and payment-related claims are scoped within the declared corpus only.',
    extra_units=['FN6'])
ext('ext_ets_postpone', ['s_a10p1b', 's_a19p1'], ['A10.P1', 'A19.P1'],
    'Directive 2003/87/EC, Articles 30k (postponement of the emissions trading system for buildings and road transport until 2028) and 30i; Chapter IVa',
    LI, 'supplies_rule_or_standard', ['qr_fund', 'qr_agreement'], 'conditions', 'Y',
    'Which maximum amount (EUR 65 000 000 000 or EUR 54 600 000 000) and which timing of the agreements apply depends on an external event; the claim is scoped to both branches as stated in W.',
    extra_units=['FN6'])
ext('ext_ets_distrib', ['s_a20p10', 's_a27p4'], ['A20.P10', 'A27.P4'],
    'Directive 2003/87/EC, Article 30d(5) (rules for distribution of allowances)', LI, 'supplies_rule_or_standard',
    ['qr_unused', 'na_propose2'], 'specifies', 'Y',
    'The distribution keys applied to unused appropriations are outside W; the allocation to Member States is recorded without those keys.', extra_units=['FN6'])
ext('ext_ets_scope', ['s_a1p3', 's_a2_vh', 's_a2_vme', 's_a2_vtu', 's_a3p1', 's_a27p2'],
    ['A1.P3', 'A2.P0.pt10', 'A2.P0.pt11', 'A2.P0.pt12', 'A3.P1', 'A27.P2.ptd'],
    'Directive 2003/87/EC (inclusion of greenhouse gas emissions from buildings and road transport within its scope; Chapter IVa)', LI, 'defines_term',
    ['p_vh', 'p_vme', 'p_vtu', 'qr_eval1'], 'qualifies', 'N',
    'The price-impact criterion in the vulnerable-group definitions refers to the scope of the Directive; its content is outside W.', extra_units=['FN6'])
ext('ext_ets_md', ['s_a22'], ['A22.P0'], 'Directive 2003/87/EC, Article 10d (Modernisation Fund)', LI, 'other',
    ['na_coord_com', 'na_coord_ms'], 'qualifies', 'N', 'The Modernisation Fund is a coordination target only; no relation of W depends on its content.', extra_units=['FN6'])
ext('ext_cpr_transfer', ['s_a11p1a', 's_a11p2a', 's_a11p2b', 's_a11p3a', 's_a6p3'], ['A11.P1', 'A11.P2', 'A11.P3', 'A6.P3.ptb'],
    'Regulation (EU) 2021/1060 (Common Provisions Regulation): conditions for transfers, funds under shared management, programmes, managing authorities of cohesion policy programmes',
    LI, 'designates_competence', ['qr_transfer_in', 'qr_transfer_in_use', 'qr_transfer_out', 'qr_entrust', 'p_manauth'], 'constitutes', 'Y',
    'The managing authorities (position), the transfer conditions and the rules of the receiving funds are outside W; claims about transfers and entrustment are restricted to the highest level supported by W (relation level, documented).',
    extra_units=['FN12'])
ext('ext_cpr_amend', ['s_a28p0', 's_a28i1', 's_a28i2a', 's_a28i2b', 's_a28i3', 's_a28i4'],
    ['A28.P0', 'A28.INS26a.P1', 'A28.INS26a.P2', 'A28.INS26a.P3', 'A28.INS26a.P4', 'A28.INS26a.P5'],
    'Regulation (EU) 2021/1060 as amended by insertion of Article 26a (amended act; references to its Articles 6(1), 18, 24, 86(1), 105(1) and 110)', LI,
    'other', ['na_a28i2a', 'na_a28i2b', 'na_a28i3', 'qr_transfer_out'], 'specifies', 'Y',
    'Reference role: amendment of another instrument (GAP-02). The legal effect expressed in W is coded; the amended act is not added to W and not analysed; interaction with the amended act is undetermined.',
    extra_units=['FN12'])
ext('ext_gov_report', ['s_a18p5b', 's_a24p1a'], ['A18.P5', 'A24.P1'],
    'Regulation (EU) 2018/1999, Articles 17 and 28 (integrated national energy and climate progress reports)', LI, 'supplies_rule_or_standard',
    ['qr_report', 'qr_selfassess_submit'], 'specifies', 'Y',
    'The vehicle, timing and content of the integrated report are defined outside W; reporting claims are scoped to the Plan-implementation report as stated in A24.P1 and A18.P5.',
    extra_units=['FN14'])
ext('ext_gov_plans', ['s_a4p2', 's_a6p3', 's_a16_ext1'], ['A4.P2', 'A6.P3.pte', 'A16.P3.pta.pti'],
    'Regulation (EU) 2018/1999 (updated integrated national energy and climate plans; Articles 9(3), 13, 14(2), 29 and 34)', LI,
    'supplies_rule_or_standard', ['na_consist_necp', 'na_consist_plans', 'qr_assess'], 'qualifies', 'N',
    'The content of the referenced plans and assessments is outside W; the consistency duty is recorded as stated.', extra_units=['FN14'])
ext('ext_gov_consult', ['s_a5p1b'], ['A5.P1'], 'Regulation (EU) 2018/1999, Article 10 (public consultation requirements)', LI,
    'supplies_rule_or_standard', ['qr_consult'], 'specifies', 'N',
    'The detailed consultation requirements are outside W; the consultation relation is recorded as stated.', extra_units=['FN14'])
ext('ext_gov_anx4', ['s_anx4c'], ['ANX4.pt19'], 'Regulation (EU) 2018/1999, Articles 3(3)(d) and 24(b) (energy poverty reporting)', LI,
    'supplies_rule_or_standard', ['qr_report'], 'specifies', 'N', 'Which Member States are concerned by Article 3(3)(d) is determined outside W.', extra_units=['FN14'])
ext('ext_recomm_2020_1563', ['s_anx4c'], ['ANX4.pt19'],
    'Commission Recommendation (EU) 2020/1563 of 14 October 2020 on energy poverty (OJ L 357, 27.10.2020, p. 35) and Eurostat indicators', ON,
    'supplies_rule_or_standard', ['qr_report'], 'specifies', 'N',
    'Indicators are referred to as usable, not mandatory; no relation depends on them.', extra_units=['ANX4.FN1'])
ext('ext_dnsh', ['s_a7p3', 's_a6p5', 's_a16_ext3', 's_a6p1'], ['A7.P3', 'A6.P5', 'A16.P3.pta.ptii', 'A6.P1.ptl'],
    "Regulation (EU) 2020/852, Article 17 ('do no significant harm')", LI, 'defines_term', ['na_dnsh', 'qr_guidance', 'qr_assess'], 'specifies', 'N',
    "The substantive criteria of 'significant harm' are outside W; compliance with the principle cannot be assessed within W.", extra_units=['FN13'])
ext('ext_climatelaw', ['s_a7p2b'], ['A7.P2'], 'Regulation (EU) 2021/1119 (European Climate Law)', LI, 'supplies_rule_or_standard',
    ['na_milestones_content'], 'qualifies', 'N', 'The objective of the Climate Law is a compatibility reference for milestones and targets.', extra_units=['FN5'])
ext('ext_tsi', ['s_a6p4b', 's_a11p4a'], ['A6.P4', 'A11.P4'], 'Regulation (EU) 2021/240 (Technical Support Instrument), including Article 7', LI,
    'supplies_rule_or_standard', ['na_request_tech', 'na_a11p4', 'na_a18p1b'], 'specifies', 'N',
    'The provider, conditions and procedure of technical support are outside W.', extra_units=['FN30'])
ext('ext_elena', ['s_a6p4b'], ['A6.P4'],
    'European Local ENergy Assistance (ELENA) facility, established by an Agreement between the Commission and the European Investment Bank in 2009', AA,
    'supplies_rule_or_standard', ['na_request_tech'], 'specifies', 'N', 'The provider and conditions of ELENA support are outside W; no counterparty is recorded.')
ext('ext_investeu', ['s_a11p4a'], ['A11.P4'], 'Regulation (EU) 2021/523 (InvestEU Programme), Member State compartment', LI,
    'supplies_rule_or_standard', ['na_a11p4'], 'specifies', 'N', 'The rules of the Member State compartment are outside W.', extra_units=['FN31'])
ext('ext_rrf', ['s_a6p3'], ['A6.P3.ptc'], 'Regulation (EU) 2021/241 (Recovery and Resilience Facility; recovery and resilience plans)', LI,
    'other', ['na_consist_plans'], 'qualifies', 'N', 'Consistency reference only; described reference role: consistency target.', extra_units=['FN11'])
ext('ext_jtf', ['s_a6p3'], ['A6.P3.ptf'], 'Regulation (EU) 2021/1056 (Just Transition Fund; territorial just transition plans)', LI,
    'other', ['na_consist_plans'], 'qualifies', 'N', 'Consistency reference only; described reference role: consistency target.', extra_units=['FN15'])
ext('ext_pillar', ['s_a6p3'], ['A6.P3.pta'], 'European Pillar of Social Rights Action Plan', ON, 'other', ['na_consist_plans'], 'qualifies', 'N',
    'Consistency reference only; described reference role: consistency target; no version or date stated in the cited provision.')
ext('ext_epbd', ['s_a2_ext2', 's_a6p3', 's_anx4b'], ['A2.P0.pt13', 'A6.P3.ptd', 'ANX4.pt9'],
    'Directive of the European Parliament and of the Council on the energy performance of buildings (recast), referred to in W without number or date',
    LI, 'defines_term', ['na_consist_plans', 'qr_report'], 'specifies', 'N',
    'The referred instrument is not identified by number or date within W and cannot be verified; the relevant requirements are outside W.')
ext('ext_ee_directive', ['s_a16_ext2', 's_anx4d'], ['A16.P3.ptb.ptiii', 'ANX4.pt20'],
    'Directive of the European Parliament and of the Council on energy efficiency (recast), referred to in W without number or date', LI,
    'supplies_rule_or_standard', ['qr_assess', 'qr_report'], 'specifies', 'N', 'Referred to without number or date; outside W and unverified.')
ext('ext_afi_reg', ['s_a16_ext2', 's_anx4b'], ['A16.P3.ptb.ptiii', 'ANX4.pt33'],
    'Regulation of the European Parliament and of the Council on the deployment of alternative fuels infrastructure, repealing Directive 2014/94/EU, referred to in W without number or date',
    LI, 'defines_term', ['qr_assess', 'qr_report'], 'specifies', 'N', 'Referred to without number or date; outside W and unverified.')
ext('ext_re_directive', ['s_a2_ext2', 's_a16_ext2', 's_anx4b'], ['A2.P0.pt7', 'A2.P0.pt17', 'A2.P0.pt18', 'A16.P3.ptb.ptiii', 'ANX4.pt13'],
    'Directive (EU) 2018/2001 (renewable energy), including Article 2 definitions', LI, 'defines_term', ['qr_assess', 'qr_report'], 'specifies', 'N',
    'Definitions of renewable energy, renewable energy community and peer-to-peer trading are outside W.', extra_units=['FN25'])
ext('ext_dir2019944', ['s_a2_ext2'], ['A2.P0.pt15', 'A2.P0.pt16'], 'Directive (EU) 2019/944, Article 2 points (8) and (11) (active customer; citizen energy community)', LI,
    'defines_term', [], 'specifies', 'N', 'Defined terms used in A8.P1; no relation depends on them.', extra_units=['FN28'])
ext('ext_reg20191700', ['s_a2_ext1'], ['A2.P0.pt8'], 'Regulation (EU) 2019/1700, Article 2 point (15) (private household)', LI, 'defines_term',
    ['p_vh', 'qr_pass_on'], 'specifies', 'Y',
    "Scope of 'household' (and therefore of the vulnerable households category) rests on an external definition; claims on the extent of the category are within the declared corpus only.",
    extra_units=['FN26'])
ext('ext_reg6512014', ['s_a2_ext1'], ['A2.P0.pt9'], 'Commission Regulation (EU) No 651/2014, Articles 3 to 6 of Annex I (calculation of enterprise size)', LI,
    'defines_term', ['p_vme', 'qr_pass_on'], 'specifies', 'Y',
    "Scope of 'micro-enterprise' (and therefore of the vulnerable micro-enterprises category) rests on an external calculation rule; claims on the extent of the category are within the declared corpus only.",
    extra_units=['FN27'])
ext('ext_reg2019631', ['s_a2_ext2'], ['A2.P0.pt19'], 'Regulation (EU) 2019/631, Article 3(1) point (m) (zero- and low-emission vehicle)', LI, 'defines_term', [],
    'specifies', 'N', 'Defined term used in eligible measures; no relation depends on it.', extra_units=['FN29'])
ext('ext_dir_2023_959', ['s_a29p2'], ['A29.P2'],
    'Directive (EU) 2023/959 amending Directive 2003/87/EC as regards Chapter IVa (date by which Member States are to bring it into force)', LI,
    'other', ['p_fund'], 'qualifies', 'N',
    'The application date of W is stated as a fixed date (30 June 2024); the external reference only explains the date; no claim depends on the content of the Directive.',
    extra_units=['FN37'])
ext('ext_opendata', ['s_a23p1a'], ['A23.P1'], 'Directive (EU) 2019/1024, Article 5(1) (open data formats)', LI, 'supplies_rule_or_standard', ['na_publish'],
    'specifies', 'N', 'The format requirements are outside W.', extra_units=['FN35'])
ext('ext_gdpr', ['s_a21p3a'], ['A21.P3'], 'Regulation (EU) 2016/679 and Regulation (EU) 2018/1725 (personal data protection)', LI, 'supplies_rule_or_standard',
    ['na_data_ms', 'na_data_com'], 'qualifies', 'N', 'The applicable data protection regime is outside W.', extra_units=['FN18', 'FN19'])
ext('ext_eppo', ['s_a21p2e1', 's_anx3_6b'], ['A21.P2.pte', 'ANX3.pt6.ptb'],
    'Regulation (EU) 2017/1939 (European Public Prosecutor’s Office; enhanced cooperation)', LI, 'constitutes_position',
    ['p_eppo', 'qr_auditauth', 'qr_access'], 'constitutes', 'Y',
    'The EPPO as a position and the identity of the Member States participating in enhanced cooperation are determined outside W; the relations are recorded with the EPPO as a recipient only where participation applies.',
    extra_units=['FN23'])
ext('ext_dir_procure', ['s_a21p2g'], ['A21.P2.cont1'], 'Directive 2014/24/EU, Article 4 (Union thresholds for public procurement)', LI, 'supplies_rule_or_standard',
    ['qr_agree_terms'], 'specifies', 'N', 'The threshold values are outside W.', extra_units=['FN34'])
ext('ext_dir_amld', ['s_a21p2d'], ['A21.P2.ptd.ptiii'], 'Directive (EU) 2015/849, Article 3 point (6) (beneficial owner)', LI, 'defines_term',
    ['qr_agree_terms'], 'specifies', 'N', 'The definition of beneficial owner is outside W.', extra_units=['FN33'])
ext('ext_reg2018_842', ['s_anx1', 's_a27p2'], ['ANX1.pt8', 'ANX1.pt33', 'A27.P2.ptd'],
    'Regulation (EU) 2018/842, Article 4(2) and (3) (reference emissions; annual greenhouse gas emission reductions)', LI, 'supplies_rule_or_standard',
    ['qr_fund', 'qr_eval1'], 'specifies', 'N',
    'The values of reference emissions used in the Annex I methodology are outside W; allocation shares are not recomputed.', extra_units=['FN36'])
ext('ext_ipcc', ['s_anx1', 's_anx4b'], ['ANX1.pt8', 'ANX1.pt33', 'ANX4.pt18', 'ANX4.pt41'],
    '2006 IPCC Guidelines for National Greenhouse Gas Inventories (emission sources 1A3b, 1A4a and 1A4b)', TS, 'supplies_rule_or_standard',
    ['qr_fund', 'qr_report'], 'specifies', 'N', 'A technical standard, not a legal source in the strict sense; outside W.')
ext('ext_reg2020_2092', ['s_a12'], ['A12.P0'], 'Regulation (EU, Euratom) 2020/2092 (general regime of conditionality for the protection of the Union budget)', LI,
    'other', ['na_a12'], 'qualifies', 'N',
    'Described reference role: conditionality regime applicable to implementation; its application to payments cannot be assessed within W.', extra_units=['FN17'])
ext('ext_national_law', ['s_a5p1b', 's_a21p1a'], ['A5.P1', 'A21.P1'],
    'National legal framework of the Member State; applicable Union and national law (generic reference; no specific instrument identified in W)', ON,
    'supplies_rule_or_standard', ['qr_consult', 'na_a21p1a'], 'qualifies', 'N',
    'Generic reference; the content of national law is outside W; the relations are recorded as stated.')
