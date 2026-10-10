# Documentary pending items register — G3C closeout

**Date:** 2026-10-04 · **Append-only.** Statuses: `RESOLVED` · `OPEN` · `OPEN_REGISTERED` (documented, decision needed) · `CARRIED_FORWARD`.
Nothing here modifies any frozen artifact. Hash values quoted are recalculated locally on 2026-10-04 (see `FOUR_CELL_FINAL_INTEGRITY_MANIFEST.csv`).

| ID | Item | Status | Severity for G4 |
|---|---|---|---|
| P-01 | External G3C audit package and G4 spec draft not found | OPEN | Moderate |
| P-02 | Codex Track B auxiliary freeze file missing (Issue A) | OPEN_REGISTERED | Low–moderate |
| P-03 | Frozen primary evidence accessible and unchanged (Issue B) | RESOLVED | — |
| P-04 | Evidence boundary, R-P04-05 and uniform scope rule (Issue C) | OPEN_REGISTERED | Moderate–high |
| P-05 | Main execution/decision registers lacked G3 and replication entries | PARTLY_RESOLVED (append now; G3 original absent) | Low |
| P-06 | Method-input documents differ across executing environments | OPEN_REGISTERED | Moderate–high |
| P-07 | Codex model identity, version and parameters not documented in examined files | OPEN | Moderate |
| P-08 | Codex Track A has no execution/independence log | OPEN | Low–moderate |
| P-09 | David's original e-mail evidence (pre-existing) | CARRIED_FORWARD | Not blocking G4 |
| P-10 | No human reviewers identified; no human ratings exist | OPEN | Blocking for the human phase only |

## P-01 — External G3C audit package not located

- **Searched:** the project root (`G:\Meu Drive\PRJ-David\Prf-David`, depth 8), `C:\Users\Adm\Downloads`, `Desktop`, `Documents`, `OneDrive`; filename patterns `*G3C*`, `*FOUR_CELL*`, `*G4_OPERATIONAL*`, `*G4_COMPARISON*`; and the file lists of all `.zip` files in Downloads. **No match.**
- **Consequence:** `G3C_FOUR_CELL_AUDIT.md`, `FOUR_CELL_FILE_VERIFICATION.csv` and `G4_OPERATIONAL_COMPARISON_SPEC_DRAFT.md` could not be registered with source attribution and hash; their reference counts (Codex A 6/6; Codex B 11/11; Claude A 7/7; Claude B 11/11) are treated only as reference observations, **independently reproduced** locally (same counts).
- **What was not done:** no document was recreated or paraphrased as if it were the external one.
- **To resolve:** Igor to place the zip in the workspace (or Downloads); on receipt, copy unchanged under original names into `G4_COMPARISON_PREPARATION/EXTERNAL_AUDIT_SUPPLEMENTARY/`, record source, date received and SHA-256, and perform the G4 step 0.5 reconciliation (matching rules file) against `G4_OPERATIONAL_COMPARISON_SPEC_DRAFT.md`.
- **Dependency note:** the evaluation matrix and matching rules were finalised **without** the draft spec; they cite only the protocol and pre-registered criteria. If the draft differs materially, a decision (append-only) is needed on which prevails; the default stated in the matching rules is that the finalised rules prevail.

## P-02 — Issue A: Codex Track B freeze (`TRACK_B_FREEZE_MANIFEST_SHA256.txt`)

- **Original expected:** `TRACK_B/TRACK_B_FREEZE_MANIFEST_SHA256.txt`, pointed to by manifest row TBF-024 (`SELF_HASH_RECORDED_IN_TRACK_B_FREEZE_MANIFEST_SHA256.txt`).
- **Found:** **absent** from `TRACK_B/` and from `TRACK_B.zip` (12 entries; no such file). The equivalent Track A file exists (`695AC62F…E0D8`) and equals the recalculated hash of `TRACK_A_FREEZE_MANIFEST.csv`.
- **Hash of the Track B manifest as it exists now (observation, not an original record):** `5204962C29A0C0F9D0D7F262EF6495589D4E2D99D2890159FA59D5999409962F`. It cannot be compared with an original registered self-hash.
- **What is verified independently of the missing file:** all 11 Track B analytic outputs recalculate to the values written in the manifest (11/11 MATCH); the same 12 files inside `TRACK_B.zip` (entry times 13:40–13:43) are byte-identical to the current files; file modification times (last 13:43:12) precede the start of the Claude replication (13:54). Modification times and zip copies are **weak** anchors: they show consistency, not an original self-hash record.
- **Not done:** the file was **not regenerated**. Doing so would produce a new artifact that cannot be passed off as the historical record.
- **Classification:** *unresolved auxiliary-chain limitation*, kept separate from the individual-file verification (which succeeded). The Track B manifest content is not independently anchored by an original self-hash.
- **To resolve:** if the Codex environment (`C:\Users\Adm\.codex\…`) or a backup holds the original file, add it unchanged and compare; otherwise Igor decides (append-only) to accept the limitation.

