# Candidate subconfigurations (S) — GDPR Pilot 01

**Status:** `MACHINE_PROVISIONAL`. Built from the 395 extracted records (157 normative assignments, 238 qualified relations) by `reconstruct.py`. Nothing here is an architecture (A); every group is an **S** until I1–I4 are applied (`ARCHITECTURAL_INFERENCE_REGISTER.csv`).

## How the candidates were produced (and the bias that comes with it)

- **Rule (DECISION_RULES §14):** a candidate S is a set of records sharing a stated *relation pattern* and a governance question; editorial chapters are not used for membership.
- **Procedure:** after the extraction was complete, I wrote fifteen predicates over the extracted records (party types, relation type, function words, supporting units, `depends_on`), each representing a functional pattern. The patterns come from my reading of the text and from V6's vocabulary (delegation, verification, oversight, authorization…); they are therefore **analyst-defined, not discovered by an independent algorithm**. This is the main bias of this stage. A second coder or an independent clustering method has not been run.
- **Chapters spanned** are computed from *all* supporting units of the members (including linking provisions such as Art. 57–58 points linked to Chapter IV relations), so they overstate "cross-chapter" content for some S.
- **Predicate quality.** The predicates were not tuned against a gold set. Inspection of SC-10 shows that 6 of its 34 members are false positives (records that merely mention a complaint right in an information duty); the worked trace therefore uses a curated core.
- **Residual.** 24 of 395 records fall in no candidate S (e.g. fine provisions stated as assignments of the SA, Art. 7(1) consent evidence, Art. 8, Art. 94(2), Art. 99). They are listed in `sc_data.json`; most are predicate gaps, not substantive exclusions.

## Candidate list

| S | Name | QR | NA | Articles touched | Chapters of supporting units |
|---|---|---:|---:|---:|---|
| SC-01 | Individual information, access and control rights against controllers | 41 | 0 | 19 | II, III, IV, V, VII |
| SC-02 | Supervisory-authority oversight and enforcement over controllers and processors | 33 | 0 | 16 | IV, V, VI, VII, VIII |
| SC-03 | Controller–processor delegation, instruction and audit | 18 | 6 | 11 | IV, VI, VIII |
| SC-04 | Internal compliance function (data protection officer) | 9 | 8 | 4 | IV |
| SC-05 | Codes of conduct: approval, accreditation of monitors, monitoring and sanction | 14 | 14 | 11 | IV, V, VI, VIII |
| SC-06 | Certification: accreditation of certification bodies, issue/withdrawal, approval of criteria | 12 | 17 | 12 | IV, V, VI, VII, VIII, X |
| SC-07 | Cooperation and consistency among supervisory authorities, the Board and the Commission | 76 | 15 | 24 | IV, V, VI, VII, VIII |
| SC-08 | Commission rule-making (delegated and implementing acts) and its control | 12 | 17 | 17 | III–VII, X, XI |
| SC-09 | Transfers of personal data to third countries and international organisations | 11 | 15 | 10 | V, VI, VII |
| SC-10 | Remedies and judicial review | 28 | 6 | 18 | III–VIII |
| SC-11 | Member State specification, establishment and notification duties | 28 | 33 | 34 | I–IX |
| SC-12 | Reporting lines to institutions | 8 | 0 | 7 | IV, VI, VII, X, XI |
| SC-13 | Constitution and internal organisation of the European Data Protection Board | 12 | 11 | 8 | VII |
| SC-14 | Constitution, independence and competence of national supervisory authorities | 29 | 24 | 17 | IV, V, VI, VIII |
| SC-15 | Regulated-side assignments without an identifiable counterpart (self-regulatory duties) | 0 | 35 | 19 | II, IV, V, VIII, IX |

(Counts are composition, not significance — V6 §6.6.)

## Overlaps (shared members)

Largest overlaps: SC-11/SC-14: 18; SC-02/SC-14: 9; SC-07/SC-14: 9; SC-10/SC-11: 9; **SC-02/SC-07: 7**; SC-05/SC-15: 7; SC-07/SC-08: 7; SC-03/SC-04: 6; SC-06/SC-14: 6; SC-07/SC-11: 6; SC-01/SC-10: 5; SC-07/SC-09: 5; **SC-05/SC-06: 4**. Shared membership shows that the same provisions support several patterns; it is **not** evidence of integration (v0.6.1 §6.2).

## Observations that follow from the candidate set (not from a hypothesis)

1. **One candidate (SC-15) contains no relation at all.** 35 assignments on controllers/processors (e.g. Arts 24(1), 25, 32(1), 35(1)) have no legally identifiable counterpart or forum. A relation-pivotal reconstruction leaves them outside any S; see `THEORY_PROBLEMS_ENCOUNTERED.md` (TP-06).
2. **SC-14 and SC-11 are mostly obligations on Member States and N2 provisions.** The national authorities (Arts 51(1), 54(1)(a)) and many specification clauses are constituted by Member State law outside W (EXT-007, EXT-015).
3. **SC-07 is the largest candidate (100 supporting units; 91 members), and 76 of its members are relations**; it is also the one in which the Board — the only body whose establishment is stated by an N1 provision (Art. 68(1)) — is a party.

## Trace selection (DECISION_RULES §17, applied as pre-fixed)

Eligible S (supporting units from ≥2 chapters): SC-01, 02, 03, 05, 06, 07, 08, 09, 10, 11, 12, 14, 15 (13 of 15). Seed = integer value of `b5085317` = 3,037,221,655; `random.Random(seed).choice` over the sorted list → **SC-10**. Deterministic second choice (largest number of distinct supporting units, 100) → **SC-07**. Neither was chosen for expected support of RGAM; both are traced in `WORKED_LEGAL_TRACE.md`.
