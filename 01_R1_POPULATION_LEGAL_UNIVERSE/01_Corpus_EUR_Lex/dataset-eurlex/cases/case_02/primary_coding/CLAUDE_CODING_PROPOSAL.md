# Claude Primary Coding Proposal — Case 02

## A. Case overview

**Act:** Regulation (EU) 2023/956 of the European Parliament and of the Council of 10 May 2023 establishing a carbon border adjustment mechanism (CBAM)
**CELEX:** `32023R0956`
**Corpus hash (SHA-256):** `01357c4c34c9f6009e72265a163bcd45cebc4e4bd9d806398b5c05e8487c692b` (verified against `cases/CASE_REGISTRY.yaml` before coding)

The Regulation establishes a market-based mechanism that requires importers of specified carbon-intensive goods (cement, electricity, fertilisers, iron and steel, aluminium, hydrogen) to become "authorised CBAM declarants," to report the embedded greenhouse gas emissions in those goods, to have those emissions independently verified, and to surrender CBAM certificates priced to track the EU ETS. Governance is distributed across the European Commission (registry, price-setting, review, risk analysis, circumvention monitoring, coordination of competent authorities), Member State "competent authorities" (authorisation, enforcement, penalties), customs authorities (border control and data transmission), and a small set of private/technical intermediary actors: accredited verifiers (who verify declarants' and third-country operators' embedded-emissions reports), national accreditation bodies (who accredit those verifiers), and an "independent person" who certifies carbon-price documentation. A separate transitional-reporting regime (2023–2025), with no verification requirement, precedes the definitive regime (from 2026).

**Proposed relationships: 22 total**
- `intermediated`: 5
- `direct`: 16
- `uncertain`: 1
- `not_supported`: 0

**Uncertainty log entries:** 11

## B. Proposed relationships

| relation_id | source_location | R | I | T | relation_type | mechanism | confidence |
|---|---|---|---|---|---|---|---|
| rel-001 | Art 8(1); Art 6(2)(d); Annex VI | European Commission; competent authority | accredited verifier | authorised CBAM declarant | intermediated | verification | high |
| rel-002 | Art 10(5)(b),(6),(7); Annex VI | European Commission | accredited verifier | operator of installation in third country | intermediated | verification | high |
| rel-003 | Art 9(2) | competent authority; European Commission | independent person | authorised CBAM declarant | intermediated | certification | medium |
| rel-004 | Art 14(1); Art 19(3); Art 25(2)-(4); Recital 43 | European Commission; competent authority | customs authorities | authorised CBAM declarant | intermediated | information_transmission | medium |
| rel-005 | Art 33(1)-(3) | European Commission | customs authorities | importer; indirect customs representative | intermediated | information_transmission | medium |
| rel-006 | Art 27(1),(3),(5) | European Commission | competent authorities; customs authorities (uncertain) | operators/exporters/producers (circumvention) | uncertain | other_mechanism | low |
| rel-007 | Art 5(1); Art 17(1)-(3) | competent authority | — | importer/indirect customs representative (applicant) | direct | other_mechanism | high |
| rel-008 | Art 4; Art 25(1) | customs authorities | — | person other than authorised CBAM declarant | direct | enforcement_support | high |
| rel-009 | Art 6(1)-(2) | European Commission; competent authority | — | authorised CBAM declarant | direct | reporting | high |
| rel-010 | Art 7(1)-(2),(7); Annex IV | European Commission | — | authorised CBAM declarant; operator | direct | standard_setting | high |
| rel-011 | Art 8(3); Art 18(1) | European Commission | — | accredited verifier | direct | standard_setting | medium |
| rel-012 | Art 18(2); Recital 47 | national accreditation body | — | person seeking accreditation as verifier | direct | accreditation | high |
| rel-013 | Art 10(1),(3),(4),(8); Art 14(1)-(2); Art 16 | European Commission | — | operator; authorised CBAM declarant | direct | other_mechanism | high |
| rel-014 | Art 11(1); Art 12 | European Commission | — | competent authority | direct | coordination | high |
| rel-015 | Art 15 | European Commission; competent authority | — | authorised CBAM declarant | direct | monitoring_supervision | medium |
| rel-016 | Art 19(1)-(2) | European Commission; competent authority | — | authorised CBAM declarant | direct | monitoring_supervision | high |
| rel-017 | Art 20-24 | Member State; European Commission | — | authorised CBAM declarant | direct | other_mechanism | high |
| rel-018 | Art 26(1)-(6) | competent authority | — | authorised CBAM declarant; unauthorised importer | direct | enforcement_support | high |
| rel-019 | Art 27(1)-(3),(6) | European Commission | — | operators/exporters/producers (circumvention) | direct | monitoring_supervision | high |
| rel-020 | Art 2(6)-(9); Annex III | European Commission | — | third country or territory | direct | monitoring_supervision | medium |
| rel-021 | Art 32; Art 34; Art 35(1)-(2) | European Commission | — | importer; indirect customs representative | direct | reporting | high |
| rel-022 | Art 35(3)-(6) | European Commission; competent authority | — | importer; indirect customs representative | direct | enforcement_support | high |

