"""Build the ENVIO_R4_TO_DAVID delivery package.

Packaging and documentation only. No scientific source file is modified, moved or
deleted. Every copy is byte-verified against its source; a mismatch aborts that file
and is reported as COPY_INTEGRITY_FAILURE.
"""
import csv, hashlib, os, shutil, sys

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
R4 = os.path.join(REPO, 'R4_CROSS_DOMAIN_VALIDATION')
PKG = os.path.join(REPO, 'ENVIO_R4_TO_DAVID')

TERRA = 'GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)'
CLAUDE = ('Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; '
          'RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; '
          'MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE')
LUNA = 'Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv'
HUMAN = 'Igor Caires Machado (human researcher)'
DET = 'Deterministic script (no model inference)'
MIXED_TC = f'{TERRA} + {CLAUDE}'

# (src_rel_to_R4, dest_subpath, phase, artifact_type, evidence_level, created_by,
#  model_provenance, human_validated, frozen, final_or_supporting, purpose, supports, notes)
F = []


def add(src, dest, phase, atype, elevel, by, prov, hv, frozen, fos, purpose, supports, notes=''):
    F.append(dict(src=src, dest=dest, phase=phase, atype=atype, elevel=elevel, by=by,
                  prov=prov, hv=hv, frozen=frozen, fos=fos, purpose=purpose,
                  supports=supports, notes=notes))


D1 = '01_FINAL_R4_DATASET'
# Absolute source: the workbook was authored outside the repository.
add('ABS::' + os.path.join(os.path.expanduser('~'), 'Downloads',
                           'R4_Digital_Validation_Dashboard.xlsx'),
    D1, 'R4 delivery', 'FINAL OUTPUT', 'AUTHORITATIVE_FINAL',
    HUMAN + ' with Claude assistance', CLAUDE, 'YES', 'YES', 'FINAL',
    'FINAL_R4_CONSOLIDATED_DATASET. Five worksheets (Dashboard, Key Findings, Metrics, '
    'Source Data, Method Notes) plus four charts, consolidating the R4 digital '
    'structural-validation findings in researcher-facing form.',
    'All headline R4 findings and interpretation guardrails',
    'FINAL_R4_CONSOLIDATED_DATASET / FINAL_R4_DELIVERY_DATASET. Does NOT replace '
    'R4_STRUCTURAL_EXTRACTION.csv, which remains the immutable 1,404-record source.')
add('08_reports/R4_DIGITAL_VALIDATION_SUMMARY_FOR_DAVID.csv', D1, 'R4 delivery',
    'FINAL OUTPUT', 'AUTHORITATIVE_FINAL', HUMAN + ' with Claude assistance', CLAUDE, 'YES', 'YES',
    'FINAL', 'Compact aggregate metrics table for the R4 digital structural-validation round.',
    'All headline R4 findings', 'FINAL_R4_EXECUTIVE_SUMMARY_DATA')

D2 = '02_EXECUTIVE_REPORTS'
add('08_reports/R4_DIGITAL_VALIDATION_MEMO_FOR_DAVID.md', D2, 'R4 delivery', 'FINAL OUTPUT',
    'AUTHORITATIVE_FINAL', HUMAN + ' with Claude assistance', CLAUDE, 'YES', 'YES', 'FINAL',
    'Main researcher-facing memo: portability, parsimony, method, limitations.',
    'Portability; parsimony; counterpart/recipient; limitations')
add('08_reports/R4_EMAIL_TO_DAVID_DRAFT.md', D2, 'R4 delivery', 'FINAL OUTPUT',
    'AUTHORITATIVE_FINAL', HUMAN + ' with Claude assistance', CLAUDE, 'YES', 'YES', 'FINAL',
    'Concise cover email summarising the round.', 'Delivery communication')

D3 = '03_SOURCE_DATA_AND_CORPUS'
add('03_extraction/R4_STRUCTURAL_EXTRACTION.csv', D3, 'R4.2', 'SOURCE DATA',
    'AUTHORITATIVE_SOURCE', LUNA, LUNA, 'PARTIAL (QA sampled)', 'YES', 'SOURCE',
    'The immutable 1,404-record structural extraction. Unit: legal provision x actor x legal action.',
    'Every downstream R4 finding', 'IMMUTABLE. CORPUS_WIDE_REPAIR = NOT_EXECUTED.')
add('R4_DIGITAL_CORPUS_REGISTER.csv', D3, 'R4.1', 'SOURCE DATA', 'AUTHORITATIVE_SOURCE', HUMAN,
    DET, 'YES', 'YES', 'SOURCE', 'Register of the three digital instruments and their CELEX ids.',
    'Corpus definition')
add('R4_LEGAL_STRUCTURE_INDEX.csv', D3, 'R4.1', 'SOURCE DATA', 'AUTHORITATIVE_SOURCE', DET, DET,
    'YES', 'YES', 'SOURCE', 'Structural index of articles, recitals and annexes per instrument.',
    'Corpus structure counts')
add('R4_LEGAL_STRUCTURE_QC.csv', D3, 'R4.1', 'QA', 'SUPPORTING_EVIDENCE', DET, DET, 'YES', 'YES',
    'SUPPORTING', 'Quality control on the structural index.', 'Corpus integrity')
