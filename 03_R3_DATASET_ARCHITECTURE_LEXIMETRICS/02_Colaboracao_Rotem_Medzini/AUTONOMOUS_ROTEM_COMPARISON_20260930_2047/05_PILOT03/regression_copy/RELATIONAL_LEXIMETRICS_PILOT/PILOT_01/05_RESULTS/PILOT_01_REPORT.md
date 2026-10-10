# PILOT_01_REPORT

## Gate classification

**RELATIONAL_MODEL_SUPPORTED_WITH_REVISIONS**

The pilot supports the relational extension as a diagnostic representation, but only with revisions before scaling: structured provision capture, an explicit evidence-confidence state, a controlled function/mechanism distinction, and a policy for unresolved actor categories. The finding is mixed and does not justify changing the production codebook.

## Scope and sample

The source workbook named by the codebook was selected: `dataset_of_EU_regulatory_intermediation.xlsx`. Five already assessed rows were purposively selected: 76/889/EEC, 89/336/EEC, 91/263/EEC, EC 874/2004 and 1781/2006. The sample covers simple assurance, multiple intermediary categories, ongoing surveillance/audit, a multi-intermediary architecture, and an assurance/audit/self-regulatory boundary case.

The sample is not representative. Four of five selected coding rows contain multiple intermediary categories or alternative categories in one flat record. The pilot reconstructs 20 provisional edges from those rows and links each edge to the original workbook record.

## Findings against the required questions

1. **Can current intermediary-level coding be represented without information loss?** Partly. Actor names, functions, devices, provisions, recognition and obligations can be carried forward. Information is not lost if original values and pilot splits are retained. Direct legal text is not available for every selected row, so full legal validation remains incomplete.

2. **One INTERMEDIARY_MAP row: one relationship or several?** Several in the sampled material. A flat row may contain a category bundle, several actions and several devices. The relational representation makes the multiplicity explicit. This is a structural result, not a population estimate.

3. **Does provision anchoring improve traceability?** Yes. P01 and P04 show how article-level references connect an action to a relationship and device. P02/P03/P05 show the cost of missing references: a rich narrative remains difficult to audit.

4. **Are Actor A / Actor B sufficient?** Not for R–I–T. The optional `ACTOR_I` position is necessary when the intermediary is a distinct third actor. Additional recipient/oversight positions may be needed for reporting and consent chains.

5. **Can regulator_context and target_context be separated from identities?** Yes. They are contextual attributes of an edge, not substitutes for actor identities. The same Registry or public authority can occupy different positions across edges.

6. **Does Function × Mechanism work?** It works provisionally but is not yet production-ready. Assurance, validation, testing, monitoring, audit and surveillance can be separated by action/object/device, but current flags sometimes collapse them or use mechanism-like terms as functions.

7. **Which variables are genuinely relational?** Actor A/B/I, orientation, direction, action, object acted upon, function, mechanism, legal device, recipient and relationship type.

8. **Which are act-level?** Act title, instrument type, enactment year, sector, legislation code, corpus status, broad regulatory object and act-level narrative of who regulates.

9. **Which should be derived?** Intermediary status across an act, R–I–T configuration, regulatory strategy, architecture, governance logic and counts of functions/mechanisms.

10. **Can architectures be reconstructed from lower-level relationships?** Plausibly. P04 is the clearest demonstration: Registry, registrars, validation agents, auditor, escrow and ADR edges form a configuration. The inference must remain rule-based and evidence-linked.

11. **Does the proposed sequence work?** Yes as a research workflow: legal text → observed actors/actions/provisions → coded object/function/mechanism/relationship → strategy → architecture → governance logic. The pilot does not test causal or implementation claims.

12. **What is lost by retaining only the intermediary-level unit?** Multiple recipients, separate actions, action order, different objects, reporting direction, legally distinct devices, and the ability to distinguish oversight of the intermediary from work performed by it.

13. **What is duplicated by simply adding relational fields to the flat table?** Act title, sector, regulator context, target context, intermediary name, legal provisions and obligations would repeat across every edge. A normalized evidence and act layer is preferable.

14. **What must change before scaling?** Add structured provision IDs and direct excerpts; define whether function and mechanism are orthogonal; split composite actor cells; formalize `ACTOR_I` plus optional recipient/oversight positions; preserve human/model provenance; and run an intercoder reliability test.

## Evidence and limitations

The pilot is grounded primarily in the existing workbook's normalized statements (`HUMAN_EXISTING`) and the conceptual sources. It does not claim that those statements are verbatim quotations. Missing structured provision references are recorded as issues, not silently repaired. Insurance companies, self-regulatory bodies and enforcement labels are treated cautiously where the source row does not clearly establish a regulatory-intermediary relationship.

No production file was altered. No new mechanism category was introduced into production. All pilot values are labeled `MODEL_PILOT` or `DERIVED_RULE`, and unresolved matters are in `PILOT_01_ISSUE_REGISTER.csv`.

## Recommended Next Step

**A. Refine the schema and conduct PILOT_02**, with a small blind/manual provision-retrieval exercise on the same five cases. PILOT_02 should test whether two independent coders can reproduce the action/function/mechanism splits and whether direct provision excerpts reduce the current uncertainty. Only after that should selected relational elements be considered for integration into the existing codebook.
