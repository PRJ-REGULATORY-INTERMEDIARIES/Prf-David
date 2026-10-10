# Validation log

## Source and method checks

- Rotem's position is drawn only from her substantive reply in `Enviados/30_09_26/email e chat` (lines 12–20). The later commentary in that file is not attributed to her. The pasted reply ends with an ellipsis, so any missing tail is unknown.
- The revised codebook is treated as `ROTEM_DOCUMENTED`; the September 2 workbook as `ROTEM_IMPLEMENTED`; the reply as `ROTEM_CONCEPTUAL`. The older workbook's missing revised fields are a version gap, not proof that the documented design omits them.
- PILOT_02 and PILOT_03 A/B rows were constructed by build scripts. In PILOT_03, the variant B challenge rows are altered by code. The 19 human-decision records remain historical adjudications, but 245/264 is not treated as independent agreement or a reliability coefficient.
- The historical final gate `ONTOLOGY_STABLE_WITH_REVISIONS` is hard-coded in the incorporation script. It is a project judgment, not statistical validation or production authorization.
- The 16 selected legal excerpts were checked against original official-act archives; article/annex keys were checked against R07 case packs. The R07 packs include the exact text; the share workbook uses only short excerpts.
- R08's context-field Cartesian calculation is rejected as an error test. Its only legitimate possible reading is extra relational detail unavailable at the parent context level. It is not included in the workbook.
- The 89/336 insurer boundary is open: Rotem identifies risk underwriting through structural reliance, while historical human H_009/H_010 decline to infer a qualifying relational edge from Annex II alone. Neither position was overwritten.

## Workbook checks

All checks in `02_VALIDATION/WORKBOOK_QA.md` passed. Sources referenced in the workbook retain the SHA-256 hashes registered at build time. All recovered R08 copies match the historical files byte-for-byte. No formula or external workbook reference determines a classification. No flat CSV was produced because a single table would discard the case–event–source relationships.
