# Methodology

## Working draft — current through Stage 4 (pre-adjudication)

**Project:** `dataset-eurlex`  
**Empirical case:** Regulation (EU) 2021/1119 — European Climate Law (CELEX 32021R1119)  
**Current methodological version:** v1.1.0  
**Status of this chapter:** provisional working text. It describes the design and procedures implemented up to the completion of the four-way pre-adjudication comparison. The final version will be updated after reference adjudication, researcher review, benchmark lock, and the G0/G1/G2 experimental runs.

---

## 1. Research purpose and overall design

This pilot investigates whether large language models can be used to identify and code regulatory relationships in European Union legislation in a way that is transparent, auditable, and reproducible. The substantive focus is regulatory intermediation, operationalised through a relational **Regulator–Intermediary–Target (R–I–T)** architecture.

The pilot is deliberately narrow. It uses **one EU legislative act**, applies a source-bounded coding protocol to that act, constructs a researcher-adjudicated reference benchmark, and will subsequently compare three experimental prompt conditions:

- **G0 — General:** minimal task framing;
- **G1 — Methodological:** G0 plus the operational codebook, inclusion/exclusion criteria, decision rules, and schema;
- **G2 — Methodological + substantive:** G1 plus domain-specific guidance on regulation, climate governance, and relevant EU regulatory context.

The intended experimental design is therefore:

```text
1 legislative act
        ×
3 prompt conditions
        ×
1 independent run per condition
        =
3 experimental runs
```

This is a **single-case methodological pilot**, not a performance benchmark intended to estimate the general capability of LLMs across EU law. The purpose is to test the feasibility of a reproducible workflow, observe how different levels of methodological scaffolding affect coding behaviour, identify failure modes, and determine whether the approach is worth scaling to a larger legislative population.

The main experimental question is:

> **How do progressively stronger levels of methodological and substantive guidance affect an LLM's ability to identify and code regulatory relationships in a European legislative act?**

The analysis will consider both potential gains and potential adverse effects, including improved recall, improved precision, fewer omissions, more accurate actor-role reconstruction, and possible over-coding caused by excessive substantive guidance.

---

## 2. Conceptual foundation: regulation as a relational structure

The project follows a regulatory-governance perspective in which regulation is not reduced to the actions of formally designated regulatory agencies. Instead, the analytic problem is to reconstruct **who performs a regulatory function, in relation to whom, through what mechanism, and on the basis of what legal evidence**.

The focal construct is:

```text
Regulator (R) → Intermediary (I) → Target (T)
```

The three positions are **relational rather than intrinsic actor attributes**. The same organisation may be a regulator in one relationship, an intermediary in another, and a target in a third. Accordingly, the unit of analysis is not an organisation or a pre-classified actor list. It is a **candidate regulatory relationship anchored in a specific legal provision**.

A coded relationship should, when the text permits, identify:

- the regulator (`R`);
- the intermediary (`I`);
- the target (`T`);
- the relevant regulatory action;
- the object of regulation;
- the mediating function;
- the regulatory mechanism;
- the instrument or procedure involved;
- the precise legal location; and
- the textual evidence supporting the coding decision.

This distinction is central because many institutions appearing in legislation are not intermediaries in the relevant relational sense. A body may provide advice, information, coordination, expertise, or administrative assistance without necessarily mediating a regulatory relationship between a regulator and a target.

---

## 3. Source-bounded evidence rule

A central design decision is that the coding is **source-bounded**.

The supplied legislative text is the evidentiary authority for the exercise. Coders are not allowed to complete missing elements by relying on external legislation, institutional knowledge, administrative practice, doctrine, case law, or assumptions about how an EU regime normally operates.

The intended logic is:

```text
LEGAL EVIDENCE
      ↓
INSTITUTIONAL INTERPRETATION
      ↓
CODING
```

Internal context from the same act may be used when necessary. This includes parent clauses, paragraphs, points, and cross-references to other provisions reproduced within the canonical corpus. External cross-references may be recorded, but their absent content may not be imported.

This rule is especially important for R–I–T reconstruction because a model may otherwise infer a plausible target or intermediary from general institutional knowledge rather than from the supplied legislative evidence.

---

## 4. Case selection and source acquisition

The pilot uses **Regulation (EU) 2021/1119 of 30 June 2021**, the European Climate Law, identified by CELEX `32021R1119`.

