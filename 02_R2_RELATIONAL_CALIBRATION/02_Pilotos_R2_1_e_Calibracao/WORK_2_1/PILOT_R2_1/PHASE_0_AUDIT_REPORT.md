# WORK 2.1 — PILOT R2.1 — PHASE 0 AUDIT REPORT
**Environment and Source Audit** · executed 2026-09-19 · agent: Claude (Sonnet 5)

---

## Phase 0 findings (required content)

### 0.1 Files found

Two roots were inventoried (every file hashed with SHA-256; `.git/` excluded):

| Root | Path | Files |
|---|---|---|
| `GITHUB_REPO` | `C:\PROJETOS\GITHUB\git-PRJ-REGULATORY-INTERMEDIARIES--Prf-David` (git, branch `main`, 1 commit `27ba3e4`, clean before this work) | 602 |
| `ICM_PMO_PROJECT` | `C:\PROJETOS\ICM-PMO\10_PROGRAMAS\GP5_JRG\PROJETOS\Prf-David` | 4 (admin notes only; `entregas/` and `reunioes/` empty) |

Main blocks inside `GITHUB_REPO`:

| Block | Content |
|---|---|
| `Arquitetura de trabalho/` | G0/G1/G2/“Geral” prompts and the experiment diagram (5 files) |
| `Before_R2/dataset-eurlex/` | Production project: 3 locked cases, legacy 1-act pilot (`01_source`…`07_report`), R1/R2/Terra/Claude/RA four-way replication under `03_human/stage4_attempt_0{1,2}`, methodology v1.1.0–v1.1.2 and production_v1.0/v1.1, primary + secondary coding proposals, `final_human_review_v2/`, prompts, docs |
| `Before_R2/dataset-eurlex-cleanroom/` | Independent clean-room rebuild (3 cases, sources + corpora only; state `corpus_locked`) |
| `Before_R2/Estudos Preliminares e testes/` | Legacy PoC (`v1`, `Entrega-02`, `Entrega-03`, `PoC 01`) |
| `Before_R2/Inputs/` and `Before_R2/Exercício Dataset/` | Theory/framework inputs (Mapatz proposal, technical notes, methodology draft) |
| `Enviados/` | What was sent to David: final 3-case dataset (CSV/XLSX), technical note, 12-Sep meeting decks, chats |
| `Post_R2/R2_notes/` | Meeting notes after R2 (AI summary + near-empty transcript) |

### 0.2 Source hierarchy (proposed for this pilot)

| Tier | Role | Where | Files |
|---|---|---|---|
| T1 | **Authoritative legal source** (official EUR-Lex/CELLAR XHTML) | `act_official.xhtml` ×7 (3 production cases, 1 legacy `01_source`, 3 clean-room) | 7 |
| T2 | Provenance / registries / manifests | `provenance.yaml`, `*_manifest.yaml`, `CASE_REGISTRY.yaml`, `case_registry.yaml` | 16 |
| T3 | Derived corpus (normalized Markdown/PDF) | `act.md`, `act_numbered.md`, `act_full/operative/recitals.md`, `act.pdf` | 18 |
| T4 | Methodology, codebooks, schemas, prompts | see inventory | 141 |
| T5 | Prior coding / review outputs (**not ground truth**) | `primary_coding`, R1/R2, RA, `final_human_review_v2`, `Enviados/Email 01` dataset, etc. | 173 |
| T6 | Theory inputs, legacy PoC, communications | `Inputs`, `Estudos Preliminares`, `Enviados`, `Post_R2` | 148 |
| T7 | Scripts / tests | `.py`, `tests/` | 47 |
| T8 | Unclassified / other | | 56 |

Rule proposed: legal claims are anchored only in T1 (via T3 as a navigation aid, verified against T1). T5 is used only for the Phase 9 comparison, never as evidence.

### 0.3 Missing items (not found in either root)

1. **No object named “Pilot A”.** The likeliest referent is the three-case, researcher-adjudicated dataset (`Enviados/Email 01/DATASET_EURLEX_RIT_FINAL_FOR_DAVID.*` + `final_human_review_v2/`). Unconfirmed (see D3).
2. **The “five substantive R2 cases” are not defined anywhere.** The registries list only 3 cases (CELEX 32021R1119, 32023R0956, 32023R1115). The 12-Sep deck proposes Fit for 55 as a population but I found no list of five.
3. **The instrument for this pilot is not named in the prompt** (it refers to “the instrument”). Phase 1 cannot start without it (see D1).
4. **The source of the Levi-Faur corrections (§2) and the 3–4–2 ontology is this prompt only.** There is no file for it in the repo; David’s guidance is not traceable to a document.
5. `FIT_FOR_55_POPULATION_MASTER.csv` (mentioned in the 12-Sep deck) does not exist yet — expected, it is future work.
6. `Enviados/Reunião…/regulatory_intermediation_discussion_panel_light.html`, three other decks and the `.docx` files were **not opened** (only the Fit-for-55 deck, pp. 1–6, and the final CSV were read).

