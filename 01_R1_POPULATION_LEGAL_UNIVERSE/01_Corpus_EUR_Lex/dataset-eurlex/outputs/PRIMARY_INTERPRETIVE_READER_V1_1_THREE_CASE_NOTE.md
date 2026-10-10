# Three-case v1.1 recoding — handoff note

**To:** Secondary Critical Reviewer, researcher
**From:** Primary Interpretive Reader, production v1.1
**Scope:** case_01 (Climate Law), case_02 (CBAM), case_03 (EUDR) — full fresh recoding under
`prompts/production/PRIMARY_INTERPRETIVE_READER.md` and
`methodology/production_v1.1/coding_matrix_schema.json`
**Status:** proposals only — not ground truth, not adjudicated, not yet secondarily reviewed

Each case was recoded by a separate, memoryless run reading only that case's own frozen
corpus and the v1.1 prompt. No run had access to its own v1.0 proposal, the v1.0 secondary
review, or (for case_01) the earlier intensive pilot. Model and prompt version were held
constant across all three runs and across the v1.0 and v1.1 cycles (see each case's
`RUN_METADATA.yaml`), so differences between v1.0 and v1.1 counts below are attributable to
the protocol change, not to a different underlying model.

## 1. Volume per case, v1.0 vs v1.1

| Case | v1.0 total | v1.0 intermediated | v1.1 total | v1.1 intermediated | v1.1 direct | v1.1 uncertain |
|---|---|---|---|---|---|---|
| case_01 — Climate Law | 7 | 1 | 4 | **0** | 4 | 0 |
| case_02 — CBAM | 22 | 5 | 15 | **7** | 8 | 0 |
| case_03 — EUDR | 10 | 3 | 9 | **2** | 6 | 1 |
| **Total** | **39** | **9** | **28** | **9** | **18** | **1** |

The totals are not a validity signal in either direction. v1.1 is more selective about what
enters the main matrix at all (recital-only candidates now go to the uncertainty log by
design, per the operative-anchor rule), which alone shrinks every case's total independent of
any change in intermediated findings. The aggregate intermediated count is unchanged (9→9),
but its composition shifted across all three cases — this is the expected and intended effect
of re-testing each candidate on its own, not a wash to be read as "nothing changed."

## 2. Case 01 — the sequence change produced a different answer, not just a different process

