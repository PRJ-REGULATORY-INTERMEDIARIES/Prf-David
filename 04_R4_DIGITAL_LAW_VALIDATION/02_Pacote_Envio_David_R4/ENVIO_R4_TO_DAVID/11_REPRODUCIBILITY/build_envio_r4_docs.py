"""Generate the ENVIO_R4_TO_DAVID documentation: section READMEs, file guide, manifest."""
import csv, hashlib, os

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PKG = os.path.join(REPO, 'ENVIO_R4_TO_DAVID')
MAP = os.path.join(PKG, '00_START_HERE', 'R4_TRACEABILITY_MAP.csv')

FIREWALL = """```text
RIT_CODING             = NOT_STARTED
MECHANISM_CODING       = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                   = NOT_STARTED
CORPUS_WIDE_REPAIR     = NOT_EXECUTED
```"""

SECTIONS = {
'01_FINAL_R4_DATASET': ('README_FINAL_DATASET.md', """# 01 — Final R4 dataset

## Final consolidated delivery dataset

**`R4_Digital_Validation_Dashboard.xlsx`**

Status: `FINAL_R4_CONSOLIDATED_DATASET` / `FINAL_R4_DELIVERY_DATASET`

Purpose: the researcher-facing consolidation of the R4 digital structural-validation findings.
It integrates the final interpreted metrics, the source summary and the interpretation
guardrails needed to understand the result of this round without reading the full evidence
chain.

Worksheets:

| Sheet | Contents |
| --- | --- |
| **Dashboard** | Headline figures — 1,404 structural records, 143 advanced-reviewed cases, 63 sensitivity-adjusted Action corrections, 296 potential template coverage — with per-act records, reviewed counts and review share, plus four charts: corpus and B1 review by act, B1 defect decisions by act, field corrections proposed, and relational differentiation. |
| **Key Findings** | Executive interpretation in five numbered findings — structural portability, variable parsimony, Action sensitivity, repair templates, diagnostic controls — followed by an explicit "what is NOT yet concluded" block. |
| **Metrics** | Normalised per-act and total metrics behind the charts, each row carrying its own method note (for example "Within B1 only", "Purposive/enriched validation set"). |
| **Source Data** | The full dimension-by-instrument table, mirroring `R4_DIGITAL_VALIDATION_SUMMARY_FOR_DAVID.csv`. |
| **Method Notes** | Interpretation guardrails: B1 review design, sampling interpretation, the Action sensitivity audit, the status of the controls, the compression gate, template validation, the untouched original corpus, the next analytical layer, and the independence firewall. |

> The Excel workbook is the final consolidated R4 delivery dataset. It integrates the final
> validated R4 findings in a researcher-facing format with dashboard, metrics, methodological
> notes and source-summary views. The original 1,404-row structural extraction remains preserved
> separately as the immutable source dataset and was not corpus-wide repaired.

## Supporting summary

**`R4_DIGITAL_VALIDATION_SUMMARY_FOR_DAVID.csv`**

Status: `FINAL_R4_EXECUTIVE_SUMMARY_DATA`

The same aggregate table in plain CSV, for anyone who wants the numbers without the workbook.
It reports both the frozen and the sensitivity-adjusted Action correction counts side by side.

## Immutable structural source

`R4_STRUCTURAL_EXTRACTION.csv`, in `03_SOURCE_DATA_AND_CORPUS/`, holds the **1,404 original
structural records** and remains the frozen source extraction. It was read only throughout R4
and is unmodified.

```text
CORPUS_WIDE_REPAIR = NOT_EXECUTED
```

No repaired 1,404-row corpus was produced, and none is claimed. The Excel workbook is the final
consolidated R4 **delivery** dataset; the 1,404-row extraction remains the immutable underlying
**structural** dataset. The two serve different purposes and neither replaces the other.

""" + FIREWALL),

'02_EXECUTIVE_REPORTS': ('README_EXECUTIVE_REPORTS.md', """# 02 — Executive reports

Two documents written for Professor David Levi-Faur.

**`R4_DIGITAL_VALIDATION_MEMO_FOR_DAVID.md`** is the main report. It sets out why the round was
conducted against the three questions originally posed, describes the corpus and the structural
dataset, explains the layered validation design, and reports the findings: the three recurring
defect families, the variable-parsimony results, the counterpart/recipient result in detail, and
what does and does not travel from green to digital regulation.

It also contains, in its own section, the correction the project had to make to its own method —
the Action representation problem — rather than burying it. That section explains why the Action
correction count is reported as both 87 and 63, and why only one of 143 overall defect decisions
is affected.

The memo closes with an explicit list of what the round does **not** show, and a recommendation
against launching the corpus repair before the compression design is reassessed.

**`R4_EMAIL_TO_DAVID_DRAFT.md`** is a concise cover email carrying the same substance in about a
page, without the implementation detail. It is a draft for the researcher to send, edit or
discard.

Neither document claims that R4 as a whole is complete, that R/I/T or mechanism coding has been
performed, or that a Green × Digital governance comparison has been made.

""" + FIREWALL),

'03_SOURCE_DATA_AND_CORPUS': ('README_SOURCE_DATA.md', """# 03 — Source data and corpus

This folder holds the frozen inputs on which everything else depends.

**`R4_STRUCTURAL_EXTRACTION.csv`** is the immutable 1,404-record structural extraction — GDPR
485, DSA 424, AI Act 495 — on the unit *legal provision × actor × legal action*. Every finding
in this package derives from it, and it was never modified. If you want to check any claim in
the memo against the underlying data, this is the file.

The corpus registers document what was collected and from where. **`R4_DIGITAL_CORPUS_REGISTER.csv`**
identifies the three instruments and their CELEX ids. **`R4_LEGAL_STRUCTURE_INDEX.csv`** and
**`R4_ARTICLE_INDEX.csv`** index articles, recitals and annexes.
**`R4_LEGAL_STRUCTURE_QC.csv`** is the quality check on that index, and
**`R4_LEGAL_TEXT_PROVENANCE.csv`** records the source, retrieval and hash of each frozen text.
**`R4_LEGAL_CORPUS_VALIDATION_REPORT.md`** is the narrative confirmation that the corpus matches
the official EU sources.

**`R4_1_METHOD_NOTE.md`** explains how the corpus was constructed and why original rather than
consolidated texts were used.

`source_metadata/` carries, per instrument, the retrieval metadata and the structural validation
output produced when the text was normalised.

The frozen normalised texts themselves are large and remain in the main repository under
`R4_CROSS_DOMAIN_VALIDATION/02_sources/`; they are not duplicated here. Their identity is
established by the provenance and validation files included in this folder.

""" + FIREWALL),

'04_R4_2_STRUCTURAL_EXTRACTION': ('README_R4_2_EXTRACTION.md', """# 04 — R4.2 structural extraction

The artifacts produced when the 1,404 records were extracted.

**`R4_2_METHOD_NOTE.md`** sets out the extraction method and the unit of analysis.
**`R4_2_AI_EXTRACTION_RUN_SUMMARY.csv`** records the extraction run itself, and
**`R4_2_SOURCE_COVERAGE_REPORT.csv`** shows how much of each instrument the extraction covers.

Four registers capture what was found across the corpus rather than per record:
**`R4_DIGITAL_ACTOR_CANDIDATE_REGISTER.csv`** (candidate actors),
**`R4_LEGAL_ACTION_REGISTER.csv`** (legal actions),
**`R4_LEGAL_DEFINITION_REGISTER.csv`** (definitions given in the instruments) and
**`R4_CROSS_REFERENCE_REGISTER.csv`** (cross-references between provisions). These are useful if
you want to see the vocabulary the digital corpus actually uses before any theoretical coding.

**`R4_STRUCTURAL_AMBIGUITY_LOG.csv`** records ambiguities the extractor flagged at the time, and
**`R4_2_HUMAN_QA_SAMPLE.csv`** is the initial sample drawn for human checking.

A caution when reading these: the extraction stage is descriptive and pre-theoretical. It does
not classify regulators, intermediaries or targets, and the later validation stages showed that
several of its fields need repair before they can support that classification.

""" + FIREWALL),

'05_QA_AND_HUMAN_ADJUDICATION': ('README_QA_HUMAN.md', """# 05 — QA and human adjudication

Three stages, in order.

## R4.2B — stratified human QA

A stratified sample was reviewed through an offline panel. The stage produced an ambiguity
typology, a confidence calibration table, a correction register, QA metrics and a systematic
error audit (with a later updated version, both preserved). Two cross-model-supported patterns
emerged: counterpart/recipient over-attribution and actor/action fragmentation.

`human_review_interface/` holds the panel and its working file — the actual instrument the human
researcher used.

## R4.2C — cross-model review

Two model families reviewed the extraction independently and their outputs were compared. The
comparison tables, the calibrated and independent Terra reviews, their freeze manifests and the
closure report are all here.

This stage also produced an explicit **model provenance correction**
(`R4_2C_MODEL_PROVENANCE_CORRECTION.md` and `R4_2C_OUTPUT_RECLASSIFICATION.csv`): outputs whose
model provenance could not be confirmed were reclassified rather than assumed. The same
discipline was applied later to the Claude model label, which is recorded as
`MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE`.

`r4_2c_working_copies/` holds six files that share a filename with a file in this folder but
differ byte-for-byte. Both versions are preserved rather than one silently overwriting the other.

## R4.2D — human diagnostic

`R4_2D_human_diagnostic/` is the most important evidence in this folder for anyone auditing the
human contribution. Twelve purposively selected, cross-model-supported cases were adjudicated by
the researcher; all twelve contained confirmed structural defects.

Read `R4_2D_HUMAN_DIAGNOSTIC_REPORT.md` for the narrative,
`R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv` for the case-by-case adjudication, and
`R4_2D_HUMAN_DIAGNOSTIC_RULE_CANDIDATES.md` for the **15 candidate structural rules** frozen
from it. Those rules governed every later stage and were not modified by any AI process.

Two interpretation points carried throughout the project: the twelve cases are diagnostic
evidence about failure modes, **not** a corpus error rate, because they were selected precisely
because models flagged them; and the human root cause frequently differed from the model
detection pattern, which is itself recorded as rule 15.

""" + FIREWALL),

'06_REPAIR_TRIAGE_AND_COMPRESSION': ('README_REPAIR_TRIAGE.md', """# 06 — Repair triage and compression

## R4.2E-A — deterministic triage

`R4_2E_A_triage/` holds a deterministic heuristic run across all 1,404 records, classifying each
as a repair candidate: **YES 713, UNCERTAIN 346, NO 345**, with complexity NONE 345, SIMPLE 160,
MODERATE 514, COMPLEX 385.

These are **candidate signals, not confirmed defects**. The heuristic was validated against the
known human cases and rediscovered **9 of 12**, missing three that remain recorded blind spots in
`R4_2E_A_HUMAN_CASE_RULE_REDISCOVERY.csv`. A step that misses a quarter of known defects is a
triage device, not a detector, and it was used only as the former.

Two focused audits sit alongside it: one on actor/action fragmentation and one on the
counterpart/recipient coding burden, the latter feeding directly into the parsimony question.

## R4.2E-B0 — compression

`R4_2E_B0_compression/` holds the compression of 524 candidate records into **211 repair
families** sharing a structural signature, reducing advanced review to **131 cases** and
reserving 185 for human-only handling.

`R4_2E_B0_REPAIR_FAMILY_REGISTER.csv` defines the families and their sizes;
`R4_2E_B0_REPAIR_SIGNATURE_REGISTER.csv` gives each record its signature and route. These two
files are what later made it possible to test whether a family's representative is actually
representative — and the advanced validation found that in six families it is not.

`R4_2E_B0_RELATIONAL_FIELD_STRATEGY.md` is worth reading directly. It froze the requirement that
counterpart and recipient be assessed independently, with a separate rationale each, and recorded
the 995/995 identity as an operational property explicitly **not** as theoretical equivalence.

`R4_2E_B0_HEURISTIC_BLIND_SPOTS.md` documents the known limitations honestly rather than leaving
them implicit.

""" + FIREWALL),

'07_ADVANCED_VALIDATION_B1': ('README_ADVANCED_VALIDATION.md', """# 07 — Advanced validation (R4.2E-B1)

143 cases reviewed against the frozen legal sources: 99 family representatives, 32 individual
advanced cases and 12 NO_REPAIR diagnostic controls, in four frozen batches.

## `batch_outputs/`

The four authoritative outputs. B1-01, B1-02 and B1-03 were produced with GPT-5.6 Terra High
under OpenAI Codex; B1-04 was produced in Claude Code after that environment reached its usage
limit. No earlier batch was rerun or relabelled. Each row carries its own model provenance.

Frozen results across all 143 cases: **YES 111, PARTIALLY 15, NO 17, ABSTAIN 0**. Anchor
confidence HIGH 124, MEDIUM 12, LOW 7. Field corrections: Actor 47, Action 87, Object 83,
Counterpart 88, Recipient 98.

**These are not corpus prevalence.** The set was built by concentrating suspected defects.

## `design/`

The frozen batch allocation and manifest, plus `R4_2E_B1_BLIND_SUBSTANTIVE_REVIEW_INPUT.csv` —
the exact input reviewers saw. That last file is worth opening: it exposes `LEGAL_ACTION` and not
`LEGAL_VERB` or `MODALITY`, which is the design flaw the sensitivity audit in folder 08 then
quantified.

## `diagnostic_controls/`

The control sample and the per-batch results, consolidated in
`R4_2E_B1_CONTROL_DIAGNOSTIC_CONSOLIDATED.csv`: **CLEAN_CONFIRMED 5, DEFECT_FOUND 7,
PARTIAL_DEFECT 0, ABSTAIN 0, SERIOUS 0**.

These are **NO_REPAIR diagnostic controls**, not blind controls. The control sample file lists
all twelve with no batch column and the protocol requires reading it to unblind each batch, so
blinding was not guaranteed. No false-negative rate is calculated from them.

## `freeze_records/`

One per batch. The B1-04 record also documents the corrected Claude provenance and three recorded
design limitations: the blinding compromise, the schema under-exposure, and the cross-model
threshold difference.

## `combined_reports/`

`R4_2E_B1_METHOD_REPORT.md` is the full method report, including the sensitivity audit and the
reasoning behind `B0_COMPRESSION_REASSESSMENT_REQUIRED`. `R4_2E_B1_FINAL_SUMMARY.csv` holds the
reconciled metrics. `R4_2E_B1_NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATES.csv` records seven new issues
for adjudication without altering the 15 frozen rules. `R4_2E_B1_HANDOFF_STATE.md` states the
current position and the unresolved questions.

""" + FIREWALL),

'08_ACTION_SENSITIVITY_AUDIT': ('README_ACTION_SENSITIVITY.md', """# 08 — Action representation sensitivity audit (R4.2E-B1S)

After B1 closed, final QA found a problem with the review instrument rather than with the corpus.

The review input presented an Action field populated from `LEGAL_ACTION`, a controlled-vocabulary
label. The extraction separately holds `LEGAL_VERB`, carrying the source predicate with its
modality, and a `MODALITY` category. Verified deterministically: an explicit modal appears in
`LEGAL_VERB` in **1,370 of 1,404** records and in `LEGAL_ACTION` in **5**. Reviewers therefore
recorded modality as missing when it was present in a column they were not shown.

`R4_2E_B1_ACTION_SENSITIVITY_AUDIT.csv` re-examines all 143 Action judgments against the full
representation, one row per case, with the original judgment, the judgment under full
representation, a sensitivity result and a written reason. No case was rerun and no frozen
adjudication was modified.

`R4_2E_B1_ACTION_SENSITIVITY_SUMMARY.csv` gives the aggregates:

| | |
| --- | --- |
| `ORIGINAL_B1_ACTION_CORRECTION_COUNT` | **87** (frozen, not overwritten) |
| `SENSITIVITY_ADJUSTED_ACTION_CORRECTION_COUNT` | **63** (descriptive) |
| Action decisions changed | 26 (25 one way, 1 the other) |
| Overall defect decisions materially affected | **1 of 143** |

Both counts are reported. The adjusted figure is a
`POST_HOC_ACTION_REPRESENTATION_SENSITIVITY_RESULT`, not a re-review.

Two Action defect classes survive the audit as real rather than representational: entitlement
constructions recorded without "shall" and with modality UNCLEAR, and coordinated predicates
buried inside the object.

`R4_VARIABLE_REDUNDANCY_AUDIT.csv` recomputes five variable pairs with their overlap, exactness,
direction and parsimony status — counterpart/recipient, the two object fields, ambiguity versus
confidence, legal action versus legal verb, and modality versus legal verb. It is the single
best file to read for the variable-parsimony question.

""" + FIREWALL),

'09_MODEL_PROVENANCE': ('README_MODEL_PROVENANCE.md', """# 09 — Model provenance

`R4_AI_EXECUTION_LOG.csv` records every AI execution across R4 with its model and purpose.
`R4_MODEL_ESCALATION_LOG.csv` records escalations and model changes. Together they are the
authoritative answer to "which model did what" in this round.

## Terra — B1-01, B1-02, B1-03

```text
REQUESTED_MODEL         = GPT-5.6 Terra High
RESEARCHER_SELECTED_MODEL = GPT-5.6 Terra High
MODEL_RUNTIME_VARIANT   = MODEL_VARIANT_NOT_EXPOSED
```

Executed under OpenAI Codex. The runtime variant was never exposed and is recorded as such.

## Claude — B1-04 and the B1S sensitivity audit

```text
EXECUTION_ENVIRONMENT         = Claude Code / VS Code extension
RESEARCHER_SELECTED_MODEL     = Claude Opus 5.5 Extra High
RUNTIME_REPORTED_MODEL        = Claude Opus 5
RUNTIME_MODEL_ID              = claude-opus-5
MODEL_SELECTION_RUNTIME_MATCH = NOT_VERIFIABLE
```

The researcher selected `Claude Opus 5.5 Extra High` in the VS Code Claude agent UI; the
execution environment reported `Claude Opus 5`. The relationship between the two labels could not
be verified from inside the session. **Both are recorded. The runtime did not verify the
researcher's selection, and the two labels are not asserted to be equivalent.**

The correction that established this rewrote only provenance columns; substantive cells were
verified byte-identical. The pre-correction exports are preserved in
`10_FREEZE_AND_INTEGRITY/superseded_preserved/`.

## Earlier stages

Initial extraction and early QA were performed with Luna; R4.2C compared Luna and Terra. That
stage produced its own provenance correction, preserved in folder 05, in which outputs whose
provenance could not be confirmed were reclassified rather than assumed.

## Human authority

`Igor Caires Machado` is the final methodological authority for theoretical decisions, human
adjudication, acceptance or rejection of candidate rules, interpretation, research design and
scientific conclusions. AI output is extraction assistance, structural review, diagnostic
proposal, QA and sensitivity analysis — **not autonomous ground truth**.

`R4_SESSION_CHECKPOINT_2026-09-26.md` and `R4_GIT_SYNC_LOG.md` record execution continuity and
repository synchronisation.

""" + FIREWALL),

'10_FREEZE_AND_INTEGRITY': ('README_INTEGRITY.md', """# 10 — Freeze and integrity

**`R4_DIGITAL_STRUCTURAL_VALIDATION_FREEZE_RECORD.md`** is the single authoritative statement of
where the round ended: corpus, dataset, B1 design and completion, provenance, batch hashes,
frozen results, the sensitivity audit, the parsimony findings, the control limitation, the B0
decision, the template position, the limitations and the firewalls.

**`R4_DIGITAL_STRUCTURAL_VALIDATION_MANIFEST.csv`** is the SHA-256 manifest of the 24 final
scientific artifacts, each with its authoritative status. Use it to verify that any file you
have matches what was frozen.

`R4_BASELINE_FREEZE_RECORD.md` and `R4_PRE_R4_2_CHECKPOINT.md` mark the earlier stage boundaries.

## `superseded_preserved/`

**NOT AUTHORITATIVE — PRESERVED FOR AUDIT TRAIL.**

These five files are kept because their preservation itself documents a methodological incident.
Do not use them as data.

- Three **B1-01 v1 schema-defective** exports. The first B1-01 export was malformed because note
  text contained separators. It is preserved as evidence of the incident that led to the rule
  that all CSV output goes through a CSV library with full quoting. The authoritative B1-01
  output is `R4_2E_B1_ADVANCED_VALIDATION.csv` in folder 07.
- Two **provenance-superseded** exports, for B1-04 and the sensitivity audit, taken before the
  Claude provenance correction. Their substantive cells are byte-identical to the authoritative
  versions; only the provenance columns differ. They are preserved as part of the recorded
  correction chain.

The current version of every artifact is the one in folders 01 to 09. Nothing in
`superseded_preserved/` should be read as a competing result.

## Verifying this package

`00_START_HERE/R4_PACKAGE_MANIFEST.csv` lists every file in the delivery folder with its size,
SHA-256, category and authoritative status. Every copied evidence file was byte-verified against
its source at packaging time; a mismatch would have excluded the file and been reported as
`COPY_INTEGRITY_FAILURE`. None occurred.

""" + FIREWALL),

'11_REPRODUCIBILITY': ('README_REPRODUCIBILITY.md', """# 11 — Reproducibility

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

""" + FIREWALL),

'12_ARCHIVE_SUPPORT': ('README_ARCHIVE_SUPPORT.md', """# 12 — Archive and support

Material that is not part of the R4 findings but is needed to audit how the round was set up and
governed.

**Baseline continuity.** `R4_R3_BASELINE_MANIFEST.md` records the frozen R3 green baseline;
`R4_R3_RECONCILIATION.csv` gives the reconciled R3 totals carried into R4;
`R4_R3_TO_R4_INTEGRATION_MAP.csv` maps R3 artifacts onto R4 structures;
`R4_R3_HISTORICAL_INTEGRATION_REPORT.md` narrates the integration; and
`R4_R3_HISTORY_FILE_INVENTORY.csv` with `R4_R3_HISTORY_ARCHIVE_METADATA.json` inventory the
archived history. These matter because R4's claim is comparative — that an architecture built on
green regulation travels to digital regulation — so the green side must be auditable too.

**Change control.** `R4_PREEXISTING_R4_2_CHANGE_AUDIT.csv` audits changes present before R4.2
began, so that later findings cannot be confused with earlier drift.

**Design and governance.** `R4_INITIAL_METHOD_NOTE.md` states the original R4 research question.
`R4_WORKSPACE_STRUCTURE.md` defines the workspace layout.
`R4_INITIAL_SETUP_PROMPT_VERBATIM.txt` preserves the verbatim instruction that set up R4, and
`PROTOCOLO_USO_IA_R1_R3_PRE_R4_v1_1.docx` is the researcher's protocol governing AI use across
the earlier rounds. The last two are included for transparency about how AI was instructed and
constrained, which is part of the methodological record rather than an afterthought.

The full R3 history archive itself is large and remains in the main repository under
`R4_CROSS_DOMAIN_VALIDATION/01_baseline/`; it is inventoried here rather than duplicated.

""" + FIREWALL),
}


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest().upper()


