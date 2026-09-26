# R3 — Phase 6B Targeted Adjudication Audit

Status: complete. Phase 6B reviewed only the OLAF relation and the three auction-platform relations. All unrelated Phase 6 adjudications remained frozen, and Phase 7 did not begin.

## Inputs and clean-room compliance

The review used only the validated R3 corpora, Phase 4 actor materials, Phase 5 relation materials, the four Phase 6 CSV outputs, and `R3_PHASE_6_INTERMEDIATION_AUDIT.md`.

No prior-round coding, previous empirical output, earlier intermediary classification, mechanism coding, or human-review artifact was consulted.

## Issue A — OLAF

- relation: `REL-32023-015`
- CELEX: `32023R0955`
- R: European Commission (`ACT-32023-003`)
- I candidate: European Anti-Fraud Office — OLAF (`ACT-32023-027`)
- T: Member States (`ACT-32023-004`)
- regulatory object: financial records, Fund implementation and protection of Union financial interests
- legal basis: Articles 20 and 21(1)-(4), especially Article 21(2)(e)

### Three-condition decision

| Condition | Decision | Reason |
|---|---|---|
| C1 — identifiable R–T relation | YES | The Commission assesses payment requests, authorizes or suspends payment, reduces allocations and may recover support; Member States hold corresponding implementation, control and information obligations. |
| C2 — distinct institutionalized third party | YES | OLAF is expressly named and must be authorized to exercise its legally established rights in Plan implementation. |
| C3 — demonstrable mediating function | NO | The cited act does not establish an object, transformation, output and recipient through which OLAF mediates the Commission–Member State relation. |

### Mediating-function reconstruction

- `mediated_object`: no object is shown to pass through OLAF between the Commission and the Member State; implementation records may instead be examined in a separate investigative or control function;
- `OLAF_action`: exercises legally authorized access, investigative and control rights under its own institutional mandate;
- `transformation_or_handling`: the Fund Regulation does not establish a transformation serving the Commission–Member State relation;
- `output`: no mediating output is specified; any investigative finding belongs to a separate anti-fraud function;
- `output_recipient`: not specified for this candidate R–T relation;
- `connection_to_RT_relation`: no `R → OLAF → T` chain or equivalent mediated structure is demonstrated.

Removal diagnostic: removing OLAF would remove a separate anti-fraud investigative and control capacity. It would not remove the Commission's direct authority to assess, pay, suspend, reduce or recover support from Member States. Therefore, the required mediating step is absent.

Final decision: `DIRECT_R_T`.

The prior `UNCERTAIN` classification was replaced, the I fields were cleared in the adjudicated relation, C3 was changed to `NO`, and `UNCERTAIN_RELATIONS.csv` now contains zero data rows.

## Issue B — auction platforms

Affected relations:

| Relation | Actor structure reviewed | Prior evidence | Decision |
|---|---|---|---|
| REL-32015-001 | Commission–Member States with common auction platform considered as third actor | E1 in Phase 6 | E2 |
| REL-32015-002 | Member States–common auction platform | E2 in Phase 6; E1 in Phase 5 | E2 confirmed; Phase 5 corrected |
| REL-32015-003 | Member States–opt-out auction platforms | E2 in Phase 6; E1 in Phase 5 | E2 confirmed; Phase 5 corrected |

Reviewed evidence:

- recital 6, `02_corpus/32015D1814/act_numbered.md:L000060-L000066`, expressly identifies the common and opt-out auction platforms and connects them to calendar adjustment;
- Article 1(4)-(8), `02_corpus/32015D1814/act_numbered.md:L000136-L000168`, establishes Commission publication, reserve placement or release, auction-volume consequences and calendar adjustment;
- Article 1(8) does not itself name either platform.

Decision: all three relations are `E2_CROSS_PROVISION_RECONSTRUCTED`. Establishing the platform identity together with the operative legal consequence requires combining recital 6 and Article 1. E2 records the reconstruction route and does not indicate weak confidence.

Substantive classifications remain unchanged: all three are `DIRECT_R_T`. For `REL-32015-001`, the common auction platform fails C3 because no mediating handling or transformation between Commission and Member States is demonstrated.

## Correction log

Records directly updated:

- `RELATION_CANDIDATES.csv`: evidence level changed from E1 to E2 for `REL-32015-001`, `REL-32015-002` and `REL-32015-003`;
- `CROSS_PROVISION_RELATION_MAP.csv`: evidence level changed from E1 to E2 for all 13 evidence-component rows belonging to those three relations;
- `RELATIONS_ADJUDICATED.csv`: `REL-32015-001` changed from E1 to E2; `REL-32023-015` changed from `UNCERTAIN` to `DIRECT_R_T`; the platform review flags were closed;
- `INTERMEDIATION_TEST_MATRIX.csv`: `REL-32015-001` changed from E1 to E2; `REL-32023-015` changed to C3=NO and `DIRECT_R_T`; the platform review flags were closed;
- `UNCERTAIN_RELATIONS.csv`: the resolved OLAF row was removed, leaving the required header and zero uncertain relations.

`NEGATIVE_BOUNDARY_CASES.csv` was not modified because it was not among the permitted update targets. Its Phase 6 OLAF note is superseded by decision `P6B-A-001` and this audit.

### SHA-256 audit trail

| File | Before Phase 6B | After Phase 6B |
|---|---|---|
| RELATION_CANDIDATES.csv | `75FAC01C5B8AFC3FEA142590CACB3682A5E34AF8064DBF3316DC09268C3901E4` | `C6D25D4955B79C934E1CBE1922D53C8C5D097C1E86AAF298E2343564B78CECE0` |
| CROSS_PROVISION_RELATION_MAP.csv | `23F3E526E8C20B4A2353D4719226C07804FB945A5A2D175B7190BE76A091C456` | `85BEBB82FB079DD3410E590408648AA8D83F3D9921EF10E6D865C9AD6452FF3A` |
| RELATIONS_ADJUDICATED.csv | `5151EED837D8B2FB813F5188AFE1DF3A944C6FCBF3110B164ED218F383E33D58` | `63761A6E61EA0A96D4A78957BA78CC01D4B82800CA9FBABE3C2A7E90E3E1574D` |
| INTERMEDIATION_TEST_MATRIX.csv | `3DCDF413EAF64AE80F612213D051C394EEEA04E068BEA0A5A056AD1E4F577BDF` | `CF1DBE7770C1A01CE860E028B9CEF0984A93AF6407E99E84EDD373414480CEE6` |
| UNCERTAIN_RELATIONS.csv | `C41B53F3043166B7B28159E14D376EAB74103842D301C9B8B99AEA6AB9D538C7` | `F7A83B5A4F4D4F0C200B99F1673DC9F300DABB8DA58FFF25E5AC2284EDCC25E6` |

## Post-correction status

The relation universe remains 56:

- `SUPPORTED_INTERMEDIATION`: 9;
- `DIRECT_R_T`: 24;
- `LEGAL_RELATION_NON_RIT`: 23;
- `UNCERTAIN`: 0;
- `NOT_SUPPORTED`: 0.

All Phase 6B review flags are resolved. No formal mechanism coding occurred, no LAW × INTERMEDIARY table was created, and no Phase 7 output exists.

## Success conditions

| Condition | Result |
|---|---|
| OLAF received a final adjudication | PASS |
| Auction-platform evidence levels confirmed or corrected | PASS |
| Corrections are traceable by record and hash | PASS |
| Relation total remains 56 | PASS |
| No mechanism coding | PASS |
| No LAW × INTERMEDIARY table | PASS |
| Phase 7 not begun | PASS |

R3_PHASE_6B_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION
