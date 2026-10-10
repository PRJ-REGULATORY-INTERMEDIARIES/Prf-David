# 02 — Evidence ledger

**Purpose.** Hold the evidence for the four cases in one place, with a strict separation between what was observed in the frozen record, what is an interpretation of it, and what is not established. No narrative. No scores. No method ranking.

**Reading rule.** "Baseline" = the reconstruction that applied David's framework relatively directly. "Controlled" = the reconstruction that applied the same framework with additional explicit procedural and inferential controls. Both arms received the identical, hash-verified official source file for each case (`SOURCE_COMPLETENESS_AUDIT.md`, `AI_ACT_SOURCE_RECOVERY_REPORT.md`).

**Standing caveat on all counts.** Under the frozen materiality rule, longer or more numerous output never converts a difference into a gain. Counts below are composition descriptors, not quality evidence.

---

## 0. Family-level observations (all four cases)

**OBSERVED** (`PRE_ADJUDICATION_DESCRIPTIVE_SUMMARY.md`, 2026-10-07):

- 264 comparative units constructed across the five comparative levels C0–C4; 113 of them `M1_SUBSTANTIVE_EQUIVALENT`.
- 151 units carry a difference (M2–M7); 96 of those are `COMPARATIVELY_MATERIAL`.
- Material differences by level: C0 = 1, C1 = 30, C2 = 26, C3 = 23, C4 = 16.
- 56 human-review cards (SCF 12, CBAM 16, AI Act 21, Directive 7). 19 of the 56 turn on legal evidence outside the instrument's own text.
- Blind assignment: baseline was Proposition A in 31 cards, controlled in 25, by a deterministic hash rule.
- D4 (inferential explicitation): `RGAM_CLEARER` 38, `EQUIVALENT` 21, `NOT_APPLICABLE` 37 — no `V8_CLEARER`.
- D5 (boundary / sensitivity control): `RGAM_GAIN` 41, `DIFFERENT_NONORDERABLE` 20, `EQUIVALENT` 2, `NOT_APPLICABLE` 33 — no `V8_GAIN`.
- D3 (vertical traceability): `EQUIVALENT` 51, `NOT_APPLICABLE` 45 — **neither arm clearer on traceability in any unit.**
- D6 (uncertainty calibration): `INDETERMINATE` 93, `WELL_CALIBRATED_BOTH` 3 — calibration could not be assessed pre-adjudication in 93 of 96 material units.
- D7/D8 risk flags (conditional on open cards, per-method, not a comparison): possible over-inference baseline 38 / controlled 6; possible material omission baseline 55 / controlled 15.
- Every one of the 56 cards remains `OPEN_AWAITING_HUMAN_ADJUDICATION`. QA check 28: no human decision simulated; no adjudication register created.

**INTERPRETED:**

- The differences concentrate in the upper transitions and in the epistemic layer: 65 of the 96 material differences sit at C2, C3 or C4, i.e. at relationship→configuration, configuration→architecture, and uncertainty/stopping. Only one material difference arose at the evidence level C0. The arms largely agree about what the legal text says and diverge about what may be inferred from it.
- The D3/D4 contrast is informative. The controlled arm was judged clearer on **exposing the inferential step** in 38 units and never clearer on **recoverability of the chain**. Read against David §6.9, this suggests the baseline already satisfied vertical traceability; what the controls added was explicitness about the move between levels, not auditability of the evidence.
- The absence of any `V8_GAIN` on D5 and of any `V8_CLEARER` on D3/D4 is a one-sided distribution. It is consistent with the controlled procedure doing more of this work by construction, and it is therefore weak evidence of quality: a procedure that requires a rival-grouping field will be recorded as stating rival groupings.

**NOT ESTABLISHED:**

- That either arm is more accurate. No adjudication of the 56 exists.
- That the D7/D8 flag counts compare the arms. The QA report states they follow where each arm records a proposition the other does not.
- That the differences are attributable to the controls rather than to prompt length or structure. Both arms and the comparator ran on the same model (`claude-sonnet-5-5`); no arm-blind model control was run.

---

## 1. SCF — Regulation (EU) 2023/955 (Social Climate Fund)

### Main substantive convergence — OBSERVED
26 of 57 units `M1_SUBSTANTIVE_EQUIVALENT`, including 9 of 11 at C0 and 9 of 16 at C1. Both arms reconstruct the same core: Member State submits a Social Climate Plan; Commission assesses and decides by implementing act; an agreement follows; payments are conditioned on milestones and targets; financial control and audit obligations attach; monitoring, reporting and evaluation run on a shared indicator set; transfers between the Fund and shared-management programmes are available. The baseline recorded 15 claims, 9 typed relations, 3 configurations, 1 bounded architecture; the controlled arm recorded 7 subconfigurations (SC-01…SC-07) and 3 architecture candidates.

