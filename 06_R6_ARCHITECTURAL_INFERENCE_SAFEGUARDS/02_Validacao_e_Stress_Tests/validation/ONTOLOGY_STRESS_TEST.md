# Ontology stress test for v0.2

These are invented hypotheticals for testing the ontology. They are not legal evidence, not claims about any jurisdiction, and not examples from PILOT_03. A test passes only if the schema preserves the text span, actor position, modality, condition, temporal scope, relationship direction, and inference status without silently creating an edge.

| ID | Invented hypothetical | Stress point | Required representation / failure to avoid |
|---|---|---|---|
| S01 | A statute requires an **organization** to appoint an independent officer, but elsewhere gives the officer a distinct reporting position. | Organization vs position | Store organization and officer as separate actors; store “position” as a role occupied in a relationship. Do not merge the organization node with the position node. |
| S02 | A regulator may inspect a facility only if a risk threshold is met and funding is available. | Conditional power | Record a power with trigger conditions and resource condition. Do not code an unconditional inspection relation. |
| S03 | A single clause requires reporting, audit access, and corrective action as one compliance package. | Composite norm | Preserve the source span but decompose into legally distinct primitive actions only when each direction and modality are recoverable. Keep a parent composite identifier. |
| S04 | A board, regulator, auditor, and affected community jointly approve a remediation plan. | N-ary relationship | Represent the approval event as an event node with four participant roles, or as explicitly typed binary projections linked to the same event. Do not invent pairwise approval relations. |
| S05 | A firm is permitted to use a mark if certified, but is not required to seek certification. | Permission vs duty | Code permission and condition; do not infer a duty to certify from a conditional permission. |
| S06 | A regulation expressly prohibits disclosure to a named recipient, while a separate provision is silent about disclosure to another recipient. | Express prohibition vs missing link | Code only the express prohibition. Silence is `NO_EVIDENCE`, not permission, prohibition, or relationship absence. |
| S07 | An authorization lasts until 31 December unless renewed, and renewal requires a new assessment. | Amendment / expiry | Add temporal validity, renewal condition, and version/provision lineage. Do not carry the old relation forward after expiry without an explicit renewal event. |
| S08 | A national authority supervises a regional body, while a sectoral agency supervises the same body for one product class. | Overlapping domains | Attach domain/scope to each relationship. Do not collapse the two supervisors into a single global relation. |
| S09 | A platform must obtain a certificate from an accredited laboratory, but the laboratory may subcontract testing. | Intermediaries | Distinguish direct legal relation from possible operational chain. Subcontracting is not a derived legal edge unless the text establishes it. |
| S10 | A clause says “the authority shall publish guidance” without specifying whether the duty applies nationally or only to a pilot zone. | Local/global ambiguity | Record scope as unresolved and route to adjudication. Do not default to global scope. |
| S11 | A dashboard visualizes reporting relationships but has no legal effect and is not incorporated by reference. | Visualization vs object | Model the dashboard as an information artefact, not as a governed actor, legal object, or legal relationship. |
| S12 | A constitution formally assigns review power to a court, but an administrative rule describes how the review is conducted in practice. | Formal vs enacted governance | Keep formal legal architecture and enacted/implemented arrangement in separate layers. Do not use the practice rule to rewrite the constitutional relation. |
| S13 | A ministry both designates a certifier and receives the certifier’s reports. | Actor position and direction | Use two directed relationships with distinct functions: designation and reporting. “Designated” does not make the ministry the recipient of every related action. |
| S14 | A law says an entity “may consult experts” and separately says it “shall consider” a published expert report. | Permission vs duty, linked objects | Code the optional consultation and the mandatory consideration separately; link them only if the text establishes the dependency. |
| S15 | An exception applies only during an emergency declared by another authority and ends when the declaration is revoked. | Conditional norm and temporal scope | Represent declaration as a trigger event, exception as conditional modality, and revocation as an expiry event. Do not code the exception as a permanent permission. |
| S16 | A professional association writes a standard, certifies members, and is itself audited by a public agency. | Multi-role actor | Preserve one actor with role-specific positions and separate relations. Do not classify it globally as only regulator, intermediary, or target. |

## Decision rules to carry into v0.2

1. Every inferred relation must point back to one or more verbatim source spans and carry `DIRECT`, `DERIVED`, or `NO_EVIDENCE` status.
2. Conditions, exceptions, expiry, and domain are first-class fields, not prose notes.
3. A graph projection is a representation of coded relations, not a legal source and not proof of legal effect.
4. An organization, an institutional position, an event, an object, and a visualization must be different entity types.
5. Missing links remain missing links. They are never converted into permissions, duties, prohibitions, or negative findings by default.

