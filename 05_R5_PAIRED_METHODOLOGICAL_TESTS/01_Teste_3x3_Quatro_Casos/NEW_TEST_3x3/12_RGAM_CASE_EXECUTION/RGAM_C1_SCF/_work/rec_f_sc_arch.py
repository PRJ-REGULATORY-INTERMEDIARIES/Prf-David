# Authored subconfigurations (S), architecture candidates (A), closure records, properties
from reg import *

# ============================== CLOSURE (coverage + absence claims) ==============================
cl('cl_cov', 'COVERAGE',
   'Coverage of W: every unit of the complete frozen official source file (headers, title, citations, recitals, enacting formula, 5 chapter headings, 29 articles with their paragraphs, points and sub-points, final formula, 37 footnotes, 5 annexes with their items and table rows) is inventoried and screened in source order.',
   'Mechanical parse enumerated units; the executor then read the text of every unit in source order and screened each (UNIT_SCREENING); a mechanical check confirmed that every text node of the source file is contained in some unit (only list markers, and image-only paragraphs of Annex I carried as image placeholders, are not text units). Statements, assignments, positions, relations and external references come from the executor reading. Instruments outside W were not searched.',
   [], 'ASSERTED_WITHIN_DECLARED_CORPUS', ['p_ms', 'p_com'])
cl('cl_extcov', 'COVERAGE',
   'Coverage of sources outside W: no instrument outside W was retrieved, read or searched (GAP-04); every reference made in W to an outside source is recorded as an EXT record (not_checked; outside_corpus_not_expanded).',
   'References were collected by reading every unit; the referenced sources themselves were not opened. Annex I formula images were viewed only in part (three of six image units) and are not transcribed.',
   ['ext_fr_general', 'ext_fr_rights', 'ext_discharge', 'ext_tfeu311', 'ext_ets_revenue', 'ext_ets_postpone', 'ext_ets_distrib', 'ext_cpr_transfer',
    'ext_cpr_amend', 'ext_gov_report', 'ext_eppo', 'ext_reg20191700', 'ext_reg6512014'], 'UNDETERMINED', ['arch_integrated', 'arch_monitor', 'arch_dialogue'])
cl('cl_cent_sc1', 'ABSENCE_CLAIM',
   'Within SC-01, no position other than the Commission holds competence to decide on, approve, reject or require changes to a Plan or an amended Plan.',
   'Reading of all units for decision, approval, rejection, requirement and agreement competences relating to Plans: Commission (A17.P1, A17.P3(c), A18.P3, A18.P4); Member State and Commission by agreement on the assessment deadline (A16.P1). No competence of the Council, the European Parliament, consultative committees or stakeholders to approve or reject a Plan was found. "Not found" is a statement about the search of W, not about the law; the adoption procedure of implementing acts is not stated (see CL for implementing acts).',
   [], 'ASSERTED_WITHIN_DECLARED_CORPUS', ['prop_cent_sc1', 'prop_vert_sc1', 'prop_cent_arch'])
cl('cl_cent_sc3', 'ABSENCE_CLAIM',
   'Within SC-03, no position other than the Commission holds competence to authorise, suspend, reduce, terminate or pro-rate payments of financial allocations.',
   'Reading of all units for payment-related competences: Commission (A20.P3, A20.P4, A20.P6, A20.P7, A20.P9, A20.P10, A21.P4); Member States only request, observe and are assessed. No other position was found within W; the Financial Regulation rules on disbursement are outside W.',
   ['ext_fr_general'], 'ASSERTED_WITHIN_DECLARED_CORPUS', ['prop_cent_sc3', 'prop_cent_arch'])
cl('cl_implact', 'ABSENCE_CLAIM',
   'The procedure for adopting the implementing acts and individual decisions of the Commission (committee involvement, voting) is stated within W.',
   'All units were read for procedural rules on implementing acts (A17.P1, A18.P3, A20.P3); none states a committee or adoption procedure. The procedure, if any, lies outside W and is not cited.',
   [], 'UNDETERMINED', ['prop_plur_sc1', 'arch_integrated'])
cl('cl_private', 'ABSENCE_CLAIM',
   'No private or self-regulatory body holds assessment, decision, standard-setting or enforcement competence within W.',
   'Reading of all units for competences of non-public bodies: private entities appear as intermediaries and recipients (A9.P1, A23.P2) and as parties under Union rules only; none holds a competence of the listed kinds in W.',
   [], 'ASSERTED_WITHIN_DECLARED_CORPUS', ['prop_pubpriv_sc1', 'prop_selfreg_arch'])
cl('cl_review', 'ABSENCE_CLAIM',
   'No review, appeal or independent adjudication body for decisions of the Commission under W is stated within W.',
   'Reading of all units for review or appeal competences: the Member State has the possibility to present observations (A18.P4, A20.P4, A20.P6, A20.P7, A21.P4) but no review body is named. Judicial review under the Treaties is outside W and not cited.',
   [], 'ASSERTED_WITHIN_DECLARED_CORPUS', ['prop_func_arch'])
cl('cl_necessary', 'ABSENCE_CLAIM',
   'Within the Union, the Article 17 decision is a necessary stage for every payment of Fund resources to a Member State and no alternative payment route exists.',
   'Reading of A7, A10-A12, A14, A17, A19-A21 and Annexes I-II: payments are tied to A17/A19/A20 where those provisions apply, but A11.P1 states that resources transferred to the Fund are implemented directly by the Commission without cross-reference to A17-A20, and the Financial Regulation and Directive 2003/87/EC rules on funding and payment are outside W. Neither necessity nor substitutability can be asserted.',
   ['ext_fr_general', 'ext_ets_revenue', 'ext_cpr_transfer'], 'UNDETERMINED', ['prop_necessary', 'prop_subst'])
