# Pair source and freeze verification — Regulation (EU) 2023/956 — Carbon Border Adjustment Mechanism (CBAM)

Run `CMP-R1-CBAM-20261007` · 2026-10-07T09:55:00-03:00

## Comparator and independence attestation (recorded before substantive outputs were opened)

```text
V8_EXECUTION_PARTICIPATION = NO
RGAM_EXECUTION_PARTICIPATION = NO
HUMAN_ADJUDICATION_PARTICIPATION = NO
PREVIOUS_SUBSTANTIVE_V8_EXPOSURE = NO
PREVIOUS_SUBSTANTIVE_RGAM_EXPOSURE = NO
```
- Model: `claude-sonnet-5-5`; UI selection recorded by user: Claude Sonnet 5.5 High (`USER_CONFIRMED_HIGH_MODE = YES`)
- Reasoning/effort setting visible to executor: NOT_EXPOSED; temperature: not exposed; seed: not exposed
- Comparator-policy amendment 001 manifest SHA-256 (verified): `866700e7859b8a79cfb1703bf59f391193b0828a514a1ade5e682835c2af159b`
- Comparison-preregistration manifest SHA-256 (verified): `0eeab8866b404523012ae39a1ff3e01ea15466ae4ff54a4c49a1a1bcfd2a514a`
- V8 family manifest SHA-256 (verified): `2e0e9e31bd7c4811e020bc62012418dc994d27e1292ef5031a9ecfa4be246818`; RGAM family manifest SHA-256 (verified): `699bc9f4fef41b79d0aa20c132ffb164195b466ad4cc18dd048b2a3d7595938f`
- No model deviation (`COMPARATOR_MODEL_DEVIATION` not triggered).

## Common-evidence verification

| Item | Value |
|---|---|
| Common corpus register hash | `c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e` |
| Recomputed hash of frozen source file | `c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e` |
| V8 recorded controlling-source hash | `c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e` |
| RGAM W_DECLARATION source_sha256 / hash_match | `c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e` / Y |
| Source file | `07_COMMON_EXECUTION_CORPUS/CASE-32023R0956/32023R0956_official_en.xhtml` |
| RGAM parsed structure (articles/annexes/recitals) | 36/6/82 |
| **Classification** | **`EVIDENCE_IDENTICAL_CONFIRMED`** |

## Freeze integrity of the two arms

| Arm | Case manifest SHA-256 (recomputed) | Recorded | Match | Listed artefacts re-hashed | Mismatches |
|---|---|---|---|---|---|
| V8 `V8_C2_CBAM` | `335d01086591a48072425ddf48ca0667a4c9667b06d90d9a106c328361078adf` | `335d01086591a48072425ddf48ca0667a4c9667b06d90d9a106c328361078adf` | YES | 10 of 10 artefacts (0 method-source rows outside the authorised comparator scope were not re-hashed; recorded as MATCH in the V8 manifest) | 0  |
| RGAM `RGAM_C2_CBAM` | `84647523b5800816b7d56279383cbbfaaeea95296765e7e171e2329dafe6e096` | `84647523b5800816b7d56279383cbbfaaeea95296765e7e171e2329dafe6e096` | YES | 25 of 25 | 0  |

No frozen V8, RGAM, preregistration or comparator-policy artefact was modified. Only the neutral common-corpus files and the two frozen arms were read for this pair.

- Note: EVIDENCE_IDENTICAL_CONFIRMED_WITH_CBAM_MANIFEST_DOCUMENTATION_ASYMMETRY: the V8 case manifest has no legal-source row; the identical source hash is stated in V8 SOURCE_AND_METHOD_PROVENANCE.md and the source file hash was recomputed here.
