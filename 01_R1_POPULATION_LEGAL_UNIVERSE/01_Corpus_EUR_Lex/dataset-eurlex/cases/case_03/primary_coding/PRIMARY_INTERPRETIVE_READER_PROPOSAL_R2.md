# Primary Interpretive Reader Proposal — Second Independent Reading (R2)

**Case 03 — Regulation (EU) 2023/1115 (EUDR)** | prompt: `prompts/production/PRIMARY_INTERPRETIVE_READER.md`, production v1.1 | schema: `methodology/production_v1.1/coding_matrix_schema.json`

Second, independently produced Primary Interpretive Reader proposal for Case 03, run at the researcher's request alongside the existing `PRIMARY_INTERPRETIVE_READER_PROPOSAL.{json,md}`. Does not overwrite or treat the first proposal as ground truth. See `RUN_METADATA_R2.yaml` for a transparency note on limited context exposure during this session.

## Relation matrix (summary)

| ID | Type | R | I | T | Mechanism |
|---|---|---|---|---|---|
| REL_C03_001 | direct | Competent authorities; Commission | — | operators; traders | none_or_direct |
| REL_C03_002 | **intermediated** | Competent authorities; Commission | customs authorities | operators; traders | information_transmission |
| REL_C03_003 | direct | Commission | — | Member States; third countries | none_or_direct |
| REL_C03_004 | **intermediated** | Competent authorities | natural/legal persons (substantiated concerns) | operators; traders | information_transmission |
| REL_C03_005 | uncertain | Competent authorities | certification/third-party schemes (candidate) | operators | certification |
| REL_C03_006 | **intermediated** | Competent authorities | FLEGT licensing authorities/scheme | operators/traders of FLEGT wood | certification |

## Relation detail

### REL_C03_001 — Core due-diligence / market-access compliance (direct)
**Anchor:** Article 3; Article 4(1)-(2); Article 16(1).
The prohibition-and-due-diligence architecture directly binding operators and traders.

### REL_C03_002 — Customs authorities (intermediated)
**Anchor:** Article 26(3)-(9); Article 27.
Customs authorities examine due-diligence-statement status via the electronic interface and suspend or allow release for free circulation/export — implementing, at the border, the compliance determination that Article 26(2) assigns to competent authorities.

### REL_C03_003 — Country risk benchmarking and cooperation (direct)
**Anchor:** Article 29(1)-(8); Article 30(1).
The Commission classifies Member States and third countries into risk tiers and engages in cooperative partnerships; diverse optional information sources feeding the classification (Article 29(4)) are treated as external influence, not intermediation (uncertainty U7).

### REL_C03_004 — Substantiated concerns mechanism (intermediated) — strongest case together with REL_C03_006
**Anchor:** Article 31(1)-(2); Article 16(12); Article 23(a).
A dedicated chapter (Chapter 6) establishes a formally defined ("substantiated concern," Article 2(31)) third-party notification channel that *mandatorily* triggers competent-authority assessment and is explicitly incorporated into the risk-based check-selection (Article 16(12)) and interim-measures (Article 23(a)) criteria, with a response deadline (Article 31(3)) and whistleblower-style identity protection (Article 31(4)). Materially more institutionalised than the comparable channel in Case 02 (CBAM Article 27(4)), which was coded uncertain there — see uncertainty U9 for the explicit cross-case contrast.

### REL_C03_005 — Third-party certification schemes as risk-assessment input (uncertain)
**Anchor:** Article 10(2)(n).
Certification/third-party-verified schemes are one of fourteen optional risk-assessment criteria an *operator* may use in its own self-assessment; Recital 52 explicitly states such schemes do not substitute the operator's own due-diligence responsibility. A structurally different position from classic intermediation (I supports T's self-assessment, rather than mediating R's assessment of T) — genuinely uncertain rather than confidently positive or negative.

