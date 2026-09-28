# 11 — Reproducibility

The scripts that generated the R4 artifacts, in stage order. PowerShell scripts were used in the
earlier stages and under Codex; Python from B1-04 onward.

## What each script reproduces

| Script | Reproduces |
| --- | --- |
| `build_r4_1_structural_corpus.ps1` | The frozen digital corpus and structural index |
| `build_r4_2_structural_extraction.ps1` | The 1,404-record structural extraction |
| `build_r4_2_history_inventory.ps1` | The inventory of R3 history carried into R4 |
| `build_r4_2b_qa_package.ps1` | The R4.2B QA package and metrics |
| `build_r4_2b_human_review_interface.ps1` | The offline human review panel |
| `build_r4_2c_calibrated_qa.ps1` | The R4.2C calibrated QA comparison |
| `build_r4_2cr_true_terra_review.ps1` | The independent true-Terra review inputs |
| `build_r4_2d_human_diagnostic_panel.ps1` | The human diagnostic adjudication panel |
| `build_r4_2d_human_diagnostic_completed.ps1` | The completed human diagnostic record |
| `build_r4_2e_a_repair_candidate_identification.ps1` | The deterministic triage over 1,404 records |
| `build_r4_2e_b0_repair_strategy_compression.ps1` | The 211 repair families and route assignment |
| `build_r4_2e_b1_batch_allocation.ps1` | The allocation of 143 cases into four batches |
| `build_r4_2e_b1_batch01_validation.ps1`, `close_r4_2e_b1_batch01.ps1` | B1-01 output and freeze |
| `build_r4_2e_b1_batch02_validation.ps1` | B1-02 output |
| `build_r4_2e_b1_batch03_validation.ps1` | B1-03 output |
| `build_r4_2e_b1_batch03_control_results.ps1` | B1-03 control unblinding |
| `build_r4_2e_b1_batch04_validation.py` | B1-04 output, with explicit schema gates |
| `build_r4_2e_b1_batch04_control_results.py` | B1-04 control unblinding |
| `build_r4_2e_b1_final_consolidation.py` | Reconciliation of 143 cases and 12 controls |
| `build_r4_2e_b1_new_diagnostic_candidates.py` | The new structural diagnostic candidates |
| `build_r4_2e_b1s_action_sensitivity_audit.py` | The Action representation sensitivity audit |
| `build_r4_variable_redundancy_audit.py` | The five variable-pair redundancy findings |
| `build_r4_david_summary.py` | The David-facing summary table |
| `build_r4_final_manifest.py` | The SHA-256 manifest of final artifacts |
| `apply_r4_claude_provenance_correction.py` | The Claude provenance correction, with byte verification |
| `build_envio_r4_to_david_package.py` | This delivery package |

## Three kinds of reproducibility — and what is honestly claimed

**Deterministic reproducibility.** The triage, the compression, the consolidation, the sensitivity
audit arithmetic, the redundancy audit and every manifest are deterministic. Re-running these
scripts against the same frozen inputs reproduces the same outputs, and the redundancy and
manifest scripts recompute their figures from the corpus at run time rather than reciting stored
numbers. This is fully reproducible.

**Model-assisted reproducibility.** The substantive adjudications in B1-01 to B1-04 are **not**
reproducible in this sense. The batch scripts are faithful records of the decisions — each
decision is written into the script as structured data and exported through a CSV library — but
re-running them replays the recorded decisions; it does not regenerate them from the model. The
model runtimes involved are not available for re-execution, and for the Claude work the runtime
label could not even be verified against the researcher's selection. **Full computational
reproducibility of the model judgments is therefore not claimed.** What is available is a complete,
hashed record of what was decided, by which model, on which input.

**Human adjudication provenance.** The R4.2D diagnostic and the human QA decisions are human
judgments. They are not reproducible by execution at all. They are auditable: the panel, the
working files, the completed adjudications and the resulting rules are all preserved in folder 05,
so a reader can check the reasoning against the frozen legal sources and disagree with it.

```text
RIT_CODING             = NOT_STARTED
MECHANISM_CODING       = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                   = NOT_STARTED
CORPUS_WIDE_REPAIR     = NOT_EXECUTED
```
