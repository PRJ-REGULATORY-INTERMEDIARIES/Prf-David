# Authored qualified relations (R): both parties identifiable in the provision or by explicit cross-reference; no prohibitions
from reg import *

PLANART = 'INS-TYPE: Social Climate Plan (documentary artifact; not a device)'
VALID = 'Applies from 30 June 2024 (A29.P2); Fund period 2026-2032 (A1.P1); payments until 31 December 2033 (A20.P8)'
GAP = ('Material establishment of the positions/devices on which the relation depends is not assessed (layer X, not collected '
       'from legal text); dependencies are expectations, never gates.')
EXTYQ = {'qr_fund', 'qr_agreement', 'qr_paydec', 'qr_prorata', 'qr_unused', 'qr_selfassess_submit', 'qr_report',
         'qr_auditauth', 'qr_transfer_in', 'qr_transfer_in_use', 'qr_transfer_out', 'qr_entrust'}
FORCE = ('A29.P1', 'A29.P2', 'FIN.BIND')


def Q(key, sts, origin, cp, rtype, action, obj, fn, mod, mech='', instr='', tnote='', gdir='', cond='',
      deriv='direct', rule='', auth='', disc='', acc='NONE', accs='NA', accmiss='', accvia=(), ext=(), unc=(), hq=(),
      ind=(), add=(), tdir='', legal='in_force', epi=None, gap=GAP, units=None):
    ind = list(L(ind))
    if epi is None:
        if deriv == 'direct' and legal == 'in_force' and key not in EXTYQ:
            epi = 'legal_constitution_evidenced'
            for x in FORCE:
                if x not in ind:
                    ind.append(x)
        else:
            epi = 'documented'
    return qr(key, sts, origin, cp, rtype, action, obj, fn, mod, mech=mech, instr=instr, tnote=tnote, gdir=gdir,
              cond=cond, validity=VALID, legal=legal, epi=epi, deriv=deriv, rule=rule, auth=auth, disc=disc, acc=acc,
              accs=accs, accmiss=accmiss, accvia=accvia, gap=gap, ext=ext, unc=unc, hq=hq, ind=ind, add=add,
              tdir=tdir, units=units)


# ======================= Plan cycle (Chapters II-III) =======================
Q('qr_fund', ['s_a1p2', 's_a7p1', 's_a7p2a', 's_a12', 's_a2_fa', 's_anx2'], 'p_com', 'p_ms', 'contractual_exchange',
  'provide financial support (financial allocation) to Member States for the measures and investments in their Plans, payment being conditional upon achievement of milestones and targets',
  'non-repayable financial support under the Fund up to the maximum financial allocation of each Member State (Annexes I and II)',
  'implementation', 'obligation', mech='direct management by the Commission; payments conditional on milestones and targets; allocation ceilings per Annexes I-II',
  instr='p_fund',
  tnote="Textual subject of A1.P2/A7.P1 is the Fund, a device and never an actor; origin attributed to the Commission as implementer under direct management (A12.P0). Nearest relation type (contractual_exchange) flagged: performance-conditioned funding.",
  gdir='Commission -> Member States', tdir='the Fund -> Member States (textual subject of A1.P2 and A7.P1)',
  cond='payment conditional upon the Member State achieving milestones and targets (A7.P2); subject to availability of funding (A20.P1)',
  deriv='derived',
  rule='A1.P2 and A7.P1 name the Fund as provider of support; A12.P0 states that the Fund is implemented by the Commission under direct management; origin is attributed to the Commission as operator of the Fund (device), with the Fund as instrument.',
  auth='Commission determines allocation and disbursement (A17, A20); Member States receive support',
  disc='conditionality stated (A7.P2); allocation ceilings fixed by formula and table (Annexes I-II)', accvia=['qr_acc_perf'],
  ext=['ext_fr_general', 'ext_ets_revenue', 'ext_ets_postpone'], unc=['u_fund_origin', 'u_revenue', 'u_nearest_type'],
  hq=['hq_direction', 'hq_extdep_revenue', 'hq_extdep_fr'], ind=['A2.P0.pt4'])
Q('qr_plansub', ['s_a4p1a', 's_a5p1a'], 'p_ms', 'p_com', 'information_reporting',
  'submit its Plan to the Commission following a public consultation', 'Social Climate Plan', 'information_provision',
  'obligation', mech='submission of the Plan in the Annex V template (A6.P7)', instr=PLANART,
  cond='following a public consultation with local and regional authorities, economic and social partners, civil society organisations, youth organisations and other stakeholders (A5.P1)',
  gdir='Member State -> Commission', auth='Member State initiates the Plan cycle; the Commission is the identified recipient',
  disc='no discretion stated as to whether to submit (shall); content options in A4.P3-P5, A8, A9 and A11', accvia=['qr_acc_perf'],
  ind=['A6.P7'])
Q('qr_consult', ['s_a5p1a', 's_a5p1b'], 'p_ms', 'p_lra', 'representation_participation',
  'conduct a public consultation on the Plan before submitting it', 'public consultation on the Plan', 'representation_participation*',
  'obligation', mech='public consultation in accordance with the requirements of Article 10 of Regulation (EU) 2018/1999 and the national legal framework',
  tnote='Residual function tag (flagged). Relation typed representation_participation as nearest type: participation of stakeholder categories in Plan preparation.',
  add=['p_socpart', 'p_cso', 'p_youth', 'p_stake'], gdir='Member State consults -> stakeholder categories',
  auth='Member State conducts the consultation; stakeholders participate', disc='consultation design left to Article 10 of Regulation (EU) 2018/1999 and national law (outside W)',
  ext=['ext_gov_consult', 'ext_national_law'], unc=['u_residual_tag', 'u_open_category', 'u_generic_national_law'])