### REL_C03_006 — FLEGT licensing deemed-compliance (intermediated) — easily overlooked, strong case
**Anchor:** Article 10(3).
"Wood products... covered by a valid FLEGT license... shall be deemed to comply with Article 3, point (b)" — an automatic, mandatory legal effect (contrast REL_C03_005's merely optional, non-substitutive certification), anchored in a single paragraph of this Act's own operative text even though the underlying FLEGT/VPA licensing regime lives in a different Regulation.

## Uncertainty / boundary-case log

9 entries recorded. The standout is **U1 — the EU Observatory** (Recital 31): an elaborately described regulator-facing monitoring and scientific-evidence body, with an explicit mandate to cooperate with competent authorities, international organisations, research institutes, NGOs, operators, traders and third countries — textbook intermediary shape, but with *zero* mention or assigned function anywhere in Articles 1–38. This is the single clearest illustration, across all three cases read in this session, of why the operative/recital evidentiary distinction (Section 15/16 of the governing methodology) is not a technicality: a recital this elaborate could easily be mistaken for an operative finding if recitals were read as equal-weight evidence. Other entries: Commission expert groups excluded for failing distinctness (U2, parallel to Case 01's JRC exclusion); authorised representatives excluded as procedural agency/proxy for the operator/trader, not an independent function (U3); the Commission's Article 15 coordination role, rejected as intermediary in favour of joint-regulator treatment (U4, parallel to Case 02's Article 12); the Article 36 comitology committee (U5); delegated-act expert consultation (U6); diverse optional information sources feeding Article 29 classification (U7, external influence); the information system and electronic interface as instruments (U8); and the explicit cross-case methodological contrast with Case 02's weaker circumvention-notification analogue (U9).

## Methodological note

**A. Regulatory architecture.** A supply-chain due-diligence and market-access regime (prohibition, due diligence, risk assessment/mitigation) enforced by Member State competent authorities with Commission support, layered with a country risk-benchmarking system, a formally institutionalised third-party complaint channel, a border-control mechanism run through customs authorities, and a narrow but strong certification shortcut for FLEGT-licensed wood.

**B. Totals.** Intermediated = 3; direct = 2; uncertain = 1; not_supported = 0.

**C. Orientation.** All three intermediated relations are **target-facing**: customs authorities, substantiated-concern submitters, and FLEGT licensing authorities each bear directly on operators'/traders' own compliance status, rather than feeding an internal Commission process.

**D. Mechanisms found.** `information_transmission` (customs authorities; substantiated concerns) and `certification` (FLEGT licensing, confidently; third-party schemes, uncertainly). No verification, auditing, accreditation, ranking/rating, monitoring_supervision-as-third-party, standard_setting, or delegated_implementation mechanisms were found as distinct intermediary functions in the operative text.

**E. Strongest cases.** REL_C03_004 (substantiated concerns) and REL_C03_006 (FLEGT licensing) — the latter especially notable for being easy to miss (a single paragraph) yet fully operative-anchored and mandatory in effect.

**F. Boundary cases.** REL_C03_005 (third-party certification as optional, non-substitutive risk-assessment input) is the most instructive boundary case in this reading: contrasted directly against REL_C03_006, it shows how the *same general mechanism type* (certification) can sit on either side of the intermediated/uncertain line depending purely on whether the text gives it automatic legal effect or merely permissive evidentiary weight.

**G. External influence excluded.** Diverse country-classification information sources (U7) and the Commission's own expert groups (U2, on distinctness grounds).

**H. Recital-only candidates.** The EU Observatory (U1) is by a clear margin the most significant recital-only finding across all three cases in this session.

**I. False-negative audit.** A targeted second pass for the full functional list confirmed no further operative-anchored candidates; the FLEGT-licensing relation (REL_C03_006) was itself a product of this second pass, having been easy to overlook on a first read given its single-paragraph, cross-referential form — a useful illustration of why the recall check matters even when it does not change the overall count materially.

## Completion checklist

- [x] Full operative corpus read (Articles 1–38, Chapters 1–9, Annexes I–II reviewed for cross-reference content)
- [x] R-T reconstructed before I classification
- [x] Regulator-facing intermediation considered (Article 15, rejected — U4; Article 10(2)(k) expert groups, rejected — U2)
- [x] Target-facing intermediation considered and found (customs, substantiated concerns, FLEGT licensing)
- [x] External influence distinguished from I (U7)
- [x] Reporting not mechanically equated with I
- [x] Advice/expertise not mechanically excluded
- [x] Recital-only positives prohibited (U1, the EU Observatory)
- [x] Cross-references followed (Article 26(2) ↔ Article 16; Article 16(12)/Article 23(a) ↔ Article 31; Article 10(3) ↔ Regulation (EC) No 2173/2005)
- [x] Second-pass recall check completed (surfaced REL_C03_006)
- [x] Boundary-case log completed
- [x] No previous empirical outputs consulted for their substantive content

```
THEORETICALLY_RECALIBRATED_READING_COMPLETE
SOURCE_BOUNDED
PREVIOUS_RESULTS_NOT_CONSULTED
READY_FOR_CRITICAL_REVIEW
```