## P-03 — Issue B: frozen primary evidence

- `COMMON_STATEMENT_REGISTER.csv` = `417A35A361E44F8BECFBD8FC39B34738C026591C59B7E837FDDF292F9EF3E77F` (MATCH; 20 data rows; P03 = 6, P04 = 14; file modified 12:45:28, before all four executions).
- `31991L0263.html` = `01D5BDB117B370AE9DAD7F3ABB151583A75519CBAD0E7808EFC9040C8D656888` (MATCH). EUR-Lex title `31991L0263 - EN`; instrument "Council Directive 91/263/EEC of 29 April 1991"; version as registered: OJ L 128, 23.05.1991.
- `32004R0874.html` = `62AFB4DDCCAE5E7157590B1386040AA8D160701D7194DBD2F2403AC4B6781449` (MATCH). EUR-Lex title `32004R0874 - EN`; "Commission Regulation (EC) No 874/2004 of 28 April 2004"; version as registered: OJ L 162, 30.04.2004.
- All four cells use the same 20 statement IDs (set equality with the register in each `*_CODING.csv`).
- **Status: RESOLVED.** Analytical scope was not widened.
- Residual note: the HTML files are historical captures (acquired 2026-09-30); this audit confirms integrity and identity, not that the text equals current consolidated law (not required for the formal-text design).

## P-04 — Issue C: evidence boundary and R-P04-05

**Registered, not corrected.** No Claude artifact was changed.

### Facts
1. The frozen statements CS-P04-001 and CS-P04-002 contain: at the end of phased registration an independent audit shall be performed **at the expense of the Registry** and report findings to the Commission; the auditor shall be appointed **by the Registry** after consulting the Commission.
2. The official text of Article 12(5) has a **third sentence** (the purpose of the audit: to confirm the fair, appropriate and sound operational and technical administration of the phased registration period by the Registry). It is **not** in the register.
3. **Claude Track A**, R-P04-05 (Auditor → Registry): decision `DEFERRED`, `coding_status` `deferred`; cross-provision field: "Article 12(5), third sentence … read for context; **NOT used** (outside the frozen statements)".
4. **Claude Track B**, R-P04-05 (auditor → Registry, "verification/assurance, audit of the Registry's administration of the phased registration"): decision `ACCEPTED`, `cross_provision_inference`, `claim_level` relation; cross-provision field: "Art 12(5), third sentence (purpose: administration of the phased registration by the Registry; wording ambiguity 'audit of what')"; flagged for human review.
5. Both Claude prompts allowed consultation of wider provisions "only to resolve a cross-reference quoted in a statement or a wording ambiguity"; the original task statement said official HTML only "to resolve a cited wording question, preserving the same scope". The rule did not say whether a sentence supplying a missing object/purpose counted as a "wording question".
6. The Codex relationship tables have **no** cross-provision field (only `source_manifest_ids` / `source_sha256`); whether any Codex claim depends on non-frozen text is **not determinable** from structured fields.

