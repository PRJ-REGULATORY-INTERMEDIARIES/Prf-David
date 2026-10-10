# Authored normative assignments (P): duties, powers, permissions attached to positions without an identifiable counterparty
from reg import *

PLANART = 'INS-TYPE: Social Climate Plan (documentary artifact; not a device)'
UNRES = 'FUNCTION_VOCABULARY_UNRESOLVED'

EXTY = {'na_a12', 'na_report_discharge', 'na_propose2', 'na_a28i2a', 'na_a28i2b', 'na_a28i3', 'na_a10p3'}

_EFFECT = {
    'obligation': ('duty (obligation) of the bearer as stated',
                   'does not constitute any entity, competence or counterparty relation'),
    'obligation_promotional': ('promotional duty (obligation of means) of the bearer as stated',
                               'does not constitute any entity, competence or counterparty relation'),
    'permission': ('permission/competence of the bearer as stated',
                   'does not constitute a duty, an entity, or a counterparty relation'),
    'competence': ('competence of the bearer as stated', 'does not constitute a duty, an entity, or a counterparty relation'),
    'entitlement': ('entitlement of the bearer as stated (obligor not identified in the provision)',
                    'does not constitute the obligor, an entity, or a counterparty relation'),
    'prohibition': ('constraint on the bearer (prohibition / limit) as stated',
                    'not admitted as a relation; constrains the bearer only (RGAM-DR-16)'),
}


def N(key, sts, subj, action, obj, fn, mod, mech='', instr='', cond='', cp='', cpstat='NONE_IDENTIFIABLE', nt='N0',
      effect=None, notc=None, constraint=None, deriv='direct', rule='', ind=(), legal='in_force', epi=None,
      unc=(), hq=(), deps=None, units=None, span=None):
    e, n = _EFFECT[mod]
    if nt == 'N2':
        e = 'obligation to establish/designate (N2): constitutes the obligation, not the entity'
        n = 'the entity/arrangement itself is not constituted by this norm (N2)'
    if nt == 'N4':
        e = 'conditional constitution (N4): effective after the condition is met'
    if constraint is None:
        constraint = 'Y' if mod == 'prohibition' else 'N'
    ind = list(L(ind))
    if epi is None:
        # status rule: legal_constitution_evidenced only for direct norms in force whose constitution does not rest on an unresolved external reference
        if deriv == 'direct' and legal == 'in_force' and key not in EXTY:
            epi = 'legal_constitution_evidenced'
            for x in ('A29.P1', 'A29.P2', 'FIN.BIND'):
                if x not in ind:
                    ind.append(x)
        else:
            epi = 'documented'
    return na(key, sts, subj, action, obj, fn, mech, instr, mod, cond, cp, cpstat, nt, effect or e, notc or n,
              constraint=constraint, deriv=deriv, rule=rule, deps=deps, legal=legal, epi=epi, unc=unc, hq=hq,
              ind=ind, units=units, span=span)


R_PLAN = ("The sentence's grammatical subject is 'the Plan' (a documentary artifact, not a position); the duty is attributed to "
          "the submitting Member State by A4.P1 ('Each Member State shall submit ... its Plan').")

# ---- Chapter II
N('na_content1', 's_a4p1b', 'p_ms', 'ensure that its Plan contains a coherent set of national measures and investments',
  'existing or new national measures and investments addressing the impact of carbon pricing on vulnerable households, micro-enterprises and transport users, to ensure affordable heating, cooling and mobility',
  'implementation', 'obligation', mech='Plan content requirement', instr=PLANART, deriv='derived', rule=R_PLAN,
  ind=['A6.P1'], deps=['p_ms'])
N('na_consist_necp', 's_a4p2', 'p_ms', 'ensure consistency between its Plan and its updated integrated national energy and climate plan',
  'consistency of the Plan with the updated integrated national energy and climate plan referred to in Article 14(2) of Regulation (EU) 2018/1999',
  'cooperation_coordination*', 'obligation', mech='consistency requirement between plans', instr=PLANART,
  unc=['u_residual_tag'])
