# CASE_SELECTION_PROTOCOL (R07)

## 1. Eligible universe
An act–intermediary pair is **eligible** if all three conditions hold:
1. **E-a:** Rotem's implemented workbook (L3) contains a substantive intermediary coding for it, either an act-level `Coding Digital Intermediaries` (CDI) row or an intermediary-level `List of actors` (LoA) row.
2. **E-b:** the official text is verifiable in this run (Cellar download and/or local R4 copy).
3. **E-c:** it falls within Rotem's codebook scope (EU digital governance, REV ¶13).

| Pool | Eligible units | Notes |
|---|---|---|
| PILOT_03 acts with CDI rows | 10 acts: 76/889, 86/361, 87/95, 89/336, 91/263, 92/44, 2004/48, 874/2004, 1781/2006, 2006/115 | All 10 official texts fetched. Human relational decisions exist for 9 of them (not 2004/48) |
| DSA (2022/2065) LoA rows | 21 intermediary-level rows, all with article references | DSA text: Cellar + R4 local copy (all sentences of Arts 22, 37 and 42 match) |
| P2B (2019/1150), CDSM (2019/790) LoA/LoI rows | 13 rows | Official texts not fetched in this run; not needed for coverage |
| **Not eligible** | R2/R3 climate acts (outside Rotem's scope, E-c); GDPR / AI Act (no Rotem coding, E-a) | — |

## 2. Selection criteria (purposive, stated ex ante)
- **S1.** Each of the coverage dimensions A–E of the master prompt (§6 R07) is covered by at least one case as PRIMARY.
- **S2.** Prefer acts with pre-existing **human** relational decisions (PILOT_03), so that the comparison is differential against a human baseline and does not rest only on our model coding.
- **S3.** Include **at least one case in which Rotem's own unit (intermediary × act) is implemented** (LoA). Otherwise the test would only compare against the act-level packing that her revised codebook already abandons.
- **S4.** Include Rotem's insurance example only if a real act supports it. Directive 89/336/EEC Annex II point 5 does ("possession of civil liability insurance unless such liability is covered by the State under national law"), and so does 91/263/EEC Annex V point 6.
- **S5.** Maximum 6 cases. Every case must have every coded provision in a verbatim pack (`case_texts/`).

**Not a selection criterion:** the expected outcome of the comparison. The sample is purposive and **not statistically representative**. It cannot support prevalence claims ("how often Rotem's schema loses information").

## 3. Selected cases
`CASE_REGISTER.csv` details each case; `COVERAGE_MATRIX.csv` gives the coverage.

| Case | Act | Primary dimension | Human baseline | Rotem unit |
|---|---|---|---|---|
| CASE_01 | Reg. 874/2004 (.eu): auditor, validation agents, ADR providers | A, D | H_015, H_016, H_017 | act-level packed |
| CASE_02 | Dir. 89/336/EEC: competent bodies, notified bodies, insurers | B | H_009, H_010 | act-level packed |
| CASE_03 | Dir. 91/263/EEC: notified bodies, test labs (insurers) | C | H_011–H_014 | act-level packed |
| CASE_04 | Dir. 86/361/EEC: approved testing laboratories | E | H_001, H_002 | act-level (single) |
| CASE_05 | DSA Art 37 (+42(4)): independent audit organisations | A, C, E | none | **intermediary × act** |
| CASE_06 | DSA Art 22: trusted flaggers | B, C, E | none | **intermediary × act** |

**Count of real cases: 6. No case is hypothetical.** No `ILLUSTRATION_ONLY` case was needed.

## 4. Eligible but excluded (with reason)

| Unit | Reason for exclusion | Use in this run |
|---|---|---|
| 76/889/EEC Art 3(2) (H_006–H_008) | Axes D/E already covered by CASE_01 and CASE_04 | Supplementary illustration in E7 (legal effect vs actor edge) |
| 92/44/EEC Art 11 (H_003) | The PILOT_03 actor (national regulatory authority) is a public authority, i.e. a *regulator* under REV ¶31. Rotem's intermediary for this act (telecommunications organisations) is a different actor | Boundary illustration in E5 (transmission by a regulator ≠ intermediation) |
| 2006/115/EC Art 5(4) (H_004) | Modality is covered by CASE_04/05/06 | Supplementary illustration in E7 (legal possibility vs instantiation) |
| 1781/2006 Art 18 (H_018/H_019) | Alternative-condition safeguards; overlaps with CASE_02 on status | Mentioned in E3 |
| 87/95/EEC (H_005); 2004/48/EC (no human decision) | Coverage already met | — |
| DSA Art 21 out-of-court dispute settlement bodies | Coverage met by CASE_06 | Recognition value 'Certification' discussed in E3 |
| DSA Art 40 vetted researchers, other LoA rows | Coverage met | — |

## 5. Insufficiency statement
Coverage of A–E is met with real cases. Remaining limits:
- **(i)** Two cases (CASE_05 and CASE_06) have **no human relational baseline**. All relational coding there is `MODEL_CODED`.
- **(ii)** No case comes from P2B or CDSM.
- **(iii)** With n = 6 purposive cases, results are **case-illustrative, not population estimates**.
