# Extraction uncertainties — GDPR Pilot 01

**Status:** `MACHINE_PROVISIONAL`. Generated from the extraction store; each item states what it affects. These are limits of the pilot's own extraction, not findings about the GDPR.

| ID | Units | Type | Description | Effect |
|---|---|---|---|---|
| UNC-001 | A62.P7 | interpretation | 'a provisional measure on the territory of its Member State' — referent of 'its' (non-complying SA's Member State vs the adopting SA's) is ambiguous in the text | affects the direction of the peer-enforcement relation in 62(7) |
| UNC-002 | A68.P1;A99.P1;A99.P2 | interpretation | Effective date of the N1 establishment of the Board (entry into force 24 May 2016 versus application 25 May 2018) is not stated in Art.68(1); Art.92(2) shows that some provisions take effect from entry into force | affects the temporal reference for the legal-constitution claim of the Board |
| UNC-003 | A99.P2 | coding-rule | Provision-level application dates differ from the general application date (24 May 2016, 25 May 2018, 25 May 2020) | legal_status_of_norm is recorded as the baseline value for all units; unit-level temporal exceptions are noted but not individually coded |
| UNC-004 | A4.P0;A57.P1;A58.P1;A58.P2;A58.P3;A70.P1;A83.P4;A83.P5 | coding-rule | Granularity: 382 point-level units were inventoried automatically, but screening and extraction were done at paragraph level. Long lists (Art.4 definitions; Art.57(1) 22 tasks; Art.58 powers; Art.70(1) 25 tasks; Art.83(4)-(5) tiers) were grouped into few records, with point citations only where relation-bearing points were separated or linked. | Point-level distinctions (e.g. which of the 22 SA tasks is a relation and which a self-contained duty) may be lost; extraction coverage is therefore 'paragraph-level complete, point-level partial'. |
| UNC-005 | A57.P1.ptf;A77.P1;A77.P2;A60.P7 | coding-rule | Possible duplicate observations: the complaint-handling duty of the SA appears in QR for Art.57(1)(f) (with Art.77 units linked), Art.77(2) and Art.60(7). They were kept as distinct statements by unit but state overlapping duties. | Counts of relations in SC-10 and SC-07 may overstate independent observations; many-to-many provenance (not duplication) is the intended rule. |
| UNC-006 | A12.P4;A77.P2;A57.P1.ptf | interpretation | Relation type 'information/reporting' is used for 106 of 238 relations (44.5%) and lumps notifications, consultations, cooperation, reasons-giving and information duties. V6's ten relation types do not provide a type for peer cooperation, jurisdictional or liability allocation. | Type-level analyses (e.g. 'information relations dominate') are artefacts of the type inventory; discrimination is carried by `function`, `object` and `type_note`. |
| UNC-007 | A5.P2;A24.P1;A58.P1;A58.P2;A83.P2 | inference | Accountability is recorded unit by unit (INFO / ANSWERABILITY candidates). A **derived** controller/processor→SA accountability relation can be assembled across Arts 5(2), 24(1), 58(1)(a),(e), 58(2), 83 (see INITIAL_ARCHITECTURAL_PROFILE §5) but was not entered as an extraction record because it is a reconstruction, not a provision-level observation. | AC (full) appears only as a derived, cross-provision relation; no single unit satisfies all five elements. |
| UNC-008 | A21.P5 | coding-rule | Unit left on Hold: a permission of the data subject to object by automated means without an identifiable counterpart in the unit; referred to Directive 2002/58/EC. | No record; unit counted as screened with extraction status Hold. |
| UNC-009 | A1.P3;A2.P3;A4.P0.pt7;A6.P3;A10.P0;A23.P1;A49.P5;A53.P4;A85. | interpretation | Twenty assignments have an unstated or unnamed subject ('Union or Member State law', passive voice, unspecified legislator). They are recorded as NA with `subject-unstated`; no actor was invented. | These provisions describe the rule-making competence of national and Union legislators, which is not represented as a position of the architecture. |
| UNC-010 | A4.P0.pt7;A4.P0.pt8;A4.P0.pt22;A56.P1 | ontology | Functionally defined positions: controller, processor, joint controllers, supervisory authority concerned and lead supervisory authority are roles defined by conduct or by facts (determining purposes and means; establishment; affected data subjects), not legally specified offices. They were recorded as `position_type` with a note. | The ontology's notion of 'a legally specified place' does not fit them straightforwardly (TP-01). |
| UNC-011 | A43.P1;A53.P1;A54.P1;A68.P3;A93.P1 | external dependency | Several decisive constitutive dependencies lie outside W and were not retrieved: Member State law constituting each SA (EXT-015); Regulation (EC) No 765/2008 and EN-ISO/IEC 17065/2012 (EXT-009–011); the instrument constituting the EDPS (EXT-017); Regulation (EU) No 182/2011 (EXT-008, 018, 019). | Absence-dependent claims and some S→A outcomes are limited to W or indeterminate. |
| UNC-012 | A6.P1;A9.P2;A14.P5;A17.P3;A23.P1;A49.P1;A85.P2;A88.P1;A89.P2 | external dependency | Generic references to 'Union or Member State law' occur throughout (29 records carry an explicit Member State law dependency; 48 records mention Union or Member State law). Only constitutive references were registered as EXT rows (22 rows for roughly 16 distinct sources, with some sources repeated per provision); generic national-law references are not in the external-reference register. | The external-reference register is incomplete for generic national-law dependencies; counts of external dependencies are lower bounds. |
| UNC-013 | A99.P1;A99.P2;A92.P2;A51.P4;A83.P9 | coding-rule | All records carry the baseline `legal_status_of_norm` (in force; applicable from 25 May 2018). Provision-level dates (24 May 2016; 25 May 2018; 25 May 2020) are mentioned in notes but are not coded unit by unit. | Legal status is not time-indexed at unit level. |
| UNC-014 | (all recitals) | coding-rule | Recitals were extracted into the working text but not reviewed for interpretive context beyond their identification as non-operative. No record was created from a recital. | Interpretive ambiguities (e.g. 62(7)) are unresolved; a recital review is a pending step. |
| UNC-015 | A1.P1;A2.P1;A3.P1 | coding-rule | Sixty units (15%) were screened 'No' as scope, exceptions, content specifications or passive substantive rules. Several (e.g. exceptions in 14(5), 17(3), 22(2)) modify the conditions of recorded relations but were not coded as separate records. | Condition fields of the affected relations are summarised in their notes. |

## Review flags carried by records

- NA `N1`: 1
- NA `N2-designation`: 2
- NA `N2-establishment`: 2
- NA `N2-register`: 3
- NA `accountability-label`: 1
- NA `derived-relation`: 1
- NA `external-dependency`: 1
- NA `self-modifying-scope`: 2
- NA `subject-unstated`: 20
- NA `temporal-interpretation`: 1
- PD `DEV-threshold`: 10
- PD `N-type-ambiguous`: 1
- PD `N2-register`: 3
- PD `external-constitution`: 3
- QR `N-type-ambiguous`: 1
- QR `interpretation`: 1
- QR `no-counterpart-position`: 1
- QR `soft-law`: 1
- QR `type-uncertain`: 2