N('na_a4p3', 's_a4p3', 'p_ms', 'include in the Plan national measures providing temporary direct income support',
  'temporary direct income support to vulnerable households and vulnerable transport users to reduce the impact of fossil fuel price increases',
  'implementation', 'permission', mech='Plan content option', instr=PLANART, nt='N3',
  deriv='derived', rule=R_PLAN, ind=['A4.P1'])
N('na_a4p4', 's_a4p4', 'p_ms', 'include in the Plan national and, where relevant, local and regional measures and investments',
  'measures and investments, in accordance with Article 8, to carry out building renovation and decarbonise heating and cooling, and to increase the uptake of zero- and low-emission mobility and transport',
  'implementation', 'obligation', mech='Plan content requirement', instr=PLANART, cond='in accordance with Article 8',
  deriv='derived', rule=R_PLAN, ind=['A4.P1', 'A8.P1'])
N('na_a4p5', 's_a4p5', 'p_ms', 'include in the Plan national measures already in place to mitigate social impacts',
  'existing national mitigation measures', 'implementation', 'permission', mech='Plan content option', instr=PLANART,
  cond='the Member State already has in place a national emission trading system for buildings and road transport or a carbon tax; the measures comply with this Regulation',
  nt='N3')
N('na_consult_summary', 's_a5p2', 'p_ms', "include in its Plan a summary of the consultation held and of how stakeholder input is reflected",
  'summary of the public consultation (A5.P1) and of how the input of participating stakeholders is reflected in the Plan',
  'information_provision', 'obligation', mech='summary within the Plan', instr=PLANART)
N('na_plan_elements', ['s_a6p1', 's_a6p1h', 's_a6p1m', 's_a6p1o'], 'p_ms', 'set out in the Plan the listed elements',
  'elements (a) to (q): concrete measures and investments, accompanying measures, financing information, price-effect estimates, identification of vulnerable groups, definitions applied, income support criteria, milestones, targets and timetable (to 31 July 2032), costs, national contribution, do-no-significant-harm explanation, monitoring arrangements incl. Annex IV indicators, consultation summary, anti-fraud system explanation, geographic and gender considerations',
  'information_provision', 'obligation', mech='Plan content requirement', instr=PLANART, deriv='derived', rule=R_PLAN,
  ind=['A4.P1'])
N('na_a6p2', 's_a6p2', 'p_ms', 'include technical assistance actions in the Plan',
  'technical assistance actions necessary for effective administration and implementation of the measures and investments',
  'implementation', 'permission', mech='Plan content option', instr=PLANART, nt='N3', deriv='derived', rule=R_PLAN,
  ind=['A4.P1'])
N('na_consist_plans', 's_a6p3', 'p_ms', 'ensure that the Plan is consistent with information and commitments under six listed plans and programmes',
  'consistency of the Plan with: European Pillar of Social Rights Action Plan; cohesion policy programmes (Regulation (EU) 2021/1060); recovery and resilience plan (Regulation (EU) 2021/241); building renovation plan; updated integrated national energy and climate plan (Regulation (EU) 2018/1999); territorial just transition plans (Regulation (EU) 2021/1056)',
  'cooperation_coordination*', 'obligation', mech='consistency requirement between plans', instr=PLANART,
  unc=['u_residual_tag', 'u_epbd'])
N('na_exchange_gp', 's_a6p4a', 'p_com', 'organise an exchange of good practices during the preparation of the Plans',
  'exchange of good practices, including on cost-effective measures and investments to be included in the Plans',
  'cooperation_coordination*', 'obligation', mech='organisation of an exchange', unc=['u_residual_tag', 'u_a6p4a_participants'])
