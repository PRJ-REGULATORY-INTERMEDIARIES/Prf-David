# Case Selection Protocol — Production v1.0

## Purpose

This protocol defines how the three empirical cases are selected before production coding. A `case` is one EU legislative act and one frozen legal corpus. Selection is a design decision, not an output of Claude, Luna, keyword screening, or an earlier benchmark.

## Required sequence

1. Reserve three case slots in `cases/CASE_REGISTRY.yaml`.
2. Define and record the selection criteria before reading production coding outputs.
3. Select one official EU legislative act for each slot, using a stable CELEX identifier.
4. Record the title, date, domain, rationale, official URL, source hash, and corpus hash.
5. Acquire and freeze the official source and its normalized corpus.
6. Record the case as `source_locked`, then `corpus_locked` only after integrity checks.
7. Use the same versioned Claude and Luna prompts for all three cases.

## Selection criteria

The researcher should document, before coding, criteria such as:

- relevance to the substantive research question and declared EU/climate domain;
- a stable CELEX identifier and accessible official EUR-Lex text;
- a clearly bounded legislative act suitable for a complete frozen corpus;
- sufficient institutional and normative variation to support comparative interpretation across cases;
- manageable scope for complete reading and auditable evidence capture; and
- diversity of regulatory instruments, obligations, procedures, or governance arrangements where this is part of the research design.

The researcher should also state exclusions, language/version choices, and any temporal or legal-form boundaries.

## Prohibited selection bases

Do not choose cases based on:

- known or expected intermediaries;
- the number of keyword hits;
- prior Claude, Luna, Terra, human, or benchmark results;
- the expectation of positive R–I–T relations;
- convenience created by a desired result; or
- silent substitution of a consolidated version, corrigendum, delegated act, or related instrument.

If the repository does not unequivocally define a case, leave it as `PENDING_RESEARCHER_SELECTION`. Do not select Case 02 or Case 03 automatically. The act and corpus must be frozen before any primary coding begins.

## Change control

The same `CLAUDE_PRIMARY_CODER.md` and `LUNA_SECONDARY_REVIEWER.md` are used for all cases. A necessary prompt or codebook change must be versioned, documented, justified, and preferably reapplied to every case. No prompt is adapted after observing Case 01 results without this change control.
