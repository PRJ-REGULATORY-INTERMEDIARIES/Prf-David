# R2_REPLICATION_NOTE — R2 corpus control (historical round R2, "calibração conceitual")

## 1. Verified facts (re-executed in this run)
`R2_CORPUS_RECONCILIATION.csv` records the checks, all run 2026-09-30:

| CELEX | Act | C1 PDF hash vs R3 manifest | C2 25 corpus-file hashes vs R3 manifest | C3 article set R3 = official (fresh) | C4 act number in official text |
|---|---|---|---|---|---|
| 32003L0087 | Directive 2003/87/EC (EU ETS) | PASS | PASS (as-is) | PASS (33 = 33) | PASS |
| 32015D1814 | Decision (EU) 2015/1814 (Market Stability Reserve) | PASS | PASS | PASS (5 = 5) | PASS |
| 32018R0842 | Regulation (EU) 2018/842 (Effort Sharing) | PASS | PASS | PASS (17 = 17) | PASS |
| 32021R1119 | Regulation (EU) 2021/1119 (European Climate Law) | PASS | PASS | PASS (14 = 14) | PASS |
| 32023R0955 | Regulation (EU) 2023/955 (Social Climate Fund) | PASS | PASS | PASS (29 = 29) | PASS |
| 32000D0293 | Decision 293/2000/EC (Daphne programme) — excluded | n/a | n/a | n/a | PASS; 0 climate/greenhouse/emission/environment terms, 47 × "violence" |

**Scope of the check.** The R3 corpus files for the five acts are intact against their own manifests, and they are structurally consistent with the official texts downloaded today. This check does **not** verify the substantive coding built on them (that is R04).

## 2. Chronology of R2, reconciled

| Date | Event | Source |
|---|---|---|
| 13 Sep | "Início da R2". After a historical false positive was excluded, the corpus was locked at five acts; status recorded as `TEXTS_VERIFIED`; "A extração estrutural foi preparada para esses casos, ainda sem classificação final dos intermediários" | Learning log lines 267–281 (SRC-LEARNLOG) |
| 13–17 Sep | What R2 actually executed was a **calibration on the EU Taxonomy Regulation (32020R0852)**, "outside the five substantive R2 cases": 27/27 articles screened, 41 atomic units, 40 relation candidates (28 RIT-eligible, 10 non-RIT, 2 uncertain; 5 support intermediation, 7 direct, 18 uncertain); 26 audit findings from a separate auditing model in Excel; David validation package v1.3 (17 Sep) | R2 method report ¶2, ¶7, ¶15, ¶21 (SRC-R2-REPORT); SRC-R2-PKG |
| 15 Sep | The learning log's "Prioridade 1 — Completar R2" still lists, for each of the five acts: "identificar atores; extrair trechos; construir relações…" | Learning log lines 1221–1231 |
| 19 Sep | R2.1 (WORK_2_1) re-ran the Taxonomy instrument under an instrument-first design. D4: the five R2 cases "stay outside this execution". It stopped at `PHASE_0B_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION` | `WORK_2_1/PILOT_R2_1/RESEARCHER_DECISION_LOG.md` |
| 20 Sep | R3 Phase 1 re-acquired **fresh** original-OJ PDFs of the five acts (retrieved_at 2026-09-20T16:29…). This was the first executed structural extraction of the five acts (R3 Phase 2) | R3 `SOURCE_MANIFEST.yaml`; R3 Phase 1/2 audits |

## 3. Conflicts and their reconciliation (both versions preserved)

| Conflict | Version A | Version B | Reconciliation |
|---|---|---|---|
| Was structural extraction performed on the five acts in R2? | The protocol row for R2 lists "Extração estrutural, identificação de atores e relações…" as AI tasks (SRC-PROTO-IA, line 55) | The learning log says extraction was "preparada" and later lists it as still to be done. R2.1 Phase 0 (line 47) found the five cases "not defined anywhere" in its 606-file inventory | The protocol row most plausibly describes the **Taxonomy calibration** carried out in R2. No artefact of an R2 extraction on the five acts exists. **Conclusion:** extraction of the five acts first happened in R3. Confidence: moderate (inference from the absence of artefacts; flagged `RECONSTRUCTED_FROM_CONTEXT`) |
| Are the five R2 cases documented? | Learning log (Downloads) lists them with roles | R2.1 Phase 0: "not defined anywhere" | Both are true. The list lived in a Downloads log outside the project tree that R2.1 inventoried. **Documentation-dispersion finding, not a contradiction** |
| What does `TEXTS_VERIFIED` certify? | Text acquisition and verification on 13 Sep | Later stages (R3 corpus validation, extraction, adjudication) carry their own statuses (`CORPUS_VALIDATED_WITH_DOCUMENTED_LIMITATIONS`, etc.) | `TEXTS_VERIFIED` is a historical status for text acquisition only. It is **not** a certificate for any later stage. The 13 Sep texts themselves are not located; R3 used fresh 20 Sep downloads |

## 4. Open items
- Why 32015D1814 was chosen as the fifth act, and whether it is a member of P4: **not documented** (EVIDENCE_GAP, `ISSUES_AND_DECISIONS.csv` I-010).
- The 13 Sep texts behind `TEXTS_VERIFIED`: not located.

## 5. Consequence for the comparison with Rotem
The five R2 acts are EU climate acts, outside the scope of Rotem's codebook (EU digital governance, revised codebook ¶13), and her workbook codes none of them. They are therefore **not eligible** as comparison cases for her coding (R07). They remain relevant only as history of the relational pipeline.
