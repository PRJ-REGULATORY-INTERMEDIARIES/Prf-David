# Decision rules — GDPR Pilot 01 — version 1.0 (FROZEN before extraction)

**Frozen:** 2026-10-03, before any screening or extraction reading of the operative text beyond the structural parse. **Change policy:** any change is logged in §10, prospectively, with the earlier records it affects. No silent edits.

## 1. Units and identifiers
- Unit = a paragraph of an article (`GDPR.A{n}.P{k}`); points are `GDPR.A{n}.P{k}.pt{x}`; a single-paragraph article uses `P0`. Article 4 definitions are points of `GDPR.A4.P0`.
- Observation IDs: normative assignment `NA-nnnn`; position/device `PD-nnn`; qualified relation `QR-nnnn`; external reference `EXT-nnn`; subconfiguration `SC-nn`; architectural inference `AI-nn`; uncertainty `UNC-nnn`; human queue `HQ-nnn`.
- Provenance is many-to-many: an observation lists all supporting unit IDs separated by `;`.

## 2. Text baseline
Authentic OJ L 119, 4.5.2016 (EN) **with the 2018 corrigendum (OJ L 127, 23.5.2018, p. 2) applied** to the listed units; the application is logged (`01_SOURCES/parsed/corrigendum_application_log.json`). The consolidated EUR-Lex text is navigation only and has no legal effect. The baseline is a historical authentic text, **not asserted to be the currently applicable GDPR on 3 October 2026.**

## 3. Screening (every unit, article order)
`governance_relevance`: **Yes** = at least one extracted assignment, position, device or relation; **No** = none; **Uncertain**. `governance_role` (free tag): operative-assignment, relation-bearing, position-defining, scope/definitional-context, procedural-mechanism, substantive-rule-without-governance-structure, final/formal, etc. Editorial headings are never evidence of architectural membership. A "No" is a legitimate result.

## 4. Extraction records (kept separate)
1. **Normative assignment (NA):** subject position, action, object, function, modality, conditions/exceptions, counterpart (if legally identifiable), instrument/device, norm type (N0 ordinary; N1–N4 establishment-related), direct/derived, supporting units, limitations.
2. **Position / device (PD):** type-level positions; devices; no instances; `legal_multiplicity` if stated.
3. **Qualified relation (QR):** only when **both** parties (position types or defined categories) are identifiable in the same provision or by an explicit cross-reference. Otherwise the statement remains an NA.
4. **External reference (EXT):** every reference to another instrument, to national/Union law "as referred to", or to a standard.
5. Evidence of material establishment/exercise: **not collected** (layer X). All DEV carry `establishment_evidence = not_assessed`.

## 5. Modality vocabulary
`obligation` (shall / must); `prohibition` (shall not / prohibited); `permission` (may, for a party not an authority); `competence` (power conferred on an authority or body); `entitlement` (right of a data subject or similar); `definition`; `declaratory`. Hortatory verbs ("shall encourage") = `obligation (promotional)`.

## 6. Function vocabulary (V6 §3.3)
rule-making/standard-setting; implementation; interpretation/translation; information provision; monitoring; verification/assurance; enforcement; adjudication/dispute resolution; remediation; plus `representation/participation`, `authorization/designation`, `cooperation/coordination` (recorded as a residual tag; flagged as outside V6 §3.3 list).

## 7. Relation types (V6 §3.6)
authority/control; delegation/authorization; oversight/supervision; accountability; information/reporting; verification/assurance; review/adjudication; representation/participation; contractual/exchange; beneficiary/protective. Where a provision supports two types, two QR records are made. `cooperation` is **not** a V6 type; coded as `information/reporting` or `representation/participation` per content with a `type_note`, and flagged.

## 8. Establishment norms (N1–N4)
Classify by wording: **N1** "is established/hereby established"; **N2** "shall establish/provide for/designate/set up"; **N3** "may establish/set up"; **N4** effect conditional on further requirements (dates, acts). Compound and ambiguous wording is recorded as such. **A body or device is `legally_constituted` only under N1.** An obligation on Member States to provide for a body (N2) constitutes the obligation, and the body is a **type-level** position referenced by the Regulation; no national instance is created.

## 9. Devices
DEV requires the text to give identity **and** (operator **or** governing rules **or** bounded function). Otherwise INS-TYPE. Borderline → INS-TYPE + queue.