N('na_request_tech', 's_a6p4b', 'p_ms', 'request technical support under the ELENA facility or the Technical Support Instrument',
  'technical support', 'implementation', 'permission', mech='request for technical support', nt='N3',
  unc=['u_a6p4b_provider'])
N('na_template', ['s_a6p7', 's_anx5_1', 's_anx5_2', 's_anx5_3', 's_anx5_4'], 'p_ms', 'use the template set out in Annex V for the Plan',
  'Plan template (Annex V): sections 1 to 4 prescribing the information items of the Plan', 'information_provision',
  'obligation', mech='mandatory template', instr='INS-TYPE: Plan template (Annex V; documentary artifact)',
  deriv='derived',
  rule='A6.P7 imposes the duty to use the Annex V template; Annex V (internal cross-reference resolved within W, GAP-03) supplies the information items of the template.',
  unc=['u_anx5'])

# ---- Chapter III
N('na_milestones_content', 's_a7p2b', 'p_ms', 'ensure that the milestones and targets of its Plan are compatible with the Union climate targets and Regulation (EU) 2021/1119 and cover listed areas',
  'milestones and targets covering in particular energy efficiency, building renovation, zero- and low-emission mobility and transport, greenhouse gas emission reductions, and reductions in the number of vulnerable households, micro-enterprises and transport users',
  'implementation', 'obligation', mech='content and compatibility requirement for milestones and targets', instr=PLANART,
  deriv='derived',
  rule="'Those milestones and targets' are the milestones and targets of the Plan required by A6.P1(h); the duty is attributed to the Member State that submits the Plan (A4.P1).",
  ind=['A6.P1.pth', 'A4.P1'], unc=['u_normtype_a7p2'])
N('na_dnsh', 's_a7p3', 'p_fund', "support only measures and investments complying with the 'do no significant harm' principle",
  "support for measures and investments that do not comply with the 'do no significant harm' principle (Article 17 of Regulation (EU) 2020/852)",
  'implementation', 'prohibition', mech='eligibility limit on Fund support',
  cond="applies to the Fund's support; the textual subject is the Fund (a device)", unc=['u_fund_origin'])
N('na_a8p1', 's_a8p1', 'p_ms', 'include in the estimated total costs of the Plan listed categories of measures and investments with lasting impacts',
  'measures and investments (a)-(g): building renovations; affordable energy-efficient housing; decarbonisation of heating, cooling and cooking; information and advice; support to public and private entities; zero- and low-emission vehicles and bicycles; public transport and shared mobility',
  'implementation', 'permission', mech='eligibility of costs', instr=PLANART,
  cond='the measures and investments principally target vulnerable households, vulnerable micro-enterprises or vulnerable transport users', nt='N3')
N('na_a8p1f', 's_a8p1f', 'p_ms', 'aim to ensure that support to zero-emission vehicles is prioritised in the Plans',
  'prioritisation of support to zero-emission vehicles', 'implementation', 'obligation_promotional', mech='prioritisation in Plans',
  instr=PLANART, cond='zero-emission vehicles are an affordable and deployable solution', nt='AMBIGUOUS', unc=['u_normtype_a8p1f'], hq=['hq_normtype'])
N('na_a8p2', ['s_a8p2a', 's_a8p2c'], 'p_ms', 'include in the estimated total costs of the Plans the costs of measures providing temporary direct income support',
  'direct income support to vulnerable households and vulnerable transport users to reduce the impact of the increase in road transport and heating fuel prices',
  'implementation', 'permission', mech='eligibility of costs (temporary, decreasing support)', instr=PLANART,
  cond='the Plans contain measures or investments aimed at the same vulnerable households and transport users in accordance with Article 8(1); the support is temporary, decreases over time and is limited to the direct impact of the inclusion of buildings and road transport in Directive 2003/87/EC',
  nt='COMPOUND', unc=['u_normtype_a8p2'], hq=['hq_normtype'])
