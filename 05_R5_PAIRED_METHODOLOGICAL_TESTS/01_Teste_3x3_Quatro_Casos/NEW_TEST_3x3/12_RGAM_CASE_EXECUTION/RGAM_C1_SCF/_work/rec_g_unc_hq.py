# Authored uncertainties, human-review queue items and protocol deviation entries
from reg import *

# ============================== UNCERTAINTY LOG ==============================
U = unc
U('u_art1_ordinal', [], ['A1.P1', 'A1.P2', 'A1.P3', 'A29.P1', 'A29.P2'], 'SOURCE_AMBIGUITY',
  'Articles 1 and 29 consist of unnumbered paragraphs in the source file; paragraph identifiers A1.P1-P3 and A29.P1-P2 are ordinal.',
  'Ordinal identifiers assigned in source order; citations of these provisions in the text itself are not affected.',
  'None on the content of records; locator only.', None)
U('u_img', [], ['ANX1.pt10', 'ANX1.pt13', 'ANX1.pt15', 'ANX1.pt16', 'ANX1.pt17', 'ANX1.pt18'], 'SOURCE_AMBIGUITY',
  'Annex I formulae are embedded images (11 image elements in the source: six image-only paragraphs and five images inline in text units); they are not transcribed as text.',
  'Image-only paragraphs carried as placeholder units; the executor viewed three of the six image-only units (the formulae for MFAi, alpha i and beta i); the remaining images were not interpreted; no record rests on the formulae.',
  'Annex I content is represented only by its textual parts; allocation shares of Annex II are not recomputed.', 'hq_gap_annex')
U('u_gap03', [], ['A5.P3', 'A16.P2', 'A17.P1', 'A18.P2', 'A19.P1', 'A21.P1', 'A21.P2', 'A24.P4'], 'PROTOCOL_GAP',
  'Internal cross-references (GAP-03) resolve within W and supply supporting units and derivation rules.',
  'Followed as prescribed; the inferential path is stated in derivation_rule of each derived record.',
  'Derived records are limited to documented status.', None)
U('u_residual_tag', [], [], 'OTHER',
  'The function slot of many records carries a residual (flagged) tag of the RGAM-lineage function vocabulary (representation_participation*, authorization_designation*, cooperation_coordination*).',
  'Tag retained and flagged in type_note where relevant (GAP-05); no S or A rests on function tags.',
  'Counts by function are descriptors only.', 'hq_gap_function')
U('u_function_unres', [], ['A10.P3', 'A21.P3', 'A27.P1', 'A27.P4'], 'PROTOCOL_GAP',
  'The legally grounded function of the provision (budgetary use of appropriations; purpose-limited processing of personal data; proposals for amendment of the instrument) cannot be placed in the documented function vocabulary.',
  'FUNCTION_VOCABULARY_UNRESOLVED written in the function field (GAP-05); the legally grounded description is kept in action, object and mechanism.',
  'No function-based claim is made for these records.', 'hq_gap_function')
U('u_nearest_type', [], [], 'OTHER',
  'Relation type fitted to the nearest of the ten RGAM types: contractual_exchange for performance-conditioned funding; information_reporting for guidance and joint communication; oversight_supervision for the duty to take account of dialogue views.',
  'Nearest type recorded with type_note flag (RGAM-DR-15); no new type created.', 'Counts by relation type are descriptors only.', 'hq_other_types')
U('u_fund_origin', [], ['A1.P2', 'A7.P1', 'A7.P3', 'A12.P0'], 'DIRECTION',
  'The textual subject of A1.P2, A7.P1 and A7.P3 is the Fund, a device (never an actor); the origin of the funding relation is attributed to the Commission through A12.P0 (derived); the prohibition of A7.P3 is borne by the device as textual subject.',
  'Derived relation with the Fund as instrument; NA borne by the device; the attribution is flagged and queued.', 'Direction Commission to Member State is derived; textual direction recorded separately.', 'hq_direction')
U('u_revenue', [], ['A10.P1', 'A19.P1', 'A20.P9', 'A20.P10', 'A27.P4'], 'EXTERNAL_DEPENDENCY',
  'Availability, amounts and distribution of the revenue financing the Fund rest on Directive 2003/87/EC (Articles 10a(8b), 30d(3), 30d(4), 30d(5), 30k).',
  'EXT records with constitutive dependency; funding-related claims scoped within the declared corpus; conditional status recorded where the trigger is an external event.',
  'Claims about availability of funding are undetermined.', 'hq_extdep_revenue')
U('u_fr_dependence', [], ['A11.P1', 'A12.P0', 'A19.P1', 'A20.P3', 'A20.P5', 'A20.P9'], 'EXTERNAL_DEPENDENCY',
  'Direct management, individual legal commitment, authorisation of disbursement and budgetary derogations rest on Regulation (EU, Euratom) 2018/1046.',
  'EXT records; relations recorded as stated in W; mechanics outside W not assessed.', 'Claims on commitment and payment mechanics are within the declared corpus only.', 'hq_extdep_fr')