Q('qr_consult_assess', ['s_a5p3'], 'p_com', 'p_ms', 'review_adjudication',
  'assess whether the Plan has been developed in consultation with stakeholders in accordance with A5.P1 (for the purposes of Article 16(3))',
  "the Member State's consultation process for the Plan", 'verification_assurance', 'obligation',
  mech='assessment as part of the Article 16(3) assessment', instr=PLANART, deriv='derived',
  rule="The Member State party is resolved from A5.P1 by the explicit cross-reference 'in accordance with paragraph 1 of this Article' (each Member State submits a Plan after consultation); the Commission is the assessor named in A5.P3.",
  ind=['A5.P1', 'A16.P3'], gdir='Commission -> Member State', auth='Commission as assessor', disc='no criteria beyond conformity with A5.P1 stated',
  accvia=['qr_acc_perf'])
Q('qr_gp_support', ['s_a5p4'], 'p_com', 'p_ms', 'information_reporting',
  'support Member States by providing examples of good practices of consultations on the Plans in accordance with Article 6(4)',
  'examples of good practices of consultations', 'information_provision', 'obligation', mech='examples of good practices',
  ind=['A6.P4'], gdir='Commission -> Member States')
Q('qr_guidance', ['s_a6p5'], 'p_com', 'p_ms', 'information_reporting',
  "provide technical guidance on compliance of measures and investments with the 'do no significant harm' principle",
  "technical guidance tailored to the scope of the Fund, for the purposes of A6.P1(l)", 'interpretation_translation',
  'obligation', mech='technical guidance',
  tnote='Guidance (soft normative output) typed information_reporting as nearest type; flagged.', ind=['A6.P1.ptl'],
  gdir='Commission -> Member States', ext=['ext_dnsh'], unc=['u_nearest_type'])
Q('qr_carbonprice', ['s_a6p6'], 'p_com', 'p_ms', 'information_reporting',
  'provide a common value to be considered as an estimate for the carbon price', 'common carbon-price value for the estimate required by A6.P1(d)',
  'information_provision', 'obligation', mech='common value', ind=['A6.P1.ptd'], gdir='Commission -> Member States')
Q('qr_assess', ['s_a16p1a', 's_a16p1b', 's_a16p3', 's_a16_ext1', 's_a16_ext2', 's_a16_ext3'], 'p_com', 'p_ms', 'review_adjudication',
  'assess the Plan and any amendment submitted under Article 18 for compliance with the Regulation, in close cooperation with the Member State concerned, against the criteria of relevance, effectiveness, efficiency and coherence',
  'the Plan (and any amended Plan) of the Member State', 'verification_assurance', 'obligation',
  mech='assessment against criteria set out in Article 16(3)', instr=PLANART, gdir='Commission -> Member State',
  auth='Commission assesses; Member State is assessed', disc='criteria stated but no thresholds, weights or scoring rules stated (e.g. "adequate response", "reasonable, plausible")',
  accvia=['qr_acc_perf'], ext=['ext_gov_plans', 'ext_dnsh', 'ext_ee_directive', 'ext_afi_reg', 'ext_re_directive'], unc=['u_epbd'])
Q('qr_inforeq', ['s_a16p1c'], 'p_com', 'p_ms', 'oversight_supervision',
  'make observations or seek additional information within two months from the date of submission of the Plan',
  'additional information on the Plan', 'monitoring', 'competence', mech='observations / information request',
  cond='within two months from the date of submission of the Plan', gdir='Commission -> Member State',
  disc='discretionary (may)')
Q('qr_infoprov', ['s_a16p1d1'], 'p_ms', 'p_com', 'information_reporting',
  'provide the additional information requested by the Commission', 'additional information on the Plan', 'information_provision',
  'obligation', mech='response to information request', cond='information requested under A16.P1', ind=['A16.P1'],
  gdir='Member State -> Commission')
Q('qr_extend', ['s_a16p1e'], 'p_ms', 'p_com', 'contractual_exchange',
  'agree to extend the deadline for assessment by a reasonable period if necessary', 'extension of the assessment deadline',
  'cooperation_coordination*', 'permission', mech='agreement between the Member State and the Commission',
  cond='if necessary',
  tnote="Symmetric permission ('The Member State and the Commission may agree'); direction by textual order only; no governance direction stated. Residual function tag flagged.",
  unc=['u_residual_tag', 'u_symmetric'], hq=['hq_direction'])
Q('qr_assess_transfer', ['s_a16p2'], 'p_com', 'p_ms', 'review_adjudication',
  'assess whether transfers requested in accordance with Article 11 meet the objectives of the Regulation',
  'transfer requests of Member States under Article 11', 'verification_assurance', 'obligation',
  mech='assessment of transfer requests', deriv='derived',
  rule='The Member State party is resolved from Article 11 (A11.P1 and A11.P2), under which Member States request transfers; explicit cross-reference in A16.P2 (GAP-03).',
  ind=['A11.P1', 'A11.P2'], gdir='Commission -> Member State', accvia=['qr_acc_perf'])