### Main configurational difference — OBSERVED
6 material differences at C2. The controlled arm separated public consultation on the Plan (SC-02), protection of financial interests and internal control (SC-04), monitoring/reporting/evaluation (SC-05), the Parliamentary social climate dialogue (SC-06) and Fund/shared-management transfers (SC-07) as distinct subconfigurations. The baseline grouped the same material into 3 configurations.

### Main architectural difference — OBSERVED
8 material differences at C3, the largest concentration of any case at that level. Baseline: one bounded formal architecture covering the whole Fund design (Arts. 1–27 and Annex III). Controlled: ARCH-01 [SC-01,02,03,04,07] `INTEGRATED`; ARCH-02 [SC-05] `OVERLAPPING_OR_PARTIALLY_INTEGRATED` (shared indicator interface); ARCH-03 [SC-06] `INDETERMINATE` (I3 and I4 not satisfied) — instrument-level result `OVERLAPPING_OR_PARTIALLY_INTEGRATED`, highest level reached A. Card HQ-SCF-02 states this disagreement exactly.

### Relevant external dependency — OBSERVED
46 external references recorded, 13 with `constitutive_dependency = Y`; all `not_checked` / `outside_corpus_not_expanded`. 5 of the 12 cards depend on evidence outside the Regulation (HQ-SCF-04, -06, -07, -08, -10). D1 on material units: `EXTERNAL_DEPENDENCY` 3, `INDETERMINATE` 8, `PARTIALLY_SUPPORTED` 6, `SUPPORTED` 5.

### Uncertainty / stopping issue — OBSERVED
Baseline uncertainty register: 12 entries, covering source/reference, actor, action, counterparty, modality, condition, cross-provision, architectural-inference and stopping-rule uncertainty. Baseline stopping record: stops at architecture, refuses regime and implementation claims. Controlled arm: stops at A but records one `INDETERMINATE` candidate; D6 `INDETERMINATE` in 20 of 22 material units.

### Human-validation evidence — ARCHIVED 2026-10-08 (no recorded justification)
HQ-SCF-02 (C3; triggers H5, H6, H11; priority HIGH; no external dependency): blind decision **B** = the controlled reconstruction. Archived in `NEW TEST 3x3/16_HUMAN_VALIDATION_IMPORT_2026-10-08/`; no justification was captured. See `01_SOURCE_MAP.md` §7.

### Evidence of useful methodological control — INTERPRETED
Two controls are implicated in the one HIGH-priority architectural card: the **configuration-boundary / coupling test** (I2–I3: what property becomes attributable to the whole rather than to each part) and the **architecture-candidate status** (a grouping stays a candidate until I1–I4 are met). The question in HQ-SCF-02 is exactly David's container fallacy (§6.8): whether provisions in one act necessarily form one architecture. The controlled arm declined to assume it; the reported decision agreed.

### Evidence of excessive procedural decomposition — OBSERVED/INTERPRETED
482 analytical records and 27 artefacts in the controlled arm against 40 records and 10 artefacts in the baseline, for a case where 26 of 57 units are substantively equivalent and the architectural disagreement reduces to one HIGH card. The frozen rule forbids reading this as a gain; it is equally not evidence of waste. What is observable is that the ratio of recorded material to contested inferential decisions is roughly 480:1 at the case level, and that 19 internal review items were generated internally before the paired comparison added 12 more.

### NOT ESTABLISHED for SCF
Whether monitoring/evaluation belongs inside the architecture; whether the Parliamentary dialogue channel is an architecture at all; whether either arm's confidence level is warranted (D6 indeterminate in 20 of 22 units).

---

## 2. CBAM — Regulation (EU) 2023/956

### Main substantive convergence — OBSERVED
27 of 70 units `M1`, including 14 of 15 at C0 — the strongest evidence-level agreement in the family. Both arms reconstruct: authorisation of CBAM declarants; declaration of embedded emissions; verification by accredited verifiers; a registry; purchase and surrender of certificates; review and enforcement. Baseline: 16 claims, 10 relations, 5 configurations, 1 architecture. Controlled: 101 qualified relations, 11 subconfigurations, 7 architecture candidates.

### Main configurational difference — OBSERVED
8 material differences at C2. The controlled arm separated the transitional reporting regime (SC-07), the delegated/implementing-act frame (SC-08), third-country listing and the conditional electricity arrangement (SC-09), circumvention (SC-10) and reporting to Parliament and Council (SC-11) from the core.