## C. Intermediated relations

**rel-001 — Verification of the authorised CBAM declarant's embedded emissions (Article 8; Article 6(2)(d); Annex VI).** The declarant must ensure its self-reported total embedded emissions are verified by an accredited verifier applying the Annex VI principles (professional scepticism, reasonable assurance, mandatory installation visit unless waived). The resulting verification report is expressly folded into the CBAM declaration (Art 6(2)(d)) and is material to the Commission's/competent authority's review (Art 19(2)). This is the clearest and most complete R–I–T structure in the Act. Confidence: high.

**rel-002 — Verification of a third-country operator's embedded emissions for CBAM-registry disclosure (Article 10(5)(b),(6),(7); Annex VI).** Structurally parallel to rel-001 but with a distinct target: the operator of a production installation registered under Article 10, whose verified data may be disclosed to and relied on by an authorised CBAM declarant, and which is tied by the text to enabling the Article 19 review. Confidence: high.

**rel-003 — Certification of carbon-price documentation by an "independent person" (Article 9(2)).** To support a declarant's claim for a reduction in certificates to be surrendered on account of carbon price paid abroad, the supporting documentation must be certified by a person independent of both the declarant and the country-of-origin authorities. This mirrors the verifier structure but rests on a much thinner institutional basis: no accreditation, qualification, or oversight regime is defined for this "independent person" in the corpus (the implementing act on qualifications/independence under Art 9(4) does not yet exist). Coded intermediated but flagged `[reviewer_attention: conceptual_boundary]`, confidence medium.

**rel-004 — Customs authorities feeding Commission/competent-authority supervision of the declarant (Article 14(1); Article 19(3); Article 25(2)-(4); Recital 43).** One of the case's flagged "real candidate structures," examined carefully. Customs authorities actively check goods and declarant identity (Recital 43) and periodically, automatically transmit the resulting data to the Commission, which cross-checks it against the CBAM registry and forwards it to the competent authority, feeding risk analysis (Art 19(3)) and enforcement. Coded intermediated with medium confidence and flagged `[reviewer_attention: conceptual_boundary]`, because an alternative reading — parallel co-regulator cooperation rather than mediation of an R–T relation — is plausible and should be weighed by the secondary reviewer.

**rel-005 — Transitional-period analogue of rel-004 (Article 33(1)-(3)).** Same structure, weaker because the transitional regime carries no verification requirement and the customs function is closer to notice-giving plus data relay. Confidence medium, `[reviewer_attention: conceptual_boundary]`.

## D. Important direct relations

The Act's core compliance architecture is mostly direct, layered between two co-regulators (the Commission and the Member State competent authority) and the authorised CBAM declarant / importer:

- **Authorisation** (rel-007, Art 5/17): competent authority licenses the applicant as authorised CBAM declarant.
- **Reporting** (rel-009, rel-021): direct declaration/report obligations, definitive period (verified, via rel-001) and transitional period (unverified, self-reported) respectively.
- **Standard-setting** (rel-010, rel-011): the Commission directly fixes the embedded-emissions calculation methodology (Annex IV) and the qualification/verification-principle rules applied to verifiers — showing the Commission regulates the intermediary (verifier) directly in addition to relying on it as I elsewhere.
- **Registry administration** (rel-013): the Commission's direct management of the CBAM registry for operators and declarants.
- **Coordination among regulators** (rel-014): the Commission assists and coordinates competent authorities — an example of role instability, since competent authorities are R toward declarants elsewhere (rel-007, rel-018) but T here.
- **Monitoring/review/risk analysis** (rel-015, rel-016): direct Commission/competent-authority oversight of declarants, distinct from the verifier-mediated relations because these are the regulators' own review and audit powers.
- **Certificate market administration** (rel-017): sale, pricing, surrender, repurchase and cancellation of CBAM certificates, bundled into one record since Articles 20–24 form a single coherent, non-mediated architecture.
- **Enforcement** (rel-018, rel-022): direct penalty regimes for the definitive and transitional periods.
- **Circumvention monitoring** (rel-019) and **third-country electricity-market conditions** (rel-020): direct Commission oversight of, respectively, trade-pattern circumvention and third-country/territory decarbonisation commitments — the latter notable for treating a state/territory as T.
- **Accreditation of verifiers** (rel-012): the national accreditation body directly accredits verifiers, establishing the pedigree of the intermediary used in rel-001/rel-002.

