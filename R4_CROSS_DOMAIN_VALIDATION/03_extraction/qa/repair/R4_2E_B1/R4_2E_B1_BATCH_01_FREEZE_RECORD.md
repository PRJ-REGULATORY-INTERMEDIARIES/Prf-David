# R4.2E-B1 Batch 01 freeze record

**Freeze ID:** `R4_2E_B1_BATCH_01_FREEZE_001`  
**Frozen status:** `R4_2E_B1_BATCH_01_FROZEN_READY_FOR_CLAUDE_HANDOFF`  
**Completed scope:** 36 of 143 B1 records: 25 family representatives, 8 individual advanced cases and 3 hidden NO_REPAIR controls.

## Provenance

- `REQUESTED_MODEL = GPT-5.6 Terra High`
- `RESEARCHER_SELECTED_MODEL = GPT-5.6 Terra High`
- `MODEL_RUNTIME_VARIANT = MODEL_VARIANT_NOT_EXPOSED`

No Claude execution has occurred. Batches B1-02 (36), B1-03 (36) and B1-04 (35) remain pending: 107 records total.

## Authoritative B1-01 output and schema incident

The first B1-01 export is preserved as historical provenance only:

- `B1_01_V1 = SCHEMA_DEFECTIVE_PRESERVED`
- file: `R4_2E_B1_ADVANCED_VALIDATION_B1_01_v1_SCHEMA_DEFECT.csv`
- SHA-256: `5CD40A975BCF642DE4941BA8F7FC28877BFB6BC4F2309CFC0EA9C94AEA66F4E0`

Its schema defect was a delimiter-induced field displacement in some notes. The substantive decisions were not changed. The authoritative output is:

- `RUN_VERSION = v2_SCHEMA_CORRECTED`
- file: `R4_2E_B1_ADVANCED_VALIDATION.csv`
- SHA-256: `1D03CD4514CF08D80963985470DDF4B509AA30049C69F2C58C302FC03415D4EC`

The B1 batch manifest SHA-256 is `4B559AAC1147F84049E0C23DD1DAC6089B051AEB44CCA616C3AFBB9CE0312D62`.

## Frozen results

- `ADVANCED_DEFECT_PRESENT`: YES = 25; PARTIALLY = 6; NO = 5.
- Proposition anchor: HIGH = 30; MEDIUM = 5; LOW = 1.
- Proposed field corrections: Actor = 11; Action = 25; Object = 20; Counterpart = 24; Recipient = 26.
- Family template status: VALIDATED_WITH_CONDITIONS = 14; REQUIRES_MORE_REPRESENTATIVES = 5; HUMAN_REVIEW_REQUIRED = 3; REJECTED = 3.
- Individual routes: MODEL_REPAIR_PROPOSAL_ACCEPTABLE_FOR_HUMAN_QA = 2; HUMAN_ADJUDICATION_REQUIRED = 6.
- Relational differentiation: NEITHER = 24; RECIPIENT_ONLY = 7; COUNTERPART_ONLY = 3; UNCERTAIN = 2.

The relational results are preliminary advanced-validation evidence that the theoretically distinct fields may have been collapsed by the initial extraction. They suspend any field-merger inference; they do not establish a final corpus-wide conclusion.

## Controls and gate

The three controls were unblinded only after B1-01 decisions were frozen: CLEAN_CONFIRMED = 2; DEFECT_FOUND = 1 (`EXT-000085`). The control-result file SHA-256 is `B4040C50186CD65F9A59498DD0C3024B2B98EE9B19B327E25C9BFB3BB825F28F`.

Nine hidden controls remain. No `B0_COMPRESSION_SAFETY` conclusion is authorized yet, and B0 is not reopened.

## Firewalls

- `RIT_CODING = NOT_STARTED`
- `MECHANISM_CODING = NOT_STARTED`
- `ROTEM_CODING_CONSULTED = NO`
- `R4_3 = NOT_STARTED`
- `CORPUS_WIDE_REPAIR = NOT_EXECUTED`

No corpus repair, R/I/T coding, mechanism coding or Rotem consultation occurred. Claude may continue only the frozen pending batches and must preserve separate model provenance.
