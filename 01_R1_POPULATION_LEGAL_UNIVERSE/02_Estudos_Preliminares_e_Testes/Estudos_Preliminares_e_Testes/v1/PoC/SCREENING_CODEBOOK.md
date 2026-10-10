# Screening codebook (Stage A — candidate detection layer)

This is the renamed, reframed pointer to `CODEBOOK.md`, kept as the single
canonical source of the lexical patterns, counts and examples (not
duplicated here to avoid the two files drifting apart). What changes here is
the framing, not the patterns themselves.

## What this layer is, and is not
Stage A (this codebook) answers: *does this paragraph contain a textual
signal associated with one of Levi-Faur's four primary mechanisms?* It is a
**candidate detection layer** — it locates provisions worth reading closely.
It does not, on its own, establish that a regulatory intermediary exists;
that determination belongs to Stage B (`RIT_CODEBOOK.md`,
`data/rit_coded_sample_v2.csv`).

## Two additions to how each pattern should be read
1. **`semantic_role`** (already present in `CODEBOOK.md` as the "Ontologia"
   column: `ator`/`mecanismo`/`instrumento`) — only patterns tagged **ator**
   point directly at a Stage B intermediary candidate. A pattern tagged
   **mecanismo** or **instrumento** locates relevant context, not a
   candidate actor.
2. **`candidate_mechanism`** — the mechanism field emitted by
   `codebook_screen.py` (`reportar`/`certificacao`/`ranking_rating`/
   `auditoria`) should be read as *candidate* mechanism, not confirmed
   mechanism — the same relabeling already applied to `screening_confidence`
   (`high`/`low`, never "confirmed") in METHODOLOGY_v2.md, section 11.

## Where the actual patterns live
`CODEBOOK.md` — unchanged: anchor/weak/exclusion patterns, per-pattern
counts from the 4-act run, real evidence examples, and the
actor/mechanism/instrument tag per pattern. Read it alongside this file, not
instead of it.
