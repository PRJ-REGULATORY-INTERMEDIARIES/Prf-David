# SOURCE COMPLETENESS AUDIT

**Audit date:** 2026-10-06  
**Scope:** The four cases in the existing paired 2+2 selection freeze; official original acts in English.

| Case | Version frozen | Complete local source | Structural check | Annexes | Result |
|---|---|---|---|---|---|
| CASE-32023R0955 | Original OJ act, 16 May 2023 | `CASE-32023R0955/32023R0955_official_en.html` | 29 articles; official file matches source manifest and has document-end marker | I–V, included | PASS |
| CASE-32023R0956 | Original OJ act, 16 May 2023 | `CASE-32023R0956/32023R0956_official_en.xhtml` | 36 articles; six annexes; official file has document-end marker | I–VI, included | PASS |
| CASE-32004R0874 | Original OJ act, 30 April 2004 | `CASE-32004R0874/32004R0874_official_en.html` | 24 articles; file matches source manifest; signature/end matter present | None in original act | PASS |
| CASE-31986L0361 | Original OJ act, 5 August 1986 | `CASE-31986L0361/31986L0361_official_en.html` | 12 articles; file matches source manifest; signature/end matter present | None | PASS |

## Integrity findings

- The old CBAM file at `Before_R2/dataset-eurlex/cases/case_02/source/act_official.xhtml` has 505,722 bytes and SHA-256 `04f40e92a692a5fb91f798b382f665e45843e822ad84341ba9e926613c3a40b9`. Its preserved provenance says 499,130 bytes and SHA-256 `B61FD911875E5C9C7839EFDB3998A040CE75477C77E9259E0091BAB329F7DDDF`. The local file therefore fails the historical hash check.
- The common corpus uses a fresh original-act XHTML retrieved from the official Publications Office CELLAR resource. It is 496,976 bytes with SHA-256 `c47e2793e7b92333ce9a891aba18924ff21b15b2745fffda98348b04b15a770e`; article, annex and end-marker checks pass. The problematic historical file was not changed.
- SCF's original official PDF is independently recorded in R3 as 51 pages, complete, and hash-matching its source-phase manifest. The common corpus uses its official English XHTML copy, which independently matches the official source manifest in the prior project register.
- The .eu and 86/361 files match their official source manifest rows exactly. Neither source contains an omitted annex in the original published act.
- The AI Act is not one of the four frozen cases, but is the only strict-AI candidate found in previous work. Its R4 provenance records SHA-256 `8F0B656302F9864CC87E040C371F209A9D65AE1A6CECC25CA5EB737E872D721A`; the current local file hashes to `68212334816C835903662618668BD4CBF51AFCD553DA15B482AFC2175705CE7B`. Its structural validation reports 113 articles and 13 annexes, but the source integrity mismatch must be repaired before any new AI Act extraction.

## Version boundary

These are original acts as published, not current consolidated law. Regulation 874/2004 was repealed on 13 October 2022; Directive 86/361/EEC was repealed on 6 November 1992. The source packages do not append amending or successor acts. No provision was excluded from the selected original acts.
