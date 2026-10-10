# R4 Complete Work Note
## Chronological methodological record of the R4 digital structural-validation round

**Author:** Igor Caires Machado
**Research context:** collaboration with Professor David Levi-Faur
**Scope:** R4 cross-domain structural validation. Not the Green × Digital governance comparison.

```text
RIT_CODING             = NOT_STARTED
MECHANISM_CODING       = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                   = NOT_STARTED
CORPUS_WIDE_REPAIR     = NOT_EXECUTED
```

---

## R4.0 — Baseline preparation

R4 begins from a completed R3 round on green-transition regulation. Before any digital work
started, the R3 baseline was preserved rather than assumed.

The R3 corpus of five EU instruments (`32003L0087`, `32015D1814`, `32018R0842`, `32021R1119`,
`32023R0955`) and its reconciled totals were brought into R4 as a frozen reference: 5 laws,
89 LAW × ACTOR records, 56 adjudicated relations, 7 LAW × INTERMEDIARY units, 10 mechanism
events and 1 substantive-zero law. The R3 mechanism ontology remains a provisional
researcher-adjudicated construct; R4 does **not** assume it transfers.

Alongside the dataset, the project history and the communications record were reconciled and
archived, so that decisions taken earlier remain auditable from inside R4. The stage closed with
a baseline freeze record.

Evidence: `12_ARCHIVE_SUPPORT/R4_R3_BASELINE_MANIFEST.md`,
`R4_R3_RECONCILIATION.csv`, `R4_R3_HISTORICAL_INTEGRATION_REPORT.md`,
`R4_R3_TO_R4_INTEGRATION_MAP.csv`; `10_FREEZE_AND_INTEGRITY/R4_BASELINE_FREEZE_RECORD.md`.

## R4.1 — Digital corpus construction

Rotem suggested the three digital instruments. Each was retrieved from official EU sources in
its **original** form — not a consolidated version — and frozen with retrieval metadata and a
hash:

| Instrument | CELEX | Structure |
| --- | --- | --- |
| GDPR, Regulation (EU) 2016/679 | `32016R0679` | 99 articles, 173 recitals |
| Digital Services Act, Regulation (EU) 2022/2065 | `32022R2065` | 93 articles, 156 recitals |
| AI Act, Regulation (EU) 2024/1689 | `32024R1689` | 113 articles, 180 recitals, 13 annexes |

Each text was normalised into a processing form with explicit structural markers for recitals,
chapters, articles and annexes, then indexed and quality-checked. The frozen originals remain
authoritative for every later adjudication: throughout the validation stages, reviewers were
required to read the source provision rather than decide from an extracted fragment.

Evidence: `03_SOURCE_DATA_AND_CORPUS/` — corpus register, legal structure index and QC, text
provenance, corpus validation report, and per-instrument retrieval metadata and structural
validation under `source_metadata/`.

## R4.2 — Initial structural extraction

Structural extraction produced **1,404 records**: GDPR 485, DSA 424, AI Act 495. By source,
842 come from operative articles, 546 from recitals and 16 from annexes — only the AI Act
contributes annex records, which is itself a structural difference from the green corpus.

The unit of analysis is **legal provision × actor × legal action**. Each record carries the
actor, the legal verb, a normalised legal action label, a modality category, the action object,
counterpart and recipient, plus conditions, triggers, outputs, legal effects, cross-references,
a source excerpt and a source pointer, along with the extractor's own ambiguity flag and
confidence rating.

This stage is descriptive and pre-theoretical. It does not classify regulators, intermediaries
or targets, and it does not code mechanisms.

Evidence: `03_SOURCE_DATA_AND_CORPUS/R4_STRUCTURAL_EXTRACTION.csv` (immutable);
`04_R4_2_STRUCTURAL_EXTRACTION/` — run summary, coverage report, actor candidate register,
legal action register, definition register, cross-reference register and ambiguity log.

## R4.2B — Human QA preparation

A stratified human QA sample was drawn and reviewed through an offline panel. The stage produced
an ambiguity typology, a confidence calibration table, a correction register and a systematic
error audit, later updated.

