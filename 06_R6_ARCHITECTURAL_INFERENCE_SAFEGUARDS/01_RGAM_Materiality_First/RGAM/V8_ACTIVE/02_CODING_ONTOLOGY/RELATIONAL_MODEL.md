# Relational model and traceability

```text
Source ──< LegalUnit ──< InstitutionalStatement ──< Element
                              │                         │
                              ├──< NormativeAssignment   └──< Relationship >── Element
                              │                                      │
                              └────────< RelationEvidence >──────────┤
                                                                     ├──< Attribute
Relationship / Element ──< ConfigurationMember >── Configuration ──< ArchitecturalClaim
Configuration / Architecture ──< RegimeMember >── Regime ──< RegimeRelation >── Regime
Any record ──< Adjudication / Uncertainty
```

The model preserves V8's pivotal relationship without treating every statement as a relation. A relation is typed and can be supported by multiple statements; a statement can support multiple relations. Architectural and regime claims remain downstream of, and recoverable through, their evidence chain.

**Traceability requirement:** architectural claim → configuration → members/qualified relationships and elements → institutional statements → original legal units → source/version.