N('na_a8p2cap', 's_a8p2b', 'p_ms', 'not exceed 37,5 % of the estimated total costs of the Plan with costs of temporary direct income support',
  'costs of temporary direct income support above 37,5 % of the estimated total costs of the Plan (Article 6(1), point (j))',
  'implementation', 'prohibition', mech='cost cap', instr=PLANART)
N('na_a8p3', 's_a8p3a', 'p_ms', 'include in the estimated total costs of the Plans the costs of technical assistance',
  'technical assistance covering training, programming, monitoring, control, audit and evaluation activities, studies, IT expenses, public consultation, information and communication actions',
  'implementation', 'permission', mech='eligibility of costs', instr=PLANART, nt='N3')
N('na_a8p3cap', 's_a8p3b', 'p_ms', 'keep the costs of technical assistance up to 2,5 % of the estimated total costs of the Plan',
  'costs of technical assistance above 2,5 % of the estimated total costs of the Plan (Article 6(1), point (j))',
  'implementation', 'prohibition', mech='cost cap', instr=PLANART, unc=['u_cap_wording'])
N('na_a9p1', 's_a9p1', 'p_ms', 'include in the Plans support provided through public or private entities other than the vulnerable groups',
  'support delivered through public or private entities',
  'implementation', 'permission', mech='delivery through intermediaries', instr=PLANART,
  cond='those entities carry out measures and investments ultimately benefitting vulnerable households, vulnerable micro-enterprises or vulnerable transport users', nt='N3')
N('na_a10p3', 's_a10p3', 'p_com', 'use the amounts made available for the Fund to cover preparatory, monitoring, control, audit, evaluation and administrative expenses incurred by the Commission',
  'expenses incurred by the Commission for the management of the Fund (studies, expert meetings, consultation, information and communication, IT, technical and administrative assistance)',
  UNRES, 'permission', mech='use of Fund appropriations for administrative expenditure', nt='N3',
  unc=['u_function_unres'], ind=['A10.P1'])
N('na_a11p3b', 's_a11p3b', 'p_ms', 'state in the Plans the intention to entrust the managing authorities of cohesion policy programmes',
  'statement of intention in the Plan', 'information_provision', 'obligation', mech='statement within the Plan', instr=PLANART)
N('na_a11p4', 's_a11p4a', 'p_ms', 'include in the Plans, as part of the estimated total costs, payments for additional technical support and the cash contribution to the Member State compartment',
  'payments under Article 7 of Regulation (EU) 2021/240 and cash contribution under Regulation (EU) 2021/523', 'implementation',
  'permission', mech='eligibility of costs', instr=PLANART, nt='N3')
N('na_a11p4cap', 's_a11p4b', 'p_ms', 'not exceed 4 % of the maximum financial allocation for the Plan with costs of additional technical support and cash contribution',
  'costs above 4 % of the maximum financial allocation for the Plan', 'implementation', 'prohibition', mech='cost cap', instr=PLANART)
N('na_a12', 's_a12', 'p_com', 'implement the Fund under direct management',
  'implementation of the Fund in accordance with rules adopted pursuant to Article 322 TFEU, in particular Regulations (EU, Euratom) 2018/1046 and 2020/2092',
  'implementation', 'obligation', mech='direct management', instr='p_fund', unc=['u_fr_dependence'])
N('na_a14p2', 's_a14p2', 'p_ms', 'submit a request up to its maximum financial allocation to implement its Plan',
  'request for financial support up to the maximum financial allocation', 'implementation', 'permission',
  mech='request', nt='N3', unc=['u_a14p2'], hq=['hq_direction'], ind=['A14.P1'])
N('na_a15', 's_a15', 'p_ms', 'contribute at least 25 % of the estimated total costs of its Plans',
  'national contribution of at least 25 % of the estimated total costs of the Plans', 'implementation', 'obligation',
  mech='national co-financing', instr=PLANART, ind=['A6.P1.ptk'])