U('u_cpr_dependence', [], ['A11.P1', 'A11.P2', 'A11.P3', 'A28.INS26a.P1'], 'EXTERNAL_DEPENDENCY',
  'Transfers, receiving funds, programmes and managing authorities rest on Regulation (EU) 2021/1060, which W also amends by Article 28.',
  'EXT records; effect expressed in W coded (GAP-02); the amended act is not analysed.', 'SC-07 claims stop at the highest level supported by W.', 'hq_extdep_cpr')
U('u_manauth_ext', [], ['A11.P3'], 'EXTERNAL_DEPENDENCY',
  'The managing authorities of cohesion policy programmes are positions established under Regulation (EU) 2021/1060, not constituted in W.',
  'Position recorded as type-level without establishment norm (NONE; not_applicable).', 'No claim about their constitution or powers.', 'hq_extdep_cpr')
U('u_ext_bodies', [], ['A21.P2.pte', 'ANX3.pt6.ptb'], 'EXTERNAL_DEPENDENCY',
  'The rights of OLAF, the Court of Auditors, the Commission and the EPPO, and the identity of Member States participating in enhanced cooperation, are determined outside W.',
  'Authorisation and access relations recorded with the bodies as recipients; content of rights not asserted.', 'Claims on the scope of audit powers are restricted.', 'hq_extdep_audit')
U('u_ext_category', [], ['A2.P0.pt8', 'A2.P0.pt9', 'A2.P0.pt10', 'A2.P0.pt11'], 'EXTERNAL_DEPENDENCY',
  "The scope of 'household' and 'micro-enterprise', and so of the vulnerable households and micro-enterprises categories, rests on definitions in Regulation (EU) 2019/1700 and Commission Regulation (EU) No 651/2014.",
  'Categories recorded as type-level positions; EXT with constitutive dependency.', 'Claims about the extent of these categories are within the declared corpus only.', 'hq_extdep_definitions')
U('u_ext_reporting_channel', [], ['A18.P5', 'A24.P1'], 'EXTERNAL_DEPENDENCY',
  'The reporting vehicle (integrated national energy and climate progress reports under Regulation (EU) 2018/1999, Articles 17 and 28) is defined outside W.',
  'Relations recorded as stated in W with documented status; EXT with constitutive dependency.', 'Claims on timing and content of the vehicle are restricted.', 'hq_extdep_reporting')
U('u_epbd', [], ['A2.P0.pt13', 'A6.P3.ptd', 'A16.P3.ptb.ptiii', 'ANX4.pt9', 'ANX4.pt20', 'ANX4.pt33'], 'SOURCE_AMBIGUITY',
  'Several instruments (energy performance of buildings recast, energy efficiency recast, alternative fuels infrastructure) are referred to without number or date and cannot be identified within W.',
  'EXT records state the reference as printed; no verification (GAP-04).', 'No relation depends on the content of these instruments.', 'hq_extdep_definitions')
U('u_implact', [], ['A17.P1', 'A18.P3', 'A20.P3'], 'CLOSURE',
  'W does not state the adoption procedure of the Commission implementing acts and individual decisions (committee involvement, if any).',
  'Closure record (undetermined); decision-centre plurality recorded undetermined.', 'Plurality and sole-decision-taker claims are within the declared corpus only.', None)
U('u_a26_acc', [], ['A26.P1', 'A26.P2', 'A25.P3'], 'ACCOUNTABILITY_SUFFICIENCY',
  "A26.P1 states transparency and accountability as purpose; forum, channel and questioning capacity are evidenced, but the duty to explain, assessment capacity and consequences are not stated ('may invite').",
  'Recorded as ANSWERABILITY with sufficiency indeterminate and missing elements listed (answerability_only flag).', 'Accountability of the Commission toward the Parliament is not asserted.', 'hq_acc_ep')
U('u_acc_perf', [], ['A20.P1', 'A20.P2', 'A20.P4', 'A20.P6', 'A20.P7', 'A21.P2.ptc', 'A21.P4'], 'ACCOUNTABILITY_SUFFICIENCY',
  'Accountability of Member States to the Commission is assembled from several provisions; the elements are stated in W, while payment mechanics rest partly on the Financial Regulation.',
  'Recorded as ACCOUNTABILITY with sufficiency sufficient within W; elements listed in the derivation rule.', 'Claim restricted to the elements stated in W.', None)
U('u_discharge', [], ['A21.P3'], 'EXTERNAL_DEPENDENCY',
  'The discharge procedure (Article 319 TFEU) and integrated accountability reporting (Article 247 of the Financial Regulation) are outside W; the discharge authority and its capacities are not stated.',
  'EXT with constitutive dependency; no accountability relation toward a discharge authority admitted.', 'Any accountability claim toward a discharge authority is undetermined.', 'hq_extdep_discharge')