The act was selected as the single case for the methodological pilot. Importantly, selection was **not conditioned on prior knowledge that the act contained regulatory intermediaries**, nor on the presence of specific lexical markers associated with intermediation. This avoids defining the empirical universe by the dependent construct.

The official act was acquired from EUR-Lex and preserved as the source artifact:

```text
01_source/act_official.xhtml
```

The preserved source file has SHA-256:

```text
8BBE15AF032AF1A3950CF1E42BEAD62E0C816AFBF56DCED883ECECB604DA6075
```

EUR-Lex/CELEX was used because it provides a stable legal identifier, official text, provenance, and a path toward future scalable collection through EU data infrastructure.

---

## 5. Corpus normalisation and lock

The official XHTML was normalised into a canonical analytical corpus:

```text
02_corpus/act.md
```

A numbered representation was also created for audit and location control:

```text
02_corpus/act_numbered.md
```

Normalisation was structural only. No translation, summarisation, paraphrase, relevance filtering, actor coding, keyword annotation, or substantive interpretation was introduced into the canonical text.

The resulting corpus preserves:

- the title and preamble;
- 40 recitals;
- Articles 1–14;
- paragraphs, points, and subparagraphs;
- amendment text inserted by the Regulation; and
- the original order of the official source.

The act contains no annexes of its own.

The canonical corpus contains approximately 9,803 words and 64,928 bytes. Its SHA-256 is:

```text
B24A02EA241CA631B606660BB48BB5A2222B29F849C4E4552FB99F871B2E8FD4
```

The numbered version has SHA-256:

```text
0EB336AEA6C8FF19AF3B6536F3E9029A2E9AF68CA763E962429A8A3DACBB49ED
```

Once validated, the corpus was locked. Subsequent methodology, reference construction, and experimental runs are required to use this same frozen text.

---

## 6. Isolation from previous empirical work

The pilot was implemented in a new project directory:

```text
Prf-David/dataset-eurlex
```

The isolation is methodological rather than merely organisational.

Earlier project materials may inform generic concepts, literature, codebook design, strings, and methodological decisions, but they may not supply empirical answers for the current case. In particular, the new experiment must not inherit:

- previously classified candidate IDs;
- prior R–I–T decisions;
- old LLM outputs;
- previous datasets;
- prior case-level benchmark labels; or
- earlier adjudications of the same legal provisions.

This separation is intended to prevent contamination of the new reference benchmark and experimental conditions.

---

## 7. Operational codebook and methodology freeze

The methodology was formalised and versioned before substantive reference coding.

An initial v1.0.0 was preserved, after which an external methodological review identified several conceptual and implementation issues. A revised **v1.1.0** was then created and locked before the successful Stage 4 coding attempt.

The v1.1.0 methodological package contains, among other artifacts:

```text
methodology/v1.1.0/codebook.md
methodology/v1.1.0/strings.yaml
methodology/v1.1.0/reference_coding_schema.json
methodology/v1.1.0/experimental_output_schema.json
methodology/v1.1.0/methodology_manifest.yaml
```

Key revisions introduced in v1.1.0 included:

1. **Target restriction.** `T` was restricted to an actor, actor class, or institutional role subject to the focal regulatory relationship. Activities, information, products, processes, conduct, and states of compliance are coded as `object`, not as `T`.

2. **Separate reference and experimental schemas.** The reference workflow (independent coders, adjudication, and benchmark) uses a richer reference schema, while G0/G1/G2 use a common experimental output schema.

3. **Expanded mechanism taxonomy.** Mechanisms include reporting, verification, certification, auditing, monitoring/supervision, ranking/rating, standard-setting, enforcement support, coordination, information transmission, delegated implementation, accreditation, other mechanism, and none/direct.

4. **Lexical and structural candidate channels.** A legal unit can enter the candidate universe through lexical screening, structural reading, or both. Structural inclusion does not require a keyword hit.

5. **No act-specific tuning.** The methodology manifest records that the selected act's empirical content was not used to tune the codebook, and no benchmark or empirical result was used in the revision.

The main reference schema is:

```text
methodology/v1.1.0/reference_coding_schema.json
```

Its role is to keep R1, R2, adjudication, and the eventual reference benchmark structurally comparable.

---

## 8. Five-condition relational test

Each candidate is evaluated through five explicit conditions:

### Condition A — Regulator

