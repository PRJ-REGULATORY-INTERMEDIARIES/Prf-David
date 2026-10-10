Template variables (filled by scripts/run_stage.py):

- {{CANDIDATE_ID}}
- {{FULL_ARTICLE_TEXT}} / {{CROSS_REFERENCED_TEXT}} / {{KNOWN_CROSS_ACT_TEXT}}
  — same legal-context package given to Stage B1
- {{STAGE_B1_OUTPUT_JSON}} — the full JSON output from this same
  candidate's Stage B1 run

---

Candidate ID: {{CANDIDATE_ID}}

Legal-context package (same as supplied to the architecture-reconstruction
step):
"""
{{FULL_ARTICLE_TEXT}}

{{CROSS_REFERENCED_TEXT}}

{{KNOWN_CROSS_ACT_TEXT}}
"""

Stage B1 architecture reconstruction (actors and relations, no roles
assigned yet):
{{STAGE_B1_OUTPUT_JSON}}

Apply the five-condition relational test per your instructions. Respond
only in the required schema.
