# Track A: dataset landscape protocol

**DRAFT — NOT VALIDATED · version 0.1.0 · no searches executed**

## Objective and unit

Map datasets, legislative portals, APIs and institutional documentary collections that may support identification of regulatory actors, functions or relationships. The unit is a data resource/version, not an episode. Explicitly distinguish discovery, eligibility, accessibility and demonstrated analytical usefulness.

## Scope and eligibility

EU coverage is a proposed starting point. Approve jurisdictions, domains, languages, dates and the operational definition of dataset before searching. Candidate inclusion requires identifiable provenance and potentially relevant regulatory information; record insufficient information as pending. Duplicate, out-of-scope and non-dataset exclusions need written reasons. An inaccessible source is not automatically irrelevant; log access barriers and disposition.

## Search-source categories and recording

Proposed categories: legislative portals, institutional open-data catalogs, repositories, API documentation, academic data supplements and bibliographic leads. This phase does not identify or visit actual sources. Use `search-log.csv` to record source/category, full query or navigation path, filters, language, coverage, search timestamp, result count, operator and saved-result reference. Log zero results and failed access. Amend strategies prospectively with a version and reason; avoid silently replacing searches.

## Screening

Deduplicate with persistent resource/version IDs, retaining duplicate links. Screen description first, then documentation where permitted. Use `screening.csv` to record stage, decision (include/exclude/pending/duplicate), reason, reviewer and date. A second review and disagreement process must be specified before formal review claims. Keep excluded/pending records and adjudication history.

## Metadata extraction and verification

Use `metadata-template.csv`: title, provider, source URL, geographic/temporal coverage, unit, variables, format, access method, version, license, terms, verification date, reviewer, evidence locator and RIT relevance. Record unknown license as unknown, never as permission. Independently verify source existence, access route, provenance, version and rights before treating metadata as verified. Archive only permitted documentation; retain hashes where appropriate.

RIT relevance values: explicit; inferable_pending_validation; not_demonstrable; unknown. `not_demonstrable` concerns this resource's evidence capacity, not absence of intermediaries in the world. Record the supporting rationale and limitations separately. The database stores core catalog metadata; detailed extraction remains in the versioned intake form pending a pilot-driven extension.

## Reproducibility and outputs

Preserve query logs, screening decisions, metadata versions and source references. Move approved structured metadata into candidate catalog records only after review; no automatic import is provided in Phase 01. Report coverage and access limitations. If the work will be presented as a formal scoping review, review reporting requirements before adopting that designation. No review registration or compliance is claimed.