Is there an identifiable regulator or regulatory authority in the focal relationship?

### Condition B — Target

Is there an identifiable actor or institutional role that is subject to the focal regulatory relationship?

### Condition C — Distinct third actor

Is there a third actor analytically distinct from R and T?

### Condition D — Mediating regulatory function

Does that third actor perform a regulatory function that mediates the relationship between R and T?

### Condition E — Evidence

Is there sufficient legal evidence in the supplied corpus to support the proposed reconstruction?

Each condition is coded as:

```text
YES
NO
UNCLEAR
```

The final relational result is constrained by these conditions:

- `positive` requires A–E all equal to `YES`;
- `negative` applies when a necessary structural condition is `NO`, including direct R–T relations with no intermediary;
- `conditional` applies when a materially relevant condition remains `UNCLEAR`;
- `insufficient_evidence` applies when the text does not support responsible adjudication.

Abstention is therefore a valid methodological outcome. The workflow is explicitly designed to avoid forcing ambiguous cases into a positive R–I–T structure.

---

## 9. Candidate generation: lexical screening plus structural reading

Candidate generation is deliberately separated from substantive coding.

### 9.1 Lexical channel

Strings, regex patterns, and linguistic markers are used to locate potentially relevant passages and improve recall. These may include terms associated with obligations, reporting, monitoring, verification, certification, auditing, supervision, delegation, coordination, and enforcement.

However:

> **a lexical hit is not a regulatory relationship.**

Strings are a screening device only.

### 9.2 Structural channel

A second channel examines the legal structure independently of keyword hits. This is necessary because regulatory relationships may be expressed through legal architecture that does not contain a preselected lexical marker.

The structural pass considers hierarchy and context, including:

- article;
- paragraph;
- point;
- parent clause;
- legally necessary surrounding text; and
- same-act cross-references when the required evidence remains within the canonical corpus.

Each candidate is therefore labelled by origin:

```text
lexical
structural
both
```

---

## 10. Methodological learning from the first Stage 4 attempt

The first implementation of Stage 4 generated a 106-candidate universe. It was not carried forward to the benchmark.

A methodological audit conducted before the human gate identified two serious problems.

First, the two nominally independent codings were not substantively independent enough. Their core R/I/T and related fields were effectively shared or reproduced, so differences were concentrated in peripheral fields rather than reflecting genuine independent reconstruction.

Second, candidate segmentation was too granular. Some chapeaux, points, and dependent clauses were treated as independent legal units even where a larger hierarchical context was required to reconstruct the relationship. This created a risk of **fragment blindness**: the model could miss an R–I–T relationship because the regulator, intermediary, and target were distributed across a paragraph and its subparts.

For these reasons, the first attempt was declared **superseded before researcher adjudication**. Its artifacts were preserved for audit, but its substantive coding was not used as ground truth and no R/I/T coding fields from it were reused.

This failure was treated as a methodological pretest rather than as part of the final empirical reference.

---

## 11. Reconstructed candidate universe

The candidate universe was rebuilt in `stage4_attempt_02` using:

- lexical screening;
- substantive structural reading;
- hierarchical parent context;
- same-act context references; and
- explicit transition auditing from the superseded candidate set.

The final reconstructed universe contains **90 candidate units**:

- 25 lexical;
- 21 structural;
- 44 identified by both channels.

The candidate reconstruction has SHA-256:

```text
38416B70F9337AD66DBD6C6D41D280D18AD9E5694E0CACB0C938C5833B1AFF55
```

Two byte-identical coding packets were generated for independent reference coding:

```text
R1_coding_input.json
R2_coding_input.json
```

Both have SHA-256:

```text
813B984C5E80AA03C98BC4399F40644C7D802EEDD45F55A2D7A9A787A82D0B38
```

No substantive R/I/T field was pre-populated in the candidate packets.

Strings were used only during screening and reconstruction and were prohibited from the substantive coding contexts.

---

## 12. Independent reference coding

The original reference design called for two independent coding passes, R1 and R2, over the same 90-candidate universe.

The isolation principle required:

- the same frozen candidate packet;
- the same corpus;
- the same codebook;
- the same reference schema;
- no access to the other coder's output;
- no access to previous Stage 4 attempts;
- no access to future experimental G0/G1/G2 outputs;
- no access to any benchmark; and
- preservation of raw output before validation.

