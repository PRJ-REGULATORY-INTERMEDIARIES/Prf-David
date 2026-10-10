# G4 Step 2A — matching QA report

**Date:** 2026-10-04T20:56:09-03:00 · **Executor:** Claude Code (Sonnet 5.5), single sequential pass · **Checks:** 32 PASS, 0 FAIL (of 32)

The checks are automatic comparisons against the frozen Step 1 register, the cell files and the common register. They test integrity, completeness, level discipline, scope preservation, label hygiene and identity separation. **They do not validate the correspondence judgements themselves**, which are preliminary AI-assisted candidates requiring human review where marked.

## 1. Results

| ID | Check | Result | Detail |
|---|---|---|---|
| Q01 | Step 1 manifest SHA-256 equals expected and its SHA-256 file | **PASS** | 0DEC88FFF9CF9D5B… |
| Q02 | All Step 1 manifest rows except the four appended registers recalculate to their recorded hashes (27 rows: 7 outputs, 9 references, 11 cell source files) | **PASS** | mismatches: [] |
| Q03 | The four appended registers still equal their Step 1 manifest values at QA time (they are appended after QA; see Step 2A manifest) | **PASS** | differing: [] |
| Q04 | Four frozen cells (35 outputs: Codex 6+11, Claude 7+11 — recalculated: 35) and the common register unchanged | **PASS** | mismatches: []; register ok: True |
| Q05 | Step 0 files (other than the appended registers) unchanged | **PASS** | changed: [] |
| Q06 | Recovery report, claim-matching rules, Step 1 review queue and original criteria present | **PASS** | present |
| Q07 | The 13 required group fields present, in the stated order | **PASS** | ok |
| Q08 | 26 groups with unique IDs; levels and types as designed | **PASS** | {'relation': 16, 'configuration': 6, 'position': 2, 'architecture-level decision': 2} |
| Q09 | Every one of the 112 original units appears exactly once as grouped or as unmatched (no loss, no overlap) | **PASS** | grouped 101 + unmatched 11 = 112 |
| Q10 | The two STEP0_DERIVED cores appear only as attached units, marked STEP0_DERIVED, never as original members | **PASS** | ok |
| Q11 | Original claim IDs, cells and unit IDs in the mapping match the Step 1 register exactly | **PASS** | 115 mapping rows |
| Q12 | No group mixes analytical levels or legal cases (level discipline) | **PASS** | level mismatches: []; case mismatches: [] |
| Q13 | Within every group the members are connected through at least one shared frozen statement (traceability to the common evidence) | **PASS** | disconnected: [] |
| Q14 | Every group lists its frozen statements (union) and anchors; relation groups of the same act share all anchors | **PASS** | ok |
| Q15 | Scope class, primary-comparison eligibility and human-review priority are identical to Step 1 for every mapping row | **PASS** | differences: [] |
| Q16 | Preserved Step 0/1 findings: 5 SC-C, 2 SC-B, 105 SC-A among originals; 2 derived; 13 peripheral observations | **PASS** | {'SC-A': 105, 'SC-B': 2, 'SC-C': 5} |
| Q17 | Each of the 5 material-dependency units is visible in the mapping or unmatched file with its flag (grouped: 2; unmatched: 3) | **PASS** | ok |
| Q18 | Every group containing an SC-C, SC-B or derived unit carries a non-empty evidence-scope flag | **PASS** | missing: [] |
| Q19 | Scope flags propagated to higher-order groups (CG-025 from CG-018; CG-026 from CG-019 and CG-022) | **PASS** | ok |
| Q20 | Evidence-scope conflicts identified (members of a group with different classes) | **PASS** | ['CG-018', 'CG-019', 'CG-022'] |
| Q21 | No agreement score, improvement, regression, ranking or superiority label or field; no value of the five-category scheme or of the seven working labels in the CSV outputs | **PASS** | label hits: 0; headers: [] |
| Q22 | All correspondence types are CANDIDATE_* (no assertion of equivalence); outcome label status NOT_ASSIGNED in every group | **PASS** | ok |
| Q23 | CONFOUNDED_INPUT note present in every group | **PASS** | 26 of 26 |
| Q24 | Normalised propositions in the groups are the Step 1 normalised texts, unchanged | **PASS** | differences: [] |
| Q25 | Cardinality cases identified: many-to-one groups CG-001, CG-011; one-to-many unit CLAUDE_A:CL-P04-04 (2 groups) | **PASS** | many-to-one: ['CG-001', 'CG-011']; one-to-many: [('CLAUDE_A', 'CL-P04-04')] |
| Q26 | Unmatched file consistent with the mapping (11 units) | **PASS** | 11 |
| Q27 | Reviewer-facing package contains no cell names, claim IDs, unit IDs, group IDs or queue IDs | **PASS** | leaks: [] |
| Q28 | Package has one card per group requiring review (YES or SPOT_CHECK): 13 | **PASS** | 13 |
| Q29 | Identity key complete: every proposition of every card is mapped to exactly one unit | **PASS** | 50 key rows |
| Q30 | No reviewer field filled and no human decision simulated (package and Step 1 queue) | **PASS** | all blank |
| Q31 | Seven priority-1 items remain pending (queue unchanged) | **PASS** | 7 pending |
| Q32 | Git HEAD unchanged (ae1af32…) and no tracked-file changes | **PASS** | ae1af320 |