cl('cl_thresholds', 'ABSENCE_CLAIM',
   'No numeric threshold, weight or scoring rule is stated within W for "complies satisfactorily" (A17.P3), the criteria of A16.P3, "satisfactorily achieved" (A20.P2) or "tangible progress" (A20.P7).',
   'Reading of A16, A17 and A20 and of the Annexes: percentages appear for cost caps (A8.P2, A8.P3, A11.P4), the national contribution (A15) and minor adjustments (A18.P6) but not for the assessment standards listed.',
   [], 'ASSERTED_WITHIN_DECLARED_CORPUS', ['prop_disc_sc1', 'prop_disc_sc3'])
cl('cl_discharge', 'ABSENCE_CLAIM',
   'No accountability capacity of the European Parliament over the Commission implementation of the Fund beyond A25.P3, A26 and A27 is stated within W.',
   'Reading of all units for forum, assessment and consequence elements toward the European Parliament: only invitations (A25.P3, A26.P1), the duty to take account (A26.P2) and reports (A27) were found. The discharge procedure referred to in A21.P3 (Article 319 TFEU) is outside W and its capacities are not stated.',
   ['ext_discharge'], 'UNDETERMINED', ['prop_acc_ep', 'qr_acc_ep', 'arch_dialogue'])
cl('cl_eval_assess', 'ABSENCE_CLAIM',
   'The European Parliament, the Council, the European Economic and Social Committee and the Committee of the Regions, as recipients of Commission reports under A25 and A27, hold no assessment, approval or sanction capacity over those reports within W.',
   'Reading of A24-A27 and the whole instrument for any follow-up capacity of these recipients: none found; the Commission is only required to take account of views expressed in the dialogue (A26.P2).',
   [], 'ASSERTED_WITHIN_DECLARED_CORPUS', ['prop_acc_monitor'])
cl('cl_rulemaking', 'ABSENCE_CLAIM',
   'The rule-making position (the legislator enacting W) is not a party of any qualified relation of W.',
   'All relations were recorded from the text; none has the European Parliament and the Council acting as rule-makers; the European Parliament and Council appear only as recipients of information and as dialogue partner.',
   [], 'ASSERTED_WITHIN_DECLARED_CORPUS', ['prop_depth_rule'])
cl('cl_monitor_link', 'ABSENCE_CLAIM',
   'No explicit legal link is stated within W between the Article 24 monitoring reports and the Article 20 payment assessment (payment depends on milestones and targets of the Plan and the Commission decision, A20.P1-P2).',
   'Reading of A20, A24 and A17: A20.P2 refers to milestones and targets set out in the Commission decision under Article 17; A24 reports are not mentioned in A20; the Plan and the decision must contain monitoring arrangements and the Annex IV indicators (A6.P1(m), A17.P2(d)-(e)), which is an interface between the two sets of provisions.',
   [], 'ASSERTED_WITHIN_DECLARED_CORPUS', ['arch_monitor'])
cl('cl_nos', 'ABSENCE_CLAIM',
   'No subconfiguration is warranted for the information and communication provisions of A23, for the delivery relations of A9 and A11(3), or for the A25 transmission and the A25(3) invitation taken together with A26: each rests on a single relation or on thematic proximity without a stated legal coupling.',
   'Reading of A9, A11(3), A23, A25, A26: a single qualified relation does not make a subconfiguration (RGAM-DR-23); the A25 provisions and A26.P1 concern the same recipients and the same subject (the Plans and their assessment) but no provision couples them.',
   [], 'ASSERTED_WITHIN_DECLARED_CORPUS', ['qr_pass_on', 'qr_entrust', 'qr_jointcomm', 'qr_transmit', 'qr_epinfo'])

# ============================== SUBCONFIGURATIONS ==============================
SC_PLAN_QR = ['qr_plansub', 'qr_consult', 'qr_consult_assess', 'qr_gp_support', 'qr_guidance', 'qr_carbonprice', 'qr_assess',
              'qr_inforeq', 'qr_infoprov', 'qr_extend', 'qr_decision', 'qr_require', 'qr_resubmit', 'qr_amend_submit',
              'qr_amend_assess', 'qr_amend_decision', 'qr_amend_reject', 'qr_hear_a18', 'qr_selfassess_submit', 'qr_notify_minor']
SC_PLAN_NA = ['na_content1', 'na_consist_necp', 'na_a4p3', 'na_a4p4', 'na_a4p5', 'na_consult_summary', 'na_plan_elements', 'na_a6p2',
              'na_consist_plans', 'na_exchange_gp', 'na_request_tech', 'na_template', 'na_milestones_content', 'na_a8p1', 'na_a8p1f',
              'na_a8p2', 'na_a8p2cap', 'na_a8p3', 'na_a8p3cap', 'na_a9p1', 'na_a11p3b', 'na_a11p4', 'na_a11p4cap', 'na_a14p2', 'na_a15',
              'na_revise', 'na_a18p1b', 'na_a18p5a', 'na_anx4_nonapp', 'na_dnsh']
sc('sc_plan', 'Plan submission, assessment, decision and amendment (Commission and Member State)',
   'Sequential procedural dependency: the output of one qualified relation is the legally stated precondition or object of the next (submission, assessment, decision, amendment or resubmission), each link made by explicit cross-reference.',
   "Who prepares, assesses and decides the content and financial envelope of each Member State's Social Climate Plan, and how may a decided Plan be modified?",
   SC_PLAN_QR, SC_PLAN_NA, ['p_com', 'p_ms', 'p_fund', 'p_lra', 'p_socpart', 'p_cso', 'p_youth', 'p_stake'],
   "Explicit cross-references among provisions: A17.P1 decides 'on the basis of the assessment carried out in accordance with Article 16'; A18.P2 and A18.P3 refer to Articles 16 and 17(1); A17.P4 and A18.P1 refer back to submission under Article 4(1); A5.P3 refers to Article 16(3). The Commission is the single named assessor and decision-taker and the Member State the single named submitter within the S.",
   'The relations satisfy the sequential-dependency pattern through legally stated cross-references (decision relations are defined on the basis of the preceding assessment relation), not through chapter membership, shared actors or vocabulary.',
   [], 'Stops at the Commission decision (A17), amendment and resubmission (A17.P4, A18). Commitment and payment lie in SC-03; control relations in SC-04; transfers in SC-07. The content of other plans and instruments referred to in the Plan provisions is outside W.',
   [], '', "Rival grouping: three separate S (preparation and consultation; assessment; amendment), rejected because A17.P1 and A18.P2-P3 explicitly bind the relations; or one S together with SC-03 (a single financing chain), considered at the architecture level (ARCH-01).",
   unc=['u_implact', 'u_residual_tag'])
