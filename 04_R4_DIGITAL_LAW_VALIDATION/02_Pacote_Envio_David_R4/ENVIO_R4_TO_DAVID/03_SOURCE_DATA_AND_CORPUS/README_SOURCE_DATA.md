# 03 — Source data and corpus

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

```text
RIT_CODING             = NOT_STARTED
MECHANISM_CODING       = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                   = NOT_STARTED
CORPUS_WIDE_REPAIR     = NOT_EXECUTED
```