add('R4_LEGAL_TEXT_PROVENANCE.csv', D3, 'R4.1', 'PROVENANCE', 'AUTHORITATIVE_SOURCE', HUMAN, DET,
    'YES', 'YES', 'SOURCE', 'Provenance of each frozen legal text: source, retrieval, hash.',
    'Corpus authenticity')
add('R4_ARTICLE_INDEX.csv', D3, 'R4.1', 'SOURCE DATA', 'SUPPORTING_EVIDENCE', DET, DET, 'YES',
    'YES', 'SUPPORTING', 'Article-level index across the three instruments.', 'Corpus navigation')
add('R4_LEGAL_CORPUS_VALIDATION_REPORT.md', D3, 'R4.1', 'QA', 'SUPPORTING_EVIDENCE', HUMAN,
    'Human + deterministic checks', 'YES', 'YES', 'SUPPORTING',
    'Validation report confirming the corpus matches official EU sources.', 'Corpus authenticity')
add('R4_1_METHOD_NOTE.md', D3, 'R4.1', 'HUMAN EVIDENCE', 'SUPPORTING_EVIDENCE', HUMAN, 'n/a',
    'YES', 'YES', 'SUPPORTING', 'Method note for digital corpus construction.',
    'Corpus methodology')
for act in ['D1_GDPR', 'D2_DSA', 'D3_AI_ACT']:
    add(f'02_sources/{act}/metadata/{act}_metadata.json', f'{D3}/source_metadata', 'R4.1',
        'PROVENANCE', 'AUTHORITATIVE_SOURCE', DET, DET, 'YES', 'YES', 'SOURCE',
        f'Retrieval metadata for {act}.', 'Corpus authenticity')
    add(f'02_sources/{act}/validation/{act}_structural_validation.json',
        f'{D3}/source_metadata', 'R4.1', 'QA', 'SUPPORTING_EVIDENCE', DET, DET, 'YES', 'YES',
        'SUPPORTING', f'Structural validation output for {act}.', 'Corpus integrity')

D4 = '04_R4_2_STRUCTURAL_EXTRACTION'
for fn, desc, sup in [
    ('R4_2_METHOD_NOTE.md', 'Method note for the structural extraction stage.', 'Extraction method'),
    ('03_extraction/R4_2_AI_EXTRACTION_RUN_SUMMARY.csv', 'Run summary of the AI extraction pass.', 'Extraction provenance'),
    ('03_extraction/R4_2_SOURCE_COVERAGE_REPORT.csv', 'Coverage of the corpus by extracted records.', 'Extraction completeness'),
    ('03_extraction/R4_DIGITAL_ACTOR_CANDIDATE_REGISTER.csv', 'Candidate actors identified across the digital corpus.', 'Actor variable'),
    ('03_extraction/R4_LEGAL_ACTION_REGISTER.csv', 'Register of legal actions encountered.', 'Action variable'),
    ('03_extraction/R4_LEGAL_DEFINITION_REGISTER.csv', 'Legal definitions extracted from the instruments.', 'Definitional grounding'),
    ('03_extraction/R4_CROSS_REFERENCE_REGISTER.csv', 'Cross-references between provisions.', 'Provision linkage'),
    ('03_extraction/R4_STRUCTURAL_AMBIGUITY_LOG.csv', 'Log of structural ambiguities flagged at extraction.', 'Ambiguity metadata'),
    ('03_extraction/R4_2_HUMAN_QA_SAMPLE.csv', 'Initial human QA sample drawn from the extraction.', 'QA design'),
]:
    add(fn, D4, 'R4.2', 'MODEL OUTPUT' if fn.endswith('.csv') else 'HUMAN EVIDENCE',
        'SUPPORTING_EVIDENCE', LUNA if fn.endswith('.csv') else HUMAN,
        LUNA if fn.endswith('.csv') else 'n/a', 'PARTIAL', 'YES', 'SUPPORTING', desc, sup)