N('na_revise', 's_a16p1d2', 'p_ms', 'revise the Plan if needed, including after its submission',
  'revision of the Plan', 'implementation', 'permission', mech='revision', instr=PLANART, nt='N3',
  unc=['u_a16p1d2_recipient'])
N('na_a18p1b', 's_a18p1b', 'p_ms', 'request technical support, in accordance with Article 11(4), for the preparation of the amended Plan',
  'technical support', 'implementation', 'permission', mech='request for technical support', nt='N3', ind=['A11.P4'],
  deriv='derived',
  rule="A18.P1 refers explicitly to Article 11(4) (internal cross-reference, GAP-03), which allows Member States to include technical support payments in Plans; the provider is not identified.")
N('na_a18p5a', 's_a18p5a', 'p_ms', 'assess the appropriateness of its Plan in view of the actual direct effects of the ETS inclusion of buildings and road transport by 15 March 2029',
  'assessment of the appropriateness of the Plan', 'monitoring', 'obligation', mech='self-assessment', instr=PLANART)

# ---- Financial-interest protection (Article 21)
N('na_a21p1a', 's_a21p1a', 'p_ms', 'take all appropriate measures to protect the financial interests of the Union and ensure lawful use of the financial allocations',
  'protection of the financial interests of the Union; compliance of use of financial allocations with applicable Union and national law, in particular prevention, detection and correction of fraud, corruption and conflicts of interests',
  'verification_assurance', 'obligation', mech='measures to protect financial interests',
  cond="when implementing the Plans, as beneficiaries of funds under the Fund; includes measures carried out by public or private entities in accordance with Article 9", unc=['u_generic_national_law'])
N('na_ics', ['s_a21p1b1', 's_anx3_1'], 'p_ms', 'provide an effective and efficient internal control system',
  'internal control system as set out in Annex III, in accordance with the Member State institutional, legal and financial framework, including separation of functions and reporting, supervising and monitoring arrangements',
  'verification_assurance', 'obligation', mech='internal control system per Annex III',
  instr='INS-TYPE: internal control system (BORDERLINE_INS-TYPE; see HQ-DEV)', nt='N2', deriv='derived',
  rule='A21.P1 requires an internal control system "as further set out in Annex III"; Annex III (internal cross-reference resolved within W, GAP-03) states the key requirements.',
  unc=['u_ics_dev'], hq=['hq_dev_ics'])
N('na_recover', 's_a21p1b2', 'p_ms', 'provide for the recovery of amounts wrongly paid or incorrectly used',
  'recovery of amounts wrongly paid or incorrectly used', 'remediation', 'obligation', mech='recovery')
N('na_rely', 's_a21p1c', 'p_ms', 'rely on regular national budget management systems',
  'national budget management systems', 'implementation', 'permission', mech='reliance on existing systems', nt='N3')
N('na_data_ms', 's_a21p3a', 'p_ms', 'process personal data for discharge, audit and control proceedings and information, communication and visibility activities',
  'personal data referred to in Article 21(2)(d)', UNRES, 'permission', mech='purpose-limited processing',
  cond='for the purpose and corresponding duration of discharge, audit and control proceedings and of information, communication and visibility activities; in accordance with Regulation (EU) 2016/679 or Regulation (EU) 2018/1725 whichever applies',
  nt='N3', ind=['A21.P2.ptd'], unc=['u_function_unres'])
N('na_data_com', 's_a21p3a', 'p_com', 'process personal data for discharge, audit and control proceedings and information, communication and visibility activities',
  'personal data referred to in Article 21(2)(d)', UNRES, 'permission', mech='purpose-limited processing',
  cond='for the purpose and corresponding duration of discharge, audit and control proceedings and of information, communication and visibility activities; in accordance with Regulation (EU) 2016/679 or Regulation (EU) 2018/1725 whichever applies',
  nt='N3', ind=['A21.P2.ptd'], unc=['u_function_unres'])
