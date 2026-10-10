# Orchestrator isolation audit summary (non-substantive; for the family contamination audit)

Method: for every case executor (including interrupted ones) the orchestrator inspected only the **tool inputs** (file paths, shell commands) recorded in the executor's transcript, never tool results or analytical text, against the strict allow-list (frozen method documents, execution addendum, own capsule, own output directory, plus single explicitly authorised recovery notes). Technical read-deny rules were not active in the session (a test read of a denied path succeeded) and shell commands bypass them, so the allow-list was the control. Each executor was a fresh `general-purpose` subagent (model alias `sonnet`; Agent tool exposes no reasoning-effort parameter), launched sequentially; no case content was passed between executors; executors returned only seven non-substantive fields.

| Case | Executor(s) | Tool calls (Read/Bash/Write/Edit/PowerShell) | Flagged accesses outside allow-list | Gate | Case freeze-manifest SHA-256 |
|---|---|---|---|---|---|
| RGAM_C1_SCF | a773412851ad46032 | 20/72/22/0/0 | 0 | RGAM_CASE_FROZEN | 7fd01ed8e0e95616c8dfb836694e00f29c5887f04b24f0f483b2220b15ef3f65 |
| RGAM_C2_CBAM | aee1506e1d0e70177 | 12/47/17/0/0 | 0 | RGAM_CASE_FROZEN | 84647523b5800816b7d56279383cbbfaaeea95296765e7e171e2329dafe6e096 |
| RGAM_AI_AI_ACT | ad1c4f939eaef025b (interrupted at 12 calls; blank templates only; not reused) | 7/5/0/0/0 | 0 | — | — |
| RGAM_AI_AI_ACT | ad615b1d8063b1df2 (fresh recovery run) | 25/100/28/0/0 | 1 benign (the one authorised recovery-state note) | RGAM_CASE_FROZEN | 160217c11f2cf5e70f22a3eb527ac916cb460ce3d9c70a313ae91160e5e15372 |
| RGAM_O_DIR_86_361 | a86c431b77ac102f0 (interrupted; analytical tables produced; later adopted as partial state) | 8/8/9/0/0 | 0 | — | — |
| RGAM_O_DIR_86_361 | a04521a3bcdf0d1d0 (fresh recovery run) | 33/24/6/1/1 | 2 benign (the authorised recovery-state note; a progress-note text containing "/logs/") | RGAM_CASE_FROZEN | 3dc9add69f04c3a9e5658c0dc90a4a1b5fe6be348e286aae102c4ba8a6c30b1b |

Shared method (re-verified before launch of the family assembler): protocol manifest SHA-256 `9ca016b97289b39049dc099b265c20662c1ebc05e86bc720f0fbe80e0bac5932` (107 files OK); execution addendum SHA-256 `b9dc184ebc857e5e3aae85ea5e1b5ac28f64c9947086b2bbe763a3b936e02da4`. Common-corpus source hashes equal the register. Recovery snapshots: `_RECOVERY_AI_ACT_2026-10-06/`, `_RECOVERY_DIR_86_361_2026-10-06/` (immutable; not frozen case directories; not to be read by the assembler).
The orchestrator did not read the analytical content of any case before the family stage.
