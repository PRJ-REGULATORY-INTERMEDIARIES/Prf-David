# Pre-experiment readiness audit — G0/G1/G2

**Date:** 2026-09-07  
**Scope:** infrastructure and protocol validation only  
**Empirical status:** RA is external/pending; human gate, benchmark lock, G0, G1 and G2 have not been executed

## 1. Files reviewed

- `methodology/v1.1.0/experimental_output_schema.json`
- `methodology/v1.1.1/experimental_output_schema.json` (historical correction)
- `methodology/v1.1.2/experimental_output_schema.json`
- `methodology/v1.1.0/reference_coding_schema.json`
- `methodology/v1.1.0/codebook.md`
- `methodology/v1.1.0/methodology_manifest.yaml`
- `04_prompts/G0.md`, `04_prompts/G1.md`, `04_prompts/G2.md`
- `04_prompts/README.md`
- `config/project.yaml`
- `config/experiment.yaml`
- `docs/RESEARCH_DESIGN.md`
- `prompts/ETAPA_06_G0_G1_G2.md` and `prompts/ETAPA_07_COMPARACAO.md`

The existing G0/G1/G2 files are placeholders and contain no empirical content. No output from Terra, Claude, R1, R2, or RA was modified or used as experimental input.

## 2. Information held constant

The protocol requires the following to be identical across G0, G1 and G2:

| Item | Requirement | Current readiness |
|---|---|---|
| Act | the same normative act | defined; canonical corpus exists |
| Corpus | the same `02_corpus/act.md` | locked and hash-recorded |
| Model | the same model | not configured yet (`null`) |
| Reasoning effort | the same level | not configured yet (`null`) |
| Output format | the same experimental interface | v1.1.2 proposed; v1.1.1 retained historically |
| Session | independent context per condition | required by design; not yet executed |
| Benchmark visibility | inaccessible to all conditions | required; benchmark not locked and no prompt contains it |

Model and reasoning remain unresolved in `config/experiment.yaml`; the future execution phase must not select them silently.

## 3. Experimental manipulation

The intended manipulation is exactly:

- **G0:** task + corpus + minimal output structure;
- **G1:** G0 + methodological/codebook guidance;
- **G2:** G1 + substantive climate/regulatory guidance.

The following shared controls must not differ across conditions: act, corpus text, model, reasoning effort, output schema, output serialization rules, run count, matching rules, benchmark access, prior-condition outputs, human judgments, and hidden state or memory. Reference-construction artifacts are not condition inputs.

**No reference candidate list, candidate IDs, candidate origins, or preselected benchmark locations will be supplied to G0, G1 or G2. Each condition receives the same complete frozen corpus and independently identifies and codes supported relationships.**

The G0/G1/G2 prompt files are still undefined, so prompt-level symmetry is pending the authorized execution stage. This audit records the rule; it does not define or execute those prompts.

## 4. Leakage audit

### 4.1 `candidate_origin`

The locked v1.1.0 experimental schema requires `candidate_origin` and restricts it to `lexical`, `structural`, and `both`. Those values are generated during reference candidate-universe construction. Supplying them to an experimental agent would reveal whether a candidate originated in the lexical screen, the structural reading, or both, and would therefore expose Stage 3/4 construction information that G0 must not receive.

This is a confirmed leakage issue, not merely a documentation concern. The field is not present in the future experimental input requirements and is not needed for a run-local response.

### 4.2 Other schema observations

- `relation_id` is suitable as an output-local identifier; it must not be pre-populated from reference candidate IDs.
- `location` and `evidence` are needed for later transparent matching and do not, by themselves, reveal the candidate-universe channel.
- `R`, `I`, `T`, action, object, mediating function, mechanism, decision, confidence, and notes are comparable output fields, subject to normalization and observability limits.
- The reference-only five-condition test, actor sub-roles, observability classes, and secondary dimensions are not in the experimental schema and must remain reference-only.

## 5. Decision on experimental v1.1.2

`methodology/v1.1.1/` remains preserved as the historical pre-experiment correction that removed `candidate_origin` from the experimental schema. The new `methodology/v1.1.2/` is the prospective **experimental-only protocol correction** used for future interface validation. It changes only R/I/T representation from scalar string/null fields to arrays of actor-label strings, allowing zero, one, or multiple actors, while retaining the v1.1.1 leakage correction. It does not alter:

- `methodology/v1.1.0/codebook.md`;
- `methodology/v1.1.0/reference_coding_schema.json`;
- the candidate universe;
- benchmark construction;
- any Terra/Claude/R1/R2/RA output.

The correction is justified solely by pre-experiment interface and output-symmetry analysis. It is not based on G0/G1/G2 results, which do not yet exist. The future prompt manifest must record v1.1.2 as the common output interface for all three conditions before execution.

## 6. Readiness status

Infrastructure is ready for the later protocol transition, but the experiment is not executable now. The following remain deliberate gates:

- reference lock is false;
- the human gate has not been executed;
- model and reasoning are null;
- G0/G1/G2 prompt files are not defined;
- G0/G1/G2 have not been executed.

The prospective matching rules are recorded in `docs/protocol/EXPERIMENTAL_REFERENCE_MATCHING_PROTOCOL.md` and apply only after runs exist; they do not supply candidate locations to any condition.

All future comparison scripts abort with `REFERENCE_NOT_LOCKED` until the state is changed through the authorized reference-lock workflow.
