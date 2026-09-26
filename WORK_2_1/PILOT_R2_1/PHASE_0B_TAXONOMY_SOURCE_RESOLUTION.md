# PHASE 0B — TAXONOMY SOURCE RESOLUTION
WORK 2.1 / PILOT R2.1 · instrument: Regulation (EU) 2020/852, CELEX 32020R0852 · executed 2026-09-19

## 0B.1 Result in one paragraph
The authoritative legal text of CELEX 32020R0852 **is available and verified**: a legacy copy from the earlier PoC (hash matches its manifest) and an independent fresh download from EUR-Lex/CELLAR today have byte-different markup but **identical extracted text** (124,151 characters; 27 articles, 60 recitals, no annex detected). The previous Taxonomy pilot materials **were located** in `Downloads` and in a second repository on OneDrive, and were inventoried, hashed and closed under the firewall. One item is **not found**: David Levi-Faur’s original feedback as a standalone source.

## 0B.2 Legal source (T1)

| File (in `00_source/32020R0852/`) | Bytes | SHA-256 |
|---|---|---|
| `act_official_legacy_PilotA_2026-09-06.xhtml` | 339,583 | `B006E305…9B531F2` (full hash in `SOURCE_MANIFEST.yaml`) |
| `act_official_fresh_2026-09-19.xhtml` | 337,514 | `9CF32A28…F8E5A6` |

- Legacy copy is byte-identical to `Before_R2/Estudos Preliminares e testes/PoC 01/Entrega-04/data/raw_html/taxonomy_raw.html`; its hash equals the one in that folder’s `CELEX_MANIFEST_v4.json` (acquired 2026-09-06, original OJ text, not consolidated).
- Fresh copy: `http://publications.europa.eu/resource/celex/32020R0852` → 303 → `…/cellar/e5ba36a8-b454-11ea-bb7a-01aa75ed71a1.0006.03/DOC_1`, HTTP 200, `application/xhtml+xml`, same content-negotiation method the clean-room project used. Both files carry the same converter stamp (CONVEX 9.15.0, generated 2023-12-07) and document id `L_2020198EN.01001301.xml`.
- Equivalence: after stripping head/scripts/styles/tags and normalising whitespace, the two texts are identical. The 2,069-byte difference is markup only; cause not diagnosed.
- This is the reverse of the CBAM/EUDR case in Phase 0 (issue I1): there the texts were not compared.
- **Proposed designation** (needs your confirmation): legacy copy = primary (same bytes the earlier Taxonomy PoC used, hash locked); fresh copy = verification copy.

Not verified: official article/recital counts against the Official Journal (Phase 1 should confirm 27 / 60); later amendments or corrigenda to the act; consolidated versions; whether the Pilot A workbooks themselves were coded on this text (closed).

## 0B.3 Previous Taxonomy pilot materials (inventoried, not read)

