# R4.2 Method Note — AI-Assisted Structural Extraction

**Status:** `R4_2_STRUCTURAL_EXTRACTION_COMPLETE_PENDING_HUMAN_REVIEW`
**Date:** 2026-09-26
**Baseline:** `a90ccc0605ea03ac9374a8d9bd0217983633f843`
**Human corpus acceptance:** `APPROVED`
**Rotem coding consulted:** `NO`

## Scope and boundary

R4.2 is a structural extraction phase. It represents explicit legal text as evidence and does not identify regulators, intermediaries, targets or regulatory intermediation mechanisms. No `R`, `I` or `T` fields were created, and no R3 substantive classification was imported.

The empirical sources were limited to the frozen original Official Journal XHTML files and their traceable normalized processing copies for:

- GDPR — CELEX `32016R0679`;
- DSA — CELEX `32022R2065`;
- AI Act — CELEX `32024R1689`.

No consolidated text, commentary, academic source, prior AI summary or Rotem material was used.

## Corpus acceptance

The researcher acceptance required by the R4.2 prompt was recorded as `HUMAN_CORPUS_ACCEPTANCE=APPROVED`. The corpus register now marks all three cases `VALIDATED_AND_FROZEN`; original source hashes were not changed.

## Extraction strategy

The processing copies were traversed independently by case in the sequence GDPR, DSA and AI Act. The parser processed every marked operative article, recital and available annex, retaining source type distinctions. Article paragraphs and lettered points were kept as separate structural segments where the processing copy exposed them.

The primary output unit is `LEGAL PROVISION × ACTOR × LEGAL ACTION`. A provision can therefore produce multiple rows. Each row retains CELEX, structure pointer, source type, textual actor, provisional textual normalization, descriptive legal verb/action, modality, objects, counterpart/recipient where explicit, conditions/triggers, cross-references, excerpt, confidence and human-review status.

## Model and runtime disclosure

The requested model designation was `GPT-5.6 Luna High`. The connected runtime did not expose a Luna/Terra variant identifier; the execution therefore records the actual environment as `Codex GPT-5 runtime; GPT-5.6 Luna High requested; exact runtime variant not exposed`. This is a provenance limitation, not a retrospective claim that an unobservable variant was used.

No Terra escalation occurred. The extraction used structural parsing and normalization only; ambiguity flags were retained for human review rather than resolved through substantive legal interpretation.

## Normalization rules

- `ACTOR_TEXT` preserves the textual actor phrase.
- `ACTOR_NORMALIZED_PROVISIONAL` lowercases and removes only obvious leading articles; theoretical equivalence is not inferred.
- `ACTOR_TYPE_TEXTUAL` uses descriptive textual categories and never assigns regulator, intermediary or target roles.
- `LEGAL_ACTION` is a descriptive verb normalization such as provide information, submit/transmit, notify/inform, conduct assessment, designate/appoint, cooperate, monitor, verify, request/require or issue/adopt decision.
- Legal actions are not mapped to the R3 codebook or to any mechanism category.
- Explicit cross-references are registered but are not automatically interpreted as relational or institutional roles.
- Recitals and annexes remain separate from operative articles.

## Confidence and ambiguity

`HIGH` indicates a clear textual actor/action relationship. `MEDIUM` indicates a cross-reference or longer structural context. `LOW` marks multiple structural matches, coordination, pronoun dependence or another parsing issue. Low-confidence and ambiguous records are flagged `HUMAN_REVIEW_REQUIRED=YES` and remain `PENDING`.

The ambiguity log concerns extraction/parsing only. It does not contain R/I/T adjudications, intermediary disputes or mechanism disputes.

## QA procedure

The package includes:

- source coverage for all 99 GDPR articles, 93 DSA articles, 113 AI Act articles, 509 recitals and 13 AI Act annexes;
- duplicate-key suppression at the provision/actor/action/excerpt level;
- checks for missing source pointers, missing actors/actions, invalid case IDs and orphan actor IDs;
- cross-reference registration;
- a stratified human QA sample across confidence levels and source types where records were available;
- run summaries with confidence, ambiguity, review and escalation counts.

No substantive human adjudication was performed in this phase. Human review is pending and must assess extraction fidelity only.

## Outputs

The generated outputs are in `03_extraction/`:

`R4_STRUCTURAL_EXTRACTION.csv`, `R4_DIGITAL_ACTOR_CANDIDATE_REGISTER.csv`, `R4_LEGAL_ACTION_REGISTER.csv`, `R4_CROSS_REFERENCE_REGISTER.csv`, `R4_STRUCTURAL_AMBIGUITY_LOG.csv`, `R4_2_AI_EXTRACTION_RUN_SUMMARY.csv`, `R4_2_SOURCE_COVERAGE_REPORT.csv`, `R4_2_HUMAN_QA_SAMPLE.csv` and `R4_LEGAL_DEFINITION_REGISTER.csv`.

## Limitations

The extraction is a machine-generated structural representation, not a legal interpretation. Actor phrase detection, long coordinated provisions, pronouns and distributed cross-references can require human correction. The requested Luna designation could not be independently verified from the runtime. No Terra escalation was triggered, and no comparison across legal domains or with R3/Rotem was performed.

## Stop condition

R4.2 stops after this structural extraction package. The next phase must separately authorize any regulator, intermediary, target, R–I–T, mechanism or cross-domain interpretation.
