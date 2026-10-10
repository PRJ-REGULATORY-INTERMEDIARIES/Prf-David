# PILOT_02_REPORT

## Gate

**RELATIONAL_MODEL_RELIABILITY_SUPPORTED_WITH_REVISIONS**

This gate applies to procedural model replication, not human intercoder reliability. The two passes were labeled `MODEL_INDEPENDENT_A` and `MODEL_INDEPENDENT_B`; no human pair was available.

## Design

The same five PILOT_01 cases were used: 76/889/EEC, 89/336/EEC, 91/263/EEC, EC 874/2004 and 1781/2006. The source-first pass began with 17 official EUR-Lex provisions and 17 candidate relationship slots. The current workbook and PILOT_01 outputs were consulted only as methodological context and were not treated as legal evidence.

## Answers to the research questions

1. **Can two independent codings identify substantially the same relationships?** Mostly, at the level of candidate provision/action existence. Relationship-existence raw agreement was 0.941 (16/17). The agreement is not sufficient to claim stable fine-grained coding because actor positions, function/mechanism and intermediary status generate systematic disagreements.

2. **Which variables have high agreement?** Provision-linked case identity, act identifier, legal location and most basic actor/action/object fields have high agreement. The variable-level table reports the exact counts rather than collapsing them into one reliability number.

3. **Which variables generate systematic disagreement?** `ACTOR_I`, relationship type, function, mechanism and intermediary status. Ternary versus binary representation is the dominant schema disagreement.

4. **Main source of disagreement?** Mixed: schema ambiguity for ACTOR_I and R–I–T; ontology overlap for assurance/monitoring/audit; source ambiguity for insurance and Article 18's conditional audit/supervision; normalization ambiguity for legal actor categories.

5. **Does direct provision capture reduce uncertainty?** Yes. It resolves the missing-reference problem found in PILOT_01 and allows the pilot to reject at least one prior overextension: P05 Article 18 is a statutory condition, not automatically an intermediary relationship. Direct text does not by itself solve ontology boundaries.

6. **Is Function distinguishable from Mechanism?** Provisionally. Action, governance work, means and device can be separated in P01, P03 and P04. The distinction is not yet reproducible enough for an unqualified production taxonomy.

7. **Is Device/Instrument necessary?** Yes. Certificates, audit reports, documentary evidence, escrow agreements and ADR procedures carry legal effects that would be lost if function and mechanism were the only fields.

8. **Is ACTOR_I necessary as a primitive?** No, not always. It is useful in a derived R–I–T view, but the binary graph preserves evidence better in the tested cases.

9. **Is R–I–T better derived compositionally?** Yes. Model B reduces duplication and avoids inferring a combined ternary relation from provisions that legally express separate edges.

10. **Can intermediary status be derived?** Partly. It is strongly supported where an actor occupies a distinct connected position in a legally constituted configuration. It remains unresolved for supporting devices and conditional oversight actors, especially P02 insurance and P05 audit/supervision.

11. **PILOT_01 issues resolved?** Structured provision traceability is materially improved; the need for role-specific identities is confirmed; the unit-of-observation problem is clarified in favor of elementary binary edges.

12. **PILOT_01 issues unresolved?** Function × mechanism boundary, intermediary status for insurance/oversight, modality granularity, and human intercoder reliability remain unresolved.

13. **New issues:** direct legal text can support several equally defensible relation cuts; a derived R–I–T configuration needs a formal edge-linking rule; legal category labels and normalized actor identities need separate fields.

14. **Stable for a larger pilot?** Stable enough for a larger *reliability* pilot using the binary core, but not stable enough for corpus-wide recoding or production integration.

## Limitations

The sample is purposive and small. The two passes are simulated model independence, not independent human coders. Raw agreement is therefore a reproducibility diagnostic. Cohen's kappa values are reported descriptively where computable, but prevalence and sample size make them unsuitable as a sole decision rule.

## Recommended next step

Run a human-adjudicated PILOT_03 or a larger duplicate-coding exercise using the binary/compositional core, with direct provision excerpts and a preregistered rule for linking R–I and I–T edges into derived R–I–T configurations. Do not modify production until human agreement is tested.
