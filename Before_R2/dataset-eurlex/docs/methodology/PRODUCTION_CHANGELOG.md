# Production Changelog

## v1.3 — 2026-09-08

### Change

```text
regulatory relationship as the sole stated analytical unit
→
four-level actor-in-role architecture
```

### Decision

Actor-in-role is now the principal substantive unit for mapping regulatory
intermediation. Regulatory relationships are retained as the primary coding and
evidentiary units used to establish relational roles; act/regime is the higher-level
comparative unit; intermediary function/mechanism is a distinct level for I roles.

This does not treat prior relationship-level coding as an error. It is the necessary
evidentiary layer from which the actor-in-role map is derived. R/I/T remain contextual
roles, not permanent actor attributes. Legislative proposer, formal adopter, rule-maker,
regulator, implementing regulator, supervisory authority, intermediary and target remain
distinct categories where the corpus supports the distinction.

### New artifacts

- `docs/methodology/METHODOLOGY_WORKING_DRAFT_V1_3.md` — versioned methodology statement.
- `scripts/build_final_human_review_v2.py` — reproducible transformation and validation.
- `cases/final_human_review_v2/` — final human-review package, created without replacing
  `cases/FINAL_DATASET_FOR_HUMAN_REVIEW.csv`.

### Integrity note

The v1.3 package is derived only from the current 25-record reconstructed relationship
matrix, the recorded R2 human decisions, and the frozen corpora where required to verify
the status of `case_02-U07`. It performs no open-ended recoding. The damaged
`R2_HUMAN_VALIDATION_relations.csv` remains preserved and is labelled as a damaged original;
its derivative rows remain explicitly labelled
`reconstructed_from_session_and_surviving_decisions`. The unresolved `case_02-U07` remains
outside the accepted datasets as `RESEARCHER_DECISION_REQUIRED`.

No historical corpus, R2 validation file, primary coding output, or prior final dataset was
overwritten, moved, or deleted by this change.

## v1.0 — 2026-09-07

### Change

```text
intensive methodological pilot
→
simplified three-case production workflow
```

### Rationale

Reduction of operational complexity while retaining source traceability, explicit coding rules, independent secondary review, and researcher adjudication.

### Consequences

- The four-way Terra/Claude, R1/R2, blinded-RA exercise remains historical methodological calibration and robustness evidence.
- Claude is the primary coder for one consolidated prompt.
- Luna is the independent secondary reviewer and never silently overwrites Claude output.
- The researcher is the authority for `APPROVE`, `CHANGE`, `EXCLUDE`, or `UNRESOLVED`.
- G0/G1/G2 are not production conditions for Cases 01–03.
- No new coding or final dataset was created by this preparation change.

### Integrity note

Legacy files were not deleted, moved, or overwritten. The existing pilot README and legacy configuration still describe the historical workflow and are retained for audit. The production-specific files under `cases/`, `prompts/production/`, `methodology/production_v1.0/`, `config/production.yaml`, and this documentation define the new preparation layer.

## v1.1 — 2026-09-08

### Change

```text
search for intermediaries directly, operative text and recitals as equal-weight evidence
→
find R-T first then test third actors functionally, recitals as interpretive support only
```

### Trigger

A researcher's deep reading of Case 01 (European Climate Law), reviewed against Abbott/Levi-Faur/Snidal's RIT model and EU legislative-drafting doctrine on the non-normative status of recitals (Interinstitutional Agreement of 22 December 1998, Guideline 10; CJEU Case C-134/08 *Tyson Parketthandel*, para. 16). See `outputs/` for the researcher's technical note preceding this change and `docs/methodology/METHODOLOGY_WORKING_DRAFT_V1_1.md` for the full rationale.

### Decisions

1. Reading sequence reorders to R-T first, third actors second, with a five-dimension Third-Actor Functional Test (distinction, function, regulatory integration, evidence, counterfactual) recorded per candidate intermediary.
2. The corpus is treated as two evidentiary layers (operative enacting terms vs. recitals). A relation coded `intermediated` or `direct` now requires a non-null `operative_anchor_location`; a recital alone can only support a `contextual_candidate_recital_only` entry in the uncertainty log, never a positive main-matrix relation.
3. Analytical roles are renamed functionally: "Claude primary coder" → **Primary Interpretive Reader**; "Luna secondary reviewer" → **Secondary Critical Reviewer**. Per-run computational metadata (provider, model, version, reasoning effort, run date, run id, prompt version) is recorded separately per run and never invented when unobserved.