def main():
    for folder, (fname, text) in SECTIONS.items():
        d = os.path.join(PKG, folder)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, fname), 'w', encoding='utf-8') as fh:
            fh.write(text + '\n')
    print(f'section READMEs written: {len(SECTIONS)}')

    rows = list(csv.DictReader(open(MAP, encoding='utf-8-sig')))
    groups = {}
    for r in rows:
        groups.setdefault(os.path.dirname(r['PACKAGE_PATH']), []).append(r)

    lines = ['# R4 File Guide', '',
             'Every evidence file copied into this package, documented individually. Files are',
             'grouped by folder and listed alphabetically. For the machine-readable version with',
             'SHA-256 hashes, see `R4_TRACEABILITY_MAP.csv`.', '',
             'The documentation files generated for this package '
             '(this guide, the README files, the manifest and the package note) are described in',
             '`README_R4_FOR_DAVID.md` and are not repeated below.', '',
             f'**Evidence files documented: {len(rows)}**', '', '---', '']
    for folder in sorted(groups):
        lines.append(f'## `{folder}/`')
        lines.append('')
        for r in sorted(groups[folder], key=lambda x: x['FILE_NAME']):
            lines.append(f"### {r['FILE_NAME']}")
            lines.append('')
            lines.append(f"**Folder:** `{folder}/` | **Phase:** {r['PHASE']} | "
                         f"**Type:** {r['ARTIFACT_TYPE']} | **Status:** {r['EVIDENCE_LEVEL']}")
            lines.append('')
            lines.append(f"**Origin:** `{r['ORIGINAL_PATH']}`")
            lines.append('')
            lines.append(f"**Contents and why it exists.** {r['PURPOSE']} It was produced at the "
                         f"{r['PHASE']} stage by {r['CREATED_BY']}.")
            lines.append('')
            lines.append(f"**Model provenance.** {r['MODEL_PROVENANCE']}")
            lines.append('')
            lines.append(f"**What it supports.** {r['SUPPORTS_FINDING']}. "
                         f"Human-validated: {r['HUMAN_VALIDATED']}. Frozen: {r['FROZEN']}. "
                         f"Role: {r['FINAL_OR_SUPPORTING']}.")
            lines.append('')
            if r['NOTES']:
                lines.append(f"**Note.** {r['NOTES']}")
                lines.append('')
            lines.append(f"**How to use it.** {how_to_use(r)}")
            lines.append('')
        lines.append('---')
        lines.append('')
    with open(os.path.join(PKG, '00_START_HERE', 'R4_FILE_GUIDE.md'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(lines))
    print(f'file guide written: {len(rows)} files documented')
    return len(rows)


def how_to_use(r):
    t, lvl = r['ARTIFACT_TYPE'], r['EVIDENCE_LEVEL']
    if lvl == 'SUPERSEDED_PRESERVED':
        return ('Do not use as data. Read it only to audit the incident it documents; the '
                'authoritative counterpart is in folders 01 to 09.')
    if lvl == 'AUTHORITATIVE_FINAL':
        return 'Read this directly. It is a final deliverable of the round.'
    if t == 'SOURCE DATA' or lvl == 'AUTHORITATIVE_SOURCE':
        return ('Use this to check any downstream claim against the underlying data. It is '
                'frozen, so figures quoted elsewhere should reconcile exactly against it.')
    if t == 'HUMAN EVIDENCE':
        return ('Read this to audit the human contribution: what the researcher decided and on '
                'what reasoning. These decisions govern where a model disagreed.')
    if t == 'PROVENANCE':
        return 'Consult this to establish which model or person produced a given output, and when.'
    if t == 'FREEZE/INTEGRITY':
        return 'Use this to verify that an artifact matches what was frozen at the time.'
    if t == 'REPRODUCIBILITY':
        return ('Re-run it against the frozen inputs to regenerate the deterministic outputs. '
                'For batch scripts this replays recorded decisions rather than regenerating them.')
    if t == 'SUPPORTING ARCHIVE':
        return 'Background material; consult it if you are auditing how the round was set up.'
    if t == 'QA':
        return 'Read this to see how quality was assessed at that stage and what it found.'
    return ('Supporting model output. Read it alongside the method report for the stage rather '
            'than on its own.')


if __name__ == '__main__':
    main()