The Terra-labelled R1 and R2 outputs were generated under separate protocol contexts and subsequently validated. Their repository artifacts record the independent-context labels and the protected input/output hashes. However, exact model and reasoning-effort telemetry for those two runs is not machine-recorded in the repository. For that reason, later Terra-versus-Claude differences are treated descriptively rather than as a controlled causal model comparison.

Raw and validated Terra outputs were preserved, and no post-hoc substantive correction was recorded for those two validated outputs.

---

## 13. Adaptive cross-model replication

After the Terra R1/R2 outputs were frozen, a second pair of independent codings was introduced as an **adaptive robustness check** before benchmark lock.

This was not part of the earliest pilot architecture and is therefore treated transparently as a methodological extension prompted by uncertainty observed during reference construction, not as an originally pre-registered comparison.

The cross-model replication used:

```text
Claude Sonnet 5
```

for two fresh, memoryless coding contexts:

```text
Claude-R1
Claude-R2
```

The two Claude agents received the same 90-candidate universe, corpus, v1.1.0 codebook, and reference schema. They were not permitted to access Terra outputs, each other's outputs, the superseded Stage 4 attempt, strings, any benchmark, or G0/G1/G2 results.

The execution logs record that Claude-R1 was closed before Claude-R2 was spawned. The two contexts therefore functioned as separate coding replications rather than sequential revisions.

Raw outputs were preserved before validation. Any structural corrections required by the validator were logged rather than silently replacing the original raw output.

At this stage the reference-construction evidence therefore consists of four independent coding replicas:

```text
Terra-R1
Terra-R2
Claude-R1
Claude-R2
```

These four replicas are not treated as four votes whose majority determines truth. They are competing reconstructions used to identify stable cases, disagreements, and candidates requiring adjudication.

---

## 14. Four-way comparison and normalisation

A dedicated pre-adjudication comparator was created after the four outputs were frozen:

```text
03_human/stage4_attempt_02/pre_ra_4way/cross_model_comparator_v1.py
```

The comparator is intentionally separate from the original reference validator. Its purpose is descriptive comparison, not adjudication.

A specific problem discovered during the cross-model review was that `actor.role` is free text in the schema. Literal equality of that field can therefore produce false disagreement when two coders identify the same actor in the same structural R/I/T position but describe the role differently.

The four-way comparator consequently normalises actor identity using:

- Unicode NFKC;
- case folding;
- trimming;
- whitespace collapse;
- trivial punctuation normalisation; and
- explicit, auditable aliases.

It does **not** use fuzzy matching or hidden semantic entity resolution.

The principal comparative signature uses:

- normalised R labels;
- normalised I labels;
- normalised T labels;
- Conditions A–E;
- relational result; and
- primary mechanism.

It does not use free-text `actor.role`, action, object, interpretive notes, evidence wording, or confidence as primary substantive equality criteria.

This comparison confirmed that all four outputs contain the same 90 candidate IDs and that the original artifacts and methodology remained unchanged.

At the current pre-adjudication snapshot, the empirical union of candidates coded as positive in at least one of the four replicas contains four candidates. The current human-review queue generated by rules 1–7 plus a reproducible random audit sample contains 21 candidates, of which eight are randomly selected stable negatives for quality control. These counts are procedural outputs of the reference-construction stage, not substantive findings of the final benchmark.

---

## 15. Known methodological limitations identified before adjudication

The replication process exposed several limitations that are now explicitly documented without modifying methodology v1.1.0.

### 15.1 Condition C and the overloaded `I` field

Conceptually:

```text
C = a distinct third actor exists
D = the third actor performs a mediating regulatory function
```

Therefore:

```text
C = YES
D = NO
```

is logically possible.

However, the current validator requires a populated `I` field whenever C=`YES`. In some records this means that `I` can structurally contain a third actor even when D=`NO` and the actor was not substantively judged to mediate the relationship.

For the current pilot, this is recorded as a known v1.1.0 limitation rather than corrected after seeing empirical outputs. Accordingly, `I != null` alone is not treated as proof of regulatory intermediation. Condition D and the final relational result are more informative.

### 15.2 Free-text role descriptions

`actor.role` is a free-text field. It is retained in source outputs but excluded from literal cross-model identity comparisons.

### 15.3 Negative-class prevalence

Most candidate units are negative in all codings. High raw agreement can therefore coexist with instability in the rare positive class. Pairwise agreement and Cohen's kappa are reported descriptively, but rare-positive overlap is also examined separately.