sc('sc_consult', 'Public consultation on the Plan (Member State, stakeholder categories, Commission)',
   'Participation followed by verification: a participation relation (A5.P1) is followed by Commission verification that the participation took place (A5.P3, by reference to paragraph 1).',
   'Who must be consulted before a Plan is submitted, and who verifies that the consultation took place?',
   ['qr_consult', 'qr_consult_assess'], ['na_consult_summary'], ['p_ms', 'p_com', 'p_lra', 'p_socpart', 'p_cso', 'p_youth', 'p_stake'],
   "A5.P3 refers to 'paragraph 1 of this Article' (consultation) and to Article 16(3); the summary of the consultation is part of the Plan (A5.P2).",
   'Two relations coupled by an explicit cross-reference and a Plan content duty referring to the same consultation; not a grouping by theme alone.',
   [], 'Only the consultation step; the content of consultation requirements (Article 10 of Regulation (EU) 2018/1999) and national law are outside W.',
   [], 'sc_plan', "Rival grouping: treat the consultation only as a condition of the submission relation (QR for A4.P1/A5.P1) rather than as an S.",
   unc=['u_open_category'])
sc('sc_pay', 'Agreement, performance-conditioned payment and enforcement (Commission and Member State)',
   'Conditional sequence with enforcement branches: the Article 17 decision conditions the Article 19 agreement; milestones and targets set in the decision condition payments (A20.P1-P3); failure triggers suspension, reduction or termination (A20.P4-P7).',
   'How are Fund resources committed to a Member State and released, withheld or withdrawn against performance?',
   ['qr_fund', 'qr_agreement', 'qr_payreq', 'qr_payassess', 'qr_paydec', 'qr_suspend', 'qr_obs_a20p4', 'qr_reduce', 'qr_hear_a20p6',
    'qr_terminate', 'qr_hear_a20p7', 'qr_prorata', 'qr_unused', 'qr_acc_perf'],
   ['na_a12', 'na_a10p3'], ['p_fund', 'p_com', 'p_ms'],
   "A19.P1 ('after the Commission has adopted a positive decision as referred to in Article 17'); A20.P1 ('milestones and targets indicated in the Plan, as approved in accordance with Article 17'); A20.P2 ('set out in the Commission decision referred to in Article 17'); A17.P2(b) (allocation 'to be paid in instalments, in accordance with Article 20'); A7.P2 (payment conditional on milestones and targets); A20.P4, P6, P7 refer to the preceding steps.",
   'The relations are coupled by explicit legal conditions (each step defined by reference to the preceding decision or assessment), not by the shared actors Commission and Member State.',
   [], 'Commission-Member State financing relations of A7, A10, A12, A14, A17(2)-(3), A19, A20 and Annexes I-II; the source of the revenue (Directive 2003/87/EC) and the Financial Regulation rules are outside W.',
   ['sc_control'], '', 'Rival grouping: one S with SC-01 (a single financing chain) or a split at the Article 17 decision; considered at the architecture level.',
   unc=['u_revenue', 'u_fr_dependence'])
sc('sc_control', 'Protection of financial interests and internal control (Member State, Commission, Union control bodies)',
   'Layered assurance chain: designation of national implementing, signing and audit positions (Annex III); management declaration and audit summary accompanying payment requests (A21.P2(c)); authorisation and access of Union control bodies (A21.P2(e), Annex III item 6); Commission reduction and recovery (A21.P4).',
   'How are the financial interests of the Union protected in the use of Fund resources, and who may check and sanction?',
   ['qr_assure', 'qr_agree_terms', 'qr_auditauth', 'qr_oblig_finrec', 'qr_access', 'qr_desig_implauth', 'qr_desig_signauth',
    'qr_assurance_signauth', 'qr_desig_audit', 'qr_recover', 'qr_hear_a21', 'qr_acc_perf'],
   ['na_a21p1a', 'na_ics', 'na_recover', 'na_rely', 'na_data_ms', 'na_data_com', 'na_report_discharge', 'na_ics1d', 'na_ics2', 'na_ics3',
    'na_ics4', 'na_ics4a', 'na_ics4b', 'na_ics5', 'na_auditbody', 'na_ics6'],
   ['p_ms', 'p_com', 'p_olaf', 'p_eca', 'p_eppo', 'p_finrec', 'p_implauth', 'p_signauth', 'p_auditbody', 'p_fund'],
   "A21.P1 requires an internal control system 'as further set out in Annex III'; A21.P2 states that 'the agreements referred to in Article 19 shall provide for' the obligations; A21.P2(c) refers to the payment request (A20.P1); A21.P4 refers to the agreements and to the reduction of support; A17.P3(c) links weaknesses in internal control systems to the first payment.",
   'Relations are coupled by explicit cross-references to the Annex III requirements, to the Article 19 agreements and to the payment request, and by a common object (the payment request and the agreements), not by the shared Member State actor alone.',
   [], 'National control arrangements and Union audit and recovery relations stated in A21 and Annex III; the content of the audit and control rights (Financial Regulation Art. 129(1)), the EPPO and the discharge procedure are outside W.',
   ['sc_pay'], '', 'Rival grouping: a national internal-control S (Annex III designations) separate from a Union protection S (A21.P2(e), A21.P4).',
   unc=['u_unresolved_authorities', 'u_ext_bodies'])
