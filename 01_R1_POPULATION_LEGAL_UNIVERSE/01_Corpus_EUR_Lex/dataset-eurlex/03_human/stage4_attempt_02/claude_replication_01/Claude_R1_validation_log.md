# Claude_R1 Validation Log

**Replicate:** Claude-R1 (independent coder, dataset-eurlex, CELEX 32021R1119)
**Methodology:** v1.1.0 (`methodology/v1.1.0/codebook.md`, `methodology/v1.1.0/reference_coding_schema.json`)
**Candidates processed:** 90 (from `03_human/stage4_attempt_02/R1_coding_input.json`)

## 1. Method used for validation

Validation was performed in two independent passes, both run against
`Claude_R1_output_raw.json` (the frozen, unvalidated output written in Step 1 of the
preservation protocol) via a throwaway driver script,
`claude_replication_01/_r1_validate_driver.py`:

1. **Schema validation (structural).** The `jsonschema` package (v4.26.0, confirmed
   available via `python -c "import jsonschema"`) was used to validate every one of the
   90 records against `methodology/v1.1.0/reference_coding_schema.json` with a
   `Draft202012Validator`. All required keys, enum values (e.g.
   `screening_status`, `relational_result`, `primary_mechanism`,
   `evidence_role`, `observability`, `confidence`), and nested object shapes
   (`source_location`, `actor`, `condition_result`, `evidence_item`) were checked this way.
   **Result: 0 schema errors across all 90 records** (both before and after the
   corrections described below).

2. **Relational logic validation.** `validate_relational_logic` and
   `substantive_signature` were imported directly from
   `03_human/stage4_attempt_02/validate_reference_logic.py` (loaded via
   `importlib.util`, never edited) and called on every record. This function checks,
   among other things:
   - that each of the five A–E conditions carries a valid result (`YES`/`NO`/`UNCLEAR`)
     and non-empty `evidence_refs`;
   - that `relational_result` is logically compatible with the A–E pattern
     (all YES → `positive`; any of A–D = `NO` → `negative`; E = `NO` alone →
     `insufficient_evidence`; otherwise, with an `UNCLEAR` present → `conditional`);
   - that a `positive` result carries non-empty `R`, `I`, and `T`, and is never paired
     with an exclusionary `screening_status`;
   - that `screening_status = "direct_relationship"` never carries a populated `I`;
   - that `condition_C = "YES"` and `condition_D = "YES"` each require a populated `I`.

   Separately, before running this check, a manual self-consistency check (independent
   of `validate_reference_logic.py`, run only against the codebook's own stated A–E →
   `relational_result` mapping) was performed across all 90 records and found **0
   inconsistencies**, confirming the substantive coding was internally coherent with the
   codebook's own logic before the reference validator's additional structural
   constraints (on the `I` field specifically) were checked.

   **Result on `Claude_R1_output_raw.json`: 2 records raised `ValueError`.**

## 2. Corrections made

Both violations were logged and corrected in `Claude_R1_output.json`. **The raw file,
`Claude_R1_output_raw.json`, was never modified** — corrections were applied only to a
copy loaded fresh from the raw file's content, which was then written out as
`Claude_R1_output.json` (see `claude_replication_01/_r1_make_validated.py`).

### Correction 1

- **candidate_id:** `CAND2-D64B4FFA6C04` (Article 4(4) — Union 2040 greenhouse gas
  budget, Commission "shall ... take into account the advice of the Advisory Board")
- **field:** `I`
- **original value:** `null`
- **rule violated:** `validate_relational_logic`: `condition_C == "YES"` requires
  `record["I"]` to be populated.
- **corrected value:** `[{"label": "Advisory Board", "role": "provides advice taken
  into account by the Commission when setting the projected indicative Union
  greenhouse gas budget", "evidence_refs": ["E1"]}]`
- **nature of correction:** Substantive/structural. The raw record had already judged
  `condition_C = YES` (the Advisory Board is a distinct third actor named in this
  paragraph) but left the `I` field empty, reasoning that no target (`T`) existed for it
  to mediate towards (`condition_B = NO`). This was an internal inconsistency between an
  already-made C-condition judgment and the `I` field, which the correction resolves by
  populating `I` to match. **No A–E condition result, and no `relational_result`, was
  changed** (`relational_result` remains `negative`, driven independently by
  `condition_B = NO`).

### Correction 2a