D5 = '05_QA_AND_HUMAN_ADJUDICATION'
QA = '03_extraction/qa/'
for fn, desc, sup, atype in [
    ('R4_2B_QA_REPORT.md', 'R4.2B QA report over the stratified sample.', 'QA design and findings', 'QA'),
    (QA + 'R4_2B_AMBIGUITY_TYPOLOGY.csv', 'Typology of ambiguity classes observed in QA.', 'Ambiguity typology', 'QA'),
    (QA + 'R4_2B_CONFIDENCE_CALIBRATION.csv', 'Calibration of extraction confidence against QA outcomes.', 'Confidence flag reliability', 'QA'),
    (QA + 'R4_2B_EXTRACTION_CORRECTION_REGISTER.csv', 'Corrections registered during R4.2B QA.', 'QA corrections', 'QA'),
    (QA + 'R4_2B_HUMAN_CALIBRATION_SEED_V1.csv', 'Seed set used to calibrate human QA.', 'QA calibration', 'HUMAN EVIDENCE'),
    (QA + 'R4_2B_HUMAN_DECISION_REGISTER.csv', 'Register of human QA decisions.', 'Human authority over QA', 'HUMAN EVIDENCE'),
    (QA + 'R4_2B_HUMAN_QA_SAMPLE.csv', 'The stratified human QA sample.', 'QA sampling design', 'QA'),
    (QA + 'R4_2B_HUMAN_REVIEW_SOURCE_MANIFEST.csv', 'Manifest of sources used in human review.', 'Review provenance', 'PROVENANCE'),
    (QA + 'R4_2B_LUNA_EXTRACTION_FREEZE_MANIFEST.csv', 'Freeze manifest for the Luna extraction output.', 'Extraction freeze', 'FREEZE/INTEGRITY'),
    (QA + 'R4_2B_QA_METRICS.csv', 'Quantitative QA metrics.', 'QA results', 'QA'),
    (QA + 'R4_2B_SYSTEMATIC_ERROR_AUDIT.csv', 'First systematic error audit.', 'Error patterns', 'QA'),
    (QA + 'R4_2B_SYSTEMATIC_ERROR_AUDIT_UPDATED.csv', 'Updated systematic error audit.', 'Error patterns', 'QA'),
    (QA + 'R4_2C_HISTORICAL_OUTPUT_PRESERVATION_MANIFEST.csv', 'Manifest preserving superseded R4.2C outputs.', 'Audit trail', 'FREEZE/INTEGRITY'),
    (QA + 'R4_2C_LUNA_SELFREVIEW_TERRA_COMPARISON.csv', 'Comparison of Luna self-review against Terra review.', 'Cross-model comparison', 'MODEL OUTPUT'),
    (QA + 'R4_2C_LUNA_TERRA_QA_COMPARISON.csv', 'Luna versus Terra QA comparison table.', 'Cross-model comparison', 'MODEL OUTPUT'),
    (QA + 'R4_2C_MODEL_PROVENANCE_CORRECTION.md', 'Record of an earlier model-provenance correction in R4.2C.', 'Provenance discipline', 'PROVENANCE'),
    (QA + 'R4_2C_OUTPUT_RECLASSIFICATION.csv', 'Reclassification of R4.2C outputs after provenance review.', 'Provenance discipline', 'PROVENANCE'),
    (QA + 'R4_2C_R_PATTERN_CONFIRMATION.csv', 'Confirmation of recurring patterns across models.', 'Cross-model support', 'MODEL OUTPUT'),
    (QA + 'R4_2C_R_TRUE_TERRA_CALIBRATION_REPORT.md', 'Calibration report for the true-Terra review.', 'Cross-model calibration', 'QA'),
    (QA + 'R4_2C_TARGETED_HUMAN_REVIEW_QUEUE.csv', 'Queue of cases routed to targeted human review.', 'Human routing', 'HUMAN EVIDENCE'),
    (QA + 'R4_2C_TARGETED_HUMAN_REVIEW_QUEUE_V2.csv', 'Second version of the targeted human review queue.', 'Human routing', 'HUMAN EVIDENCE'),
    (QA + 'R4_2C_TERRA_BLIND_INPUT_V2.csv', 'Blind input presented to Terra in R4.2C v2.', 'Blind review design', 'MODEL OUTPUT'),
    (QA + 'R4_2C_TERRA_CALIBRATED_REVIEW.csv', 'Terra calibrated review output.', 'Cross-model review', 'MODEL OUTPUT'),
    (QA + 'R4_2C_TERRA_CALIBRATION_AND_CLOSURE_REPORT.md', 'Closure report for the Terra calibration stage.', 'Cross-model closure', 'QA'),
    (QA + 'R4_2C_TERRA_INDEPENDENT_CALIBRATED_REVIEW_V2.csv', 'Independent Terra calibrated review, v2.', 'Cross-model review', 'MODEL OUTPUT'),
    (QA + 'R4_2C_TERRA_INDEPENDENT_REVIEW_V2_FREEZE_MANIFEST.csv', 'Freeze manifest for the v2 Terra review.', 'Review freeze', 'FREEZE/INTEGRITY'),
    (QA + 'R4_STRUCTURAL_EXTRACTION_QA_CALIBRATED.csv', 'Extraction with calibrated QA annotations.', 'QA-annotated extraction', 'QA'),
    (QA + 'R4_2_FINAL_CHECKPOINT.md', 'Checkpoint closing the R4.2 QA stage.', 'Stage closure', 'HUMAN EVIDENCE'),
]:
    prov = TERRA if 'TERRA' in fn.upper() else (LUNA if 'LUNA' in fn.upper() else 'Mixed; see R4_AI_EXECUTION_LOG.csv')
    if atype == 'HUMAN EVIDENCE':
        prov = 'n/a (human decision record)'
    add(fn, D5, 'R4.2B / R4.2C', atype, 'SUPPORTING_EVIDENCE',
        HUMAN if atype == 'HUMAN EVIDENCE' else 'AI-assisted, human-supervised',
        prov, 'YES' if atype == 'HUMAN EVIDENCE' else 'PARTIAL', 'YES', 'SUPPORTING', desc, sup)