Two cross-model-supported patterns emerged as candidate problems:
`COUNTERPART_RECIPIENT_OVERATTRIBUTION` and `ACTOR_ACTION_FRAGMENTATION`.

Evidence: `05_QA_AND_HUMAN_ADJUDICATION/` — `R4_2B_*` files and
`human_review_interface/`.

## R4.2C — Cross-model review

Two model families were used to review the extraction independently, and their outputs compared.
This stage also produced an explicit **model provenance correction**: outputs initially attributed
to one model were reclassified once their provenance could not be confirmed.

That correction matters methodologically, and it is included in this package deliberately. The
project's position throughout has been that an unverifiable runtime label is recorded as
unverifiable rather than resolved by assumption. The same discipline is applied later to the
Claude model label.

Evidence: `05_QA_AND_HUMAN_ADJUDICATION/R4_2C_MODEL_PROVENANCE_CORRECTION.md`,
`R4_2C_OUTPUT_RECLASSIFICATION.csv`, the Luna/Terra comparison tables, the Terra calibrated and
independent reviews with their freeze manifests, and the closure report. Byte-differing working
copies are preserved under `r4_2c_working_copies/`.

## R4.2D — Human diagnostic

Twelve cases were selected purposively, all with cross-model support, and adjudicated by the
human researcher. All 12 contained confirmed structural defects.

Two points about interpretation are essential:

1. **This is not a 100 per cent corpus error rate.** The cases were selected *because* models
   flagged them. They are diagnostic evidence about failure modes, not an estimate of prevalence.
2. **The model detection pattern frequently differed from the human root cause.** What the models
   flagged as counterpart/recipient over-attribution often turned out, on human reading, to be a
   proposition-boundary or predicate-reconstruction failure instead.

From this diagnostic the researcher froze **15 candidate structural rules**, covering preservation
of the legal verb and modality, the treatment of passive constructions and missing actors, the
principle that a preposition does not imply a recipient, the requirement that a relational entity
be actor-capable, the preservation of proposition boundaries and coordinated predicates, and the
prohibition on the object acting as a residual bucket. The fifteenth records the distinction above:
`MODEL_DETECTION_PATTERN_DOES_NOT_EQUAL_HUMAN_ROOT_CAUSE`.

These rules are guidance for later stages, not automatic truth, and they were not modified by any
later AI stage.

Evidence: `05_QA_AND_HUMAN_ADJUDICATION/R4_2D_human_diagnostic/` — the diagnostic sample, the
completed human adjudication, the summary, the narrative report, the rule candidates and the
adjudication panel.

## R4.2E-A — Candidate triage

A deterministic heuristic was run across all 1,404 records, classifying each as a repair
candidate:

| Classification | Count |
| --- | --- |
| YES | 713 |
| UNCERTAIN | 346 |
| NO | 345 |

with complexity distributed as NONE 345, SIMPLE 160, MODERATE 514, COMPLEX 385.

These are **candidate signals, not confirmed defects**. The heuristic's validity was tested
against the known human cases: it rediscovered **9 of 12** and missed three
(`R4_2D-QA2B-026`, `-056`, `-089`), which remain recorded blind spots. A triage step that misses
a quarter of known defects cannot be treated as a defect detector, and it was not.

Evidence: `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_A_triage/`.

## R4.2E-B0 — Compression

Reviewing 524 candidate records individually with an advanced model was not affordable, so the
candidates were compressed into **211 repair families** sharing a structural signature, with
routes assigned:

| Route | Records |
| --- | --- |
| NO_REPAIR | 698 |
| TEMPLATE_VALIDATION_REQUIRED | 489 |
| ADVANCED_MODEL_CASE_REVIEW | 32 |
| HUMAN_ONLY | 185 |
| DETERMINISTIC_SAFE_CANDIDATE | 0 |

Advanced-review workload fell from **524 to 131** cases (99 family representatives plus 32
individual cases), and the human-only burden was reduced to 185 reserved cases.

B0 also froze a **relational field strategy**: counterpart and recipient must be evaluated
independently, with a separate rationale recorded for each, rather than inferring one from the
other. At that point the extraction showed counterpart and recipient populated together in 995
records and identical in all 995, with zero counterpart-only and zero recipient-only. This was
recorded as an operational observation, explicitly not as theoretical equivalence, and neither
field was merged or deleted.

