# R1_DIFFERENCES — prompt premises vs evidence, and historical vs fresh

| # | Premise (master prompt §1) or earlier description | What the evidence shows | Classification |
|---|---|---|---|
| D1 | "R1: survey of normative acts and delimitation of a calibration corpus from EUR-Lex" | Confirmed in part. R1 had two branches: (a) a national multi-source discovery branch (EEA, OECD, CCLW, …, 35 sources; 4,010 instruments; **0 EU-level**), frozen as a discovery asset; (b) a separate EU-level CELEX/Cellar branch that produced P4 = 35 acts. EUR-Lex/Cellar was one of 35 discovery sources and the backbone of branch (b) only | REFINEMENT |
| D2 | "reports on population, selection criteria and search strategies" | One consolidated report (13 Sep) covers all three. The underlying datasets are not located | EVIDENCE_GAP |
| D3 | S2 five-case sample = R2 corpus | **Different.** S2 (R1 ¶89) contains 32000D0293. The R2 lock (learning log, 13 Sep, line 269) replaces it with **32015D1814**. No file documents why 32015D1814 was chosen or whether it belongs to P4 | EVIDENCE_GAP (open) |
| D4 | Exclusion of 32000D0293 as a historical false positive | Confirmed: R1 ¶90 flags it; the learning log records the exclusion; R3 governance forbids reintroduction; the fresh official text confirms the Daphne programme | VERIFIED (fresh) |
| D5 | R1 numbers can be re-run | No. The query logs are partly illustrative (¶57); EUR-Lex search blocks scripted access from this environment (I-002); and the intermediate datasets are missing | NOT_REPRODUCIBLE_IN_THIS_RUN |
| D6 | Earlier cross-project summaries that describe R1 as "5 acts, TEXTS_VERIFIED" | `TEXTS_VERIFIED` belongs to the **R2 start** (learning log, 13 Sep), not to R1. It certifies text acquisition only (see `03_R2/R2_REPLICATION_NOTE.md`) | LABEL_SCOPE_CORRECTION |