## 10. Accountability
Apply the v0.6.1 classes: INFO; ANSWERABILITY; ACCOUNTABILITY (all of: identifiable actor and forum, duty to explain/justify, questioning capacity, assessment/judgment capacity, grounded possibility of consequences); with a separate sufficiency assessment (sufficient/indeterminate). Reporting, supervision or publicity alone is never ACCOUNTABILITY. Exercise is not inferred.

## 11. Recitals
Interpretive context only. No assignment, position or relation is created from a recital alone. A recital may be cited in `evidence_note`.

## 12. Statuses
Per record: `modality`; `conditions`; `legal_status_of_norm` (baseline value: *in force; applicable from 25 May 2018 (Art. 99(2)); subject to unit-level conditions*); `epistemic_status` ∈ {documented, legal_constitution_evidenced, …}; operative provisions of the authenticated text receive `legal_constitution_evidenced(baseline)`, recitals `documented`; establishment/exercise = `not_assessed`.

## 13. Reachability is not transmission
No forwarding, data flow or operative dependency is inferred from graph paths. A path property is a *candidate* positional property until a legal rule links the relations.

## 14. Subconfigurations (S)
A candidate S is a set of QR/NA records sharing a stated pattern and a governance question, defined from relations, not from chapters. Fields: id, pattern, question, members, supporting units, chapters spanned, overlap with other S. Default status of every candidate grouping is **S**.

## 15. S→A (I1–I4) and anti-circularity
Apply I1–I4 and the directive's sequence: (1) delimit the governance question; (2) identify legally evidenced coupling *independently of the expected global property*; (3) examine the configurational consequence; (4) test rival groupings and boundary sensitivity. Answer the six questions of the directive for every candidate A. Outcomes: **integrated architecture / distinguishable architectures / overlapping or partially integrated architectures / indeterminate**. Kinds of connection are distinguished (shared participation; coordination or communication; qualified procedural dependency; mandatory interface; conditional dependency; integration through distributed powers/duties/decisions) and are **not** an ordered scale. A shared authority is insufficient. Absence of an edge does not establish separation. No numeric integration scores or thresholds.

## 16. Closure and absence
Absence-dependent claims require a stated coverage; external references with constitutive dependency make them `undetermined` or "within the declared corpus".

## 17. Selection of the worked trace
After screening and construction of the candidate S list, the worked legal trace is chosen **by a rule fixed here**: among candidate S/A groupings that cite supporting units from **at least two chapters**, draw one with a seeded pseudo-random draw (`random.Random(seed)`, seed = integer value of the first 8 hex digits of the SHA-256 of the original authentic HTML, `b5085317`), over the list sorted by SC id. A second trace is chosen deterministically: the candidate with the **largest number of distinct supporting units**. Neither is chosen for expected support of RGAM.

## 18. Machine status
All records are machine-generated and **provisional**. Repetition by the same model is not inter-coder reliability. Consequential ambiguity goes to the human queue (HQ), not silently resolved.

## 19. Layer discipline
D (strategies, logics) and X (implementation, operation) are not coded in the pilot beyond a note where the text itself states an implementation requirement.

## 20. Change log (prospective)
| Version | Date | Change | Earlier records affected |
|---|---|---|---|
| 1.0 | 2026-10-03 | Initial freeze | — |
| 1.1 | 2026-10-03 | Direction convention for entitlements and rights: `origin` = the **obligor** (position bearing the duty or the power exercised toward the counterpart); `counterpart` = the right-holder or addressee; modality `entitlement (of counterpart)`. Needed because rights are stated from the right-holder's side. Also: an NA is made only where no counterpart is legally identifiable; where a QR exists it is not duplicated as an NA | QR for A7.P3 (draft direction reversed, recorded in its `unresolved_interpretation`) |
| 1.2 | 2026-10-03 | Direction clarification: `origin` = the legal subject of the statement (obligor/power-holder); the *governance direction* in V6 terms (e.g. "supervisory authority oversees controller") is written in `type_note` as `gov-direction: X→Y` where it differs from origin→counterpart. `depends_on` field added to NA records (devices/positions the assignment relies on) | None (applied from Chapter IV on; earlier QRs read origin→counterpart as written) |