sc('sc_monitor', 'Monitoring, reporting and evaluation (Member State, Commission, Union institutions)',
   'Information-return chain: Member State implementation report with Annex IV indicators (A24.P1); Commission monitoring and use of the same indicators (A24.P2, A24.P4); Commission evaluation reports that take Member State reports into account (A27.P1) addressed to four Union bodies.',
   'How is implementation of the Fund monitored and evaluated and to whom is the information returned?',
   ['qr_report', 'qr_eval1', 'qr_eval2'], ['na_monitor', 'na_perfsys', 'na_recip_report', 'na_indicators', 'na_propose1'],
   ['p_ms', 'p_com', 'p_ep', 'p_council', 'p_eesc', 'p_cor', 'p_perfsys', 'p_recip'],
   "A27.P1 evaluates 'taking into account the results of the first reports submitted by Member States in accordance with Article 24'; A24.P1 and A24.P4 both rely on the Annex IV indicators; A6.P1(m) and A17.P2(d)-(e) require the Plan and decision to contain monitoring arrangements and indicators.",
   'Three relations coupled by an explicit cross-reference (A27.P1 to Article 24) and a common indicator set (Annex IV), not by a shared actor alone.',
   [], 'Information flows only; no assessment or sanction capacity of the recipients is stated in W (see closure). Recipients other than the Commission are not given a follow-up competence.',
   ['sc_parl'], '', 'Rival grouping: monitoring as a stage inside SC-03 (milestone verification); rejected as a separate S because A24 reports are not linked to the A20 payment assessment (closure CL monitor link).',
   unc=['u_perfsys_dev', 'u_a24p3b_obligor', 'u_independent_eval'])
sc('sc_parl', 'Social climate dialogue with the European Parliament (Commission and competent committees)',
   'Invitation followed by response: the competent committees invite the Commission to discuss (A26.P1); the Commission takes account of the views expressed through that dialogue (A26.P2).',
   'Through which channel can the European Parliament question the Commission on the Fund, and what must the Commission do with the views expressed?',
   ['qr_dialogue', 'qr_takeaccount', 'qr_acc_ep'], [], ['p_com', 'p_epcom', 'p_ep'],
   "A26.P2 refers to 'the views expressed through the social climate dialogue' (A26.P1).",
   'Two relations coupled by explicit cross-reference plus one derived accountability object; the A25 provisions are not included because no provision couples them to the dialogue (thematic proximity only).',
   [], 'The dialogue relations of A26 only; transmission (A25.P1) and the invitation to provide information (A25.P3) remain ungrouped relations.',
   [], '', 'Rival grouping: include A25.P1 and A25.P3 with A26 as one parliamentary-information S; rejected for want of a stated legal coupling.',
   unc=['u_a26_acc'], hq=['hq_acc_ep'])
sc('sc_transfer', 'Transfers between the Fund and shared-management programmes (Member State, Commission)',
   'Request-assessment-implementation: Member States request transfers (A11.P1, A11.P2); the Commission assesses requested transfers (A16.P2); transferred resources are implemented directly or through programme amendments (A11.P1, A28 Article 26a).',
   'How can resources move into and out of the Fund and who assesses the transfer?',
   ['qr_transfer_in', 'qr_transfer_in_use', 'qr_transfer_out', 'qr_assess_transfer'], ['na_a28i2a', 'na_a28i2b', 'na_a28i3'], ['p_ms', 'p_com'],
   "A16.P2 refers to 'transfers requested in accordance with Article 11'; A11.P2 refers to Plans submitted under Article 4(1) and to Article 26a of Regulation (EU) 2021/1060, inserted by Article 28.",
   'Relations coupled by explicit cross-references between Articles 11, 16(2) and 28; external instrument content is not used.',
   [], 'Relations stated in W only; the rules of the receiving funds and Regulation (EU) 2021/1060 are outside W (stop at the highest level supported by W).',
   [], '', 'Rival grouping: the transfer relations as part of SC-01 (Plan content, since transfers are requested in Plans).',
   unc=['u_cpr_dependence', 'u_xref_26a'], hq=['hq_xref', 'hq_extdep_cpr'])

# ============================== ARCHITECTURE CANDIDATES ==============================
arch('arch_integrated', ['sc_plan', 'sc_consult', 'sc_pay', 'sc_control', 'sc_transfer'],
     "Governing problem: how Union financial support from the Fund is allocated to Member States on the basis of approved Social Climate Plans, released against performance and protected against misuse. Scale: Union level (Commission) and Member State level (with national control bodies). Domain: financing of the social impacts of including buildings and road transport in the emissions trading system. Jurisdiction: European Union. Interval: 2026-2032 with payments until 31 December 2033.",
     ['A1.P1', 'A1.P2', 'A3.P1', 'A3.P2', 'A7.P1', 'A7.P2', 'A10.P1', 'A20.P8'], 'SATISFIED',
     "Qualified procedural dependency among the S by explicit cross-reference: (a) SC-01 to SC-03: A19.P1 (agreement after the positive decision of Article 17), A20.P1 and A20.P2 (milestones and targets as set in the Article 17 decision), A17.P2(b) (instalments in accordance with Article 20); (b) SC-03 to SC-04: A21.P2 (the Article 19 agreements provide for the control obligations), A21.P2(c) (accompaniment of payment requests), A21.P4 (reduction and recovery right in the agreements), A17.P3(c) (additional internal-control measures before the first payment), A21.P1 and Annex III; (c) SC-01 to SC-07: A16.P2 (assessment of transfers requested under Article 11), A11.P2; (d) SC-02 nested in SC-01 via A5.P3.",
     'qualified_procedural_dependency',
     ['qr_decision', 'qr_agreement', 'qr_payreq', 'qr_payassess', 'qr_paydec', 'qr_assure', 'qr_agree_terms', 'qr_recover', 'qr_require',
      'qr_assess_transfer', 'qr_transfer_out', 'qr_consult_assess'], 'SATISFIED',
     "Conditional sequence attributable to the whole: disbursement of Fund resources is legally tied, within W, to a prior Commission decision on the Plan, an agreement and a milestone-based assessment, with national and Union control relations attached to the payment request; the Commission is the single named decision-taker at the decision points (Plan decision; individual payment decision) while Member States, national authorities and Union control bodies hold submission, control and access roles.",
     "Bearer: ARCHITECTURE ARCH-01 (emergent/whole property: conditional sequence of authorisation and control across SC-01, SC-03, SC-04). Inferential rule: the sequence is read from the cross-referenced conditions identified in I2 (not from reachability, from a common actor or from graph connectivity) and is recorded as a configuration of stated conditions, not as a path property or a score.",
     'SATISFIED',
     'CL cov (all units read); CL cent_sc1, cent_sc3, thresholds, review, private, implact and necessary (absence claims); CL extcov (outside sources not searched).',
     ['ext_ets_revenue', 'ext_ets_postpone', 'ext_fr_general', 'ext_cpr_transfer', 'ext_cpr_amend', 'ext_gov_report', 'ext_fr_rights', 'ext_eppo', 'ext_reg20191700', 'ext_reg6512014'],
     "Rival groupings: (i) SC-01 and SC-03 as two separate architectures joined only at the Article 17 decision; (ii) SC-04 as a separate national internal-control architecture; (iii) merger with ARCH-02 and ARCH-03 into one whole-instrument architecture (not warranted: see those candidates).",
     "If rules outside W provided other payment routes or different conditions, the sequence of A19-A20 could be bypassed; the claim is therefore stated within the declared corpus W only. The coupling of SC-07 would weaken if the rules of the receiving funds (Regulation (EU) 2021/1060) separated transferred resources from Article 17 decisions.",
     'SATISFIED', 'INTEGRATED',
     "I1 to I4 each stated and evidenced within W: the governing problem and scale are fixed by A1, A3, A7, A10 and A20.P8; the coupling is a qualified procedural dependency resting on explicit cross-references independent of any expected global property; the configurational consequence is a conditional sequence of decision points; boundaries, rival groupings and unresolved external dependencies are stated. The outcome is scoped to the declared corpus and queued for human review because the I2/I3 thresholds are unvalidated.",
     'AUTO', unc=['u_coupling_threshold', 'u_implact', 'u_revenue', 'u_fr_dependence', 'u_cpr_dependence'], hq=['hq_integration'])