### Three-way distinction applied to R-P04-05 (Claude Track B)
| Layer | Content |
|---|---|
| **1. Explicitly in frozen evidence** | The Registry appoints and pays for the auditor; the audit reports to the Commission; timing "end of phased registration"; a Registry–auditor link of **appointment/funding** type. |
| **2. Contextual material permitted for provenance verification** | Reading of Article 12(5) as a whole to confirm locator, sentence segmentation and wording. |
| **3. Additional substantive legal evidence outside the boundary** | The **object/purpose of the audit** (the Registry's administration of the phased registration), which supplies the *type* ("verification of the Registry's administration") and the audited-party/object of the relation. This element is not in the frozen excerpts → `E3` under the uniform rule. |

Pre-classification: R-P04-05 (Claude B) = `SCOPE_EXTENDED_PARTIAL` (the Registry–auditor link is E1 in a different type; the "audit of the Registry's administration" content is E3). Claude A R-P04-05 = `E2` only, not used (deferred). Both are **scope-consistent in outcome in A and inconsistent in B**; the within-Claude A→B difference on this relation must not be classified as `B_IMPROVES` (matching rule 2).

### Uniform evidence-scope rule (all four cells)
See `G4_FINAL_EVALUATION_MATRIX.md` §1: E1 (frozen content) · E1x (referent of a cross-reference quoted in a cited excerpt, no new element) · E2 (context for provenance/wording, never a warrant) · E3 (any element from non-frozen text used in a claim → `SCOPE_EXTENDED`). Codex claims whose scope cannot be established are `SCOPE_NOT_DETERMINABLE` until checked by a reviewer; they are not presumed clean.

### Other Claude cross-provision uses to be tagged at G4 step 0 (not classified here)
Claude Track A: R-P03-01 (Art. 9, referent), R-P03-04 (Annex III 3.1, 3.2 — 3.2 is quoted in the excerpt; 3.1 is ownership context), R-P04-15 (same-paragraph antecedent), R-P04-21 (Art. 23(1) second sentence, published list, coupling), R-P04-22 (Art. 23(1)). Claude Track B: R-P03-01, R-P03-02 (Annex III points 2 and 3.1; stated "corroboration only"), R-P04-10 (Art. 14 wording), R-P04-14, R-P04-15 (Art. 15(1) anaphora), R-P04-16 and R-P04-19 (Art. 23(1) list). Claude Track B also contains, in a *declined* claim, an assertion "the audited entity appoints and funds (per wider text)" which is **not** used to support an accepted claim. Each requires tagging E1x vs E3 by checking whether any new element was supplied.

### To resolve
(a) Igor confirms the uniform rule (default adopted in the finalised matrix). (b) G4 step 0 tags all four cells. (c) Optional, only on explicit authorisation and recorded as a new artifact: a scope-clean re-coding of R-P04-05 is **not** performed by default.

## P-05 — Main registers

- At G3C start, `EXECUTION_LOG.md` ended at "G2 / Track A only" and `UPDATED_RESPONSE_REGISTER.md` / `RESPONSE_LOG.csv` at D-G2-001. **No G3 entry (Codex Track B), no entry for the Claude replication, and no D-G3 authorisation record** existed. (Their SHA-256 before this closeout: EXECUTION_LOG `0577DB34…E203A`; UPDATED_RESPONSE_REGISTER `AFD04FC2…2A34`; RESPONSE_AND_DECISION_REGISTER `9D3FEAD4…7CED`; RESPONSE_LOG `C748C7DE…568D`.)
- **Done now:** append-only entries for the Claude replication and for G3C, flagged as written at G3C from frozen evidence; the Codex G3 execution is referenced through its own freeze manifest and log, **not reconstructed**.
- **Open:** the original G3 authorisation text (Codex attachment `C:\Users\Adm\.codex\attachments\a7ffed73-…\Pasted text.txt`, SHA-256 `97FE15DE…AF2FC`, recorded as TBF-012) exists; whether Igor wants a D-G3-001 decision entry created from it is for Igor to decide.

## P-06 — Method-input documents differ across executing environments

| Input | Codex | Claude |
|---|---|---|
| Specification of the eight operations (Track B) | `RGAM/V8_ACTIVE/01_THEORETICAL_FRAMEWORK/ARCHITECTURAL_THEORY_AND_METHOD.md` (SHA-256 `2D2195EE…5475`), plus `…/03_METHODOLOGY/CONFIGURATION_RECONSTRUCTION.md` (recorded in the manifest as `UNVERSIONED_SUPPORT_READ`; hash now `9CBFF38C…00EC`, file dated 03 Oct 18:57, before the runs) | `RESEARCH_PROTOCOL_v0_1.md` §5 (eight operations, shorter formulation) and `FOUNDATIONAL_PREPAPER_V8.md`; the two Codex documents were **not** in the Claude allow-list |
| V8 support (Track A) | codebook, inference rules, relational model, V8 manuscript (per manifest TAF-004…007) | the same four, **plus** `V8_CONCEPTUAL_BASELINE.md` and `V8_ANALYTICAL_STRUCTURE.md`, and `COMPARISON_EVALUATION_CRITERIA.md` (listed in Codex only for Track B, TBF-011) |
| Task prompts | G2 prompt (Track A), G3 prompt (Track B) as originally issued | orchestrator-written prompts (`PROMPTS_AND_LOGS/01…`, `02…`) with explicit allow/forbid lists |

- The eight operation names are the same; the **wording and added tests differ** (for example the Codex specification contains a "distinctive methodological question" and "test of theoretical innovation" paragraph; the Claude specification contains the one-line operation definitions of the protocol). Effects on outputs are **not** assessed here.
- **Status:** registered as deviation D-07. Differences in outputs that could stem from these inputs are to be tagged `CONFOUNDED_INPUT`.
- **To resolve:** Igor decides (append-only) whether to treat as a documented limitation (default) or to authorise a harmonised re-run.

## P-07 — Codex model identity and parameters

The Codex manifests, QA reports and Track B log examined here contain **no** model name, version, reasoning setting or sampling parameters (a text search for model identifiers found only a path under `.codex`). Claude's identity is recorded (`claude-sonnet-5-5`), its sampling parameters are not exposed. **To resolve:** Igor supplies the Codex model/version/configuration if known, as a dated statement, otherwise it remains `NOT_DOCUMENTED`.

## P-08 — Codex Track A process record

There is no Track A execution log. Track A isolation from Track B is trivially satisfied (A ran first); Track A's own independence from other analyses (for example from earlier Codex analyses in the same environment) is not recorded; Track B's log records that the same researcher/environment executed both and that Track B was "procedurally separated at the document-input level but not genuinely blind". **To resolve:** none required; carried as limitation D-01/D-05.

## P-09 — Carried forward (pre-existing)

`UPDATED_RESPONSE_REGISTER.md` records that David Levi-Faur's original e-mail evidence remains `MISSING_PENDING_INCORPORATION`; R-001 is a paraphrase. Does not block G4, but the research question attributed to David is documented only second-hand.

## P-10 — Human review

No reviewers have been named; no human ratings exist and none have been generated. The instrument (`G4_HUMAN_REVIEW_TEMPLATE.csv`) is ready. Not blocking the AI-assisted preparatory steps, blocking for any validity statement.

---
## Addendum — 2026-10-04 (G4 Step 0; append-only)

| ID | Update |
|---|---|
| P-01 | **Still OPEN.** Expected zip hash `686E322F7451B3050C85FCA394459FC1757AC09C0B7DBE7E5B39676FB102FA99`; not found in Downloads (known folder `C:\Users\Adm\Downloads`), workspace or searched user folders; rechecked 2026-10-04 18:08 -03:00. Reconciliation done only against the original registered criteria (`EXTERNAL_AUDIT_RECONCILIATION.md`). |
| P-02 | **ACCEPTED WITH DOCUMENTED LIMITATION** (decision C2). File not regenerated. |
| P-04 | **EXECUTED at Step 0.** Uniform dictionary in `G4_EVIDENCE_SCOPE_DICTIONARY.md`; R-P04-05 (Claude B) classified SC-C; the same rule applied to all 112 units; 5 material deviations (Claude A: R-P03-04, CL-P03-02, CL-P03-03; Claude B: R-P04-05, CL-P04-02), 2 borderline SC-B, 13 flagged units. Earlier note that other Claude cross-provision uses must be "tagged at G4 step 0" is now fulfilled. |
| P-06 | **Treated as `CONFOUNDED_INPUT`** (decision C4). |
| P-07 | **PROVENANCE_FOUND_EXTERNAL_TO_CELL_ARTIFACTS:** Codex model `gpt-5.6-terra`, reasoning effort high, Codex VS Code extension CLI 0.159.2, provider `openai` (session), approval `never`; one session (11:14–13:43 -03:00) covers Track A and Track B. Details and limits: `G3C_DECISIONS_C1_C6.md`. Replaces `NOT_DOCUMENTED` for the model identity; the cell artifacts themselves still carry no model identification. |
| P-08 | Unchanged (Codex A has no execution log); session-level evidence corroborates D-01. |
| P-09, P-10 | Unchanged. |
| New | **UPQ-01…UPQ-05** unresolved provenance questions (see `G4_STEP0_SOURCE_BOUNDARY_REPORT.md` §2.5). |
