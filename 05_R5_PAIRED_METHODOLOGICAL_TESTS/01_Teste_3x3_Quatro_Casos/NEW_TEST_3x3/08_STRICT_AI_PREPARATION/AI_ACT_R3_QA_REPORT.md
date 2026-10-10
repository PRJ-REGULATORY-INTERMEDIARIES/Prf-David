# AI Act R3 pre-analytical extraction — QA report

## Result

Status: `PRE_ANALYTICAL_RELATIONAL_BASELINE`. The restricted scan records 26 legally named actor classes, 8 regulator-role classes, 5 intermediary classes, 8 regulated target/operator classes in the actor register, 12 retained relation records, and 5 supported regulatory intermediation relations. It preserves three uncertain relation candidates and four not-supported candidates. These are descriptive results from the full official instrument and were generated after case selection.

## Gate applied

The frozen R3 Phase 6 gate was applied without adding a new definition: C1 identifiable regulator-target relation; C2 distinct institutionalized third party; C3 demonstrable mediating function. All three affirmative conditions are required for `SUPPORTED_INTERMEDIATION`. Direct R-T, legal relations that are not RIT, uncertainty, and non-support remain separate statuses. Advice, expertise, consultation, institutional presence, and information exchange alone are not treated as intermediation. The coding unit is the adjudicated relation record in `AI_ACT_R3_RELATION_REGISTER.csv`; repeated provisions supporting one legally coherent relation are grouped, while separate actor role pairs are not collapsed.

## Count interpretation and limits

Actor totals count actor classes registered in the accompanying actor register, not individual organizations, persons, every mention in the act, or a reconstructed governance architecture. Regulator and target totals are role-class counts and may overlap with other roles. The relation count is the number of register rows marked retained, including supported, direct, legal-non-RIT, and uncertain rows; it is not a positive RIT count. Only five rows are positive RIT. The boundary register includes eight disposition records; these are not an additional relation denominator, and its rows cross-reference the relation register.

The positive count is deliberately conservative. Articles 40, 69 and 77 preserve real boundary questions around standardisation, expert support, and fundamental-rights authority requests. They are not counted as supported RIT. The extraction is a standardized relational baseline only: no architecture, actor centrality, mechanisms, accountability, policy outcome, V8 or RGAM inference was performed. This file does not reproduce prior R3 empirical rows; it applies only the frozen gate to the fresh AI Act source.

## Non-circularity and provenance

The AI Act was selected on `UNIQUE_ELIGIBLE_AI_SPECIFIC_CASE` before this new count was generated. The count is labelled `PRE_ANALYTICAL_RELATIONAL_BASELINE`, not `CASE_SELECTION_EVIDENCE`. Source identity, retrieval and hash are in `AI_ACT_SOURCE_MANIFEST.csv`; the full-source recovery narrative is in `AI_ACT_SOURCE_RECOVERY_REPORT.md`. The extraction and source were frozen separately by `AI_ACT_R3_FREEZE_MANIFEST.csv` and its SHA-256 companion.

The gate source is the prior R3 Phase 6 audit at `R4_CROSS_DOMAIN_VALIDATION/01_baseline/R3_HISTORY_STAGING/PRJ-DAVID-R3/R3_CLEANROOM/12_audits/R3_PHASE_6_INTERMEDIATION_AUDIT.md`, with operational detail in the adjacent `R3_CLEANROOM_OPERATIONAL_PROMPT.md`. These are cited as rule provenance only. No prior R3 empirical relationship rows were used as AI Act evidence; the evidence for each new relation is the cited provision of the freshly recovered AI Act itself.