| Group | Location | Status |
|---|---|---|
| **Pilot A candidate — package sent to David**: `R2_DAVID_VALIDATION_PACKAGE_v1_3.zip` (2026-09-17; members: method note `.docx`, `R2_calibration_…_v1_3_researcher_adjudicated.xlsx`) | `C:\Users\Adm\Downloads` | closed |
| **Pilot A candidates — earlier versions**: `R2_calibration_regulatory_intermediation_v0_2_descriptive.xlsx`, `…_v1_2_audited.xlsx`, `R2_METHOD_REPORT_TAXONOMY_CALIBRATION_v1_2.docx` (2026-09-15) | `C:\Users\Adm\Downloads` | closed |
| **Post-David recalibration v1.4** (2026-09-18): workbook, method note, changelog, codebook, validation report, `build_pilot_v14.py` | `C:\Users\Adm\OneDrive\ICM-Gov\05_PROJETOS\prj-intermediaries\` (own git repo; the v1.4 files are untracked) | closed; **not Pilot A**, a later attempt after feedback |
| Legacy multi-act PoC (Taxonomy is 1 of 5 acts): `Entrega-04/data/*_v4.csv` etc. | `Before_R2/Estudos Preliminares e testes/PoC 01/Entrega-04` | closed |
| Context documents that may hold David’s feedback or the Pilot A narrative: `PROJECT_LEARNING_LOG_PRJ_DAVID_LEVI_FAUR.md`, `Meeting Briefing — David Levi-Faur.pdf` | `Downloads` | closed pending your designation |

Identity of Pilot A among the candidates is **inferred from names and dates** and needs your confirmation: the one submitted to David appears to be `v1_3` in the `R2_DAVID_VALIDATION_PACKAGE_v1_3.zip`, with v0_2 and v1_2 as its predecessors. Nothing marked `40 candidate relations` was found in any text file; `41 atomic` matches only the v1.4 method note and build script.

Machine-readable: `PHASE_0B_SOURCE_INVENTORY_ADDENDUM.csv` (28 rows) and `FIREWALL_REGISTER.csv` (20 closed files, with hashes).

## 0B.4 What I actually touched under the firewall (disclosure)
- Listed names, sizes, dates and SHA-256 of every file above.
- Listed member **names** of the v1_3 zip; did not extract it.
- For the v1.4 workbook: read sheet **names** (`README, DECISION_LOG_v1_4, RELATIONS_v1_4, MECHANISM_AUDIT, ADVICE_EXPERTISE_BOUNDARY, NEGATIVE_BOUNDARY_CASES, V1_3_V1_4_CHANGES, MECHANISM_DICTIONARY, UNCERTAIN_CASES, DATA_DICTIONARY`) and a true/false check for the string `2020/852` (true; `Taxonomy` and `32020R0852` false; the three other locked CELEX ids false). No cell content read.
- File-name-only text search for the tokens you listed. No matched content was displayed.
- Read the Taxonomy entry of the legacy `CELEX_MANIFEST_v4.json` (source URL, dates, hash), which also displayed four other acts’ provenance rows; no coding fields.
- Read your application e-mail `01_resposta_david.md` (its name is misleading; it is not David’s reply).
- **Not opened**: any workbook cell, method note, changelog, codebook, adjudication, or Pilot A document.
- The sheet names above hint that v1.4 tracks changes from v1.3 and has advice/expertise and mechanism-audit sheets. That is structural knowledge I now have; I will not use it to shape Phases 1–8.

## 0B.5 Deviations from prompt / instructions
1. I did not create `PHASE_0_SOURCE_INVENTORY` v0_2; the original file is untouched and 0B rows are in a separate addendum.
2. I ran one over-broad file-name search over the user profile that returned noise (“copilot”) and stopped it; a narrower search then found the Downloads files.
3. The prompt copy was first typed by me, then replaced with a byte-exact copy once the original file was found. The log records this.
4. A fresh network acquisition was done (D8 authorises acquiring text if absent; the text was present, so this was a verification step rather than a necessity).

## 0B.6 Quality checks
Hashes of the prompt original, its duplicate and the namespace copy agree; legacy source hash equals the manifest hash; both XHTML files show 27 contiguous article ids and 60 contiguous recital ids; no file outside `WORK_2_1/` was modified (the only writes are new files under `WORK_2_1/PILOT_R2_1/`); firewall register lists every closed file with SHA-256.

## 0B.7 Researcher decisions required before Phase 1
1. **Confirm Pilot A** = `R2_DAVID_VALIDATION_PACKAGE_v1_3` (with v0_2/v1_2 as predecessors) and that v1.4 is the *post-feedback* attempt, not Pilot A. If v1.4 was in fact the version David reviewed, say so.
2. **Confirm the primary legal text** (legacy copy proposed) and whether the original OJ text, not a consolidated version, is the object of comparison.
3. **David’s original feedback** (D6): designate the file that holds it (candidates: the learning log or the meeting briefing), or provide it. I will copy it into `provenance/` byte-exact **without analysing it**, unless you say it may be read. If it exists only in e-mail, tell me whether I may search your Gmail; I have not.
4. **Is reading your feedback-holding file allowed before Phase 9?** It probably states Pilot A’s deficiencies, which is precisely what the new architecture is designed to answer, so it could bias Phases 1–8. Section 2 of the prompt already encodes his corrections; I suggest using only that.
5. **Firewall extent**: the v1.4 files are in your other repo and are untracked. Should I leave them there, or do you want them hashed and frozen elsewhere? I have left them unchanged.
6. Is it acceptable that the Phase 0 report keeps its superseded D3 inference, with `RESEARCHER_DECISION_LOG.md` as the correction? (Alternative: a v0_2 of the report.)

## Status
`READY_FOR_RESEARCHER_REVIEW`

STOP.

`PHASE_0B_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`
