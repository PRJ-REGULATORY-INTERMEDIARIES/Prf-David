# R4 File Guide

Every evidence file copied into this package, documented individually. Files are
grouped by folder and listed alphabetically. For the machine-readable version with
SHA-256 hashes, see `R4_TRACEABILITY_MAP.csv`.

The documentation files generated for this package (this guide, the README files, the manifest and the package note) are described in
`README_R4_FOR_DAVID.md` and are not repeated below.

**Evidence files documented: 170**

---

## `01_FINAL_R4_DATASET/`

### R4_DIGITAL_VALIDATION_SUMMARY_FOR_DAVID.csv

**Folder:** `01_FINAL_R4_DATASET/` | **Phase:** R4 delivery | **Type:** FINAL OUTPUT | **Status:** AUTHORITATIVE_FINAL

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/08_reports/R4_DIGITAL_VALIDATION_SUMMARY_FOR_DAVID.csv`

**Contents and why it exists.** Compact aggregate metrics table for the R4 digital structural-validation round. It was produced at the R4 delivery stage by Igor Caires Machado (human researcher) with Claude assistance.

**Model provenance.** Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** All headline R4 findings. Human-validated: YES. Frozen: YES. Role: FINAL.

**Note.** FINAL_R4_EXECUTIVE_SUMMARY_DATA

**How to use it.** Read this directly. It is a final deliverable of the round.

### R4_Digital_Validation_Dashboard.xlsx

**Folder:** `01_FINAL_R4_DATASET/` | **Phase:** R4 delivery | **Type:** FINAL OUTPUT | **Status:** AUTHORITATIVE_FINAL

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/08_reports/R4_Digital_Validation_Dashboard.xlsx`

**Contents and why it exists.** FINAL_R4_CONSOLIDATED_DATASET. Five worksheets (Dashboard, Key Findings, Metrics, Source Data, Method Notes) plus four charts, consolidating the R4 digital structural-validation findings in researcher-facing form. It was produced at the R4 delivery stage by Igor Caires Machado (human researcher) with Claude assistance.

**Model provenance.** Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** All headline R4 findings and interpretation guardrails. Human-validated: YES. Frozen: YES. Role: FINAL.

**Note.** FINAL_R4_CONSOLIDATED_DATASET / FINAL_R4_DELIVERY_DATASET. Does NOT replace R4_STRUCTURAL_EXTRACTION.csv, which remains the immutable 1,404-record source.

**How to use it.** Read this directly. It is a final deliverable of the round.

---

## `02_EXECUTIVE_REPORTS/`

### R4_DIGITAL_VALIDATION_MEMO.pdf

**Folder:** `02_EXECUTIVE_REPORTS/` | **Phase:** R4 delivery | **Type:** FINAL OUTPUT | **Status:** AUTHORITATIVE_FINAL

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/08_reports/R4_DIGITAL_VALIDATION_MEMO.pdf`

**Contents and why it exists.** Eight-page typeset PDF of the David memo, for reading or circulation without a Markdown viewer. It was produced at the R4 delivery stage by Igor Caires Machado (human researcher).

**Model provenance.** Typeset export of the memo; content provenance as per the memo

**What it supports.** All headline R4 findings. Human-validated: YES. Frozen: YES. Role: FINAL.

**Note.** Same content as R4_DIGITAL_VALIDATION_MEMO_FOR_DAVID.md in this folder.

**How to use it.** Read this directly. It is a final deliverable of the round.

### R4_DIGITAL_VALIDATION_MEMO_FOR_DAVID.md

**Folder:** `02_EXECUTIVE_REPORTS/` | **Phase:** R4 delivery | **Type:** FINAL OUTPUT | **Status:** AUTHORITATIVE_FINAL

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/08_reports/R4_DIGITAL_VALIDATION_MEMO_FOR_DAVID.md`

**Contents and why it exists.** Main researcher-facing memo: portability, parsimony, method, limitations. It was produced at the R4 delivery stage by Igor Caires Machado (human researcher) with Claude assistance.

**Model provenance.** Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** Portability; parsimony; counterpart/recipient; limitations. Human-validated: YES. Frozen: YES. Role: FINAL.

**How to use it.** Read this directly. It is a final deliverable of the round.

### R4_EMAIL_TO_DAVID_DRAFT.md

**Folder:** `02_EXECUTIVE_REPORTS/` | **Phase:** R4 delivery | **Type:** FINAL OUTPUT | **Status:** AUTHORITATIVE_FINAL

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/08_reports/R4_EMAIL_TO_DAVID_DRAFT.md`

**Contents and why it exists.** Concise cover email summarising the round. It was produced at the R4 delivery stage by Igor Caires Machado (human researcher) with Claude assistance.

**Model provenance.** Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** Delivery communication. Human-validated: YES. Frozen: YES. Role: FINAL.

**How to use it.** Read this directly. It is a final deliverable of the round.

---

## `03_SOURCE_DATA_AND_CORPUS/`

### R4_1_METHOD_NOTE.md

**Folder:** `03_SOURCE_DATA_AND_CORPUS/` | **Phase:** R4.1 | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_1_METHOD_NOTE.md`

**Contents and why it exists.** Method note for digital corpus construction. It was produced at the R4.1 stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** Corpus methodology. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### R4_ARTICLE_INDEX.csv

**Folder:** `03_SOURCE_DATA_AND_CORPUS/` | **Phase:** R4.1 | **Type:** SOURCE DATA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_ARTICLE_INDEX.csv`

**Contents and why it exists.** Article-level index across the three instruments. It was produced at the R4.1 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Corpus navigation. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

### R4_DIGITAL_CORPUS_REGISTER.csv

**Folder:** `03_SOURCE_DATA_AND_CORPUS/` | **Phase:** R4.1 | **Type:** SOURCE DATA | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_DIGITAL_CORPUS_REGISTER.csv`

**Contents and why it exists.** Register of the three digital instruments and their CELEX ids. It was produced at the R4.1 stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Corpus definition. Human-validated: YES. Frozen: YES. Role: SOURCE.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

### R4_LEGAL_CORPUS_VALIDATION_REPORT.md

**Folder:** `03_SOURCE_DATA_AND_CORPUS/` | **Phase:** R4.1 | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_LEGAL_CORPUS_VALIDATION_REPORT.md`

**Contents and why it exists.** Validation report confirming the corpus matches official EU sources. It was produced at the R4.1 stage by Igor Caires Machado (human researcher).

**Model provenance.** Human + deterministic checks

**What it supports.** Corpus authenticity. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_LEGAL_STRUCTURE_INDEX.csv

**Folder:** `03_SOURCE_DATA_AND_CORPUS/` | **Phase:** R4.1 | **Type:** SOURCE DATA | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_LEGAL_STRUCTURE_INDEX.csv`

**Contents and why it exists.** Structural index of articles, recitals and annexes per instrument. It was produced at the R4.1 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Corpus structure counts. Human-validated: YES. Frozen: YES. Role: SOURCE.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

### R4_LEGAL_STRUCTURE_QC.csv

**Folder:** `03_SOURCE_DATA_AND_CORPUS/` | **Phase:** R4.1 | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_LEGAL_STRUCTURE_QC.csv`

**Contents and why it exists.** Quality control on the structural index. It was produced at the R4.1 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Corpus integrity. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_LEGAL_TEXT_PROVENANCE.csv

**Folder:** `03_SOURCE_DATA_AND_CORPUS/` | **Phase:** R4.1 | **Type:** PROVENANCE | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_LEGAL_TEXT_PROVENANCE.csv`

**Contents and why it exists.** Provenance of each frozen legal text: source, retrieval, hash. It was produced at the R4.1 stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Corpus authenticity. Human-validated: YES. Frozen: YES. Role: SOURCE.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

### R4_STRUCTURAL_EXTRACTION.csv

**Folder:** `03_SOURCE_DATA_AND_CORPUS/` | **Phase:** R4.2 | **Type:** SOURCE DATA | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/R4_STRUCTURAL_EXTRACTION.csv`

**Contents and why it exists.** The immutable 1,404-record structural extraction. Unit: legal provision x actor x legal action. It was produced at the R4.2 stage by Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv.

**Model provenance.** Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv

**What it supports.** Every downstream R4 finding. Human-validated: PARTIAL (QA sampled). Frozen: YES. Role: SOURCE.

**Note.** IMMUTABLE. CORPUS_WIDE_REPAIR = NOT_EXECUTED.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

---

## `03_SOURCE_DATA_AND_CORPUS/source_metadata/`

### D1_GDPR_metadata.json

**Folder:** `03_SOURCE_DATA_AND_CORPUS/source_metadata/` | **Phase:** R4.1 | **Type:** PROVENANCE | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/02_sources/D1_GDPR/metadata/D1_GDPR_metadata.json`