The compression rests on one assumption: that a family's representative is representative. R4.2E-B1
later tested that assumption and found it does not always hold.

Evidence: `06_REPAIR_TRIAGE_AND_COMPRESSION/R4_2E_B0_compression/`.

## R4.2E-B1 — Advanced validation

B1 reviewed **143 cases**: 99 family representatives, 32 individual advanced cases, and **12
NO_REPAIR diagnostic controls** inserted from records B0 had declared to need no repair. Cases
were allocated into four frozen batches of 36, 36, 36 and 35.

Each case was reviewed against the frozen legal source, identifying the proposition anchor and
then assessing actor, action, object and the two relational fields separately, with modifiers
separated out.

Batches 1 to 3 were reviewed with GPT-5.6 Terra High under OpenAI Codex. That environment reached
its usage limit after batch 3 was frozen, and batch 4 was completed in Claude Code as a planned
continuity fallback. No earlier batch was rerun, reopened or relabelled.

**Frozen B1 results across 143 cases:**

| Defect decision | Count |
| --- | --- |
| YES | 111 |
| PARTIALLY | 15 |
| NO | 17 |
| ABSTAIN | 0 |

Proposition anchor confidence: HIGH 124, MEDIUM 12, LOW 7. Field corrections: Actor 47,
Action 87, Object 83, Counterpart 88, Recipient 98.

**These proportions do not estimate corpus prevalence.** The B1 set was constructed by selecting
family representatives and individually flagged cases — that is, by concentrating suspected
defects. It is an enriched validation set.

Three recurring defect families were identified: span-boundary errors, where the action or object
span cuts across a grammatical constituent or absorbs its neighbour; cross-sentence relational
copying, where counterpart and recipient hold a phrase lifted from a different sentence; and
coordinated-predicate collapse, where a second obligation is buried inside the object of the
first. The third is the most consequential, because it silently removes obligations from the
dataset rather than merely misplacing text.

Evidence: `07_ADVANCED_VALIDATION_B1/`.

## Diagnostic controls

The twelve controls were unblinded only after each batch was frozen and hashed.

| Result | Count |
| --- | --- |
| CLEAN_CONFIRMED | 5 |
| DEFECT_FOUND | 7 |
| PARTIAL_DEFECT | 0 |
| ABSTAIN | 0 |
| SERIOUS | 0 |

Defective controls: EXT-000085 (B1-01, local), EXT-000919 (B1-02, unclassified — it predates the
severity taxonomy), EXT-000163 and EXT-000660 (B1-03, moderate), EXT-000093, EXT-000777 and
EXT-000937 (B1-04, moderate).

**Blinding was not guaranteed.** The control sample file lists all twelve controls with no batch
column, and the protocol requires reading it to unblind each batch in turn. Any reviewer who had
already unblinded an earlier batch had therefore seen the remaining control identities. This is
confirmed for batch 4 and structurally possible for batches 2 and 3; it cannot be verified from
the repository for the Terra batches. Accordingly these are described throughout as
**NO_REPAIR diagnostic controls**, never as blind controls, and **no false-negative rate is
calculated from them**.

### `B0_COMPRESSION_REASSESSMENT_REQUIRED`

The gate is set, and the reasoning is not a count alone.

Supporting reassessment: seven of twelve controls drawn from the `NO_REPAIR` route contain
structural defects, so that route's assertion did not hold for the majority of its sampled
members; the same failure types recur across batches and across both reviewing models; and
within-family heterogeneity is demonstrated — family `RF-098E1C096964` returned two clean controls
and one defective, family `RF-4EAB0DF25480` returned two defective, and six families in total
returned disagreeing representatives, covering 141 corpus records.

Limiting it: no control was graded serious, none showed proposition-anchor failure, and none
showed systematic actor invention. In every defective control the anchored legal proposition
remained identifiable.

**The conclusion therefore concerns coverage and family representativeness, not proof that the
corpus is broadly corrupted.** The `NO_REPAIR` route of 698 records cannot be treated as
validated-clean on this evidence, and one representative per family is insufficient where
representatives disagree.

