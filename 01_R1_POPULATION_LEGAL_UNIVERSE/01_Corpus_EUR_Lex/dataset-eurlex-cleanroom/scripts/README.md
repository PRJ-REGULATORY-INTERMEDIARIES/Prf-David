# scripts/

| script | purpose |
|---|---|
| `acquire_source.py` | Downloads all 3 acts fresh from EUR-Lex/CELLAR (content negotiation on CELEX id); refuses to write anything if the resolved source is not official. |
| `normalize_corpus.py` | Converts each case's `act_official.xhtml` into `act_full.md` / `act_operative.md` / `act_recitals.md` + `corpus_manifest.yaml`. |
| `validate_corpus.py` | Cross-checks every hash and independently re-derives article/recital/annex counts from the raw XHTML to confirm consistency with the manifests and the generated Markdown. |

Run order: `acquire_source.py` → `normalize_corpus.py` → `validate_corpus.py`.
Equivalent checks are also runnable via `pytest ../tests/`.