### 0.4 Inconsistencies found

| # | Inconsistency | Evidence | Severity |
|---|---|---|---|
| I1 | **Two non-identical source files for the same CELEX in cases 02 and 03.** Production XHTML ≠ clean-room XHTML (case 02: `B61FD911…` 499,130 B vs `C47E2793…` 496,976 B; case 03: `2DE95792…` 390,156 B vs `FC30A30A…` 387,997 B). Case 01 is byte-identical in both. Corpus hashes also differ. Production was fetched 2026-09-07 via `eur-lex.europa.eu/.../TXT/HTML`; clean-room 2026-09-09 via CELLAR content negotiation. Cause not diagnosed; textual equivalence **not** verified. | SHA-256 comparison | **High** |
| I2 | `Before_R2/dataset-eurlex/README.md` (“Estado atual”: `methodology_locked`, `experiment not_started`, “PARE”) is stale relative to `README_PRODUCTION.md`, `CASE_REGISTRY.yaml` (`production_v1.0`, corpora locked) and the coding outputs. The clean-room `STATE.md` says only `corpus_locked`. | README/registry comparison | Medium |
| I3 | Methodology sprawl in `dataset-eurlex/methodology/`: root, `v1.1.0`, `v1.1.1`, `v1.1.2`, `production_v1.0`, `production_v1.1`, plus four working drafts (`STAGE4`, `V1_1`, `V1_3`, `SIMPLIFIED`). Which one Pilot A actually used was not established in this phase. | file listing | Medium |
| I4 | `PoC 01/Entrega-03/CHANGELOG_v4.md` (4,584 B) differs from `Estudos Preliminares/Entrega-03/CHANGELOG_v4.md` (4,176 B), though the two trees are otherwise duplicates. | size comparison (content not diffed) | Low |
| I5 | Pilot A’s mechanism vocabulary (reporting / certification / auditing / ranking-rating / other) does not map one-to-one to the nine R2.1 mechanisms. A crosswalk is needed before Phase 9. | `DATASET_EURLEX_RIT_FINAL_FOR_DAVID.csv` | Medium |
| I6 | Post-R2 meeting note (12-Sep): David suggested testing first on laws **before 2019**. All locked cases are 2021–2023. | `Post_R2/R2_notes/Resumos IA` | Medium (design) |

### 0.5 Version risks

- **Original vs consolidated text.** Production provenance records “original legal act, not a consolidated version”, and excludes corrigendum `32021R1119R(01)` and later consolidations. I did not check EUR-Lex for later amendments or corrigenda (no web access used). The pilot must state which text version it codes.
- **Two competing corpora** for cases 02/03 (I1). Coding on the wrong one would silently change article/paragraph anchors.
- **Two normalizations**: production `act.md`/`act_numbered.md` (line-numbered) vs clean-room `act_full/operative/recitals.md`. Evidence citations must state which was used.
- **Duplicates**: 92 hash-identical groups covering 223 files (mostly `PoC 01` vs `Estudos Preliminares`, and `Inputs` vs `Exercício Dataset/Inputs`). Risk of citing a copy as if it were the original.
- **Superseded material**: `03_human/stage4_attempt_01` (14 files flagged `SUPERSEDED_ATTEMPT`) is preserved but superseded.
- **Hash verification**: production `source_hash` and `corpus_hash` in `CASE_REGISTRY.yaml` match recomputed SHA-256 for all 3 cases (verified). Clean-room manifest hash for case 02 matches its own file (verified); other clean-room manifests were not individually cross-checked.
- `.gitignore` excludes `*.env`, `API-*` and the `PoC 01/API-prj-inter-reg` path; anything there is outside version control and outside this inventory.

### 0.6 Proposed working directory

```
C:\PROJETOS\GITHUB\git-PRJ-REGULATORY-INTERMEDIARIES--Prf-David\WORK_2_1\PILOT_R2_1\
```

- New sibling of `Before_R2/`, `Post_R2/`, `Enviados/`. Did not exist before this run; nothing overwritten.
- `Before_R2/` and everything else stays read-only for this pilot. Sources are referenced in place; if copied into the namespace they are copied with hash verification and never edited.
- Phase outputs will be created as new files with `_v0_1` suffixes; a later change creates `_v0_2`, never an overwrite.
- Not committed to git (`?? WORK_2_1/` untracked). Commit only on your instruction.

---

## A. What was done
Located both project roots; listed and SHA-256-hashed every file (606); classified each by source tier and role using path rules; checked recorded source/corpus hashes against recomputed ones; read the registries, provenance files, READMEs, meeting notes, the Fit-for-55 deck (pp. 1–6) and the delivered 3-case dataset header; searched for “Pilot A”, “five cases” and prior R2.1 material; created the new namespace. No legal text was read for analysis and no coding was done.

