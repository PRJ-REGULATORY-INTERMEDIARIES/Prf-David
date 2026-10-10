# Recovery state assessment — 2026-10-05

## Classification

**`REC-B — STEP2A_PARTIAL_RECOVERABLE`**

The correspondence analysis, QA report, gate decision and freeze pair exist; the eight output entries in the Step 2A manifest match their hashes. However, the required `G4_STEP2A_EXECUTION_LOG.md` is absent and is not registered in the freeze manifest. Therefore the required Step 2A deliverable set was incomplete despite the prior gate decision's `FROZEN` label. This is a packaging/completion defect; it does not establish that the correspondence judgments themselves are wrong.

## Frozen-state audit

- Step 1 freeze-manifest hash: expected `0DEC88FFF9CF9D5B53DAC593AA54368FA7E59DED55D7AFE9E186A3AB7150DD0B`; actual match.
- Step 1: 27 frozen output/reference/cell-source rows match. Four append-only registers differ from their pre-Step-1 values; each old hash is preserved as `sha256_before_step2a` and each present hash matches the later Step 2A manifest. No unexplained Step 1 mismatch.
- Common register: expected `417A35A361E44F8BECFBD8FC39B34738C026591C59B7E837FDDF292F9EF3E77F`, match.
- Official P03/P04 HTML: FE-001 and FE-003 hashes match.
- Four-cell manifest: all 41 rows with registered SHA-256 values match: Codex A 7, Codex B 11, Claude A 8, Claude B 12, common 3. The Codex B auxiliary manifest self-hash text file is historically absent and explicitly identified in the four-cell manifest; the Codex B manifest itself and all listed analytic outputs match. No cell was rerun.
- Step 2A manifest and hash text: both self-referential files match; all 34 manifest entries with file hashes match their targets.

## Pre-recovery preservation

Before any Step 2A analytical file was changed, all 11 existing files with `G4_STEP2A_*` names were copied to `STEP2A_PRE_RECOVERY/`. Their SHA-256 values match source files. Original and recovery-copy byte lengths and original last-write times are in `PRE_RECOVERY_FILE_INVENTORY.csv`. Copy creation times changed; content hashes and last-write times did not. The missing execution log is explicitly recorded as absent.

## Git state at recovery audit

- Branch: `main`.
- HEAD: `ae1af320b1f952a0e2fdd0d2142caf5d3886db46` (same as reference).
- Tracked modifications: 0.
- Untracked status entries: 26 at initial audit.
- Merge, rebase, cherry-pick, revert and index-lock markers: none found.

## Recovery action authorized by the request

Continue without re-running any of the four experimental cells. Independently validate existing Step 2A correspondence coverage against frozen Step 1 units and matching rules; add the missing execution log and a recovery QA supplement; extend the freeze metadata with an append-only completion record while retaining this pre-recovery copy as the prior manifest version.
