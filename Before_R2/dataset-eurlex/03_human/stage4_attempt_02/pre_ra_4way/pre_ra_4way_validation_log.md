# Pre-RA four-way validation log

Date (local, date only): 2026-09-07
Comparator version: 1.0.0
Status: **PASS**

## Automated checks

- PASS — each of the four validated outputs contains exactly 90 unique candidate IDs.
- PASS — all four outputs contain exactly the same 90 IDs as the frozen R1/R2 coding input; no new ID exists.
- PASS — all protected files match the SHA-256 baseline recorded before generation.
- PASS — `cross_model_comparison.csv` contains exactly 90 data rows in frozen-input order.
- PASS — the positive union was recomputed from current validated outputs, not hardcoded.
- PASS — no RA output, human-gate output, or benchmark artifact was created.
- PASS — all files written by this operation are inside `pre_ra_4way/`.
- PASS — principal signature ignores actor.role and excluded free-text fields.
- PASS — principal signature ignores screening_status and confidence.
- PASS — explicit aliases and conservative textual normalization collapse wording-only variants.
- PASS — condition and actor-identity changes remain substantive disagreements.
- PASS — no fuzzy matching is implemented.

## Protected-file SHA-256 verification

| protected path | expected | observed |
|---|---|---|
| `02_corpus/act.md` | `b24a02ea241ca631b606660bb48bb5a2222b29f849c4e4552fb99f871b2e8fd4` | `b24a02ea241ca631b606660bb48bb5a2222b29f849c4e4552fb99f871b2e8fd4` |
| `03_human/stage4_attempt_02/R1_coding_input.json` | `813b984c5e80aa03c98bc4399f40644c7d802eedd45f55a2d7a9a787a82d0b38` | `813b984c5e80aa03c98bc4399f40644c7d802eedd45f55a2d7a9a787a82d0b38` |
| `03_human/stage4_attempt_02/R1_output.json` | `af443a0f98307a9d989816c5f0e15d4aa009553174eb470753f4134cb6640f29` | `af443a0f98307a9d989816c5f0e15d4aa009553174eb470753f4134cb6640f29` |
| `03_human/stage4_attempt_02/R1_output_raw.json` | `af443a0f98307a9d989816c5f0e15d4aa009553174eb470753f4134cb6640f29` | `af443a0f98307a9d989816c5f0e15d4aa009553174eb470753f4134cb6640f29` |
| `03_human/stage4_attempt_02/R2_coding_input.json` | `813b984c5e80aa03c98bc4399f40644c7d802eedd45f55a2d7a9a787a82d0b38` | `813b984c5e80aa03c98bc4399f40644c7d802eedd45f55a2d7a9a787a82d0b38` |
| `03_human/stage4_attempt_02/R2_output.json` | `18855b2053447d061be3c1fcfae9ebdbd579620d922a6394223f57b0f21ad2f6` | `18855b2053447d061be3c1fcfae9ebdbd579620d922a6394223f57b0f21ad2f6` |
| `03_human/stage4_attempt_02/R2_output_raw.json` | `18855b2053447d061be3c1fcfae9ebdbd579620d922a6394223f57b0f21ad2f6` | `18855b2053447d061be3c1fcfae9ebdbd579620d922a6394223f57b0f21ad2f6` |
| `03_human/stage4_attempt_02/candidate_reconstruction.json` | `38416b70f9337ad66dbd6c6d41d280d18ad9e5694e0cacb0c938c5833b1aff55` | `38416b70f9337ad66dbd6c6d41d280d18ad9e5694e0cacb0c938c5833b1aff55` |
| `03_human/stage4_attempt_02/claude_replication_01/Claude_R1_output.json` | `86cf2af470fad31165efd0af8ac1cb02fa77c20b6bacad265a40601d5611e2e5` | `86cf2af470fad31165efd0af8ac1cb02fa77c20b6bacad265a40601d5611e2e5` |
| `03_human/stage4_attempt_02/claude_replication_01/Claude_R1_output_raw.json` | `f997f3d763836887d858528e78ac3753be9fb0dfe23bfd0fa0bf885ea4870daa` | `f997f3d763836887d858528e78ac3753be9fb0dfe23bfd0fa0bf885ea4870daa` |
| `03_human/stage4_attempt_02/claude_replication_01/Claude_R2_output.json` | `cfea747db3441279cb4293092a7cc9435434bb967880ae0f5404e1b401f5a06e` | `cfea747db3441279cb4293092a7cc9435434bb967880ae0f5404e1b401f5a06e` |
| `03_human/stage4_attempt_02/claude_replication_01/Claude_R2_output_raw.json` | `e9cecdb87207a636d94b54e5e86e4d099986bac77fcb6428844b2631a5844df5` | `e9cecdb87207a636d94b54e5e86e4d099986bac77fcb6428844b2631a5844df5` |
| `03_human/stage4_attempt_02/validate_reference_logic.py` | `b502413da838f1b447ab67b49fe073ab0a1d6a076fe86a9298d9d4a021ff998d` | `b502413da838f1b447ab67b49fe073ab0a1d6a076fe86a9298d9d4a021ff998d` |
| `methodology/v1.1.0/codebook.md` | `c160e153907a786c04070cb09f6e9baa11de709a4432a5f89ebe375a8a7eb472` | `c160e153907a786c04070cb09f6e9baa11de709a4432a5f89ebe375a8a7eb472` |
| `methodology/v1.1.0/experimental_output_schema.json` | `aaa0c351836120cadef86d051ef8d950675577afbabefd5ac5d3931f33ae875c` | `aaa0c351836120cadef86d051ef8d950675577afbabefd5ac5d3931f33ae875c` |
| `methodology/v1.1.0/methodology_manifest.yaml` | `4bb92019f932a836707d81d087503b60913b3770cdc3881b05fc0662d036fb00` | `4bb92019f932a836707d81d087503b60913b3770cdc3881b05fc0662d036fb00` |
| `methodology/v1.1.0/reference_coding_schema.json` | `abbc4325a5e749cf31836fb24314c27ed22061d6e6539fb435fce8236d5ad2ec` | `abbc4325a5e749cf31836fb24314c27ed22061d6e6539fb435fce8236d5ad2ec` |
| `methodology/v1.1.0/strings.yaml` | `242c288db010320619a0cdb58c38cb73c6be8aa499497ccfae7bfbfc33f34305` | `242c288db010320619a0cdb58c38cb73c6be8aa499497ccfae7bfbfc33f34305` |

## Derived selection checks

- Positive union count: 4
- Positive union IDs (derived): CAND2-11BF388480EA, CAND2-27E84BD23730, CAND2-465FC96778A7, CAND2-88A2261C68DE
- Current pre-RA human-gate queue count (rules 1–7 plus rule 10): 21
- Rule-10 audit sample count: 8
- Rule-10 audit sample IDs: CAND2-0E374F1C7A4C, CAND2-474D6A7B8FCA, CAND2-5891C83730AB, CAND2-937128584EE2, CAND2-A1B35C3F8A0A, CAND2-E5D1DF913444, CAND2-EC26B7CB9612, CAND2-F5D039301252
- Audit ranking seed: `14247a36cdaf03030cde50e5ffc6a11627d78dd33a0bd45b7b3fbb3d879e42fa`
- RA-dependent rules 8–9: not evaluated because RA does not exist.

## Explicit non-actions

RA_NOT_EXECUTED

HUMAN_GATE_NOT_EXECUTED

BENCHMARK_NOT_LOCKED
