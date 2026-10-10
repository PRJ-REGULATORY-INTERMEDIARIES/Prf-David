# 10 — Freeze and integrity

**`R4_DIGITAL_STRUCTURAL_VALIDATION_FREEZE_RECORD.md`** is the single authoritative statement of
where the round ended: corpus, dataset, B1 design and completion, provenance, batch hashes,
frozen results, the sensitivity audit, the parsimony findings, the control limitation, the B0
decision, the template position, the limitations and the firewalls.

**`R4_DIGITAL_STRUCTURAL_VALIDATION_MANIFEST.csv`** is the SHA-256 manifest of the 24 final
scientific artifacts, each with its authoritative status. Use it to verify that any file you
have matches what was frozen.

`R4_BASELINE_FREEZE_RECORD.md` and `R4_PRE_R4_2_CHECKPOINT.md` mark the earlier stage boundaries.

## `superseded_preserved/`

**NOT AUTHORITATIVE — PRESERVED FOR AUDIT TRAIL.**

These five files are kept because their preservation itself documents a methodological incident.
Do not use them as data.

- Three **B1-01 v1 schema-defective** exports. The first B1-01 export was malformed because note
  text contained separators. It is preserved as evidence of the incident that led to the rule
  that all CSV output goes through a CSV library with full quoting. The authoritative B1-01
  output is `R4_2E_B1_ADVANCED_VALIDATION.csv` in folder 07.
- Two **provenance-superseded** exports, for B1-04 and the sensitivity audit, taken before the
  Claude provenance correction. Their substantive cells are byte-identical to the authoritative
  versions; only the provenance columns differ. They are preserved as part of the recorded
  correction chain.

The current version of every artifact is the one in folders 01 to 09. Nothing in
`superseded_preserved/` should be read as a competing result.

## Verifying this package

`00_START_HERE/R4_PACKAGE_MANIFEST.csv` lists every file in the delivery folder with its size,
SHA-256, category and authoritative status. Every copied evidence file was byte-verified against
its source at packaging time; a mismatch would have excluded the file and been reported as
`COPY_INTEGRITY_FAILURE`. None occurred.

```text
RIT_CODING             = NOT_STARTED
MECHANISM_CODING       = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                   = NOT_STARTED
CORPUS_WIDE_REPAIR     = NOT_EXECUTED
```