### New artifacts

- `methodology/production_v1.1/coding_matrix_schema.json` — adds `operative_anchor_location`, `contextual_support`, `third_actor_test` to the v1.0 record shape; `relation_type` enum unchanged.
- `methodology/production_v1.1/validate_production_logic.py` — structural/logical validator. Deliberately does not mechanically force `relation_type` from the `third_actor_test` result pattern, to avoid reproducing the v1.1.0 pilot's documented `condition_C=YES ⇒ I required regardless of condition_D` conflict (see `03_human/stage4_attempt_02/pre_ra_4way/KNOWN_LIMITATIONS_V1_1.md`).
- `docs/methodology/METHODOLOGY_WORKING_DRAFT_V1_1.md` — supersedes the v1.0 working draft for production purposes; v1.0 draft preserved unchanged.
- `prompts/production/PRIMARY_INTERPRETIVE_READER.md`, `prompts/production/SECONDARY_CRITICAL_REVIEWER.md` — functionally-named prompts superseding `CLAUDE_PRIMARY_CODER.md` and `LUNA_SECONDARY_REVIEWER.md`, both of which are preserved unchanged as historical artifacts.

### Consequences

- Applies identically to Case 01, Case 02, and Case 03 — no case-specific adaptation, per the change-control principle in `docs/methodology/CASE_SELECTION_PROTOCOL.md`.
- All three cases are re-coded fresh under v1.1 by a memoryless run of the Primary Interpretive Reader, reading only that case's own frozen corpus. This is not a correction of the v1.0 proposals and does not treat them, the v1.0 secondary review, or the earlier pilot's outputs as ground truth.
- Re-coded outputs are written to new, distinctly named files (`PRIMARY_INTERPRETIVE_READER_PROPOSAL.{md,json}` per case) rather than overwriting `CLAUDE_CODING_PROPOSAL.{md,json}`, which remain as v1.0 historical artifacts.
- A specific open disagreement is carried forward rather than resolved by this change: Case 01 Article 8(4) (Commission-EEA-Member States) has both an operative anchor and a documented counter-reading from the earlier pilot's blind RA (that EEA assistance to the Commission's own assessment process fails the regulatory-integration dimension toward Member States). v1.1 does not adjudicate this; it remains for the secondary reviewer and the researcher.

### Integrity note

No file under `methodology/v1.1.0/`, `methodology/production_v1.0/`, `prompts/production/CLAUDE_PRIMARY_CODER.md`, `prompts/production/LUNA_SECONDARY_REVIEWER.md`, `cases/*/corpus/`, `cases/*/primary_coding/CLAUDE_CODING_PROPOSAL.*`, `outputs/CLAUDE_THREE_CASE_PRIMARY_CODING_NOTE.md`, `outputs/LUNA_SECONDARY_REVIEW_NOTE.md`, or any prior pilot artifact was altered, moved, or deleted by this change.

## v1.2 — 2026-09-08

### Change

```text
comitology/co-regulation and pre-norm advisory input treated as categorical exclusions from I
→
regulatory_integration and counterfactual re-read per the researcher's own validation decisions
```

### Trigger

The researcher's human validation pass over the v1.1 three-case proposals, recorded in
`cases/R2_HUMAN_VALIDATION_relations.csv` (20 consolidated relations, "R2" round) and
`cases/R2_HUMAN_VALIDATION_uncertainties.csv` (28 uncertainty entries, decisions in the
`Decisão do pesquisador` / `Correção final` columns). This is a prompt-only, interpretive
revision -- it does not change `methodology/production_v1.1/coding_matrix_schema.json` or
`validate_production_logic.py`, both of which remain current and unversioned by this change.

### Decisions (researcher-authored, adopted verbatim in substance)

1. A comitology committee "assisting" the Commission adopt a binding implementing act that
   governs the target's obligations is a legitimate `I` candidate, not an automatic exclusion
   as co-regulation. Overturned for: Energy Union Committee (case_01, Art. 13(7)(b)), CBAM
   Committee (case_02, Art. 29), and the equivalent committee in case_03 (Art. 36) -- all three
   had been excluded on the co-regulation theory in the v1.1 proposals; the researcher reversed
   all three ("Há relação de intermediação").
2. Advisory/expert input that demonstrably shapes a forthcoming binding norm counts as
   intermediation "em sentido mais amplo" (in a broader sense) even at the proposal- or
   delegated-act-drafting stage, before any target conduct is yet regulated. Overturned for:
   the Advisory Board's opinion on the future 2040 climate target/GHG budget (case_01, Art.
   4(4)-(5)) and Member-State-designated experts consulted before a delegated act (case_02,
   Art. 28(5)).
