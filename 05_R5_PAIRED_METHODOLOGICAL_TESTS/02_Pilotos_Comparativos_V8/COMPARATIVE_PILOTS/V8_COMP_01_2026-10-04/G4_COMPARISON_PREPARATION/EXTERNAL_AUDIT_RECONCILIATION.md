# External audit reconciliation

**Date:** 2026-10-04 · **Status:** `PARTIAL — EXTERNAL PACKAGE NOT FOUND`

## 1. Package status (C1: INCORPORATE_AND_RECONCILE)

| Item | Value |
|---|---|
| Expected file | `G3C_AUDIT_AND_G4_PREPARATION_2026-10-04.zip` |
| Expected SHA-256 | `686E322F7451B3050C85FCA394459FC1757AC09C0B7DBE7E5B39676FB102FA99` |
| Expected location | Windows Downloads (`C:\Users\Adm\Downloads`; confirmed as the Downloads known folder; not redirected) |
| Found | **No.** No file with that name or hash exists in Downloads; nothing in Downloads was modified after 15:00 on 2026-10-04; none of the zip files in Downloads contains `G3C`, `FOUR_CELL` or `G4_OPERATIONAL` entries; a recursive search of `C:\Users\Adm`, `G:\Meu Drive` and the project root (depth 6–8) found no file named `G3C_AUDIT*`, `*FOUR_CELL*`, `*G4_OPERATIONAL*` |
| Integrity verification | **Not possible** (file absent) |
| Import into `G4_COMPARISON_PREPARATION/EXTERNAL_AUDIT_SUPPLEMENTARY/` | **Not performed.** The subdirectory was not created, to avoid implying that anything is registered in it |
| Documents read | **None** of `G3C_FOUR_CELL_AUDIT.md`, `FOUR_CELL_FILE_VERIFICATION.csv`, `G4_OPERATIONAL_COMPARISON_SPEC_DRAFT.md` |

**To complete:** place the zip in Downloads (or the workspace), verify the SHA-256 above, extract the three documents unchanged into `EXTERNAL_AUDIT_SUPPLEMENTARY/`, record the source and date received, then run section 4 below. The check must be repeated; it was last attempted at 18:0x -03:00 on 2026-10-04 (see the closing note in `G4_STEP0_GATE_DECISION.md`).

## 2. What could be reconciled now: local matrix vs original registered criteria

The original registered criteria (`COMPARISON_EVALUATION_CRITERIA.md`; protocol `RESEARCH_PROTOCOL_v0_1.md` §6) remain authoritative. The local matrix (`G4_FINAL_EVALUATION_MATRIX.md`) was written to implement them. Reconciliation of the actual definitions:

### 2.1 Equivalences

| Original criterion (registered) | Local matrix dimension | Relation |
|---|---|---|
| Defensabilidade inferencial — claim stops at the supported level (warrant, counter-evidence, stopping rule) | D (and A) | Equivalent; D additionally requires the bearer statement and is applied per claim |
| Rastreabilidade jurídica — claim → configuration → relation → statement → source/hash | E | Equivalent |
| Relação sem suporte — unilateral attribution/duty turned into an edge | C (and B) | Equivalent; C also covers actors inferred from passive/unexpressed actors |
| Erro entre níveis — property of actor/relation promoted to configuration/architecture/regime | D (bearer declared) | Equivalent, contained in D |
| Clarificação estrutural — does B clarify order, gateway, condition, position, part–whole (specific difference, not an extra label) | I (and procedural-improvement rule in matching rules) | Equivalent |
| Incerteza e parada — ambiguities preserved; no promotion; `deferred`/`human_review_needed` | F (and D) | Equivalent |
| Valor incremental — B corrects or only repeats A; five protocol labels | I and matching rules §5 | Equivalent for contrast family 1; see 2.3 |
| Esforço adicional — fields, time, decisions | G | Equivalent |
| Protocol §6 (a)–(g) | A–I mapping in matrix §3 | Equivalent |