U('u_ics_dev', [], ['A21.P1', 'ANX3.pt1'], 'DEV_THRESHOLD',
  "The 'internal control system' of A21.P1 and Annex III is singled out and governed by Annex III key requirements, but it is a bundle of arrangements and designations of each Member State without a stated operator or bounded legal form of its own.",
  'Kept as INS-TYPE characteristic (BORDERLINE_INS-TYPE) in instrument_ref; queued.', 'No device record; no claim that the system is an actor or position.', 'hq_dev_ics')
U('u_perfsys_dev', [], ['A24.P3'], 'DEV_THRESHOLD',
  "The 'performance reporting system of the Commission' is identified and has a bounded function but is not constituted by W and has no stated governing rules.",
  'PD record with BORDERLINE_INS-TYPE classification because it bears an NA as textual subject; queued.', 'No claim about its establishment.', 'hq_dev_perfsys')
U('u_unresolved_authorities', [], ['ANX3.pt1.pta', 'ANX3.pt1.ptb', 'ANX3.pt4.pta', 'ANX3.pt5.pta'], 'SOURCE_AMBIGUITY',
  "Annex III positions (implementing authorities, signing authority, audit body) are type-level; whether they coincide, overlap, or coincide with managing authorities is not stated; the obligation is to designate them (N2).",
  'Three separate type-level positions recorded; no instances inferred; N2 recorded.', 'No claim about their number or identity.', None)
U('u_recip_overlap', [], ['A21.P2.pte', 'A23.P2', 'A24.P3'], 'SOURCE_AMBIGUITY',
  "'Final recipients of the financial allocations', 'recipients of support from the Fund' and the vulnerable groups are used without a stated relationship (overlap or identity).",
  'Recorded as separate type-level positions as printed; no identity inferred.', 'Relations involving these categories are recorded separately.', None)
U('u_open_category', [], ['A5.P1'], 'SOURCE_AMBIGUITY',
  "'Other stakeholders' is an open-ended category; no member is identifiable.", 'Recorded as a type-level position with unspecified multiplicity.', 'Consultation relation recorded with an open category.', None)
U('u_generic_national_law', [], ['A5.P1', 'A21.P1'], 'EXTERNAL_DEPENDENCY',
  "Generic references to 'national legal framework' and 'applicable Union and national law' identify no specific source.", 'Recorded as one generic EXT; no content assumed.', 'No claim on national law content.', None)
U('u_a14p2', [], ['A14.P2'], 'DIRECTION',
  'The recipient of the request up to the maximum financial allocation is not stated in A14.P2.', 'NA recorded without counterparty; no counterparty invented.', 'No relation admitted.', 'hq_direction')
U('u_a20p4b', [], ['A20.P4'], 'DIRECTION',
  'The recipient of the observations the Member State may present is not stated in A20.P4.',
  'Recorded as an entitlement relation with the Commission as origin (assessor whose communication starts the period), flagged.', 'Direction defensible from context but not stated.', 'hq_direction')
U('u_a23p2_obligor', [], ['A23.P2'], 'DIRECTION', 'The obligor of the duty to inform the recipients of the origin of the funds is not stated (passive wording).',
  'NA with entitlement modality on the recipients; no obligor invented.', 'No relation admitted.', 'hq_direction')
U('u_a25p2', ['s_a25p2'], ['A25.P2'], 'DIRECTION', 'The obligor of the duty that information transmitted to the Council be made available simultaneously to the European Parliament is not stated (passive wording).',
  'Statement kept without a record; no obligor invented (the Commission is the transmitter of the information but is not named as the party making it available).', 'No relation admitted for this duty.', 'hq_direction')
U('u_a24p3b_obligor', [], ['A24.P3'], 'DIRECTION', 'The party imposing proportionate reporting requirements on recipients is not stated (passive wording).',
  'NA on the recipients; no counterparty invented.', 'No relation admitted.', 'hq_direction')
U('u_a28_counterpart', [], ['A28.INS26a.P2', 'A28.INS26a.P3'], 'DIRECTION',
  'The counterparty to which programme amendments and notifications are submitted is not stated in the inserted provisions (it may follow from the amended act, outside W).',
  'NAs recorded without counterparty; no counterparty invented.', 'No relation admitted for these duties.', 'hq_direction')
U('u_assurance_source', [], ['ANX3.pt1.ptc'], 'DIRECTION', 'The source of the assurance that the signing authority is to get is not stated.',
  'Relation recorded between the Member State (obligor) and the signing authority (recipient); flagged.', 'Direction defensible only partly.', 'hq_direction')
U('u_symmetric', [], ['A16.P1'], 'DIRECTION', "The permission to extend the assessment deadline is symmetric ('The Member State and the Commission may agree').",
  'Direction by textual order only; no governance direction.', 'None.', 'hq_direction')
U('u_a16p1d2_recipient', [], ['A16.P1'], 'DIRECTION', 'The recipient of a revised Plan is not stated in the sentence granting the permission to revise.',
  'NA without counterparty.', 'No relation admitted.', 'hq_direction')
U('u_a6p4a_participants', [], ['A6.P4'], 'SOURCE_AMBIGUITY', 'The participants in the exchange of good practices organised by the Commission are not stated.',
  'NA without counterparty.', 'No relation admitted.', None)
U('u_a6p4b_provider', [], ['A6.P4'], 'SOURCE_AMBIGUITY', 'The provider of technical support under the ELENA facility or the Technical Support Instrument is not a position named in W.',
  'NA without counterparty; EXT records.', 'No relation admitted.', None)
U('u_xref_26a', [], ['A11.P2', 'A28.INS26a.P1'], 'SOURCE_AMBIGUITY',
  "A11.P2 refers to 'Article 26a of Regulation (EU) 2021/1060', which Article 28 of W inserts; inside the inserted text 'this Regulation' means Regulation (EU) 2021/1060 and 'Regulation (EU) 2023/955' means W; the reading of internal versus external reference is ambiguous.",
  'Treated as an internal cross-reference for the text of inserted Article 26a (GAP-03) and as external for the rest of Regulation (EU) 2021/1060 (GAP-02); queued.', 'Transfer relations scoped to the text inserted by W.', 'hq_xref')
U('u_xref_a22', [], ['A22.P0', 'A6.P3'], 'SOURCE_AMBIGUITY',
  "A22.P0 refers to 'the Union programmes and instruments referred to in Article 6(3)', but A6.P3 lists plans and programmes under various acts, not all of which are Union programmes or instruments.",
  'Followed as an internal cross-reference to the A6.P3 list; the NA is recorded without counterparty.', 'No relation admitted for the coordination duties.', 'hq_xref')
U('u_coupling_threshold', [], ['A17.P1', 'A19.P1', 'A20.P1', 'A21.P2', 'A24.P1', 'A27.P1'], 'COUPLING_THRESHOLD',
  'The I2/I3 warrant thresholds are unvalidated: whether explicit cross-references among S qualify as coupling that makes an integrated whole is a matter for human adjudication.',
  'Each INTEGRATED or OVERLAPPING outcome is queued; no numeric threshold used.', 'Outcomes are provisional.', 'hq_integration')
U('u_independent_eval', [], ['A27.P3'], 'SOURCE_AMBIGUITY', "The ex post evaluation report is called 'independent' but the body ensuring independence is not stated.",
  'Relation recorded with the Commission as origin.', 'No claim about the independence.', None)
U('u_diffuse_public', [], ['A23.P1', 'A23.P2'], 'SOURCE_AMBIGUITY',
  "The public, the media and 'multiple audiences' are diffuse categories without institutionally identifiable capacities; not admitted as parties of a relation.",
  'Duties recorded as NAs with no counterparty.', 'No information relation toward the public is admitted.', None)
U('u_cap_wording', [], ['A8.P3'], 'DRAFTING_CUE', "'shall be up to 2,5 %' expresses a limit without an explicit prohibition formula.",
  'Treated as a limit (prohibition recorded as constraint_only) without further inference.', 'None.', None)
U('u_normtype_a7p2', [], ['A7.P2', 'A20.P1'], 'DRAFTING_CUE',
  "Payment 'shall be conditional upon' achievement of milestones and targets: an N4 condition on legal effect combined with a stated duty to pay on achievement.",
  'Condition recorded in conditions of the funding and payment relations; queued as a possible compound norm type.', 'Norm type not stated on relation records (no field).', 'hq_normtype')
U('u_normtype_a8p1f', [], ['A8.P1.ptf'], 'DRAFTING_CUE',
  "'shall aim to ensure that where ... prioritised' combines a promotional duty of means with a condition.", 'Recorded as obligation_promotional with norm type AMBIGUOUS; queued.',
  'None.', 'hq_normtype')
U('u_normtype_a8p2', [], ['A8.P2'], 'DRAFTING_CUE',
  "A8.P2 combines a permission ('may include'), a conditional permission ('may provide ... if their Plans contain') and mandatory qualifications ('shall be temporary and decrease over time').",
  'Recorded as COMPOUND; queued.', 'None.', 'hq_normtype')
U('u_normtype_a28i3', [], ['A28.INS26a.P3'], 'DRAFTING_CUE', 'A permission conditional on a prior approval and a restriction on the content of changes.',
  'Recorded as COMPOUND; queued.', 'None.', 'hq_normtype')
U('u_annex2_inst', [], ['ANX2.pt6', 'ANX2.pt32'], 'OTHER',
  'Annex II names 27 Member States with allocation values; they are not recorded as individual INSTANCE positions because the named states bear no separate assignment or relation.',
  'Member State recorded as one type-level position with stated multiplicity (27 named rows).', 'Allocation values are an attribute of the funding relation.', None)
U('u_anx5', [], ['ANX5.pt1', 'ANX5.pt40'], 'SOURCE_AMBIGUITY',
  'Annex V is a template: table-of-contents rows (some with marker-only or empty cells), summary-box placeholders and empty template tables are carried as units; the structure of the template tables cannot be fully represented in the source file.',
  'Template content captured in four section statements; marker-only rows screened as not relevant.', 'No relation rests on the empty template cells.', 'hq_gap_annex')