Q('qr_decision', ['s_a17p1', 's_a17p2', 's_a17p3a', 's_a17p4a'], 'p_com', 'p_ms', 'review_adjudication',
  'decide on the Plan of the Member State by means of an implementing act, on the basis of the Article 16 assessment, no later than five months from submission; where positive, set out measures and investments, estimated total costs, milestones and targets, the maximum financial allocation and instalments, the national contribution, monitoring arrangements, indicators and data-access arrangements; where negative, state the reasons',
  'decision on the Plan and on the financial allocation allocated to the Member State', 'authorization_designation*', 'obligation',
  mech='implementing act', instr='INS-TYPE: implementing act (legal act type; adoption procedure not stated in W)',
  tnote='Residual function tag (flagged): decision approving or refusing a Plan and fixing the allocation.',
  deriv='derived',
  rule="The decision is made 'on the basis of the assessment carried out in accordance with Article 16' (explicit cross-reference to the assessment relation) and concerns 'the Plan of a Member State' submitted pursuant to Article 4(1); parties resolved by these cross-references.",
  ind=['A16.P1', 'A4.P1'], gdir='Commission -> Member State', auth='Commission decides; decision determines the allocation (A17.P3)',
  disc='criteria of Article 16(3) govern; "complies satisfactorily" is not further specified', accvia=['qr_acc_perf'],
  unc=['u_residual_tag', 'u_implact'])
Q('qr_require', ['s_a17p3c'], 'p_com', 'p_ms', 'authority_control',
  'require that additional measures to address weaknesses in the internal control systems be included in the Plan and achieved before the first payment',
  'additional measures addressing weaknesses in internal control systems', 'enforcement', 'competence',
  mech='requirement of additional measures', cond='the Plan complies satisfactorily with the Article 16(3) criteria but the assessment identifies weaknesses in the internal control systems',
  gdir='Commission -> Member State', disc='discretionary (may); no criteria for weaknesses stated')
Q('qr_resubmit', ['s_a17p4b'], 'p_ms', 'p_com', 'information_reporting',
  'resubmit the Plan after taking into account the assessment of the Commission', 'revised Plan', 'information_provision', 'obligation',
  mech='resubmission', instr=PLANART, deriv='derived',
  rule='The recipient of the resubmission is the Commission, the assessing authority named in A17.P4 (first sentence) and the recipient of Plans under A4.P1 (explicit cross-reference via Article 4(1) in A17.P1).',
  ind=['A4.P1'], gdir='Member State -> Commission', cond='negative assessment of the Plan')
Q('qr_amend_submit', ['s_a18p1a'], 'p_ms', 'p_com', 'information_reporting',
  'submit an amended Plan to the Commission', 'amended Plan including necessary and duly justified changes', 'information_provision',
  'obligation', mech='submission of amended Plan', instr=PLANART,
  cond='the Plan is no longer achievable, including relevant milestones and targets, or needs to be significantly adjusted because of objective circumstances, in particular the actual direct effects of the ETS inclusion',
  gdir='Member State -> Commission', accvia=['qr_acc_perf'])
Q('qr_amend_assess', ['s_a18p2'], 'p_com', 'p_ms', 'review_adjudication',
  'assess the amended Plan in accordance with Article 16', 'amended Plan', 'verification_assurance', 'obligation',
  mech='assessment under Article 16', instr=PLANART, deriv='derived',
  rule="A18.P2 refers to Article 16 (assessment relation) and to the amended Plan submitted by the Member State under A18.P1 (explicit cross-references).",
  ind=['A16.P1', 'A18.P1'], gdir='Commission -> Member State')
Q('qr_amend_decision', ['s_a18p3'], 'p_com', 'p_ms', 'review_adjudication',
  'adopt, by means of an implementing act and within three months from submission, a decision setting out the reasons for the positive assessment of the amended Plan',
  'decision on the amended Plan', 'authorization_designation*', 'obligation', mech='implementing act',
  instr='INS-TYPE: implementing act (legal act type; adoption procedure not stated in W)',
  tnote='Residual function tag (flagged).', deriv='derived',
  rule="A18.P3 states 'in accordance with Article 17(1)' (decision on the Plan) and derogates from its deadline; Member State resolved via the amended Plan of A18.P1.",
  ind=['A17.P1', 'A18.P1'], gdir='Commission -> Member State', unc=['u_residual_tag', 'u_implact'])
Q('qr_amend_reject', ['s_a18p4a'], 'p_com', 'p_ms', 'review_adjudication',
  'reject the amended Plan within the period referred to in paragraph 3', 'amended Plan', 'authorization_designation*', 'obligation',
  mech='rejection', instr=PLANART, tnote='Residual function tag (flagged).', cond='negative assessment of the amended Plan',
  gdir='Commission -> Member State', unc=['u_residual_tag'])
Q('qr_hear_a18', ['s_a18p4b'], 'p_com', 'p_ms', 'representation_participation',
  'give the Member State the possibility to present its observations within three months from the communication of the assessment of the amended Plan',
  'observations of the Member State', 'representation_participation*', 'obligation', mech='opportunity to present observations',
  tnote='Right of the Member State stated from the Commission side (obligation of the Commission); residual function tag flagged.',
  cond='before rejecting the amended Plan', gdir='Commission -> Member State (right to be heard)', unc=['u_residual_tag'])
Q('qr_selfassess_submit', ['s_a18p5b'], 'p_ms', 'p_com', 'information_reporting',
  'submit the assessments of the appropriateness of the Plan to the Commission together with the integrated national energy and climate progress reports',
  'assessments of the appropriateness of the Plan (due by 15 March 2029)', 'information_provision', 'obligation',
  mech='submission together with reports under Article 17 of Regulation (EU) 2018/1999', gdir='Member State -> Commission',
  ext=['ext_gov_report'], unc=['u_ext_reporting_channel'], hq=['hq_extdep_reporting'], ind=['A18.P5'])
Q('qr_notify_minor', ['s_a18p6'], 'p_ms', 'p_com', 'information_reporting',
  'notify the Commission of minor adjustments of the Plan (increase or decrease of less than 5 % of a target) or correction of clerical errors',
  'minor changes to the Plan', 'information_provision', 'obligation', mech='notification', instr=PLANART,
  gdir='Member State -> Commission', disc='no Commission approval step stated for minor adjustments')

# ======================= Commitment, payment, conditionality =======================
Q('qr_agreement', ['s_a19p1'], 'p_com', 'p_ms', 'contractual_exchange',
  'conclude in due time an agreement constituting an individual legal commitment for the period 2026-2032',
  'agreement with the Member State concerned', 'implementation', 'obligation', mech='agreement',
  instr='INS-TYPE: agreement constituting an individual legal commitment (instrument; not a device)',
  cond='after the Commission has adopted a positive decision as referred to in Article 17; concluded at the earliest one year before the year of the start of the auctions under Chapter IVa of Directive 2003/87/EC, or two years before in the cases where Article 10(1), third subparagraph, applies',
  deriv='derived',
  rule="A19.P1 makes the agreement follow 'a positive decision as referred to in Article 17' (explicit cross-reference); 'the Member State concerned' is the addressee of that decision.",
  ind=['A17.P1', 'A17.P2'], gdir='Commission -> Member State', auth='Commission concludes the commitment; Member State is party',
  disc='timing bounds stated; "in due time" not specified further', accvia=['qr_acc_perf'],
  ext=['ext_fr_general', 'ext_ets_revenue', 'ext_ets_postpone'], unc=['u_fr_dependence'], hq=['hq_extdep_fr'])
Q('qr_payreq', ['s_a20p1b'], 'p_ms', 'p_com', 'information_reporting',
  'submit a duly reasoned payment request to the Commission once or twice a year, by 31 July or by 31 December',
  'payment request following achievement of milestones and targets', 'information_provision', 'obligation',
  mech='duly reasoned payment request', gdir='Member State -> Commission', accvia=['qr_acc_perf'],
  disc='timing fixed (31 July or 31 December); once or twice a year at the Member State discretion')
Q('qr_payassess', ['s_a20p2'], 'p_com', 'p_ms', 'review_adjudication',
  'assess whether the relevant milestones and targets set out in the Article 17 decision have been satisfactorily achieved (satisfactory achievement presupposes that measures related to previously achieved milestones and targets have not been reversed)',
  'milestones and targets of the Plan', 'verification_assurance', 'obligation', mech='assessment of milestones and targets',
  gdir='Commission -> Member State', ind=['A17.P2'], disc='"satisfactorily achieved" is not defined by a threshold in W', accvia=['qr_acc_perf'])
Q('qr_paydec', ['s_a20p1a', 's_a20p3'], 'p_com', 'p_ms', 'contractual_exchange',
  'adopt an individual decision authorising the disbursement of the financial allocation upon a positive assessment of an individual payment request, in accordance with Regulation (EU, Euratom) 2018/1046, subject to availability of funding and ensuring equal treatment of Member States',
  'disbursement of the financial allocation', 'implementation', 'obligation', mech='individual decision authorising disbursement',
  cond='positive assessment of an individual payment request; availability of funding; decision adopted not earlier than two months and not later than three months after the deadline for submission of payment requests',
  gdir='Commission -> Member State', auth='Commission authorises disbursement', accvia=['qr_acc_perf'],
  ext=['ext_fr_general', 'ext_ets_revenue'], unc=['u_fr_dependence', 'u_revenue'], hq=['hq_extdep_fr', 'hq_extdep_revenue'])
Q('qr_suspend', ['s_a20p4a'], 'p_com', 'p_ms', 'authority_control',
  'suspend the payment of the part of the financial allocation proportional to the unachieved target or milestone', 'part of the financial allocation',
  'enforcement', 'obligation', mech='suspension',
  cond='the Commission establishes, as a result of the assessment of paragraph 3, that milestones and targets have not been satisfactorily achieved; the suspension is lifted only where they have been satisfactorily achieved',
  gdir='Commission -> Member State', accvia=['qr_acc_perf'], ind=['A20.P3'])
Q('qr_obs_a20p4', ['s_a20p4b'], 'p_com', 'p_ms', 'representation_participation',
  'receive the observations that the Member State may present within one month of the communication of the Commission assessment',
  "observations of the Member State on the Commission's assessment", 'representation_participation*', 'entitlement',
  mech='opportunity to present observations',
  tnote="Right stated from the Member State side ('The Member State may present its observations'); the recipient of the observations is not stated in A20.P4; origin recorded as the Commission, the assessor whose communication starts the one-month period. Residual function tag flagged.",
  cond='within one month of the communication of the Commission assessment', gdir='Member State -> Commission (observations)',
  unc=['u_a20p4b', 'u_residual_tag'], hq=['hq_direction'], ind=['A20.P3'])
Q('qr_reduce', ['s_a20p6'], 'p_com', 'p_ms', 'authority_control',
  'reduce the amount of the financial allocation proportionately where the milestones and targets have not been satisfactorily achieved within nine months from the suspension',
  'amount of the financial allocation', 'enforcement', 'obligation', mech='proportionate reduction',
  gdir='Commission -> Member State', accvia=['qr_acc_perf'], ind=['A20.P4'])
Q('qr_hear_a20p6', ['s_a20p6'], 'p_com', 'p_ms', 'representation_participation',
  'give the Member State the possibility to present its observations within two months from the communication of the Commission conclusions',
  'observations of the Member State', 'representation_participation*', 'obligation', mech='opportunity to present observations',
  tnote='Right of the Member State stated from the Commission side; residual function tag flagged.', cond='before reducing the financial allocation',
  gdir='Commission -> Member State (right to be heard)', unc=['u_residual_tag'])
Q('qr_terminate', ['s_a20p7a'], 'p_com', 'p_ms', 'authority_control',
  'terminate the agreements and decommit the amount of the financial allocation where, within 15 months from the conclusion of the agreements, no tangible progress has been made in respect of any relevant milestones and targets',
  'agreements referred to in Article 19 and the amount of the financial allocation', 'enforcement', 'obligation', mech='termination and decommitment',
  gdir='Commission -> Member State', accvia=['qr_acc_perf'], ind=['A19.P1'], ext=['ext_fr_budget'])
Q('qr_hear_a20p7', ['s_a20p7b'], 'p_com', 'p_ms', 'representation_participation',
  'give the Member State the possibility to present its observations within two months of the communication of the assessment that no tangible progress has been made',
  'observations of the Member State', 'representation_participation*', 'obligation', mech='opportunity to present observations',
  tnote='Right of the Member State stated from the Commission side; residual function tag flagged.', cond='before the decision on termination of the agreements',
  gdir='Commission -> Member State (right to be heard)', unc=['u_residual_tag'])
Q('qr_prorata', ['s_a20p9'], 'p_com', 'p_ms', 'contractual_exchange',
  'pay the Member States on a pro-rata basis determined as a share of the payment availabilities to the total approved payments and, in the following round, give priority to Member States with delayed payments',
  'payments of financial allocations', 'implementation', 'obligation', mech='pro-rata payment',
  cond='in a given round of payment requests, the revenue assigned to the Fund in accordance with Article 30d(4) of Directive 2003/87/EC is not sufficient to cover the submitted payment requests',
  gdir='Commission -> Member States', ext=['ext_ets_revenue', 'ext_fr_general'], unc=['u_revenue'], hq=['hq_extdep_revenue'])
Q('qr_unused', ['s_a20p10'], 'p_com', 'p_ms', 'contractual_exchange',
  'allocate to Member States the amounts corresponding to appropriations unused by 31 December 2033 in accordance with the distribution rules of Article 30d(5) of Directive 2003/87/EC',
  'unused appropriations', 'implementation', 'obligation', mech='allocation of unused amounts',
  cond='by way of derogation from Article 12(4), point (c), of Regulation (EU, Euratom) 2018/1046 and without prejudice to Article 30d(4), sixth subparagraph, of Directive 2003/87/EC; to achieve the objectives of Article 3',
  gdir='Commission -> Member States', ext=['ext_ets_distrib', 'ext_fr_budget'], unc=['u_revenue'], hq=['hq_extdep_revenue'])

# ======================= Financial-interest protection and control =======================
Q('qr_recover', ['s_a21p4a'], 'p_com', 'p_ms', 'authority_control',
  'reduce proportionately the support under the Fund and recover any amount due to the Union budget in cases of fraud, corruption and conflict of interests affecting the financial interests of the Union that have not been corrected by the Member State, or a serious breach of an obligation resulting from the agreements',
  'support under the Fund and amounts due to the Union budget', 'enforcement', 'competence',
  mech='right provided for in the Article 19 agreements; proportionality (seriousness of the fraud, corruption or conflict of interests)', deriv='derived',
  rule='A21.P4 requires the Article 19 agreements to provide the right of the Commission; the parties are the Commission and the Member State that concludes the agreement (A19.P1), by explicit cross-reference.',
  ind=['A19.P1'], gdir='Commission -> Member State', accvia=['qr_acc_perf'])
Q('qr_hear_a21', ['s_a21p4b'], 'p_com', 'p_ms', 'representation_participation',
  'give the Member State the opportunity to present its observations before the reduction is made', 'observations of the Member State',
  'representation_participation*', 'obligation', mech='opportunity to present observations',
  tnote='Right of the Member State stated from the Commission side; residual function tag flagged.', cond='before a reduction under A21.P4',
  gdir='Commission -> Member State (right to be heard)', unc=['u_residual_tag'])
Q('qr_acc_perf', ['s_a20p1b', 's_a20p2', 's_a20p4a', 's_a20p6', 's_a20p7a', 's_a21p2c', 's_a21p4a'], 'p_ms', 'p_com', 'accountability',
  'answer to the Commission for the achievement of the milestones and targets and the proper use of the financial allocation',
  'milestones, targets and use of the financial allocation', 'verification_assurance', 'obligation',
  mech='duly reasoned payment request, management declaration, summary of audits; Commission assessment; suspension, reduction, termination, recovery',
  deriv='derived',
  rule='Accountability elements assembled from several provisions (the accountability relation exists as one object; other relations point to it): forum = Commission; duty to justify = duly reasoned payment request (A20.P1) and management declaration and summary of audits accompanying it (A21.P2(c)); assessment/judgment capacity = Commission assessment of milestones and targets (A20.P2); possibility of consequences = suspension (A20.P4), proportional reduction (A20.P6), termination and decommitment (A20.P7), reduction and recovery (A21.P4). No exercise is inferred (RGAM-DR-17).',
  ind=['A20.P1', 'A20.P3'], tdir='Member State -> Commission',
  gdir='Member State (answers) -> Commission (forum)', acc='ACCOUNTABILITY', accs='sufficient',
  auth='Commission as forum with assessment and sanction capacity', unc=['u_acc_perf'])
Q('qr_assure', ['s_a21p2c'], 'p_ms', 'p_com', 'verification_assurance',
  'accompany a payment request by a management declaration and a summary of the audits carried out in accordance with internationally accepted audit standards',
  'management declaration (intended purpose, completeness, accuracy and reliability of information, assurance from internal control systems) and summary of audits with analysis of weaknesses and corrective action',
  'verification_assurance', 'obligation', mech='management declaration and audit summary accompanying the payment request',
  deriv='derived',
  rule='A21.P2(c) obliges the Member State to accompany a payment request; the payment request is submitted to the Commission (A20.P1), resolving the recipient by explicit cross-reference. The obligation is one that the Article 19 agreements shall provide for (A21.P2).',
  ind=['A20.P1', 'A19.P1'], cond='obligation provided for in the agreements referred to in Article 19', gdir='Member State -> Commission',
  accvia=['qr_acc_perf'])