**Contents and why it exists.** Retrieval metadata for D1_GDPR. It was produced at the R4.1 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Corpus authenticity. Human-validated: YES. Frozen: YES. Role: SOURCE.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

### D1_GDPR_structural_validation.json

**Folder:** `03_SOURCE_DATA_AND_CORPUS/source_metadata/` | **Phase:** R4.1 | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/02_sources/D1_GDPR/validation/D1_GDPR_structural_validation.json`

**Contents and why it exists.** Structural validation output for D1_GDPR. It was produced at the R4.1 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Corpus integrity. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### D2_DSA_metadata.json

**Folder:** `03_SOURCE_DATA_AND_CORPUS/source_metadata/` | **Phase:** R4.1 | **Type:** PROVENANCE | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/02_sources/D2_DSA/metadata/D2_DSA_metadata.json`

**Contents and why it exists.** Retrieval metadata for D2_DSA. It was produced at the R4.1 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Corpus authenticity. Human-validated: YES. Frozen: YES. Role: SOURCE.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

### D2_DSA_structural_validation.json

**Folder:** `03_SOURCE_DATA_AND_CORPUS/source_metadata/` | **Phase:** R4.1 | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/02_sources/D2_DSA/validation/D2_DSA_structural_validation.json`

**Contents and why it exists.** Structural validation output for D2_DSA. It was produced at the R4.1 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Corpus integrity. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### D3_AI_ACT_metadata.json

**Folder:** `03_SOURCE_DATA_AND_CORPUS/source_metadata/` | **Phase:** R4.1 | **Type:** PROVENANCE | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/02_sources/D3_AI_ACT/metadata/D3_AI_ACT_metadata.json`

**Contents and why it exists.** Retrieval metadata for D3_AI_ACT. It was produced at the R4.1 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Corpus authenticity. Human-validated: YES. Frozen: YES. Role: SOURCE.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

### D3_AI_ACT_structural_validation.json

**Folder:** `03_SOURCE_DATA_AND_CORPUS/source_metadata/` | **Phase:** R4.1 | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/02_sources/D3_AI_ACT/validation/D3_AI_ACT_structural_validation.json`

**Contents and why it exists.** Structural validation output for D3_AI_ACT. It was produced at the R4.1 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Corpus integrity. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

---

## `04_R4_2_STRUCTURAL_EXTRACTION/`

### R4_2_AI_EXTRACTION_RUN_SUMMARY.csv

**Folder:** `04_R4_2_STRUCTURAL_EXTRACTION/` | **Phase:** R4.2 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/R4_2_AI_EXTRACTION_RUN_SUMMARY.csv`

**Contents and why it exists.** Run summary of the AI extraction pass. It was produced at the R4.2 stage by Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv.

**Model provenance.** Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv

**What it supports.** Extraction provenance. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2_HUMAN_QA_SAMPLE.csv

**Folder:** `04_R4_2_STRUCTURAL_EXTRACTION/` | **Phase:** R4.2 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/R4_2_HUMAN_QA_SAMPLE.csv`

**Contents and why it exists.** Initial human QA sample drawn from the extraction. It was produced at the R4.2 stage by Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv.

**Model provenance.** Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv

**What it supports.** QA design. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2_METHOD_NOTE.md

**Folder:** `04_R4_2_STRUCTURAL_EXTRACTION/` | **Phase:** R4.2 | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_2_METHOD_NOTE.md`

**Contents and why it exists.** Method note for the structural extraction stage. It was produced at the R4.2 stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** Extraction method. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### R4_2_SOURCE_COVERAGE_REPORT.csv

**Folder:** `04_R4_2_STRUCTURAL_EXTRACTION/` | **Phase:** R4.2 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/R4_2_SOURCE_COVERAGE_REPORT.csv`

**Contents and why it exists.** Coverage of the corpus by extracted records. It was produced at the R4.2 stage by Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv.

**Model provenance.** Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv

**What it supports.** Extraction completeness. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_CROSS_REFERENCE_REGISTER.csv

**Folder:** `04_R4_2_STRUCTURAL_EXTRACTION/` | **Phase:** R4.2 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/R4_CROSS_REFERENCE_REGISTER.csv`

**Contents and why it exists.** Cross-references between provisions. It was produced at the R4.2 stage by Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv.

**Model provenance.** Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv

**What it supports.** Provision linkage. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_DIGITAL_ACTOR_CANDIDATE_REGISTER.csv

**Folder:** `04_R4_2_STRUCTURAL_EXTRACTION/` | **Phase:** R4.2 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/R4_DIGITAL_ACTOR_CANDIDATE_REGISTER.csv`

**Contents and why it exists.** Candidate actors identified across the digital corpus. It was produced at the R4.2 stage by Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv.

**Model provenance.** Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv

**What it supports.** Actor variable. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_LEGAL_ACTION_REGISTER.csv

**Folder:** `04_R4_2_STRUCTURAL_EXTRACTION/` | **Phase:** R4.2 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/R4_LEGAL_ACTION_REGISTER.csv`

**Contents and why it exists.** Register of legal actions encountered. It was produced at the R4.2 stage by Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv.

**Model provenance.** Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv

**What it supports.** Action variable. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_LEGAL_DEFINITION_REGISTER.csv

**Folder:** `04_R4_2_STRUCTURAL_EXTRACTION/` | **Phase:** R4.2 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/R4_LEGAL_DEFINITION_REGISTER.csv`

**Contents and why it exists.** Legal definitions extracted from the instruments. It was produced at the R4.2 stage by Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv.

**Model provenance.** Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv

**What it supports.** Definitional grounding. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_STRUCTURAL_AMBIGUITY_LOG.csv

**Folder:** `04_R4_2_STRUCTURAL_EXTRACTION/` | **Phase:** R4.2 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/R4_STRUCTURAL_AMBIGUITY_LOG.csv`

**Contents and why it exists.** Log of structural ambiguities flagged at extraction. It was produced at the R4.2 stage by Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv.

**Model provenance.** Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv

**What it supports.** Ambiguity metadata. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

---

## `05_QA_AND_HUMAN_ADJUDICATION/`

### R4_2B_AMBIGUITY_TYPOLOGY.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2B_AMBIGUITY_TYPOLOGY.csv`

**Contents and why it exists.** Typology of ambiguity classes observed in QA. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** Ambiguity typology. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2B_CONFIDENCE_CALIBRATION.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2B_CONFIDENCE_CALIBRATION.csv`

**Contents and why it exists.** Calibration of extraction confidence against QA outcomes. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** Confidence flag reliability. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2B_EXTRACTION_CORRECTION_REGISTER.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2B_EXTRACTION_CORRECTION_REGISTER.csv`

**Contents and why it exists.** Corrections registered during R4.2B QA. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** QA corrections. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2B_HUMAN_CALIBRATION_SEED_V1.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2B_HUMAN_CALIBRATION_SEED_V1.csv`

**Contents and why it exists.** Seed set used to calibrate human QA. It was produced at the R4.2B / R4.2C stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human decision record)

**What it supports.** QA calibration. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### R4_2B_HUMAN_DECISION_REGISTER.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2B_HUMAN_DECISION_REGISTER.csv`

**Contents and why it exists.** Register of human QA decisions. It was produced at the R4.2B / R4.2C stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human decision record)

**What it supports.** Human authority over QA. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### R4_2B_HUMAN_QA_SAMPLE.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2B_HUMAN_QA_SAMPLE.csv`

**Contents and why it exists.** The stratified human QA sample. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** QA sampling design. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2B_HUMAN_REVIEW_SOURCE_MANIFEST.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** PROVENANCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2B_HUMAN_REVIEW_SOURCE_MANIFEST.csv`

**Contents and why it exists.** Manifest of sources used in human review. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** Review provenance. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Consult this to establish which model or person produced a given output, and when.

### R4_2B_LUNA_EXTRACTION_FREEZE_MANIFEST.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** FREEZE/INTEGRITY | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2B_LUNA_EXTRACTION_FREEZE_MANIFEST.csv`

