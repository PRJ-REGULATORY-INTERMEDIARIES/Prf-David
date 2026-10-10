# Round-1 family comparison QA report

Created 2026-10-07T10:11:37-03:00 · Comparator claude-sonnet-5-5 (UI: Claude Sonnet 5.5 High; reasoning effort not exposed to executor; user-confirmed High)

| # | Check | Result | Detail |
|---|---|---|---|
| 1 | SCF: case Round-1 package matches its freeze manifest (10 files) and detached hash | **PASS** | manifest 58385c5d32c3146f884d70ccad62b7cf1580de71032290c07331d65d17c35f16; mismatches [] |
| 2 | SCF: all 12 required case artefacts present, none extra | **PASS** | missing []; extra [] |
| 3 | CBAM: case Round-1 package matches its freeze manifest (10 files) and detached hash | **PASS** | manifest 4367527cb358f36763aa86c2a06b7ead2a631e916d4a43793fe0060d604b8875; mismatches [] |
| 4 | CBAM: all 12 required case artefacts present, none extra | **PASS** | missing []; extra [] |
| 5 | AI: case Round-1 package matches its freeze manifest (10 files) and detached hash | **PASS** | manifest 8a6d2f44b057dea894940b0788a33d079824036d9d54adf25b4e005e607fd1e5; mismatches [] |
| 6 | AI: all 12 required case artefacts present, none extra | **PASS** | missing []; extra [] |
| 7 | DIR: case Round-1 package matches its freeze manifest (10 files) and detached hash | **PASS** | manifest fb7e7db35c0b0a7ba42b558ccf00a6d6f6e94677e402e7dbbc9e920fb60149c5; mismatches [] |
| 8 | DIR: all 12 required case artefacts present, none extra | **PASS** | missing []; extra [] |
| 9 | Comparison preregistration manifest unchanged | **PASS** | 0eeab8866b404523012ae39a1ff3e01ea15466ae4ff54a4c49a1a1bcfd2a514a |
| 10 | Comparator amendment 001 manifest unchanged | **PASS** | 866700e7859b8a79cfb1703bf59f391193b0828a514a1ade5e682835c2af159b |
| 11 | V8 family manifest unchanged | **PASS** | 2e0e9e31bd7c4811e020bc62012418dc994d27e1292ef5031a9ecfa4be246818 |
| 12 | RGAM family manifest unchanged | **PASS** | 699bc9f4fef41b79d0aa20c132ffb164195b466ad4cc18dd048b2a3d7595938f |
| 13 | V8 family: 63 listed files re-hashed | **PASS** | mismatches [] |
| 14 | RGAM family: 6 listed files re-hashed | **PASS** | mismatches [] |
| 15 | SCF: V8 and RGAM case manifests unchanged since verification | **PASS** | V8 49090d6e169bee7f…; RGAM 7fd01ed8e0e95616… |
| 16 | CBAM: V8 and RGAM case manifests unchanged since verification | **PASS** | V8 335d01086591a480…; RGAM 84647523b5800816… |
| 17 | AI: V8 and RGAM case manifests unchanged since verification | **PASS** | V8 ede488e5d01594fc…; RGAM 160217c11f2cf5e7… |
| 18 | DIR: V8 and RGAM case manifests unchanged since verification | **PASS** | V8 5ea5f2d2addb2512…; RGAM 3dc9add69f04c3a9… |
| 19 | All four cases completed and frozen before the family package | **PASS** | SCF, CBAM, AI Act, Directive 86/361/EEC |
| 20 | Unique human-review IDs across the family | **PASS** | 56 cards |
| 21 | Master queue = sum of case queues; master identity key covers every card exactly once | **PASS** | 56 / 56 |
| 22 | Matching and difference registers equal the concatenation of the case registers | **PASS** | 264 units; 151 differences |
| 23 | Every unit carries exactly one M1–M7 category (no other value) | **PASS** | M1_SUBSTANTIVE_EQUIVALENT, M2_PARTIAL_OVERLAP, M3_V8_ONLY, M4_RGAM_ONLY, M5_SUBSTANTIVE_CONFLICT, M6_REPRESENTATIONAL_DIFFERENCE_ONLY, M7_NOT_COMPARABLE |
| 24 | Master cards expose no method labels or native record IDs | **PASS** |  |
| 25 | Master queue holds no native references (WITHHELD for all cards) | **PASS** |  |
| 26 | All reviewer decision, confidence, justification, reviewer and date fields blank | **PASS** | 56 cards |
| 27 | No case synthesis category (C-A–C-F), F1–F7 or interpretation label assigned in the family summary (mentions of the prohibition excluded) | **PASS** | matched: ['C-A', 'C-F', 'F1', 'F7'] |
| 28 | No human decision simulated | **PASS** | All queue status = OPEN_AWAITING_HUMAN_ADJUDICATION; adjudication register not created |
| 29 | No frozen comparison rule modified after paired outputs were opened (C0–C4, M1–M7, D1–D8, H1–H11, materiality rule) | **PASS** | Codes imported verbatim in build_pair.py; interpretive choices (materiality operationalisation, clustering of absence claims, blinding) logged in each PAIR_COMPARISON_QA.md |
| 30 | Comparator model unchanged across the four cases | **PASS** | claude-sonnet-5-5 (UI: Claude Sonnet 5.5 High; reasoning effort not exposed to executor; user-confirmed High) |
| 31 | Round-1 outputs confined to 14_PAIRED_COMPARISON_ROUND1; frozen arms and preregistration not written to | **PASS** | family and case manifests re-hashed above |
| 32 | No git operation performed by this run (HEAD still the pre-session commit ae1af32) | **PASS** | HEAD=ae1af32 |
| 33 | Project memory not updated | **PASS** | No write to the memory directory in this run |

