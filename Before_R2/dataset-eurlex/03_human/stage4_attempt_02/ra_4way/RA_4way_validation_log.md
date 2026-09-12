# RA 4-way adjudication — validation log

**Project:** `dataset-eurlex` · **Corpus:** Regulation (EU) 2021/1119 (CELEX 32021R1119)
**Methodology:** v1.1.0 · **Package:** `RA_blind_input.json` (90 frozen candidates, four anonymized proposals each)
**Role:** Reference Adjudicator (RA), blind 4-way

---

## 1. Preservation protocol

| Step | Artifact | State |
|---|---|---|
| 1 | `RA_4way_output_raw.json` | written first, complete and unvalidated; **not modified afterwards** |
| 2 | SHA-256 of raw | computed and recorded (§5) |
| 3 | `RA_4way_adjudication_notes.json` | written before the validator was opened |
| 4 | `validate_reference_logic.py` | opened **only after** steps 1–3; imported unmodified |
| 5 | `RA_4way_output.json` | validated copy, produced from the raw file by transformation, not by editing it |
| 6 | this log | — |

`validate_reference_logic.py` was not read, listed, grepped or executed before `RA_4way_output_raw.json`
existed on disk with the SHA-256 recorded in §5. The raw file's digest was re-verified after the validated
copy was produced and is unchanged.

The adjudication notes were regenerated once at step 5 so that the `screening_status` values quoted inside
their rationales match the delivered validated copy. Only the five records affected by the correction in §3
gained an explanatory sentence; no `relationship_to_coder_*` value and no substantive rationale was altered.
The digest in §5 is that of the regenerated file.

## 2. Validation method

Driver: `_ra_validate_driver.py` (throwaway, in this directory). It

1. loads the records file;
2. validates every record against `methodology/v1.1.0/reference_coding_schema.json` using **`jsonschema` 4.26.0**
   (importable, so the automatic path was used), *and* additionally runs an independent manual check of
   required keys, `additionalProperties: false`, every enum (`candidate_origin`, `screening_status`,
   `relational_result`, `primary_mechanism`, `secondary_mechanisms`, `confidence`, `evidence_role`,
   `observability`, `condition_result.result`), the six-key shape of `source_location`, the
   `label`/`role`/`evidence_refs` shape of every actor object, the `evidence_item` shape, and the types of all
   array fields;
3. imports `validate_relational_logic` from `../validate_reference_logic.py` **unmodified** and calls it on
   every record, logging each `ValueError` by `candidate_id`.

Two passes were run: one on the raw file, one on the validated copy.

**Pass 1 — `RA_4way_output_raw.json`** (sha `cb03a5dd…`)
`records=90 · schema_invalid=0 · logic_errors=5 · valid=85`

**Pass 2 — `RA_4way_output.json`** (sha `f2fac559…`)
`records=90 · schema_invalid=0 · logic_errors=0 · valid=90`

## 3. Corrections

Five records, and only five. All are one and the same correction, and all are classed
**structural-limitation**, not mechanical-formatting and not substantive.

### The conflict

`validate_relational_logic` enforces two rules that cannot both be satisfied by a record in which a distinct
third actor exists but does **not** mediate:

```
line 73-74:  screening_status == "direct_relationship"  ->  I must be null
line 75-76:  condition_C == "YES"                       ->  I must be non-null
```

`KNOWN_LIMITATIONS_V1_1.md` already documents the second rule (`I != null` is forced whenever `C=YES`, so a
non-null `I` "alone is not proof of intermediation"). The interaction with the first rule is the practical
consequence: v1.1.0 has no vocabulary for the case that is conceptually central to this adjudication — a third
actor that exists (C=YES) and does not mediate (D=NO), leaving the R–T relation running directly.

### What was changed

Only `screening_status`, from the value describing the substance (`direct_relationship`) to the neutral value
(`candidate`). **No condition result, no actor, no mechanism, no confidence and no `relational_result` was
touched**, and no condition was flipped to make an error disappear. Each corrected record carries, in `notes`,
both the standing `N_STRUCT` disclaimer (I is populated as a v1.1.0 technical requirement and the actors in it
were adjudicated non-mediating) and an explicit record of this correction.

| candidate_id | source_location | field | original value | rule violated | corrected value | class |
|---|---|---|---|---|---|---|
| `CAND2-AB84F16B6A72` | Recital 37 | `screening_status` | `direct_relationship` | "direct relationship cannot contain I" (l.73-74) vs "C=YES requires I" (l.75-76) | `candidate` | structural-limitation |
| `CAND2-465FC96778A7` | Art. 8(3)(b) | `screening_status` | `direct_relationship` | same | `candidate` | structural-limitation |
| `CAND2-8607C66ECE11` | Art. 8(3)(d) | `screening_status` | `direct_relationship` | same | `candidate` | structural-limitation |
| `CAND2-CBC911FFFEDF` | Art. 11, point (a) | `screening_status` | `direct_relationship` | same | `candidate` | structural-limitation |
| `CAND2-27E84BD23730` | Art. 13, point (b) | `screening_status` | `direct_relationship` | same | `candidate` | structural-limitation |

**Mechanical corrections: 0. Substantive corrections: 0.**

Recommendation for a future v1.1.x/v1.2.0 (outside this task): either allow `I` under `direct_relationship`
when `D=NO`, or stop forcing `I` from `C` and force it from `D` instead.

## 4. Summary statistics

**Candidates processed:** 90 of 90 (every candidate adjudicated, not only the contested ones)
**Records valid (schema + relational logic):** 90 / 90

