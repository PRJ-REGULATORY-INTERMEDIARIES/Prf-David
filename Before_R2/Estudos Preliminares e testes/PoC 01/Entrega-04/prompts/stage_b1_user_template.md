Template variables (filled by scripts/context_package.py):

- {{CANDIDATE_ID}}
- {{SOURCE_ACT_TITLE}} / {{SOURCE_CELEX}} / {{ARTICLE}}
- {{FULL_ARTICLE_TEXT}} — ALL paragraphs under the carrier article, not
  just the single paragraph that triggered Stage A screening
- {{CROSS_REFERENCED_TEXT}} — text of any provisions explicitly
  cross-referenced within the same act, auto-resolved from already-
  downloaded HTML; empty if none apply
- {{KNOWN_CROSS_ACT_TEXT}} — text of pre-fetched cross-act references
  known to matter for this corpus (e.g. Regulation (EC) No 765/2008 Art.
  14, Directive 2006/43/EC); empty if not applicable to this candidate

---

Candidate ID: {{CANDIDATE_ID}}

Source act: {{SOURCE_ACT_TITLE}} (CELEX {{SOURCE_CELEX}}), {{ARTICLE}}

Full article text:
"""
{{FULL_ARTICLE_TEXT}}
"""

Cross-referenced provisions (same act):
"""
{{CROSS_REFERENCED_TEXT}}
"""

Known cross-act reference material (pre-fetched):
"""
{{KNOWN_CROSS_ACT_TEXT}}
"""

Reconstruct the architecture per your instructions. Do not assign R/I/T
roles. Respond only in the required schema.