### Main architectural difference — OBSERVED
8 material differences at C3. Baseline: one formal architecture over the whole design, medium-high confidence, no regime claim. Controlled: ARCH-01 [SC-01,04,05] `INTEGRATED`; ARCH-05 [SC-09] `INTEGRATED`; ARCH-02 (verification + registration), ARCH-03 (transitional), ARCH-04 (delegation), ARCH-06 (circumvention) all `INDETERMINATE` on I3; ARCH-07 (the whole instrument) `OVERLAPPING_OR_PARTIALLY_INTEGRATED` with I2, I3, I4 indeterminate. Card HQ-CBAM-10 states this disagreement.

### Second architectural-level observation — OBSERVED
Notably, the controlled arm's verification candidate (ARCH-02, containing SC-03 "accreditation of verifiers and verification of declared embedded emissions") is `INDETERMINATE` on I3/I4 — i.e. the arm declined to say that verification is integrated into the core architecture, on the ground that the coupling is not established in the instrument.

### Relevant external dependency — OBSERVED
33 external references, 17 constitutive. Two are directly load-bearing for intermediation: **EXT-014** — the position "national accreditation body" is constituted by Regulation (EC) No 765/2008 Art. 4(1); **EXT-018** — the status "accredited verifier" for the purposes of this Regulation arises from accreditation under Commission Implementing Regulation (EU) 2018/2067. Both `not_checked`. 7 of the 16 cards depend on evidence outside the Regulation.

### Uncertainty / stopping issue — OBSERVED
Baseline uncertainty register: 11 entries; the baseline stopping record explicitly notes that although Art. 1 says CBAM complements the EU ETS, the corpus does not supply the material needed to map the regime boundary — and stops. Controlled arm: 4 of 7 candidates `INDETERMINATE`; D6 `INDETERMINATE` in 28 of 29 material units.

### Human-validation evidence — ARCHIVED 2026-10-08 (no recorded justification)
- **HQ-CBAM-04** (C1; H1, H2, H10; HIGH; no external dependency): blind decision **B** = the controlled reconstruction, which names the Member State as seller and repurchaser of certificates and the Commission as platform operator, registrar and canceller. The baseline proposition left the seller unidentified. Art. 20(1) reads: "A Member State shall sell CBAM certificates on a common central platform to authorised CBAM declarants established in that Member State."
- **HQ-CBAM-10** (C3; H5, H6, H11; HIGH): blind decision **A** = the controlled reconstruction (integrated core plus overlapping and uncoupled arrangements).

### Evidence of useful methodological control — INTERPRETED
HQ-CBAM-04 implicates the **actor / counterparty precision control** (every relation must have identifiable, named parties; no fabricated or generic counterparty). This is the one validated case in which the control changed a *relational* fact, not an inferential boundary — and it is the clearest instance in the family where the added discipline recovered something the text states plainly and the baseline left blank.
HQ-CBAM-10 implicates the same coupling / candidate-status controls as HQ-SCF-02.

### Evidence of excessive procedural decomposition — OBSERVED
488 analytical records vs 43; 27 artefacts vs 10; 16 internal review items plus 16 paired cards. 48 of 101 qualified relations are `information_reporting` — the largest single relation class — and the frozen materiality operationalization treats purely informational/administrative relations as non-material. A substantial share of the controlled arm's relational volume therefore cannot, by the comparison's own rule, bear on any material difference.

### NOT ESTABLISHED for CBAM
Whether verification is architecturally integrated into the core (I3 indeterminate on both sides of the question); whether the transitional regime is part of the same architecture; the confidence warranted for either architectural claim.

---

## 3. AI Act — Regulation (EU) 2024/1689

### Main substantive convergence — OBSERVED
30 of 85 units `M1`, including 12 of 13 at C0 and 6 of 18 at C3. Both arms reconstruct: provider and deployer duties across the high-risk lifecycle; conditional third-party conformity assessment; designation of notified bodies; harmonised standards and presumptions of conformity; national market surveillance with a Union safeguard; a distinct Commission-centred pathway for general-purpose AI models. Baseline: 14 claims, 11 relations, 3 configurations (K01–K03), 1 architecture. Controlled: 281 qualified relations, 19 subconfigurations, 9 architecture candidates.

### Main configurational difference — OBSERVED
11 material differences at C2 and 15 at C1 — the largest relational and configurational divergence in the family. The controlled arm produced 19 subconfigurations where the baseline produced 3 configurations. 26 of 85 units are `M4_RGAM_ONLY` (controlled-arm-only propositions), concentrated at C1 (10) and C2 (6).

### Main architectural difference — OBSERVED
5 material differences at C3. Baseline: one bounded formal architecture, differentiated, hybrid and multilevel, over three pathways, high confidence, no regime claim. Controlled: 5 candidates `INTEGRATED` (incl. ARCH-02 [SC-01,02,03,18] conformity, ARCH-03 [SC-04,05,12,17] enforcement, ARCH-01 [SC-06,07,16] GPAI, ARCH-04 sandboxes, ARCH-06 delegation), 3 `INDETERMINATE`, and ARCH-09 (the whole instrument, 16 subconfigurations) `OVERLAPPING_OR_PARTIALLY_INTEGRATED` with I3 `NOT_SATISFIED` — i.e. the controlled arm found no property attributable to the instrument as a whole. Card HQ-AI-14 states this disagreement.

### The counterexample — OBSERVED
**HQ-AI-12 is at C2, not C3.** It is a configuration-membership and boundary question (triggers H4, H6), and the only one of the six validated cards at that level. The disagreement is where three groups of relations belong: designation of notified bodies, operator duties toward authorities, and incident reporting.
- Controlled arm (Proposition A): seven separate overlapping arrangements, with **designation grouped with certification** (SC-02 next to SC-03, both later inside ARCH-02).
- Baseline (Proposition B): three arrangements, with **designation grouped with market surveillance** and incident/information duties placed there too.

### Relevant external dependency — OBSERVED
59 external references, **39 constitutive** — by far the highest in the family. 5 of the 21 cards depend on external evidence. D1 on material units: `SUPPORTED` 15, `EXTERNAL_DEPENDENCY` 8, `PARTIALLY_SUPPORTED` 6, `INDETERMINATE` 7.

### Uncertainty / stopping issue — OBSERVED
Baseline: 9 uncertainty entries; stops at Level III architecture, declines regime and a single governance logic for every pathway. Controlled: 30 `SOURCE_AMBIGUITY` entries (the highest of the four cases), 35 internal review items; D6 `INDETERMINATE` in all 36 material units.

### Human-validation evidence — ARCHIVED 2026-10-08 (no recorded justification)
- **HQ-AI-14** (C3; H5, H6, H11; HIGH): blind decision **B** = the controlled reconstruction (several partially integrated candidates; no whole-level property).
- **HQ-AI-12** (C2; H4, H6; HIGH): blind decision **B** = **the baseline reconstruction** (three arrangements; designation with market surveillance).

### Evidence of useful methodological control — INTERPRETED
HQ-AI-14 implicates the **coupling test and whole-level property rule**: I3 `NOT_SATISFIED` for the whole instrument meant no architectural property could be asserted for the Regulation as such. The reported decision agreed. This is the case where the baseline's confidence was highest ("high confidence") and where the control had most to constrain.

### Evidence of excessive procedural decomposition — OBSERVED/INTERPRETED
1,163 analytical records vs 38; 19 subconfigurations vs 3 configurations; 9 architecture candidates vs 1 architecture; 35 internal review items plus 21 paired cards. 136 of 281 qualified relations are `information_reporting`. HQ-AI-12 is the one validated instance where the finer partition was **not** preferred.
Important qualification: the controlled arm did not finally keep designation and certification apart — ARCH-02 groups SC-01, SC-02, SC-03 and SC-18 as `INTEGRATED`. So the finer subconfiguration layer did not resolve the membership question; it deferred it to the architecture layer and then resolved it in a way the reported decision did not endorse.

### NOT ESTABLISHED for the AI Act
Which partition of the high-risk and market-surveillance relations is correct beyond the single reported decision; whether a whole-level property can be attributed to the Regulation; whether the 39 constitutive external dependencies would change the picture if verified.

---

## 4. Directive 86/361/EEC

### Main substantive convergence — OBSERVED
30 of 52 units `M1` — the highest proportion in the family (58%), including 13 of 16 at C1 and 5 of 12 at C3. Both arms reconstruct the same mechanism: the Commission requests CEPT to draw up NETs; NETs count as common conformity specifications; approved testing laboratories test and certify; a certificate of conformity with a published specification removes further testing; competent authorities recognise certificates for type approval; recognition may be suspended, with consultation, a laboratory opinion, Committee referral, delisting and revocation. Baseline: 21 register records, 12 relations, 1 configuration, 1 architecture. Controlled: 39 qualified relations, 6 subconfigurations, 2 architecture candidates.
Only 9 of 22 differences were material — the lowest in the family. Materiality concentrates at C4 (4 of 9), i.e. in the epistemic layer rather than in the substance.

### Main configurational difference — OBSERVED
1 material difference at C2. The two arms essentially agree on the configuration.

