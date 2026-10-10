# V8 operational codebook

**Status legend:** `V8_DEFINED` = defined directly in V8; `OPERATIONAL_SPECIFICATION` = project field/rule implementing a V8 concept; `METHOD_HYPOTHESIS` = additional architectural-method proposition needing assessment.

## Evidence and direct coding

| Object | Status | Minimum rule |
|---|---|---|
| Documentary source/version; legal unit; institutional statement | OPERATIONAL_SPECIFICATION | Preserve CELEX/source, version, location, exact text and provenance. One provision can yield several statements. |
| Governance object | V8_DEFINED | Record the behaviour, entity, process, relation or arrangement governed. |
| Actor / situated position | V8_DEFINED + OPERATIONAL_SPECIFICATION | Record the legal actor/category and, where supported, jurisdiction, temporal scope and role. Do not invent an instance from a generic actor class. |
| Function | V8_DEFINED | What governance work is performed: rule-making, implementation, interpretation, information, monitoring, verification/assurance, enforcement, adjudication, remediation, or evidence-supported equivalent. |
| Mechanism | V8_DEFINED | How influence operates. Do not equate it with a function or device. Use `uncertain_boundary` where the text does not support separation. |
| Instrument | V8_DEFINED | Concrete legal/institutional device: e.g., authorisation, audit, register, code, certification, complaint procedure. It may organize several functions/mechanisms. |
| Qualified relationship | V8_DEFINED + OPERATIONAL_SPECIFICATION | Record only where parties and a governance-relevant connection are evidenced, directly or through stated cross-provisions. Store type, direction, modality, condition, evidence and attributes. |
| Normative assignment without counterpart | OPERATIONAL_SPECIFICATION | Preserve as an institutional statement/assignment. It is not automatically an actor-to-actor relation. |

## Relational attributes

| Attribute | Status | Operational treatment |
|---|---|---|
| Authority | V8_DEFINED | Record legally consequential capacity and its function: rule-making, authorization, supervision, review, sanction, or other text-supported power. |
| Discretion | V8_DEFINED | Record function-specific range, specificity/constraint, conditionality, reviewability and justification where text supports them. Do not infer discretion from job title. |
| Accountability | V8_DEFINED + OPERATIONAL_SPECIFICATION | Decompose actor, forum, object, information, explanation/justification, assessment/judgment and consequence. Reporting alone is information, not automatic accountability. |

## Higher-order constructs

| Construct | Status | Rule |
|---|---|---|
| Regulatory strategy | V8_DEFINED | Infer from patterned mechanisms/intervention, not one clause. Multiple strategies can coexist. |
| Governance configuration | V8_DEFINED + OPERATIONAL_SPECIFICATION | A stated combination of relations, elements and attributes organized around a function, stage or problem. Membership may overlap. |
| Governance architecture | V8_DEFINED + METHOD_HYPOTHESIS | A higher-order claim from configurations under the inference protocol; never a default property of the whole statute. |
| Governance logic | V8_DEFINED | Infer from coordination/authority patterns after lower-level coding; allow hybrid or competing logics. |
| Regulatory regime | V8_DEFINED | Broad higher-order system. A candidate regime is not presumed from document membership. |
| Regime relation | V8_DEFINED + OPERATIONAL_SPECIFICATION | Store many-to-many relations and evidence for nested, embedded, layered, overlapping, cross-cutting, coupled, constitutive, meta-regulatory, complex or latent claims. |

## Quality states

Every record carries `coding_status` (`direct_text`, `cross_provision_inference`, `machine_candidate`, `human_review_needed`, `deferred`) and `claim_level` (`textual`, `statement`, `relation`, `configuration`, `architecture`, `regime`, `operational`). Higher-level states cannot be assigned as if directly stated by the legal text.

## Coordination and interoperability

This codebook is a bridge specification, not a replacement for any existing coding instrument. Its minimum interoperable layer is the provision-linked institutional statement and its parties, action, modality, object and evidence link. A crosswalk to another dataset should retain the source record unchanged, record the mapping as a separate many-to-many link, identify information lost or added, and never overwrite the originating codebook. The added architectural layer—qualified relations, configurations, property bearers, boundaries and inference records—can therefore be evaluated alongside existing relational-leximetric observations without claiming that all projects use identical units or thresholds.
