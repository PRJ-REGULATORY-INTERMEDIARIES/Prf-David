# CODING_RULES_V0_3_ADJUDICATED

These rules incorporate H_001–H_019. The pre-adjudication rules and outputs remain preserved.

1. **Action-recipient matching.** `ACTOR_A + ACTION_VERBATIM + OBJECT + ACTOR_B` must match the legal text. A qualifier such as `designated` does not make the qualified actor the recipient of `inform` (H_006, H_011).
2. **One primitive edge per legally distinct directional action.** A change in actor, recipient, direction, legally expressed action, or legally relevant object normally creates a new edge (H_001, H_005, H_015, H_017).
3. **Composite provisions.** Use `COMPOSITE_CANDIDATE` when valid legal moves were compressed; decompose into elementary edges without treating the provision as uncertain (H_001, H_005, H_015, H_017).
4. **Legal effects.** Exemptions, eligibility and conditional authorization are recorded as `LEGAL_EFFECT` unless the text supports an actor-to-actor action. Do not create `enable`, `allow` or `grant` edges from legal effects alone (H_007).
5. **Modality.** Preserve `shall`, `may`, conditional triggers and optional Member-State implementation. A legally possible position is not an effectively instantiated relationship (H_002, H_004).
6. **Action normalization.** Normalize only after Actor A and Actor B are correct. If the candidate edge is invalid, use `NOT_APPLICABLE_TO_CANDIDATE_EDGE` or leave normalization unresolved (H_008).
7. **Intermediary status.** It is a relational position, never a permanent actor attribute. Insurance or required support services, co-occurrence, and conditional safeguards alone do not establish direct or derived status (H_002, H_004, H_009, H_010, H_018, H_019).
8. **Evidence versus candidate construction.** `UNRESOLVED` means the specific candidate lacks sufficient support; it does not mean the whole act is uncertain. `NEITHER` preserves a corrected value when both options are wrong (H_006–H_011, H_016).
9. **Function × Mechanism × Device.** For the tested Annex III point 3.3 provision, use `assurance`, `quality_system_assessment`, and `quality-system assessment`. Do not generalize this label to all conformity provisions; distinguish it from later periodic surveillance (H_012–H_014).
10. **Outcome vocabulary.** Preserve `UNRESOLVED`, `COMPOSITE_CANDIDATE`, `BOTH_IN_PART`, and `NEITHER`; none may be silently forced into a binary agreement result (H_001, H_008, H_015, H_016, H_017).
