# Terra execution provenance note

Scope: the two Terra-labelled codings used in the four-way pre-RA comparison, with provenance claims limited to preserved project artifacts and the researcher's supplied labels. This note does not alter methodology v1.1.0.

## Machine-recorded information

The current Terra context manifests identify the executions internally as `R1` and `R2`; they do not contain provider, exact model, reasoning effort, timestamps, duration, or technical isolation metadata.

| item | Terra-R1 | Terra-R2 |
|---|---|---|
| context manifest | `../R1_context_manifest.yaml` | `../R2_context_manifest.yaml` |
| status | `completed_validated` | `completed_validated` |
| execution-context label | `independent_context_R1` | `independent_context_R2` |
| input packet | `R1_coding_input.json` | `R2_coding_input.json` |
| input SHA-256 | `813b984c5e80aa03c98bc4399f40644c7d802eedd45f55a2d7a9a787a82d0b38` | `813b984c5e80aa03c98bc4399f40644c7d802eedd45f55a2d7a9a787a82d0b38` |
| raw SHA-256 | `af443a0f98307a9d989816c5f0e15d4aa009553174eb470753f4134cb6640f29` | `18855b2053447d061be3c1fcfae9ebdbd579620d922a6394223f57b0f21ad2f6` |
| validated SHA-256 | `af443a0f98307a9d989816c5f0e15d4aa009553174eb470753f4134cb6640f29` | `18855b2053447d061be3c1fcfae9ebdbd579620d922a6394223f57b0f21ad2f6` |
| validation status | pass | pass |
| raw preserved before validation | true | true |
| post-hoc substantive corrections | none recorded | none recorded |

The equality of each Terra raw/validated hash proves byte identity for that pair. It does not independently prove unrecorded execution configuration or isolation properties.

## Researcher-supplied information

The labels `Terra-R1` and `Terra-R2` are supplied by the researcher in the instruction for this preparation. No separate preserved artifact examined for this note states an exact Terra model ID or effort setting.

**Exact execution model/effort is not machine-recorded in the Terra execution artifacts.**

No `researcher_observed` assertion of “GPT-5.6 Terra Extra High” is recorded here because the supplied instruction makes that statement conditional on documentary evidence; it does not itself assert that configuration as an observed fact.

## Configuration that cannot be proved from the Terra artifacts

- exact provider and model ID;
- reasoning/effort setting;
- execution timestamps and duration;
- context-window configuration;
- technical isolation mechanism or isolation guarantee.

The context labels and forbidden-input lists are machine-recorded protocol declarations. They are not treated as telemetry proving every access event.

## Cross-family provenance context

The Claude manifests explicitly record provider `Anthropic`, model ID `claude-sonnet-5`, default/no explicit effort override, UTC execution timestamps, and fresh-context declarations. These are claims preserved in `../claude_replication_01/Claude_R1_context_manifest.yaml`, `Claude_R2_context_manifest.yaml`, and `CLAUDE_REPLICATION_MANIFEST.yaml`; this preparation does not independently reproduce or causally verify them.

The Claude validation logs record post-hoc validation corrections while preserving raw files:

- Claude-R1: two records had `I` populated to match an existing `C=YES` judgment; one of those also changed `screening_status` from `direct_relationship` to `candidate`. A–E and `relational_result` were unchanged. Raw and validated hashes differ.
- Claude-R2: one record had `I` populated to match an existing `C=YES` judgment. A–E, `relational_result`, and `screening_status` were unchanged. Raw and validated hashes differ.

These provenance differences constrain interpretation: Terra × Claude divergences cannot be treated as a pure causal effect of model architecture.