**Contents and why it exists.** Freeze manifest for the Luna extraction output. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Luna (initial extraction/QA); see R4_AI_EXECUTION_LOG.csv

**What it supports.** Extraction freeze. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to verify that an artifact matches what was frozen at the time.

### R4_2B_QA_METRICS.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2B_QA_METRICS.csv`

**Contents and why it exists.** Quantitative QA metrics. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** QA results. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2B_QA_REPORT.md

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_2B_QA_REPORT.md`

**Contents and why it exists.** R4.2B QA report over the stratified sample. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** QA design and findings. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2B_SYSTEMATIC_ERROR_AUDIT.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2B_SYSTEMATIC_ERROR_AUDIT.csv`

**Contents and why it exists.** First systematic error audit. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** Error patterns. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2B_SYSTEMATIC_ERROR_AUDIT_UPDATED.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2B_SYSTEMATIC_ERROR_AUDIT_UPDATED.csv`

**Contents and why it exists.** Updated systematic error audit. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** Error patterns. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2C_HISTORICAL_OUTPUT_PRESERVATION_MANIFEST.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** FREEZE/INTEGRITY | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_HISTORICAL_OUTPUT_PRESERVATION_MANIFEST.csv`

**Contents and why it exists.** Manifest preserving superseded R4.2C outputs. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** Audit trail. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to verify that an artifact matches what was frozen at the time.

### R4_2C_LUNA_SELFREVIEW_TERRA_COMPARISON.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_LUNA_SELFREVIEW_TERRA_COMPARISON.csv`

**Contents and why it exists.** Comparison of Luna self-review against Terra review. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Cross-model comparison. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2C_LUNA_TERRA_QA_COMPARISON.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_LUNA_TERRA_QA_COMPARISON.csv`

**Contents and why it exists.** Luna versus Terra QA comparison table. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Cross-model comparison. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2C_MODEL_PROVENANCE_CORRECTION.md

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** PROVENANCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_MODEL_PROVENANCE_CORRECTION.md`

**Contents and why it exists.** Record of an earlier model-provenance correction in R4.2C. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** Provenance discipline. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Consult this to establish which model or person produced a given output, and when.

### R4_2C_OUTPUT_RECLASSIFICATION.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** PROVENANCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_OUTPUT_RECLASSIFICATION.csv`

**Contents and why it exists.** Reclassification of R4.2C outputs after provenance review. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** Provenance discipline. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Consult this to establish which model or person produced a given output, and when.

### R4_2C_R_PATTERN_CONFIRMATION.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_R_PATTERN_CONFIRMATION.csv`

**Contents and why it exists.** Confirmation of recurring patterns across models. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** Cross-model support. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2C_R_TRUE_TERRA_CALIBRATION_REPORT.md

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_R_TRUE_TERRA_CALIBRATION_REPORT.md`

**Contents and why it exists.** Calibration report for the true-Terra review. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Cross-model calibration. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2C_TARGETED_HUMAN_REVIEW_QUEUE.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_TARGETED_HUMAN_REVIEW_QUEUE.csv`

**Contents and why it exists.** Queue of cases routed to targeted human review. It was produced at the R4.2B / R4.2C stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human decision record)

**What it supports.** Human routing. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### R4_2C_TARGETED_HUMAN_REVIEW_QUEUE_V2.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_TARGETED_HUMAN_REVIEW_QUEUE_V2.csv`

**Contents and why it exists.** Second version of the targeted human review queue. It was produced at the R4.2B / R4.2C stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human decision record)

**What it supports.** Human routing. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### R4_2C_TERRA_BLIND_INPUT_V2.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_TERRA_BLIND_INPUT_V2.csv`

**Contents and why it exists.** Blind input presented to Terra in R4.2C v2. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Blind review design. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2C_TERRA_CALIBRATED_REVIEW.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_TERRA_CALIBRATED_REVIEW.csv`

**Contents and why it exists.** Terra calibrated review output. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Cross-model review. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2C_TERRA_CALIBRATION_AND_CLOSURE_REPORT.md

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_TERRA_CALIBRATION_AND_CLOSURE_REPORT.md`

**Contents and why it exists.** Closure report for the Terra calibration stage. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Cross-model closure. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2C_TERRA_INDEPENDENT_CALIBRATED_REVIEW_V2.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_TERRA_INDEPENDENT_CALIBRATED_REVIEW_V2.csv`

**Contents and why it exists.** Independent Terra calibrated review, v2. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Cross-model review. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2C_TERRA_INDEPENDENT_REVIEW_V2_FREEZE_MANIFEST.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** FREEZE/INTEGRITY | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2C_TERRA_INDEPENDENT_REVIEW_V2_FREEZE_MANIFEST.csv`

**Contents and why it exists.** Freeze manifest for the v2 Terra review. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Review freeze. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to verify that an artifact matches what was frozen at the time.

