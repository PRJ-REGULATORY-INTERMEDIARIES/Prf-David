# Primary Interpretive Reader Proposal — Case 03

## A. Case overview

**Act:** Regulation (EU) 2023/1115 of the European Parliament and of the Council of 31 May 2023 on the making available on the Union market and the export from the Union of certain commodities and products associated with deforestation and forest degradation and repealing Regulation (EU) No 995/2010 ("EUDR").
**CELEX:** 32023R1115
**Corpus:** `cases/case_03/corpus/act.md` (sha256 `d2393fd43a024b1e430175951da9dfd61f08c74f9c9fb038ad431e21a61b3b3c`, confirmed against `cases/CASE_REGISTRY.yaml`).

**Architecture summary.** The Regulation prohibits placing, making available on the market, or exporting relevant commodities/products (cattle, cocoa, coffee, oil palm, rubber, soya, wood, and listed derived products) unless they are deforestation-free, legally produced, and covered by a due diligence statement (Article 3). Operators and non-SME traders (Articles 4-5, assimilated by Article 5(1)) must exercise due diligence — information collection, risk assessment, and risk mitigation (Articles 8-13) — and submit due diligence statements to Member States' competent authorities through a Commission-run information system (Article 33). Member States designate competent authorities (Article 14) that carry out risk-based checks, corrective action and penalties (Articles 16-25). A distinct chapter governs products entering or leaving the Union market, where customs authorities examine and act on the compliance status assigned by competent authorities (Articles 26-28). A country-benchmarking system lets the Commission classify countries into low/standard/high deforestation-risk categories, differentiating operators' due diligence intensity and competent authorities' check quotas (Article 29-30). A dedicated channel lets any natural or legal person submit "substantiated concerns" that competent authorities must assess and may act on (Articles 31-32). Delegated- and implementing-act powers, a review clause, and repeal of the predecessor Regulation (EU) No 995/2010 close out the operative text (Articles 33-38).

**Counts by relation_type** (9 relations proposed):

| relation_type | count |
|---|---|
| intermediated | 2 |
| uncertain | 1 |
| direct | 6 |
| not_supported | 0 |

## B. Proposed relationships

| relation_id | source_location | operative_anchor_location | R | I | T | relation_type | mechanism | confidence |
|---|---|---|---|---|---|---|---|---|
| rel-001 | Art 26(2),(6)-(9); Art 17(1)-(3); Art 23; Art 28 | Art 26(9) | competent authorities | customs authorities | operators and traders | intermediated | enforcement_support | high |
| rel-002 | Art 31(1)-(4) | Art 31(1)-(2) | competent authorities | natural/legal persons submitting substantiated concerns | operators and traders | intermediated | reporting | high |
| rel-003 | Art 18(2)(e); Art 21(1) | Art 18(2)(e) | competent authorities | administrative authorities of third countries | operators and traders | uncertain | enforcement_support | medium |
| rel-004 | Art 16(1),(3),(5); Art 18(1); Art 23; Art 24(1); Art 25(1)-(2) | Art 16(1) | competent authorities | — | operators and traders | direct | monitoring_supervision | high |
| rel-005 | Art 4(1)-(3); Art 33(1)-(2) | Art 4(2) | competent authorities | — | operators | direct | reporting | high |
| rel-006 | Art 29(1)-(3); Art 13(1); Art 16(8)-(10) | Art 29(2) | Commission | — | operators and traders | direct | standard_setting | high |
| rel-007 | Art 14(2)-(3); Art 22(1)-(2); Art 25(3) | Art 22(1) | Commission | — | Member States | direct | reporting | medium |
| rel-008 | Art 34(5); Art 35(1)-(6) | Art 34(5) | Commission | — | operators and traders | direct | standard_setting | medium |
| rel-009 | Art 5(2)-(6) | Art 5(3)-(4) | competent authorities | — | SME traders | direct | reporting | high |

## C. Intermediated relations

### rel-001 — Customs authorities between competent authorities and operators/traders (enforcement at the border)

Competent authorities hold "overall enforcement" responsibility for relevant products entering or leaving the market (Article 26(2)) and determine compliance status through the information system (Article 33). Customs authorities are a legally distinct body (Article 2, point (33)) with their own statutory customs-control competence (Article 26(3)), but under this Regulation they perform a specific, textually attributed function: examining, via the electronic interface, the status assigned by competent authorities to a due diligence statement (Article 26(6)), suspending release for free circulation or export where that status flags a required check (Article 26(7), cross-referencing Article 17(2)), and refusing release outright once competent authorities conclude the product is non-compliant (Article 26(9)).