arch('arch_monitor', ['sc_monitor'],
     "Governing problem: monitoring and evaluation of implementation and results of the Fund (Member State reporting, Commission monitoring and evaluation, reports to Union institutions). Scale: Member State and Union levels. Jurisdiction: European Union. Interval: from the start of implementation of the Plans to the ex post evaluation by 31 December 2033.",
     ['A24.P1', 'A24.P2', 'A24.P4', 'A27.P1', 'A27.P3'], 'SATISFIED',
     "Qualified procedural dependency internal to SC-05: A27.P1 evaluates 'taking into account the results of the first reports submitted by Member States in accordance with Article 24'; A24.P4 requires the Commission to use the Annex IV indicators that A24.P1 requires Member States to include. Interface with ARCH-01: A6.P1(m) and A17.P2(d)-(e) require the Plan and the decision to contain monitoring arrangements and the Annex IV indicators.",
     'qualified_procedural_dependency', ['qr_report', 'qr_eval1'], 'SATISFIED',
     "Feedback of implementation information into review of the instrument: the evaluation report is legally conditioned on Member State reports and assesses the continued relevance of objectives, measures and assigned revenues (A27.P2(d)), with a duty to propose amendments where appropriate (A27.P1).",
     "Bearer: ARCHITECTURE ARCH-02 (emergent/whole property: reporting-to-evaluation feedback). Inferential rule: conditional sequence read from the explicit cross-reference A27.P1 to Article 24; no exercise and no transmission is inferred from reachability.",
     'SATISFIED', 'CL cov; CL monitor link; CL eval_assess; CL extcov.', ['ext_gov_report'],
     "Rival grouping: monitoring as a stage inside ARCH-01 (the payment assessment of A20 verifies milestones and targets); not supported by a legal link between A24 reports and A20 (CL monitor link), but the Annex IV interface of the Plan content and decision ties the two sets of provisions.",
     "If A24 reports were legally linked to payment assessment, SC-05 would fall inside ARCH-01; if the Annex IV interface were disregarded, SC-05 would be a distinguishable candidate. The coupling with ARCH-01 rests on a mandatory interface through the Plan content and decision, not on a shared actor alone.",
     'SATISFIED', 'OVERLAPPING_OR_PARTIALLY_INTEGRATED',
     "I1 to I4 are satisfied within SC-05; the candidate overlaps ARCH-01 through the source-supported mandatory interface (Annex IV indicators referred to in A6.P1(m), A17.P2(d)-(e), A24.P1 and A24.P4). The intersection is not treated as a separate architecture. Queued for human review because the I2/I3 thresholds are unvalidated.",
     'AUTO', unc=['u_coupling_threshold', 'u_ext_reporting_channel'], hq=['hq_overlap'])
arch('arch_dialogue', ['sc_parl'],
     "Governing problem: parliamentary information and dialogue with the Commission on the Fund, stated in A26.P1 as enhancing dialogue between Union institutions and ensuring greater transparency and accountability. Scale: Union institutional level. Jurisdiction: European Union.",
     ['A26.P1', 'A26.P2', 'A25.P3'], 'SATISFIED',
     "Coordination or communication internal to SC-06: A26.P2 refers to 'the views expressed through the social climate dialogue' (A26.P1).",
     'coordination_or_communication', ['qr_dialogue', 'qr_takeaccount'], 'SATISFIED',
     "Candidate property: an accountability interface of the Commission toward the competent European Parliament committees. Forum, channel, questioning capacity and a duty to take account are evidenced; the duty to explain, assessment capacity and consequences are not stated; the property can be attributed only as answerability with indeterminate sufficiency.",
     "Bearer: ARCHITECTURE ARCH-03 (accountability structure). Inferential rule: DR-17 elements assembled in qr_acc_ep; no element is inferred from exercise or from the stated purpose.",
     'INDETERMINATE', 'CL cov; CL discharge; CL eval_assess; CL extcov.', ['ext_discharge'],
     "Rival grouping: the dialogue together with A25.P1 and A25.P3 as one parliamentary-information architecture, or together with the discharge procedure of Article 319 TFEU (outside W).",
     "If the discharge procedure outside W were included, accountability toward the Parliament could be fuller; within W the claim cannot be completed.",
     'INDETERMINATE', 'INDETERMINATE',
     "I3 is indeterminate (accountability elements missing) and the constitutive external dependency on the discharge procedure touches the claim; no architecture is asserted for this candidate (stopping rule). The question is queued as HQ-ACCOUNT.",
     'AUTO', unc=['u_a26_acc', 'u_discharge'], hq=['hq_acc_ep'])

