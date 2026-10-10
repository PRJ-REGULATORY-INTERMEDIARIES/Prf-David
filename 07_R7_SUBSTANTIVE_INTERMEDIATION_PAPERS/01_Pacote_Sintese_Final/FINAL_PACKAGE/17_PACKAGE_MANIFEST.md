# 17 — Package manifest

**Created** 2026-10-08. **Location** `G:/Meu Drive/PRJ-David/Prf-David/FINAL_PACKAGE/`.

**Scope of the work.** Synthesis and consolidation only. No legal text was recoded, no frozen analytical output was modified, no adjudication was performed, no new comparison was run, and no external source was retrieved. All reads of the frozen arms and registers were read-only.

---

## What to send to David

**Send this:**

1. **`14_FINAL_NOTE_FOR_DAVID.md`** — the clean, red-team-corrected note, with the three figures embedded. This is the deliverable.
2. **`15_EMAIL_TO_DAVID.md`** — the covering message.

**Optionally also send:**

3. **`11_ONE_PAGE_BRIEF.md`** — if David would rather read five minutes than twenty. Best placed at the front of the same attachment rather than sent as a second file.

**Do not send:** `10_EXECUTIVE_SUMMARY_FOR_DAVID.md` is a redundant middle length — it exists for Igor's own use (e.g. a seminar abstract or a message to a third party) and sending all three versions would look like padding. Files `01`–`08`, `12`, `13`, `16` and this manifest are internal: source maps, evidence ledgers, control reviews, claims audits and red-team commentary. They are what makes the note defensible if challenged; they are not what David asked for.

---

## File-by-file

| File | Purpose | Principal authoritative sources | Send? |
|---|---|---|---|
| `01_SOURCE_MAP.md` | The smallest authoritative source set; exclusions; unresolved provenance | David's V8 manuscript; both frozen arms; preregistration; Round-1 registers; stage-15 preparation | internal |
| `02_EVIDENCE_LEDGER.md` | Evidence by case, separating OBSERVED / INTERPRETED / NOT ESTABLISHED | `PRE_ADJUDICATION_DESCRIPTIVE_SUMMARY.md`; four `PAIR_PRE_ADJUDICATION_SUMMARY.md`; both cross-case summaries; `MASTER_HUMAN_REVIEW_CARDS.md`; `MASTER_IDENTITY_KEY.csv`; the 19 frozen tables per controlled case | internal |
| `03_INFERENTIAL_PROBLEM.md` | Why the exercise became elaborate; where AI coding is vulnerable | Manuscript §6.1–§6.10; `RGAM_PAIRED_EXECUTION_PROTOCOL_v1_0.md` §9–§11; `V8_RGAM_METHOD_CROSSWALK.md` | internal |
| `04_FOUR_CASE_SYNTHESIS.md` | Case-by-case comparison and comparison table | Round-1 per-pair registers and QA; both arms' stopping records and architecture registers | internal |
| `05_METHOD_CONTROLS_REVIEW.md` | Twelve controls classified RETAIN / SIMPLIFY / OPTIONAL / REMOVE, with reasons | Frozen protocol and decision rules; D1–D8 distributions; crosswalk; family cost descriptors | internal |
| `06_INTERMEDIATION_AGENDA.md` | David's four questions: what coding can establish, suggest, and not reach (incl. governed governors and intermediation-in-hierarchy) | Manuscript §6.12 and conclusion; `QUALIFIED_RELATIONS.csv`, `POSITIONS_AND_DEVICES.csv`, `EXTERNAL_REFERENCES.csv` for all four cases | internal |
| `07_WHAT_WE_CAN_AND_CANNOT_CLAIM.md` | The claims boundary | Manuscript §6.8, §6.13–§6.14; frozen external-reference and absence rules | internal (attach to any Phase 3 output) |
| `08_FIGURES.md` | Three figures, Mermaid plus plain-text fallback | Round-1 distributions; `05`; AI Act relational record | internal (figures are embedded in `14`) |
| `09_FROM_CODING_TO_ARCHITECTURE_NOTE_FOR_DAVID.md` | **Pre-red-team draft of the note.** Superseded | as `14` | **no — superseded by `14`** |
| `10_EXECUTIVE_SUMMARY_FOR_DAVID.md` | Standalone ~1,000-word summary | as `14` | not recommended (see above) |
| `11_ONE_PAGE_BRIEF.md` | Standalone short brief | as `14` | optional |
| `12_CLAIMS_AUDIT.md` | 54 claims audited SAFE / SAFE WITH QUALIFICATION / PRELIMINARY / DO NOT REPORT, plus prohibited-claim checks | the whole frozen record | internal |
| `13_RED_TEAM_REVIEW.md` | Adversarial review; thirteen attacks; eleven required corrections | `12`; the frozen record | internal |
| `14_FINAL_NOTE_FOR_DAVID.md` | **The sendable note**, corrections applied, figures embedded | all of the above | **yes** |
| `15_EMAIL_TO_DAVID.md` | Covering message | — | **yes** |
| `16_NEXT_PHASE.md` | Phase 1 complete / Phase 2 integrate / Phase 3 substantive | `05`; `06`; `12` | internal (its substance is in §11 of the note) |
| `17_PACKAGE_MANIFEST.md` | This file | — | internal |

**Provenance artefacts outside this folder** (created 2026-10-08, in the workspace provenance chain rather than the package):

| File | Purpose |
|---|---|
| `NEW TEST 3x3/16_HUMAN_VALIDATION_IMPORT_2026-10-08/HUMAN_VALIDATION_REGISTER_6.csv` | the six blinded decisions as archived |
| `.../POST_REVEAL_LINKAGE_6.csv` | each decision resolved against the frozen identity key |
| `.../HUMAN_VALIDATION_PROVENANCE.md` | provenance statement, incl. the machine-simulation exclusion |
| `.../PROTOCOL_DEVIATION_LOG.csv` | DEV-16-01, DEV-16-02 |
| `.../IMPORT_MANIFEST.csv` + `_SHA256.txt` | SHA-256 of each imported file and of the three Round-1 artefacts read |

---

## Unresolved limitations

These are disclosed in the note itself and are not artefacts of this synthesis.

1. **Fifty of the 56 cards were never human-adjudicated.** They retain `status = OPEN_AWAITING_HUMAN_ADJUDICATION`. Every claim about comparative quality rests on six purposively selected cards, and the fifty are never described as adjudicated by any means.
2. **The six decisions are archived, their reasons are not.** Imported on 2026-10-08 into `NEW TEST 3x3/16_HUMAN_VALIDATION_IMPORT_2026-10-08/` (register, post-reveal linkage, deviation log, provenance statement, SHA-256 manifest). No justification, confidence or per-card date was captured and none was reconstructed (DEV-16-02). Because the freeze-before-reveal sequence in `IDENTITY_REVEAL_PROTOCOL.md` cannot be satisfied retrospectively, this is a new versioned artefact, not a protocol-compliant frozen adjudication (DEV-16-01). Each decision is auditable as a decision and not as reasoning.
3. **Single adjudicator, and that adjudicator designed the study.** Blinding to arm identity does not remove the conflict. Disclosed in §4 of the note.
4. **The machine-simulated adjudication is formally excluded.** A non-authoritative machine-simulated adjudication was produced during exploratory workflow outside the frozen workspace; it is excluded from the evidentiary basis of this report, not imported, and relied on nowhere. See `HUMAN_VALIDATION_PROVENANCE.md` §5 and `01_SOURCE_MAP.md` §6.
5. **Controls and prompt structure are confounded.** Both arms and the comparator ran on `claude-sonnet-5-5`, with reasoning effort not exposed to the executor. No arm-blind control was run.
6. **No external source was retrieved.** 148 external references across the four cases, 73 constitutive, all `not_checked` / `outside_corpus_not_expanded`. Every claim touching them is about what an instrument *refers out to*.
7. **Case selection is not a sample.** Four instruments chosen to stress-test an inferential procedure: two climate, one unique-eligible AI case, one Directive repealed in 1992.
8. **Comparator interpretive latitude.** The comparison rules were frozen, but the operationalization of materiality, the clustering of absence-based claims and the blinding procedure were the comparator's choices, logged rather than pre-specified (Round-1 QA check 29).
9. **David's four priority questions are researcher-supplied**, not archived in the workspace. Stage 6 grounds each in a numbered section of the manuscript rather than in the prompt alone. See `01_SOURCE_MAP.md` §8.
10. **Disclosed Round-1 incidents** carried forward unchanged: a stale deny rule on the baseline arm path; digest-only access to five files under a forbidden path (contents never opened); heterogeneous baseline manifest schemas, with the CBAM baseline manifest lacking a legal-source row; an interruption with same-context recovery; and two self-corrections made before freezing. None alters a comparison category.

---

## Deviations from the specification for this synthesis

Recorded rather than concealed.

| Specified | Delivered | Why |
|---|---|---|
| `09` as the main note | `09` written, then superseded by `14` after the red-team pass | Eleven corrections were required, including a restatement of the headline claim. `09` is retained as the pre-correction draft for audit. |
| `10` at 600–900 words | ~1,040 | Three rounds of trimming, then the provenance correction. Further cuts would have required dropping a disclosed limitation, which is the worse error. |
| `11` at approximately 600 words | ~800 (including a ~90-word figure) | Same reason. |
| `14` at 3,500–5,000 words | ~5,185 prose plus ~490 words of figure appendix | ~5,070 after the red-team pass; the 2026-10-08 provenance correction added ~115 words to §4 (the preferred description of the six-card assessment, and the no-recorded-justification qualification). Both are required disclosures, so the overage was accepted rather than paid for by cutting a limitation. |
| Stages 6, 7, 8 as separate outputs | Combined in `06_INTERMEDIATION_AGENDA.md` | The specification allows the governed-governors and intermediation-in-hierarchy material as subsections of Stage 6, and they read better as one argument. |
| Figures in Mermaid | Mermaid plus plain-text fallback in `08`; plain-text only in `14` | The sendable note must render in any Markdown viewer and in an email client. `08` holds both forms. |

---

## Provenance status

`FINAL_PACKAGE_PROVENANCE_COMPLETE / HUMAN_VALIDATION_ARCHIVED / MACHINE_SIMULATION_EXCLUDED / READY_FOR_DAVID`

The six blinded decisions were archived on 2026-10-08 in `NEW TEST 3x3/16_HUMAN_VALIDATION_IMPORT_2026-10-08/`, a new numbered stage created so that the stage-15 preparation freeze remains valid. Stages 00–15 are untouched. The machine-simulated adjudication is formally excluded and relied on nowhere.

Nothing further is required before sending. The remaining evidential gap — independent adjudication of a subset of the 56 by someone who did not design the arms — is disclosed in §4 of the note and scheduled in Phase 2; it is not a blocker, because the note claims nothing that depends on it.
