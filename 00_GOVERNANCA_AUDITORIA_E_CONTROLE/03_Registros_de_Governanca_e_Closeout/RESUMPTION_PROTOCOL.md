# Resumption Protocol — External Review Hold

**Current state:** `EXTERNAL_REVIEW_PENDING`
**Trigger:** substantive feedback from David Levi-Faur and/or Rotem Medzini

## Entry condition

Do not resume substantive research because of silence, elapsed time, a link update or an unverified delivery signal. Resume only after an identifiable response is received and registered in `EXTERNAL_REVIEW_REGISTER.md`.

## Required sequence

### 1. Preserve the response

Save the original response verbatim, including attachments or links as received, with sender, date, channel, message identifier if available, and SHA-256 where a local file is saved. Do not edit the original. Create a working copy for analysis.

### 2. Classify the feedback

For each substantive statement, assign one of:

- `EXPLICIT_AUTHOR_RECOMMENDATION`
- `AUTHOR_QUESTION`
- `METHODOLOGICAL_OBSERVATION`
- `REQUEST_FOR_EVIDENCE`
- `OUR_INTERPRETATION`
- `UNRESOLVED`

Only explicit author recommendations are treated as authorization to change an author-owned conceptual or coding artifact. Questions and observations require an interpreted response and, where appropriate, a new human decision.

### 3. Map impact before editing

Create a change-impact matrix with at least these columns:

| Feedback_ID | Exact statement | Classification | Affected stream | Affected artifact/version | Rule or field | Evidence | Historical records affected | Proposed action | Human decision required |
|---|---|---|---|---|---|---|---|---|---|

Map conceptual feedback to the manuscript reconstruction, ontology and ARQGOV model. Map Rotem feedback to the revised codebook, workbook fields, pilot rules, provision events and documented decisions. Identify whether the request is clarification, documentation, optional extension, reclassification or structural change.

### 4. Protect the frozen baseline

Never overwrite the baseline. Copy the affected artifact into a dated working area, record its original hash, and preserve the pre-change version. Do not modify historical source documents, the 19 human decisions, the Rotem workbook, preregistered rules or the ARQGOV v1.2 archive during initial review.

### 5. Decide whether human adjudication is required

Human adjudication is required when feedback changes an inclusion rule, actor/action/recipient relation, function boundary, recognition pathway, modality, condition, or interpretation of a previously adjudicated record. A model review may prepare a queue, but cannot replace the human decision.

### 6. Prepare proposed revisions

For every accepted change, record:

- old and proposed definition or rule;
- exact source and rationale;
- affected records and expected retrospective impact;
- compatibility with the existing codebook and workbook;
- whether the change is conceptual, documentary or operational;
- required human adjudication;
- implementation and rollback plan.

Do not call the revised state validated until the required human and author decisions have been completed and documented.

### 7. Resume broader development only after decisions are closed

Production coding, model publication, manuscript incorporation and dataset consolidation remain suspended until the relevant external decisions are recorded. Update the closeout register, version identifiers, hashes and project status at each approved transition.

## Status vocabulary

- `EXTERNAL_REVIEW_PENDING`: no substantive external decision has been incorporated.
- `FEEDBACK_REGISTERED`: response preserved and classified; no baseline changed.
- `IMPACT_ANALYSIS_IN_PROGRESS`: change-impact matrix and human-review queue prepared.
- `DECISION_PENDING`: author or human adjudication is required.
- `REVISION_AUTHORIZED`: explicit authorization and documented scope exist.
- `BASELINE_UPDATED`: approved changes implemented, validated and versioned.

The project must return to `EXTERNAL_REVIEW_PENDING` whenever a new external response opens a new issue.
