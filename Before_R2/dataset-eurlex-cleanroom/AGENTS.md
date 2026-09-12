# AGENTS.md — operating rules for this repository

This file binds any agent (human or LLM) that reads, writes, or codes in
this project. It is the operational distillation of the project's
methodological contract. When in doubt, stop and ask the researcher rather
than proceed past a gate.

## 0. Clean-room boundary (hard rule)

This project's only permitted relationship to `../dataset-eurlex` is via
*general* methodological lessons, theoretical references, and
infrastructure patterns (directory layout, manifest conventions, hashing
approach). It is forbidden to read or import from that project:

- relation datasets, actor-role datasets, LLM outputs, researcher
  adjudications, relation counts, case-specific coding decisions,
  benchmark files, or uncertainty decisions.

Do not open files under `../dataset-eurlex/cases/`, `../dataset-eurlex/outputs/`,
or `../dataset-eurlex/methodology/production_*` while working in this
repository. If you need a methodological reference from that project,
summarize the *general* lesson from memory/documentation only — never quote
or paraphrase its case-specific empirical content.

## 1. State machine — never advance past a gate without explicit instruction

```
setup → source_acquired → corpus_locked → methodology_locked →
primary_complete → secondary_blind_complete → cross_review_complete →
awaiting_human_validation → human_validated → final_dataset_locked
```

Current state is tracked in `logs/STATE.md`. Read it before doing anything.
Every gate transition requires the researcher's explicit instruction —
this includes methodology lock, any primary/secondary coding run, cross
review, building `dataset/`, human validation, and `final/`.

## 2. Analytical architecture (four levels)

1. **Act / regulatory regime** — the case as a whole.
2. **Actor-in-role** — the principal substantive unit. Roles (Regulator /
   Intermediary / Target — R/I/T) are **relational, not permanent
   identities**. The same organization can be R in one relation and T or I
   in another. Never assign a fixed R/I/T label to an organization itself.
3. **Intermediary function / mechanism** — what a third actor institutionally
   does within the regulatory process.
4. **Regulatory relation / episode** — the coding and evidentiary unit.
   Every claim must cash out as a relation: R, T, regulatory action,
   regulated behavior/object, third actor(s), function(s), evidence.

## 3. Third-actor test (apply before coding any X as intermediary)

For every plausible third actor X:

- A. Is X distinct from R and T?
- B. Does the *operative* legal text assign or recognize a function performed by X?
- C. Does the function materially contribute to the regulatory process involving R and T?
- D. Is the function institutionally integrated, not merely external influence?
- E. Orientation: target_facing / regulator_facing / bidirectional / uncertain?
- F. If X's function were removed, would a distinct functional contribution be lost?
- G. Is the claimed function supported by operative text (not recitals alone)?

Do not mechanically infer intermediary status from these fields — apply
substantive interpretation. Reject if: third-actor mention only, keyword
hit only, instrument mistaken for actor, or influence-on-R without an
institutionally integrated function.

## 4. Guardrails

- **A recital alone cannot support a positive regulatory relationship.**
  Recitals are contextual (`act_recitals.md`); the coding corpus is
  `act_operative.md`.
- **Actor ≠ instrument.** Reports, databases, information systems,
  platforms, certificates, methodologies, schemes, and documents are not
  actors unless the operative text identifies the legal actor behind them.
- **Proposer ≠ regulator, automatically.** Do not assume the institution
  that proposed the legislation is R in every relation it appears in.
  Distinguish legislative proposer / formal adopter / rule-maker /
  regulator / implementing regulator / oversight authority / intermediary
  / target case by case.
- **Mechanism taxonomy is two separate fields**, never collapsed into one:
  - `intermediary_function` (free-text/controlled, substantive description)
  - `project_mechanism_family` ∈ {reporting, certification, ranking_rating,
    auditing, outside_four, uncertain} — do not force-fit every function
    into one of the first four; use `outside_four` or `uncertain` rather
    than distort the taxonomy.

## 5. Corpus rules (already enforced by `scripts/normalize_corpus.py`)

- No translation, no summarization, no paraphrasing, no semantic labels.
- Article/paragraph/recital numbering is preserved verbatim (it is embedded
  in the source text itself — the converter does not add or remove it).
- `act_operative.md` is the primary coding corpus (articles + annexes).
- `act_recitals.md` is contextual only.
- Every derived file is hashed in `corpus_manifest.yaml`; re-run
  `scripts/validate_corpus.py` after any change to confirm consistency.

## 6. Coding-run isolation (once methodology is locked)

- Each case's primary reader may access **only**: its own case corpus,
  the locked methodology, the locked primary prompt, and the locked
  schemas. It may not access other case outputs, `../dataset-eurlex`,
  secondary outputs, or human decisions.
- Secondary review Pass 1 is **blind**: corpus + locked methodology +
  locked secondary prompt only — no primary coding. Freeze Pass 1 outputs
  before running Pass 2 (cross-review).
- After methodology lock: **do not modify the codebook or prompts** until
  all three cases have completed primary and secondary coding. No
  case-specific recalibration.

## 7. Human gates

- Cross-review disagreements are never silently adjudicated by an agent —
  they go to `CROSS_REVIEW.csv` with status AGREE/REVISE/REJECT/ADD_MISSING/QUESTION.
- Human review workbook fields (`final_human_decision`, `final_human_role`,
  `final_human_mechanism`, `final_human_notes`) are created blank and must
  never be pre-filled by an agent.
- `final/` is created **only** after explicit researcher instruction.
