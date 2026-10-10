# V8-COMP-01 — Comparative Architectural Inference Pilot

**Research design registration:** 2026-10-04  
**Version:** protocol v0.1 (pre-execution)  
**Status:** DESIGN_REGISTERED / EXECUTION_NOT_STARTED / TEAM_FEEDBACK_OPEN  
**Proponent:** Igor Caires Machado  
**Conceptual baseline:** David Levi-Faur, *Law and the Architectures of Governance: Towards a Relational Leximetrics Approach*, draft V8 (October 3, 2026).  
**Relationship to prior work:** complementary methodological test, not a replacement ontology, new standalone theory, production dataset, or validated GDPR replication.

## 1. Provenance and distinction among decisions

- **Documented direction from David (email relayed 2026-10-04):** treat the GDPR as a methodological pilot; test the added architectural procedure on two or three quite different laws; compare whether it produces better, clearer, or more defensible inferences than V8 alone; circulate material to the team; contribute to V8 revision, intermediaries research, database and theory. David did **not** choose the cases below or authorize a standalone foundational paper.
- **Igor's decision (conversation, 2026-10-04):** register a comparative pilot and initiate preparation before incoming team suggestions, while inviting further laws/cases/research directions to strengthen V8.
- **Initial case suggestions (assistant, accepted by Igor as a working design on 2026-10-04):** MDR, DSA, Lei 13.848/2019. These are **provisional selections**, subject to source verification and team review.
- **Pending:** responses from Rotem, Ivana, Nir, Michael and other collaborators; no approval, objection or recommendation should be invented for them.

## 2. Core research question

Holding the primary legal evidence and V8 coding constant, does an explicit eight-operation architectural reconstruction protocol add **demonstrable inferential value** relative to an implementation of V8 alone? In which legal contexts does it clarify, qualify, correct or fail to improve the conclusions?

### Competing expectations

- **H1 (incremental benefit):** V8 + eight operations increases source-linked defensibility, prevents unsupported relationships and cross-level jumps, clarifies positions/conditionality and improves boundary robustness.
- **H0 (no material gain):** the additional protocol makes explicit what careful V8 application already provides, without materially improving the result or justifying its extra analytical cost.
- **Potential adverse result:** the protocol adds jargon, interpretive choices or false precision; document this rather than suppressing it.

The architecture analogy (Alexander; Hillier and Hanson) is a bounded methodological inspiration, **not** a claim to import physical-space metrics mechanically into law.

## 3. Case-selection matrix — provisional, not approved by the group

| Case | Legal instrument | Main stress test | Initial candidate scope (VERIFY current official text first) | Initial order |
|---|---|---|---|---|
| MDR | Regulation (EU) 2017/745 on medical devices | Intermediary indispensability, notified bodies, conformity assessment, designation/oversight, legal gateways | Articles 35–45 and 52, plus necessary cross-references | 1 |
| DSA | Regulation (EU) 2022/2065, Digital Services Act | Distributed authority, platform obligations, trusted flaggers, review/oversight, multiple pathways | Articles 16, 20–22, 37, 49–56, plus cross-references | 2 |
| Regulatory Agencies Law | Brazilian Law 13,848/2019 | Governance of regulators, autonomy, participation, transparency and accountability | Articles 3–11 and 14–15, plus cross-references | 3 |

**Official source entry points for subsequent verification, not proof of a frozen legal version:**
- MDR: https://eur-lex.europa.eu/eli/reg/2017/745/oj/eng
- DSA: https://eur-lex.europa.eu/eli/reg/2022/2065/oj/eng
- Lei 13.848: https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/lei/l13848.htm

**GDPR:** methodological antecedent/reference only; the earlier small, curated exercise is not a fully coded or independently validated dataset. Do not present GDPR as a fourth verified comparative result.  
**Reserve cases:** AI Act (Regulation EU 2024/1689) and the Brazilian CNJ (Constitutional Amendment 45/2004 and specifically delimited normative acts), subject to separate rationale and approval.

Case heterogeneity is deliberate: comparison of **A against B within each law** is primary. Cross-case comparisons are a robustness/external-scope probe, not a claim that the domains, instruments, legal traditions and lengths are naturally equivalent. Do not compare raw counts across legal acts without denominator and scope justification.

## 4. Design: same observations, two inferential tracks

### Common legal-evidence layer (freeze before inference)

1. Verify official legal text, language, consolidation/amendment status, retrieval date and provision IDs.
2. Delimit a functionally coherent subsystem with source-grounded inclusion/exclusion rules.
3. Produce a small, source-linked **V8-based primary coding set**. Distinguish assignment to an actor from an actual legally established actor–actor relationship. Preserve directions, conditions, exceptions, triggering events, qualifiers and multiple provisions per relationship.
4. Freeze/export the same observations and retain checksum for use by both tracks.

### Track A — V8 alone

Reconstruct the warranted relationships, configurations and architecture using V8's own inference ladder, criteria for architectural significance, traceability and stopping rule, **without introducing the eight extra operations as a mandatory template**. Save, timestamp and freeze this result before Track B is written.

### Track B — V8 + eight-operation protocol