N('na_report_discharge', 's_a21p3b', 'p_fund', 'be subject to reporting under the integrated financial and accountability reporting of Article 247 of Regulation (EU, Euratom) 2018/1046, separately in the annual management and performance report',
  'reporting of the Fund within the discharge procedure to the Commission (Article 319 TFEU)', 'information_provision',
  'obligation', mech='integrated financial and accountability reporting',
  cond='within the framework of the discharge procedure to the Commission under Article 319 TFEU', unc=['u_discharge'],
  hq=['hq_extdep_discharge'])

# ---- Chapter IV
N('na_coord_com', 's_a22', 'p_com', 'foster synergies and ensure effective coordination between the Fund and Union programmes and instruments referred to in Article 6(3) and the Modernisation Fund',
  'complementarity, synergy, coherence and consistency among instruments; optimised coordination mechanisms; close cooperation between those responsible for implementation and control',
  'cooperation_coordination*', 'obligation', mech='coordination',
  cond="in a manner commensurate to the Commission's responsibilities; jointly with the Member States concerned", unc=['u_residual_tag', 'u_xref_a22'])
N('na_coord_ms', 's_a22', 'p_ms', 'foster synergies and ensure effective coordination between the Fund and Union programmes and instruments referred to in Article 6(3) and the Modernisation Fund',
  'complementarity, synergy, coherence and consistency among instruments; optimised coordination mechanisms; close cooperation between those responsible for implementation and control',
  'cooperation_coordination*', 'obligation', mech='coordination',
  cond="in a manner commensurate to the Member States' responsibilities; jointly with the Commission", unc=['u_residual_tag', 'u_xref_a22'])
N('na_publish', ['s_a23p1a', 's_a23p1b'], 'p_ms', 'make the data referred to in Article 21(2)(d)(i), (ii) and (iv) publicly available and keep them up to date on a single website',
  'data on final recipients, contractors and subcontractors, and the list of measures and investments, in open machine-readable formats',
  'information_provision', 'obligation', mech='publication on a single website in open machine-readable formats (Article 5(1) of Directive (EU) 2019/1024)',
  instr='INS-TYPE: single website (below device threshold)',
  cond='the information in Article 21(2)(d)(i) and (ii) is not published in the cases of Article 38(3) of Regulation (EU, Euratom) 2018/1046 or in the case of temporary direct income support to vulnerable households',
  ind=['A21.P2.ptd.pti', 'A21.P2.ptd.ptii', 'A21.P2.ptd.ptiv'], unc=['u_diffuse_public'])
N('na_recip_entitled', 's_a23p2a', 'p_recip', 'be informed of the origin of the funds, including where benefiting through intermediaries',
  'information on the origin of the funds including the Union emblem and the funding statement', 'information_provision',
  'entitlement', mech='information on the Union origin of funds', unc=['u_a23p2_obligor'], hq=['hq_direction'])
N('na_recip_visibility', 's_a23p2b', 'p_recip', 'ensure the visibility of the Union funding',
  'visibility of Union funding when promoting actions and results, by coherent, effective and proportionate targeted information to multiple audiences including the media and the public',
  'information_provision', 'obligation', mech='visibility measures',
  cond='except for support to natural persons or where there is risk of commercially sensitive information being made public', unc=['u_diffuse_public'])
N('na_commcom', 's_a23p3a', 'p_com', 'implement information and communication actions relating to the Fund',
  'information and communication actions on the Fund, on actions taken under the Regulation and on the results obtained',
  'information_provision', 'obligation', mech='information and communication actions')

# ---- Monitoring and evaluation
N('na_monitor', 's_a24p2', 'p_com', 'monitor the implementation of the Fund and measure the achievement of its objectives',
  'implementation of the Fund and achievement of its objectives; monitoring targeted and proportionate to the activities carried out under the Fund',
  'monitoring', 'obligation', mech='monitoring')
