# Simplified Production Methodology — Working Draft

**Project:** `dataset-eurlex`  
**Version:** production v1.0  
**Status:** preparation only; empirical coding has not started

## 1. Research workflow

Candidate regulatory relationships are identified by a specialised LLM using a predefined relational codebook. A second model reviews the proposed codings for omissions and conceptual errors. The researcher adjudicates the resulting matrix and produces the final dataset. All coding decisions remain traceable to the original legal text.

The production workflow is:

```text
OFFICIAL EU ACT
       ↓
FROZEN CORPUS
       ↓
CLAUDE PRIMARY CODING
       ↓
STRUCTURED R-I-T MATRIX
       ↓
LUNA SECONDARY REVIEW
       ↓
RESEARCHER ADJUDICATION
       ↓
FINAL CASE DATASET
```

After three cases, the researcher may consolidate the three researcher-adjudicated case datasets into one consolidated dataset:

```text
CASE 01   CASE 02   CASE 03
       \     |     /
        CONSOLIDATED DATASET
```

## 2. Unit of analysis and cases

A case is one EU legislative act and one frozen legal corpus. The production design contains three cases. Case 01 is the European Climate Law, Regulation (EU) 2021/1119, CELEX `32021R1119`, which is already represented by a locked source and corpus in the repository. Case 02 is Regulation (EU) 2023/956, CELEX `32023R0956`, and Case 03 is Regulation (EU) 2023/1115, CELEX `32023R1115`; both were selected prospectively under `docs/methodology/CASE_SELECTION_MATRIX.md`. No case is selected because it is expected to contain intermediaries or positive relations.

Selection criteria are recorded in `CASE_SELECTION_PROTOCOL.md` before production coding. The case registry records the official source, source hash, corpus hash, and status.

## 3. Relational codebook

The core construct is regulatory intermediation as a relation:

```text
R = Regulator
I = Intermediary
T = Target
```

R, I, and T are relational roles, not fixed actor attributes. An intermediated relation requires R, a regulatory relationship to I, a demonstrated mediating regulatory function, and T. The mere appearance of a third actor is insufficient.

The coding distinguishes:

- `keyword hit ≠ regulatory relationship`;
- `actor mention ≠ intermediary`;
- information, advice, or assistance does not automatically constitute intermediation; and
- `object ≠ target`.

Activities, information, products, processes, conduct, and compliance states belong in `object`, while T is an actor, class of actors, or institutional role subject to the regulatory relationship.

The primary source is the complete text of the act, including its internal structure, parent clauses, and cross-references reproduced in the frozen corpus. External legislation, doctrine, institutional knowledge, and previous results are not imported silently. Where external context is indispensable, the record sets `external_context_required: true` and explains the limitation.

## 4. Primary coding

Claude reads the complete case corpus and produces a proposed matrix. One consolidated prompt combines task framing, the methodological codebook, R–I–T decision rules, substantive regulatory guidance, and relevant EU/climate guidance. G0, G1, and G2 are not separate production executions.

Each proposed relation records arrays for R, I, and T, evidence, action, object, mediating function, mechanism, relation type, confidence, and coder notes. Relation types are `intermediated`, `direct`, `uncertain`, and `not_supported`. Borderline cases, rejected possible intermediaries, incomplete structures, external-context limitations, and passages requiring attention are recorded in an uncertainty log.

The raw Claude response is preserved before parsing. Parsed `primary_coding.csv`, `primary_coding.json`, and `uncertainty_log.csv` are proposals and are never treated as final data.

## 5. Secondary review

Luna receives the same frozen corpus, the codebook, and the Claude output. It checks omissions, over-coding, target/object confusion, actor-role errors, unsupported mediating functions, mechanism errors, and evidentiary limitations. It classifies each proposal as `ACCEPT`, `REVISE`, `QUESTION`, or `ADD_MISSING_RELATION` and explains the review with evidence.

Luna does not silently alter `primary_coding`. It does not see researcher decisions before completing its review, and it is not treated as ground truth. Its separate `secondary_review.csv` is an auditable review layer.

## 6. Researcher adjudication and final data

The researcher reviews the Claude proposal, Luna review, and canonical evidence in `researcher_review_matrix.csv`. The researcher alone assigns `APPROVE`, `CHANGE`, `EXCLUDE`, or `UNRESOLVED`, and records final R, I, T, and relation type where applicable.

Only after human adjudication may the workflow create `final_case_dataset.csv` and `final_case_dataset.json`. The final dataset represents researcher adjudication informed by LLM-assisted coding. It is not a copy of Claude or Luna output.

## 7. Audit trail and states

For each case and execution, preserve the official source, frozen corpus, hashes, codebook, prompt, model metadata, observable reasoning effort, raw output, secondary review, researcher decisions, and final dataset. The workflow uses only these states:

```text
selected → source_locked → corpus_locked → primary_coded
→ secondary_reviewed → human_reviewed → finalized
```

The exact primary model and reasoning telemetry remain null until observed and recorded. No unobserved metadata is invented.

## 8. Relationship to the pilot

The four-way pilot is mentioned only as an initial methodological calibration exercise used to refine the coding protocol. Its Terra/Claude replications, reference work, comparison, and human-gate artifacts remain intact and auditable. The new production design is a prospective simplification, not a retroactive reinterpretation of pilot results.
