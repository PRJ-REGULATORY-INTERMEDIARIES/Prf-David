# Claude-R2 Validation Log

**Candidate:** Claude-R2 (independent second coder), stage4_attempt_02
**Corpus:** CELEX 32021R1119 (Regulation (EU) 2021/1119, "European Climate Law")
**Methodology:** v1.1.0 (`codebook.md`, `reference_coding_schema.json`)

## 1. Method used for validation

A throwaway driver script, `_r2_validate_driver.py`, was written in this folder after
`Claude_R2_output_raw.json` had already been produced and hashed (Steps 1-2 of the
preservation protocol were completed first; this script and everything below it followed
only afterward, per Step 3).

The driver:

1. Loaded `Claude_R2_output_raw.json` (90 records).
2. Validated every record's structure against `methodology/v1.1.0/reference_coding_schema.json`
   using the `jsonschema` package (`jsonschema.Draft202012Validator`, confirmed available in
   the environment: version 4.26.0). All 90 records passed schema validation with **zero**
   structural errors (required keys, enum values, and nested object shapes for
   `source_location`, `relational_test`, `evidence_items`, actor lists, etc. all conform).
3. Imported `validate_reference_logic.validate_relational_logic` from
   `03_human/stage4_attempt_02/validate_reference_logic.py` (not modified) and called it on
   every record, catching and logging any `ValueError` per `candidate_id`.

`validate_relational_logic` checks, per record: that each of conditions A-E is one of
`YES/NO/UNCLEAR` with non-empty `evidence_refs`; that `relational_result` is logically
consistent with the A-E pattern (all YES -> positive; any of A/B/C/D = NO -> negative;
E = NO with no A-D = NO -> insufficient_evidence; otherwise -> conditional); that a
`positive` result requires non-empty `R`, `I` and `T`, and a non-exclusionary
`screening_status`; that `screening_status = "direct_relationship"` cannot carry a
non-empty `I`; and that `condition_C = "YES"` or `condition_D = "YES"` each require a
non-empty `I`.

## 2. Corrections made

**One correction was required**, logged below in full. No other schema or logic errors
were found across the other 89 records.

| Candidate ID | Field | Original value | Rule violated | Corrected value | Nature |
|---|---|---|---|---|---|
| `CAND2-D64B4FFA6C04` (Article 4(4)) | `I` | `null` | `validate_relational_logic`: `condition_C.result == "YES"` requires a non-empty `I` list | `[{"label": "Advisory Board", "role": "provides advice taken into account by the Commission (distinct third actor per condition_C; no target actor/mediated relation established, per condition_D = NO)", "evidence_refs": ["EV2"]}]` | **Mechanical/structural.** The raw record's `condition_C` was already coded `YES` and its `interpretive_note` already identified the Advisory Board as "a distinct third actor" in this provision; the `I` actor-list field had simply not been populated to match that already-made determination. No A-E condition result, no `relational_result` (`negative`, unchanged — `condition_D = NO` on its own already precludes a positive result), and no other substantive judgment was altered. |

No condition result (A-E), no `relational_result`, and no `screening_status` was changed
for any candidate. The raw file `Claude_R2_output_raw.json` was not touched.

## 3. Summary statistics

- **Candidates processed:** 90
- **Records valid (post-correction):** 90 / 90 (0 schema errors, 0 relational-logic errors)

**Distribution of `relational_result`:**

| Value | Count |
|---|---|
| negative | 87 |
| positive | 3 |
| conditional | 0 |
| insufficient_evidence | 0 |

**Distribution of `confidence`:**

| Value | Count |
|---|---|
| high | 76 |
| medium | 14 |
| low | 0 |
| not_assessed | 0 |

**Distribution of `screening_status`** (for reference, not requested in the fixed table above but relevant to interpretation):

| Value | Count |
|---|---|
| not_candidate | 44 |
| candidate | 30 |
| direct_relationship | 16 |
| insufficient_evidence | 0 |

- **Candidates where `I != null`:** 4
  (`CAND2-465FC96778A7` — Article 8(3)(b), EEA/Advisory Board/JRC feeding the Commission's Article 6-7 assessment;
  `CAND2-88A2261C68DE` — Article 8(4), EEA assisting the Commission's Article 6-7 assessment preparation;
  `CAND2-27E84BD23730` — Article 13 point (b) replacing Article 17(4) of Regulation (EU) 2018/1999, Energy Union Committee assisting the Commission's implementing acts on Member State reporting format;
  `CAND2-D64B4FFA6C04` — Article 4(4), Advisory Board as a distinct third actor with no mediating function towards a target, corrected as above).
- **Candidates where `condition_C.result == "YES"`:** 4 (the same four records listed above)
- **Candidates where `condition_D.result == "YES"`:** 3 (all of the above except `CAND2-D64B4FFA6C04`, whose `condition_D` is `NO`)
- **SHA-256 of `Claude_R2_output_raw.json`:** `e9cecdb87207a636d94b54e5e86e4d099986bac77fcb6428844b2631a5844df5`
- **SHA-256 of `Claude_R2_output.json`:** `cfea747db3441279cb4293092a7cc9435434bb967880ae0f5404e1b401f5a06e`

## 4. Notes on interpretive approach (for audit transparency)

- All 27 recital-level candidates were coded `screening_status = not_candidate`,
  `relational_result = negative`, on the basis that recitals provide interpretive context
  but do not by themselves create an operative obligation (codebook §13), and none of them
  independently identifies both a regulator exercising a function and a target actor
  distinct from the rhetorical/collective subject of the sentence.
- Only 3 of the 90 candidates were coded `relational_result = positive`, all requiring a
  textually explicit, distinct third-party institutional actor (European Environment
  Agency, European Scientific Advisory Board on Climate Change, Commission's Joint Research
  Centre, or the Energy Union Committee) performing a genuine mediating function between the
  Commission and Member States within the Commission's own oversight/standard-setting
  architecture (Articles 6-8 and the Article 13 amendment to Regulation (EU) 2018/1999,
  Article 17(4)). Generic international scientific bodies (IPCC, IPBES) cited only for their
  scientific authority, and pure data/statistics sources (e.g., the Copernicus programme),
  were deliberately not treated as mediating intermediaries, to avoid converting mere
  informational input into a regulatory relation (codebook §1, §3).
- 16 candidates were coded `screening_status = direct_relationship` with
  `relational_result = negative`, reflecting genuine, well-evidenced two-party
  regulator-target relations (typically Commission-Member State) with no textually
  supported intermediary — consistent with the codebook's instruction that a direct R-T
  relation must not be given an artificial `I`.
- Several candidates amending Regulation (EU) 2018/1999 via Article 13 that consist of bare
  noun-phrase list items (lacking their own subject-verb clause and reliant on an external,
  non-imported chapeau) were coded `not_candidate` with `additional_context_required` noting
  the external provision that would be needed for full reconstruction, rather than forcing
  an inferred positive or negative relation.

## 5. Throwaway scripts retained for audit

- `_r2_validate_driver.py` — validation driver described above (kept for audit).
- `_r2_validation_errors.json` — raw dump of the single pre-correction error.
- `_r2_corrections.json` — machine-readable record of the one correction applied.
- `_r2_final_hashes.json` — machine-readable record of the two SHA-256 hashes above.

`validate_reference_logic.py` itself was not modified.