### relational_result

| value | n |
|---|---|
| `negative` | 89 |
| `insufficient_evidence` | 1 |
| `conditional` | 0 |
| `positive` | 0 |

### confidence

| value | n |
|---|---|
| `high` | 59 |
| `medium` | 30 |
| `low` | 1 |
| `not_assessed` | 0 |

### key relational counts

| measure | n |
|---|---|
| `I != null` | 5 |
| `condition_C = YES` | 5 |
| `condition_D = YES` | 0 |
| `relational_result = positive` | 0 |

The five `I != null` records are exactly the five `condition_C = YES` records, and every one of them has
`condition_D = NO`. Per `KNOWN_LIMITATIONS_V1_1.md`, `I != null` here is a v1.1.0 artefact and is **not** a
finding of intermediation. The informative count is `condition_D = YES` and `positive`, both zero.

### screening_status (validated copy)

| value | n |
|---|---|
| `direct_relationship` | 34 |
| `candidate` | 32 |
| `not_candidate` | 23 |
| `insufficient_evidence` | 1 |

### other distributions

`candidate_origin`: `both` 44 · `lexical` 25 · `structural` 21
`regulatory_act_type`: `regulation_operative_provision` 46 · `recital` 27 · `regulation_amending_provision` 17
`is_regulatory_act = true`: 63
`primary_mechanism`: `none_or_direct` 31 · `monitoring_supervision` 19 · `standard_setting` 17 · `reporting` 11 ·
`coordination` 6 · `information_transmission` 3 · `enforcement_support` 2 · `verification` 1
Evidence items recorded: 142 · Records naming a specific absent external provision in
`additional_context_required`: 19

### the four provisions requiring explicit reasoning

| provision | candidate_id | relational_result | A/B/C/D/E | confidence |
|---|---|---|---|---|
| Article 3(4) — national climate advisory body | `CAND2-11BF388480EA` | `negative` | YES/YES/NO/NO/YES | medium |
| Article 8(3)(b) — reports of the EEA, Advisory Board, JRC | `CAND2-465FC96778A7` | `negative` | YES/YES/**YES**/NO/YES | medium |
| Article 8(4) — the EEA assisting the Commission | `CAND2-88A2261C68DE` | `negative` | YES/YES/NO/NO/YES | medium |
| Article 13, point (b) — Commission assisted by the Energy Union Committee | `CAND2-27E84BD23730` | `negative` | YES/YES/**YES**/NO/YES | medium |

Full reasoning for each (R, T, third actor, internal same-act context used, source-bounded limit, and why every
competing interpretation was rejected) is in `RA_4way_adjudication_notes.json` under
`rationale_for_adjudication`.

## 5. Digests

| file | SHA-256 |
|---|---|
| `RA_4way_output_raw.json` | `cb03a5dd907142defab7a03e2e817eccc2b019ed4e1412a99393dd8afa444893` |
| `RA_4way_output.json` | `f2fac559fd668b71b102e5197b20126a4008ab6437474d80982f7110e16c2fba` |
| `RA_4way_adjudication_notes.json` | `8cec91809e712c3aaae1d98a72f79a4bb65a8f303249d159683ac8f695094176` |

## 6. Blinding and source-boundedness

- No file under `ra_4way_private/` was opened, listed or referenced; no attempt was made to de-anonymize
  Coder A/B/C/D; no provider, model, family or replicate identity appears in any output.
- No `R1_*`/`R2_*` output, validation log or context manifest, nothing under `claude_replication_01/`,
  nothing under `stage4_attempt_01/`, `04_prompts/`, `05_runs/`, `06_comparison/`, `07_report/`, no
  `pre_ra_4way` comparison/comparator/provenance/manifest artifact, no `strings.yaml` and no older
  methodology version was opened.
- Authorized inputs actually read: `ra_4way/RA_blind_input.json`, `02_corpus/act.md`,
  `methodology/v1.1.0/codebook.md`, `methodology/v1.1.0/reference_coding_schema.json`,
  `pre_ra_4way/KNOWN_LIMITATIONS_V1_1.md`, and — only at step 4 — `validate_reference_logic.py`.
- Every literal cross-reference quote used as evidence beyond the package's own `focal_excerpt` was asserted
  at build time to be a verbatim substring of `02_corpus/act.md`.
- No text of Regulation (EU) 2018/1999, Regulation (EC) No 401/2009, Regulation (EU) 182/2011, Directive
  2003/87/EC or any other external act was imported. Where an indispensable element depended on absent
  external content, the limit was recorded through `additional_context_required` (19 records) and, in the one
  case where nothing could be responsibly determined, through `condition_E = NO` and
  `relational_result = insufficient_evidence` (see note below).

> The single `insufficient_evidence` record is `CAND2-8D7D5ED06FD0` (`source_location`: article 13, point "a"
> — the amended point (a) of Article 1(1) of Regulation (EU) 2018/1999): the reproduced fragment is an objectives clause
> whose grammatical subject sits in a chapeau that is not in the corpus, so R, T, the existence of a third
> actor and any mediating function are all undeterminable rather than absent.

## 7. Note on agreement

Agreement counts among the four proposals were treated throughout as features of the proposals and never as a
truth rule. Every candidate was re-derived from `act.md` and the codebook before the proposals were consulted.
Unanimity was not taken as proof (several 4/4 patterns were only partially adopted, typically on the
identification of R), and isolation was not taken as error. `relationship_to_coder_*` values in the notes file
record, per candidate, whether each proposal was adopted, partially adopted or rejected **on the merits**.
