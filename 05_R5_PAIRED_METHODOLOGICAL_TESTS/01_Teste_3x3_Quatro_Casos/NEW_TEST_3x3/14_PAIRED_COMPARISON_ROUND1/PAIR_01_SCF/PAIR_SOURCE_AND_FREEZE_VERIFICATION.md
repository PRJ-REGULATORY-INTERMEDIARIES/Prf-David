# Pair source and freeze verification — Regulation (EU) 2023/955 — Social Climate Fund

Run `CMP-R1-SCF-20261007` · 2026-10-07T09:46:40-03:00

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
| Common corpus register hash | `cf8c60fc233311436dfdd3ee236d0c8399eda55fea174610e91b5594f84a0408` |
| Recomputed hash of frozen source file | `cf8c60fc233311436dfdd3ee236d0c8399eda55fea174610e91b5594f84a0408` |
| V8 recorded controlling-source hash | `cf8c60fc233311436dfdd3ee236d0c8399eda55fea174610e91b5594f84a0408` |
| RGAM W_DECLARATION source_sha256 / hash_match | `cf8c60fc233311436dfdd3ee236d0c8399eda55fea174610e91b5594f84a0408` / Y |
| Source file | `07_COMMON_EXECUTION_CORPUS/CASE-32023R0955/32023R0955_official_en.html` |
| RGAM parsed structure (articles/annexes/recitals) | 29/5/47 |
| **Classification** | **`EVIDENCE_IDENTICAL_CONFIRMED`** |

## Freeze integrity of the two arms

| Arm | Case manifest SHA-256 (recomputed) | Recorded | Match | Listed artefacts re-hashed | Mismatches |
|---|---|---|---|---|---|
| V8 `V8_C1_SCF` | `49090d6e169bee7f178b89580e042882a550824939b6f636e96ec3d3f652b547` | `49090d6e169bee7f178b89580e042882a550824939b6f636e96ec3d3f652b547` | YES | 10 of 10 artefacts (4 method-source rows outside the authorised comparator scope were not re-hashed; recorded as MATCH in the V8 manifest) | 0  |
| RGAM `RGAM_C1_SCF` | `7fd01ed8e0e95616c8dfb836694e00f29c5887f04b24f0f483b2220b15ef3f65` | `7fd01ed8e0e95616c8dfb836694e00f29c5887f04b24f0f483b2220b15ef3f65` | YES | 25 of 25 | 0  |

No frozen V8, RGAM, preregistration or comparator-policy artefact was modified. Only the neutral common-corpus files and the two frozen arms were read for this pair.

- Note: V8 SCF case manifest lists four method-source rows (V8 manuscript, three V8_ACTIVE method files) recorded MATCH in the V8 manifest; they lie outside the comparator's authorised read scope and were not re-hashed.