for fn, desc, sup in [
    ('r4_2c/R4_2C_LUNA_TERRA_QA_COMPARISON.csv', 'Working-copy variant of the Luna/Terra comparison (differs from the qa/ root version).', 'Cross-model comparison'),
    ('r4_2c/R4_2C_TARGETED_HUMAN_REVIEW_QUEUE.csv', 'Working-copy variant of the targeted review queue.', 'Human routing'),
    ('r4_2c/R4_2C_TERRA_CALIBRATED_REVIEW.csv', 'Working-copy variant of the Terra calibrated review.', 'Cross-model review'),
    ('r4_2c/R4_2C_TERRA_CALIBRATION_AND_CLOSURE_REPORT.md', 'Working-copy variant of the calibration closure report.', 'Cross-model closure'),
    ('r4_2c/R4_2_FINAL_CHECKPOINT.md', 'Working-copy variant of the R4.2 checkpoint.', 'Stage closure'),
    ('r4_2c/R4_STRUCTURAL_EXTRACTION_QA_CALIBRATED.csv', 'Working-copy variant of the calibrated extraction.', 'QA-annotated extraction'),
]:
    add(QA + fn, f'{D5}/r4_2c_working_copies', 'R4.2C', 'MODEL OUTPUT', 'SUPPORTING_EVIDENCE',
        'AI-assisted, human-supervised', TERRA, 'PARTIAL', 'YES', 'SUPPORTING', desc, sup,
        'Byte-differs from the same-named file in the qa/ root; both preserved.')

RP = '03_extraction/qa/repair/'
for fn, desc, sup, atype in [
    (RP + 'R4_2D_CROSS_MODEL_DIAGNOSTIC_SAMPLE.csv', 'The 12 purposively selected cross-model-supported diagnostic cases.', 'Human diagnostic design', 'QA'),
    (RP + 'R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv', 'Completed human adjudication of all 12 diagnostic cases.', 'Human root-cause findings', 'HUMAN EVIDENCE'),
    (RP + 'R4_2D_HUMAN_DIAGNOSTIC_SUMMARY.csv', 'Summary of the human diagnostic outcomes.', 'Human diagnostic results', 'HUMAN EVIDENCE'),
    (RP + 'R4_2D_HUMAN_DIAGNOSTIC_REPORT.md', 'Narrative report of the human diagnostic.', 'Human root-cause findings', 'HUMAN EVIDENCE'),
    (RP + 'R4_2D_HUMAN_DIAGNOSTIC_RULE_CANDIDATES.md', 'The 15 human-derived candidate structural rules.', '15 frozen rules', 'HUMAN EVIDENCE'),
    (RP + 'README_R4_2D_HUMAN_DIAGNOSTIC.md', 'Explanatory readme for the human diagnostic stage.', 'Human diagnostic method', 'HUMAN EVIDENCE'),
    (RP + 'R4_2D_HUMAN_DIAGNOSTIC_PANEL.html', 'Offline adjudication panel used by the human researcher.', 'Human adjudication instrument', 'HUMAN EVIDENCE'),
]:
    add(fn, f'{D5}/R4_2D_human_diagnostic', 'R4.2D', atype, 'SUPPORTING_EVIDENCE', HUMAN,
        'n/a (human adjudication)', 'YES', 'YES', 'SUPPORTING', desc, sup)
for fn, desc in [
    ('R4_2B_HUMAN_REVIEW_PANEL.html', 'Offline human review panel used in R4.2B.'),
    ('R4_2B_HUMAN_REVIEW_WORKING.csv', 'Working file behind the R4.2B human review.'),
    ('README_HUMAN_REVIEW.md', 'Readme for the human review interface.'),
]:
    add(f'{QA}human_review/{fn}', f'{D5}/human_review_interface', 'R4.2B', 'HUMAN EVIDENCE',
        'SUPPORTING_EVIDENCE', HUMAN, 'n/a (human decision record)', 'YES', 'YES', 'SUPPORTING',
        desc, 'Human authority over QA')

D6 = '06_REPAIR_TRIAGE_AND_COMPRESSION'
for fn, desc, sup in [
    ('R4_2E_A_METHOD_REPORT.md', 'Method report for deterministic candidate triage over all 1,404 records.', 'Triage method'),
    ('R4_2E_A_REPAIR_CANDIDATE_REGISTER.csv', 'Per-record triage classification (YES 713 / UNCERTAIN 346 / NO 345).', 'Candidate signals'),
    ('R4_2E_A_REPAIR_CANDIDATE_SUMMARY.csv', 'Aggregate triage counts and complexity distribution.', 'Triage results'),
    ('R4_2E_A_HUMAN_CASE_RULE_REDISCOVERY.csv', 'Which of the 12 human cases the heuristic rediscovered (9/12).', 'Heuristic blind spots'),
    ('R4_2E_A_ACTOR_ACTION_REPAIR_AUDIT.csv', 'Audit of actor/action fragmentation candidates.', 'Actor/action defects'),
    ('R4_2E_A_COUNTERPART_RECIPIENT_BURDEN_AUDIT.csv', 'Audit of the counterpart/recipient coding burden.', 'Counterpart/recipient finding'),
    ('R4_2E_A_NEW_RULE_CANDIDATES.csv', 'New rule candidates raised during triage.', 'Rule evolution'),
]:
    add(f'{RP}R4_2E_A/{fn}', f'{D6}/R4_2E_A_triage', 'R4.2E-A', 'MODEL OUTPUT' if fn.endswith('.csv') else 'QA',
        'SUPPORTING_EVIDENCE', DET, DET, 'PARTIAL', 'YES', 'SUPPORTING', desc, sup,
        'Deterministic heuristic; candidate signals, not confirmed defects.')
for fn, desc, sup in [
    ('R4_2E_B0_METHOD_REPORT.md', 'Method report for repair-family compression.', 'Compression method'),
    ('R4_2E_B0_FREEZE_RECORD.md', 'Freeze record for the B0 compression stage.', 'Stage freeze'),
    ('R4_2E_B0_COMPRESSION_SUMMARY.csv', 'Compression metrics: 211 families; advanced workload 524 to 131.', 'Compression results'),
    ('R4_2E_B0_REPAIR_FAMILY_REGISTER.csv', 'The 211 repair families with sizes and routes.', 'Family definitions and coverage'),
    ('R4_2E_B0_REPAIR_SIGNATURE_REGISTER.csv', 'Per-record structural signature and assigned repair route.', 'Route assignment'),
    ('R4_2E_B0_MODEL_REPRESENTATIVE_SAMPLE.csv', 'Representatives selected for advanced review.', 'Representative selection'),
    ('R4_2E_B0_RELATIONAL_FIELD_STRATEGY.md', 'Frozen strategy for evaluating counterpart and recipient separately.', 'Counterpart/recipient method'),
    ('R4_2E_B0_HEURISTIC_BLIND_SPOTS.md', 'Documented blind spots of the triage heuristic.', 'Known limitations'),
    ('R4_2E_B0_OBJECT_TRIGGER_TYPOLOGY.csv', 'Typology of object-field residual-bucket triggers.', 'Object variable defects'),
    ('R4_2E_B0_NEW_DETECTION_RULE_CANDIDATES.csv', 'New detection rule candidates from B0.', 'Rule evolution'),
]:
    add(f'{RP}R4_2E_B0/{fn}', f'{D6}/R4_2E_B0_compression', 'R4.2E-B0',
        'MODEL OUTPUT' if fn.endswith('.csv') else 'QA', 'SUPPORTING_EVIDENCE', DET, DET,
        'PARTIAL', 'YES', 'SUPPORTING', desc, sup)

D7 = '07_ADVANCED_VALIDATION_B1'
B1 = RP + 'R4_2E_B1/'
for fn, dest, desc, sup, prov, note in [
    ('R4_2E_B1_ADVANCED_VALIDATION.csv', 'batch_outputs', 'B1-01 authoritative output, 36 cases.', 'B1 results', TERRA, 'Authoritative v2.'),
    ('R4_2E_B1_ADVANCED_VALIDATION_B1_02.csv', 'batch_outputs', 'B1-02 authoritative output, 36 cases.', 'B1 results', TERRA, ''),
    ('R4_2E_B1_ADVANCED_VALIDATION_B1_03.csv', 'batch_outputs', 'B1-03 authoritative output, 36 cases.', 'B1 results', TERRA, ''),
    ('R4_2E_B1_ADVANCED_VALIDATION_B1_04.csv', 'batch_outputs', 'B1-04 authoritative output, 35 cases.', 'B1 results', CLAUDE, 'Provenance-corrected authoritative version.'),
    ('R4_2E_B1_BATCH_01_FREEZE_RECORD.md', 'freeze_records', 'B1-01 freeze record.', 'Batch freeze', TERRA, ''),
    ('R4_2E_B1_BATCH_02_FREEZE_RECORD.md', 'freeze_records', 'B1-02 freeze record.', 'Batch freeze', TERRA, ''),
    ('R4_2E_B1_BATCH_03_FREEZE_RECORD.md', 'freeze_records', 'B1-03 freeze record.', 'Batch freeze', TERRA, ''),
    ('R4_2E_B1_BATCH_04_FREEZE_RECORD.md', 'freeze_records', 'B1-04 freeze record, with corrected provenance and recorded design limitations.', 'Batch freeze; blinding limitation', CLAUDE, ''),
    ('R4_2E_B1_BATCH_ALLOCATION_FREEZE.md', 'design', 'Frozen allocation of the 143 cases into four batches.', 'B1 design', DET, ''),
    ('R4_2E_B1_BATCH_MANIFEST.csv', 'design', 'Case-level batch manifest.', 'B1 design', DET, ''),
    ('R4_2E_B1_BLIND_SUBSTANTIVE_REVIEW_INPUT.csv', 'design', 'The exact input shown to reviewers for all 143 cases.', 'Review input; schema under-exposure finding', DET, 'Exposes LEGAL_ACTION only; see the sensitivity audit.'),
    ('R4_2E_B1_NO_REPAIR_CONTROL_SAMPLE.csv', 'diagnostic_controls', 'The 12 NO_REPAIR diagnostic controls as selected before review.', 'Control design', DET, 'Lists all 12 with no batch column; this is why blinding was not guaranteed.'),
    ('R4_2E_B1_NO_REPAIR_CONTROL_RESULTS.csv', 'diagnostic_controls', 'B1-01 control results.', 'Control diagnostic', TERRA, ''),
    ('R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_02.csv', 'diagnostic_controls', 'B1-02 control results.', 'Control diagnostic', TERRA, ''),
    ('R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_03.csv', 'diagnostic_controls', 'B1-03 control results.', 'Control diagnostic', TERRA, ''),
    ('R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_04.csv', 'diagnostic_controls', 'B1-04 control results.', 'Control diagnostic', CLAUDE, ''),
    ('R4_2E_B1_CONTROL_DIAGNOSTIC_CONSOLIDATED.csv', 'diagnostic_controls', 'All 12 controls consolidated with type and severity.', 'B0 compression safety', MIXED_TC, ''),
    ('R4_2E_B1_FINAL_SUMMARY.csv', 'combined_reports', 'Consolidated metrics across all 143 cases.', 'All combined B1 findings', MIXED_TC, ''),
    ('R4_2E_B1_METHOD_REPORT.md', 'combined_reports', 'Full B1 method report including the sensitivity audit and B0 decision.', 'All B1 findings', MIXED_TC, ''),
    ('R4_2E_B1_NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATES.csv', 'combined_reports', 'Seven new structural diagnostic candidates recorded for adjudication.', 'Rule evolution', CLAUDE, 'The 15 frozen rules were not modified.'),
    ('R4_2E_B1_RELATIONAL_FIELD_DIFFERENTIATION.csv', 'combined_reports', 'Relational differentiation detail from B1-01.', 'Counterpart/recipient finding', TERRA, ''),
    ('R4_2E_B1_FAMILY_TEMPLATE_VALIDATION.csv', 'combined_reports', 'Family template validation detail from B1-01.', 'Template status', TERRA, ''),
    ('R4_2E_B1_INDIVIDUAL_CASE_DECISIONS.csv', 'combined_reports', 'Individual advanced case routing from B1-01.', 'Individual routes', TERRA, ''),
    ('R4_2E_B1_BATCH_RUN_LOG.csv', 'combined_reports', 'Run log for all four batches with input/output hashes and provenance.', 'Execution provenance', MIXED_TC, ''),
    ('R4_2E_B1_HANDOFF_STATE.md', 'combined_reports', 'Final B1 handoff state and unresolved questions.', 'Current status', MIXED_TC, ''),
]:
    add(B1 + fn, f'{D7}/{dest}', 'R4.2E-B1', 'MODEL OUTPUT' if fn.endswith('.csv') else 'FREEZE/INTEGRITY',
        'AUTHORITATIVE_SOURCE' if 'ADVANCED_VALIDATION' in fn else 'SUPPORTING_EVIDENCE',
        'AI-assisted, human-supervised', prov, 'PARTIAL', 'YES', 'SUPPORTING', desc, sup, note)

D8 = '08_ACTION_SENSITIVITY_AUDIT'
add(B1 + 'R4_2E_B1_ACTION_SENSITIVITY_AUDIT.csv', D8, 'R4.2E-B1S', 'MODEL OUTPUT',
    'AUTHORITATIVE_SOURCE', 'AI-assisted, human-supervised', CLAUDE, 'PARTIAL', 'YES', 'SUPPORTING',
    'Per-case re-examination of all 143 Action judgments against LEGAL_ACTION + LEGAL_VERB + MODALITY.',
    'Action 87 vs 63; 26 changed; 1/143 material')
add(B1 + 'R4_2E_B1_ACTION_SENSITIVITY_SUMMARY.csv', D8, 'R4.2E-B1S', 'MODEL OUTPUT',
    'AUTHORITATIVE_SOURCE', 'AI-assisted, human-supervised', CLAUDE, 'PARTIAL', 'YES', 'SUPPORTING',
    'Aggregate metrics for the sensitivity audit, reporting frozen and adjusted counts side by side.',
    'Action sensitivity result')
add('08_reports/R4_VARIABLE_REDUNDANCY_AUDIT.csv', D8, 'R4.2E-B1S', 'MODEL OUTPUT',
    'AUTHORITATIVE_SOURCE', DET + ' with interpretation', CLAUDE, 'PARTIAL', 'YES', 'SUPPORTING',
    'Five variable pairs with recomputed overlap, exactness, direction and parsimony status.',
    'Variable parsimony findings')

D9 = '09_MODEL_PROVENANCE'
for fn, desc, sup in [
    ('R4_AI_EXECUTION_LOG.csv', 'Log of every AI execution across R4 with model and purpose.', 'Model provenance'),
    ('R4_MODEL_ESCALATION_LOG.csv', 'Record of model escalations and changes during R4.', 'Model provenance'),
    ('09_logs/R4_SESSION_CHECKPOINT_2026-09-26.md', 'Session checkpoint preceding the final rounds.', 'Execution continuity'),
    ('09_logs/R4_GIT_SYNC_LOG.md', 'Log of repository synchronisation events.', 'Version provenance'),
]:
    add(fn, D9, 'R4 (all stages)', 'PROVENANCE', 'SUPPORTING_EVIDENCE', HUMAN, 'Mixed; see file',
        'YES', 'YES', 'SUPPORTING', desc, sup)

D10 = '10_FREEZE_AND_INTEGRITY'
for fn, desc, sup in [
    ('08_reports/R4_DIGITAL_STRUCTURAL_VALIDATION_FREEZE_RECORD.md', 'Final freeze record for the whole R4 digital structural-validation round.', 'Final status and all findings'),
    ('08_reports/R4_DIGITAL_STRUCTURAL_VALIDATION_MANIFEST.csv', 'SHA-256 manifest of the 24 final scientific artifacts.', 'Integrity verification'),
    ('R4_BASELINE_FREEZE_RECORD.md', 'Freeze record for the R4 baseline (R3 reconciliation).', 'Baseline integrity'),
    ('R4_PRE_R4_2_CHECKPOINT.md', 'Checkpoint immediately before structural extraction.', 'Stage boundary'),
]:
    add(fn, D10, 'R4 (freeze)', 'FREEZE/INTEGRITY', 'AUTHORITATIVE_FINAL', HUMAN,
        'Mixed; see file', 'YES', 'YES',
        'FINAL' if 'DIGITAL_STRUCTURAL' in fn else 'SUPPORTING', desc, sup)
SUP = f'{D10}/superseded_preserved'
for fn, desc, why in [
    (B1 + 'R4_2E_B1_ADVANCED_VALIDATION_B1_01_v1_SCHEMA_DEFECT.csv',
     'First B1-01 export, malformed by separators inside note fields.',
     'Preserved because it documents the CSV schema incident that led to library-based CSV writing.'),
    (B1 + 'R4_2E_B1_FAMILY_TEMPLATE_VALIDATION_B1_01_v1_SCHEMA_DEFECT.csv',
     'Companion malformed B1-01 template export.', 'Same schema incident.'),
    (B1 + 'R4_2E_B1_INDIVIDUAL_CASE_DECISIONS_B1_01_v1_SCHEMA_DEFECT.csv',
     'Companion malformed B1-01 individual-case export.', 'Same schema incident.'),
    (B1 + 'R4_2E_B1_ADVANCED_VALIDATION_B1_04_v1_PROVENANCE_SUPERSEDED.csv',
     'B1-04 export before the Claude provenance correction.',
     'Preserved as part of the recorded provenance-correction chain. Substantive cells are identical to the authoritative version.'),
    (B1 + 'R4_2E_B1_ACTION_SENSITIVITY_AUDIT_v1_PROVENANCE_SUPERSEDED.csv',
     'Sensitivity audit before the Claude provenance correction.',
     'Same provenance-correction chain. Substantive cells identical to the authoritative version.'),
]:
    add(fn, SUP, 'R4.2E-B1 / B1S', 'SUPPORTING ARCHIVE', 'SUPERSEDED_PRESERVED',
        'AI-assisted, human-supervised', 'See authoritative counterpart', 'PARTIAL', 'YES',
        'SUPPORTING', desc, 'Audit trail',
        'NOT AUTHORITATIVE - PRESERVED FOR AUDIT TRAIL. ' + why)

D11 = '11_REPRODUCIBILITY'
for fn, desc in [
    ('build_r4_1_structural_corpus.ps1', 'Builds the frozen digital corpus and structural index.'),
    ('build_r4_2_structural_extraction.ps1', 'Produces the 1,404-record structural extraction.'),
    ('build_r4_2_history_inventory.ps1', 'Inventories the R3 history brought into R4.'),
    ('build_r4_2b_qa_package.ps1', 'Builds the R4.2B QA package and metrics.'),
    ('build_r4_2b_human_review_interface.ps1', 'Generates the offline human review panel.'),
    ('build_r4_2c_calibrated_qa.ps1', 'Builds the R4.2C calibrated QA comparison.'),
    ('build_r4_2cr_true_terra_review.ps1', 'Builds the independent true-Terra review inputs.'),
    ('build_r4_2d_human_diagnostic_panel.ps1', 'Generates the human diagnostic adjudication panel.'),
    ('build_r4_2d_human_diagnostic_completed.ps1', 'Assembles the completed human diagnostic record.'),
    ('build_r4_2e_a_repair_candidate_identification.ps1', 'Runs deterministic triage over all 1,404 records.'),
    ('build_r4_2e_b0_repair_strategy_compression.ps1', 'Builds the 211 repair families and routes.'),
    ('build_r4_2e_b1_batch_allocation.ps1', 'Allocates the 143 cases into four batches.'),
    ('build_r4_2e_b1_batch01_validation.ps1', 'Writes the B1-01 validation output.'),
    ('close_r4_2e_b1_batch01.ps1', 'Closes and freezes B1-01.'),
    ('build_r4_2e_b1_batch02_validation.ps1', 'Writes the B1-02 validation output.'),
    ('build_r4_2e_b1_batch03_validation.ps1', 'Writes the B1-03 validation output.'),
    ('build_r4_2e_b1_batch03_control_results.ps1', 'Unblinds and records the B1-03 diagnostic controls.'),
    ('build_r4_2e_b1_batch04_validation.py', 'Writes the B1-04 validation output with schema gates.'),
    ('build_r4_2e_b1_batch04_control_results.py', 'Unblinds and records the B1-04 diagnostic controls.'),
    ('build_r4_2e_b1_final_consolidation.py', 'Reconciles all 143 cases and the 12 controls.'),
    ('build_r4_2e_b1_new_diagnostic_candidates.py', 'Records the new structural diagnostic candidates.'),
    ('build_r4_2e_b1s_action_sensitivity_audit.py', 'Runs the Action representation sensitivity audit.'),
    ('build_r4_variable_redundancy_audit.py', 'Recomputes the five variable-pair redundancy findings.'),
    ('build_r4_david_summary.py', 'Builds the David-facing summary table.'),
    ('build_r4_final_manifest.py', 'Builds the SHA-256 manifest of final artifacts.'),
    ('apply_r4_claude_provenance_correction.py', 'Applies the Claude provenance correction with byte verification.'),
    ('build_envio_r4_to_david_package.py', 'Builds this delivery package.'),
]:
    add(f'09_logs/{fn}', D11, 'R4 (tooling)', 'REPRODUCIBILITY', 'REPRODUCIBILITY_SUPPORT', HUMAN,
        DET, 'YES', 'NO', 'SUPPORTING', desc, 'Reproducibility')