## Access-control and integrity incidents (disclosed)

1. **Deny rule on the V8 arm.** A technical deny rule `Read(NEW TEST 3x3/09_V8_BASELINE_EXECUTION/**)` set for RGAM-phase isolation remained in `.claude/settings.local.json` when the paired comparison began. Relative-path access was blocked; absolute-path shell reads of the authorised V8 arm succeeded under explicit user authorisation. After the interruption the user instructed removal of that single rule; it was removed (`ROUND1_TECHNICAL_ACCESS_CONTROL_CORRECTION`); the other 32 deny rules were retained and none was relied on to read a forbidden path. This is an implementation issue, not a comparison-method amendment.
2. **Hash-only access under a forbidden path.** While re-verifying the preregistration manifest (34 `SOURCE`/file entries) a verification script computed SHA-256 digests of five files under `RGAM/V8_ACTIVE/03_METHODOLOGY/` and `RGAM/V8_ACTIVE/05_CONCEPTUAL_ARTICLE/` (the four V8 method protocols and the foundational preprint, as listed in the frozen manifest). Only byte digests were computed (0 mismatches); the content of these files was not opened, read or used in any comparison. The earlier per-case V8 manifest verification deliberately skipped such rows. Reported for transparency; the user may treat this as outside the 'analytical use' prohibition or request re-verification.
3. **V8 manifest schema heterogeneity.** The four V8 case manifests use four different column schemas; an early parser error produced false 'MISSING' lines (`V8_CASE_MANIFEST_SCHEMA_HETEROGENEITY / NO_FREEZE_FAILURE`). The V8 CBAM case manifest has no legal-source row; the identical hash is in its provenance record (`EVIDENCE_IDENTICAL_CONFIRMED_WITH_CBAM_MANIFEST_DOCUMENTATION_ASYMMETRY`).
4. **Interruption recovery.** `COMPARATOR_CONTEXT_CONTINUITY = SAME_CONTEXT_AFTER_INTERRUPTION`; no Round-1 artefact existed at the interruption; see `_RECOVERY_SCF_INTERRUPTION_2026-10-07/`.
5. **Self-correction before freezing.** Two omissions of V8-only propositions (SCF C3.14 'control-intensive' label) and two missing RGAM-side risk flags (CBAM C1.07 omission, C3.05 over-inference) were identified in my own review and corrected before the affected packages were frozen; no frozen package was altered afterward.

## Schema additions (logged; no category or rule changed)

See each `PAIR_COMPARISON_QA.md`: added queue columns (`comparison_level`, `external_evidence_dependency`, `possible_decisions`), blinded native-reference fields, and three files without pre-frozen templates (unit register, long-form dimensions, identity key).

## Methodological cautions carried forward

- False-equivalence risk: M1 units rest on equal legal propositions expressed with different vocabulary; the V8 and RGAM identifier schemes differ and are never used as comparison criteria.
- Segmentation mismatch: RGAM decomposes into statements/relations; V8 groups at claim/relation level; many-to-many mappings were used and 1:1 matching was not forced (see cardinality distribution in each pair QA).
- Architecture-candidate versus supported-architecture: raw RGAM 'A' rows and V8's higher-order inferences are compared as inferences; none is treated as accepted before adjudication (special rule for Directive 86/361).
- D7/D8 'POSSIBLE_*' flags are conditional on open cards; their per-method counts are descriptive and reflect where each arm records a proposition the other does not.
- Materiality was operationalised conservatively but consistently (informational/administrative relations non-material; relations with legal effect, party identity, modality, membership, boundary or stopping level potentially material). A reviewer who disagrees with this operationalisation can re-weight units without changing any M category.
