# Primary Interpretive Reader Proposal — Second Independent Reading (R2)

**Case 02 — Regulation (EU) 2023/956 (CBAM)** | prompt: `prompts/production/PRIMARY_INTERPRETIVE_READER.md`, production v1.1 | schema: `methodology/production_v1.1/coding_matrix_schema.json`

Second, independently produced Primary Interpretive Reader proposal for Case 02, run at the researcher's request alongside the existing `PRIMARY_INTERPRETIVE_READER_PROPOSAL.{json,md}`. Does not overwrite or treat the first proposal as ground truth. See `RUN_METADATA_R2.yaml` for a transparency note on limited context exposure during this session.

## Relation matrix (summary)

| ID | Type | R | I | T | Mechanism |
|---|---|---|---|---|---|
| REL_C02_001 | **intermediated** | Commission; competent authorities | accredited verifiers | authorised CBAM declarants | verification |
| REL_C02_002 | **intermediated** | Commission | national accreditation bodies | verifiers | accreditation |
| REL_C02_003 | **intermediated** | Commission; competent authorities | customs authorities | authorised CBAM declarants / importers | information_transmission |
| REL_C02_004 | direct | Commission; competent authorities | — | authorised CBAM declarants | none_or_direct |
| REL_C02_005 | direct | competent authorities | — | authorised CBAM declarants; unauthorised persons | none_or_direct |
| REL_C02_006 | direct | Commission | — | operators (third-country installations) | none_or_direct |
| REL_C02_007 | direct | Commission | — | third countries/territories | none_or_direct |
| REL_C02_008 | uncertain | Commission | MS, affected parties, NGOs (candidate) | producers/traders circumventing | information_transmission |

## Relation detail

### REL_C02_001 — Verification of embedded emissions (intermediated) — strongest case
**Anchor:** Article 6(2)(d); Article 8(1)-(3).
Accredited verifiers independently verify declarants' declared embedded emissions per Annex VI principles; Article 6(2)(d) makes the verification report a mandatory declaration component. The clearest, most textbook verification-type intermediary in this project's three cases so far.

### REL_C02_002 — Accreditation of verifiers (intermediated) — nested intermediation
**Anchor:** Article 18(1)-(3).
National accreditation bodies qualify (and can withdraw the qualification of) the verifiers who perform REL_C02_001's function — an upstream link in the same chain. Illustrates the RIT framework's relational roles: verifiers are I in REL_C02_001 and T here.

### REL_C02_003 — Customs authorities (intermediated)
**Anchor:** Article 25(1)-(4); Article 33.
Customs authorities gatekeep unauthorised importation and transmit import data that feeds the Commission's Article 15 risk analysis and Article 19 declaration review.

### REL_C02_004 / REL_C02_005 / REL_C02_006 / REL_C02_007 — Direct relations
The core declaration/registry/certificate-lifecycle compliance architecture (004), penalties (005), third-country-operator registration (006), and the third-country electricity-market exemption assessment (007) are all direct Commission/competent-authority-to-target relations without an integrated third-party intermediary.

### REL_C02_008 — Circumvention notification channel (uncertain)
**Anchor:** Article 27(4)-(5).
Member States, affected/benefited parties, and NGOs may notify the Commission of circumvention, formally triggering an investigation. More institutionalised than ordinary lobbying, but the Commission has its own independent detection means (Article 27(3)) and the notifier does not verify or certify anything — a genuinely closer call than the verification/accreditation relations above. Contrast the more strongly institutionalised analogue in Case 03 (uncertainty U9 there).

## Uncertainty / boundary-case log

9 entries recorded, spanning: a comitology committee (U1, co-regulation, consistent with Case 01's Energy Union Committee); delegated-act expert consultation (U2, rule-making assistance, not intermediation); the Commission's Article 12 coordination role toward competent authorities, considered as a candidate regulator-facing intermediary and rejected in favour of joint-regulator treatment (U3); the Climate Club (U4, recital-only — Recital 72 has zero operative implementation); generic stakeholder consultation (U5, external influence); the CBAM registry and common central platform (U6, instruments not actors); LDC technical assistance under an external instrument (U7); accreditation-body peer evaluation (U8, reinforcing note for REL_C02_002); and operator-to-declarant voluntary disclosure (U9, agency between two already-regulated targets).

## Methodological note

**A. Regulatory architecture.** A market-based carbon-pricing-equivalence mechanism combining declarant authorisation, emissions declaration, independent verification (itself gated by accreditation), certificate purchase/surrender, customs border-control, and penalties, with the Commission and Member State competent authorities acting throughout as joint regulators.

**B. Totals.** Intermediated = 3; direct = 4; uncertain = 1; not_supported = 0.

**C. Orientation.** All three intermediated relations are **target-facing**: verifiers, accreditation bodies and customs authorities each perform a function that bears directly on the declarant's/verifier's own compliance object, unlike Case 01's purely regulator-facing finding.

**D. Mechanisms found.** `verification`, `accreditation`, `information_transmission`. No reporting-as-scientific-advice, monitoring_supervision-as-third-party, ranking/rating, standard_setting, or delegated_implementation mechanisms were found as distinct intermediary functions (the Commission's and competent authorities' own direct actions account for the rest of the architecture).

**E. Strongest cases.** REL_C02_001 (verification) and REL_C02_002 (accreditation) together form a clean, well-evidenced nested intermediation chain; REL_C02_003 (customs authorities) is nearly as strong.

**F. Boundary cases.** The Commission's Article 12 coordination role (U3) — considered and rejected as intermediary in favour of co-regulator status — and the circumvention-notification channel (REL_C02_008/uncertain) are the two most difficult calls, the latter directly contrasted with Case 03's stronger analogue.

**G. External influence excluded.** Generic stakeholder consultation (U5) and, on balance, the circumvention-notification channel (coded uncertain rather than confidently excluded or included).

**H. Recital-only candidates.** The Climate Club (Recital 72, U4) is the clearest recital-only candidate in this case.

**I. False-negative audit.** A targeted second pass for the full functional list (reporting, information transmission, assessment, advice, technical assistance, monitoring, verification, certification, auditing, accreditation, ranking, implementation/compliance/enforcement support, coordination, feedback, evaluation) surfaced no further operative-anchored intermediaries beyond those logged; the mutual-recognition/peer-evaluation clause among accreditation bodies (U8) and the operator-declarant disclosure detail (U9) were the two marginal items this pass added, both folded into existing relations rather than treated as new ones.

## Completion checklist

- [x] Full operative corpus read (Articles 1–36, Chapters I–XI, Annexes I–VI reviewed for cross-reference content)
- [x] R-T reconstructed before I classification
- [x] Regulator-facing intermediation considered (Article 12, rejected — U3)
- [x] Target-facing intermediation considered and found (verification, accreditation, customs)
- [x] External influence distinguished from I (U5; REL_C02_008 kept uncertain rather than forced)
- [x] Reporting not mechanically equated with I
- [x] Advice/expertise not mechanically excluded
- [x] Recital-only positives prohibited (U4)
- [x] Cross-references followed (Article 6(2)(d) ↔ Article 8; Article 8(1) ↔ Article 18; Article 19 ↔ Article 25/15)
- [x] Second-pass recall check completed
- [x] Boundary-case log completed
- [x] No previous empirical outputs consulted for their substantive content

```
THEORETICALLY_RECALIBRATED_READING_COMPLETE
SOURCE_BOUNDED
PREVIOUS_RESULTS_NOT_CONSULTED
READY_FOR_CRITICAL_REVIEW
```