## B. Inputs used
`CASE_REGISTRY.yaml`; clean-room `case_registry.yaml`, `STATE.md`, `source_manifest.yaml`, `corpus_manifest.yaml` (case 02); `provenance.yaml` (production 01_source and case 02); `LEGACY_PILOT_AND_SIMPLIFICATION_NOTE.md`; `README.md` files; `Post_R2/R2_notes/*`; `Enviados/.../5 - Nexts_Steps_Fit_for_55_RIT_Proposal.pdf` (pp. 1–6); `DATASET_EURLEX_RIT_FINAL_FOR_DAVID.csv`; the WORK 2.1 prompt.

## C. Outputs created
- `WORK_2_1/PILOT_R2_1/PHASE_0_SOURCE_INVENTORY.csv`
- `WORK_2_1/PILOT_R2_1/PHASE_0_AUDIT_REPORT.md` (this file)

## D. Quantitative summary
- Files inventoried: **606** (602 + 4); zero-byte files: 0; every row has a SHA-256.
- Authoritative legal sources (XHTML): **7** (3 CELEX × production, 3 × clean-room, 1 legacy copy of Climate Law).
- Distinct instruments locally available: **3** (32021R1119, 32023R0956, 32023R1115).
- Source-hash mismatches between production and clean-room copies: **2 of 3** cases.
- Duplicate groups: **92** (223 files).
- Tier counts: T1 7 · T2 16 · T3 18 · T4 141 · T5 173 · T6 148 · T7 47 · T8 56.

## E. Methodological decisions
1. Tiering is heuristic (regex on paths); it is a navigation aid and not a finding. T8 (56 files) was not hand-sorted.
2. T5 (all earlier codings, including the delivered 3-case dataset) is designated **comparison-only, not evidence**.
3. Namespace placed at repo root as `WORK_2_1/PILOT_R2_1/`, as recommended in the prompt.
4. I did not resolve I1 by choosing a source; that is left to you.

## F. Uncertainties
- Identity of “Pilot A” (inferred, not confirmed).
- Cause and content-level impact of the source differences in I1.
- Which methodology version Pilot A actually used (I3).
- Whether later amendments/corrigenda affect any of the three acts.
- Contents of documents I did not open (0.3 item 6).

## G. Deviations from prompt
1. The inventory covers **two roots** (the GitHub repo and the ICM-PMO admin folder) in one CSV; the prompt says “all relevant pilot files” without naming locations. The `root` column keeps them separable.
2. No prior WORK 2.1 / R2.1 files existed, so the “identify prior coding outputs” objective was answered with the *pre-R2.1* outputs (T5), not with earlier R2.1 versions.
3. I did not save a copy of the prompt into the namespace (see D6).

## H. Quality-control checks
- Row count (606) equals the sum of both roots; `file_id` unique, sequential; 0 empty `sha256`.
- Recomputed SHA-256 vs registry: `source_hash` ×3 ✔, `corpus_hash` ×3 ✔.
- Production vs clean-room source hashes compared: case 01 ✔ identical, cases 02/03 ✘ different (I1).
- `git status` after the run: only `?? WORK_2_1/`; no tracked or pre-existing file was modified.
- Not done: content diff of duplicate groups; content diff of I1 sources; verification against live EUR-Lex.

## I. Researcher decisions required
- **D1 — Instrument.** Which single instrument is the R2.1 pilot on? Options: Climate Law 32021R1119 (smallest, 68 KB corpus), CBAM 32023R0956, EUDR 32023R1115 (all three already coded in Pilot A, so Phase 9 can compare), or a pre-2019 act per David’s 12-Sep suggestion (no local corpus yet; Phase 0 would need extending). My recommendation: one of the three existing cases, to keep Phase 9 comparable.
- **D2 — Source authority for cases 02/03.** Production XHTML (matches locked registry hashes and what Pilot A was coded on) or clean-room XHTML? My recommendation: production, with a text-level diff against the clean-room copy as the first step of Phase 1.
- **D3 — Confirm “Pilot A”** = the three-case adjudicated dataset sent to David, or name it.
- **D4 — Five R2 cases.** Provide the list (or confirm it is deferred). Not needed before Phase 9, but the prompt refers to it.
- **D5 — Approve the working directory** in 0.6, or name another.
- **D6 — Save the WORK 2.1 prompt** verbatim into the namespace as a provenance file? (Otherwise §2 and the 3–4–2 ontology have no traceable source.)
- **D7 — Pre-2019 tension (I6):** proceed with a 2021–2023 instrument for the pilot anyway?

## J. Status
`READY_FOR_RESEARCHER_REVIEW`

STOP.

`PHASE_0_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`