### R4_2_FINAL_CHECKPOINT.md

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_2_FINAL_CHECKPOINT.md`

**Contents and why it exists.** Checkpoint closing the R4.2 QA stage. It was produced at the R4.2B / R4.2C stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human decision record)

**What it supports.** Stage closure. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### R4_STRUCTURAL_EXTRACTION_QA_CALIBRATED.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/` | **Phase:** R4.2B / R4.2C | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/R4_STRUCTURAL_EXTRACTION_QA_CALIBRATED.csv`

**Contents and why it exists.** Extraction with calibrated QA annotations. It was produced at the R4.2B / R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** Mixed; see R4_AI_EXECUTION_LOG.csv

**What it supports.** QA-annotated extraction. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

---

## `05_QA_AND_HUMAN_ADJUDICATION/R4_2D_human_diagnostic/`

### R4_2D_CROSS_MODEL_DIAGNOSTIC_SAMPLE.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/R4_2D_human_diagnostic/` | **Phase:** R4.2D | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2D_CROSS_MODEL_DIAGNOSTIC_SAMPLE.csv`

**Contents and why it exists.** The 12 purposively selected cross-model-supported diagnostic cases. It was produced at the R4.2D stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human adjudication)

**What it supports.** Human diagnostic design. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/R4_2D_human_diagnostic/` | **Phase:** R4.2D | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2D_HUMAN_DIAGNOSTIC_COMPLETED.csv`

**Contents and why it exists.** Completed human adjudication of all 12 diagnostic cases. It was produced at the R4.2D stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human adjudication)

**What it supports.** Human root-cause findings. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### R4_2D_HUMAN_DIAGNOSTIC_PANEL.html

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/R4_2D_human_diagnostic/` | **Phase:** R4.2D | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2D_HUMAN_DIAGNOSTIC_PANEL.html`

**Contents and why it exists.** Offline adjudication panel used by the human researcher. It was produced at the R4.2D stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human adjudication)

**What it supports.** Human adjudication instrument. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### R4_2D_HUMAN_DIAGNOSTIC_REPORT.md

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/R4_2D_human_diagnostic/` | **Phase:** R4.2D | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2D_HUMAN_DIAGNOSTIC_REPORT.md`

**Contents and why it exists.** Narrative report of the human diagnostic. It was produced at the R4.2D stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human adjudication)

**What it supports.** Human root-cause findings. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### R4_2D_HUMAN_DIAGNOSTIC_RULE_CANDIDATES.md

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/R4_2D_human_diagnostic/` | **Phase:** R4.2D | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2D_HUMAN_DIAGNOSTIC_RULE_CANDIDATES.md`

**Contents and why it exists.** The 15 human-derived candidate structural rules. It was produced at the R4.2D stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human adjudication)

**What it supports.** 15 frozen rules. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### R4_2D_HUMAN_DIAGNOSTIC_SUMMARY.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/R4_2D_human_diagnostic/` | **Phase:** R4.2D | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2D_HUMAN_DIAGNOSTIC_SUMMARY.csv`

**Contents and why it exists.** Summary of the human diagnostic outcomes. It was produced at the R4.2D stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human adjudication)

**What it supports.** Human diagnostic results. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### README_R4_2D_HUMAN_DIAGNOSTIC.md

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/R4_2D_human_diagnostic/` | **Phase:** R4.2D | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/README_R4_2D_HUMAN_DIAGNOSTIC.md`

**Contents and why it exists.** Explanatory readme for the human diagnostic stage. It was produced at the R4.2D stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human adjudication)

**What it supports.** Human diagnostic method. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

---

## `05_QA_AND_HUMAN_ADJUDICATION/human_review_interface/`

### R4_2B_HUMAN_REVIEW_PANEL.html

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/human_review_interface/` | **Phase:** R4.2B | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/human_review/R4_2B_HUMAN_REVIEW_PANEL.html`

**Contents and why it exists.** Offline human review panel used in R4.2B. It was produced at the R4.2B stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human decision record)

**What it supports.** Human authority over QA. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### R4_2B_HUMAN_REVIEW_WORKING.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/human_review_interface/` | **Phase:** R4.2B | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/human_review/R4_2B_HUMAN_REVIEW_WORKING.csv`

**Contents and why it exists.** Working file behind the R4.2B human review. It was produced at the R4.2B stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human decision record)

**What it supports.** Human authority over QA. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

### README_HUMAN_REVIEW.md

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/human_review_interface/` | **Phase:** R4.2B | **Type:** HUMAN EVIDENCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/human_review/README_HUMAN_REVIEW.md`

**Contents and why it exists.** Readme for the human review interface. It was produced at the R4.2B stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a (human decision record)

**What it supports.** Human authority over QA. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to audit the human contribution: what the researcher decided and on what reasoning. These decisions govern where a model disagreed.

---

## `05_QA_AND_HUMAN_ADJUDICATION/r4_2c_working_copies/`

### R4_2C_LUNA_TERRA_QA_COMPARISON.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/r4_2c_working_copies/` | **Phase:** R4.2C | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/r4_2c/R4_2C_LUNA_TERRA_QA_COMPARISON.csv`

**Contents and why it exists.** Working-copy variant of the Luna/Terra comparison (differs from the qa/ root version). It was produced at the R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Cross-model comparison. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Byte-differs from the same-named file in the qa/ root; both preserved.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2C_TARGETED_HUMAN_REVIEW_QUEUE.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/r4_2c_working_copies/` | **Phase:** R4.2C | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/r4_2c/R4_2C_TARGETED_HUMAN_REVIEW_QUEUE.csv`

**Contents and why it exists.** Working-copy variant of the targeted review queue. It was produced at the R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Human routing. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Byte-differs from the same-named file in the qa/ root; both preserved.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2C_TERRA_CALIBRATED_REVIEW.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/r4_2c_working_copies/` | **Phase:** R4.2C | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/r4_2c/R4_2C_TERRA_CALIBRATED_REVIEW.csv`

**Contents and why it exists.** Working-copy variant of the Terra calibrated review. It was produced at the R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Cross-model review. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Byte-differs from the same-named file in the qa/ root; both preserved.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2C_TERRA_CALIBRATION_AND_CLOSURE_REPORT.md

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/r4_2c_working_copies/` | **Phase:** R4.2C | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/r4_2c/R4_2C_TERRA_CALIBRATION_AND_CLOSURE_REPORT.md`

**Contents and why it exists.** Working-copy variant of the calibration closure report. It was produced at the R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Cross-model closure. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Byte-differs from the same-named file in the qa/ root; both preserved.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2_FINAL_CHECKPOINT.md

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/r4_2c_working_copies/` | **Phase:** R4.2C | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/r4_2c/R4_2_FINAL_CHECKPOINT.md`

**Contents and why it exists.** Working-copy variant of the R4.2 checkpoint. It was produced at the R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Stage closure. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Byte-differs from the same-named file in the qa/ root; both preserved.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_STRUCTURAL_EXTRACTION_QA_CALIBRATED.csv

**Folder:** `05_QA_AND_HUMAN_ADJUDICATION/r4_2c_working_copies/` | **Phase:** R4.2C | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/r4_2c/R4_STRUCTURAL_EXTRACTION_QA_CALIBRATED.csv`

**Contents and why it exists.** Working-copy variant of the calibrated extraction. It was produced at the R4.2C stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** QA-annotated extraction. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Byte-differs from the same-named file in the qa/ root; both preserved.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

---

## `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_A_triage/`

### R4_2E_A_ACTOR_ACTION_REPAIR_AUDIT.csv

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_A_triage/` | **Phase:** R4.2E-A | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_A/R4_2E_A_ACTOR_ACTION_REPAIR_AUDIT.csv`

**Contents and why it exists.** Audit of actor/action fragmentation candidates. It was produced at the R4.2E-A stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Actor/action defects. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Deterministic heuristic; candidate signals, not confirmed defects.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_A_COUNTERPART_RECIPIENT_BURDEN_AUDIT.csv

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_A_triage/` | **Phase:** R4.2E-A | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_A/R4_2E_A_COUNTERPART_RECIPIENT_BURDEN_AUDIT.csv`

**Contents and why it exists.** Audit of the counterpart/recipient coding burden. It was produced at the R4.2E-A stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Counterpart/recipient finding. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Deterministic heuristic; candidate signals, not confirmed defects.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_A_HUMAN_CASE_RULE_REDISCOVERY.csv

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_A_triage/` | **Phase:** R4.2E-A | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_A/R4_2E_A_HUMAN_CASE_RULE_REDISCOVERY.csv`

**Contents and why it exists.** Which of the 12 human cases the heuristic rediscovered (9/12). It was produced at the R4.2E-A stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Heuristic blind spots. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Deterministic heuristic; candidate signals, not confirmed defects.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_A_METHOD_REPORT.md

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_A_triage/` | **Phase:** R4.2E-A | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_A/R4_2E_A_METHOD_REPORT.md`

**Contents and why it exists.** Method report for deterministic candidate triage over all 1,404 records. It was produced at the R4.2E-A stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Triage method. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Deterministic heuristic; candidate signals, not confirmed defects.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2E_A_NEW_RULE_CANDIDATES.csv

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_A_triage/` | **Phase:** R4.2E-A | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_A/R4_2E_A_NEW_RULE_CANDIDATES.csv`

**Contents and why it exists.** New rule candidates raised during triage. It was produced at the R4.2E-A stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Rule evolution. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Deterministic heuristic; candidate signals, not confirmed defects.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_A_REPAIR_CANDIDATE_REGISTER.csv

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_A_triage/` | **Phase:** R4.2E-A | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_A/R4_2E_A_REPAIR_CANDIDATE_REGISTER.csv`

**Contents and why it exists.** Per-record triage classification (YES 713 / UNCERTAIN 346 / NO 345). It was produced at the R4.2E-A stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Candidate signals. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Deterministic heuristic; candidate signals, not confirmed defects.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_A_REPAIR_CANDIDATE_SUMMARY.csv

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_A_triage/` | **Phase:** R4.2E-A | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_A/R4_2E_A_REPAIR_CANDIDATE_SUMMARY.csv`

**Contents and why it exists.** Aggregate triage counts and complexity distribution. It was produced at the R4.2E-A stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Triage results. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Deterministic heuristic; candidate signals, not confirmed defects.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

---

## `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_B0_compression/`

### R4_2E_B0_COMPRESSION_SUMMARY.csv

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_B0_compression/` | **Phase:** R4.2E-B0 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B0/R4_2E_B0_COMPRESSION_SUMMARY.csv`

**Contents and why it exists.** Compression metrics: 211 families; advanced workload 524 to 131. It was produced at the R4.2E-B0 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Compression results. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B0_FREEZE_RECORD.md

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_B0_compression/` | **Phase:** R4.2E-B0 | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B0/R4_2E_B0_FREEZE_RECORD.md`

**Contents and why it exists.** Freeze record for the B0 compression stage. It was produced at the R4.2E-B0 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Stage freeze. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2E_B0_HEURISTIC_BLIND_SPOTS.md

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_B0_compression/` | **Phase:** R4.2E-B0 | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B0/R4_2E_B0_HEURISTIC_BLIND_SPOTS.md`

**Contents and why it exists.** Documented blind spots of the triage heuristic. It was produced at the R4.2E-B0 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Known limitations. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2E_B0_METHOD_REPORT.md

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_B0_compression/` | **Phase:** R4.2E-B0 | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B0/R4_2E_B0_METHOD_REPORT.md`

**Contents and why it exists.** Method report for repair-family compression. It was produced at the R4.2E-B0 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Compression method. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2E_B0_MODEL_REPRESENTATIVE_SAMPLE.csv

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_B0_compression/` | **Phase:** R4.2E-B0 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B0/R4_2E_B0_MODEL_REPRESENTATIVE_SAMPLE.csv`

