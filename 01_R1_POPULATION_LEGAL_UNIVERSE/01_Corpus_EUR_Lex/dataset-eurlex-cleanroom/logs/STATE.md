# Pipeline state

```
setup → source_acquired → corpus_locked → methodology_locked →
primary_complete → secondary_blind_complete → cross_review_complete →
awaiting_human_validation → human_validated → final_dataset_locked
```

**Current state: `corpus_locked`**

## History

| date (UTC) | transition | notes |
|---|---|---|
| 2026-09-09 | setup → source_acquired | 3 acts downloaded fresh from EUR-Lex/CELLAR content negotiation. See `phase_01_source.md`. |
| 2026-09-09 | source_acquired → corpus_locked | Deterministic Markdown generated and validated for all 3 cases. See `phase_02_corpus.md`. |

## Next gate

`corpus_locked → methodology_locked` requires the researcher to instruct
creation of `methodology/METHODOLOGY_LOCK.md`, `CODEBOOK.md`,
`coding_schema.json`, `actor_role_schema.json`, `mechanism_taxonomy.yaml`,
and the three locked prompts. **Do not create these, and do not run any
LLM coding pass, without that explicit instruction.**