### 15.4 Cross-model asymmetry

The Terra and Claude workflows differ in provider, execution environment, documented reasoning settings, and correction history. The cross-model exercise is therefore a robustness analysis, not a controlled estimate of a pure model-family effect.

---

## 16. Planned blinded reference adjudication

At the time of this working draft, the four-way pre-adjudication preparation has been completed, but the final automatic adjudication has **not yet been executed**.

The planned next step is one complete adjudication over all 90 candidates using a fresh adjudicator context.

The four existing coding proposals will be anonymised through a random mapping:

```text
Coder A
Coder B
Coder C
Coder D
```

The adjudicator will not receive:

- provider identity;
- model identity;
- R1/R2 labels;
- information about which two coders belong to the same model family;
- model-specific notes;
- free-text fields likely to reveal stylistic provenance; or
- majority-by-family statistics.

The adjudicator will receive, for every candidate:

- candidate ID and legal location;
- focal excerpt;
- parent context;
- authorised same-act context;
- access to the canonical corpus when required;
- the locked v1.1.0 codebook and reference schema; and
- the four anonymised categorical proposals.

The decision rule is expressly **not majority voting**.

```text
3/4 ≠ truth
4/4 ≠ exemption from evidence review
1/4 ≠ automatic error
```

The adjudicator must reconstruct the relationship independently from the evidence and codebook and then explain why competing proposals were accepted or rejected.

For operational continuity, the researcher has chosen to perform this single adjudication stage in a new Claude context. Because two of the four source replicas were also produced by Claude, the identity-blinding procedure is particularly important. This design choice will be retained as a limitation in the final report rather than presented as model-neutral.

---

## 17. Researcher human gate and benchmark construction

The final reference will not be called a “human gold standard”, because the researcher will not independently recode the entire act.

The appropriate term is:

> **researcher-adjudicated reference benchmark**

The human role is deliberately limited but substantively authoritative.

After automatic adjudication, the researcher will review a targeted queue including, at minimum:

- any candidate coded `positive` by at least one replica;
- any `conditional` case;
- any `insufficient_evidence` case;
- any case with D=`YES` in at least one replica;
- divergences in relational result;
- substantive disagreements concerning intermediary identity;
- relevant R/I/T disagreements;
- low-confidence adjudications;
- adjudications that disagree with all replicas or the largest agreement grouping; and
- a reproducible random sample of otherwise stable negative cases.

The researcher will make one of three decisions:

```text
APPROVE_RA
CHANGE
UNRESOLVED
```

Only after this gate is completed will the benchmark be frozen.

This limited human intervention is retained because eliminating it entirely would leave the project vulnerable to the circularity of AI systems evaluating one another without an external substantive authority.

---

## 18. Experimental conditions G0, G1, and G2

Only after the reference benchmark is locked will the experimental model be run.

The three conditions must share:

- the same legal act;
- the same frozen textual version;
- the same base model;
- the same reasoning effort;
- the same output structure;
- independent sessions;
- no communication across conditions; and
- no access to the reference benchmark.

The experimental manipulation is the level of scaffolding.

### G0 — General

The model receives:

- the task;
- the corpus; and
- a minimal output structure.

It does not receive the full codebook, specialised screening strings, or additional substantive climate-regulation guidance.

### G1 — Methodological

The model receives:

- the task;
- the corpus;
- the codebook;
- inclusion/exclusion rules;
- decision criteria; and
- the experimental schema.

This condition isolates the effect of explicit methodological scaffolding.

### G2 — Methodological + substantive

The model receives everything in G1 plus domain-specific substantive guidance relevant to:

- regulatory governance;
- climate regulation;
- the EU institutional context; and
- interpretation of the relevant regulatory mechanisms.

G2 will not receive benchmark answers or case-specific adjudications.

The experimental output schema is common across the three conditions so that output comparability is not confounded with prompt condition.

---

## 19. Evaluation strategy

Once G0/G1/G2 are complete, each experimental output will be compared with the locked researcher-adjudicated reference benchmark.

Where meaningful, the analysis will report descriptive measures such as:

- true positives;
- false positives;
- false negatives;
- precision;
- recall;
- F1;
- agreement on relational result;
- agreement on actor-role reconstruction;
- mechanism agreement; and
- attribute-level agreement.