**Contents and why it exists.** Representatives selected for advanced review. It was produced at the R4.2E-B0 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Representative selection. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B0_NEW_DETECTION_RULE_CANDIDATES.csv

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_B0_compression/` | **Phase:** R4.2E-B0 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B0/R4_2E_B0_NEW_DETECTION_RULE_CANDIDATES.csv`

**Contents and why it exists.** New detection rule candidates from B0. It was produced at the R4.2E-B0 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Rule evolution. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B0_OBJECT_TRIGGER_TYPOLOGY.csv

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_B0_compression/` | **Phase:** R4.2E-B0 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B0/R4_2E_B0_OBJECT_TRIGGER_TYPOLOGY.csv`

**Contents and why it exists.** Typology of object-field residual-bucket triggers. It was produced at the R4.2E-B0 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Object variable defects. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B0_RELATIONAL_FIELD_STRATEGY.md

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_B0_compression/` | **Phase:** R4.2E-B0 | **Type:** QA | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B0/R4_2E_B0_RELATIONAL_FIELD_STRATEGY.md`

**Contents and why it exists.** Frozen strategy for evaluating counterpart and recipient separately. It was produced at the R4.2E-B0 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Counterpart/recipient method. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this to see how quality was assessed at that stage and what it found.

### R4_2E_B0_REPAIR_FAMILY_REGISTER.csv

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_B0_compression/` | **Phase:** R4.2E-B0 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B0/R4_2E_B0_REPAIR_FAMILY_REGISTER.csv`

**Contents and why it exists.** The 211 repair families with sizes and routes. It was produced at the R4.2E-B0 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Family definitions and coverage. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B0_REPAIR_SIGNATURE_REGISTER.csv

**Folder:** `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_B0_compression/` | **Phase:** R4.2E-B0 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B0/R4_2E_B0_REPAIR_SIGNATURE_REGISTER.csv`

**Contents and why it exists.** Per-record structural signature and assigned repair route. It was produced at the R4.2E-B0 stage by Deterministic script (no model inference).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Route assignment. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

---

## `07_ADVANCED_VALIDATION_B1/batch_outputs/`

### R4_2E_B1_ADVANCED_VALIDATION.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/batch_outputs/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ADVANCED_VALIDATION.csv`

**Contents and why it exists.** B1-01 authoritative output, 36 cases. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** B1 results. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Authoritative v2.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

### R4_2E_B1_ADVANCED_VALIDATION_B1_02.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/batch_outputs/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ADVANCED_VALIDATION_B1_02.csv`

**Contents and why it exists.** B1-02 authoritative output, 36 cases. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** B1 results. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

### R4_2E_B1_ADVANCED_VALIDATION_B1_03.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/batch_outputs/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ADVANCED_VALIDATION_B1_03.csv`

**Contents and why it exists.** B1-03 authoritative output, 36 cases. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** B1 results. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

### R4_2E_B1_ADVANCED_VALIDATION_B1_04.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/batch_outputs/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ADVANCED_VALIDATION_B1_04.csv`

**Contents and why it exists.** B1-04 authoritative output, 35 cases. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** B1 results. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Provenance-corrected authoritative version.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

---

## `07_ADVANCED_VALIDATION_B1/combined_reports/`

### R4_2E_B1_BATCH_RUN_LOG.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/combined_reports/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_BATCH_RUN_LOG.csv`

**Contents and why it exists.** Run log for all four batches with input/output hashes and provenance. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED) + Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** Execution provenance. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B1_FAMILY_TEMPLATE_VALIDATION.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/combined_reports/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_FAMILY_TEMPLATE_VALIDATION.csv`

**Contents and why it exists.** Family template validation detail from B1-01. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Template status. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B1_FINAL_SUMMARY.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/combined_reports/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_FINAL_SUMMARY.csv`

**Contents and why it exists.** Consolidated metrics across all 143 cases. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED) + Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** All combined B1 findings. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B1_HANDOFF_STATE.md

**Folder:** `07_ADVANCED_VALIDATION_B1/combined_reports/` | **Phase:** R4.2E-B1 | **Type:** FREEZE/INTEGRITY | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_HANDOFF_STATE.md`

**Contents and why it exists.** Final B1 handoff state and unresolved questions. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED) + Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** Current status. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to verify that an artifact matches what was frozen at the time.

### R4_2E_B1_INDIVIDUAL_CASE_DECISIONS.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/combined_reports/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_INDIVIDUAL_CASE_DECISIONS.csv`

**Contents and why it exists.** Individual advanced case routing from B1-01. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Individual routes. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B1_METHOD_REPORT.md

**Folder:** `07_ADVANCED_VALIDATION_B1/combined_reports/` | **Phase:** R4.2E-B1 | **Type:** FREEZE/INTEGRITY | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_METHOD_REPORT.md`

**Contents and why it exists.** Full B1 method report including the sensitivity audit and B0 decision. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED) + Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** All B1 findings. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to verify that an artifact matches what was frozen at the time.

### R4_2E_B1_NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATES.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/combined_reports/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATES.csv`

**Contents and why it exists.** Seven new structural diagnostic candidates recorded for adjudication. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** Rule evolution. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** The 15 frozen rules were not modified.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B1_RELATIONAL_FIELD_DIFFERENTIATION.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/combined_reports/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_RELATIONAL_FIELD_DIFFERENTIATION.csv`

**Contents and why it exists.** Relational differentiation detail from B1-01. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Counterpart/recipient finding. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

---

## `07_ADVANCED_VALIDATION_B1/design/`

### R4_2E_B1_BATCH_ALLOCATION_FREEZE.md

**Folder:** `07_ADVANCED_VALIDATION_B1/design/` | **Phase:** R4.2E-B1 | **Type:** FREEZE/INTEGRITY | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_BATCH_ALLOCATION_FREEZE.md`

**Contents and why it exists.** Frozen allocation of the 143 cases into four batches. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** Deterministic script (no model inference)

**What it supports.** B1 design. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to verify that an artifact matches what was frozen at the time.

### R4_2E_B1_BATCH_MANIFEST.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/design/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_BATCH_MANIFEST.csv`

**Contents and why it exists.** Case-level batch manifest. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** Deterministic script (no model inference)

**What it supports.** B1 design. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B1_BLIND_SUBSTANTIVE_REVIEW_INPUT.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/design/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_BLIND_SUBSTANTIVE_REVIEW_INPUT.csv`

**Contents and why it exists.** The exact input shown to reviewers for all 143 cases. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Review input; schema under-exposure finding. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Exposes LEGAL_ACTION only; see the sensitivity audit.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

---

## `07_ADVANCED_VALIDATION_B1/diagnostic_controls/`

### R4_2E_B1_CONTROL_DIAGNOSTIC_CONSOLIDATED.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/diagnostic_controls/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_CONTROL_DIAGNOSTIC_CONSOLIDATED.csv`

**Contents and why it exists.** All 12 controls consolidated with type and severity. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED) + Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** B0 compression safety. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B1_NO_REPAIR_CONTROL_RESULTS.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/diagnostic_controls/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_NO_REPAIR_CONTROL_RESULTS.csv`

**Contents and why it exists.** B1-01 control results. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Control diagnostic. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_02.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/diagnostic_controls/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_02.csv`

**Contents and why it exists.** B1-02 control results. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Control diagnostic. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_03.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/diagnostic_controls/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_03.csv`

**Contents and why it exists.** B1-03 control results. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Control diagnostic. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_04.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/diagnostic_controls/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_NO_REPAIR_CONTROL_RESULTS_B1_04.csv`

**Contents and why it exists.** B1-04 control results. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** Control diagnostic. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

### R4_2E_B1_NO_REPAIR_CONTROL_SAMPLE.csv

**Folder:** `07_ADVANCED_VALIDATION_B1/diagnostic_controls/` | **Phase:** R4.2E-B1 | **Type:** MODEL OUTPUT | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_NO_REPAIR_CONTROL_SAMPLE.csv`

**Contents and why it exists.** The 12 NO_REPAIR diagnostic controls as selected before review. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Control design. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** Lists all 12 with no batch column; this is why blinding was not guaranteed.

**How to use it.** Supporting model output. Read it alongside the method report for the stage rather than on its own.

---

## `07_ADVANCED_VALIDATION_B1/freeze_records/`

### R4_2E_B1_BATCH_01_FREEZE_RECORD.md

**Folder:** `07_ADVANCED_VALIDATION_B1/freeze_records/` | **Phase:** R4.2E-B1 | **Type:** FREEZE/INTEGRITY | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_BATCH_01_FREEZE_RECORD.md`

