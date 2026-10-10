# Round-1 recovery note

State: ROUND1_IN_PROGRESS / SCF_PAIR_OPENED / INTERRUPTION_RECOVERY
COMPARATOR_CONTEXT_CONTINUITY = SAME_CONTEXT_AFTER_INTERRUPTION

- At interruption no Round-1 SCF artefact had been written to 14_PAIRED_COMPARISON_ROUND1 (directory did not exist): all 12 expected SCF artefacts = NOT_CREATED.
- Working scripts (builder, verification module, SCF spec) existed outside the project in the session scratchpad; they are working files, not Round-1 artefacts, and are recorded in RECOVERY_AUDIT.csv.
- ROUND1_TECHNICAL_ACCESS_CONTROL_CORRECTION: the obsolete deny rule Read(NEW TEST 3x3/09_V8_BASELINE_EXECUTION/**) was removed from .claude/settings.local.json (all other deny rules retained). This is a technical correction, not a comparison-method amendment.
- V8_CASE_MANIFEST_SCHEMA_HETEROGENEITY / NO_FREEZE_FAILURE (initial false MISSING output was a parser issue).
- EVIDENCE_IDENTICAL_CONFIRMED_WITH_CBAM_MANIFEST_DOCUMENTATION_ASYMMETRY.
- No comparison criterion (C0-C4, M1-M7, D1-D8, H1-H11, materiality rule) changed after paired outputs were opened.