U('u_family_gap', [], [], 'PROTOCOL_GAP',
  'The allocation of the ten architectural dimensions to families F1-F5 is not stated in the allowed protocol sources.',
  'Families assigned by the listed order of the dimensions (two per family); the three positional examples (necessary stage, depth from the rule-making position, substitutability) have no family value; flagged in PROTOCOL_DEVIATION_LOG.',
  'The family field is an organising proposal only; no claim depends on it.', 'hq_gap_family')

# ============================== HUMAN REVIEW QUEUE ==============================
hq('hq_integration', 'HQ-INTEGRATION', ['arch_integrated'],
   'Is the candidate ARCH-01 (SC-01 with nested SC-02, SC-03, SC-04, SC-07) an integrated architecture within W under I1-I4, that is, are the qualified procedural dependencies (I2) and the conditional-sequence consequence (I3) sufficient?',
   '(a) integrated within W; (b) two or more separately constituted architectures joined only at the Article 17 decision; (c) indeterminate pending the external funding and financial rules.',
   'Retain INTEGRATED scoped to the declared corpus W; I2 rests on explicit cross-references independent of shared actors; I3 is a conditional sequence read from stated conditions.',
   'The I2/I3 thresholds are unvalidated (RGAM-DR-28).')
hq('hq_overlap', 'HQ-OVERLAP', ['arch_monitor'],
   'Is the candidate ARCH-02 (SC-05 monitoring, reporting and evaluation) partially integrated with ARCH-01 through the Annex IV interface (A6.P1(m), A17.P2(d)-(e), A24.P1, A24.P4), or is it a distinguishable candidate or part of ARCH-01?',
   '(a) partially integrated (overlap through the mandatory Annex IV interface); (b) distinguishable; (c) a monitoring stage inside ARCH-01.',
   'Retain OVERLAPPING_OR_PARTIALLY_INTEGRATED; the intersection is not a third architecture; no legal link between A24 reports and A20 payment assessment was found.',
   'The overlap and I2/I3 thresholds are unvalidated.')
hq('hq_acc_ep', 'HQ-ACCOUNT', ['qr_acc_ep', 'qr_dialogue', 'qr_takeaccount', 'qr_epinfo', 'sc_parl', 'arch_dialogue', 'prop_acc_ep'],
   "Does the social climate dialogue of A26 (with A25.P3 and A26.P2) constitute accountability, answerability only, or information only, given that the provision states accountability as a purpose but 'may invite' creates no stated duty to explain and no assessment capacity or consequence?",
   '(a) ANSWERABILITY with insufficient evidence; (b) INFO only; (c) ACCOUNTABILITY supported by the Treaty framework outside W.',
   'Retain ANSWERABILITY with sufficiency indeterminate (answerability_only) and list the missing elements.',
   'The sufficiency of accountability elements is borderline and the provision itself asserts accountability.')
hq('hq_normtype', 'HQ-NORMTYPE', ['na_a8p1f', 'na_a8p2', 'na_a28i3', 'na_propose2', 'qr_fund', 'qr_paydec', 'qr_transfer_in'],
   "What norm type (N1-N4, compound or ambiguous) applies to: 'shall aim to ensure that where ... prioritised' (A8.P1(f)); the combined permissions and mandatory qualifications of A8.P2; the conditional notification permission of Article 26a(3) inserted by A28; the proposal duty conditional on the establishment of an own resource (A27.P4); conditional payment (A7.P2, A20.P1); and the permission to request transfers 'subject to the conditions' of Regulation (EU) 2021/1060 (A11.P1)?",
   'Each wording may be read as N0 (ordinary norm), N3 (permission/competence), N4 (condition on legal effect) or COMPOUND.',
   'Keep the recorded types (AMBIGUOUS, COMPOUND, N4) pending adjudication; conditions are recorded in the conditions slot.',
   'Wording is compound or ambiguous on the authentic text; drafting cues are not inferred (RGAM-DR-13).')
hq('hq_dev_ics', 'HQ-DEV', ['na_ics', 'na_ics1d', 'na_ics2', 'na_ics3', 'na_ics4', 'na_ics5'],
   "Is the 'internal control system' of A21.P1 and Annex III an institutional device (DEV: identity plus operator, governing rules or bounded function) or a typed characteristic (INS-TYPE) of the duties of the Member State?",
   '(a) DEV (identity: the Member State internal control system; governing rules: Annex III); (b) INS-TYPE (a bundle of arrangements and designations without own operator or legal form).',
   'Keep as INS-TYPE (BORDERLINE_INS-TYPE) in instrument_ref; no device record.',
   'Device threshold borderline (RGAM-DR-12).')
