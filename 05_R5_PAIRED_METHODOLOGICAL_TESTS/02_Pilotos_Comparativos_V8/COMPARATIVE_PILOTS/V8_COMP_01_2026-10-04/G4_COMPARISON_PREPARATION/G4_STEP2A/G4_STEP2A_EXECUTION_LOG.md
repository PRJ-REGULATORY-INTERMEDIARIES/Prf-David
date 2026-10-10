# G4 Step 2A execution log — recovery completion

**Date:** 2026-10-05  
**Recovery class:** `REC-B — STEP2A_PARTIAL_RECOVERABLE`  
**Final state:** `G4_STEP2A_FROZEN / COMPARATIVE_SCORING_NOT_STARTED`

## Recovery and inputs

The power-loss audit found the Step 2A outputs in the preparation directory root, not in the required `G4_STEP2A/` subdirectory. The prior Step 2A freeze manifest and its self-hash were internally valid, and all 34 file-valued manifest entries matched. The required `G4_STEP2A_EXECUTION_LOG.md` was absent and omitted from that manifest. The prior gate's frozen label was therefore incomplete as a required deliverable set.

Before completing the stage, all 11 existing `G4_STEP2A_*` files were copied byte-for-byte to `RECOVERY_2026-10-05/STEP2A_PRE_RECOVERY/`. The original root files remain unchanged. Their original and recovery-copy hashes are recorded in the recovery inventory and manifest.

Controlling inputs used for recovery validation:

- Frozen normalized claims: `../G4_STEP1_NORMALIZED_CLAIMS.csv`.
- Eligibility/scope: `../G4_STEP1_ELIGIBILITY_REGISTER.csv` and `../G4_STEP0_EVIDENCE_CLASSIFICATION.csv`.
- Matching rulebook: `../G4_CLAIM_MATCHING_RULES.md`.
- Frozen source boundary: `../G4_EVIDENCE_SCOPE_DICTIONARY.md` and `../FOUR_CELL_FINAL_INTEGRITY_MANIFEST.csv`.
- Common legal evidence: `../COMMON_STATEMENT_REGISTER.csv`.

No Codex or Claude experimental cell was rerun. Existing correspondence files were adopted only after the independent coverage, scope, membership, and disposition checks documented in the recovery QA supplement.

## Step 2A documentary result

- 26 candidate correspondence groups: 16 relation, 6 configuration, 2 positional, 2 architecture-level decisions.
- 112 original analytical units: 101 placed in groups and 11 unmatched; all 112 retain explicit dispositions.
- Original units grouped/unmatched: Codex A 24/0; Codex B 27/2; Claude A 24/4; Claude B 26/5.
- Two `STEP0_DERIVED` cores remain attached derived constructs and are excluded from the original-claim population.
- 115 mapping rows represent memberships and dispositions, not 115 unique claims. All 114 unique Step 1 units (112 original plus 2 derived) are represented. The one-to-many membership for `S1-098` is preserved and counts as one underlying unit.
- The five material external dependencies (`R-P03-04`, `CL-P03-02`, `CL-P03-03`, `R-P04-05`, `CL-P04-02`) remain scope-flagged. The two borderline SC-B units (`CL-P04-04`, `CL-P04-07`) remain provisional.
- Three correspondence groups carry mixed evidence-scope classes: CG-018, CG-019, CG-022. These are candidate documentary correspondences only.
- No outcome category, agreement score, legal-validity decision, improvement, regression, or superiority label was assigned.

## Recovery actions

1. Checked all manifest source and target hashes; found no unexplained mismatch.
2. Checked unit coverage, original/derived status, group and unmatched references, scope/eligibility inheritance, group case/level discipline, review-field vacancy, and candidate-label hygiene.
3. Copied the eight existing required Step 2A outputs and sealed identity key into this required subdirectory without changing their contents.
4. Added this execution log and appended a recovery-specific QA section and gate addendum to the newly assembled subdirectory copies. The original root copies and original Step 2A freeze pair remain preserved.
5. Created a final Step 2A freeze manifest and SHA-256 file covering the required outputs and controlling references.

## Git and stopping status

Branch `main`; HEAD `ae1af320b1f952a0e2fdd0d2142caf5d3886db46`; tracked modifications were zero at the recovery audit. The 26 untracked status entries were recorded. No merge/rebase/lock marker existed. No Git operation was performed.

Step 2A is now frozen. Comparative scoring remains unstarted pending the human-adjudication gate.