**Contents and why it exists.** B1-01 freeze record. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Batch freeze. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to verify that an artifact matches what was frozen at the time.

### R4_2E_B1_BATCH_02_FREEZE_RECORD.md

**Folder:** `07_ADVANCED_VALIDATION_B1/freeze_records/` | **Phase:** R4.2E-B1 | **Type:** FREEZE/INTEGRITY | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_BATCH_02_FREEZE_RECORD.md`

**Contents and why it exists.** B1-02 freeze record. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Batch freeze. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to verify that an artifact matches what was frozen at the time.

### R4_2E_B1_BATCH_03_FREEZE_RECORD.md

**Folder:** `07_ADVANCED_VALIDATION_B1/freeze_records/` | **Phase:** R4.2E-B1 | **Type:** FREEZE/INTEGRITY | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_BATCH_03_FREEZE_RECORD.md`

**Contents and why it exists.** B1-03 freeze record. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** GPT-5.6 Terra High (MODEL_VARIANT_NOT_EXPOSED)

**What it supports.** Batch freeze. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to verify that an artifact matches what was frozen at the time.

### R4_2E_B1_BATCH_04_FREEZE_RECORD.md

**Folder:** `07_ADVANCED_VALIDATION_B1/freeze_records/` | **Phase:** R4.2E-B1 | **Type:** FREEZE/INTEGRITY | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_BATCH_04_FREEZE_RECORD.md`

**Contents and why it exists.** B1-04 freeze record, with corrected provenance and recorded design limitations. It was produced at the R4.2E-B1 stage by AI-assisted, human-supervised.

**Model provenance.** Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** Batch freeze; blinding limitation. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to verify that an artifact matches what was frozen at the time.

---

## `08_ACTION_SENSITIVITY_AUDIT/`

### R4_2E_B1_ACTION_SENSITIVITY_AUDIT.csv

**Folder:** `08_ACTION_SENSITIVITY_AUDIT/` | **Phase:** R4.2E-B1S | **Type:** MODEL OUTPUT | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ACTION_SENSITIVITY_AUDIT.csv`

**Contents and why it exists.** Per-case re-examination of all 143 Action judgments against LEGAL_ACTION + LEGAL_VERB + MODALITY. It was produced at the R4.2E-B1S stage by AI-assisted, human-supervised.

**Model provenance.** Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** Action 87 vs 63; 26 changed; 1/143 material. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

### R4_2E_B1_ACTION_SENSITIVITY_SUMMARY.csv

**Folder:** `08_ACTION_SENSITIVITY_AUDIT/` | **Phase:** R4.2E-B1S | **Type:** MODEL OUTPUT | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ACTION_SENSITIVITY_SUMMARY.csv`

**Contents and why it exists.** Aggregate metrics for the sensitivity audit, reporting frozen and adjusted counts side by side. It was produced at the R4.2E-B1S stage by AI-assisted, human-supervised.

**Model provenance.** Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** Action sensitivity result. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

### R4_VARIABLE_REDUNDANCY_AUDIT.csv

**Folder:** `08_ACTION_SENSITIVITY_AUDIT/` | **Phase:** R4.2E-B1S | **Type:** MODEL OUTPUT | **Status:** AUTHORITATIVE_SOURCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/08_reports/R4_VARIABLE_REDUNDANCY_AUDIT.csv`

**Contents and why it exists.** Five variable pairs with recomputed overlap, exactness, direction and parsimony status. It was produced at the R4.2E-B1S stage by Deterministic script (no model inference) with interpretation.

**Model provenance.** Claude: RESEARCHER_SELECTED_MODEL=Claude Opus 5.5 Extra High; RUNTIME_REPORTED_MODEL=Claude Opus 5; RUNTIME_MODEL_ID=claude-opus-5; MODEL_SELECTION_RUNTIME_MATCH=NOT_VERIFIABLE

**What it supports.** Variable parsimony findings. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**How to use it.** Use this to check any downstream claim against the underlying data. It is frozen, so figures quoted elsewhere should reconcile exactly against it.

---

## `09_MODEL_PROVENANCE/`

### R4_AI_EXECUTION_LOG.csv

**Folder:** `09_MODEL_PROVENANCE/` | **Phase:** R4 (all stages) | **Type:** PROVENANCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_AI_EXECUTION_LOG.csv`

**Contents and why it exists.** Log of every AI execution across R4 with model and purpose. It was produced at the R4 (all stages) stage by Igor Caires Machado (human researcher).

**Model provenance.** Mixed; see file

**What it supports.** Model provenance. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Consult this to establish which model or person produced a given output, and when.

### R4_GIT_SYNC_LOG.md

**Folder:** `09_MODEL_PROVENANCE/` | **Phase:** R4 (all stages) | **Type:** PROVENANCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/R4_GIT_SYNC_LOG.md`

**Contents and why it exists.** Log of repository synchronisation events. It was produced at the R4 (all stages) stage by Igor Caires Machado (human researcher).

**Model provenance.** Mixed; see file

**What it supports.** Version provenance. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Consult this to establish which model or person produced a given output, and when.

### R4_MODEL_ESCALATION_LOG.csv

**Folder:** `09_MODEL_PROVENANCE/` | **Phase:** R4 (all stages) | **Type:** PROVENANCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_MODEL_ESCALATION_LOG.csv`

**Contents and why it exists.** Record of model escalations and changes during R4. It was produced at the R4 (all stages) stage by Igor Caires Machado (human researcher).

**Model provenance.** Mixed; see file

**What it supports.** Model provenance. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Consult this to establish which model or person produced a given output, and when.

### R4_SESSION_CHECKPOINT_2026-09-26.md

**Folder:** `09_MODEL_PROVENANCE/` | **Phase:** R4 (all stages) | **Type:** PROVENANCE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/R4_SESSION_CHECKPOINT_2026-09-26.md`

**Contents and why it exists.** Session checkpoint preceding the final rounds. It was produced at the R4 (all stages) stage by Igor Caires Machado (human researcher).

**Model provenance.** Mixed; see file

**What it supports.** Execution continuity. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Consult this to establish which model or person produced a given output, and when.

---

## `10_FREEZE_AND_INTEGRITY/`

### R4_BASELINE_FREEZE_RECORD.md

**Folder:** `10_FREEZE_AND_INTEGRITY/` | **Phase:** R4 (freeze) | **Type:** FREEZE/INTEGRITY | **Status:** AUTHORITATIVE_FINAL

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_BASELINE_FREEZE_RECORD.md`

**Contents and why it exists.** Freeze record for the R4 baseline (R3 reconciliation). It was produced at the R4 (freeze) stage by Igor Caires Machado (human researcher).

**Model provenance.** Mixed; see file

**What it supports.** Baseline integrity. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this directly. It is a final deliverable of the round.

### R4_DIGITAL_STRUCTURAL_VALIDATION_FREEZE_RECORD.md

**Folder:** `10_FREEZE_AND_INTEGRITY/` | **Phase:** R4 (freeze) | **Type:** FREEZE/INTEGRITY | **Status:** AUTHORITATIVE_FINAL

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/08_reports/R4_DIGITAL_STRUCTURAL_VALIDATION_FREEZE_RECORD.md`

**Contents and why it exists.** Final freeze record for the whole R4 digital structural-validation round. It was produced at the R4 (freeze) stage by Igor Caires Machado (human researcher).

**Model provenance.** Mixed; see file

**What it supports.** Final status and all findings. Human-validated: YES. Frozen: YES. Role: FINAL.

**How to use it.** Read this directly. It is a final deliverable of the round.

### R4_DIGITAL_STRUCTURAL_VALIDATION_MANIFEST.csv

