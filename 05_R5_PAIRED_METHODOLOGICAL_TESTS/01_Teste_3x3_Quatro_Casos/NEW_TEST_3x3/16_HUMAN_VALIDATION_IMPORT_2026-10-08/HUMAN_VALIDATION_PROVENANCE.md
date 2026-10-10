# Human validation — provenance statement

**Stage:** `16_HUMAN_VALIDATION_IMPORT_2026-10-08`
**Workspace archival / import timestamp:** 2026-10-08T14:30:46-03:00
**Reviewer:** Igor Caires Machado
**Validation design:** targeted blinded human validation, purposive sample, 6 of 56 cards
**Status:** `HUMAN_VALIDATION_ARCHIVED / NOT_A_PROTOCOL_COMPLIANT_FREEZE / MACHINE_SIMULATION_EXCLUDED`

This stage imports an external artefact into the workspace provenance chain. It performs no analysis, adjudicates nothing further, and modifies no frozen output. Stages 00–15 are untouched; this is a new numbered stage precisely so that the stage-15 preparation freeze (`PREPARATION_MANIFEST_SHA256.txt`) remains valid.

---

## 1. What is being imported

Six blinded human decisions on six of the 56 review cards frozen in `14_PAIRED_COMPARISON_ROUND1/FAMILY_PRE_ADJUDICATION/`.

| Card | Case | Level | Triggers | Blind decision |
|---|---|---|---|---|
| HQ-SCF-02 | SCF | C3 | H5; H6; H11 | B |
| HQ-CBAM-04 | CBAM | C1 | H1; H2; H10 | B |
| HQ-CBAM-10 | CBAM | C3 | H5; H6; H11 | A |
| HQ-AI-12 | AI Act | C2 | H4; H6 | B |
| HQ-AI-14 | AI Act | C3 | H5; H6; H11 | B |
| HQ-DIR-01 | Directive 86/361 | C3 | H5; H8; H9; H10; H11 | A |

The source export carried `card_id` and `decision` only.

---

## 2. Provenance facts

1. **The six decisions were collected through an external human-review interface**, in the working conversation, not through any workspace artefact.
2. **They were not originally stored in the workspace.** At the time the decisions were made, no adjudication file existed here. The Round-1 QA report (check 28) correctly recorded, as of 2026-10-07T10:11, that no human decision had been made or simulated and that no adjudication register existed.
3. **They are being imported for provenance after completion.** This is a retrospective record, created today, of decisions taken earlier.
4. **A/B was blind at the time of the decisions.** Each card carries two unattributed propositions over the same frozen legal evidence; arm identity was held only in `MASTER_IDENTITY_KEY.csv`, with blind assignment by a deterministic hash rule. The reviewer attests that the decisions were made before the key was opened.
5. **The later identity reveal is analytically separate.** It is recorded in `POST_REVEAL_LINKAGE_6.csv`, a distinct artefact that resolves each blind decision against the frozen key without rewriting the decision. The decision column and the resolved-arm column are kept apart by design.
6. **No written justification was captured.** `justification` and `human_confidence` are `NOT_RECORDED` in every row. No justification has been reconstructed, inferred or supplied.
7. **The sample was purposive, not representative.** The six were selected for methodological centrality. Four of the six are at the architectural level C3, one at the configurational level C2, one at the relational level C1. The remaining 50 cards are not human-adjudicated and retain `status = OPEN_AWAITING_HUMAN_ADJUDICATION`.

---

## 3. Dates: two distinct things

| | Value | Basis |
|---|---|---|
| **Decision date** | not recorded in the export | The export carried no per-card timestamp. Recorded as `DATE_NOT_RECORDED_IN_EXPORT`. The decision *context* is recorded instead: made in the working conversation, before identity reveal. |
| **Workspace archival / import date** | 2026-10-08T14:30:46-03:00 | The time these files were written. |

No file has been backdated. No timestamp has been invented. The decision date is absent, and absent is what the register says.

---

## 4. Protocol deviations (recorded, not waived)

The frozen `IDENTITY_REVEAL_PROTOCOL.md` requires, cumulatively and in order: the adjudication file's SHA-256 recorded in a freeze register; an approved completeness gate; no blank mandatory fields; and a freeze timestamp — *all before* the A/B key is opened.

**That sequence cannot be satisfied retrospectively**, because the reveal already happened. Two deviations are logged in `PROTOCOL_DEVIATION_LOG.csv`:

- **DEV-16-01** — freeze-before-reveal preconditions not met. The protocol's own clause on later administrative correction requires a *new versioned artefact with justification, preserving the original*, rather than a silent substitution. That is what this stage is. Blinding at decision time rests on the reviewer's attestation, not on a contemporaneous hash. Every linkage row is marked `LINKED_RETROSPECTIVELY_NO_CONTEMPORANEOUS_FREEZE`.
- **DEV-16-02** — `justification` and `human_confidence` are mandatory card fields and are blank. Recorded as `NOT_RECORDED`.

**Consequence.** The six decisions are usable as qualitative, purposively selected human validation. They are **not** a protocol-compliant frozen adjudication, and because no justification was captured, each decision is auditable as a decision but not as reasoning.

---

## 5. Machine-simulated adjudication — excluded

> A non-authoritative machine-simulated adjudication was produced during exploratory workflow outside the frozen workspace. It is excluded from the evidentiary basis of the present report.

Its decisions are not imported, are not part of the analytical record, and are not relied on anywhere in `FINAL_PACKAGE/`. No further analysis of that simulation has been performed or is required. The frozen `HUMAN_ADJUDICATION_PROTOCOL.md` in any case provides that the executor neither fills in nor simulates the human decision.

---

## 6. What this does and does not change

**Changes:** the claim in the note that rests on human judgment is now archived in the workspace and can be inspected against the frozen cards and key. The recommendation to archive it is discharged.

**Does not change:** any substantive conclusion. Resolving the six decisions against `MASTER_IDENTITY_KEY.csv` yields five supporting propositions produced under the additional inferential controls and one — HQ-AI-12 — supporting the more compact baseline reconstruction, which is exactly what the synthesis already described. The counterexample stands, and the sample remains too small and too purposively chosen to support any rate or performance estimate.

---

## 7. Files in this stage

| File | Role |
|---|---|
| `HUMAN_VALIDATION_REGISTER_6.csv` | the imported decisions, with reviewer, design, blank justification and provenance note |
| `POST_REVEAL_LINKAGE_6.csv` | blind decision resolved against the frozen identity key, per the reveal protocol's separate-artefact requirement |
| `PROTOCOL_DEVIATION_LOG.csv` | DEV-16-01, DEV-16-02 |
| `HUMAN_VALIDATION_PROVENANCE.md` | this statement |
| `IMPORT_MANIFEST.csv` / `IMPORT_MANIFEST_SHA256.txt` | SHA-256 of each file in this stage, and of the two Round-1 artefacts it depends on |