**Third-actor test:**
- *Distinction* — YES. Customs authorities are defined separately from competent authorities and from operators/traders and have their own statutory function.
- *Function* — YES. Article 26(6)-(9), Article 17(2)-(3) and Article 23 attribute the examine/suspend/refuse actions specifically to customs authorities.
- *Regulatory integration* — YES. Customs authorities' suspension/refusal is the operational act that makes the competent authority's non-compliance finding effective against the specific target's product at the border; it is directed at T, not merely assisting R's internal process.
- *Evidence* — YES. Entirely operative text (Article 26, Article 17, Article 23); Regulation (EU) No 952/2013 cross-references describe customs authorities' general competence but are not relied on for anything beyond what this corpus itself reproduces.
- *Counterfactual* — YES. Without customs authorities' suspension/refusal function, competent authorities would have no mechanism under this Regulation to prevent release of a product they have flagged; a genuine step of the R-to-T mechanism would be lost.

All five dimensions lean YES with high confidence; this is the clearest intermediated relation in the case.

### rel-002 — Third-party informants ("substantiated concerns") between competent authorities and operators/traders

Article 31(1) lets "natural or legal persons" submit a "substantiated concern" — a duly reasoned, objective and verifiable claim of non-compliance (Article 2, point (31)) — to competent authorities. Article 31(2) then imposes a mandatory duty: competent authorities "shall, without undue delay, diligently and impartially assess the substantiated concerns... and take the necessary steps, including carrying out checks and conducting hearings of operators and traders... and, where appropriate, taking interim measures under Article 23." The channel recurs as a cross-referenced trigger throughout the enforcement architecture: Article 16(12) (checks), Article 23(a) (interim measures), Article 10(2)(l) (risk assessment criterion), Article 4(5)/Article 5(5) (operator/trader notification duties), and Article 13(2) (loss of simplified due diligence).

**Third-actor test:**
- *Distinction* — YES. Any natural or legal person, distinct from R and T.
- *Function* — YES. Article 2(31) and Article 31(1) attribute a specific, defined act (submitting a substantiated concern).
- *Regulatory integration* — YES. Article 31(2)'s mandatory assessment-and-action duty, plus the repeated cross-references, show this function structures competent authorities' action toward a specific target — not merely R's internal policy process.
- *Evidence* — YES. Entirely operative text.
- *Counterfactual* — YES. Removing this channel would remove a specific, legally mandated route for third parties to trigger scrutiny of a named operator or trader.

Coded intermediated at high confidence, flagged `[reviewer_attention: conceptual_boundary]` because, unlike an accredited verifier, an informant here may be literally anyone — the classification rests on the textually mandatory, cross-referenced integration of the function, not on institutional pedigree, precisely as the ten-step procedure requires.

### rel-003 (uncertain, not forced to intermediated) — Third-country administrative authorities and field audits

Article 18(2)(e) allows checks to include "spot checks, including field audits, including where appropriate in third countries, provided that such third countries agree, through cooperation with the administrative authorities of those third countries." A third-country authority's cooperation is a distinct, textually attributed function (facilitating field verification on its own territory). However, this field-audit modality is only one of several optional check types under Article 18(2) ("may also include, where appropriate"), and the core checks under Article 18(1) — examination of the due diligence system and documentation — do not depend on it. Regulatory integration and the counterfactual test are therefore genuinely unclear rather than clearly YES: removing third-country cooperation removes a discretionary supplementary verification option, not (on the text's own terms) a step that the core R-to-T supervisory mechanism cannot function without. Per the final self-check, this was left as `uncertain` rather than forced to `intermediated`.

**No other third actor was seriously considered and left unresolved as "uncertain."** All other rejected candidates (Section E) were resolved to "considered and rejected," not left open.

## D. Important direct relations

- **rel-004** — Competent authorities → operators/traders: the core domestic supervisory relation (risk-based checks, corrective action, penalties, interim measures), Articles 16-25.
- **rel-005** — Operators → competent authorities: due diligence statement submission through the Article 33 information system (treated as an instrument, not an actor — see uncertainty log).
- **rel-006** — Commission → operators/traders: country-risk classification (Article 29) directly differentiates due diligence intensity (Article 13) and check quotas (Article 16(8)-(10)).
- **rel-007** — Member States → Commission: institutional reporting/notification duties (annual application report, competent-authority designation, final-judgment notification). Confidence set to medium; this is a thinner "regulatory" relation than the operator/trader-facing ones, since the Commission's documented role is limited to receiving/publishing rather than a general supervisory power over Member States.
- **rel-008** — Commission → operators/traders: delegated-act power to amend the Annex I product list, subject to Member State expert consultation that is examined and rejected as an intermediary (Section E).
- **rel-009** — Competent authorities → SME traders: the lighter, SME-specific information-retention regime of Article 5(2)-(6).