3. The regulator cannot be its own intermediary -- confirmed (not overturned) for the
   Commission-as-coordinator candidate in case_02 (Art. 12): "A comissão já faz parte do
   regulador." Codified as an explicit rule for future runs.
4. Institutionalization density (dedicated chapter, formal definition, mandatory deadline,
   whistleblower protection, access-to-justice link) is a legitimate reason for two
   structurally similar mechanisms across cases to receive different classifications --
   confirmed for the case_03 Art. 31 vs. case_02 Art. 27(4) third-party-complaint comparison.

### New artifacts

- `prompts/production/PRIMARY_INTERPRETIVE_READER.md` updated in place (v1.1 -> v1.2); prior
  hash `3d2024c669bb70fd361c5c8a5caee923226045ae47625ebf6056244ccb85ac64`, current hash
  `05bdec4c53f61358ee453039bafc1b090631c0208d9615136d335a978c8bf8c7`. No separate frozen copy
  of the v1.1 prompt text was made -- the prior hash above, recoverable from this changelog and
  from `config/production.yaml`'s git history, is the audit trail for this in-place edit,
  consistent with how `config/production.yaml` itself is edited in place across versions.
- `cases/FINAL_DATASET_FOR_HUMAN_REVIEW.csv` -- new consolidated matrix: the 20 relations
  originally in `R2_HUMAN_VALIDATION_relations.csv`, reconstructed from a complete field-by-
  field read of that file captured earlier in the same review session (see integrity note
  below), plus 5 new relations built from the five uncertainty entries the researcher
  explicitly promoted to intermediated status, each pre-marked `APPROVE` with the researcher's
  own words carried into `researcher_note`. All 25 rows carry a `provenance` column. Built by
  `cases/_build_final_dataset.py` (kept for audit).

### Consequences

- Applies to any future recoding of case_01, case_02, or case_03, and to any future case, per
  the same change-control principle as v1.1.
- Does not retroactively alter `PRIMARY_INTERPRETIVE_READER_PROPOSAL.*` (v1.1 outputs),
  `CLAUDE_CODING_PROPOSAL.*` (v1.0 outputs), or the R2 consolidated files. The new final CSV is
  an additive consolidation, not a replacement of any prior artifact.
- One uncertainty remains genuinely unresolved and is not resolved by this change:
  `case_02-U07` (financial/technical assistance to LDCs, Recitals 71/73-74, Art. 30(1)(f)/(8))
  -- the researcher left the decision column blank, and this change does not supply one.

### Integrity note

No file under `methodology/production_v1.1/`, `methodology/v1.1.0/`, `methodology/production_v1.0/`,
any `CLAUDE_CODING_PROPOSAL.*`, any `PRIMARY_INTERPRETIVE_READER_PROPOSAL.*`,
`R2_HUMAN_VALIDATION_relations.csv`, `R2_HUMAN_VALIDATION_uncertainties.csv`, or any prior pilot
artifact was altered, moved, or deleted by this change.

**Source-file corruption discovered during this change.** `R2_HUMAN_VALIDATION_relations.csv`
was read once in full (all 20 rows, all fields) earlier in the same review session. Later in
the same session the file was found on disk resaved with `;` as the field delimiter, without
the double-quoting needed to protect fields whose own free text already used `; `-separated
lists (multiple actors, multiple locations); every field after the first `I` actor lost its
content on every row (file size dropped from 25272 to 10305 bytes). The file was **not
modified further and not "fixed" in place** -- it is the researcher's own working file. The 20
base rows in `FINAL_DATASET_FOR_HUMAN_REVIEW.csv` were instead reconstructed from the
pre-corruption read captured earlier in this session, cross-checked against the (intact)
`relation_id`, `R` (first actor only), `relation_type`, `confidence`, and decision-column values
still readable in the corrupted file (all 20 marked `APROVE` by the researcher). `evidence_quote`
and `contextual_support`, which were not part of that earlier capture, are marked
`NOT_RECOVERED` rather than invented; `coder_note` is marked truncated where the earlier capture
had been length-limited. `FINAL_DATASET_FOR_HUMAN_REVIEW.csv` itself is written with proper CSV
quoting (verified: fields containing `;` are wrapped in `"…"`), so it will not suffer the same
corruption if reopened and resaved by a spreadsheet application.