### 2.2 Additions in the local matrix (not in the registered criteria)

- **A, fidelity to primary legal evidence** and the **evidence-scope rule** (now the SC dictionary): formalise what the registered criteria leave implicit in traceability and unsupported relations.
- **H, cross-model agreement:** answers the second research question (cross-model replication), not part of the original A/B design.
- **Contrast families** (within-model, within-method, interaction, robustness) and the **seven matching labels**: the original design has only intra-case A vs B.
- **Reviewer-facing instrument** and **sealed identity key**.
These are additions; none replaces a registered criterion.

### 2.3 Disagreements found and how they are resolved

| Point | Registered | Local matrix / matching rules | Resolution |
|---|---|---|---|
| Allowed labels for A→B | "Os únicos rótulos permitidos são `B_IMPROVES`, `B_CLARIFIES_ONLY`, `B_EQUIVALENT`, `B_WORSE`, `UNRESOLVED`" | Seven working labels (EQUIVALENT, SUBSTANTIVELY_IMPROVED, PROCEDURALLY_IMPROVED, BROADER/NARROWER, CONTRADICTORY, INFERENTIAL_REGRESSION, UNRESOLVED_NON_COMPARABLE) | **Registered set prevails for the reported A→B result.** The seven labels are working labels mapped by matching-rules §5 into the five registered labels; BROADER/NARROWER/CONTRADICTORY/NON-COMPARABLE map to `UNRESOLVED` unless a reviewer assigns one of the four. Model-vs-model contrasts, absent from the registered design, use the working labels. |
| Unit of comparison | "Cada claim é comparado provision-by-provision" with fields: common evidence; conclusion A; conclusion B; difference; legal support; claimed gain; error avoided or introduced; sensitivity to cut; added cost; human review | Claims anchored by statement IDs | **Compatible**: statement IDs are provision-linked. The matching table at Step 1 must carry the registered columns. Added requirement for Step 1. |
| Pooling | "Nenhuma comparação intercaso substitui a comparação A/B intra-caso" | P03 and P04 reported separately | Consistent. |
| Track A fixed | "Track B pode qualificar, reduzir ou contradizer A, mas não altera A" | Frozen cells; derived core units are new rows, not edits | Consistent; derived units are labelled as Step 0 constructs. |
| Synthetic index | "Não há índice sintético não validado" | No composite index | Consistent. |

**No registered criterion was replaced or silently changed.**

## 3. Semantic reconciliation of scope labels

External E0/E1/E2/E3 vs local E1/E1x/E2/E3 vs the authoritative SC dictionary: the **external definitions were not available**, so only the labels are known. Labels are preserved in column `external_label_E0_E3` as `PENDING_EXTERNAL_SPEC_NOT_AVAILABLE`; no equivalence is asserted. The local labels and their SC equivalents are in `G4_EVIDENCE_SCOPE_DICTIONARY.md` §5, with the questions to ask when the external definitions arrive.

## 4. Procedure when the package is available

1. Verify the ZIP hash; stop if different.
2. Import the three documents unchanged (names, hashes, source, date).
3. Read the G4 spec draft; build a table: external element | local counterpart | same / added / different / conflicting | decision.
4. Compare E0–E3 definitions with SC-A…SC-D by actual wording; record conflicts without forcing a mapping; update only the provenance column of the classification file (append a new column or a new file; do not overwrite).
5. Compare the external audit's reference counts and notes (6/11/7/11; R-P04-05; auxiliary hash) with the local results; record differences.
6. Re-run the eligibility step if a class changes.
7. Append the outcome to `G4_AUTHORIZATION_DECISION.md`.

## 5. Consequence

C1 cannot be marked executed. Everything in Step 0 was built on the registered criteria and the local protocol; it can be re-labelled but not re-derived if the external definitions differ materially, which is why `external_label_E0_E3` is a separate column.