Q('qr_agree_terms', ['s_a21p2', 's_a21p2a', 's_a21p2b', 's_a21p2d', 's_a21p2f', 's_a21p2g'], 'p_ms', 'p_com', 'contractual_exchange',
  'undertake, through the agreements referred to in Article 19, the obligations to check regularly that financing is properly used and measures properly implemented; to prevent, detect and correct fraud, corruption and conflicts of interests and take legal action to recover misappropriated funds; to collect, record and store standardised data in an electronic system and ensure access; and to keep records',
  'control obligations of the Member State (A21.P2 points (a), (b), (d), (f))', 'verification_assurance', 'obligation',
  mech='terms of the agreement; electronic data system; record keeping', instr='INS-TYPE: electronic system (below device threshold)',
  deriv='derived',
  rule='A21.P2 requires the Article 19 agreements to provide for the listed obligations of the Member States; the agreements are concluded between the Commission and the Member State concerned (A19.P1); counterparty resolved by explicit cross-reference.',
  ind=['A19.P1'], gdir='Member State -> Commission',
  ext=['ext_fr_rights', 'ext_dir_procure', 'ext_dir_amld'], accvia=['qr_acc_perf'], unc=['u_fr_dependence'])
Q('qr_auditauth', ['s_a21p2e1'], 'p_ms', 'p_com', 'delegation_authorization',
  'expressly authorise the Commission, OLAF, the Court of Auditors and, for participating Member States, the EPPO to exert their rights as provided for in Article 129(1) of Regulation (EU, Euratom) 2018/1046',
  'rights of audit and control under Article 129(1) of the Financial Regulation', 'authorization_designation*', 'obligation',
  mech='express authorisation provided for in the agreements', add=['p_olaf', 'p_eca', 'p_eppo'], gdir='Member State -> Commission, OLAF, Court of Auditors, EPPO',
  tnote='Residual function tag (flagged); n-ary relation with four recipient bodies; EPPO only for Member States participating in enhanced cooperation.',
  ext=['ext_fr_rights', 'ext_eppo'], unc=['u_residual_tag', 'u_ext_bodies'], hq=['hq_extdep_audit'], ind=['A21.P2'])
Q('qr_oblig_finrec', ['s_a21p2e2'], 'p_ms', 'p_finrec', 'authority_control',
  'impose obligations on all final recipients (and other persons or entities involved in implementation) to expressly authorise the Commission, OLAF, the Court of Auditors and, where applicable, the EPPO to exert their rights, and to impose similar obligations',
  'obligations on final recipients of the financial allocations', 'rule_making_standard_setting', 'obligation',
  mech='imposed obligations; provided for in the agreements', gdir='Member State -> final recipients',
  ext=['ext_fr_rights'], unc=['u_recip_overlap'], ind=['A21.P2'])
Q('qr_access', ['s_anx3_6b'], 'p_ms', 'p_com', 'oversight_supervision',
  'ensure access for the Commission, OLAF, the European Court of Auditors and, for participating Member States, the EPPO to the data on final recipients',
  'data on final recipients of measures or investments', 'verification_assurance', 'obligation',
  mech='access within the audit trail system (Annex III)', add=['p_olaf', 'p_eca', 'p_eppo'], deriv='derived',
  rule='Annex III item 6(b) lists the bodies to which access is to be given; the obligor is the Member State that must maintain the audit trail system (ANX3.pt6; A21.P1 refers to Annex III).',
  ind=['ANX3.pt6', 'A21.P1'], gdir='Member State -> Commission, OLAF, Court of Auditors, EPPO', ext=['ext_eppo'], unc=['u_ext_bodies'])
Q('qr_desig_implauth', ['s_anx3_1a'], 'p_ms', 'p_implauth', 'delegation_authorization',
  'designate the authorities entrusted with the implementation of the Plan and allocate the related responsibilities and functions',
  'designation of implementing authorities', 'authorization_designation*', 'obligation', mech='designation',
  tnote='Obligation to designate type-level positions (N2); no instance is created; residual function tag flagged.',
  gdir='Member State -> implementing authorities', unc=['u_unresolved_authorities', 'u_residual_tag'])
Q('qr_desig_signauth', ['s_anx3_1b'], 'p_ms', 'p_signauth', 'delegation_authorization',
  'designate the authority or authorities responsible for signing the management declaration accompanying the payment requests',
  'designation of the signing authority', 'authorization_designation*', 'obligation', mech='designation',
  tnote='Obligation to designate type-level positions (N2); no instance is created; residual function tag flagged.',
  gdir='Member State -> signing authority', unc=['u_unresolved_authorities', 'u_residual_tag'])
Q('qr_assurance_signauth', ['s_anx3_1c'], 'p_ms', 'p_signauth', 'verification_assurance',
  'ensure procedures through which the signing authority or authorities will get assurance about the achievement of the milestones and targets set in the Plan and that funds were managed in accordance with applicable rules',
  'assurance on achievement of milestones and targets and sound management of funds', 'verification_assurance', 'obligation',
  mech='assurance procedures',
  tnote='The source of the assurance is not stated; the relation is recorded between the Member State (obligor) and the signing authority (recipient of assurance).',
  gdir='Member State -> signing authority (assurance flows to the signing authority)', unc=['u_unresolved_authorities', 'u_assurance_source'], hq=['hq_direction'])