D12 = '12_ARCHIVE_SUPPORT'
for fn, desc, sup in [
    ('R4_INITIAL_METHOD_NOTE.md', 'Initial R4 method note setting out the research question.', 'R4 design'),
    ('R4_R3_BASELINE_MANIFEST.md', 'Manifest of the frozen R3 green baseline.', 'Green baseline'),
    ('R4_R3_HISTORICAL_INTEGRATION_REPORT.md', 'Report on integrating R3 history into R4.', 'Baseline continuity'),
    ('R4_R3_RECONCILIATION.csv', 'Reconciliation of R3 totals brought into R4.', 'Green baseline totals'),
    ('R4_R3_TO_R4_INTEGRATION_MAP.csv', 'Mapping from R3 artifacts to R4 structures.', 'Baseline continuity'),
    ('R4_R3_HISTORY_FILE_INVENTORY.csv', 'Inventory of archived R3 history files.', 'Archive completeness'),
    ('R4_R3_HISTORY_ARCHIVE_METADATA.json', 'Metadata for the R3 history archive.', 'Archive provenance'),
    ('R4_PREEXISTING_R4_2_CHANGE_AUDIT.csv', 'Audit of pre-existing changes before R4.2 began.', 'Change control'),
    ('00_protocol/R4_WORKSPACE_STRUCTURE.md', 'Definition of the R4 workspace structure.', 'Project organisation'),
    ('00_protocol/R4_INITIAL_SETUP_PROMPT_VERBATIM.txt', 'Verbatim initial setup instruction for R4.', 'AI-use transparency'),
    ('00_protocol/PROTOCOLO_USO_IA_R1_R3_PRE_R4_v1_1.docx', 'Researcher protocol governing AI use across R1 to R3.', 'AI-use governance'),
]:
    add(fn, D12, 'R4.0 / protocol', 'SUPPORTING ARCHIVE', 'SUPPORTING_EVIDENCE', HUMAN,
        'n/a', 'YES', 'YES', 'SUPPORTING', desc, sup)


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest().upper()


def main():
    copied, failures, missing = [], [], []
    for item in F:
        if item['src'].startswith('ABS::'):
            src = item['src'][5:]
        else:
            src = os.path.join(R4, item['src'].replace('/', os.sep))
        if not os.path.exists(src):
            missing.append(item['src'])
            continue
        ddir = os.path.join(PKG, item['dest'].replace('/', os.sep))
        os.makedirs(ddir, exist_ok=True)
        dst = os.path.join(ddir, os.path.basename(src))
        if os.path.exists(dst):
            failures.append((item['src'], 'DESTINATION_COLLISION'))
            continue
        shutil.copy2(src, dst)
        hs, hd = sha(src), sha(dst)
        if hs != hd:
            os.remove(dst)
            failures.append((item['src'], 'COPY_INTEGRITY_FAILURE'))
            continue
        item['sha'] = hd
        item['bytes'] = os.path.getsize(dst)
        item['pkg_path'] = os.path.relpath(dst, PKG).replace(os.sep, '/')
        item['orig_path'] = (item['src'][5:].replace(os.sep, '/')
                             if item['src'].startswith('ABS::')
                             else 'R4_CROSS_DOMAIN_VALIDATION/' + item['src'])
        copied.append(item)

    with open(os.path.join(PKG, '00_START_HERE', 'R4_TRACEABILITY_MAP.csv'), 'w',
              encoding='utf-8', newline='') as fh:
        cols = ['PACKAGE_PATH', 'ORIGINAL_PATH', 'FILE_NAME', 'PHASE', 'ARTIFACT_TYPE',
                'EVIDENCE_LEVEL', 'CREATED_BY', 'MODEL_PROVENANCE', 'HUMAN_VALIDATED', 'FROZEN',
                'FINAL_OR_SUPPORTING', 'PURPOSE', 'SUPPORTS_FINDING', 'SHA256', 'NOTES']
        w = csv.writer(fh, quoting=csv.QUOTE_ALL, lineterminator='\r\n')
        w.writerow(cols)
        for i in copied:
            w.writerow([i['pkg_path'], i['orig_path'], os.path.basename(i['pkg_path']), i['phase'],
                        i['atype'], i['elevel'], i['by'], i['prov'], i['hv'], i['frozen'],
                        i['fos'], i['purpose'], i['supports'], i['sha'], i['notes']])

    print(f'copied  : {len(copied)}')
    print(f'missing : {len(missing)}')
    for m in missing:
        print('   MISSING:', m)
    print(f'failures: {len(failures)}')
    for f_, why in failures:
        print(f'   {why}: {f_}')
    return copied


if __name__ == '__main__':
    os.makedirs(os.path.join(PKG, '00_START_HERE'), exist_ok=True)
    main()