## E. Borderline cases

The following were seriously considered and either downgraded to `uncertain`, rejected as intermediaries, or excluded from the R–I–T construct entirely (full detail in the uncertainty log):

- **Article 27(5)** — "the Commission may be assisted by the competent authorities and customs authorities" in a circumvention investigation: retained in the main matrix as `uncertain` (rel-006) because the assisting function is textually unspecified.
- **Article 18(3)** — future delegated acts on accreditation-body oversight, control, withdrawal, mutual recognition and peer evaluation: a potential Commission–accreditation-body–verifier chain, not coded because the delegated act does not yet exist in this corpus (unc-001, unc-010).
- **Article 11(2)** — horizontal information exchange among competent authorities: rejected as R-I-T (no hierarchical target) (unc-002).
- **Article 17(1)/(8)** — inter-authority consultation before granting/revoking authorisation: treated as parallel co-regulator input folded into the direct relation (rel-007), not intermediation (unc-003).
- **Recital 72 "Climate Club"** — aspirational forum with a described quality-assurance role over monitoring/reporting/verification among members: recital-only, not operative in this corpus (unc-004).
- **Article 27(4)** — voluntary circumvention notifications by Member States, affected parties, and NGOs: too ad hoc and uninstitutionalised to code as intermediation (unc-005).
- **Annex IV point 5(d)-(e)** — transmission system operators' capacity-nomination role: rejected as a distinct intermediary; it is an ordinary grid-operation fact feeding the verifier's certification, not itself a CBAM verifying/reporting function (unc-006).
- **Article 30** — Commission reporting to the European Parliament and Council: institutional accountability, not a regulatory relationship over a target (unc-007).
- **Recitals 73-74** — Union financial/technical support to LDCs: programmatic assistance, not a regulatory relationship (unc-008).
- **Article 2(12)** — discretionary future agreements with third countries on carbon pricing: external content, not yet specified (unc-009).
- **Article 9(2)/(4)** — supplementary flag on the "independent person" certifying carbon-price documentation: thinner institutional basis than the verifier regime; noted for reviewer reconsideration of rel-003 (unc-011).
- **Article 15** — Commission risk-based controls with competent-authority "further investigations": considered as intermediated (competent authority as I) but coded direct (rel-015), since the competent authority otherwise functions as a primary co-regulator throughout the Act rather than as a mediator of a Commission–declarant relationship; flagged `[reviewer_attention: conceptual_boundary]` on that record.

## F. Primary-coder caveats

- **Source-boundedness.** Several operative provisions in this Regulation refer to bodies, procedures, or standards defined in full in external instruments not reproduced in this corpus — most importantly Regulation (EC) No 765/2008 and Implementing Regulation (EU) 2018/2067 (national accreditation bodies' own authority and verifier accreditation procedure), Regulation (EU) No 952/2013 (customs authorities' general powers), and multiple not-yet-adopted implementing/delegated acts (default-value methodology, verification-principle detail, accreditation oversight conditions, "independent person" qualifications). Records resting partly on such external content are marked `external_context_required: true` with the specific gap named in `coder_note`.
- **Two co-regulator pattern.** Throughout the Act, the Commission and the Member State competent authority frequently act as parallel, non-mediating co-regulators of the same target (e.g., rel-009, rel-015, rel-016, rel-022). This was deliberately not recoded as intermediation merely because one authority's output (e.g., a preliminary calculation or risk flag) informs the other's decision; the codebook's warning against converting information-sharing between regulators into intermediation was applied consistently.
- **Two genuinely case-specific candidates were coded intermediated with only medium confidence** (rel-004, rel-005): the customs-authority data-transmission chain. These are flagged for close secondary-reviewer scrutiny, since a defensible alternative reading treats them as inter-regulator cooperation rather than R–I–T mediation.
- **The independent-person certification structure (rel-003)** is the weakest of the coded intermediated relations because the Act, unlike its verifier regime, defines no accreditation or qualification standard for that person.
- No result, label, or count from any other case, prior pilot, or external model output was consulted in producing this proposal.