hq('hq_dev_perfsys', 'HQ-DEV', ['p_perfsys', 'na_perfsys'],
   "Is 'the performance reporting system of the Commission' (A24.P3) a device or an INS-TYPE characteristic, and may it bear an assignment as textual subject?",
   '(a) DEV (identity, operator Commission, bounded function); (b) INS-TYPE with the duty attributable to the Commission.',
   'Keep BORDERLINE_INS-TYPE with the textual subject recorded; no actor status.',
   'Device threshold borderline; textual subject is a system.')
hq('hq_xref', 'HQ-XREF', ['qr_transfer_out', 'sc_transfer', 'na_coord_com', 'na_coord_ms'],
   "Do (i) the reference in A11.P2 to Article 26a of Regulation (EU) 2021/1060 (inserted by Article 28 of W) and (ii) the reference in A22.P0 and A16.P3 to 'Union programmes and instruments referred to in Article 6(3)' resolve within W, and with what scope?",
   'Internal reference to the inserted text and the A6.P3 list versus external reference to the amended act and to instruments outside W.',
   'Treat both as internal for the inserted text and the A6.P3 list; keep external content undetermined.',
   'The cross-references are ambiguous (RGAM-DR-20).')
hq('hq_direction', 'HQ-DIRECTION', ['s_a25p2', 'qr_fund', 'qr_extend', 'qr_obs_a20p4', 'qr_assurance_signauth', 'na_a14p2', 'na_recip_entitled', 'na_recip_report', 'na_a28i2a', 'na_a28i3', 'na_revise'],
   "Where the text does not state the counterparty or obligor (request up to the maximum allocation, A14.P2; observations, A20.P4; information duty to recipients, A23.P2; reporting requirements, A24.P3; programme amendments and notifications, A28; revised Plan, A16.P1; source of assurance, Annex III item 1(c)) or states a symmetric permission (A16.P1), or where origin is derived from the device Fund (A1.P2, A7.P1), may a counterparty or direction be recorded?",
   'Counterparty implied by context (Commission, Member State) versus no relation admitted until stated.',
   'Keep NAs without counterparty; keep flagged relations (qr_fund derived; qr_obs_a20p4; qr_assurance_signauth) as recorded.',
   'Direction not fully defensible from text (RGAM-DR-28).')
hq('hq_gap_family', 'HQ-GAP', ['prop_cent_sc1', 'prop_vert_sc1', 'prop_depth_sc3', 'prop_func_arch', 'prop_disc_sc1', 'prop_acc_perf', 'prop_necessary'],
   'Which of the families F1-F5 does each of the ten architectural dimensions belong to, and which family (if any) do the positional examples belong to? The allowed protocol sources do not state the allocation.',
   'Allocation by the listed order of the dimensions (two per family) versus another allocation.',
   'Keep the provisional allocation by listed order; leave the positional examples without family.',
   'Protocol gap (RGAM-DR-32).')
hq('hq_gap_function', 'HQ-GAP', ['na_a10p3', 'na_data_ms', 'na_data_com', 'na_propose1', 'na_propose2', 'qr_consult', 'qr_auditauth', 'qr_decision'],
   'Which function category (if any) of the RGAM-lineage vocabulary fits: budgetary use of appropriations for administrative expenditure; purpose-limited processing of personal data; proposals for amendment of the instrument; and the residual-tag cases (consultation, authorisation and designation, decision on a Plan)?',
   'Residual tags (representation_participation*, authorization_designation*, cooperation_coordination*) versus FUNCTION_VOCABULARY_UNRESOLVED.',
   'Keep FUNCTION_VOCABULARY_UNRESOLVED and the flagged residual tags; do not create new categories.',
   'Function vocabulary gap (GAP-05).')
hq('hq_gap_annex', 'HQ-GAP', ['ext_cpr_amend', 'na_a28i2a', 'na_a28i2b', 'na_a28i3', 'na_template', 'sc_transfer'],
   'Are the coding of annexes like operative provisions (GAP-01), the coding of the amending Article 28 for its effect expressed in W only (GAP-02), and the non-transcription of Annex I formula images and Annex V template tables acceptable for this case?',
   'Annexes and the amending provision coded as stated in the execution addendum versus a different treatment.',
   'Keep the addendum treatment and the declared exclusions.', 'Protocol gap decisions require confirmation (RGAM-DR-32).')
hq('hq_extdep_revenue', 'HQ-EXTDEP', ['ext_ets_revenue', 'ext_ets_postpone', 'ext_ets_distrib', 'ext_tfeu311', 'qr_fund', 'qr_paydec', 'qr_prorata', 'qr_unused', 'na_propose2', 'na_a10p3'],
   'Funding availability, amounts, the postponement branch and the distribution of unused amounts rest on Directive 2003/87/EC and TFEU Article 311(3). Should payment-related claims remain restricted to the declared corpus (undetermined beyond W)?',
   'Within-corpus claim versus claim requiring verification of the Directive.', 'Keep claims within the declared corpus; keep conditional status for the own-resource proposal duty.',
   'Constitutive dependency on an unresolved external reference (RGAM-DR-20).')