- **candidate_id:** `CAND2-8607C66ECE11` (Article 8(3)(d) — Commission's assessment
  basis: "best available and most recent scientific evidence, including the latest
  reports of the IPCC, IPBES and other international bodies")
- **field:** `I`
- **original value:** `null`
- **rule violated:** `validate_relational_logic`: `condition_C == "YES"` requires
  `record["I"]` to be populated.
- **corrected value:** `[{"label": "IPCC", ...}, {"label": "IPBES", ...}]` (both marked
  as international scientific bodies whose reports are cited as evidence but not
  tasked with a regulatory function by this Regulation)
- **nature of correction:** Same root cause as Correction 1: `condition_C = YES` had
  already been judged (IPCC/IPBES are analytically distinct actors named in the text)
  but `I` was left empty because their function does not mediate a regulatory relation
  under this Act (`condition_D = NO`, unchanged). `relational_result` remains `negative`.

### Correction 2b

- **candidate_id:** `CAND2-8607C66ECE11`
- **field:** `screening_status`
- **original value:** `"direct_relationship"`
- **rule violated:** `validate_relational_logic`: `screening_status ==
  "direct_relationship"` requires `record["I"]` to be empty/`None`.
- **corrected value:** `"candidate"`
- **nature of correction:** Mechanical, a direct consequence of Correction 2a. Once a
  distinct (if non-mediating) third party is identified in `I`, the relation is no
  longer the pure dyadic case the reference validator reserves for
  `direct_relationship`. `screening_status` is corrected to `candidate`, the
  mechanically consistent status for a record with an identified but non-mediating
  third party. `relational_result` (`negative`) is unchanged.

No other records required correction. No A–E condition result was changed for
substantive reasons (i.e., no case was found where a condition result "misread the
evidence"); both corrections above repaired an internal inconsistency between an
already-made condition judgment and the corresponding actor field, not the substance of
the judgment itself.

## 3. Post-correction validation

Re-running both the `jsonschema` structural check and
`validate_relational_logic` against `Claude_R1_output.json` after applying the two
corrections above returns **0 schema errors and 0 relational-logic errors** across all
90 records.

## 4. Summary statistics

- **Candidates processed:** 90
- **Records valid (post-correction):** 90 / 90 (0 schema errors, 0 relational-logic errors)

**Distribution of `relational_result`** (identical in raw and validated copies — the
corrections did not change any relational_result):

| Value | Count |
|---|---|
| `positive` | 3 |
| `negative` | 86 |
| `conditional` | 1 |
| `insufficient_evidence` | 0 |

**Distribution of `confidence`** (identical in raw and validated copies):

| Value | Count |
|---|---|
| `high` | 55 |
| `medium` | 30 |
| `low` | 5 |
| `not_assessed` | 0 |

**Distribution of `screening_status`:**

| Value | Raw | Validated |
|---|---|---|
| `candidate` | 39 | 40 |
| `direct_relationship` | 31 | 30 |
| `not_candidate` | 20 | 20 |
| `insufficient_evidence` | 0 | 0 |

- **Count of candidates where `I != null`:** raw = 4; **validated = 6**
- **Count of candidates where `condition_C.result == "YES"`:** 6 (unchanged by corrections)
- **Count of candidates where `condition_D.result == "YES"`:** 4 (unchanged by corrections)

The three `positive` candidates are:
- `CAND2-465FC96778A7` (Article 8(3)(b) — Commission bases Article 6/7 assessments on
  reports of the EEA, the Advisory Board and the Commission's Joint Research Centre)
- `CAND2-88A2261C68DE` (Article 8(4) — "The EEA shall assist the Commission in the
  preparation of the assessments referred to in Articles 6 and 7")
- `CAND2-27E84BD23730` (Article 13, point (b), amending Article 17(4) of Regulation
  (EU) 2018/1999 — Commission adopts implementing acts on reporting format, "assisted
  by the Energy Union Committee")

The single `conditional` candidate is `CAND2-AB84F16B6A72` (Recital 37), which mirrors
the structure of the first two positive candidates above but rests only on non-binding
recital ("should") language rather than operative ("shall") text, so condition E was
marked `UNCLEAR` rather than `YES` per codebook section 13 (recitals do not by
themselves create an operative obligation).

## 5. File integrity

- **SHA-256 of `Claude_R1_output_raw.json`:**
  `f997f3d763836887d858528e78ac3753be9fb0dfe23bfd0fa0bf885ea4870daa`
- **SHA-256 of `Claude_R1_output.json`:**
  `86cf2af470fad31165efd0af8ac1cb02fa77c20b6bacad265a40601d5611e2e5`

`Claude_R1_output_raw.json` was written in full (Step 1 of the preservation protocol)
before `validate_reference_logic.py` was opened or any validation was performed (Step
3), and has not been modified since; its SHA-256 above was recorded immediately after
writing and reconfirmed identical after producing the validated copy.
