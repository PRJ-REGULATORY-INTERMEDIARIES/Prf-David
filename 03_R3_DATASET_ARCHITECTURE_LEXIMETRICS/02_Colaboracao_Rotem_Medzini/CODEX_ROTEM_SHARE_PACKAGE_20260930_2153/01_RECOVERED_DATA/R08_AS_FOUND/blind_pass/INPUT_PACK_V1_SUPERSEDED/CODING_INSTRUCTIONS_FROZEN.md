# CODING INSTRUCTIONS (FROZEN) — dual representation test

Frozen on 2026-09-30, before either coding pass. The same instructions bind the first pass (`08_DUAL_CODING/first_pass/`) and the blind second pass (`08_DUAL_CODING/blind_pass/OUTPUT/`).

## 0. Materials you may use
- `CASE_0X_PROVISIONS.md`: verbatim official text of the provisions. **This is the only legal evidence you may use.** Do not use memory of the law, secondary sources, or any other file.
- `CODEBOOK_REVISED.md`: the revised codebook of Rotem Medzini & David Levi-Faur (definitions and permitted values).
- `PARENT_FRAME.csv`: the fixed list of candidate intermediary × act records (parent keys).

You must **not** open any other file of the project.

## 1. Task A — PARENT records (one row per PARENT_ID in PARENT_FRAME.csv)
Apply the revised codebook's INTERMEDIARY_MAP variables to each candidate, using only the provision pack.

| Column | Rule / permitted values (from CODEBOOK_REVISED.md) |
|---|---|
| PARENT_ID, CASE_ID, ACT_ID, INTERMEDIARY_NAME | copy from PARENT_FRAME.csv |
| INTERMEDIARY_QUALIFIES | YES / NO / UNCLEAR, applying ¶26–¶31 (inclusion rule; necessary reliance ¶28; exclusions ¶29–¶31) |
| QUALIFICATION_RATIONALE | 1–3 sentences citing PROVISION_IDs |
| RELEVANT_PROVISIONS | PROVISION_IDs needed to support the row (¶36), separated by `;` |
| INTERMEDIARY_INVOLVEMENT | Required; Conditional; Optional; Member State option; Not specified; N/A (multiple allowed, `;`) |
| ORIENTATION | target-facing; regulator-facing; bidirectional; intermediary-facing; N/A (multiple allowed) |
| REGULATOR_CONTEXT | EU_public; national_public; multilevel_public; private_self_regulatory; hybrid_public_private; Unclear; N/A (multiple allowed) |
| TARGET_CONTEXT | product_economic_operator; service_provider; platform_provider; regulated_professional; public_body; individual; regulatory_intermediary; N/A (multiple allowed) |
| F_CODE_CREATION, F_ASSURANCE, F_MONITORING, F_REGISTRY_ADMINISTRATION, F_INTERNAL_COMPLIANCE, F_DISPUTE_RESOLUTION, F_COMPLAINT_HANDLING, F_AUDITING, F_INSURANCE_RISK_UNDERWRITING, F_ENFORCEMENT | Yes / No / N/A, per ¶42 and ¶50 and the definitions in ¶82 |
| MECHANISM_FAMILY | Code creation; Assurance; Monitoring; Registry administration; Internal compliance; Dispute resolution; Complaint handling; Insurance / risk underwriting; Enforcement; N/A (primary; multiple only where necessary) |
| RECOGNITION_PATHWAY | Vetting; Designation; None; N/A (¶85) |
| FUNCTION_DESCRIPTION | ≤ 2 sentences: what the intermediary is assigned to do (¶82) |
| IDENTIFICATION_BASIS_TEST | **Test field, not part of Rotem's codebook.** Which clause of ¶27 licenses inclusion: DIRECT_ASSIGNMENT (the act assigns the function to this actor); LEGAL_RECOGNITION (the act recognises/approves/selects this actor for the function); STRUCTURAL_RELIANCE (the role follows necessarily from an express legal mechanism without assignment or recognition, ¶28); NONE; multiple allowed |
| PASS_ID | FIRST_PASS or BLIND_SECOND_PASS |