## E. Borderline cases (uncertainty log)

1. **`contextual_candidate_recital_only` — the "EU Observatory" (Recital 31).** Described at length as a Commission-run monitoring and scientific-evidence body that could "support the implementation of this Regulation" and assist competent authorities, operators, traders and stakeholders through an early-warning platform. **No article in the enacting terms establishes it, assigns it any task, or connects it to any operative R-T relation.** This is the clearest recital-only candidate in the case and is logged rather than coded positive. Promoting it would require an operative article tying its outputs to a specific R-T relation (e.g., mandatory use in risk assessment or checks).
2. **`actor_vs_instrument` — the Article 33 information system.** Its "shall identify"/"shall inform" language (Article 17(2)) and risk-profiling role (Article 33(2)(g)) were seriously weighed as an independent intermediary function. Rejected: it is a Commission-established and maintained technical platform without independent legal personality or discretion; the personifying language is read as describing an automated process performed by a tool, not an actor. Flagged `[reviewer_attention: conceptual_boundary]` per the specific instruction to treat this provision with particular care.
3. **`third_actor_considered_not_mediating` — Member State experts (Article 35(4)) and the Article 36 committee.** Assist the Commission prepare its own delegated/implementing acts (Annex I amendments, country classification, electronic interface, information-system rules). No function toward operators/traders is attributed; rejected as "assisting R prepare R's own act," the same pattern the v1.1 methodology working draft describes (without pre-resolving) for Case 01's Article 8(4)/EEA episode.
4. **`third_actor_considered_not_mediating` — third-party/NGO/stakeholder input into country-risk classification (Article 29(4)).** Optional input into the Commission's own general classification process; the classification duty under Article 29(3) does not depend on it.
5. **`third_actor_considered_not_mediating` — the authorised representative (Article 6).** The mandating operator/trader "shall retain responsibility" for compliance; the representative executes an administrative act on the target's own behalf, not a function toward T from R's side.
6. **`third_actor_considered_not_mediating` — certification/third-party verified schemes (Article 10(2)(n); Recital 52).** Expressly optional "complementary information" among many listed risk-assessment criteria; Recital 52 states such schemes "should not... substitute the operator's responsibility."
7. **`incomplete_R_I_T_structure` — financial institutions (Article 34(4)).** Only a prospective impact-assessment mandate; no current operative obligation exists, so no relation is coded.
8. **`borderline_direct_relation` — Article 15 technical assistance/guidance.** Uniformly discretionary ("may") facilitation by Member States/Commission toward operators and competent authorities; logged rather than coded as a positive direct relation given its non-binding, non-supervisory character, though a reviewer could reasonably promote it.

## F. Primary-coder caveats

- This is a fresh v1.1 reading; no prior proposal, review, or output for this case (or any other case) was consulted, per the task's prohibitions.
- Several relations rest on the Commission's or competent authorities' documented *receiving/compiling/publishing* role rather than a strong, elaborated supervisory power (rel-007, rel-008); confidence was set to medium rather than high to flag this for the reviewer.
- The corpus repeatedly cross-references Regulation (EU) No 952/2013 (Union Customs Code) and Regulation (EU) 2022/2399 (EU Single Window Environment for Customs). No text of either instrument was imported; coding of rel-001 and rel-003 rests solely on what this Regulation's own articles reproduce about customs authorities' and the electronic interface's functions.
- The country-benchmarking chapter (Articles 29-30) and the substantiated-concerns chapter (Article 31) were read as genuinely fresh candidates per the task's specific instruction, without assuming any prior characterization; rel-002 and rel-003/unc-004 are the product of that fresh reading, reaching different conclusions from each other (positive intermediation for substantiated concerns; rejected/uncertain for country-classification stakeholder input and third-country field-audit cooperation, respectively) despite superficial similarity as "third-party information channels."
- No external legislation, doctrine, case law, or prior model output was consulted; where external context would be indispensable, it is flagged in the affected uncertainty entries rather than assumed.