# ============================== PROPERTIES ==============================
FAM = {'centralization': 'F1', 'directness and intermediation': 'F1', 'public-private allocation': 'F2',
       'self-regulatory autonomy': 'F2', 'vertical distribution': 'F3', 'decision-centre plurality': 'F3',
       'relational depth': 'F4', 'functional allocation': 'F4', 'discretion distribution': 'F5', 'accountability structure': 'F5'}
AGG_S = 'Value stated for this subconfiguration before any summary; no scalar score or composite; summary at the architecture level lists per-S values.'


def P(key, name, btype, bearer, scale, value, rule, support, closure=None, count='', rival='', status='asserted',
      pathsem='', agg=AGG_S, hq=()):
    fam = FAM.get(name, '')
    hq = list(L(hq))
    if fam:
        hq.append('hq_gap_family')
    return prop(key, name, fam, btype, bearer, scale, value, rule, pathsem, agg, support, 'Y' if closure else 'N', closure or '', count,
                'Y', rival, status, hq=hq)


P('prop_cent_sc1', 'centralization', 'SUBCONFIGURATION', 'sc_plan', 'SC-01',
  'Competence to assess and decide on Plans (A16, A17) and on amended Plans (A18.P2-P4) is attributed to the Commission alone among the positions named in the S; Member States hold initiating, information and revision roles; no other decision-taker is named within W.',
  'Origin of the assessment, decision, rejection and requirement relations is the Commission; absence of any other named decision-taker within W (closure statement).',
  ['qr_assess', 'qr_decision', 'qr_amend_decision', 'qr_amend_reject', 'qr_require'], closure='cl_cent_sc1',
  rival='Consultation relations give stakeholders participation but no decision role; the Parliament and the Council receive information only (A25.P1).')
P('prop_cent_sc3', 'centralization', 'SUBCONFIGURATION', 'sc_pay', 'SC-03',
  'Authorisation of disbursement, suspension, reduction, termination and pro-rata payment are attributed to the Commission alone within the S; Member States request, present observations and are assessed.',
  'Origin of the payment, suspension, reduction, termination and pro-rata relations is the Commission; absence of any other named payer or sanctioning position within W.',
  ['qr_paydec', 'qr_suspend', 'qr_reduce', 'qr_terminate', 'qr_prorata'], closure='cl_cent_sc3',
  rival='National implementing authorities verify milestones (Annex III) but hold no payment competence in W.')
P('prop_cent_arch', 'centralization', 'ARCHITECTURE', 'arch_integrated', 'ARCH-01 (SC-01, SC-03; SC-04 for contrast)',
  'Differentiated: decision competence over Plans and payments is concentrated at the Commission (SC-01, SC-03), while control and access rights are distributed among national and Union bodies (SC-04). No composite value is stated; an instrument concentrated in one function and distributed in another is not described as centralized as a whole.',
  'Per-S values listed (PROP for SC-01, SC-03 and the plurality property for SC-04); no aggregation beyond listing.',
  ['prop_cent_sc1', 'prop_cent_sc3', 'prop_plur_sc4'], closure='cl_cent_sc1',
  agg='Per-S values reported first; ecological and atomistic fallacies avoided: the SC-01 and SC-03 values are not pushed to SC-04 and vice versa.',
  rival='Reading the whole instrument as centralized or as distributed is rejected because the per-S values differ.')
P('prop_plur_sc1', 'decision-centre plurality', 'SUBCONFIGURATION', 'sc_plan', 'SC-01',
  'One decision centre is named for Plan decisions (the Commission, by implementing act); whether other bodies take part in adopting the implementing act is not stated within W.',
  'The adoption procedure of implementing acts is not stated in W; absence-dependent claim made undetermined.',
  ['qr_decision'], closure='cl_implact', status='undetermined', count='one named decision-taker (evidenced instance); procedure undetermined')
P('prop_plur_sc4', 'decision-centre plurality', 'SUBCONFIGURATION', 'sc_control', 'SC-04',
  'Access and authorisation rights for audit and control are granted in parallel to the Commission, OLAF and the Court of Auditors and, for participating Member States, the EPPO; each Member State designates its own implementing, signing and audit authorities; the decision to reduce or recover rests with the Commission.',
  'Named recipients of the authorisation and access relations (A21.P2(e), Annex III item 6) and the origin of the reduction and recovery relation (A21.P4).',
  ['qr_auditauth', 'qr_access', 'qr_recover', 'qr_desig_implauth', 'qr_desig_signauth', 'qr_desig_audit'],
  count='three Union bodies named unconditionally plus the EPPO for participating Member States (evidenced instances); number of national authorities undetermined (one_or_more per Member State)',
  rival='The EPPO participation and the content of the rights are determined outside W (EXT constitutive).')
P('prop_vert_sc1', 'vertical distribution', 'SUBCONFIGURATION', 'sc_plan', 'SC-01',
  'Functions are distributed across Union level (Commission assessment and decision), national level (Plan design, submission, amendment, self-assessment) and sub-national levels (local and regional measures in the Plan, A4.P4; consultation of local and regional authorities, A5.P1); sub-national actors hold consultative and measure-implementing roles, and no decision competence is stated for them within W.',
  'Positions and levels named in the relations and assignments of the S; absence of sub-national decision competence within W (closure statement).',
  ['qr_plansub', 'qr_consult', 'qr_decision', 'na_a4p4'], closure='cl_cent_sc1')
