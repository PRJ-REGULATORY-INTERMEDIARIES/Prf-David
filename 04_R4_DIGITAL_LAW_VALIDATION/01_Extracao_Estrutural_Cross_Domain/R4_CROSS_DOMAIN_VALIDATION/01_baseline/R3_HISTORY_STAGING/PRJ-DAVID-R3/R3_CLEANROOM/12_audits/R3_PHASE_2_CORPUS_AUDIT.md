# R3 Phase 2 — Corpus Construction Audit

**Project:** GP5_JRG / Prf-David  
**Round:** R3  
**Phase:** 2 — Corpus construction  
**Execution date:** 2026-09-20  
**Status:** `READY_FOR_RESEARCHER_REVIEW`

## A. Work completed

- Used only the five frozen Phase 1 raw PDFs.
- Generated one structural corpus package per CELEX.
- Preserved the original order of the extracted legal text, including preamble/recitals, operative provisions and annexes where present.
- Created human-readable full, recital-only, operative-only and deterministically numbered versions.
- Created one structural `article_index.csv` per act with line anchors for later evidence citation.
- Created one `CORPUS_MANIFEST.yaml` per act with source and generated-file hashes.
- Did not identify or code regulators, targets, intermediaries, R/I/T roles, mechanisms, relationships, law–intermediary units or theoretical questions.

## B. Inputs used

- `01_sources/<CELEX>/source_original_en.pdf` for the five authorized CELEX acts.
- The Phase 2 authorization supplied by the researcher.
- Structural rules in `00_governance/R3_PROMPT_VERBATIM.md`.

No prior corpus, legal-text copy, summary, coding, classification or earlier version was opened or used.

## C. Outputs created

For each CELEX under `02_corpus/<CELEX>/`:

- `act_full.md`
- `recitals.md`
- `operative.md`
- `act_numbered.md`
- `article_index.csv`
- `CORPUS_MANIFEST.yaml`

Cross-case output:

- `02_corpus/R3_CORPUS_REGISTER.csv`
- `12_audits/R3_PHASE_2_BUILD.ps1` — reproducible structural extraction helper
- this audit report

## D. Quantitative summary

| CELEX | PDF pages | Recitals | Articles | Annexes | Chapters | Words | Full-text lines | Index rows | Corpus status |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| 32003L0087 | 15 | 30 | 33 | 5 | 0 | 8,477 | 947 | 201 | `CORPUS_TEXT_REQUIRES_REVIEW` |
| 32015D1814 | 5 | 12 | 5 | 0 | 0 | 3,091 | 223 | 29 | `CORPUS_TEXT_REQUIRES_REVIEW` |
| 32018R0842 | 17 | 46 | 17 | 4 | 0 | 9,067 | 690 | 155 | `CORPUS_TEXT_REQUIRES_REVIEW` |
| 32021R1119 | 17 | 40 | 14 | 0 | 0 | 10,159 | 733 | 147 | `CORPUS_TEXT_REQUIRES_REVIEW` |
| 32023R0955 | 51 | 47 | 29 | 5 | 7 | 27,239 | 2,203 | 348 | `CORPUS_TEXT_REQUIRES_REVIEW` |

Structural sequence checks detected no missing recital numbers or missing numeric article bases in the extracted navigation layer.

## E. Methodological decisions

- The PDF text was extracted with a raw-reading-order mode to avoid the two-column ordering problem visible in the 2003 act.
- Only conservative operations were applied: removal of Official Journal page headers and page separators, trimming extraction-only whitespace, and repair of line-wrap hyphenation when the continuation begins with lowercase text.
- Paragraph, heading, numbering, table and annex line structure was retained; the corpus was not flattened into snippets.
- `act_numbered.md` uses deterministic `L000001`-style anchors corresponding to `act_full.md` lines.
- The original Phase 1 source files were not modified.

## F. Per-act technical report

### 32003L0087

- Source: `01_sources/32003L0087/source_original_en.pdf`.
- Source SHA-256: `B3941901E4FE1AF3DEFCFFA323C00A5C6F7F44C51C9EA5785C7A995C3BD68445`.
- Generated: six files listed above.
- Extraction observations: 45 page-header lines removed; 109 line-wrap hyphen repairs; 24 split footnote-marker patterns observed; 5 annex headings preserved; 0 replacement characters detected.
- Corrections made: only the allowed structural normalization operations.
- Unresolved issues: footnote-marker placement and annex/table fidelity require human spot review.
- Status: `CORPUS_TEXT_REQUIRES_REVIEW`.

### 32015D1814

- Source: `01_sources/32015D1814/source_original_en.pdf`.
- Source SHA-256: `BCA2648F3E4A312BF6F31F5270B01D933234E949F4EAC54157A0115086E18036`.
- Generated: six files listed above.
- Extraction observations: 18 page-header lines removed; no line-wrap hyphen repairs; 12 split footnote-marker patterns observed; no annex headings; 0 replacement characters detected.
- Corrections made: only the allowed structural normalization operations.
- Unresolved issues: footnote-marker placement requires human spot review.
- Status: `CORPUS_TEXT_REQUIRES_REVIEW`.

### 32018R0842

- Source: `01_sources/32018R0842/source_original_en.pdf`.
- Source SHA-256: `DD429F4752B9F0F9320CE2FC79152D02A7D34BE262EE86019D98B96E62D07048`.
- Generated: six files listed above.
- Extraction observations: 34 page-header lines removed; 3 line-wrap hyphen repairs; no split footnote-marker patterns detected; 4 annex headings preserved; 0 replacement characters detected.
- Corrections made: only the allowed structural normalization operations.
- Unresolved issues: annex tables and numeric formatting require human spot review.
- Status: `CORPUS_TEXT_REQUIRES_REVIEW`.

### 32021R1119

- Source: `01_sources/32021R1119/source_original_en.pdf`.
- Source SHA-256: `855EBC344E9FAF2DB68D75317C08034AF54A1CCE216D8D00C640C3073E639840`.
- Generated: six files listed above.
- Extraction observations: 29 page-header lines removed; 6 line-wrap hyphen repairs; 28 split footnote-marker patterns observed; no annex headings; 0 replacement characters detected.
- Corrections made: only the allowed structural normalization operations.
- Unresolved issues: footnote-marker placement and cross-reference line breaks require human spot review.
- Status: `CORPUS_TEXT_REQUIRES_REVIEW`.

### 32023R0955

- Source: `01_sources/32023R0955/source_original_en.pdf`.
- Source SHA-256: `F58712E1156435A418EC1A445F9DBB8D9742FF29E3C8317FF4C00FF929740C49`.
- Generated: six files listed above.
- Extraction observations: 84 page-header lines removed; 16 line-wrap hyphen repairs; 76 split footnote-marker patterns observed; 5 annex headings and 7 chapters preserved; 0 replacement characters detected.
- Corrections made: only the allowed structural normalization operations.
- Unresolved issues: annex templates, tables, footnotes and numeric formatting require human spot review.
- Status: `CORPUS_TEXT_REQUIRES_REVIEW`.

## G. Cross-case technical differences

These are extraction and navigation differences only, not substantive legal comparisons:

- `32003L0087` uses a two-column Official Journal layout and has the highest number of line-wrap repairs.
- `32018R0842` and `32023R0955` contain annex tables whose row structure was retained as extracted lines.
- `32023R0955` is the longest source and produces the largest numbered corpus.
- Footnote-marker line splits occur in the 2003, 2015, 2021 and 2023 PDFs; they are flagged rather than silently corrected.
- No replacement characters were detected in any extracted source.

## H. Source-to-corpus fidelity

All five cases passed the following structural checks:

- source SHA-256 still matches the Phase 1 register;
- PDF page count is preserved as the acquisition baseline;
- first and last recital markers were found where applicable;
- first and last article headings were found;
- no missing numeric recital or article-base sequence was detected;
- annex headings were retained where present;
- generated-file SHA-256 values are recorded in each corpus manifest;
- no prior corpus or prior empirical file was imported.

The formal corpus status for all five cases is deliberately:

`CORPUS_TEXT_REQUIRES_REVIEW`

This means the structural package is available for researcher inspection, but no claim is made that every footnote, table, formula or symbol has been manually confirmed against the raw PDF.

## I. Researcher decisions required

1. Review the five corpus packages, especially footnote markers, annex tables and numeric formatting.
2. Decide whether each package may be promoted from `CORPUS_TEXT_REQUIRES_REVIEW` to `CORPUS_TEXT_COMPLETE`.
3. If accepted, authorize Phase 3 explicitly with `CONTINUE TO PHASE 3` or `APPROVED — CONTINUE`.

No substantive analysis was performed and Phase 3 has not started.

## J. Status

Phase 2 is complete. The R3 process must stop here until explicit researcher authorization is received.

R3_PHASE_2_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION
