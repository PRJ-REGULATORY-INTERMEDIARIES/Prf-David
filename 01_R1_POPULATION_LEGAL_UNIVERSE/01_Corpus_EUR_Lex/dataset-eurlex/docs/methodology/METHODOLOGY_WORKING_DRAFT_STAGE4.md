# Methodology working draft — Stage 4 and pre-experiment preparation

**Project:** `dataset-eurlex`  
**Status:** provisional working draft; not the final report  
**Scope:** preparation of the adjudicated reference benchmark and the experimental interface for G0/G1/G2

## 1. Study design

This project is an exploratory single-case methodological pilot. It examines how progressive instruction changes an LLM's ability to identify and code regulatory acts or provisions in one normative act from EUR-Lex. The design supports descriptive comparison only; it does not support statistical inference or generalization to the wider regulatory universe.

The study uses one normalized and locked corpus, three experimental conditions, and one independent execution per condition. The same document, model, reasoning setting, output interface, and execution protocol must be used across conditions. The substantive manipulation is the level of instruction supplied to the model.

## 2. Unit of analysis and corpus

The unit of analysis is a candidate regulatory relationship anchored in the smallest legally sufficient provision. The canonical experimental text is `02_corpus/act.md`, whose integrity is recorded in the corpus manifest and in the methodology manifest.

The corpus text is the evidential authority. External legal sources, institutional expectations, prior codings, and empirical outputs are not substitutes for evidence in the supplied text.

## 3. Reference benchmark

The reference is a **researcher-adjudicated reference benchmark**, not a human gold standard. Its planned construction consists of lexical screening, structural reading, candidate-universe reconstruction, independent R1 and R2 coding, comparison, external RA of divergent cases, a minimal researcher review gate, and reference lock.

The candidate universe preserves channel provenance for reference auditability (`lexical`, `structural`, or `both`). That provenance belongs to reference construction and must not be exposed to G0, G1, or G2. The future experimental interface therefore uses run-local `relation_id` values and post-hoc matching; it does not pass reference candidate IDs or origins into an experimental condition.

## 4. R–I–T coding

The focal construct is a relationship:

```text
R — I — T
```

- `R` is the regulator or institutional role exercising the focal regulatory function;
- `I` is a distinct third actor or institutional role performing a mediating function;
- `T` is the actor, class of actors, or institutional role subject to the relationship.

Activities, information, products, processes, conduct, and states of compliance are objects of action, not values of `T`. The reference coding distinguishes action, object, mediating function, instrument, procedure, mechanism, evidence, confidence, and the adjudicated relational result.

## 5. Experimental conditions

The three conditions are nested in instruction:

| Condition | Shared inputs | Additional instruction |
|---|---|---|
| G0 | act, task, minimal output structure | none beyond the minimal task |
| G1 | G0 inputs | methodological and codebook guidance |
| G2 | G1 inputs | substantive climate/regulatory guidance |

No condition receives the benchmark, reference candidate origin, R1/R2/RA output, human judgments, or another condition's response. Contexts must remain independent and raw responses must be preserved before parsing.

## 6. Planned comparison

After reference lock and completion of the three runs, comparison may calculate TP, FP, FN, precision, recall, F1, relational-result agreement, R/I/T agreement, and mechanism agreement. Matching will use normalized structural location because the experimental interface does not expose reference candidate IDs; explicit candidate IDs may be used only in a legitimate post-hoc comparison artifact. Only when necessary may transparent evidence overlap or semantic review be used. No uncertain match is to be forced.

These quantities will be interpreted descriptively because the design contains one act and one run per condition.

## 7. Provisional status and future updates

This draft documents protocol decisions available before the future RA, human gate, benchmark lock, and experimental runs. It must be updated after those events, with changes tied to dated manifests and hashes. It must not be used to backfill results or justify a decision using future G0/G1/G2 outcomes.

- `[TO BE UPDATED AFTER RA]`
- `[TO BE UPDATED AFTER HUMAN GATE]`
- `[TO BE UPDATED AFTER G0/G1/G2]`
