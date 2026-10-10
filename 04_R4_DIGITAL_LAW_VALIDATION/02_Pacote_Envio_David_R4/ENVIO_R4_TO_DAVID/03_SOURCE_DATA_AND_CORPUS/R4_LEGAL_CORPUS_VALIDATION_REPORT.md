# R4.1 — Legal Corpus Validation Report

**Date:** 2026-09-26  
**Phase:** R4.1 — official legal corpus acquisition, validation and freeze  
**Scope:** source engineering and structural validation only

## Acquisition and source selection

The three fixed acts were acquired as English XHTML from the official Publications Office of the European Union / CELLAR CELEX resource, using content negotiation for `application/xhtml+xml` and `Accept-Language: en`. The fixed EUR-Lex ELI URLs remain the canonical source references in the register. The EUR-Lex browser-facing HTTPS pages returned a technical verification response in this environment; the official CELLAR representation was therefore used as the machine-readable primary source and its endpoint is recorded in the provenance table.

The selected version for all three cases is the original Official Journal act as published, not a current consolidated text. Amendments are not incorporated into these frozen source files. This choice follows the R4.1 default and preserves a stable baseline for later analysis.

## Case results

| Case | CELEX | Original bytes | Original SHA-256 | Recitals | Chapters | Sections | Articles | Annexes | Result |
|---|---|---:|---|---:|---:|---:|---:|---:|---|
| D1_GDPR | 32016R0679 | 806,864 | `962539AF03738BF552319FF4CE42D69E5F95A576307C4DFED7BF87E81B646B9D` | 173 | 11 | 15 | 99 | 0 | `VALIDATED_WITH_NOTES` |
| D2_DSA | 32022R2065 | 838,166 | `11B119A7D45F3A10CD41714061F9D907839EF5D1634E41774490F00B95856BBF` | 156 | 5 | 12 | 93 | 0 | `VALIDATED_WITH_NOTES` |
| D3_AI_ACT | 32024R1689 | 1,262,391 | `8F0B656302F9864CC87E040C371F209A9D65AE1A6CECC25CA5EB737E872D721A` | 180 | 13 | 16 | 113 | 13 | `VALIDATED_WITH_NOTES` |

All three source files begin as valid XHTML documents, contain the expected English-language header, preserve the source document ending, and have coherent article and recital numbering. The AI Act includes and preserves all 13 annex containers detected in the official source.

## Processing copies

One UTF-8 plain-text processing copy was generated for each act. The transformation is mechanical: visible XHTML text was extracted in document order, whitespace was normalized, and explicit delimiter lines were added for document boundaries, recitals, operative provisions, chapters, sections, articles and annexes. Legal wording was not paraphrased, translated, reordered or semantically compressed. The processing hashes therefore differ from the original hashes by design.

The structure index and article index provide stable local positions in the processing copies and source references back to the original XHTML element IDs.

## Validation status and notes

The mechanical structural gate passed for all cases. `VALIDATED_WITH_NOTES` records that human validation remains required for corpus inclusion and version acceptance, as required by the governing protocol. No unresolved source identity or structural ambiguity was detected.

No actor extraction, role assignment, intermediary identification, mechanism search or mechanism coding was performed. Rotem Medzini’s coding was not consulted. The R3 codebook and baseline were not modified.

## Escalation

No Luna → Terra escalation occurred. The operation remained mechanical and structured. The actual Codex runtime did not expose a selectable Luna/Terra variant; the AI execution log records this transparently rather than assigning an unsupported model label.

## Readiness

The official corpus is frozen for R4.1 as three original XHTML sources plus traceable processing copies. The project is ready for human review of the corpus package and, after explicit authorization, R4.2 structural/extraction planning. Substantive actor and mechanism analysis remains out of scope until then.
