# V8 case QA report — AI Act

## Scope and integrity

- Case: Regulation (EU) 2024/1689, complete English official XHTML.
- Expected and pre-run source SHA-256 match: `8f0b656302f9864cc87e040c371f209a9d65ae1a6cecc25ca5eb737e872d721a`.
- Four prescribed method inputs were hash-checked against their expected values before analysis.
- Corpus was read only; post-run source hash is recorded in the freeze manifest.
- No web browsing and no other case or empirical outputs were used.

## Required artifacts and internal consistency

- All 12 required case artifacts are included in the freeze manifest.
- Claim register: 14 claims (C01–C14), each with `case_id=CASE-32024R1689`, explicit analytical level, legal anchor, direct evidence, inferential step, confidence and status. Claim text and count were preserved during case-ID normalization.
- Analytical-level distribution by exact field value: Level I only: 6; Level I/II: 2; Level II: 4; Level III: 2. Totals by level represented: Level I: 8; Level II: 6; Level III: 2.
- Relation register: 11 typed relations (R01–R11), with conditions and scoped attributes; assignments without a counterpart are not forced into dyads.
- Configuration register: 3 supported configurations (K01–K03).
- Architecture register: 1 bounded formal architecture (A01), vertically traceable to configurations, claims, relations and articles.
- Uncertainty register: 9 items (U01–U09), with an explicit `uncertainty_type` mapping for every mandated category.
- Traceability matrix: 12 paths linking A01 to configurations, claims, relations and provisions.

## Mandated uncertainty-category coverage

| Category | Coverage | Status |
|---|---|---|
| Source/reference ambiguity | U08 | Screened/not material for the frozen Regulation text; external references are not treated as independently analyzed evidence. |
| Actor ambiguity | U01, U03 | Retained with limits on actor identity and overlapping mandates. |
| Action ambiguity | U04, U09 | U04 retains bounded evaluative-choice uncertainty; U09 screens core action wording as not material to coding. |
| Counterparty ambiguity | U01, U03 | Retained; relationships are limited to evidenced counterparties and links. |
| Modality ambiguity | U02, U04 | Route and authority modalities are qualified by their article-specific conditions. |
| Condition ambiguity | U02, U04 | Conditional routes and measure criteria are retained. |
| Cross-provision inference | U03, U07 | Explicitly recognized and bounded by traceability. |
| Architectural inference | U07 | Retained as a bounded configurational inference, not a frequency claim. |
| Stopping-rule uncertainty | U05, U06 | Stops at formal architecture; no regime or operation-level inference. |

## Methodological checks

- Uses only V8 Levels I/II/III and the six Level I element classes, three Level II attributes, and warranted higher-order constructs.
- Separates functions, mechanisms and instruments; distinguishes express normative assignment from relational inference.
- Treats architecture configurationally, not by frequency.
- Stops at formal architecture; does not claim a regulatory regime, operational arrangement, implementation, effectiveness or a uniform governance logic.
- Describes notified-body assessment as conditional under Article 43 and the GPAI pathway as distinct under Chapter V.

## Conclusion

QA passes with bounded higher-order inference, all nine uncertainty categories explicitly covered, and all 14 claims assigned to case `CASE-32024R1689` with an explicit analytical level. The supported conclusion is a differentiated, hybrid, multilevel **formal legal architecture** constituted by the Regulation. Broader regime boundaries and practice-level claims remain outside the evidence and are expressly unclaimed.
