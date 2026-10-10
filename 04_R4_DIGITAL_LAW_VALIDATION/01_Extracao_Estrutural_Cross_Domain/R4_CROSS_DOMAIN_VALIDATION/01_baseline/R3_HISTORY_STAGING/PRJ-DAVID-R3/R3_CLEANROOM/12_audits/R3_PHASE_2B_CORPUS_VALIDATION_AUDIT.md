# R3 Phase 2B — Corpus Validation Gate Audit

**Project:** GP5_JRG / Prf-David  
**Round:** R3  
**Phase:** 2B — Corpus validation  
**Execution date:** 2026-09-20  
**Status:** `READY_FOR_RESEARCHER_REVIEW`

## A. Decision applied

Phase 2 was provisionally approved. Phase 3 was not authorized.

This gate was executed only to validate textual and structural fidelity against the five fresh official Phase 1 PDFs. No previous corpus, summary, coding, classification or case output was consulted.

## B. Validation work completed

- Re-extracted each frozen Phase 1 PDF in raw reading order.
- Reapplied only the documented structural normalization rules.
- Compared the complete normalized source text against each current `act_full.md`.
- Verified source SHA-256 values against the Phase 1 register.
- Verified all generated-file hashes against each current corpus manifest.
- Rechecked recital and article sequences, annex headings, page boundaries and final-provision presence.
- Reviewed footnote-marker patterns, tables, formulas, symbols, superscript/subscript risks, cross-references and broken/duplicated-text risks.
- Visually checked representative fidelity-risk pages in the fresh official PDFs:
  - `32003L0087`: Annex I and final Annex V pages;
  - `32018R0842`: Annex I and final Annex IV pages;
  - `32023R0955`: formula-bearing Annex I page and final Annex V page.
- Did not identify or code regulators, targets, intermediaries, R/I/T roles, relations, mechanisms or regulatory architecture.

## C. Outputs created

- `02_corpus/R3_CORPUS_VALIDATION_REGISTER.csv`
- `02_corpus/R3_CORPUS_CORRECTION_LOG.csv`
- updated generated-file hashes in the affected corpus manifest(s)
- this audit report

## D. Validation results

Counts in the required fields refer to distinct reviewed issue classes, not the number of individual extracted lines. The 11 reviewed classes were: footnotes, tables, formulas, symbols, superscripts/subscripts, article numbering, paragraph numbering, annexes, cross-references, page-boundary text, and broken/duplicated text.

| CELEX | Issues reviewed | Cosmetic | Structural non-substantive | Potentially substantive | Substantive errors found | Corrections | Final status |
|---|---:|---:|---:|---:|---:|---:|---|
| 32003L0087 | 11 | 1 | 1 | 0 | 0 | 0 | `CORPUS_VALIDATED_WITH_DOCUMENTED_LIMITATIONS` |
| 32015D1814 | 11 | 1 | 1 | 0 | 0 | 0 | `CORPUS_VALIDATED_WITH_DOCUMENTED_LIMITATIONS` |
| 32018R0842 | 11 | 1 | 1 | 0 | 0 | 0 | `CORPUS_VALIDATED_WITH_DOCUMENTED_LIMITATIONS` |
| 32021R1119 | 11 | 1 | 1 | 0 | 0 | 0 | `CORPUS_VALIDATED_WITH_DOCUMENTED_LIMITATIONS` |
| 32023R0955 | 11 | 1 | 1 | 1 | 1 | 1 | `CORPUS_VALIDATED_WITH_DOCUMENTED_LIMITATIONS` |

All five cases passed source-hash, normalized-text and manifest-hash checks after correction. No case is `CORPUS_NOT_READY`.

## E. Correction record

One correction was required:

- **CELEX:** `32023R0955`
- **File:** `02_corpus/32023R0955/act_full.md`
- **Official location:** original Phase 1 PDF, OJ L 130, 16.5.2023, p. 29, Annex I formula
- **Original extracted form:** a standalone lowercase `i` line was absent from the corpus formula text.
- **Corrected form:** the standalone lowercase `i` line is retained.
- **Cause:** a case-insensitive filter intended to remove the Official Journal's uppercase Roman numeral page furniture also removed lowercase formula variable markers.
- **Correction type:** `SUBSTANTIVE_TEXT_ERROR`
- **Provenance:** fully recorded in `R3_CORPUS_CORRECTION_LOG.csv`.

The correction was regenerated from the official raw PDF; it was not reconstructed from any prior corpus. The affected corpus manifest now contains the new generated-file hashes.

## F. Per-case status and limitations

### 32003L0087

Validated with documented limitations. The representative Annex I table and final annex page were visually checked. Remaining limitation: footnote-marker line breaks and Markdown's inability to preserve full table geometry.

### 32015D1814

Validated with documented limitations. No table or formula extraction risk requiring visual reconstruction was identified. Remaining limitation: footnote-marker line breaks are structurally normalized.

### 32018R0842

Validated with documented limitations. Representative Annex I and Annex IV table pages were visually checked, and table rows are retained in the corpus. Remaining limitation: Markdown does not preserve table geometry.

### 32021R1119

Validated with documented limitations. Text-level comparison found no loss in the reviewed structural fields. Remaining limitation: footnote-marker line breaks are structurally normalized.

### 32023R0955

Validated with documented limitations after correction. The formula-bearing Annex I page and final Annex V page were visually checked; the missing lowercase `i` was corrected and logged. Remaining limitation: formula superscript/subscript geometry is represented through extracted text rather than rich mathematical markup, and annex tables remain row-oriented.

## G. Quality-control results

- Normalized source text equals corpus text for all five acts after the documented correction.
- Source hashes still match the Phase 1 register for all five acts.
- All generated-file hashes match the current corpus manifests.
- Recital and article sequences pass the structural checks.
- Annex headings and page-boundary transitions are present.
- No replacement characters were detected.
- No unexplained truncation or duplicated page text was detected.
- `32000D0293` was not acquired, analyzed or included.

## H. Researcher decisions required

The corpus set is eligible for researcher authorization to proceed. Phase 3 remains blocked until explicit authorization is received, for example:

`CONTINUE TO PHASE 3`

or

`APPROVED — CONTINUE`

## I. Status

Phase 2B is complete. Phase 3 has not started.

R3_PHASE_2B_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION
