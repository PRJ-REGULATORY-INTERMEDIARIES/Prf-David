# Pair source and freeze verification — Regulation (EU) 2024/1689 — Artificial Intelligence Act

Run `CMP-R1-AI-20261007` · 2026-10-07T10:04:15-03:00

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
| Common corpus register hash | `8f0b656302f9864cc87e040c371f209a9d65ae1a6cecc25ca5eb737e872d721a` |
| Recomputed hash of frozen source file | `8f0b656302f9864cc87e040c371f209a9d65ae1a6cecc25ca5eb737e872d721a` |
| V8 recorded controlling-source hash | `8f0b656302f9864cc87e040c371f209a9d65ae1a6cecc25ca5eb737e872d721a` |
| RGAM W_DECLARATION source_sha256 / hash_match | `8f0b656302f9864cc87e040c371f209a9d65ae1a6cecc25ca5eb737e872d721a` / Y |
| Source file | `07_COMMON_EXECUTION_CORPUS/CASE-32024R1689/32024R1689_official_en.xhtml` |
| RGAM parsed structure (articles/annexes/recitals) | 113/13/180 |
| **Classification** | **`EVIDENCE_IDENTICAL_CONFIRMED`** |

## Freeze integrity of the two arms

| Arm | Case manifest SHA-256 (recomputed) | Recorded | Match | Listed artefacts re-hashed | Mismatches |
|---|---|---|---|---|---|
| V8 `V8_AI_AI_ACT` | `ede488e5d01594fca0690c6c82994c1d24605fa6b42ccd62eacc05807aee007b` | `ede488e5d01594fca0690c6c82994c1d24605fa6b42ccd62eacc05807aee007b` | YES | 10 of 10 artefacts (4 method-source rows outside the authorised comparator scope were not re-hashed; recorded as MATCH in the V8 manifest) | 0  |
| RGAM `RGAM_AI_AI_ACT` | `160217c11f2cf5e70f22a3eb527ac916cb460ce3d9c70a313ae91160e5e15372` | `160217c11f2cf5e70f22a3eb527ac916cb460ce3d9c70a313ae91160e5e15372` | YES | 25 of 25 | 0  |

No frozen V8, RGAM, preregistration or comparator-policy artefact was modified. Only the neutral common-corpus files and the two frozen arms were read for this pair.

- Note: Common-source parity confirmed for the AI Act by the strict-AI final equality check (08_STRICT_AI_PREPARATION/FINAL_COMMON_EVIDENCE_EQUALITY_CHECK.csv); files with prefix AI_ACT_R3_ were not opened.