### Main architectural difference — OBSERVED
2 material differences at C3, but they are decisive. Baseline: a bounded formal legal architecture for conformity assurance and mutual recognition of the covered process, **high confidence**. Controlled: both candidates `INDETERMINATE`; ARCH-01 satisfies I1–I3 but not I4; instrument-level result `INDETERMINATE`; **highest level reached = S, not A** — the only case in which the controlled arm stopped below architecture. Card HQ-DIR-01 states this disagreement and carries five triggers (H5, H8, H9, H10, H11).

### Relevant external dependency — OBSERVED
Only 10 external references, but 4 constitutive and two of them load-bearing for the architectural question:
- **EXT-005** — a NET's legal constitution rests on a Memorandum of Understanding between CEPT signatories, outside the Directive.
- **EXT-006** — which laboratories count as "approved testing laboratories" (the issuers of recognised certificates and of the Art. 8(3) opinion) is fixed by the **CEPT accreditation system**, outside the Directive. The Directive's own Art. 2(8) defines an approved laboratory by reference to conformity *with that external system*.
- EXT-009 (Art. 9 of Directive 73/23/EEC for electrical-safety decisions) and EXT-010 (non-prejudice clause to Directive 83/189/EEC) further qualify absence-dependent claims.
Both cards flagged for external dependency (HQ-DIR-01, HQ-DIR-05) are in this case.

### Uncertainty / stopping issue — OBSERVED
This is the case where the stopping rule did the most work. The baseline's own stopping record states that the Directive "does not establish … the realized significance or substitutability of laboratories" — it recognised the limit and still asserted the architecture. The controlled arm treated the same facts as a reason not to assert the architectural level at all. 16 `SOURCE_AMBIGUITY` and 5 `EXTERNAL_DEPENDENCY` uncertainty entries; D1 on material units has **no** `SUPPORTED` at all (`EXTERNAL_DEPENDENCY` 2, `INDETERMINATE` 4, `PARTIALLY_SUPPORTED` 3).

### Human-validation evidence — ARCHIVED 2026-10-08 (no recorded justification)
**HQ-DIR-01** (C3; H5, H8, H9, H10, H11; HIGH; external dependency YES): blind decision **A** = the controlled reconstruction, which declines the architectural level and stops at the subconfiguration level because the constitution of NETs, of approved laboratories and of the safeguard branches rests on instruments outside the Directive.

### Evidence of useful methodological control — INTERPRETED
This is the strongest case for the **external-dependency marking control** and for the **stopping rule as an explicit output field**. The two arms read the same provisions identically; they differ only on whether an architectural claim may be asserted when the actors who perform its central function are constituted elsewhere. The controls here changed the top-level conclusion of the case, not its description.
It is also the case where the control has substantive, not merely procedural, consequence for David's agenda: the Directive governs *through* laboratories while the governance *of* those laboratories sits outside the instrument. That is a finding about the law, reached through the control.

### Evidence of excessive procedural decomposition — OBSERVED
232 analytical records vs 47; 27 artefacts vs 10; 19 internal review items for a 12-article Directive on which the arms agree in 30 of 52 units. For the smallest instrument, the controlled arm's overhead ratio is the highest relative to the material at issue.

### NOT ESTABLISHED for the Directive
Whether the architectural level is in fact warranted; the confidence either claim deserves; what the external instruments actually provide (none was retrieved; retrieval was not authorized).

---

## 5. Cross-case pattern in the six validated cards — INTERPRETED

| Card | Level | What the control did | Reported decision |
|---|---|---|---|
| HQ-CBAM-04 | C1 relational | named the actor the text names | controlled |
| HQ-AI-12 | C2 configurational | partitioned relations more finely; deferred membership to the A layer | **baseline** |
| HQ-SCF-02 | C3 architectural | refused to treat one act as one architecture | controlled |
| HQ-CBAM-10 | C3 architectural | refused to treat one act as one architecture | controlled |
| HQ-AI-14 | C3 architectural | refused a whole-level property when I3 failed | controlled |
| HQ-DIR-01 | C3 architectural | refused the architectural level under external constitution | controlled |

**Interpretation.** Within this purposive set of six, the controls were endorsed where they *restrained an upward inference* or *enforced a named party*, and were not endorsed where they *subdivided a representation that was already adequate*. The one non-endorsement is at the relationship→configuration transition; the four endorsements at the architectural level are at configuration→architecture and architecture→proposition.

**Not established.** That this pattern holds beyond six purposively chosen cards. The set was selected for centrality, four of the six are C3, and the sample cannot support a rate, a proportion or a generalisation. It is a pattern worth testing, not a result.
