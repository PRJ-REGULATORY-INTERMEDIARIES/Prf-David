# NEW TEST 3x3 — PRE-REGISTRATION

**Project:** PRJ-David / Law and Governance Architectures
**Experiment:** `New Test 3x3` (controlling workspace: `NEW TEST 3x3/`)
**Research coordinator:** Igor Caires Machado
**Conceptual framework to be tested later:** David Levi-Faur, V8
**Execution environment:** Claude (Sonnet 5.5) / VS Code, sequential, no parallel agents
**Registration date:** 2026-10-05 (local 20:1x, UTC-03:00)
**Stage covered:** initialization, case-universe audit, comparability gate, domain classification, ranking, case selection, selection freeze

## 0. Timing statement (binding)

This pre-registration was created **before the final case selection** and **before any new V8 run** under New Test 3x3. It was written after the case-universe discovery pass described in §11 and **before** any ranking, domain assignment or selection table was computed. Its SHA-256 is recorded in `LOGS/TEST_3X3_EXECUTION_LOG.md` at the moment of writing, so any later edit is detectable.

## 1. Purpose

Identify and freeze three previously studied legal cases that offer high empirical opportunity for observing governance architecture, drawn from three substantively different regulatory domains, **before** any V8 architectural analysis. This stage does **not** apply V8, build architectures, run the eight-operation procedure, or compare V8 with any alternative.

## 2. Controlling premise (verbatim from the research coordinator)

> Greater observed relational richness provides greater empirical opportunity to detect, reconstruct and test governance-architectural properties.

Relational richness is represented operationally by five counts: (1) regulatory intermediation relations; (2) actors; (3) intermediaries; (4) targets; (5) total identified relations. This does **not** assume that a larger law, more actors or more intermediation yield a stronger or better architecture. The aim is only to maximise *observational opportunity* for a demanding methodological test. Architecture must emerge, or fail to emerge, from later V8 analysis.

## 3. Design label

`PURPOSIVE INFORMATION-RICH CASE SELECTION FOR MAXIMUM OBSERVATIONAL OPPORTUNITY` — a methodological stress test, not a representative sample, not for statistical inference about the population of legislation.

## 4. Universe

Exclusively legal instruments already studied, extracted or coded in earlier PRJ-David pilots, datasets or extraction exercises found in the repository. No legislation is added in this stage. Every discovered case-version receives a recorded disposition; none may silently disappear. Different versions of one instrument are **not merged**; version relations are documented.

## 5. Registered ranking rule (NOT to be changed)

For case-versions that pass the comparability gate, rank lexicographically:

1. number of regulatory intermediation relations — descending (primary);
2. number of actors — descending;
3. number of intermediaries — descending;
4. number of targets — descending;
5. total number of identified relations — descending.

No composite score. No normalisation by statute length, word count, articles, pages, years or any other denominator. The criterion will not be changed because another measure yields more interesting cases.

## 6. Registered diversity constraint

The final selection contains exactly one case from each of three substantively distinct regulatory domains. Within each eligible domain the highest-ranked case under §5 is retained. If the global top three include the same domain more than once, only the highest-ranked case of that domain is retained and the next highest eligible case of a different domain is taken. Every exclusion produced by this constraint is documented.

## 7. Registered comparability gate (rules fixed before ranking)

Raw numbers from different pilots are not automatically comparable. Each case-version × metric is classified `C1_DIRECTLY_COMPARABLE`, `C2_HARMONIZABLE_FROM_EXISTING_DATA`, `C3_PARTIALLY_COMPARABLE`, `C4_NOT_COMPARABLE` or `C5_PROVENANCE_INSUFFICIENT`. Definitions and the rules below are applied mechanically.

**G1 — Reference denominator.** The common operational denominator is the *relational R–I–T test* recorded in the project's codebooks: an identifiable regulator–target relation, an analytically distinct third actor, and a demonstrable regulatory mediating function, supported by textual evidence. A "regulatory intermediation relation" is a relation adjudicated **positive/supported** under that test. If no defensible common denominator exists the ranking stops.

