# G3C decisions C1–C6 — registration and implementation status

**Date:** 2026-10-04 · **Decision-maker:** Igor Caires Machado (as stated in the G3C decision-registration instruction) · **Registered by:** Claude Code (Sonnet 5.5)
These are operational decisions that authorise preparation and evidence classification. They are **not** approval of any conclusion favouring Track B, Claude or Codex.

| # | Decision (as given) | Implementation at G4 Step 0 | Status |
|---|---|---|---|
| **C1** | External audit package: `INCORPORATE_AND_RECONCILE` | Package not found at the expected location; hash `686E322F…FA99` could not be verified; nothing imported. Reconciliation done where possible (local matrix vs original registered criteria): `EXTERNAL_AUDIT_RECONCILIATION.md` | **DECIDED — NOT YET EXECUTABLE** (awaiting file) |
| **C2** | Missing historical auxiliary SHA file: `ACCEPT_WITH_DOCUMENTED_LIMITATION` | `TRACK_B_FREEZE_MANIFEST_SHA256.txt` remains absent (workspace and `TRACK_B.zip`); not regenerated. Limitation recorded in P-02 and in the four-cell manifest (individual outputs 11/11 verified; manifest self-hash chain unresolved) | **EXECUTED** |
| **C3** | Common legal-evidence boundary: `APPROVED`, subject to semantic reconciliation of classification labels | Boundary and dictionary established (`G4_EVIDENCE_SCOPE_DICTIONARY.md`); local labels preserved; external labels E0–E3 pending because their definitions were not available | **APPROVED — RECONCILIATION PENDING** |
| **C4** | Different model prompts and methodological supporting documents: `CONFOUNDED_INPUT` | Registered as deviation D-07/D-08 (and P-06). Rule: no strong causal attribution of differences to the AI model or to the eight-operation procedure; differences that could arise from prompts or method-input documents are tagged `CONFOUNDED_INPUT` | **EXECUTED (rule in force)** |
| **C5** | Codex model/version: one final read-only provenance search; retain `NOT_DOCUMENTED` if unavailable | Search performed (below). **Provenance found** outside the cell artifacts | **EXECUTED — PROVENANCE FOUND** |
| **C6** | Preliminary analytical assessment by AI authorised; human review required for contested evidence, central architectural claims and final legal-validity conclusions | Step 0 is `PRELIMINARY_AI_ASSISTED`; queue of 28 human-review items incl. all 8 central architecture decisions and all contested scope items; no human judgement simulated | **EXECUTED (preliminary)** |

## C5 — result of the Codex provenance search (read-only)

Searched the Codex home folder `C:\Users\Adm\.codex`, reading **only** metadata fields (model, client version, reasoning effort, provider, approval policy) from `config.toml` and from the session file that references the Track B authorisation attachment; conversation content and `auth.json` were not read.

| Field | Value | Source |
|---|---|---|
| Model | `gpt-5.6-terra` (all 37 model fields in the session) | session file `sessions/2026/10/04/rollout-2026-10-04T11-14-19-01a10743-fe9c-7d62-9e75-0fd89b6bb060.jsonl` (591 lines; UTC 14:14:20 – 16:43:13, i.e. 11:14 – 13:43 -03:00); also `config.toml` line 1 |
| Client | Codex VS Code extension (`originator: codex_vscode`), CLI version `0.159.2` | session metadata |
| Reasoning effort | `high` | session metadata and `config.toml` |
| Provider | `openai` (session); `config.toml` also contains a `model_provider = "ollama-launch"` entry at line 163 (not shown to be active in the session) | session metadata; config |
| Approval policy | `never` | session metadata |
| Other config | `service_tier = "priority"` | `config.toml` |
| Session coverage | The same session file references the Track A freeze manifest (19 times), the G2 Track A prompt (22 times), the Track B freeze manifest (5) and the G3 attachment id `a7ffed73…` (6); it has no reference to the Claude replication folders. Its last timestamp (13:43 -03:00) coincides with the Track B manifest time | counts by pattern, no content read |
| Hash of the session file as observed | `3758F284C0B13F2A708390462272E17CDFA049DF4B04FAD540620AE4177A6FF6` (a live file; it will change if the session continues) | local calculation |

**Interpretation limits.** This is session-level provenance external to the frozen cell artifacts (not hashed in any freeze manifest). It indicates that Codex Track A and Track B were produced in **one** session with one recorded model and configuration, which corroborates deviation D-01 (same environment for A and B). It does not prove which turns produced which file; sampling parameters beyond reasoning effort are not recorded.
**Status change:** P-07 moves from `NOT_DOCUMENTED` to `PROVENANCE_FOUND_EXTERNAL_TO_CELL_ARTIFACTS`. The cell artifacts themselves still contain no model identification.