N('na_perfsys', 's_a24p3a', 'p_perfsys', 'ensure that data for monitoring the implementation of the activities and results are collected efficiently, effectively and in a timely manner',
  'collection of monitoring data', 'monitoring', 'obligation', mech='performance reporting', instr='p_perfsys',
  unc=['u_perfsys_dev'], hq=['hq_dev_perfsys'])
N('na_recip_report', 's_a24p3b', 'p_recip', 'be subject to proportionate reporting requirements',
  'proportionate reporting requirements imposed on recipients of support from the Fund', 'monitoring', 'obligation',
  mech='reporting requirements', unc=['u_a24p3b_obligor'], hq=['hq_direction'])
N('na_indicators', 's_a24p4', 'p_com', 'use the common indicators set out in Annex IV for reporting on progress and for monitoring and evaluation of the Fund',
  'common indicators of Annex IV, towards the achievement of the objectives of Article 3', 'monitoring', 'obligation',
  mech='common indicators', deriv='derived',
  rule='A24.P4 refers explicitly to Annex IV (internal cross-reference, GAP-03) and to Article 3; Annex IV lists the indicators.',
  ind=['A3.P1', 'A3.P2'] + [f'ANX4.pt{i}' for i in range(2, 58)])
N('na_propose1', 's_a27p1b', 'p_com', 'submit, where appropriate, proposals for amendments to this Regulation',
  'proposals for amendments to the Regulation', UNRES, 'obligation', mech='proposal', cond='where appropriate',
  unc=['u_function_unres'], ind=['A27.P1'], units=None)
N('na_propose2', 's_a27p4', 'p_com', 'present, as appropriate, the necessary proposals to ensure the effectiveness and continuity of implementation of the Fund within the post-2027 financial framework',
  'proposals ensuring effectiveness and continuity of implementation of the Fund', UNRES, 'obligation', mech='proposal',
  cond='revenue from auctioning referred to in Article 30d(5) of Directive 2003/87/EC is established as an own resource in accordance with Article 311(3) TFEU',
  nt='N4', legal='conditional_on_further_act', unc=['u_function_unres', 'u_revenue'], hq=['hq_extdep_revenue', 'hq_normtype'])

# ---- Article 28 (inserted Article 26a of Regulation (EU) 2021/1060)
N('na_a28i2a', 's_a28i2a', 'p_ms', 'submit programme amendments in accordance with Article 24 of Regulation (EU) 2021/1060 where implementing transferred resources under shared management',
  'programme amendments concerning one or more programmes', 'implementation', 'obligation', mech='programme amendment',
  cond='Member States implement the transferred resources under shared management', unc=['u_a28_counterpart'],
  hq=['hq_direction'], legal='in_force')
N('na_a28i2b', 's_a28i2b', 'p_ms', 'plan the use of the transferred resources for achieving the Union budget climate objectives',
  'planning of the transferred resources in accordance with Article 6(1) of Regulation (EU) 2021/1060', 'implementation',
  'obligation', mech='planning', unc=['u_a28_counterpart'])
N('na_a28i3', 's_a28i3', 'p_ms', 'submit a notification of financial tables instead of a programme amendment for further transfers',
  'notification of financial tables', 'information_provision', 'permission', mech='notification', nt='COMPOUND',
  cond='the Commission has already approved the Member State request for an amendment of a programme relating to a transfer; proposed changes relate exclusively to an increase of the financial resources without any further changes to the programme',
  unc=['u_a28_counterpart', 'u_normtype_a28i3'], hq=['hq_direction', 'hq_normtype'])

# ---- Annexes III and IV
N('na_ics1d', 's_anx3_1d', 'p_ms', 'ensure an appropriate separation between managing and audit functions',
  'separation of managing and audit functions within the internal control system', 'verification_assurance',
  'obligation', mech='separation of functions', instr='INS-TYPE: internal control system (BORDERLINE_INS-TYPE; see HQ-DEV)',
  nt='N2', hq=['hq_dev_ics'])
