# Data dictionary — R-I-T relationship dataset

Covers `data/rit_coded_sample_v2.csv` (9 relationships, populated) and the
fuller variable universe implied by the proposal's attributes (defined here
for the next coding round, not fabricated in this pilot — see the "status"
column). Missingness codes throughout: `1`=present/observed, `0`=absent
(explicitly established), `NA`=not applicable, `UNK`=unknown/insufficient
information, `NOE`=not observable from legal text alone, `EXT`=requires
external evidence.

## Block A — Legal source (populated)

| Variable | Construct | Definition | Values | Status |
|---|---|---|---|---|
| `relationship_id` | — | Unique id per coded relationship | free text, e.g. `CSRD-R1` | populated |
| `chain_id` | Intermediary chain | Groups relationships that are part of the same multi-level chain | free text or blank | populated |
| `intermediation_level` | Meta-regulation | Position of this relationship within a chain | `L1`, `L2`, `NA` | populated |
| `upstream_relationship_id` | Intermediary chain | The relationship immediately upstream in the same chain | `relationship_id` or blank | populated |
| `source_act` | Provenance | CELEX of the act actually processed | CELEX string | populated |
| `amended_act` | Provenance | Act being amended, when `source_act` is an amending instrument | free text or blank | populated |
| `article` | Provenance | Article/provision within `source_act` (or, for amending acts, within `amended_act`) | free text | populated |
| `provision_type` | Legal force | Recital vs. operative article vs. annex | `recital` / `article` / `annex` | populated |
| `verbatim_evidence` | Auditability | Verbatim quotation supporting the coding | free text | populated |
| `coder`, `coding_date` | Provenance | Who coded this row and when | free text / date | populated |

## Block B — Regulatory architecture (populated)

| Variable | Construct | Definition | Values | Status |
|---|---|---|---|---|
| `R_actor` | Regulator | The rule-maker/regulator in this relationship | free text | populated |
| `I_actor` | Intermediary | The candidate intermediary | free text | populated |
| `T_actor` | Target | The rule-taker/target | free text | populated |
| `intermediary_validated` | Relational test | Result of the relational test (RIT_CODEBOOK.md) | `1`/`0`/`UNK` | populated |
| `relational_test_note` | Relational test | Written justification for the validation decision | free text | populated |

**Not yet split in this pilot** (documented for the next round):
`rule_source` (the legal instrument creating the rule) vs. `direct_regulator`
(the body directly supervising) vs. `oversight_authority` (a higher-level
supervisor) — in this pilot these are folded into `R_actor` as free text
(e.g. ECO-R1's `R_actor` already names both the Commission's rule-setting
role and its register-keeping role); splitting them into separate columns
is worth doing once more relationships are coded and multi-level regulatory
stacks (EU legislature → Commission → Member State → national authority)
need to be compared systematically.

## Block C — Mechanism (populated)

| Variable | Construct | Definition | Values | Status |
|---|---|---|---|---|
| `primary_mechanism` | Mechanism | The dominant mechanism per Levi-Faur's four primary types | `reporting`/`certification`/`ranking_rating`/`auditing`/blank | populated |
| `secondary_mechanism` | Mechanism | A second mechanism present in the same relationship (e.g. ECO-R2 is certification *and* auditing) | same set, or blank | populated |
| `reporting_present` | Reporting | Whether a reporting duty exists in this provision, independent of whether it constitutes intermediation | `1`/`0` | populated |

Explicit note (per METODOLOGIA.md and RIT_CODEBOOK.md): *these four
mechanisms are the primary types selected for the empirical design of
Levi-Faur's proposal, not claimed here as an exhaustive ontology of all
possible intermediation mechanisms.* `other_mechanism` is reserved as a
free-text column for the next round if a case doesn't fit the four.

## Block D — Intermediary attributes (partially populated)

| Variable | Construct | Definition | Values | Status |
|---|---|---|---|---|
| `formal_legal_role` | Formal/legal role | Is the intermediary's role explicitly established in legislation? | `1`/`0`/`UNK` | populated |
| `mandatory_or_voluntary` | Voluntarism | Is participation/use mandatory or voluntary? | `mandatory`/`voluntary`/`NA` | populated |
| `regulatory_level` | Level | Jurisdictional level(s) of the arrangement | `EU`/`national`/`hybrid`/free text | populated |
| `sphere_primary` | Sphere | Policy domain | `sustainability`/`environmental`/`climate`/free text | populated |
| `governance_mode` | Mode of operation | Alignment with the proposal's four modes | `state-led`/`business-led`/`NGO-led`/`professional-led`/`hybrid`/`NA` | populated |
| `organizational_separation` | Degree of separation | Is the intermediary internal or external to the regulator/target? | `internal`/`external`/`hybrid`/`NA` | populated |
| `construct_validity` | — | Whether the R-I-T structure is fully supported by the text | `confirmed`/`conditional`/`confirmed (as a non-intermediation case)` | populated |

**Defined, not yet coded in this pilot round** (would require either a
second reading pass with more time, or are class-C variables per
`RIT_CODEBOOK.md` and should not be guessed from the legal text alone):

| Variable | Construct | Why not coded now |
|---|---|---|
| `motivation` | Motivation | Cannot be safely inferred from organisational form alone (e.g. "private ≠ profit-motivated" as a rule) — flagged `NOE` unless the text states motivation explicitly. |
| `intermediation_centrality` | Centrality | Requires a criterion beyond mention count, which this pilot does not yet have (see METHODOLOGY_v2.md on why hit-count ≠ centrality). |
| `legal_independence_required`, `organizational_independence`, `conflict_of_interest_rule`, `appointment_by_regulator`, `appointment_by_target`, `removal_protection`, `financial_independence_rule`, `discretionary_authority`, `professional_independence` | Autonomy | Full battery defined in RIT_CODEBOOK.md; scoped as the next coding round once a second coder is available to check them (§36 of the review that produced this v2). |
| `reporting_to_authority`, `periodic_reporting`, `supervision`, `external_review`, `accreditation`, `licensing`, `sanctions`, `license_withdrawal`, `transparency_requirement`, `appeal_or_review`, `recordkeeping`, `audit_of_intermediary` | Accountability | Same as above — full battery defined, deferred to next round. |
| `failure_risk_addressed` | Failure typology | Requires checking each relationship specifically for a preventive rule (e.g. conflict-of-interest clause) before coding a risk-addressed type; not done for all 9 rows in this pass. |
| `intermediation_strategy` | Strategy | Responsibilization vs. empowerment — requires broader reading of the act's enforcement design than the single provision coded per relationship; deferred. |
| `number_of_authority_centres`, `public_private_mix`, `self_regulation_component`, `regulatory_competition`, `single_authority_monopoly`, `multi_level_governance` | Polycentric/monocentric structure | Structural indicators intended to support future analysis, not claimed as measured in this pilot. |

## Why this dictionary is deliberately incomplete on purpose
Populating every column above for only 9 relationships, without a second
coder to check the harder judgment calls (motivation, centrality, autonomy,
accountability), would manufacture a false sense of precision. The
populated blocks (A–C, core of D) are exactly what this pilot's single-coder
reading can responsibly support; the rest is scoped, not skipped silently.
