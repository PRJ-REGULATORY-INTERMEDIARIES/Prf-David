# Methodology v4

## Conceptual starting point

David Levi-Faur's proposal treats regulatory intermediation as a move beyond
the dyadic regulator-rule-taker relation: actors, mechanisms and strategies
must be examined together. This delivery distinguishes three layers:

1. the theoretical construct — regulatory intermediation;
2. the operational proposal — a five-condition R-I-T test plus four mechanism
   families and individual institutional attributes;
3. future analysis — diffusion, effectiveness, legitimacy, trust,
   autonomy/accountability indices and regime-level polycentricity, none of
   which is estimated here.

The four mechanisms are report duty, certification, ranking/rating and audit.
They are used as an empirical scaffold because they are the proposal's own
organising vocabulary; they are not treated as an exhaustive ontology.

The institutional design battery is organised into eight attribute families:
formal role, voluntarism, regulatory level, substantive sphere, motivation,
mode of operation, centrality and organisational separation. Legal
independence and supervision are retained as separate design/accountability
indicators. `responsibilization_present` and `empowerment_present` are
independent strategy fields. Values that cannot be observed from the supplied
legal text use `NOE`, and no autonomy or accountability index is computed.

Actor roles are relationship-specific. The same actor may be R, I or T in
different reconstructed relationships; rule source, standard setter, direct
regulator, oversight authority, enforcement authority, intermediary and
target are distinct fields where evidence supports the distinction.

## Corpus

The unit of legal source is a known CELEX record collected directly from
EUR-Lex. The corpus contains CSRD (`32022L2464`), EU Ecolabel (`32010R0066`),
Climate Benchmarks (`32019R2089`), ETS Verification (`32018R2067`) and the
exploratory Taxonomy Regulation (`32020R0852`). Exact HTML responses and
SHA-256 hashes are preserved in `data/`.

This is a purposeful methodological sample, not the target population. A
future study must define that population before retrieval. SPARQL/Cellar
solves retrieval, not population definition. Base acts, amendments and
consolidated/versioned records must be deduplicated explicitly.

## Pipeline

1. `collect_v4.py` retrieves the English HTML and writes the manifest.
2. `screening_v4.py` tracks the carrier article and applies independent
   ontology-labelled lexical patterns.
3. `prepare_samples_v4.py` selects four held-out article units per act with
   seed `20260906`, excluding articles already used by v3 candidates.
4. A2 flags possible semantic candidates; B1 reconstructs actors and
   relations; B2 applies the five conditions; C proposes individual
   institutional attributes only for positive relationships.
5. Every AI unit is intended to run three times. Disagreement routes to human
   review; there is no silent majority vote.
6. AI output is append-only evidence for review. It cannot write to an
   authoritative candidate or relationship CSV.

## Results and boundary

The lexical layer is complete and reproduces the four-act baseline exactly at
1,079 rows, with 13 additional Taxonomy hits. The current authoritative
relationship table contains the seven validated v3 relationships. The new
20-unit sample remains pending human adjudication, so no Taxonomy R-I-T
relationship is asserted. The attempted live API generation was stopped by
the provider's `credit_balance_exhausted` response; the 201 dry-run calls are
only schema/orchestration tests.
