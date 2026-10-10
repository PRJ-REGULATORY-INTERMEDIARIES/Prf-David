# Variable map — construct → dimension → indicator → variable → evidence

Makes the transition from theory to data explicit, row by row. "Status"
marks whether the indicator is actually populated in
`data/rit_coded_sample_v2.csv` (see `DATA_DICTIONARY.md` for the full
non-populated battery).

| Theoretical concept | Dimension | Observable indicator | Dataset variable | Evidence source | Status |
|---|---|---|---|---|---|
| Regulatory intermediation | Actor | Rule-broker role | `I_actor` | Legal provision | populated |
| Regulatory intermediation | Relationship | R-I-T structure | `relationship_id`, `R_actor`, `T_actor` | Legal provision | populated |
| Regulatory intermediation | Validity | Relational test outcome | `intermediary_validated` | Legal provision, reasoned | populated |
| Regulatory intermediation | Meta-regulation | Intermediary governing another intermediary | `chain_id`, `intermediation_level` | Legal provision (chained) | populated |
| Regulatory intermediation | Role multiplicity | Same actor as I in one relationship, T/R in another | `chain_id` + cross-reference of `I_actor`/`T_actor` across rows | Legal provision (chained) | populated (ETS-R1/R2) |
| Mechanism (Levi-Faur A4) | Reporting | State-led disclosure duty | `primary_mechanism`/`secondary_mechanism` = `reporting`; `reporting_present` | Legal provision | populated |
| Mechanism (Levi-Faur A4) | Certification | NGO/technical-body attestation | `primary_mechanism` = `certification` | Legal provision | populated |
| Mechanism (Levi-Faur A4) | Ranking/rating | Business-led ordering/scoring | `primary_mechanism` = `ranking_rating` | Legal provision | populated, flagged `conditional` |
| Mechanism (Levi-Faur A4) | Auditing | Profession-led verification | `primary_mechanism` = `auditing` | Legal provision | populated |
| Intermediary attribute | Formal/legal role | Explicit legislative establishment | `formal_legal_role` | Legal provision | populated |
| Intermediary attribute | Voluntarism | Mandatory vs. voluntary participation | `mandatory_or_voluntary` | Legal provision | populated |
| Intermediary attribute | Level | Jurisdictional level | `regulatory_level` | Legal provision | populated |
| Intermediary attribute | Sphere | Policy domain | `sphere_primary` | Legal provision | populated |
| Intermediary attribute | Mode of operation | State/business/NGO/professional-led | `governance_mode` | Legal provision | populated |
| Intermediary attribute | Degree of separation | Internal vs. external to R/T | `organizational_separation` | Legal provision | populated |
| Intermediary attribute | Motivation | Underlying incentive | `motivation` | Would require evidence beyond the provision | defined, not populated |
| Intermediary attribute | Centrality | Institutional importance of the function | `intermediation_centrality` | Would require a criterion beyond mention count | defined, not populated |
| Autonomy | Independence | Legal/organisational/financial independence requirements | `legal_independence_required`, `organizational_independence`, `financial_independence_rule` | Legal provision (per-relationship check) | defined, not populated |
| Autonomy | Appointment/removal | Who appoints/removes the intermediary | `appointment_by_regulator`, `appointment_by_target`, `removal_protection` | Legal provision | defined, not populated |
| Accountability | Oversight | Supervision, reporting to authority | `supervision`, `reporting_to_authority`, `periodic_reporting` | Legal provision | defined, not populated |
| Accountability | Sanction/redress | Sanctions, license withdrawal, appeal | `sanctions`, `license_withdrawal`, `appeal_or_review` | Legal provision | defined, not populated |
| Failure typology | Risk addressed by design | Type of failure the design guards against (not evidence of occurrence) | `failure_risk_addressed` | Legal provision, interpreted cautiously | defined, not populated |
| Strategy | Responsibilization vs. empowerment | Enforcement design orientation | `intermediation_strategy` | Requires reading beyond the single provision | defined, not populated |
| Polycentric/monocentric governance | Structural indicators | Number of authority centres, public/private mix, self-regulation component | `number_of_authority_centres`, `public_private_mix`, `self_regulation_component` | Requires act-level, not provision-level, reading | defined, not populated |

## What this table is for
It is the single place that shows the full intended chain
**construct → dimension → indicator → variable → evidence**, including the
parts not yet coded. Anyone extending this dataset should add rows here
before adding columns to the CSV — a variable without a row in this map is
not traceable back to the theory it operationalises.
