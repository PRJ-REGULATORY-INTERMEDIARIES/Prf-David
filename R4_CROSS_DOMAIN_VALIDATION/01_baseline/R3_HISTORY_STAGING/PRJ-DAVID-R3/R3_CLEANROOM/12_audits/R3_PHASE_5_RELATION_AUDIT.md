# R3 — Phase 5 Relation Audit

Status: complete for researcher review. This audit records provisional regulatory-relation reconstruction only. It does not adjudicate final R/I/T roles, intermediaries, mechanisms, or causal explanations.

## 1. Scope and clean-room compliance

Phase 5 used only the validated R3 clean-room inputs:

- `02_corpus/` — validated R3 legal corpora;
- `03_instrument_profiles/` — Phase 3 whole-instrument profiles and reconstruction memos;
- `04_actor_register/ACTOR_REGISTER.csv`;
- `04_actor_register/ACTOR_PROVISION_MAP.csv`;
- `04_actor_register/ACTOR_ALIAS_LOG.csv`.

No previous project folder, prior empirical corpus, previous acquisition manifest, previous case name, previous classification, or previous hash was used. No external empirical material was imported. No new source retrieval was required in Phase 5; source authority remains the independently acquired official EU corpus validated in Phase 1.

Phase 5 stopped before mechanism reconstruction and before any Phase 6 construction.

## 2. Required outputs

Created:

- `06_relations/RELATION_CANDIDATES.csv`;
- `06_relations/CROSS_PROVISION_RELATION_MAP.csv`;
- this audit file.

No files were created in `07_mechanisms/`.

## 3. Corpus and relation counts

| CELEX | Candidate relations | Direct two-actor relations | Relations with third actor candidate | Review-required | E1 | E2 | E3 |
|---|---:|---:|---:|---:|---:|---:|---:|
| 32003L0087 | 9 | 8 | 1 | 1 | 9 | 0 | 0 |
| 32015D1814 | 6 | 5 | 1 | 2 | 6 | 0 | 0 |
| 32018R0842 | 10 | 7 | 3 | 3 | 9 | 1 | 0 |
| 32021R1119 | 11 | 9 | 2 | 5 | 11 | 0 | 0 |
| 32023R0955 | 20 | 14 | 6 | 7 | 20 | 0 | 0 |
| **Total** | **56** | **43** | **13** | **18** | **55** | **1** | **0** |

All 56 rows have `role_status=PROVISIONAL`. The 13 third-actor rows preserve the direct relation and add only a legally connected named actor. No row applies a final intermediation label.

## 4. Evidence and reconstruction audit

The candidate register uses the required provisional fields `R_candidate`, `T_candidate`, and `third_actor_candidate`. Every row contains source provisions and source anchors. The evidence levels are:

- `E1_EXPLICIT`: 55 relations;
- `E2_CROSS_PROVISION_RECONSTRUCTED`: 1 relation, `REL-32018-004`;
- `E3_INFERRED`: 0 relations.

The cross-provision map contains 237 rows for the 56 relations. Every relation has at least the four components `R_AUTHORITY`, `T_OBLIGATION`, `R_T_LINK`, and `RELATION_PURPOSE`; third-actor relations add `THIRD_ACTOR_ROLE`. The map does not use `INTERMEDIARY_FUNCTION`.

Reconstruction complexity in the candidate register:

- `SINGLE_PROVISION`: 51;
- `CROSS_ARTICLE`: 5;
- `OPERATIVE`: 53;
- `OPERATIVE;ANNEX`: 2;
- `OPERATIVE;RECITAL`: 1.

The only recital-dependent candidate is `REL-32018-004`. It remains provisional and requires researcher review because the actor class appears as both selling and receiving Member States and the agency-based actor is identified from the connected recital context.

## 5. Ambiguity, role switching, and third actors

Role uncertainty totals are 38 LOW, 17 MEDIUM, and 1 HIGH. Relation uncertainty totals are 38 LOW and 18 MEDIUM. The HIGH role-uncertainty case is `REL-32018-004`.