## R4.2E-B1S — Action representation sensitivity audit

After B1 closed, final QA identified a problem with the review instrument rather than the corpus.

The B1 review input presented an Action field populated from `LEGAL_ACTION` alone.
`LEGAL_ACTION` is a controlled-vocabulary label such as "notify or inform". The extraction
separately holds `LEGAL_VERB`, which carries the source predicate with its modality, and a
`MODALITY` category. Deterministic verification:

- explicit modal in `LEGAL_VERB`: **1,370 / 1,404**
- explicit modal in `LEGAL_ACTION`: **5 / 1,404**
- `LEGAL_VERB` identical to `LEGAL_ACTION`: **0 / 1,404**
- `LEGAL_ACTION` a substring of `LEGAL_VERB`: **991 / 1,404**

Reviewers working from that input therefore saw an Action field that looked stripped of deontic
force and recorded it as defective. The modality had not been lost; it was in a column they were
not shown.

All 143 Action judgments were re-examined against the full representation. No case was rerun and
no frozen adjudication was modified.

| | Count |
| --- | --- |
| `B1_ACTION_JUDGMENT_STABLE` | 66 |
| `B1_ACTION_JUDGMENT_CHANGES` | 26 |
| `B1_ACTION_JUDGMENT_PARTIALLY_CHANGES` | 16 |
| `ACTION_REPRESENTATION_NOT_MATERIAL` | 35 |
| `UNCERTAIN_REQUIRES_HUMAN` | 0 |

`ORIGINAL_B1_ACTION_CORRECTION_COUNT = 87` (frozen, not overwritten).
`SENSITIVITY_ADJUSTED_ACTION_CORRECTION_COUNT = 63` (descriptive).
26 Action decisions changed — 25 from defective to correct, one the other way.
Terra 57 → 33; the Claude batch 30 → 30, because it was already scored against the full record.

**Only 1 of 143 overall defect decisions is materially affected** (EXT-000840, where Action was
the sole basis and the reviewer note states the modal was lost when it was not). In the other 24
flipped cases the record was defective on other fields anyway. Sensitivity-adjusted defect totals,
descriptive only and reported beside the frozen ones: YES 111, PARTIALLY 14, NO 18.

Two Action defect classes survive the audit as **real, not representational**: entitlement
constructions recorded without "shall" and with `MODALITY = UNCLEAR`, and coordinated predicates
buried inside the object.

The audit also confirmed that none of the seven defective controls was defective on Action grounds
alone, so the B0 gate is unaffected.

The general lesson is worth stating: a coding interface that shows a coder one of several fields
holding a construct will produce confident, systematic, wrong judgments about that construct.

Evidence: `08_ACTION_SENSITIVITY_AUDIT/`.

## Variable parsimony findings

All figures recomputed deterministically over the full 1,404 records.

### Counterpart / Recipient

Exact textual equality across **1,404 / 1,404** rows — 995 where both are populated, 409 where
both are empty — with zero counterpart-only and zero recipient-only.

Advanced review, however, returned:

| Differentiation | Count |
| --- | --- |
| NEITHER | 95 |
| RECIPIENT_ONLY | 27 |
| COUNTERPART_ONLY | 14 |
| UNCERTAIN | 7 |
| BOTH_SAME_ENTITY_JUSTIFIED | 0 |
| DIFFERENT_ENTITIES | 0 |

GDPR Article 14(2) names the data subject as an express addressee with no counterpart; under
Article 17(1) the data subject obtains erasure *from* the controller, which is a counterpart and
not an addressee.

**Interpretation: operational collapse, with a potential conceptual distinction.** The identity
across the corpus is an artefact of how the extractor populated the fields — it copied one span
into both — not evidence that the positions coincide. Note also that review never once found an
entity genuinely occupying both positions. **Merger is not recommended at this point.**

### Action Object / Information-or-Material Object

Exact textual equality across **1,404 / 1,404** rows, never populated independently, and no
reviewed case distinguished them. Status: **strong redundancy candidate**. This is the cleanest
parsimony result in the round — one variable currently coded twice.