## 2. Task B — CHILD events (provision-anchored activities/relations)
For every provision in the pack, record **each legally distinct directional action** that involves the focal intermediary, whether as actor, as addressee or as object. Also record actions by other actors when they are needed to reconstruct where the intermediary's outputs go or how the intermediary is recognised, controlled or relied upon.

| Column | Rule |
|---|---|
| EVENT_ID | `{PARENT_ID}-E{nn}` |
| PARENT_ID | the parent record the event belongs to |
| SOURCE_PROVISION_ID | the PROVISION_ID (exactly as in the pack) |
| TEXT_SPAN | **an exact, contiguous, verbatim substring of that provision** (copy-paste; no ellipsis; ≤ 400 characters) |
| ACTOR | who performs the action (verbatim noun phrase or a short normalised label). `NOT_SPECIFIED` if the text gives no actor (e.g. passive voice) |
| ACTION | the legal verb phrase, with modal verb preserved (e.g. "shall assess") |
| ACTION_ADDRESSEE | to whom the action or communication is directed, if stated; else `NOT_SPECIFIED` |
| OBJECT | what the action operates on |
| REGULATOR_ACTOR | the public regulator involved in this event, if any, stated in the text; else `NOT_SPECIFIED` |
| INTERMEDIARY_ACTOR | the focal intermediary as named in the text |
| TARGET_ACTOR | the regulated actor whose conduct is at stake in this event, if stated; else `NOT_SPECIFIED` |
| INTERMEDIARY_ROLE_IN_EVENT | ACTOR / ADDRESSEE / OBJECT / BENEFICIARY / NOT_PRESENT |
| NORMATIVE_MODALITY | OBLIGATION (shall/must) / PERMISSION (may) / PROHIBITION / DEFINITION_OR_STATUS / OTHER |
| TRIGGER_CONDITION | verbatim condition ("where…", "if…", "upon…") or `NONE` |
| LEGAL_EFFECT | the legal consequence stated (e.g. presumption, rejection, suspension of status), or `NONE`. **Do not** turn a legal effect into an actor→actor action |
| FUNCTION_CODE | one function label from ¶82 performed **by the intermediary** in this event (assurance, monitoring, …), or `NOT_A_FUNCTION_OF_THE_INTERMEDIARY` (e.g. the regulator recognises the intermediary; the target transmits a report) |
| MECHANISM_CODE | mechanism_family label (¶82), or `N/A` |
| INFERENCE_BASIS | TEXTUAL (everything coded is stated in the span) / INFERENTIAL (some element is inferred, which must be explained in RATIONALE) |
| RATIONALE | 1–2 sentences |
| CONFIDENCE | HIGH / MEDIUM / LOW |
| REVIEW_STATUS | MODEL_CODED (first pass) or MODEL_BLIND_SECOND_PASS (blind pass) |

## 3. Binding rules (from PILOT_03 human rules and R4.2D human rule candidates; they apply to both passes)
1. **One event per legally distinct directional action and addressee.** Split "appoint … audit … report" into separate events.
2. **A preposition does not make a recipient.** Recipient/addressee ≠ regulatory target. A qualifier such as "designated" does not make the qualified actor the addressee.
3. **Never fill an actor by expectation.** Use `NOT_SPECIFIED` when the text names none.
4. **No combinatorial expansion.** Do not create an R–I–T event for every combination of regulators and targets present in the act. Code only combinations the span states.
5. **Legal effects are not actor edges.** Do not create "enable / allow / grant" edges from legal effects alone.
6. **Preserve modality and conditions.** A permission ("may") or a conditional duty is not an unconditional obligation.
7. **Do not use external law or practice.** Cross-referenced acts count only if the provision expressly incorporates them (codebook ¶35).
8. **Uncertainty is legitimate.** When a classification is ambiguous, keep the better-supported code, lower CONFIDENCE, and explain the alternative in RATIONALE.

## 4. Output format
CSV, UTF-8, comma-separated, double-quoted fields, header row exactly as the column names above (PARENT and CHILD files separately).
