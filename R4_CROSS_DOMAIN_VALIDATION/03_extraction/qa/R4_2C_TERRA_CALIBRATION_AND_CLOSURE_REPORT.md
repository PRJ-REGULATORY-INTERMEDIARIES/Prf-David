# R4.2C — Terra calibration, QA and closure report

## 1. Objective

The operation tested whether the Luna structural extraction faithfully represents the frozen legal text, using three researcher decisions as a calibration seed and a blind calibrated review of the remaining 87 records. No R/I/T or mechanism coding was performed.

## 2. Human calibration seed

The immutable export contains three reviewed records: QA2B-001, QA2B-002 and QA2B-003, all GDPR, reviewer Igor Caires Machado. The seed is registered as HUMAN_CALIBRATION_SEED_V1.

## 3. Human-seed limitations

SEED_SIZE=3, SEED_DOMAIN=GDPR, SEED_CONFIDENCE_PROFILE=HIGH. The seed is small and not domain-balanced. It calibrates decision criteria, not universal legal patterns, and is not an independent full-sample human accuracy estimate.

## 4. Terra blind-review design

Terra review covered 87 records. First-pass judgments were based on full frozen source text, source pointer and Luna extraction fields. Luna confidence, ambiguity metadata, sampling stratum and prior QA interpretation were rejoined only after the decision record was produced.

## 5. Model provenance

Requested model: GPT-5.6 Terra High.

Observable runtime provenance: MODEL_VARIANT_NOT_EXPOSED. No model identity was fabricated. ROTEM_CODING_CONSULTED=NO.

## 6. Results across 87 records

- Records reviewed: 87
- Fully correct under this calibrated QA: 18
- Records with any recorded extraction, role-slot or excerpt error: 69
- Terra abstentions: 45
- Human-review recommendations: 74
- Confidence distribution: HIGH=10; LOW=45; MEDIUM=32
- Error distribution: COUNTERPART_EXTRACTION_ERROR=51; RECIPIENT_EXTRACTION_ERROR=48; OBJECT_EXTRACTION_ERROR=25; ACTOR_EXTRACTION_ERROR=20; SOURCE_EXCERPT_ERROR=18; ACTION_EXTRACTION_ERROR=16; AMBIGUITY_FALSE_POSITIVE=3; AMBIGUITY_FALSE_NEGATIVE=2; OVER_EXTRACTION=1
- Act distribution: D1_GDPR=27; D2_DSA=30; D3_AI_ACT=30
- Source-type distribution: ANNEX=3; OPERATIVE_ARTICLE=54; RECITAL=30

## 7. Error taxonomy

Field error counts: actor=20; action=16; object=25; counterpart=51; recipient=48; source pointer=0; excerpt=18. Display truncation was treated separately from semantic extraction failure where the pointer and full text resolved.

## 8. Luna confidence calibration

The original LOW confidence stratum was enriched for abstentions and residual review. This is evidence of sensitivity, not a calibrated accuracy estimate. The original confidence field was not allowed to alter Terra decisions.

## 9. Ambiguity calibration

Several original LOW/YES flags were supported by genuinely complex provisions, while a smaller set were conservative false positives. The 1,002 ambiguity flags cannot be treated as uniformly substantive without corpus-wide follow-up.

## 10. Structural-field performance

Actor/action segmentation was materially weaker in clause-fragment cases. Counterpart and recipient slots showed repeated duplication of contextual prepositional phrases, including across all three acts. This pattern is the principal residual risk for downstream relational coding.

## 11. Systematic defects

Terra evidence indicates a potential critical recurring defect in role-slot assignment and actor/action segmentation. Counts are recorded in R4_2B_SYSTEMATIC_ERROR_AUDIT_UPDATED.csv. The complete 1,404-row corpus was not silently repaired.

## 12. Residual review queue

The targeted queue contains 83 records, including all abstentions, LOW-confidence cases, error cases, and nine future audit-success cases (three per act where available). Residual uncertainty is explicit and remains open.

## 13. Limitations

The review is human-calibrated AI adjudication, not full human review and not conventional inter-coder reliability. Actual Terra model variant was not exposed. The seed is domain-unbalanced. Terra corrections were not propagated to unsampled rows.

## 14. Implications for AI division of labor

The current experiment is consistent with the hypothesis that Luna can perform broad structural extraction, Terra can provide calibrated quality control, and humans can calibrate criteria and adjudicate difficult residuals. It does not validate that workflow beyond this experiment.

## 15. R4.2 closure decision

Final status: R4_2_STRUCTURAL_QA_REQUIRES_REPAIR.

Closure is blocked because recurring role-slot overassignment and fragmented actor/action segmentation appear across independent provisions and acts, with a plausible effect on downstream relational coding. This is a repair-audit requirement, not a silent dataset correction.

## 16. Readiness for R4.3

Not ready. Do not begin R4.3 until the systematic-defect audit and any authorized repair are completed. The original Luna extraction remains immutable.

Mandatory boundaries: no regulator/intermediary/target assignment; no R/I/T coding; no mechanism coding; no Rotem comparison.
