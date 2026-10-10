# Updated human-adjudication QA report

## Source and decision integrity

- The human-filled CSV and memo were found at their instructed paths; SHA-256 values match the two expected source hashes exactly.
- The human source names Igor Caires Machado, gives item-level decisions, 2026-10-05 dates, confidence values for the seven P1 items, justifications, and explicit conditions. The memo states that these are coordinator/researcher decisions, not independent external validation.
- Seven adjudicated rows and two explicitly pending rows were incorporated. The original human source files were not changed.
- Source decision, canonical disposition, confidence, verbatim justification, condition/follow-up, reviewer identity, and review date are preserved in the derived register.
- Each of the seven source rows is linked to its unique Step 1 P1 queue item, retaining `source_cell` and unit ID. Reused claim IDs in another cell are not adjudicated by propagation (P03 `CL-P03-02`: Claude A/S1-093 only; P04 `CL-P04-02`: Claude B/S1-104 only).

## Conditional tests and eligibility

- `R-P03-04`: PASS, using only frozen CS-P03-003/005/006 and the already registered referent-resolution rule. No points 3.1 or 3.2 wording was used to establish primary provenance.
- `CL-P03-02`: conditional A carried forward only after that pass; “as sampled” retained and no exclusive-recipient rule inferred.
- `R-P04-05`: reopening test searched only the 14 frozen P04 statements; no explicit Registry-administration statement found. Human B remains sensitivity-only.
- No B decision was autonomously changed to A.
- Both `#CORE` units remain `STEP0_DERIVED`; P03 is descriptive only, and P04 may aid primary analysis only with mandatory with/without reporting.
- No new legal text was introduced. The official legal HTML was not used in either conditional test.

## RG-06 / RG-10 packet

- Exactly two review items were compiled from the existing Step 2A cards and sealed provenance key: RG-06/CG-018 and RG-10/CG-019.
- Each group has four original cell claims plus one separately labelled attached `STEP0_DERIVED` core; the derived unit is not counted as an original experimental claim.
- Each item contains the anonymized propositions, exact frozen evidence, separate out-of-scope note, Step 2A candidate correspondence, effect of P1 decisions, exact question, neutral response frame, and blank reviewer fields.
- Source mapping distinguishes four original cell claims from the separately attached Step0-derived core in each card. The mapping is coordinator-only and marked not for blinded distribution.
- No correspondence decision, confidence, justification, reviewer identity, or review date was prefilled. Neither item was adjudicated by AI.

## Freeze and gate

Previous manifests and frozen baselines were preserved. This report is a QA record, not an independent legal opinion. Updated-manifest validation must show all listed hashes match before the package is treated as frozen.

Status after checksum verification: `P1_HUMAN_ADJUDICATION_INCORPORATED / RG06_RG10_AWAITING_HUMAN_DECISION / STEP2B_NOT_STARTED`.

## Final verification pass (2026-10-05)

- All 31 entries in `HUMAN_ADJUDICATION_UPDATED_MANIFEST.csv` were recalculated against their local paths: 31/31 SHA-256 and byte-length matches; the detached manifest digest also matches the manifest file.
- The supplied P1 CSV and decision memo still match their expected source hashes exactly. The common statement register and frozen Step 1/Step 2A baselines remain verified through their controlling manifests.
- The pre-existing four-cell evidence register records 41 registered file/hash matches. It also records one missing ancillary Codex B Track B freeze-manifest sidecar; substantive outputs are individually hash-verified, and this inherited bookkeeping limitation is not repaired or represented as a new failure in this package.
- The two RG response records remain blank in all decision, confidence, justification, reviewer, and date fields. No Step 2B output was initiated.