**Folder:** `10_FREEZE_AND_INTEGRITY/` | **Phase:** R4 (freeze) | **Type:** FREEZE/INTEGRITY | **Status:** AUTHORITATIVE_FINAL

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/08_reports/R4_DIGITAL_STRUCTURAL_VALIDATION_MANIFEST.csv`

**Contents and why it exists.** SHA-256 manifest of the 24 final scientific artifacts. It was produced at the R4 (freeze) stage by Igor Caires Machado (human researcher).

**Model provenance.** Mixed; see file

**What it supports.** Integrity verification. Human-validated: YES. Frozen: YES. Role: FINAL.

**How to use it.** Read this directly. It is a final deliverable of the round.

### R4_PRE_R4_2_CHECKPOINT.md

**Folder:** `10_FREEZE_AND_INTEGRITY/` | **Phase:** R4 (freeze) | **Type:** FREEZE/INTEGRITY | **Status:** AUTHORITATIVE_FINAL

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_PRE_R4_2_CHECKPOINT.md`

**Contents and why it exists.** Checkpoint immediately before structural extraction. It was produced at the R4 (freeze) stage by Igor Caires Machado (human researcher).

**Model provenance.** Mixed; see file

**What it supports.** Stage boundary. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Read this directly. It is a final deliverable of the round.

---

## `10_FREEZE_AND_INTEGRITY/superseded_preserved/`

### R4_2E_B1_ACTION_SENSITIVITY_AUDIT_v1_PROVENANCE_SUPERSEDED.csv

**Folder:** `10_FREEZE_AND_INTEGRITY/superseded_preserved/` | **Phase:** R4.2E-B1 / B1S | **Type:** SUPPORTING ARCHIVE | **Status:** SUPERSEDED_PRESERVED

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ACTION_SENSITIVITY_AUDIT_v1_PROVENANCE_SUPERSEDED.csv`

**Contents and why it exists.** Sensitivity audit before the Claude provenance correction. It was produced at the R4.2E-B1 / B1S stage by AI-assisted, human-supervised.

**Model provenance.** See authoritative counterpart

**What it supports.** Audit trail. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** NOT AUTHORITATIVE - PRESERVED FOR AUDIT TRAIL. Same provenance-correction chain. Substantive cells identical to the authoritative version.

**How to use it.** Do not use as data. Read it only to audit the incident it documents; the authoritative counterpart is in folders 01 to 09.

### R4_2E_B1_ADVANCED_VALIDATION_B1_01_v1_SCHEMA_DEFECT.csv

**Folder:** `10_FREEZE_AND_INTEGRITY/superseded_preserved/` | **Phase:** R4.2E-B1 / B1S | **Type:** SUPPORTING ARCHIVE | **Status:** SUPERSEDED_PRESERVED

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ADVANCED_VALIDATION_B1_01_v1_SCHEMA_DEFECT.csv`

**Contents and why it exists.** First B1-01 export, malformed by separators inside note fields. It was produced at the R4.2E-B1 / B1S stage by AI-assisted, human-supervised.

**Model provenance.** See authoritative counterpart

**What it supports.** Audit trail. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** NOT AUTHORITATIVE - PRESERVED FOR AUDIT TRAIL. Preserved because it documents the CSV schema incident that led to library-based CSV writing.

**How to use it.** Do not use as data. Read it only to audit the incident it documents; the authoritative counterpart is in folders 01 to 09.

### R4_2E_B1_ADVANCED_VALIDATION_B1_04_v1_PROVENANCE_SUPERSEDED.csv

**Folder:** `10_FREEZE_AND_INTEGRITY/superseded_preserved/` | **Phase:** R4.2E-B1 / B1S | **Type:** SUPPORTING ARCHIVE | **Status:** SUPERSEDED_PRESERVED

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_ADVANCED_VALIDATION_B1_04_v1_PROVENANCE_SUPERSEDED.csv`

**Contents and why it exists.** B1-04 export before the Claude provenance correction. It was produced at the R4.2E-B1 / B1S stage by AI-assisted, human-supervised.

**Model provenance.** See authoritative counterpart

**What it supports.** Audit trail. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** NOT AUTHORITATIVE - PRESERVED FOR AUDIT TRAIL. Preserved as part of the recorded provenance-correction chain. Substantive cells are identical to the authoritative version.

**How to use it.** Do not use as data. Read it only to audit the incident it documents; the authoritative counterpart is in folders 01 to 09.

### R4_2E_B1_FAMILY_TEMPLATE_VALIDATION_B1_01_v1_SCHEMA_DEFECT.csv

**Folder:** `10_FREEZE_AND_INTEGRITY/superseded_preserved/` | **Phase:** R4.2E-B1 / B1S | **Type:** SUPPORTING ARCHIVE | **Status:** SUPERSEDED_PRESERVED

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_FAMILY_TEMPLATE_VALIDATION_B1_01_v1_SCHEMA_DEFECT.csv`

**Contents and why it exists.** Companion malformed B1-01 template export. It was produced at the R4.2E-B1 / B1S stage by AI-assisted, human-supervised.

**Model provenance.** See authoritative counterpart

**What it supports.** Audit trail. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** NOT AUTHORITATIVE - PRESERVED FOR AUDIT TRAIL. Same schema incident.

**How to use it.** Do not use as data. Read it only to audit the incident it documents; the authoritative counterpart is in folders 01 to 09.

### R4_2E_B1_INDIVIDUAL_CASE_DECISIONS_B1_01_v1_SCHEMA_DEFECT.csv

**Folder:** `10_FREEZE_AND_INTEGRITY/superseded_preserved/` | **Phase:** R4.2E-B1 / B1S | **Type:** SUPPORTING ARCHIVE | **Status:** SUPERSEDED_PRESERVED

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/03_extraction/qa/repair/R4_2E_B1/R4_2E_B1_INDIVIDUAL_CASE_DECISIONS_B1_01_v1_SCHEMA_DEFECT.csv`

**Contents and why it exists.** Companion malformed B1-01 individual-case export. It was produced at the R4.2E-B1 / B1S stage by AI-assisted, human-supervised.

**Model provenance.** See authoritative counterpart

**What it supports.** Audit trail. Human-validated: PARTIAL. Frozen: YES. Role: SUPPORTING.

**Note.** NOT AUTHORITATIVE - PRESERVED FOR AUDIT TRAIL. Same schema incident.

**How to use it.** Do not use as data. Read it only to audit the incident it documents; the authoritative counterpart is in folders 01 to 09.

---

## `11_REPRODUCIBILITY/`

### apply_r4_claude_provenance_correction.py

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/apply_r4_claude_provenance_correction.py`

**Contents and why it exists.** Applies the Claude provenance correction with byte verification. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_envio_r4_docs.py

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_envio_r4_docs.py`

**Contents and why it exists.** Generates this package's section READMEs and the per-file guide from the traceability map. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_envio_r4_manifest.py

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_envio_r4_manifest.py`

**Contents and why it exists.** Writes the package note and the package manifest, and verifies every copy against its source hash. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_envio_r4_to_david_package.py

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_envio_r4_to_david_package.py`

**Contents and why it exists.** Builds this delivery package. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_1_structural_corpus.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_1_structural_corpus.ps1`

**Contents and why it exists.** Builds the frozen digital corpus and structural index. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2_history_inventory.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2_history_inventory.ps1`

**Contents and why it exists.** Inventories the R3 history brought into R4. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2_structural_extraction.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2_structural_extraction.ps1`

**Contents and why it exists.** Produces the 1,404-record structural extraction. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2b_human_review_interface.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2b_human_review_interface.ps1`

**Contents and why it exists.** Generates the offline human review panel. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2b_qa_package.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2b_qa_package.ps1`

**Contents and why it exists.** Builds the R4.2B QA package and metrics. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2c_calibrated_qa.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2c_calibrated_qa.ps1`

**Contents and why it exists.** Builds the R4.2C calibrated QA comparison. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2cr_true_terra_review.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2cr_true_terra_review.ps1`

**Contents and why it exists.** Builds the independent true-Terra review inputs. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2d_human_diagnostic_completed.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2d_human_diagnostic_completed.ps1`

**Contents and why it exists.** Assembles the completed human diagnostic record. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2d_human_diagnostic_panel.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2d_human_diagnostic_panel.ps1`

**Contents and why it exists.** Generates the human diagnostic adjudication panel. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2e_a_repair_candidate_identification.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2e_a_repair_candidate_identification.ps1`

**Contents and why it exists.** Runs deterministic triage over all 1,404 records. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2e_b0_repair_strategy_compression.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2e_b0_repair_strategy_compression.ps1`