**G2 — Scope rule (`CORPUS_SCOPE`).** Only case-versions with `FULL_INSTRUMENT` scope compete in the ranking. `SUBSTANTIAL_DEFINED_SUBSET`, `LIMITED_PROVISIONS` and `UNKNOWN` are classified C3/C4 for count metrics because partially extracted laws cannot automatically compete with fully extracted laws, and because their provisions were purposively selected. No correction is invented for unobserved portions of a law.

**G3 — Metric-production rule.** A metric is rank-eligible only if it was actually produced at relation/actor level under the G1 test (or deterministically recountable from existing records produced under it). A metric never produced is `C5`; a metric produced under a different construct is `C4`.

**G4 — Pipeline homogeneity and bridge check.** Counts from different extraction pipelines/codebook versions are pooled into one ranking only if (i) existing records allow a deterministic recount (C2) and (ii) a *bridge check* on any instrument covered by both pipelines shows no material divergence in the primary metric under the same gate. A failed bridge check downgrades cross-pipeline pooling to C3, and each pipeline is then ranked only within its own **comparability stratum**.

**G5 — Version precedence.** When several versions of one instrument exist, the canonical version for ranking is the one that is (a) `FULL_INSTRUMENT`, (b) designated authoritative/frozen in project records, (c) latest freeze. Other versions are retained, not merged, and cannot be used to raise a case's counts.

**G6 — Tie-breakers.** Criteria 2–5 act only when criterion 1 ties. A tie-breaker metric classified C3 may break a tie only with an explicit caveat; C4/C5 tie-breakers may not be used (the tie is then reported unresolved).

**G7 — Final gate outcomes.**
- `COMPARABILITY_PASS`: all full-instrument R–I–T-coded case-versions are mutually C1/C2 on the five metrics.
- `COMPARABILITY_CONDITIONAL_PASS`: at least one comparability stratum with ≥3 rank-eligible case-versions exists; ranking is permitted **only within strata**; feasibility of the three-domain selection is tested at the diversity step.
- `COMPARABILITY_FAIL`: no such stratum, or no common operational definition. Stop before ranking.

## 8. Registered domain-assignment rule

Domain is classified **before** ranking and **before** selection, from subject matter, regulatory field and institutional purpose stated in the instrument's title and Article 1 — never from architectural results. Level-1 domains define "substantively distinct" for the diversity constraint; Level-2 sub-fields are recorded for transparency but are not sufficient, by themselves, to count as distinct domains. Where two Level-1 domains are plausible, a primary and an alternate assignment are recorded, the diversity constraint is evaluated on the primary assignment, and sensitivity to the alternate is reported.

## 9. Harmonization rule

Where historical counts used different counting conventions but pre-existing extraction records permit deterministic recounting, a harmonized metric may be computed using only existing data, with the counting rule documented. Original values are preserved; harmonized values are stored separately; source data are never overwritten. No new legal interpretation, no new V8 analysis, no relationships added. If harmonization needs substantive reinterpretation, the metric is classified not presently comparable.

## 10. Non-circularity

Selection may not use any architectural, network, V8, eight-operation, Codex/Claude-agreement or other downstream result, nor expectations of David or Igor (see `NON_CIRCULARITY_RULES.md`).

## 11. Disclosure of prior exposure (honesty clause)

During universe discovery, the executing agent necessarily read aggregate descriptive counts printed in earlier project reports (for example, the R3 workbook overview and the three-case summary statistics). The rules in §§7–8 are defined on scope, provenance, definition and subject-matter grounds, not on the value ordering of those counts. The agent also read, as pointers only, the V8_COMP_01 corpus inventory and selection memo; no V8_COMP_01 Track A/B output, G4 comparison file, `GDPR_V8` file or RGAM architectural profile was opened or used (`NON_CIRCULARITY_RULES.md`).

## 12. Freeze and stop conditions

- A selection freeze is created **if and only if** three defensible cases can be selected under this registered protocol (§§5–8). Otherwise the stage ends as `TEST_3X3_SELECTION_BLOCKED / METHODOLOGICAL_REVIEW_REQUIRED`, with the reason documented and no freeze files written.
- After a freeze, substitution is allowed only for an objective pre-analysis failure (corrupt source; missing necessary corpus; proven historical extraction error; duplicate case; inability to reconstruct the legal source), by separate documented decision.
- The next experimental stage requires separate authorization from Igor.
- No Git commit, push, reset or branch change is performed. Previous experiments are read-only.