Q('qr_desig_audit', ['s_anx3_5a', 's_anx3_5b'], 'p_ms', 'p_auditbody', 'delegation_authorization',
  'designate the body or bodies which will carry out the audits of systems and operations, ensure their functional independence and allocate sufficient resources',
  'designation, functional independence and resourcing of the audit body', 'authorization_designation*', 'obligation', mech='designation',
  tnote='Obligation to designate type-level positions (N2); no instance is created; residual function tag flagged.',
  gdir='Member State -> audit body', unc=['u_unresolved_authorities', 'u_residual_tag'])

# ======================= Delivery to beneficiaries and transfers =======================
Q('qr_pass_on', ['s_a9p2'], 'p_ms', 'p_vh', 'beneficiary_protective',
  'provide the necessary statutory and contractual safeguards to ensure that the entire benefit is passed on', 'the entire benefit of support provided through public or private entities',
  'implementation', 'obligation', mech='statutory and contractual safeguards', add=['p_vme', 'p_vtu'],
  gdir='Member State (obligor) -> vulnerable households, vulnerable micro-enterprises and vulnerable transport users (beneficiaries)',
  ind=['A9.P1'], ext=['ext_reg20191700', 'ext_reg6512014'], unc=['u_ext_category'])
Q('qr_transfer_in', ['s_a11p1a'], 'p_ms', 'p_com', 'delegation_authorization',
  'request the transfer to the Fund of resources allocated to the Member State under shared management', 'resources under shared management',
  'authorization_designation*', 'permission', mech='request at the Member State initiative',
  tnote='Residual function tag (flagged). The Commission is the party named in the following sentence of A11.P1.',
  cond='subject to the conditions set out in the relevant provisions of Regulation (EU) 2021/1060', gdir='Member State -> Commission',
  ext=['ext_cpr_transfer'], unc=['u_residual_tag', 'u_cpr_dependence'], hq=['hq_extdep_cpr'], ind=['A11.P1'])
Q('qr_transfer_in_use', ['s_a11p1b', 's_a11p1c'], 'p_com', 'p_ms', 'beneficiary_protective',
  'implement the transferred resources directly in accordance with Article 62(1), first subparagraph, point (a), of Regulation (EU, Euratom) 2018/1046 and use them exclusively for the benefit of the Member State concerned',
  'resources transferred from shared management to the Fund', 'implementation', 'obligation',
  mech='direct implementation; exclusive use', gdir='Commission -> Member State concerned', ext=['ext_fr_general', 'ext_cpr_transfer'],
  unc=['u_cpr_dependence', 'u_fr_dependence'], hq=['hq_extdep_cpr'], ind=['A11.P1'])
Q('qr_transfer_out', ['s_a11p2a', 's_a11p2b'], 'p_ms', 'p_com', 'delegation_authorization',
  'request in the Plan the transfer of up to 15 % of the maximum annual financial allocation to funds under shared management, the transfer being made through amendment of one or more programmes in accordance with Article 26a of Regulation (EU) 2021/1060',
  'transfer of part of the annual financial allocation to funds under shared management', 'authorization_designation*', 'permission',
  mech='request in the Plan; amendment of programmes', tnote='Residual function tag (flagged).', deriv='derived',
  rule="The Plans are 'submitted in accordance with Article 4(1)' (explicit cross-reference in A11.P2) i.e. to the Commission; the receiving funds and Article 26a are in Regulation (EU) 2021/1060 (Article 26a is inserted by Article 28 of W).",
  ind=['A4.P1', 'A28.INS26a.P1'], cond='the transfer is limited to 15 % of the maximum annual financial allocation; programmes under the European territorial cooperation goal (Interreg) are excluded',
  gdir='Member State -> Commission', ext=['ext_cpr_transfer', 'ext_cpr_amend'], unc=['u_residual_tag', 'u_cpr_dependence', 'u_xref_26a'],
  hq=['hq_extdep_cpr', 'hq_xref'])
Q('qr_entrust', ['s_a11p3a'], 'p_ms', 'p_manauth', 'delegation_authorization',
  'entrust the managing authorities of the cohesion policy programmes with the implementation of measures and investments benefitting from the Fund',
  'implementation of measures and investments benefitting from the Fund', 'authorization_designation*', 'permission',
  mech='entrustment stated in the Plan', tnote='Residual function tag (flagged).', cond='where applicable, in view of the synergies with cohesion policy programmes and in conformity with the objectives of the Fund',
  gdir='Member State -> managing authorities', ext=['ext_cpr_transfer'], unc=['u_residual_tag', 'u_manauth_ext'], hq=['hq_extdep_cpr'], ind=['A11.P3'])

# ======================= Monitoring, reporting, transparency =======================
Q('qr_jointcomm', ['s_a23p3b'], 'p_com', 'p_natauth', 'information_reporting',
  'carry out joint communication activities with the national authorities and the representation offices of the European Parliament and of the Commission in the Member State concerned',
  'information and communication actions relating to the Fund', 'cooperation_coordination*', 'obligation_promotional',
  mech='joint communication activities', add=['p_repoff'],
  cond='where appropriate and with the agreement of the national authorities',
  tnote='Nearest relation type (information_reporting) and residual function tag flagged; joint activity rather than a one-way report.',
  gdir='Commission with national authorities and representation offices', unc=['u_residual_tag', 'u_nearest_type'], ind=['A23.P3'])
Q('qr_report', ['s_a24p1a', 's_a24p1b', 's_anx4b', 's_anx4c', 's_anx4d', 's_anx4e'], 'p_ms', 'p_com', 'information_reporting',
  'report to the Commission on a biennial basis on the implementation of its Plan together with the integrated national energy and climate progress report, including the Annex IV indicators',
  'implementation of the Plan; Annex IV common indicators (including quantitative information on households in energy poverty and consumption and emission reductions)',
  'monitoring', 'obligation', mech='biennial implementation report with Annex IV common indicators',
  gdir='Member State -> Commission', ext=['ext_gov_report', 'ext_gov_anx4', 'ext_recomm_2020_1563', 'ext_epbd', 'ext_ee_directive', 'ext_afi_reg'],
  unc=['u_ext_reporting_channel', 'u_epbd'], hq=['hq_extdep_reporting', 'hq_extdep_definitions'], ind=['A6.P1.ptm'])
