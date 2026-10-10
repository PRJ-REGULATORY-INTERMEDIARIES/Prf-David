# Task entrypoints

The implementation lives in src/rio and is installed with `pip install -e '.[dev]'`. Run scripts from the repository root, or prefer the equivalent `python -m rio` commands documented in README. Wrappers delegate to that shared implementation so validation/export behavior does not diverge.

- database/initialize.py → init
- validation/validate.py → validate
- import_export/export.py → export
- utilities/load_synthetic.py → load-synthetic

These utilities perform no real-data collection or remote actions.