Apply to exactly the same frozen evidence:
1. **Delimitation:** problem, legal scope, jurisdiction, boundary and dates.
2. **Decomposition:** institutional statements with legal context/modalities retained.
3. **Relational reconstruction:** only qualified actor–actor links supported by legal text; normative assignment alone is not automatically an edge.
4. **Configurational reconstruction:** coherent bundles of actors, relationships, functions, mechanisms and instruments.
5. **Positional analysis:** sequence, gateways, mandatory versus optional pathways, substitutability, conditional authority.
6. **Part–whole analysis:** distinguish actor, relation, position, configuration, law and regime properties.
7. **Architectural inference:** explicit evidence → inference warrant, counterevidence and stopping rule.
8. **Boundary/sensitivity analysis:** challenge alternative scopes, interpretations, conditions and configurations.

Track B may **qualify** or narrow Track A rather than make a grander architectural claim. Preserve all null and negative outcomes.

## 5. Prospective assessment dimensions

Assess each defensible inferential difference, with provision-level evidence and reviewer notes:

| Dimension | Evidence expected |
|---|---|
| Traceability | Can a reader traverse claim → configuration → relation → statement → provision? |
| Inferential validity | Are assignments mistakenly turned into edges? Are conditional relations represented as unconditional? Are architecture/regime claims warranted? |
| Clarity | Does the method reduce ambiguity in the claim and its scope? |
| Distinctive discovery | Does B reveal a supported position, dependence, gateway, conflicting relation or inference absent in A? |
| Robustness | Does the conclusion survive plausible boundary and interpretation alternatives? |
| Reproducibility/reviewer agreement | Can another researcher explain or replicate the reasoning? |
| Analytical cost | Time, interpretation burden, additional fields and adjudication required. |

Outcome labels at claim level: `B_IMPROVES`, `B_CLARIFIES_ONLY`, `B_EQUIVALENT`, `B_WORSE`, `UNRESOLVED`. Do not substitute a single unvalidated composite index for the underlying comparison. A blind/independent reviewer is desirable where feasible; until then, explicitly label findings **exploratory**.

## 6. Prespecified safeguards

- V8 is the **sole conceptual baseline** for this experiment; do not silently mix V6, manuscript v0.5.1 or earlier taxonomies. Other versions may be read as historical context only.
- Do not edit V8, Rotem's codebook, pre-existing PILOT_03, GDPR extracted data, protected ontology or prior adjudication material. Record crosswalk needs as proposals, not in-place schema mutations.
- Keep `V8_DEFINED`, `OPERATIONAL_SPECIFICATION`, and `METHOD_HYPOTHESIS` distinguishable.
- Separate source evidence, coded observation, interpretation, claim and reviewer decision. Every inference cites its supporting provision(s).
- No manufactured source quotations, legal article content, agreement coefficients, coding counts, dates or team decisions.
- No automated scaling before the pilot passes document/source, legal and inference-level QA.
- Formal legal architecture is **not** implementation or observed operational effectiveness.
- Do not convert the protocol into a separate foundational paper until incremental value and team direction justify it.
- Do not run Git commit, push, branch rewriting or destructive cleanup without explicit instruction.

## 7. Execution sequence and gates

| Gate | Deliverable | Exit criterion |
|---|---|---|
| G0 — Registration | Protocol, response register, source manifest, folder map | Sources and proposal/status provenance clearly documented |
| G1 — Source control | MDR official version and narrow substantive boundary | Official provision-level text verified; cross-references tracked |
| G2 — Shared evidence | MDR micro-pilot, initially 8–12 candidate institutional statements where source permits | Coded V8 observations source-linked; QA documented; immutable snapshot |
| G3 — A/B tracks | A frozen before B, equal evidence base | Independent written inference ledgers and legal anchors |
| G4 — Comparison | Difference matrix; unsupported claims and analytical costs documented | All outcome labels evidenced; no forced positive result |
| G5 — Replication | DSA and Lei 13.848 after MDR lessons are registered | Replication rules stable; deviations logged |
| G6 — Team review | Incorporate replies, suggestions and human adjudication | Changes accepted/rejected by named reviewer, rationale and effect tracked |

The first execution can create G0 and attempt G1–G4 for a **small MDR slice**, contingent on availability and verification of official legal text. If the source is missing or uncertain, stop substantive coding at `SOURCE_PENDING`, not with invented observations.

## 8. Response/decision traceability

Store the verbatim incoming/outgoing communication only if the email/chat source is actually available or supplied. Otherwise register a dated **paraphrase marked as such**. Keep these distinct: `RECEIVED_GUIDANCE`, `IGOR_DECISION`, `ASSISTANT_PROPOSAL`, `TEAM_SUGGESTION_PENDING`, `HUMAN_ADJUDICATION`, `EXECUTION_RESULT`. For each suggestion record who suggested it, why, which gate/artifact it affects, whether adopted and who made that decision. See `02_RESPONSE_AND_DECISION_REGISTER.md` and `04_RESPONSE_LOG_TEMPLATE.csv`.

## 9. Mandatory first-run report

Report: repository path inspected; protected files left unchanged; files created; git status before/after (if available); available and unavailable sources; official MDR version status; G0–G4 outcome; provisional findings and failures; incoming team messages actually inspected; suggested next command. Do not describe unperformed work as complete.
