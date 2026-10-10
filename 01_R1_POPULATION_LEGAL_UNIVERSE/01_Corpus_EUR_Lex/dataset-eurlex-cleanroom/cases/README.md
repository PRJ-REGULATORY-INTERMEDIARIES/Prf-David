# cases/

Fixed, closed set of three cases — see `../config/case_registry.yaml`.
Do not add, remove, or rename cases.

Each `case_0N/` contains:

| folder | contents | status |
|---|---|---|
| `source/` | `act_official.xhtml` + `source_manifest.yaml` | populated |
| `corpus/` | `act_full.md`, `act_operative.md`, `act_recitals.md`, `corpus_manifest.yaml` | populated, hash-locked |
| `primary/` | context-isolated primary reader outputs (`PRIMARY_RELATIONS.csv/json`, `PRIMARY_ACTOR_MAP.csv`, `PRIMARY_BOUNDARY_CASES.csv`, `RUN_METADATA.yaml`) | empty — awaiting methodology lock |
| `secondary/` | blind secondary review (Pass 1) + cross-review (Pass 2) outputs | empty — awaiting primary coding |
| `human/` | human adjudication workbook + decisions | empty — awaiting cross-review |

`corpus/act_operative.md` is the primary coding corpus. `corpus/act_recitals.md`
is contextual only — see `../AGENTS.md` §5.