Because the design contains only one act and one run per experimental condition, no inferential claim will be made about population-level model performance.

Quantitative comparison will be complemented by a qualitative error taxonomy, including:

- omission;
- over-inclusion;
- boundary error;
- category error;
- regulator/intermediary/target actor error;
- target/object confusion;
- mechanism or instrument error;
- evidence error;
- hallucination; and
- unsupported inference.

Of particular interest is whether stronger scaffolding improves detection while also creating a risk of over-coding.

---

## 20. Reproducibility, auditability, and state control

The project was designed as a state-based workflow rather than a sequence of informal manual prompts.

The intended state progression is:

```text
setup
  ↓
source_acquired
  ↓
corpus_locked
  ↓
methodology_locked
  ↓
awaiting_reference_adjudication
  ↓
reference_locked
  ↓
runs_complete
  ↓
analyzed
  ↓
completed
```

Major artifacts are hashed with SHA-256. Raw outputs are preserved before validation. Where a validator requires a correction, the correction must be logged rather than silently replacing the original decision.

The pre-adjudication integrity check confirmed:

- the same 90 candidate IDs in all four coding outputs;
- unchanged protected hashes;
- no alteration of methodology v1.1.0;
- no alteration of the canonical corpus;
- no creation of a benchmark before adjudication; and
- no execution of G0/G1/G2 before reference lock.

This design allows later reconstruction of which artifact existed at each methodological stage and prevents later outputs from silently contaminating earlier ones.

---

## 21. Scope and limitations of the pilot

The pilot is intentionally constrained.

It contains:

- one legislative act;
- one substantive legal domain;
- one run per future experimental condition;
- an AI-assisted reference-construction process;
- an adaptive cross-model robustness extension introduced before benchmark lock;
- a limited rather than full independent human recoding;
- dependence on the chosen codebook and prompt formulations; and
- no claim of statistical generalisability.

The reference benchmark itself will be partly machine-constructed and researcher-adjudicated. It should therefore be understood as a transparent and auditable operational reference, not as an infallible ground truth.

The current design can establish whether this workflow is methodologically useful and whether the G0/G1/G2 manipulation generates interpretable differences. It cannot establish universal LLM performance in EU regulatory analysis.

If the pilot proves useful, future work can expand to:

- multiple legislative acts;
- a formally defined EU legislative sampling frame;
- multiple legal domains;
- replicated runs;
- model-family comparisons;
- inter-run stability;
- larger-scale human validation;
- automated EUR-Lex/SPARQL/Cellar collection; and
- more formal reliability and validity testing.

---

## 22. Current status of the methodology

At the time of this working draft:

```text
Official source acquisition              COMPLETE
Corpus normalisation and lock            COMPLETE
Methodology v1.1.0 freeze                COMPLETE
Candidate reconstruction                 COMPLETE
Final candidate universe = 90            COMPLETE
Terra-R1 / Terra-R2                      COMPLETE
Claude-R1 / Claude-R2                    COMPLETE
Four-way comparison                      COMPLETE
Pre-RA integrity validation              COMPLETE
Blind RA protocol                        COMPLETE
Automatic RA                             PENDING
Researcher human gate                    PENDING
Reference benchmark lock                 PENDING
G0/G1/G2 experimental runs               PENDING
Final comparison                         PENDING
Final report                             PENDING
```

This chapter will be updated once the pending steps are completed. The final methodology should preserve the chronology above, distinguish pre-specified design elements from adaptive refinements, and report all final model/runtime metadata that can be verified from execution artifacts.

---

## 23. Short methodological summary

In compact form, the workflow is:

```text
Official EUR-Lex source
        ↓
Frozen canonical corpus
        ↓
Locked R–I–T methodology
        ↓
Lexical screening + structural reading
        ↓
90-candidate reconstructed universe
        ↓
Four independent coding replicas
(Terra-R1, Terra-R2, Claude-R1, Claude-R2)
        ↓
Normalised four-way comparison
        ↓
Blind single-adjudicator RA
        ↓
Targeted researcher human gate
        ↓
Researcher-adjudicated reference benchmark
        ↓
G0 / G1 / G2 independent experimental runs
        ↓
Descriptive + qualitative comparison
        ↓
Final methodological report
```

The underlying principle throughout is that **regulatory intermediation is reconstructed as a legally evidenced relationship, not inferred from actor labels or keyword occurrence alone**.
