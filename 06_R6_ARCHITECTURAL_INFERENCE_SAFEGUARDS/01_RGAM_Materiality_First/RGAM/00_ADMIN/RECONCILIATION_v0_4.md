# RGAM — Repository reconciliation (Phase 1, Step A)

**Date:** 2026-10-03 · **Status:** `WORKING_RECORD` — documentary reconciliation, not scientific validation.
**Authoritative RGAM root:** `G:\Meu Drive\PRJ-David\Prf-David\RGAM` (authorized by Igor, 2026-10-03).
**Parent repository:** `G:\Meu Drive\PRJ-David\Prf-David` — recovery-sensitive Git state (see `RELATORIOS_DE_ESTADO_DO_PROJETO/2026-10-03__GIT_RECOVERY_AUDIT.md`). No staging, commit, reset, clean or normalization was performed.

## 1. Rules applied

- Nothing outside `RGAM/` was modified. The only operation on parent files was a read, plus a copy into `RGAM/historical_audit_copy/`.
- Versioning: newly integrated outputs use `v0_4`. No intermediate version is invented; there is no v0_1/v0_2 *RGAM* ontology file in the accessible tree (see §3).
- The v0.3 prompt is untouched (hash in `protected_source_hashes.sha256`).

## 2. Source status

| Source | Path / status | Verification |
|---|---|---|
| David's V6 manuscript | `Enviados/Artigo v6/draft v6  Law_and_Governance_Architectures_Revised.docx` — original, unmodified | **Read in full** (single extraction to session scratchpad, 507 blocks). SHA-256 recorded. |
| V6 PT-BR translation | `Bibliografia/REG_GOV/…v6_Traducao_Integral_PTBR.pdf`, `Enviados/Artigo v6/…` | Located; **not read**. |
| Earlier V1 manuscript context | `AUTONOMOUS_ROTEM_COMPARISON_…/01_BASELINES/derived_text/DAVID_MANUSCRIPT_CONTEXT.md` | Read. It is the **V1** (eight dimensions), *not* V6 (twelve). Not used as V6 evidence. |
| Rotem's codebook (revised) | `…/01_BASELINES/derived_text/CODEBOOK_REVISED.md` | **Read only the `architecture_configuration` entries** (lines 195–196). Not otherwise reviewed. Not modified. |
| Seidl & Kosti (2026) | `RELATIONAL_LEXIMETRICS_PILOT/PILOT_01/00_SOURCES/seidl-kosti-paper-4-with-appendix.pdf` | Read: abstract, §3, §5 validation table, §7 limitations. Appendix not read. |
| Four AI-assisted analytical documents forwarded by David | **Not found** in the repository (searched `RELATIONSHIP_MAP`, `architecture_configuration`; only a legacy figure `fig3_rit_relationship_map.png` and Rotem codebook entries match) | **Documentary verification PENDING.** Their six recommendations are taken from Igor's message and are *not* attributed to named documents. |
| `RELATIONSHIP_MAP` | No file or definition located | **PENDING.** Treated as a *proposed bridge construct* described by Igor; the RGAM treatment (§5 of the ontology) is our own specification, not a recovered definition. |
| Abbott, Levi-Faur & Snidal (2017); Stratmann et al. (2026) | Not accessible locally | Cited only as named by V6 / the handoff; `[CITATION CHECK]`. No novelty claim. |
| Hillier & Hanson; Bhaskar; Orlikowski; Leonardi; Archer; Sayer; Latour | No local copies | Cited from general scholarly knowledge only, scope not verified against the primary text: `[CITATION CHECK]`. |
| v0.4 theoretical alignment protocol | Not a repository file | Reconstructed from the handoff messages — see `EXECUTION_ADDENDUM_v0_4.md` (explicitly *not* a verbatim original). |

## 3. Historical audit materials (copied, content-identical)

Copies in `RGAM/historical_audit_copy/`; SHA-256 of copies equals originals (`historical_audit_copy.sha256` vs `validation_originals.sha256`: identical).

| File | Content (as verified) | Note for v0.4 |
|---|---|---|
| `CLAIM_SOURCE_MATRIX.md` | 24 claims (C01–C24) | Audited against V6 ¶ locators of the *derived context extraction*; some locators may follow the V1 numbering. Re-locate before citing. |
| `ONTOLOGY_STRESS_TEST.md` | 16 invented hypotheticals (S01–S16) | Reused; materiality delta is **Phase 2**. |
| `MANUSCRIPT_V6_TRACKED_EDITS.md` | Editorial suggestions on V6 | Suggestions only; V6 original untouched. |
| `V0_2_REVISION_PLAN.md` | Records that `AGENTS.md`, `theory/`, `references/`, `scripts/validate_repository.py` were never found | Still true in the parent repository. |

## 4. Known gaps carried forward

1. `scripts/validate_repository.py` absent → **NOT RUN — SCRIPT ABSENT**. Phase 1 consistency was checked manually (§5).
2. No bibliography file; every external reference is `[CITATION CHECK]`.
3. The four David-forwarded AI documents and RELATIONSHIP_MAP are unlocated (PENDING).
4. The V6 DOCX was not diffed against the earlier V1; V6 is the sole conceptual baseline.

## 5. Manual consistency checks run in Phase 1

- Twelve V6 categories confirmed against V6 headings and tables (§§3.1–3.5, 4.1–4.3, 5.1–5.3 + relationships block before §4).
- Every ontology element in `ontology/ONTOLOGY_v0_4.md` is traceable either to a V6 section, to the Hillier–Hanson / critical-realist layer (flagged `[CITATION CHECK]`), or marked "RGAM proposal".
- These checks test internal consistency only; they do not validate the ontology.

## 6. Outputs of Phase 1

`00_ADMIN/EXECUTION_ADDENDUM_v0_4.md` · `theory/DAVID_TO_ARCHITECTURAL_ONTOLOGY_CROSSWALK.md` · `theory/THEORETICAL_SELECTION_MATRIX_v0_4.md` · `theory/MATERIALITY_CRITICAL_REALISM_NOTE_v0_4.md` · `ontology/ONTOLOGY_v0_4.md` · `handoff/00_ONTOLOGY_AT_A_GLANCE_v0_4.md`