## 2. Counts (descriptive only)

| Item | Value |
|---|---|
| Correspondence groups | 26 (relation 16, configuration 6, position 2, architecture-level decision 2) |
| Correspondence types | {"CANDIDATE_SAME_PROPOSITION_DIFFERENT_SEGMENTATION": 2, "CANDIDATE_SAME_PROPOSITION": 16, "CANDIDATE_OVERLAPPING_PROPOSITION": 6, "CANDIDATE_SAME_SUBJECT_SAME_KIND_OF_DETERMINATION": 1, "CANDIDATE_SAME_SUBJECT_DIFFERENT_KIND_OF_DETERMINATION": 1} |
| Human review required | {"SPOT_CHECK": 4, "NO_LOW_RISK_AI_PRELIMINARY": 13, "YES": 9} |
| Mapping rows | 115 (102 memberships + 2 attached derived + 11 unmatched) |

| Cell | Original | Matched | Unmatched |
|---|---|---|---|
| CODEX_A | 24 | 24 | 0 |
| CODEX_B | 29 | 27 | 2 |
| CLAUDE_A | 28 | 24 | 4 |
| CLAUDE_B | 31 | 26 | 5 |

## 3. Limitations

- Matching judgements are by one AI executor that also orchestrated the Claude arm (role conflict D-15); they are candidates, and 13 groups are queued for review (9 `YES`, 4 `SPOT_CHECK`). The 13 groups marked `NO_LOW_RISK_AI_PRELIMINARY` were screened only by the same executor and are not validated.
- Connectivity (Q13) shows that group members share a frozen statement; it does not show that they state the same proposition.
- The reviewer package hides identifiers but not style: relation vocabulary (for example snake_case labels) and length can still hint at provenance.
- Step 1 normalised texts were used unchanged; any distortion in normalisation would carry into the groups (Step 1 QA applies).
- The official text was not consulted for Step 2A; all evidence is the frozen register.
- CONFOUNDED_INPUT applies to every group.
- **QA history:** the first run of Q21 reported 26 hits and was a false positive: the regular expression matched the word 'superiority' inside the disclaimer 'no agreement, improvement or superiority assessment' written in every group row. The expression was refined to the whole word 'superior' and the QA rerun; no data file was changed between the runs.
- After this QA the four main registers receive append-only Step 2A entries; their hashes then differ from the Step 1 manifest by design (recorded in the Step 2A manifest).