Q('qr_transmit', ['s_a25p1'], 'p_com', 'p_ep', 'information_reporting',
  'transmit the Plans submitted by Member States and the decisions, as made public by the Commission, simultaneously and on equal terms to the European Parliament and the Council without undue delay',
  'Plans submitted by Member States and decisions made public by the Commission', 'information_provision', 'obligation',
  mech='transmission', add=['p_council'], gdir='Commission -> European Parliament and Council', acc='INFO', accs='NA')
Q('qr_epinfo', ['s_a25p3'], 'p_epcom', 'p_com', 'oversight_supervision',
  'invite the Commission to provide information on the state of play of the assessment of the Plans', 'information on the state of play of the assessment of the Plans',
  'monitoring', 'competence', mech='invitation',
  tnote='Invitation only; no duty of the Commission to comply is stated.', gdir='competent committees of the European Parliament -> Commission',
  acc='INFO', accs='NA', accvia=['qr_acc_ep'])
Q('qr_dialogue', ['s_a26p1'], 'p_epcom', 'p_com', 'oversight_supervision',
  'invite the Commission twice a year to discuss the Plans submitted by Member States, the Commission assessment of the Plans, the status of achievement of milestones and targets, and payment, suspension and termination procedures including observations presented and remedial measures taken by Member States',
  'social climate dialogue', 'monitoring', 'competence', mech='twice-yearly invitation to discuss (social climate dialogue)',
  tnote='Invitation only; duty of the Commission to attend or explain is not stated.', gdir='competent committees of the European Parliament -> Commission',
  accvia=['qr_acc_ep'])
Q('qr_takeaccount', ['s_a26p2'], 'p_com', 'p_epcom', 'oversight_supervision',
  'take account of any elements arising from the views expressed through the social climate dialogue, including the resolutions of the European Parliament if provided',
  'views expressed through the social climate dialogue and resolutions of the European Parliament', 'representation_participation*', 'obligation',
  mech='duty to take account', add=['p_ep'],
  tnote='Response capacity (duty to take account); residual function tag flagged; relation typed oversight_supervision as nearest type.',
  gdir='Commission -> competent committees of the European Parliament and the European Parliament', accvia=['qr_acc_ep'], unc=['u_residual_tag', 'u_nearest_type'])
Q('qr_acc_ep', ['s_a26p1', 's_a26p2', 's_a25p3'], 'p_com', 'p_epcom', 'accountability',
  'answer to the competent committees of the European Parliament within the social climate dialogue', 'implementation of the Fund as discussed in the dialogue',
  'monitoring', 'obligation', mech='invitation to discuss; information on state of play; duty to take account',
  deriv='derived',
  rule='Elements assembled from A26.P1 (forum, channel, questioning capacity: invite to discuss, twice a year), A25.P3 (invitation to provide information) and A26.P2 (duty to take account of views). No duty to attend, explain or justify, no assessment/judgment capacity and no sanction are stated; exercise is not inferred (RGAM-DR-17).',
  ind=[], tdir='Commission -> competent committees of the European Parliament', gdir='Commission (actor) -> competent EP committees (forum)',
  acc='ANSWERABILITY', accs='indeterminate',
  accmiss="duty of the Commission to attend, explain or justify not stated ('may invite'); no assessment/judgment capacity of the forum stated; possible consequences limited to the duty to take account (A26.P2)",
  tnote='answerability_only flag: the provision asserts transparency and accountability as purpose (A26.P1) but the elements of accountability are not all evidenced.',
  unc=['u_a26_acc'], hq=['hq_acc_ep'], epi='documented')
Q('qr_eval1', ['s_a27p1a', 's_a27p2'], 'p_com', 'p_ep', 'information_reporting',
  'provide an evaluation report on the implementation and functioning of the Fund two years after the start of the implementation of the Plans, taking into account the first reports submitted by Member States under Article 24, assessing achievement of objectives, efficiency, use of direct income support, application of definitions and continued relevance',
  'evaluation report', 'monitoring', 'obligation', mech='evaluation report', add=['p_council', 'p_eesc', 'p_cor'],
  gdir='Commission -> European Parliament, Council, European Economic and Social Committee, Committee of the Regions',
  ind=['A24.P1'], acc='INFO', accs='NA', ext=['ext_reg2018_842', 'ext_ets_scope'])
Q('qr_eval2', ['s_a27p3'], 'p_com', 'p_ep', 'information_reporting',
  'provide an independent ex post evaluation report by 31 December 2033 consisting of a global assessment of the Fund and information on its impact', 'ex post evaluation report',
  'monitoring', 'obligation', mech='independent ex post evaluation report', add=['p_council', 'p_eesc', 'p_cor'],
  gdir='Commission -> European Parliament, Council, European Economic and Social Committee, Committee of the Regions',
  acc='INFO', accs='NA', unc=['u_independent_eval'])


# accountability class INFO for relations that are pure information provision (never accountability on its own; RGAM-DR-17)
_INFO = {'qr_gp_support', 'qr_guidance', 'qr_carbonprice', 'qr_infoprov', 'qr_selfassess_submit', 'qr_notify_minor', 'qr_jointcomm', 'qr_report'}
for _r in REG['QR']:
    if _r['key'] in _INFO:
        _r['accountability_class'] = 'INFO'
        _r['accountability_sufficiency'] = 'NA'
