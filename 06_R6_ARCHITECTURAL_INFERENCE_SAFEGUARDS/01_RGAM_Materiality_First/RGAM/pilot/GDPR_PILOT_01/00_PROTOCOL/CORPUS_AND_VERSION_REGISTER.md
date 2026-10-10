# Corpus and version register — GDPR Pilot 01

**Date of acquisition:** 2026-10-03 (files written about 15:51 UTC; local file times 12:51 UTC−3). **Researcher:** Igor Caires Machado; acquisition and parsing executed by the AI agent. **Status:** descriptive; legal-status statements below are limited to what was retrieved and are not a legal opinion.

## Instrument

| Item | Value | How established |
|---|---|---|
| Official title | Regulation (EU) 2016/679 of the European Parliament and of the Council of 27 April 2016 on the protection of natural persons with regard to the processing of personal data and on the free movement of such data, and repealing Directive 95/46/EC (General Data Protection Regulation) (Text with EEA relevance) | text of the retrieved document |
| CELEX | 32016R0679 | EUR-Lex URL used |
| Official Journal | OJ L 119, 4.5.2016, beginning at p. 1 | document header (`L 119/1`); publication date stated in the corrigendum text ("L 119 of 4 May 2016"). **End page not verified.** ELI marker `eli/reg/2016/679/oj/eng` found in the HTML |
| Language | English (EN) | |
| Date of the act | 27 April 2016 | text |
| Entry into force | **24 May 2016** (computed: the twentieth day following publication on 4 May 2016, Art. 99(1)) | computed from Art. 99(1) and the publication date; consistent with the 24 May 2016 dates used in Arts 92(2), 94, 96 |
| Date of application | **25 May 2018** (Art. 99(2)) | text |

## Version used for the pilot (temporal control sheet)

**Pilot text = authentic OJ L 119 text (EUR-Lex rendering) with the 2018 corrigendum applied.** This is a **fixed historical baseline** for the interval from 25 May 2018. **It is not asserted to be the currently applicable GDPR on 3 October 2026.**

| Component | Status |
|---|---|
| Original OJ L 119 text (EUR-Lex XHTML rendering `L_2016119EN.01000101.xml`, converter 9.16.1) | Retrieved; SHA-256 `b5085317e90f6cc77bed4867b22de17a9bc0719e663b9f0bab1f59474fe622fd`. A web rendering of the OJ document; byte-level equivalence with the OJ PDF **not checked** |
| Corrigendum **OJ L 127, 23.5.2018, p. 2** (CELEX 32016R0679R(02)) | Retrieved (`L_2018127EN.01000201.xml`); **applied** to recital 71 and Arts 37(1)(c), 41(3),(5), 42(7), 43(3),(6), 57(1)(p), 64(1)(c),(6)–(8), 65(1)(a), 69(2), 70(1)(l),(o),(p); 18 of 18 substitutions applied by script; log kept |
| Corrigendum CELEX 32016R0679R(03) | Requested; EUR-Lex returned "The requested document does not exist" for the English HTML. **Its existence and effect on the English text are not verified** (the agent has an unverified recollection of a 2021 corrigendum affecting other language versions) |
| Corrigendum CELEX 32016R0679R(01) | **Not requested** |
| Consolidated text (CELEX 02016R0679-20160504, version 000.002) | Retrieved for navigation and as a check: article-level differences from the original occur exactly in the articles changed by the 2018 corrigendum (4 – parse noise; 37, 41, 42, 43, 57, 64, 65, 69, 70) plus layout headings. Carries only markers ►B and ►C1. **No legal effect** (stated by the document); not used as the legal text |
| Subsequent amending acts and later corrigenda | **Not verified** up to 3 October 2026. The consolidated document retrieved lists no amending act, but that is not evidence that none exists |

## Documentary boundary

W = the whole instrument: Arts 1–99 (389 paragraph units; 382 point units; Art. 4 definitions as points) and 173 recitals (interpretive context only). The instrument is **not** presumed to constitute one architecture. External instruments and standards are referenced, never silently imported.

## Files

Raw files and hashes: `01_SOURCES/raw/`, `01_SOURCES/MANIFEST_SHA256.txt`. Parsing code: `01_SOURCES/build_working_text.py`, `parse_gdpr.py`. Parsed working text: `01_SOURCES/parsed/working_text.json`; uncorrected: `original_articles_uncorrected.json`; correction log: `corrigendum_application_log.json`. Unit inventory: `01_SOURCES/SOURCE_UNIT_INVENTORY.csv`.

## Open version issues

HQ-014 (later amendments and corrigenda; 2021 corrigendum). A publication-grade use of this pilot requires resolving them first.