Zero relations were coded `intermediated`. The closest candidate, the EEA under Article 8(4)
("shall assist the Commission in the preparation of the assessments"), was tested against
the actual Commission→Member States relations it was proposed to mediate (Articles 6–7) and
failed on two of five dimensions: **regulatory_integration = NO** (the duty runs toward the
Commission's own report-preparation, not toward Member States) and **counterfactual = NO**
(Article 8(3) supplies multiple alternative evidentiary sources, so removing the EEA does not
remove a step of the Commission→Member-States mechanism). This is the same substantive
concern the earlier pilot's blind reference adjudication raised about this identical
provision, reached independently here through the new functional test rather than by
consulting that adjudication (which this run could not access). It remains flagged
`[reviewer_attention: conceptual_boundary]` as a genuinely close call, not a settled negative
— the secondary reviewer should re-examine it on the same five dimensions.

A weaker parallel candidate (Article 3(4)'s EEA-notification duty) is retained as `direct`
but flagged `[reviewer_attention: possible_overcoding]` for being possibly too thin to count
as a regulatory relationship at all; the researcher should look at this one skeptically in
the other direction.

## 3. Case 02 — the largest matrix, seven intermediated relations across three distinct patterns

**Verification/certification pattern** (rel-003, rel-004, rel-006): accredited verifiers and
an independent certifying person check declarant- or third-country-operator-supplied
emissions or carbon-price data before it reaches the Commission or competent authority. All
three pass the functional test at `high` or `medium` confidence with all five dimensions
`YES`.

**Tax-authority certification** (rel-002): a Member State tax authority's confirmation of an
applicant's tax-debt status is a documented input to the competent authority's authorisation
decision (Article 17(2)(a)) — a narrower, more procedural intermediation than the others, at
`medium` confidence.

**Customs-authority pattern** (rel-008, rel-009, rel-010): customs authorities enforce the
authorised-declarant-only import restriction at the border, and separately transmit import
data feeding Commission/competent-authority risk analysis and the transitional reporting
regime. All three pass at `high` confidence. This is the same general customs-as-intermediary
question raised in v1.0, now resolved relation-by-relation with an explicit test rather than
as a single undifferentiated flag.

Two relations remain flagged `[reviewer_attention: conceptual_boundary]` beyond the above:
rel-007 (accreditation body vs. a not-yet-operative Commission standard-setting function) and
rel-012 (Commission/competent-authority framing that could alternatively be read as
co-regulation rather than intermediation). rel-015 sits at the edge of the construct because
its T is a third country rather than a firm-level actor. None of the seven intermediated
relations themselves carry an overcoding or undercoding flag.

## 4. Case 03 — two intermediated relations survive a stricter test than v1.0 applied

**Customs enforcement of competent-authority compliance findings** (rel-001, `high`
confidence): unchanged in substance from the pattern v1.0 also found, now with a full
five-dimension record.

**Substantiated-concerns reporting channel** (rel-002, `high` confidence, Article 31): any
natural or legal person submitting a substantiated concern triggers a competent-authority
duty to assess it and can lead to checks, hearings, or interim measures — this passes all
five dimensions cleanly.

The Article 33 Commission information system — coded `intermediated` with a
`possible_overcoding` flag in v1.0 — is **not** in the main matrix as `intermediated` under
v1.1. Under the actor-versus-instrument guidance new to this version (a system is an
instrument unless the text attributes it an independently exercised function), this run
treated it more cautiously; the researcher should check the uncertainty log's account of it
directly rather than infer more from this note than the file supports.

## 5. Recurring actor types and mechanisms

Competent authorities and the Commission remain the dominant R across all three cases,
sometimes jointly. Recurring I types: accredited verifiers and independent certifiers
(case_02), customs authorities (case_02, case_03), and — new in this cycle — a tax authority
(case_02) and ordinary reporting third parties (case_03). No relation in any case coded an
object (a report, certificate, due-diligence statement, emissions figure) as T. Mechanisms
observed: `monitoring_supervision`, `standard_setting`, `information_transmission`
(case_01); the full spread including `certification`, `verification`, `accreditation`,
`enforcement_support`, `information_transmission`, `monitoring_supervision`, `reporting`,
`other_mechanism` (case_02); `enforcement_support`, `reporting`, `monitoring_supervision`,
`standard_setting` (case_03).

## 6. Recital-only contextual candidates (new category, not in the main matrix)

Three across the three cases: case_01's Recital 22 (a carbon-removal certification
framework with no operative anchor in this act); case_02's Recital 72 (a possible "Climate
Club" reference) and Recitals 71/73/74 (LDC financial/technical assistance); case_03's
Recital 31 (an "EU Observatory" with no operative-article anchor at all). Each is logged with
`issue_type: contextual_candidate_recital_only` and a note on what operative anchor, if any,
would be needed to promote it. None should be read as evidence that recitals are
substantively empty — only that this version does not let a recital alone carry a positive
classification.

## 7. Priority review for the Secondary Critical Reviewer and the researcher

1. **case_01, Article 8(4) (EEA)** — the recurring, still-open question across every version
   of this project's methodology. Re-run the five-dimension test independently.
2. **case_03, Article 33 information system** — check whether this run's more conservative
   actor-vs-instrument reading, or v1.0's `intermediated`-with-overcoding-flag reading, is
   better supported; this is the clearest test case for the new instrument/actor guidance.
3. **case_02, rel-012 and rel-007** — co-regulator vs. intermediary, and accreditation body
   vs. future standard-setter, both flagged `conceptual_boundary`.
4. **case_01, Article 3(4) (`possible_overcoding`)** and **case_03, rel-003 equivalent
   candidates logged as `uncertain`** rather than forced positive — check these did not
   under-code.

## 8. What this note does not claim

No relation here has been reviewed by the Secondary Critical Reviewer, adjudicated by the
researcher, or treated as superior to the v1.0 proposals, the v1.0 secondary review, or the
earlier pilot. A lower or higher intermediated count than v1.0 is not, by itself, evidence
that v1.1 is more or less accurate — both await independent review and researcher
adjudication under the newly versioned schema.
