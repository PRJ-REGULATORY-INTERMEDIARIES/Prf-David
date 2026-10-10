# RGAM — EXECUTION GAP DECISIONS v1.0 (prospective addendum)

**Date:** 2026-10-06 · **Decider:** research coordinator (Igor Caires Machado), via the execution instruction of 2026-10-06 · **Status:** adopted and frozen **before** any case executor is launched.
**Scope:** clarifies execution gaps GAP-01 … GAP-07 of `RGAM_PAIRED_DECISION_RULES_v1_0.md` Appendix A and one path clarification. It does **not** rewrite RGAM theory, the frozen protocol, the dictionary, the decision rules or the output schema; those remain frozen by manifest SHA-256 `9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932`. Where a decision below is narrower or broader than the wording of a frozen rule, this addendum is the operative clarification for execution and every use must be logged by the executor in PROTOCOL_DEVIATION_LOG with `gap_ref`.

## GAP-01 — Annexes and formal devices
Annexes belong to the documentary universe **W** when they are part of the complete frozen official instrument. They may provide evidence subject to the **same RGAM admission and traceability rules as articles**. A formal device or annex does not become analytically material merely because it exists; its content must satisfy the relevant RGAM admission rule.

## GAP-02 — Provisions amending other legal acts
A provision in W that amends another act may be coded for the legal effect **expressed in W**. The external act itself is **not** added to W. Do not retrieve or analyse the amended external instrument. The EXT record for the amended act remains required (RGAM-DR-08). Where the external instrument is necessary to interpret a higher-order claim, record an external-reference dependency and **stop at the highest level supported by W**.

## GAP-03 — Internal cross-references
Cross-references to another provision within the same frozen instrument may be followed. They remain inside W. They may resolve referents, definitions, conditions, scope and internal legal linkage. Record both the source provision and the referenced provision (supporting units; derivation rule). The inferential path must not be hidden. (Consistent with RGAM-DR-20 and conflict C-12.)

## GAP-04 — External retrieval
External legal retrieval is **prohibited** during case execution: no web browsing; no retrieval of other statutes, delegated acts, implementing acts, guidance, case law, explanatory documents or prior analytical outputs. External references are recorded as EXT records; they do not silently expand W. (Consistent with RGAM-DR-20.)

## GAP-05 — Function vocabulary
Use only the functional categories documented in the frozen RGAM protocol/source hierarchy (data dictionary `FUNCTION` vocabulary, including its flagged residual tags). Do not import V8 vocabulary; do not create new standardized categories. Where a legally meaningful function cannot be placed in the documented vocabulary, preserve the legally grounded description (in `action`/`mechanism`), use the protocol's flagged residual tag only if it genuinely fits, and otherwise write `FUNCTION_VOCABULARY_UNRESOLVED` in the `function` field. Do not force classification.

## GAP-06 — "Six questions"
The "six questions" referenced in the operational template but absent from the authorized RGAM sources are **not operative** in this experiment. Do not reconstruct or invent them. Record `NON_OPERATIVE_SOURCE_GAP`. They cannot be used as an admission, exclusion or inference rule.

## GAP-07 — Definition provisions
Definitions within W may establish entity identity, legal type, scope, referential meaning and applicable class. A definition does **not** automatically establish a qualified relation, authority, accountability, intermediation or architectural coupling. A relation must independently satisfy the RGAM relation admission rule (RGAM-DR-14).

## Path clarification (execution only)
The frozen documents name the output root `12_RGAM_EXECUTION/<CAPSULE_ID>/`. For this execution the output root is **`12_RGAM_CASE_EXECUTION/<CAPSULE_ID>/`** (instruction of 2026-10-06). Wherever a frozen document or capsule README says `12_RGAM_EXECUTION/`, read `12_RGAM_CASE_EXECUTION/`. The executor may additionally read this addendum. Nothing else in the frozen allow-list changes.

## Registered execution tokens
`NON_OPERATIVE_SOURCE_GAP`, `FUNCTION_VOCABULARY_UNRESOLVED` (no new vocabulary beyond these two execution tokens).
