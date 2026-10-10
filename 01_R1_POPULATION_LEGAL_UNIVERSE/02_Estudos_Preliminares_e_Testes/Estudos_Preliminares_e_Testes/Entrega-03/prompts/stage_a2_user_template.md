Template variables (filled by scripts/run_stage.py from
screening_v3.py's paragraph extraction — one call per provision):

- {{PROVISION_ID}} — e.g. the source_celex + article + paragraph index
- {{PROVISION_TEXT}} — the single paragraph's text, verbatim

---

Provision ID: {{PROVISION_ID}}

Provision text:
"""
{{PROVISION_TEXT}}
"""

Evaluate this single provision per your instructions. Respond only in the
required schema.
