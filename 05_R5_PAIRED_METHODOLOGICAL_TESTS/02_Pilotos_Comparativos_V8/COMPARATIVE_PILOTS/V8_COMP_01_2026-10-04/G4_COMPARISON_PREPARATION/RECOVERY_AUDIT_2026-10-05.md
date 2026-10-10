# G4 recovery audit — 2026-10-05

## Result

**Recovery classification: `REC-B — STEP2A_PARTIAL_RECOVERABLE`.**

The actual `G4_STEP2A/` subdirectory was not present; the existing Step 2A files were stored directly in `G4_COMPARISON_PREPARATION/`. Eight of the nine required analytical/log outputs existed and matched their registered hashes. The execution log was absent and omitted from the otherwise valid Step 2A freeze manifest, so filename presence and the former `FROZEN` label did not establish a complete required set.

## Baseline verification

- Expected Step 1 manifest SHA-256 `0DEC88FFF9CF9D5B53DAC593AA54368FA7E59DED55D7AFE9E186A3AB7150DD0B`: **MATCH**.
- Step 1 manifest: all 27 frozen output/reference/cell-source rows match. Four append-only register rows differ from their old Step 1 snapshot and are reconciled to the before/after hashes in the later Step 2A manifest; no unexplained difference.
- Common statement register expected SHA-256 `417A35A361E44F8BECFBD8FC39B34738C026591C59B7E837FDDF292F9EF3E77F`: **MATCH**, 20 records (P03 6; P04 14), Article 22(7) absent.
- P03 and P04 official HTML: **MATCH** to FE-001 and FE-003 hashes.
- Four-cell integrity: **41/41 registered file-hash entries MATCH** (Codex A 7, Codex B 11, Claude A 8, Claude B 12, common 3). All required analytical cell outputs were present and verified. Codex B’s auxiliary manifest-self-hash text file is a documented pre-existing absence; the Codex B manifest and each listed analytic output hash match. This known documentation issue did not alter the data or correspondence inputs.
- Step 2A existing freeze: manifest SHA-256 `9655A303DC5897C524ABA1BDE3BE2EB902667731AC9E7C47AE87A770E6D03EC3` matches its recorded value. Its 34 file-valued entries match. It registers eight Step 2A deliverables, not the required execution log.

## Step 2A files preserved before continuation

Eleven existing `G4_STEP2A_*` files were copied before any Step 2A analytical modification. All 11 recovery-copy hashes equal the original hashes. The missing execution log is listed in the pre-recovery inventory as absent. Copy creation timestamps changed; original last-write timestamps and content are recorded.

## Git snapshot

- Branch `main`; HEAD `ae1af320b1f952a0e2fdd0d2142caf5d3886db46`.
- Tracked modifications: 0.
- Untracked status entries: 26 (initial snapshot).
- No merge/rebase/cherry-pick/revert/index-lock markers were found.

The evidence does not meet REC-E. Recovery continues from the preserved Step 2A state; the four experimental cells will not be rerun.