**Contents and why it exists.** Builds the 211 repair families and routes. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2e_b1_batch01_validation.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2e_b1_batch01_validation.ps1`

**Contents and why it exists.** Writes the B1-01 validation output. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2e_b1_batch02_validation.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2e_b1_batch02_validation.ps1`

**Contents and why it exists.** Writes the B1-02 validation output. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2e_b1_batch03_control_results.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2e_b1_batch03_control_results.ps1`

**Contents and why it exists.** Unblinds and records the B1-03 diagnostic controls. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2e_b1_batch03_validation.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2e_b1_batch03_validation.ps1`

**Contents and why it exists.** Writes the B1-03 validation output. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2e_b1_batch04_control_results.py

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2e_b1_batch04_control_results.py`

**Contents and why it exists.** Unblinds and records the B1-04 diagnostic controls. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2e_b1_batch04_validation.py

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2e_b1_batch04_validation.py`

**Contents and why it exists.** Writes the B1-04 validation output with schema gates. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2e_b1_batch_allocation.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2e_b1_batch_allocation.ps1`

**Contents and why it exists.** Allocates the 143 cases into four batches. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2e_b1_final_consolidation.py

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2e_b1_final_consolidation.py`

**Contents and why it exists.** Reconciles all 143 cases and the 12 controls. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2e_b1_new_diagnostic_candidates.py

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2e_b1_new_diagnostic_candidates.py`

**Contents and why it exists.** Records the new structural diagnostic candidates. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_2e_b1s_action_sensitivity_audit.py

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_2e_b1s_action_sensitivity_audit.py`

**Contents and why it exists.** Runs the Action representation sensitivity audit. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_david_summary.py

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_david_summary.py`

**Contents and why it exists.** Builds the David-facing summary table. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_final_manifest.py

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_final_manifest.py`

**Contents and why it exists.** Builds the SHA-256 manifest of final artifacts. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### build_r4_variable_redundancy_audit.py

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/build_r4_variable_redundancy_audit.py`

**Contents and why it exists.** Recomputes the five variable-pair redundancy findings. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

### close_r4_2e_b1_batch01.ps1

**Folder:** `11_REPRODUCIBILITY/` | **Phase:** R4 (tooling) | **Type:** REPRODUCIBILITY | **Status:** REPRODUCIBILITY_SUPPORT

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/09_logs/close_r4_2e_b1_batch01.ps1`

**Contents and why it exists.** Closes and freezes B1-01. It was produced at the R4 (tooling) stage by Igor Caires Machado (human researcher).

**Model provenance.** Deterministic script (no model inference)

**What it supports.** Reproducibility. Human-validated: YES. Frozen: NO. Role: SUPPORTING.

**How to use it.** Re-run it against the frozen inputs to regenerate the deterministic outputs. For batch scripts this replays recorded decisions rather than regenerating them.

---

## `12_ARCHIVE_SUPPORT/`

### PROTOCOLO_USO_IA_R1_R3_PRE_R4_v1_1.docx

**Folder:** `12_ARCHIVE_SUPPORT/` | **Phase:** R4.0 / protocol | **Type:** SUPPORTING ARCHIVE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/00_protocol/PROTOCOLO_USO_IA_R1_R3_PRE_R4_v1_1.docx`

**Contents and why it exists.** Researcher protocol governing AI use across R1 to R3. It was produced at the R4.0 / protocol stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** AI-use governance. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Background material; consult it if you are auditing how the round was set up.

### R4_INITIAL_METHOD_NOTE.md

**Folder:** `12_ARCHIVE_SUPPORT/` | **Phase:** R4.0 / protocol | **Type:** SUPPORTING ARCHIVE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_INITIAL_METHOD_NOTE.md`

**Contents and why it exists.** Initial R4 method note setting out the research question. It was produced at the R4.0 / protocol stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** R4 design. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Background material; consult it if you are auditing how the round was set up.

### R4_INITIAL_SETUP_PROMPT_VERBATIM.txt

**Folder:** `12_ARCHIVE_SUPPORT/` | **Phase:** R4.0 / protocol | **Type:** SUPPORTING ARCHIVE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/00_protocol/R4_INITIAL_SETUP_PROMPT_VERBATIM.txt`

**Contents and why it exists.** Verbatim initial setup instruction for R4. It was produced at the R4.0 / protocol stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** AI-use transparency. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Background material; consult it if you are auditing how the round was set up.

### R4_PREEXISTING_R4_2_CHANGE_AUDIT.csv

**Folder:** `12_ARCHIVE_SUPPORT/` | **Phase:** R4.0 / protocol | **Type:** SUPPORTING ARCHIVE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_PREEXISTING_R4_2_CHANGE_AUDIT.csv`

**Contents and why it exists.** Audit of pre-existing changes before R4.2 began. It was produced at the R4.0 / protocol stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** Change control. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Background material; consult it if you are auditing how the round was set up.

### R4_R3_BASELINE_MANIFEST.md

**Folder:** `12_ARCHIVE_SUPPORT/` | **Phase:** R4.0 / protocol | **Type:** SUPPORTING ARCHIVE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_R3_BASELINE_MANIFEST.md`

**Contents and why it exists.** Manifest of the frozen R3 green baseline. It was produced at the R4.0 / protocol stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** Green baseline. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Background material; consult it if you are auditing how the round was set up.

### R4_R3_HISTORICAL_INTEGRATION_REPORT.md

**Folder:** `12_ARCHIVE_SUPPORT/` | **Phase:** R4.0 / protocol | **Type:** SUPPORTING ARCHIVE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_R3_HISTORICAL_INTEGRATION_REPORT.md`

**Contents and why it exists.** Report on integrating R3 history into R4. It was produced at the R4.0 / protocol stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** Baseline continuity. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Background material; consult it if you are auditing how the round was set up.

### R4_R3_HISTORY_ARCHIVE_METADATA.json

**Folder:** `12_ARCHIVE_SUPPORT/` | **Phase:** R4.0 / protocol | **Type:** SUPPORTING ARCHIVE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_R3_HISTORY_ARCHIVE_METADATA.json`

**Contents and why it exists.** Metadata for the R3 history archive. It was produced at the R4.0 / protocol stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** Archive provenance. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Background material; consult it if you are auditing how the round was set up.

### R4_R3_HISTORY_FILE_INVENTORY.csv

**Folder:** `12_ARCHIVE_SUPPORT/` | **Phase:** R4.0 / protocol | **Type:** SUPPORTING ARCHIVE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_R3_HISTORY_FILE_INVENTORY.csv`

**Contents and why it exists.** Inventory of archived R3 history files. It was produced at the R4.0 / protocol stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** Archive completeness. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Background material; consult it if you are auditing how the round was set up.

### R4_R3_RECONCILIATION.csv

**Folder:** `12_ARCHIVE_SUPPORT/` | **Phase:** R4.0 / protocol | **Type:** SUPPORTING ARCHIVE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_R3_RECONCILIATION.csv`

**Contents and why it exists.** Reconciliation of R3 totals brought into R4. It was produced at the R4.0 / protocol stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** Green baseline totals. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Background material; consult it if you are auditing how the round was set up.

### R4_R3_TO_R4_INTEGRATION_MAP.csv

**Folder:** `12_ARCHIVE_SUPPORT/` | **Phase:** R4.0 / protocol | **Type:** SUPPORTING ARCHIVE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/R4_R3_TO_R4_INTEGRATION_MAP.csv`

**Contents and why it exists.** Mapping from R3 artifacts to R4 structures. It was produced at the R4.0 / protocol stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** Baseline continuity. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Background material; consult it if you are auditing how the round was set up.

### R4_WORKSPACE_STRUCTURE.md

**Folder:** `12_ARCHIVE_SUPPORT/` | **Phase:** R4.0 / protocol | **Type:** SUPPORTING ARCHIVE | **Status:** SUPPORTING_EVIDENCE

**Origin:** `R4_CROSS_DOMAIN_VALIDATION/00_protocol/R4_WORKSPACE_STRUCTURE.md`

**Contents and why it exists.** Definition of the R4 workspace structure. It was produced at the R4.0 / protocol stage by Igor Caires Machado (human researcher).

**Model provenance.** n/a

**What it supports.** Project organisation. Human-validated: YES. Frozen: YES. Role: SUPPORTING.

**How to use it.** Background material; consult it if you are auditing how the round was set up.

---
