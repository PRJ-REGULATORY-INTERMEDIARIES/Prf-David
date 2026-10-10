# PILOT03_REGRESSION_RESULTS (R05) — genuine re-execution in a derived copy

## Procedure
1. **Copy.** `RELATIONAL_LEXIMETRICS_PILOT/` was copied whole (`cp -rp`, 75 files, `__pycache__` removed) to `05_PILOT03/regression_copy/RELATIONAL_LEXIMETRICS_PILOT/`.
2. **Safety check before running.** All four scripts resolve their root as `Path(__file__).resolve().parents[1]`, so every write lands inside the copy. The only external read is `C:/Users/Adm/Downloads/HUMAN_ADJUDICATION_RESPONSES_FILLED.csv` (hash-identical to the frozen baseline; read-only).
3. **Run order and results:**
   - `PILOT_01/.../build_pilot.py` → exit 0
   - `PILOT_02/.../build_pilot02.py` → exit 0
   - `PILOT_03/.../build_pilot03.py` → exit 0
   - `PILOT_03/.../incorporate_human_adjudication.py` → exit 0

   Run with `PYTHONDONTWRITEBYTECODE=1`. Logs: `05_PILOT03/regression_copy/run_*.log`.
4. **Comparison.** Every original file was compared with its regenerated counterpart (`00_ADMIN/scripts/r05_regression_diff.py` → `PILOT03_REGRESSION_FILE_COMPARISON.csv`, `PILOT03_REGRESSION_DIFF_LINES.csv`).

## Results
| Result class | Files |
|---|---|
| IDENTICAL (byte-equal) | 70 |
| VOLATILE_ONLY (timestamps / run date / hashes derived from them) | 4: `PILOT_02_MANIFEST.json`, `PILOT_03/03_SOURCE_PROVISIONS/PROVISION_REGISTER.csv` (field-level check: only `capture_date` differs), `PILOT_03_MANIFEST.json`, `PILOT_03_MANIFEST_FINAL.json` |
| SUBSTANTIVE_DIFF | 1: `PILOT_01/99_REPRODUCIBILITY/PILOT_MANIFEST.json`. The only non-volatile change is the absolute `source_dataset` path, which points into the copy — an expected effect of relocation |

Key fields of the regenerated final manifest compared with the original:
- `status` and `final_gate`: `ONTOLOGY_STABLE_WITH_REVISIONS` = same
- `adjudicated_items`: 19 = 19
- `backward_impact_items`: 14 = 14
- `pre_adjudication_gate_preserved`: `PILOT_03_AWAITING_HUMAN_ADJUDICATION` = same
- `pre_adjudication_manifest_sha256`: differs, as expected, because the pre-manifest embeds `built_on`

## Interpretation
- **Computational reproducibility of the pilot chain: PASS.** All data files (codings, comparisons, decision logs, backward-impact register, rules, reports) regenerate byte-identically.
- **What this does *not* show.**
  - The regression cannot show that the codings are *correct*, because they are hard-coded in the scripts (`PILOT03_AUDIT.md` Q1).
  - It cannot show that the gate is *earned*, because the gate is a constant (Q2).
  - `capture_date` is the build date, not the date the legal text was captured.
- The integrity tests on the human-decision layer (uniqueness, rationale presence, filled = log, flag = register) are in `PILOT03_RECONCILIATION.csv`, and all pass.