`role_switch_review=YES` is flagged on 54 relation rows. This reflects 13 actor-law pairs in which the same actor appears in more than one provisional position across the candidate set:

- 32003L0087: Member States; Competent authorities;
- 32015D1814: Member States; Common auction platform;
- 32018R0842: Member States; European Commission; Central Administrator;
- 32021R1119: Member States; European Commission; Management Board; European Scientific Advisory Board on Climate Change;
- 32023R0955: Member States; European Commission.

This is a review flag, not a finding that the actor legally changes role.

Third-actor candidates are limited to the 13 rows where the cited provisions expressly connect the actor to the relation. They include competent authorities, auction platforms, the agency-based market actor, the Central Administrator, the European Environment Agency, relevant stakeholders, implementing entities or authorities, audit bodies, and OLAF. Their inclusion does not test or establish intermediation.

## 6. Version, source, and integrity observations

Phase 5 did not replace or consolidate the Phase 1 primary coding sources. All anchors point into the validated R3 numbered corpus. No version conflict or corrigendum issue was newly introduced at this stage.

During integrity validation, one malformed actor ID in `REL-32018-004` was corrected from a CELEX-shaped identifier to the validated actor-register identifier `ACT-32018-004`. The corrected register was then checked against `ACTOR_REGISTER.csv`; all candidate actor IDs and canonical names now match.

Validation results:

- candidate rows parsed: 56;
- cross-provision rows parsed: 237;
- actor-ID/name mismatches: 0;
- relations with fewer than three evidence components: 0;
- non-provisional role-status violations: 0;
- forbidden `INTERMEDIARY_FUNCTION` components: 0;
- mechanism records created: 0.

## 7. Excluded non-relations

The following were excluded from the relation register:

- mere co-mention of actors without a provision-specific legal action or directed connection;
- broad participation or consultation language without a reconstructable R-to-T link;
- actor categories appearing only as contextual background and not connected to the cited regulatory object;
- any relation that would require a mechanism judgment or an intermediation test to exist;
- any LAW × INTERMEDIARY construction.

Exclusion from this Phase 5 candidate register is not a negative legal conclusion; it records that the relation did not pass the provisional reconstruction threshold.

## 8. Upstream gaps and researcher decisions required

Before corpus construction or mechanism analysis, the researcher should decide:

1. whether the 18 review-required relations can retain their provisional actor assignments;
2. how to adjudicate the 13 actor-law role-switch flags;
3. whether `REL-32018-004` should remain in the corpus as a recital-supported relation or be split into narrower candidates;
4. whether the named third actors should remain in the relation register after the direct relation is frozen;
5. whether any broad actor class should be narrowed to a specific institutional or legal entity.

No final R/I/T decision is made here.

## 9. Q1–Q15 gate

| Gate | Result |
|---|---|
| Q1 — validated clean-room inputs only | PASS |
| Q2 — required candidate fields present | PASS |
| Q3 — direct relations preserved | PASS |
| Q4 — third actors restricted to explicit legal connection | PASS |
| Q5 — no intermediation test applied | PASS |
| Q6 — no mechanism coding | PASS |
| Q7 — E1/E2/E3 evidence discipline | PASS |
| Q8 — cross-provision map complete | PASS |
| Q9 — provisions and anchors recorded | PASS |
| Q10 — no final R/I/T adjudication | PASS |
| Q11 — uncertainty and review flags recorded | PASS |
| Q12 — role-switch review flags recorded | PASS |
| Q13 — excluded non-relations documented | PASS |
| Q14 — no Phase 6 outputs created | PASS |
| Q15 — required deliverables and stopping condition satisfied | PASS |

Phase 5 is complete and stopped pending researcher authorization. No corpus construction, mechanism reconstruction, or cross-case synthesis should begin from this audit alone.

R3_PHASE_5_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION
