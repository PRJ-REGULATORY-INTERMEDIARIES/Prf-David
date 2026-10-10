Template variables (filled by scripts/run_stage.py from a positive Stage B2
output plus the relevant slice of reference/DATA_DICTIONARY_v3.md):

- {{RELATIONSHIP_ID}}
- {{RELATIONSHIP_TEXT}} — the confirmed relationship's legal-context package
- {{R_ACTOR}} / {{I_ACTOR}} / {{T_ACTOR}} — confirmed from Stage B2
- {{REQUESTED_FIXED_FIELDS}} — which of the 8 fixed attributes to code this
  call (usually all 8, but scriptable to a subset)
- {{REQUESTED_DEFERRED_FIELDS}} — which deferred battery field names (if
  any) to propose this call, per the project's own scope discipline (start
  with a small number of directly-observable ones, not the full ~20 at once)
- {{FIELD_DEFINITIONS_EXCERPT}} — the exact DATA_DICTIONARY_v3.md
  definitions, allowed_values, evidence_required, and coding_rule for
  exactly the fields listed above

---

Relationship ID: {{RELATIONSHIP_ID}}

Confirmed: R = {{R_ACTOR}} · I = {{I_ACTOR}} · T = {{T_ACTOR}}

Relationship text:
"""
{{RELATIONSHIP_TEXT}}
"""

Fixed attributes to code this call: {{REQUESTED_FIXED_FIELDS}}
Deferred-battery attributes to propose this call (if any): {{REQUESTED_DEFERRED_FIELDS}}

Field definitions (source of truth — follow exactly):
"""
{{FIELD_DEFINITIONS_EXCERPT}}
"""

Code only the requested fields. Respond only in the required schema.
