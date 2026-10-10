# V8 pilot coding decisions

1. Unit IDs use `GDPR.A{article}.P{paragraph}` and optional `.pt{point}`. Points remain linked to their parent paragraph.
2. The 2018 corrigendum is applied through a deterministic verified parser; the correction log is retained in `01_SOURCES/`.
3. A lexical screen marks `candidate_governance_relevant` without asserting a legal category or a relation.
4. Curated records distinguish direct institutional statements, normative assignments and qualified relationships.
5. Cross-provision relations cite all needed provisions and use `cross_provision_inference` status.
6. Architecture/regime/logics are derived only in reconstruction documents, never stored as direct provision facts.
7. External instruments, national law and operational evidence remain outside the declared corpus unless explicitly added by a future boundary decision.
