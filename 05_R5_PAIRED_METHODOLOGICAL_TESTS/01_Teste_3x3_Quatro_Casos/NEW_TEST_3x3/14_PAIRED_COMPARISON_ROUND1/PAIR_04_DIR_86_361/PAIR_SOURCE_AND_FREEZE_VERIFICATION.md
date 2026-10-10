# Pair source and freeze verification — Council Directive 86/361/EEC — initial stage of mutual recognition of type approval for telecommunications terminal equipment

Run `CMP-R1-DIR-20261007` · 2026-10-07T10:09:25-03:00

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
| Common corpus register hash | `d3f55bd448695b2a5e2c5f9f9167f7f5027c9a80c609a80072439756e80d8c57` |
| Recomputed hash of frozen source file | `d3f55bd448695b2a5e2c5f9f9167f7f5027c9a80c609a80072439756e80d8c57` |
| V8 recorded controlling-source hash | `d3f55bd448695b2a5e2c5f9f9167f7f5027c9a80c609a80072439756e80d8c57` |
| RGAM W_DECLARATION source_sha256 / hash_match | `d3f55bd448695b2a5e2c5f9f9167f7f5027c9a80c609a80072439756e80d8c57` / Y |
| Source file | `07_COMMON_EXECUTION_CORPUS/CASE-31986L0361/31986L0361_official_en.html` |
| RGAM parsed structure (articles/annexes/recitals) | 12/0/14 |
| **Classification** | **`EVIDENCE_IDENTICAL_CONFIRMED`** |

## Freeze integrity of the two arms

| Arm | Case manifest SHA-256 (recomputed) | Recorded | Match | Listed artefacts re-hashed | Mismatches |
|---|---|---|---|---|---|
| V8 `V8_O_DIR_86_361` | `5ea5f2d2addb251262555d0090ab131c7c14f4c063d5df4a2a0093870d4f9d85` | `5ea5f2d2addb251262555d0090ab131c7c14f4c063d5df4a2a0093870d4f9d85` | YES | 10 of 10 artefacts (4 method-source rows outside the authorised comparator scope were not re-hashed; recorded as MATCH in the V8 manifest) | 0  |
| RGAM `RGAM_O_DIR_86_361` | `3dc9add69f04c3a9e5658c0dc90a4a1b5fe6be348e286aae102c4ba8a6c30b1b` | `3dc9add69f04c3a9e5658c0dc90a4a1b5fe6be348e286aae102c4ba8a6c30b1b` | YES | 25 of 25 | 0  |

No frozen V8, RGAM, preregistration or comparator-policy artefact was modified. Only the neutral common-corpus files and the two frozen arms were read for this pair.

- Note: The RGAM Directive package is the frozen recovery package; its case manifest hash was recomputed and matches the detached record. V8's Directive case manifest and its detached hash use a distinct two-line record format; recomputed hash matches.