P('prop_vert_sc4', 'vertical distribution', 'SUBCONFIGURATION', 'sc_control', 'SC-04',
  'Control functions are distributed between the national level (internal control system, implementing, signing and audit authorities, Annex III) and the Union level (Commission, OLAF, Court of Auditors and EPPO access and authorisation; Commission reduction and recovery).',
  'Positions named in the designation, authorisation, access and recovery relations.',
  ['qr_desig_implauth', 'qr_desig_signauth', 'qr_desig_audit', 'qr_auditauth', 'qr_access', 'qr_recover'])
P('prop_inter_arch', 'directness and intermediation', 'ARCHITECTURE', 'arch_integrated', 'ARCH-01 (SC-03, SC-04, SC-07)',
  'The Commission-Member State leg of financing is a direct relation (agreement, payment decision); the Member State is the identified intermediary between the Commission and final recipients and vulnerable groups (pass-on safeguards and obligations on final recipients); further intermediation by public or private entities is permitted, not required (A9.P1); transfers to shared-management funds follow the rules of the receiving funds (outside W).',
  'Reading of the origin and counterpart of qr_fund, qr_agreement, qr_pass_on, qr_oblig_finrec and the permission na_a9p1; no path is derived.',
  ['qr_fund', 'qr_agreement', 'qr_pass_on', 'qr_oblig_finrec', 'na_a9p1', 'qr_transfer_out'],
  rival='Reading the chain as direct (Commission to final recipients) is rejected because the relations of W run through the Member State.')
P('prop_pubpriv_sc1', 'public-private allocation', 'SUBCONFIGURATION', 'sc_plan', 'SC-01',
  'Implementing roles are allocated to Member States (public) with permissions to deliver support through public or private entities (A9.P1) and to entrust cohesion-policy managing authorities (A11.P3); no private body holds an assessment, decision, standard-setting or enforcement role in the S; private entities appear as intermediaries and recipients.',
  'Reading of the permissions and the pass-on relation; absence of private competences within W (closure statement).',
  ['na_a9p1', 'qr_pass_on', 'qr_entrust'], closure='cl_private')
P('prop_selfreg_arch', 'self-regulatory autonomy', 'ARCHITECTURE', 'arch_integrated', 'ARCH-01',
  'Not attributable: no provision of W delegates rule-making or enforcement to private or self-regulatory bodies; the property is not attributed to the architecture.',
  'Absence of any such delegation within W (closure statement); silence is neither permission nor prohibition.',
  ['qr_entrust', 'qr_oblig_finrec'], closure='cl_private', status='not_attributable')
P('prop_depth_sc3', 'relational depth', 'SUBCONFIGURATION', 'sc_pay', 'SC-03',
  'The conditional sequence from the Plan decision to disbursement comprises four qualified relations in series (agreement, payment request, assessment, disbursement decision) with three enforcement branches (suspension, reduction, termination); depth is counted over qualified relations only.',
  'Count of QR records in series linked by explicit legal conditions (A19.P1; A20.P1-P3; A20.P4-P7).',
  ['qr_agreement', 'qr_payreq', 'qr_payassess', 'qr_paydec', 'qr_suspend', 'qr_reduce', 'qr_terminate'],
  pathsem='A step is a qualified relation of SC-03 whose condition is the output of the preceding relation as stated in the cross-references; successive relations are linked by explicit legal conditions (A19.P1, A20.P1, A20.P2, A20.P3, A20.P4); reachability alone is not used and no transmission is inferred.',
  count='evidenced instances: 4 relations in series and 3 branches (QR records)')
P('prop_depth_sc1', 'relational depth', 'SUBCONFIGURATION', 'sc_plan', 'SC-01',
  'The Plan cycle comprises submission, assessment and decision in series (three relations), with an information request and provision loop and an amendment loop (amended Plan submission, assessment, decision or rejection).',
  'Count of QR records in series linked by explicit legal conditions (A17.P1; A18.P2-P4; A17.P4).',
  ['qr_plansub', 'qr_assess', 'qr_decision', 'qr_amend_submit', 'qr_amend_assess', 'qr_amend_decision'],
  pathsem='A step is a qualified relation whose object is the output of the preceding relation by explicit cross-reference (A17.P1 to Article 16; A18.P2 to Article 16; A18.P3 to Article 17(1)); no path semantics beyond these stated links; no transmission is inferred.',
  count='evidenced instances: 3 relations in series; 2 loops (QR records)')
P('prop_func_arch', 'functional allocation', 'ARCHITECTURE', 'arch_integrated', 'ARCH-01 (SC-01, SC-03, SC-04)',
  'By function: implementation (Commission under direct management; Member States for Plans and measures); verification and assurance (Commission assessment; Member State internal control; national implementing, signing and audit authorities); enforcement (Commission: suspension, reduction, termination, recovery); information (Member States to the Commission; Commission to institutions); rule-making lies outside the relations of W; no review or adjudication body is stated within W.',
  'Reading of the function slot of the relations and assignments of the member S; absence of a review body within W (closure statement).',
  ['qr_fund', 'qr_assess', 'qr_decision', 'qr_suspend', 'qr_recover', 'qr_assure', 'qr_desig_audit'], closure='cl_review',
  agg='Allocation listed per function and position; no composite.')
P('prop_func_monitor', 'functional allocation', 'SUBCONFIGURATION', 'sc_monitor', 'SC-05',
  'Monitoring function: Member States report (A24.P1); recipients are subject to reporting requirements (A24.P3, obligor not stated); the Commission monitors, uses common indicators and evaluates (A24.P2, A24.P4, A27); evaluation reports are addressed to four Union bodies.',
  'Origin and counterpart of the reporting and evaluation relations and the assignments of the S.',
  ['qr_report', 'qr_eval1', 'qr_eval2', 'na_monitor', 'na_indicators'])
