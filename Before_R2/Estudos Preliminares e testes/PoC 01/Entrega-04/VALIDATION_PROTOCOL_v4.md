# Validation protocol v4

The delivery has five acceptance groups:

1. **Source integrity:** five CELEX records, required version fields, file
   existence and SHA-256 equality.
2. **Screening reproducibility:** five-act coverage, four-act regression
   counts, provision-level evidence and orthogonal ontology fields.
3. **Relational data integrity:** valid actor foreign keys, pairwise-distinct
   R/I/T, literal evidence, no negative/conditional promotion and explicit
   human approval on authoritative rows.
4. **AI provenance:** stage-schema validation, run ids, hashes, timestamps,
   cost metadata and A2 output-to-run links.
5. **Review and deferral controls:** expected auxiliary tables, explicit
   pending/dry-run status and no deferred index presented as measured.

Run `python scripts/validate_v4.py`. The script validates the generated
artifacts without treating dry-run placeholders as findings.

Researcher adjudication is not independent validation. A second coder and a
pre-registered comparison would be needed for intercoder reliability or an
AI-versus-human performance estimate. Those claims are deferred.
