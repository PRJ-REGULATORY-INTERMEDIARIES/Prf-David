# EU Regulatory Data Landscape — Research Repository

**Status:** DRAFT v1.0 — preregistration and team approval required before systematic execution.
**Date of scaffold:** 2026-10-09. **Language of protocol:** Portuguese; manuscript target: English.

## Research proposition

**Mapping European Union Legislative and Regulatory Datasets: A Scoping Review of Data Infrastructures and Their Capacity to Represent Regulatory Governance Architectures.**

This repository hosts the materials for an evidence-mapping scoping review plus a reproducible technical audit. It can yield one peer-reviewed scoping review with deposited supplementary dataset and code. The optional RIT/RGAM/V8 mapping is a separately labelled exploratory feasibility probe, not a validated benchmark.

**Caution:** The 41 entries in `inputs/seed_inventory_v0_1.csv` were imported from a previous exploratory map. They have **NOT** passed systematic search, duplicate removal, full source screening, access testing, or quality auditing. Do not report them as 41 independent eligible datasets.

## Quick start — VS Code

1. Open **this folder** in VS Code (File → Open Folder), with Python >= 3.10.
2. In integrated terminal run:
   ```bash
   python scripts/cli.py check
   python scripts/cli.py import-seeds
   python scripts/cli.py check
   python scripts/cli.py report
   python -m unittest discover -s tests -v
   ```
3. Read `protocol/PROTOCOL_v1_0_DRAFT.md` and `protocol/DECISIONS_TO_FREEZE.md`, get team feedback, and **freeze the protocol as v1.0** (git tag or OSF registration) **before** systematic searching.
4. Record search queries and exported search results in `data/search_runs.csv` and `data/discovery_records.csv`. See `protocol/SEARCH_STRATEGY.md`.
5. Complete deduplication, independent screening, data charting, technical audit, and adjudication; `python scripts/cli.py check` reports integrity issues rather than pretending review is complete.
6. Use `python scripts/cli.py report` for a status report and intermediate study flow summary. Fill `manuscript/MANUSCRIPT_SKELETON.md` only with validated results.

Run an **optional** API query **only after methodological approval**:
```bash
python scripts/eu_data_api.py --query 'EU legislation' --limit 25
```
This uses the officially documented `data.europa.eu` search endpoint. It writes the **uninterpreted response** into `data/raw/api/`; it neither screens nor labels any result. Internet access is required; API behavior and terms must be checked at execution time.

## Boundaries

- No autonomous legal inference or LLM-based final eligibility decisions.
- No inferred dataset licenses; missing access evidence is `UNVERIFIED`, never zero.
- No automatic normalization of CELEX/ELI into unverified legal relationships.
- No rehosting of restricted texts or source datasets.
- No publication claim before external validation, coder agreement and access/legal compliance.
- Analyses count **unique included datasets** separately from **portals/APIs/resources**.

## Execution with a coding agent

Copy `PROMPT_MESTRE_VSCODE.md` to your VS Code agent to stage the calibration and protocol-freeze tasks. It forbids fabricated records and independent LLM adjudication.

## Folder index

- `protocol/`: research protocol, exact search planning, screening/codebook, audit, risk control and publication gates.
- `inputs/`: original exploratory spreadsheet, 41-resource seed CSV, and draft search queries.
- `data/`: empty research tables for verified execution and optionally initial seed discovery records.
- `scripts/`: standard-library CLI for integrity/QC and provenance-safe import; optional API discovery.
- `tests/`: reproducibility smoke tests.
- `manuscript/`: English article skeleton, with explicit placeholders rather than fabricated findings.
- `outputs/`: generated status reports.

## Attribution and reproducibility

Team must approve authorship, funding statement, conflict-of-interest disclosure, license selection, and repository release. Suggested archival versioning: GitHub release + Zenodo DOI. The prior exploratory spreadsheet is kept unaltered as a provenance artifact, not the final evidence registry.