### Structural Ambiguity / Extraction Confidence

`EXTRACTION_CONFIDENCE = LOW` coincides exactly with `STRUCTURAL_AMBIGUITY = YES`, but
`AMBIGUITY = NO` splits into HIGH (263) and MEDIUM (139). The relationship is a **one-way
deterministic transformation**: ambiguity is derivable from confidence, not the reverse.
`STRUCTURAL_AMBIGUITY` is a candidate for removal; `EXTRACTION_CONFIDENCE` is not. The two are
**not** perfectly equivalent, and an earlier formulation in this project that implied they were
has been corrected.

Separately, within the enriched B1 set, extraction confidence did not separate defective from
non-defective records: of 25 reviewed cases the extractor rated HIGH, review returned 18 YES and
5 PARTIALLY against 2 NO. This is not a validated predictive-performance result and cannot
estimate corpus accuracy; it does mean the flag cannot be used to decide what to skip.

### Legal Action / Legal Verb

Never identical; `LEGAL_ACTION` is not even a substring of `LEGAL_VERB` in 413 records.
**Complementary, not redundant.** Action should be treated as a structured construct across
`LEGAL_ACTION`, `LEGAL_VERB` and `MODALITY`, and never assessed from the normalised label alone.

### Modality / Legal Verb

Partial functional overlap: the verb span largely predicts the category. But the category is not
reliably correct — absence-of-obligation is coded PROHIBITED (EXT-000001) and unconditional duties
are coded CONDITIONAL (EXT-000527, EXT-000937). **Retain pending codebook redesign and an enum
audit.**

Evidence: `08_ACTION_SENSITIVITY_AUDIT/R4_VARIABLE_REDUNDANCY_AUDIT.csv`.

## Templates

| Status | Count |
| --- | --- |
| Unconditional `VALIDATED` | **0** |
| `VALIDATED_WITH_CONDITIONS` | 64 |
| `REQUIRES_MORE_REPRESENTATIVES` | 16 |
| `HUMAN_REVIEW_REQUIRED` | 9 |
| `REJECTED` | 8 |
| `N/A` | 2 |

Grouping by family, **50 conditionally validated repair families** have all their reviewed
representatives at `VALIDATED_WITH_CONDITIONS`, covering **296 corpus records**. A further 141
records sit in six families whose representatives disagree and are excluded.

The term *fully validated families* is not used anywhere in this package, because no template
reached unconditional validation. 296 is an eligibility ceiling, not an applied repair.

## New structural diagnostic candidates

Seven issues were recorded for researcher adjudication without modifying the 15 frozen rules:
the absence of a coding convention for passives with an explicit by-agent; modality
misclassification of absence-of-obligation and of unconditional duties; action spans absorbing
the object head; relational fields quoting a different sentence; empty source excerpts in 181 of
1,404 records; and within-family heterogeneity defeating single-representative compression.

Evidence: `07_ADVANCED_VALIDATION_B1/combined_reports/R4_2E_B1_NEW_STRUCTURAL_DIAGNOSTIC_CANDIDATES.csv`.

## Final R4 structural status

```text
R4_2E_B1_ACTION_SENSITIVITY_AUDIT_COMPLETE
R4_DIGITAL_STRUCTURAL_VALIDATION_READY_FOR_DAVID
```

**Not** `R4_COMPLETE`, and not a Green × Digital governance comparison. Substantive R/I/T and
mechanism coding remain future work, and the recommended next step is to reassess the B0
compression design before designing any corpus-wide repair.

## Why this sequence was chosen

R/I/T and mechanism coding both read *from* the structural fields. If counterpart and recipient
are populated by copying one span into both, every downstream inference about who intermediates
between whom inherits that artefact — and it would be invisible at the theoretical layer, because
the data would look internally consistent. Likewise, an obligation absorbed into another record's
object cannot later be coded as a mechanism, because as far as the dataset is concerned it does
not exist.

Validating the structural layer first therefore establishes that the green unit of analysis
applies to digital law, identifies which variables carry information and which pay twice for the
same signal, and fixes the relational fields before they are used to make claims about
intermediation — which is the substantive question the project exists to answer.
