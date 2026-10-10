# R1_RECONSTRUCTION — historical round R1 ("população e corpus")

**Status: `HISTORICAL_RECONSTRUCTION_NOT_FRESH_REPLICATION`.** One exception: the identity of the S2 sample CELEX was freshly re-verified against official texts (see §4).

## 1. What R1 was
The round definitions come from the project protocol (`PROTOCOLO_USO_IA_R1_R3_PRE_R4_v1_1.docx`, derived text line 54).
- **R1 = "população e corpus"**: assisted search, query and string refinement, candidate screening, verification of acts, and the method report.
- **Human responsibility** (same protocol row): delimiting the universe, choosing the corpus, validating official sources and accepting or rejecting candidates.

## 2. Evidence base
The only substantive R1 document located is the method report `EU_green_regulatory_intermediation_method_progress_report_REVISED.docx` (Downloads; SHA-256 A4472478…; 13 Sep 2026; last_modified_by Igor Caires). Two earlier variants exist with different hashes (see `01_BASELINES/VERSION_MAP.md`).

The R1 working datasets the report cites in Appendix A were **not located** in the project or in the named Downloads files:
- P4 population list
- EU-3 / EU-3.5 / EU-4 outputs
- source registry
- reconciliation crosswalks
- five-case corpus manifest

The planning exploration also reported them absent from OneDrive, Documents and `C:/PROJETOS`; that search was not repeated here. **So no R1 number can be recomputed.** All values in `R1_EVIDENCE_TABLE.csv` are therefore *as documented* (paragraph references `¶n` point to this run's derived text).

## 3. Reconstructed sequence (as documented)
1. **Starting point: the David–Rotem materials** (¶17–¶26). The workbook was audited sheet by sheet. The report concluded that no substantive rule for why laws entered or left the coding set could be recovered (¶26).
2. **National discovery branch** (¶31–¶35, ¶39–¶49): 35 sources → 9,383 raw records → 9,478 normalized → 4,010-instrument master, with 0 EU-level instruments. It was frozen as a discovery asset, not a legal population.
3. **EU-level branch** (¶50–¶53, ¶72–¶80): 3 positive-control CELEX → 80 candidates → 52 canonical acts → 50 eligible (Option A, binding basic acts). The energy frame was `QUERY_UNRESOLVED`.
4. **Working population P4** (¶81–¶85): (climate_core ∪ broad_environment) ∩ Option A = **35 acts**.
5. **Calibration sample S2** (¶86–¶91): `32000D0293, 32003L0087, 32018R0842, 32021R1119, 32023R0955`, "formally awaiting researcher approval". The report itself flags 32000D0293 as the Daphne programme and recommends it be traced back or corrected before approval (¶90).
6. **Deliberate non-actions** (¶92–¶100): no actor, intermediary, mechanism, prevalence or trend coded.

## 4. What was freshly re-verified in this run
| Check | Result | Evidence |
|---|---|---|
| Identity of 32000D0293 | Daphne programme (violence against children, young persons and women); 0 occurrences of "climate", "greenhouse", "emission" or "environment" | `03_R2/R2_CORPUS_RECONCILIATION.csv`; `OFF-32000D0293` |
| Identity of the four other S2 CELEX | Act numbers 2003/87/EC, 2018/842, 2021/1119 and 2023/955 found in the official texts; climate/emission vocabulary present | same |
| R1 description of the workbook (¶24) | Consistent with this run's verbatim export (List of intermediaries 13 rows, List of actors 35 rows) | `01_BASELINES/BASELINE_ROTEM_WB_*.csv` |

## 5. What cannot be verified
- The query logs (the report says some strings are "a reconstructed illustration", ¶57).
- The 80 → 52 → 50 → 35 funnel.
- Membership of each act in P4. This includes whether **32015D1814** (which replaced 32000D0293 in R2) belongs to P4.
- The date and author of the researcher decision that approved the replacement.
- The one "legal-status conflict preserved" (¶79).

## 6. Relation to the present comparison
R1 matters here for two reasons:
- **It shows Rotem's materials were used from the start.** R1 ¶18–¶20 and ¶102–¶104 record that the David–Rotem codebook, workbook and Chart Key were the methodological starting point. It also records that "intermediation is relational" (¶103) was an early *lesson drawn from* those materials. It was not a critique of them.
- **The empirical domains differ.** R1's population is EU *green* legislation. Rotem's codebook scope is EU *digital* governance (revised codebook ¶13). The R2/R3 climate corpus is therefore **outside the scope of Rotem's codebook**, and it is not used as comparison material for her coding in R07–R10 (see `07_CASE_SELECTION/CASE_SELECTION_PROTOCOL.md`).