hq('hq_extdep_fr', 'HQ-EXTDEP', ['ext_fr_general', 'qr_agreement', 'qr_paydec', 'qr_fund', 'na_a12'],
   'Direct management, individual legal commitment and authorisation of disbursement rest on Regulation (EU, Euratom) 2018/1046. Should claims on commitment and payment mechanics remain restricted to what W states?',
   'Within-corpus claim versus claim requiring verification of the Financial Regulation.', 'Keep claims within the declared corpus.',
   'Constitutive dependency on an unresolved external reference.')
hq('hq_extdep_cpr', 'HQ-EXTDEP', ['ext_cpr_transfer', 'ext_cpr_amend', 'qr_transfer_in', 'qr_transfer_in_use', 'qr_transfer_out', 'qr_entrust', 'p_manauth', 'sc_transfer'],
   'Transfers to and from shared management, programme amendments, receiving funds and the managing authorities rest on Regulation (EU) 2021/1060, also amended by Article 28. Should the transfer claims stop at the relation level recorded?',
   'Stop at the highest level supported by W versus extension to the amended act.', 'Stop at the relation level; keep sc_transfer scoped to the text of W.',
   'Constitutive dependency on an unresolved external reference (and GAP-02).')
hq('hq_extdep_audit', 'HQ-EXTDEP', ['ext_fr_rights', 'ext_eppo', 'qr_auditauth', 'qr_access', 'p_eppo'],
   'The content of the rights of the Commission, OLAF, the Court of Auditors and the EPPO and the identity of Member States participating in enhanced cooperation are determined outside W. Should the relations remain at documented status?',
   'Documented status versus claims about the scope of audit powers.', 'Keep documented status and name the EPPO only where participation applies.',
   'Constitutive dependency on an unresolved external reference.')
hq('hq_extdep_discharge', 'HQ-EXTDEP', ['ext_discharge', 'na_report_discharge'],
   'A21.P3 places the Fund under reporting in the discharge procedure (Article 319 TFEU; Article 247 of the Financial Regulation). Should any accountability claim toward a discharge authority remain undetermined?',
   'Undetermined versus an accountability relation toward the discharge authority.', 'Keep undetermined; no relation admitted.', 'Constitutive dependency on an unresolved external reference.')
hq('hq_extdep_reporting', 'HQ-EXTDEP', ['ext_gov_report', 'qr_report', 'qr_selfassess_submit'],
   'The reporting vehicle for biennial implementation reports and the Plan appropriateness assessments is the integrated national energy and climate progress report of Regulation (EU) 2018/1999. Should the reporting relations remain at documented status?',
   'Documented status versus legal_constitution_evidenced.', 'Keep documented status.', 'Constitutive dependency on an unresolved external reference.')
hq('hq_extdep_definitions', 'HQ-EXTDEP', ['ext_reg20191700', 'ext_reg6512014', 'p_vh', 'p_vme', 'qr_pass_on', 'ext_epbd', 'ext_ee_directive', 'ext_afi_reg'],
   "The scope of the vulnerable households and micro-enterprises categories rests on external definitions, and three referenced instruments are cited without number or date. Should claims on the extent of the categories and on the referenced requirements remain restricted to W?",
   'Within-corpus claim versus verification of the instruments.', 'Keep claims within the declared corpus.', 'Constitutive dependency and source ambiguity.')
hq('hq_other_types', 'HQ-OTHER', ['qr_fund', 'qr_guidance', 'qr_jointcomm', 'qr_takeaccount', 'qr_consult', 'qr_obs_a20p4'],
   'Are the nearest-type codings acceptable: contractual_exchange for performance-conditioned funding (A1.P2/A7.P1/A7.P2); information_reporting for technical guidance (A6.P5) and joint communication (A23.P3); oversight_supervision for the duty to take account (A26.P2); representation_participation for consultation and hearing rights?',
   'Nearest-type coding with flags versus another of the ten types.', 'Keep nearest-type coding with flags.', 'Relation content fits none of the ten types exactly (RGAM-DR-15).')

# ============================== PROTOCOL DEVIATION / GAP LOG ==============================
dev('d_gap01', 'RGAM-DR-08', 'Annexes I-V treated as units of W and screened and coded under the same admission rules as articles: Annex I-II (allocation formula and table) yield statements but no relation or assignment; Annex III yields assignments and relations; Annex IV yields statements supporting reporting duties and one assignment; Annex V yields statements supporting the template duty.',
    'Execution addendum GAP-01.', 'Annex content does not become analytically material merely by existing; records only where admission rules are met.', 'GAP-01')
dev('d_gap02', 'RGAM-DR-08', 'Article 28 (amendment of Regulation (EU) 2021/1060 by insertion of Article 26a) coded for the legal effect expressed in W: units A28.P0 and A28.INS26a.P1-P5 screened and used for assignments and an EXT record; the amended act is neither retrieved nor analysed.',
    'Execution addendum GAP-02.', 'Transfer claims stop at the relation level supported by W; EXT constitutive dependency recorded; queued HQ-GAP and HQ-EXTDEP.', 'GAP-02')
