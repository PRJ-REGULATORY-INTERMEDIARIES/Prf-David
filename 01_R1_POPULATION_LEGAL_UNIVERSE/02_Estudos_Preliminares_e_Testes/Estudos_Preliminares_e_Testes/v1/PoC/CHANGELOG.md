# Changelog

## v2 — 05/09/2026 — relational restructuring (R-I-T)
Triggered by a detailed methodological review arguing that v1 built a
mechanism-*screening* system, not intermediary *coding*: the unit of
analysis was paragraph×mechanism, when the proposal's actual question is
"who is the intermediary, between which regulator and target, under what
institutional design?"

**Changed:**
- Unit of analysis: `paragraph × mechanism` (Stage A only) → **R-I-T
  relationship** as the substantive unit (Stage B), with Stage A explicitly
  reframed as a candidate-detection layer feeding it.
- New relational-architecture principle: actor roles are relational, not
  intrinsic — the same actor can be `I` in one relationship and `T`/`R` in
  another (demonstrated in ETS-R1/ETS-R2).
- New chain representation (`chain_id`, `intermediation_level` `L1`/`L2`,
  `upstream_relationship_id`) for meta-regulation cases (an intermediary
  governed by another intermediary), demonstrated in three of the four
  acts (CSRD, Ecolabel, ETS), not only the one found in v1 (ETS).
- Explicit relational test applied to every candidate, including two
  deliberate **negative** cases (CSRD-R3: reporting without an intermediary;
  ECO-R3: an advisory body that fails the test) — negatives are evidence the
  test works, not gaps.
- Terminology: `status`/`verificar_humano` → `screening_confidence`
  (`high`/`low`); "gold standard" → "pilot reference sample"
  (`VALIDATION_PROTOCOL.md`).
- Ontology separation formalised as `semantic_role` (actor/mechanism/
  instrument) in `SCREENING_CODEBOOK.md`, with the explicit rule that only
  "actor" patterns point to a Stage B candidate.
- Climate Benchmarks kept as an open, explicitly `conditional` construct-
  validity case (`CB-R1`) rather than a confirmed canonical example.
- New deliverables: `RIT_CODEBOOK.md`, `DATA_DICTIONARY.md`,
  `VARIABLE_MAP.md`, `VALIDATION_PROTOCOL.md`, `METHODOLOGY_v2.md`,
  `SCREENING_CODEBOOK.md`, `data/rit_coded_sample_v2.csv`,
  `Research_Note_Intermediary_Coding_EN_v2.md`/`.docx`.

**Not changed / deliberately not expanded:**
- No new acts collected — same four (CSRD, Ecolabel, Climate Benchmarks,
  ETS Verification). Nine well-justified relationships were preferred over
  a larger, shallower set (see `METHODOLOGY_v2.md`).
- Stage A screening data (`data/combined_dataset.csv`, 1,079 rows) is
  unchanged from v1 (05/09/2026, earlier session) other than the field
  renaming already applied there.
- The autonomy and accountability indicator batteries are defined
  (`DATA_DICTIONARY.md`) but not populated — scoped for the next round with
  a second coder, not fabricated for this pilot.
- Stage B has not been independently validated by a second coder
  (`VALIDATION_PROTOCOL.md`).

## v1 — 05/09/2026 — initial PoC (superseded)
Lexical screening (Stage A) of four EU acts by CELEX, one per mechanism
(reporting/certification/ranking-rating/auditing), with anchor/weak/
exclusion rules and a paragraph-level pilot precision/recall check. Kept for
the record: `RIT_CODING.md`, `GOLD_STANDARD_VALIDATION.md`,
`CODEBOOK.md`, `Candidatura_Research_Assistant_Intermediarios_UE/
06_research_note_intermediary_coding_EN.md`/`.docx`.
