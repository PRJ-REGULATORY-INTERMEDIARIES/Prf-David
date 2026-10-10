# Source manifest — GDPR Pilot 01

| Role | File | Origin (URL) | SHA-256 | Use |
|---|---|---|---|---|
| Authentic text (rendering of OJ L 119, 4.5.2016) | `raw/gdpr_eurlex_html.html` | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679 | `b5085317e90f6cc77bed4867b22de17a9bc0719e663b9f0bab1f59474fe622fd` | **Legal text base** (with corrigendum applied) |
| Corrigendum OJ L 127, 23.5.2018, p. 2 | `raw/corr_32016R0679R02.html` | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679R(02) | `52c9966557c1b4549d3580b02442e1c0defcd9f304ef90d72974d106f524f7e8` | Applied to 18 passages; log in `parsed/corrigendum_application_log.json` |
| Corrigendum CELEX 32016R0679R(03) request | `raw/corr_32016R0679R03.html` | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32016R0679R(03) | `930fba6f0a71d1994654002cd7c5963543cee3056a6f9b18d56e8a40ba55fb09` | **Error page** ("The requested document does not exist"); kept as evidence of the failed retrieval; not a source |
| Consolidated text (04.05.2016, 000.002) | `raw/corr_02016R0679-20160504.html` | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02016R0679-20160504 | `7d8d3263e23108b0d9bcbd5326aad916a9aeeae2ed365145b9335f2a9e3d3144` | Navigation and cross-check only; no legal effect |
| Parsed working text | `parsed/working_text.json` | produced by `build_working_text.py` | `6c257e4541c11dfa0f48848ba5310e6ff49aea89a63bf7f06bb3adbde977439c` | Extraction input |
| Uncorrected parse | `parsed/original_articles_uncorrected.json` | same | `216002242f82b1502fb6f8068a7cdc890c2837b60323d7959cbcb4f7093bd689` | Comparison |
| Correction log | `parsed/corrigendum_application_log.json` | same | `83cf6311256147b5d3f40f8dd693833d5ff085b6a688a67e1e2bbb91d2a144fc` | Traceability of consequential textual changes |
| Unit inventory | `SOURCE_UNIT_INVENTORY.csv` | same | `70c1192c28380db68ff29630cbf4f52fc450617d3710a33b37d26fe1e2239232` | 389 paragraph + 382 point units |

All downloads were made by `curl` with a generic research user agent on 2026-10-03. Historical GDPR extractions elsewhere in the repository (R4 materials) were **not consulted**. No external source cited by the GDPR (other instruments, standards, national law) was retrieved; see `EXTERNAL_REFERENCE_REGISTER.csv` (22 rows for about 16 distinct sources; generic national-law dependencies are recorded in `depends_on` fields and are not exhaustive in the register).

**Authenticity note.** EUR-Lex publishes the electronic Official Journal as the authentic version; the HTML file is EUR-Lex's rendering of that document. Byte-level equivalence with the PDF edition was not checked.