dev('d_gap03', 'RGAM-DR-20', 'Internal cross-references followed within W (e.g. A17.P1 to Article 16; A19.P1 to Article 17; A20.P1-P2 to Article 17; A21.P1 to Annex III; A21.P2 to Article 19; A24.P4 to Annex IV; A6.P7 to Annex V; A11.P2 to inserted Article 26a): source and referenced provisions recorded as supporting units with derivation rules.',
    'Execution addendum GAP-03.', 'Derived records capped at documented status; ambiguous references queued (HQ-XREF).', 'GAP-03')
dev('d_gap04', 'RGAM-DR-20', 'No external legal retrieval; every EXT record is not_checked and outside_corpus_not_expanded; constitutive dependencies make dependent claims undetermined or scoped to the declared corpus; no web browsing and no retrieval of statutes, delegated or implementing acts, guidance or case law.',
    'Execution addendum GAP-04.', 'See EXTERNAL_REFERENCES, CLOSURE_REGISTER and HQ-EXTDEP items.', 'GAP-04')
dev('d_gap05', 'RGAM-DR-15', "Function vocabulary: only the data-dictionary FUNCTION vocabulary used, including flagged residual tags (representation_participation*, authorization_designation*, cooperation_coordination*) and the token FUNCTION_VOCABULARY_UNRESOLVED for budgetary use of appropriations, purpose-limited processing of personal data and legislative proposals; no V8 or new category.",
    'Execution addendum GAP-05.', 'Function-based counts are descriptors only; queued HQ-GAP (function).', 'GAP-05')
dev('d_gap06', 'RGAM-DR-25', "The 'six questions' of the operational template are not operative; recorded as NON_OPERATIVE_SOURCE_GAP; they were not reconstructed and were not used as an admission, exclusion or inference rule; S to A inference follows the four-step I1-I4 sequence only.",
    'Execution addendum GAP-06 (token NON_OPERATIVE_SOURCE_GAP).', 'None on records.', 'GAP-06')
dev('d_gap07', 'RGAM-DR-12', "Definitional provisions (Article 2) screened as scope/definitional-context; defined terms yield a position only where they bear an assignment or relation elsewhere (vulnerable households, micro-enterprises and transport users); definitions do not establish relations.",
    'Execution addendum GAP-07.', 'Only three definitional units yield position records; other definitions are screened without records.', 'GAP-07')
dev('d_family', 'RGAM-DR-24', 'The allocation of the ten architectural dimensions to families F1-F5 is not stated in the allowed sources; families assigned by the listed order of the dimensions (two per family); the three positional examples are left without family value.',
    'Protocol gap: family allocation absent from the data dictionary and the decision rules.', 'Family column is an organising proposal only; queued HQ-GAP.', '')
dev('d_path', 'RGAM-DR-05', 'Output root read as 12_RGAM_CASE_EXECUTION/RGAM_C1_SCF/ instead of 12_RGAM_EXECUTION/<CAPSULE_ID>/.', 'Path clarification of the execution addendum.', 'None on content.', '')
dev('d_units', 'RGAM-DR-05', "Addressable units beyond those exemplified in the data dictionary: page header (HDR), title (TITLE), preamble formulae (PBL, WHR, ENC), citations (CIT1-CIT6), chapter and article headings (CH1-5, A{n}.HD; HEADING_ONLY), final formula (FIN.*), footnotes (FN1-FN37, ANX4.FN1; FORMAL_OTHER); unnumbered paragraphs of Articles 1 and 29 identified by ordinal (A1.P1-P3, A29.P1-P2); lead-in paragraphs of Articles 2, 22 as A{n}.P0; subparagraphs following enumerated points as .cont{n}; inserted Article 26a paragraphs as A28.INS26a.P{k}; annex items by ordinal ANX{n}.pt{k}; point labels as printed (pta, pti).",
    'Every text element of the source file must be addressable (RGAM-DR-06) and the dictionary does not cover all structural elements.', 'Identifiers are stable and documented in W_DECLARATION; headings are never evidence.', '')
dev('d_img', 'RGAM-DR-08', 'Annex I formula images are not transcribed; six image-only paragraphs carried as placeholder units; five further images inline in text units; three of the six image-only units were viewed by the executor.',
    'Content not representable as text in the source file.', 'Declared in W_DECLARATION.exclusions and the uncertainty log; no record rests on the formulae.', 'GAP-01')
dev('d_status', 'RGAM-DR-18', 'Application of the status ceiling: legal_constitution_evidenced is assigned only to direct records whose norm is in force for the reference date (evidenced by A29.P1, A29.P2 and the binding formula) and whose constitution does not rest on an unresolved constitutive external reference; derived records and records with such dependencies are documented. No record carries material_establishment_evidenced or exercise_evidenced.',
    'Operationalisation choice within the frozen rule; not a change of method.', 'See status profile.', '')