N('na_ics2', 's_anx3_2', 'p_ms', 'implement proportionate anti-fraud and anti-corruption measures and measures to avoid conflicts of interest',
  'prevention, detection and correction of fraud, corruption and conflict of interests, avoidance of double funding, legal action to recover misappropriated funds, fraud risk assessment and mitigating measures',
  'verification_assurance', 'obligation', mech='anti-fraud measures', instr='INS-TYPE: internal control system (BORDERLINE_INS-TYPE; see HQ-DEV)')
N('na_ics3', 's_anx3_3', 'p_ms', 'maintain appropriate procedures for drawing up the management declaration and summary of audits',
  'procedures for the management declaration, summary of audits, audit trail and reporting and correction through recoveries of cases of fraud, corruption and conflict of interests',
  'verification_assurance', 'obligation', mech='procedures', instr='INS-TYPE: internal control system (BORDERLINE_INS-TYPE; see HQ-DEV)')
N('na_ics4', 's_anx3_4', 'p_ms', 'ensure appropriate management verifications',
  'management verifications including procedures for checking achievement of milestones and targets and compliance with horizontal principles of sound financial management',
  'verification_assurance', 'obligation', mech='management verifications', instr='INS-TYPE: internal control system (BORDERLINE_INS-TYPE; see HQ-DEV)')
N('na_ics4a', 's_anx3_4a', 'p_implauth', 'check, through management verifications, the achievement of milestones and targets of the Fund',
  'achievement of milestones and targets of the Fund (e.g. desk reviews, on-the-spot checks)', 'verification_assurance',
  'obligation', mech='management verifications (desk reviews, on-the-spot checks)', nt='N2',
  unc=['u_unresolved_authorities'])
N('na_ics4b', 's_anx3_4b', 'p_implauth', 'check, through management verifications, the absence of serious irregularities and double funding',
  'absence of serious irregularities (fraud, corruption, conflict of interests) and double funding', 'verification_assurance',
  'obligation', mech='management verifications (desk reviews, on-the-spot checks)', nt='N2',
  unc=['u_unresolved_authorities'])
N('na_ics5', 's_anx3_5', 'p_ms', 'conduct adequate and independent audits of systems and operations in accordance with internationally accepted audit standards',
  'audits of systems and operations', 'verification_assurance', 'obligation', mech='audit',
  instr='INS-TYPE: internal control system (BORDERLINE_INS-TYPE; see HQ-DEV)')
N('na_auditbody', 's_anx3_5a', 'p_auditbody', 'carry out the audits of systems and operations with ensured functional independence',
  'audits of systems and operations', 'verification_assurance', 'obligation', mech='audit', nt='N2',
  cond='functional independence ensured by the Member State (ANX3.pt5.pta)', unc=['u_unresolved_authorities'],
  deriv='derived',
  rule='Annex III pt5 item (a) states the designation of "the body or bodies which will carry out the audits of systems and operations"; the audit task is attributed to the designated body by that wording.',
  ind=['ANX3.pt5'])
N('na_ics6', 's_anx3_6', 'p_ms', 'maintain an effective system ensuring that information and documents necessary for audit trail purposes are held',
  'audit trail system including electronic collection, recording and storage of data on final recipients of measures or investments necessary to achieve milestones and targets',
  'verification_assurance', 'obligation', mech='audit trail system',
  instr='INS-TYPE: audit trail system (below device threshold)')
N('na_anx4_nonapp', 's_anx4a', 'p_ms', "indicate 'non-applicable' for common indicators to which no measure or investment in its Plan contributes",
  'common indicators of Annex IV', 'information_provision', 'permission', mech='indication', nt='N3', instr=PLANART)