P('prop_disc_sc1', 'discretion distribution', 'SUBCONFIGURATION', 'sc_plan', 'SC-01',
  'By function: Plan content discretion lies with Member States (permissions A4.P3, A4.P5, A8, A9, A11; promotional duty A8.P1(f)); assessment discretion lies with the Commission (criteria of A16.P3 stated without thresholds or weights; "may require" A17.P3(c)); no numeric threshold for "complies satisfactorily" is stated within W.',
  'Modality and condition slots of the relations and assignments; absence of thresholds within W (closure statement).',
  ['qr_assess', 'qr_decision', 'qr_require', 'na_a8p1', 'na_a4p3', 'na_a9p1'], closure='cl_thresholds')
P('prop_disc_sc3', 'discretion distribution', 'SUBCONFIGURATION', 'sc_pay', 'SC-03',
  'Commission discretion is bounded by mandatory wording ("shall") for suspension, reduction after nine months, termination after 15 months and pro-rata payment; discretion remains in the judgement of "satisfactorily achieved" (A20.P2) and "tangible progress" (A20.P7) without stated thresholds; Member States hold a timing option (once or twice a year).',
  'Modality slot of the relations (obligation versus competence) and absence of thresholds within W (closure statement).',
  ['qr_payassess', 'qr_suspend', 'qr_reduce', 'qr_terminate', 'qr_prorata', 'qr_payreq'], closure='cl_thresholds')
P('prop_acc_perf', 'accountability structure', 'RELATION', 'qr_acc_perf', 'SC-03 and SC-04',
  'Accountability of the Member State to the Commission: forum, duty to justify, assessment capacity and possible consequences are all evidenced within W (class ACCOUNTABILITY; sufficiency sufficient within W).',
  'DR-17 elements assembled in the accountability relation; no exercise inferred.',
  ['qr_acc_perf', 'qr_payreq', 'qr_assure', 'qr_payassess', 'qr_suspend', 'qr_reduce', 'qr_terminate', 'qr_recover'],
  rival='Reading the supervision relations alone as accountability is rejected: supervision is not accountability without the duty to explain.')
P('prop_acc_ep', 'accountability structure', 'RELATION', 'qr_acc_ep', 'SC-06',
  'Accountability of the Commission toward the competent European Parliament committees: answerability only (class ANSWERABILITY) with indeterminate sufficiency; duty to explain, assessment capacity and consequences are not stated; the discharge procedure is outside W.',
  'DR-17 elements assembled in the accountability relation; closure on the discharge procedure undetermined.',
  ['qr_acc_ep', 'qr_dialogue', 'qr_takeaccount', 'qr_epinfo'], closure='cl_discharge', status='undetermined',
  hq=['hq_acc_ep'])
P('prop_acc_monitor', 'accountability structure', 'SUBCONFIGURATION', 'sc_monitor', 'SC-05',
  'Information relations only (INFO): Member States to the Commission and the Commission to four Union bodies; no relation of W gives the recipients of the evaluation reports assessment or sanction capacity; information alone is not accountability.',
  'Accountability class of the reporting relations (INFO) and absence of follow-up capacity within W (closure statement).',
  ['qr_report', 'qr_eval1', 'qr_eval2'], closure='cl_eval_assess')
P('prop_acc_arch', 'accountability structure', 'ARCHITECTURE', 'arch_integrated', 'ARCH-01 (SC-03, SC-04) with SC-05 and SC-06 for contrast',
  'Differentiated: accountability of Member States to the Commission is sufficient within W (SC-03, SC-04); information relations toward Union institutions are INFO (SC-05); the Commission-Parliament channel is answerability-only with indeterminate sufficiency (SC-06). No composite.',
  'Per-S values listed; no aggregation beyond listing.',
  ['prop_acc_perf', 'prop_acc_monitor', 'prop_acc_ep'],
  agg='Per-S values reported first; the values of SC-05 and SC-06 are not pushed down to SC-03 and SC-04 (ecological fallacy check).',
  rival='A single accountability label for the instrument is rejected because the per-S values differ.')
P('prop_necessary', 'necessary stage', 'RELATION', 'qr_decision', 'SC-03 within ARCH-01',
  'Whether the Article 17 decision is a necessary stage for every payment of Fund resources cannot be asserted: A11.P1 provides for direct implementation of transferred resources without cross-reference to A17-A20 and the funding and payment rules outside W are not available.',
  'Absence-dependent positional property; closure test result undetermined.',
  ['qr_decision', 'qr_agreement', 'qr_paydec', 'qr_transfer_in_use'], closure='cl_necessary', status='undetermined',
  pathsem='Steps are the qualified relations of SC-03 linked by explicit conditions; alternative routes outside W are not searchable.')
P('prop_subst', 'substitutability', 'RELATION', 'qr_paydec', 'SC-03 within ARCH-01',
  'Substitutability of the individual payment decision by another route cannot be asserted for the same reasons as for the necessary-stage property.',
  'Absence-dependent positional property; closure test result undetermined.',
  ['qr_paydec', 'qr_prorata', 'qr_transfer_in_use'], closure='cl_necessary', status='undetermined')
P('prop_depth_rule', 'depth from the rule-making position', 'ARCHITECTURE', 'arch_integrated', 'ARCH-01',
  'Not attributable: the rule-making position (the legislator enacting W) is not a party of any relation of W and no path semantics from it are stated; reachability is not transmission; depth is not attributed.',
  'Absence of the rule-making position among the relation parties within W (closure statement).',
  ['qr_decision', 'qr_fund'], closure='cl_rulemaking', status='not_attributable')
P('prop_inter_sc7', 'directness and intermediation', 'SUBCONFIGURATION', 'sc_transfer', 'SC-07',
  'Resources transferred into the Fund are implemented directly by the Commission (A11.P1); resources transferred out are moved by Member States through programme amendments under the rules of the receiving funds (A11.P2, inserted Article 26a); the receiving funds rules are outside W.',
  'Origin and counterpart of the transfer relations and the programme amendment assignments.',
  ['qr_transfer_in', 'qr_transfer_in_use', 'qr_transfer_out', 'na_a28i2a'],
  rival='Reading the receiving-fund relations as relations of W is rejected (stop at the highest level supported by W).')
