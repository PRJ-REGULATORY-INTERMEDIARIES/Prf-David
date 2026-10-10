# Phase 01 validation record

Date: 2026-10-09. All database test material is synthetic.

Command executed from repository root: `.\.venv\Scripts\python.exe -m pytest -q`

```text
..........................                                               [100%]
26 passed in 0.89s
```

Exit code: 0. Coverage includes initialization/no overwrite, missing database refusal, required tables, primary-key uniqueness, foreign-key/value constraints, same-episode role endpoints, multiple intermediaries and evidence links, append-only coding decisions, fixture rollback/preservation, deterministic CSV/JSON, directory separation, public denials, stale authorization refusal, simulated approved staging in temporary test storage, missing validation evidence, orphan identities and externally corrupted foreign keys.

Integration commands executed: rio init; rio init --db data/working/synthetic.sqlite; rio load-synthetic --db data/working/synthetic.sqlite; rio validate --db data/working/synthetic.sqlite; rio export --db data/working/synthetic.sqlite --out data/processed/synthetic-demo. Each exited 0. The default empty database also passed rio validate. The script wrapper scripts/validation/validate.py passed on the synthetic database.

Quarto render initially reported missing team.qmd while that file was not yet created. After completing the page, the final `quarto render website` rendered six documents and exited 0 without warnings. The first HTTP preview check returned 500; a subsequent preview using --no-watch-inputs returned 200 for all six pages and passed local link/resource checks. Directory-cleanup warnings occurred on the synchronized Drive; underlying filesystem cause was not established. See website-checks.json for the successful HTTP observations. No browser visual inspection was performed.

Git initialization succeeded; git remote -v returned no remotes. git check-ignore confirmed exclusion of the virtual environment, local databases, processed snapshot and built website. No pytest failure or missing dependency remains. The original DOCX text extraction needed UTF-8 stdout after the default Windows encoding failed; no source document was changed.
