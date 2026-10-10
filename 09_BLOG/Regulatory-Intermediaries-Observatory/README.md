# Regulatory Intermediaries Observatory

**Proposed project · Phase 01 · DRAFT — NOT VALIDATED**

RIO is a local research infrastructure for identifying and comparing regulatory intermediation with traceable evidence. Track A inventories existing datasets and documentary resources. Track B models original regulatory episodes, contextual actor roles, directed relationships, instruments and evidence. A catalog entry never establishes an empirical RIT relationship.

No empirical data have been collected. The only bundled records are labeled synthetic fixtures. No affiliation, authorship, scientific approval, license, remote repository or public release is implied. RGAM/V8 remains independent.

## Quick start: Windows, PowerShell and VS Code

Required: Python 3.11+, Git, Quarto CLI and optionally VS Code with Python and Quarto extensions. Run commands from this repository root. Runtime Python uses only the standard library; pytest is a development dependency. The editable install expects this full checkout, including `database/schema.sql`.

```powershell
code .
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e '.[dev]'
.\.venv\Scripts\python.exe -m rio init
.\.venv\Scripts\python.exe -m rio validate
.\.venv\Scripts\python.exe -m pytest -q
quarto render website
quarto preview website --host 127.0.0.1 --no-browser --no-watch-inputs
```

Stop preview with Ctrl+C. On this synchronized Drive, automatic preview regeneration produced intermittent directory-cleanup warnings and one initial HTTP 500. The documented preview command subsequently served all six pages successfully. If a filesystem lock recurs, render once and serve the finished files with `.\.venv\Scripts\python.exe -m http.server 4321 --bind 127.0.0.1 --directory website/_site`; open `http://127.0.0.1:4321/`. For long-term development, consider a separately approved non-synchronized checkout. Open the loopback URL printed by Quarto. Environment activation and changes to PowerShell execution policy are unnecessary. `init` refuses an existing database, preserving its contents. The default database is `data/working/rio.sqlite`; leave it empty until research intake is authorized.

Test the synthetic pipeline in a separate database:

```powershell
.\.venv\Scripts\python.exe -m rio init --db data/working/synthetic.sqlite
.\.venv\Scripts\python.exe -m rio load-synthetic --db data/working/synthetic.sqlite
.\.venv\Scripts\python.exe -m rio validate --db data/working/synthetic.sqlite
.\.venv\Scripts\python.exe -m rio export --db data/working/synthetic.sqlite --out data/processed/synthetic-demo
```

Each export requires a new destination. CSV and JSON snapshots are deterministic; JSON preserves NULL versus empty string. Exports include checksums. Never load the fixture into an empirical database. There is no automatic real-data ingestion or network collection command.

## Research workflow

1. Review the draft scope, codebook and governance before any collection.
2. Track A: record each search, screening decision and verified source metadata using the templates in `protocol/scoping_review/`.
3. Preserve permitted source files internally with access date, version and content hash. Review shared-drive access independently of Git exclusions.
4. Track B: allocate immutable IDs, create candidate records and typed rows together in a transaction, and attach documentary evidence to each coded claim. Open connections through `rio.storage.connect` to enforce foreign keys.
5. Code, independently review, resolve disagreements with append-only decisions and validate. Technical checks do not confer scientific validation.
6. Prepare a curated complete database for any proposed release. Every included record and dependency must be validated, explicitly public-eligible and non-synthetic. Keep internal audit decisions intact.
7. Follow the explicit, snapshot-bound authorization workflow in `docs/governance/release.md`. Public export only stages local files; publication is a separate future decision.

## Repository guide

| Directory | Function |
|---|---|
| `docs/concept`, `docs/architecture`, `docs/decisions`, `docs/governance` | Scope, design, auditable choices and human approval boundaries |
| `protocol/` | Draft search, selection, coding and validation procedures |
| `codebook/` | Draft operational definitions and field dictionary |
| `database/` | Versioned schema and migration policy |
| `src/rio/` | Tested Python implementation and command-line interface |
| `scripts/` | Small task entrypoints delegating to the shared implementation |
| `data/raw/` | Original permitted inputs; ignored by Git |
| `data/working/` | Local SQLite databases and private work; ignored |
| `data/processed/` | Internal exports; ignored |
| `data/public/` | Explicitly approved local staging only; ignored until a separate release decision |
| `data/synthetic/` | Versioned, labeled test fixtures only |
| `tests/` | Integrity, traceability and release-boundary checks |
| `reports/` | Technical execution, validation evidence and methodological pending decisions |
| `website/` | Local Quarto site and technical blog scaffold |
| `references/` | Provenance of supplied specification and unverified reference leads |

See `PROJECT_STATUS.md` for actual execution results, and `reports/technical/phase-01.md` for the execution report and actual source tree. No `.env.example` is needed: the project has no secrets or environment configuration. No license has been assigned. This is a nested, independent Git repository inside an existing workspace; use `git -C` or work from this root to avoid confusing repositories. No parent Git configuration was changed.
