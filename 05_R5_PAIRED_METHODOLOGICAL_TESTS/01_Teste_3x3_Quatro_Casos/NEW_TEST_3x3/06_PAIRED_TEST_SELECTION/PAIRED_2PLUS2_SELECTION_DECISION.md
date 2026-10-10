# PAIRED 2+2 SELECTION DECISION

**Date:** 2026-10-06  
**Historical input only:** `01_CASE_UNIVERSE/CASE_UNIVERSE_MASTER.csv`, `CASE_SOURCE_PROVENANCE.csv`, and the pre-existing domain classification.

## Decision

| Slot | Case | Historical intermediation count | Selection basis | Comparability status |
|---|---|---:|---|---|
| CLIMATE-1 | CASE-32023R0955 — Regulation (EU) 2023/955 establishing a Social Climate Fund | 5 | highest climate-relevant count; tied at 5 with CBAM, then actors 34 > 16 | DIRECTLY_COMPARABLE |
| CLIMATE-2 | CASE-32023R0956 — Regulation (EU) 2023/956 establishing a carbon border adjustment mechanism (CBAM) | 5 | next climate-relevant case after the documented tie-break | CONDITIONALLY_COMPARABLE |
| TRANSFER-AI | CASE-32004R0874 — Commission Regulation (EC) No 874/2004 governing the .eu Top Level Domain | 6 | highest historical-count candidate in the digital-governance set | HISTORICAL_COUNT_NOT_DIRECTLY_COMPARABLE |
| TRANSFER-OTHER | CASE-31986L0361 — Council Directive 86/361/EEC on terminal-equipment type approval | 3 | highest non-climate, non-digital candidate; exact tie with CASE-31991L0263 survives all available registered metrics, resolved by canonical ID | HISTORICAL_COUNT_NOT_DIRECTLY_COMPARABLE |

## Material limitations carried forward

1. `CLIMATE-1` is R3/S1 and directly comparable inside S1; `CLIMATE-2` is R2/S2, whose bridge with R3 failed. The 5–5 tie is deterministically resolved as the amended rule directs, but the two counts are not evidence of direct cross-pipeline equivalence.
2. `TRANSFER-AI` is the protocol's slot label only. The selected act is an internet-domain-governance case, not an AI-specific act. GDPR, DSA and the AI Act had no historical intermediation count in the registered universe; the selected count comes from six purposively selected provisions and flags derived R-I-T candidates rather than adjudicated positive relations.
3. `TRANSFER-OTHER` likewise comes from a limited-provision PILOT record. Its target metric was not recorded. Its tie with CASE-31991L0263 is therefore resolved by stable canonical ID after the shared recorded tie-break values (3, 6, 3, missing, 4).
4. No architectural finding, V8 finding, RGAM finding, centrality, modularity, hierarchy, topology, or expected procedure performance informed selection.

## Result

`PAIRED_2PLUS2_SELECTION_FROZEN / V8_NOT_STARTED / RGAM_NOT_STARTED`
