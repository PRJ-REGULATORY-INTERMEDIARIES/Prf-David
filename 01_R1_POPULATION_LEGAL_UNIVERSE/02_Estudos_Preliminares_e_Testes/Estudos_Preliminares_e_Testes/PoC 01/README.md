# PoC 01 — Final Research Package: Regulatory Intermediary Coding

Complete package for a regulatory-intermediary coding exercise using EU green-transition legislation, based on a research proposal by Professor David Levi-Faur. The package preserves both validated and provisional work; see the distinctions below.

## `Entrega-02/` — Human coding, v3 (validated within the original exercise)

The main material for reading and further use:

- **`ARTIGO_VALIDACAO.qmd` / `.docx`** — academic-paper format (Abstract → Introduction → Methods → Results → Validation → Discussion → Conclusion), including figures and tables. Recommended starting point.
- **`RELATORIO_FINAL_APRESENTACAO.qmd` / `.docx`** — an extended, step-by-step presentation report.
- **`RESEARCH_NOTE_v3.md` / `.docx`** — concise English research note prepared for Professor Levi-Faur.
- **Codebooks and methodological documentation:** `RIT_CODEBOOK_v3.md`, `SCREENING_CODEBOOK_v3.md`, `DATA_DICTIONARY_v3.md`, `VARIABLE_MAP_v3.md`, `METHODOLOGY_v3.md`, `SCREENING_VALIDATION_v3.md`, `RELATIONSHIP_VALIDATION_PROTOCOL_v3.md`, `CHANGELOG_v3.md`.
- **`scripts/`** — reproducible pipeline (`collect.py`, `screening_v3.py`).
- **`data/`** — three main pipeline datasets (`screening_hits_v3.csv` — 1,079 rows; `candidate_adjudications_v3.csv` — 10 candidates; `rit_relationships_v3.csv` — 7 R–I–T relationships), plus `actors_v3.csv`.
- **`figures/`** — four figures used in these research documents.

## `Entrega-03/` — AI-assisted coding layer (protocol ready; not yet executed at that stage)

Complete design (protocols, JSON Schemas, prompts and orchestration scripts) for incorporating an LLM as an assisted interpretive coder. The pipeline passed an end-to-end `dry_run` test without a real API request or cost. **No real model output was available at the time this archived version was prepared.** See `Entrega-03/CHANGELOG_v4.md` and `Entrega-03/MODEL_SELECTION_PROTOCOL.md` for historical prerequisites, including checking the chosen `model` identifier and prevailing API price.

## Materials intentionally excluded

- **`../v1/`** — superseded v1/v2 exercise versions, retained separately for historical traceability and not copied into this package.
- **`../Inputs/`** — source materials provided directly by Professor David, including his original `.docx` proposal and a WhatsApp flyer containing personal contact information. These inputs are not a product of this coding exercise.

## Relative-path dependency

`Entrega-02/` and `Entrega-03/` must remain sibling directories within the same parent folder. Scripts and documentation in `Entrega-03/` reference `../Entrega-02/...`. Do not move one without the other.

The original directory names are preserved because changing them would break existing research references.
