# R3 Phase 1 — Fresh Source Acquisition Audit

**Project:** GP5_JRG / Prf-David  
**Round:** R3  
**Phase:** 1 — Fresh source acquisition  
**Execution date:** 2026-09-20  
**Status:** `READY_FOR_RESEARCHER_REVIEW`

## A. Work completed

- Acquired one fresh English PDF for each of the five authorized CELEX acts from official EUR-Lex document URLs.
- Preserved each downloaded PDF unchanged in its CELEX-specific raw-source directory.
- Resolved the official title, instrument type, Official Journal reference and language from the fresh official EUR-Lex pages.
- Recorded retrieval timestamp, file size, SHA-256 and PDF page count.
- Designated each original act PDF as `PRIMARY_CODING_SOURCE`.
- Recorded, but did not download or use, the current consolidated version exposed by EUR-Lex.
- Checked the downloaded files for PDF signature, title-page identity and page-range completeness.

## B. Inputs used

- Official EUR-Lex/CELLAR document pages and PDF endpoints for the five requested CELEX identifiers.
- The Phase 1 authorization and source policy in `00_governance/R3_PROMPT_VERBATIM.md`.
- The Phase 0 clean-room governance records.

No prior project folder, previous acquisition manifest, prior legal-text copy, prior case summary, coding or classification was opened or used.

The excluded CELEX `32000D0293` was not acquired or analyzed.

## C. Outputs created

- `01_sources/R3_SOURCE_REGISTER.csv`
- `01_sources/32003L0087/SOURCE_MANIFEST.yaml`
- `01_sources/32015D1814/SOURCE_MANIFEST.yaml`
- `01_sources/32018R0842/SOURCE_MANIFEST.yaml`
- `01_sources/32021R1119/SOURCE_MANIFEST.yaml`
- `01_sources/32023R0955/SOURCE_MANIFEST.yaml`
- One untouched raw PDF per CELEX under its CELEX-specific directory.
- This audit report.

## D. Quantitative summary

| CELEX | Status | File size | Pages | SHA-256 | OJ page range check |
|---|---:|---:|---:|---|---|
| 32003L0087 | SUCCESS | 165,515 bytes | 15 | `B3941901E4FE1AF3DEFCFFA323C00A5C6F7F44C51C9EA5785C7A995C3BD68445` | PASS |
| 32015D1814 | SUCCESS | 346,776 bytes | 5 | `BCA2648F3E4A312BF6F31F5270B01D933234E949F4EAC54157A0115086E18036` | PASS |
| 32018R0842 | SUCCESS | 836,393 bytes | 17 | `DD429F4752B9F0F9320CE2FC79152D02A7D34BE262EE86019D98B96E62D07048` | PASS |
| 32021R1119 | SUCCESS | 568,475 bytes | 17 | `855EBC344E9FAF2DB68D75317C08034AF54A1CCE216D8D00C640C3073E639840` | PASS |
| 32023R0955 | SUCCESS | 1,126,176 bytes | 51 | `F58712E1156435A418EC1A445F9DBB8D9742FF29E3C8317FF4C00FF929740C49` | PASS |

- Successful retrievals: 5/5.
- Failed retrievals: 0.
- Languages acquired: English only, as authorized for the primary source files.
- Consolidated files downloaded: 0.
- Corrigenda identified on the EUR-Lex metadata pages checked: none.
- Prior empirical files imported: 0.

## E. Methodological decisions

- The original Official Journal act as adopted is the primary coding source for every case.
- The raw file is the EUR-Lex English PDF returned by the CELEX document endpoint with `from=EN`.
- Consolidated versions visible on EUR-Lex are recorded as version information only and remain `REFERENCE_ONLY`; none was downloaded.
- No substantive reading, law summary, actor identification, relation reconstruction or mechanism coding was performed.

## F. Uncertainties

- EUR-Lex currently displays later consolidated versions for all five acts. This is a normal version distinction, not a conflict in the newly acquired original files.
- The Phase 1 metadata-page checks did not identify a corrigendum entry. This does not substitute for later substantive corpus checks; any corrigendum discovered during authorized corpus construction must be recorded separately and must not silently replace the original act.
- No source was acquired in another language. If multilingual comparison is later required, it requires explicit authorization.

## G. Deviations from prompt

None. Corpus construction and substantive analysis were not started.

## H. Quality-control checks

- Each raw file begins with the PDF signature `%PDF-`.
- The downloaded PDF page counts match the Official Journal page spans reported by EUR-Lex:
  - 15 pages for pp. 32-46;
  - 5 pages for pp. 1-5;
  - 17 pages for pp. 26-42;
  - 17 pages for pp. 1-17;
  - 51 pages for pp. 1-51.
- First-page title/date/language markers match the corresponding Official Journal act.
- SHA-256 values were calculated from the preserved raw files.
- No consolidated PDF was substituted for an original act.
- The excluded `32000D0293` is absent from the source register and raw-source directories.

## I. Researcher decisions required

No source-selection decision is currently blocking: all five original English acts were successfully acquired and designated `PRIMARY_CODING_SOURCE`.

Before corpus construction, the researcher must explicitly authorize Phase 2, for example:

`CONTINUE TO PHASE 2`

or

`APPROVED — CONTINUE`

## J. Status

Phase 1 is complete. The R3 process must stop here. Do not construct the corpus until explicit researcher authorization is received.

`R3_PHASE_1_COMPLETE — WAITING_FOR_RESEARCHER_AUTHORIZATION`
