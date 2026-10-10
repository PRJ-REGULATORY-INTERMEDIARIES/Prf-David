# NEW TEST 3x3 — DOMAIN TAXONOMY

**Rule (pre-registration §8):** domain is assigned from subject matter, regulatory field and institutional purpose stated in the title/Article 1 — **never from architectural results** — before ranking and selection. Level-1 domains define "substantively distinct" for the diversity constraint; Level-2 sub-fields are recorded for transparency only. Ambiguous cases carry a primary and an alternate Level-1 domain; the diversity test uses the primary and reports sensitivity to the alternate.

`CASE_DOMAIN_CLASSIFICATION.csv` classifies the 29 studied instruments (the 101 Rotem-only rows and the two prohibited V8 items are not classified: they were excluded before the domain step).

## 1. Level-1 taxonomy (built from the actual universe)

| Code | Level-1 domain | Studied instruments (primary assignment) | n |
|---|---|---|---:|
| D01 | Environment & climate regulation | ETS Directive 2003/87; MSR Decision 2015/1814; ESR 2018/842; Climate Law 2021/1119; EUDR 2023/1115; Ecolabel 66/2010; ETS verification 2018/2067 | 7 |
| D02 | EU funds & public-finance management | Social Climate Fund 2023/955 | 1 |
| D03 | External trade & customs | CBAM 2023/956 | 1 |
| D04 | Financial markets, corporate reporting & sustainable finance | CSRD 2022/2464; Benchmarks 2019/2089; Taxonomy 2020/852 | 3 |
| D05 | Digital services, data protection & AI governance | GDPR 2016/679; DSA 2022/2065; AI Act 2024/1689; P2B 2019/1150 | 4 |
| D06 | Telecommunications, radio/terminal equipment & product conformity | 76/889; 86/361; 87/95; 89/336; 91/263; 92/44 | 6 |
| D07 | Intellectual property & copyright | 2004/48; 2006/115; CDSM 2019/790 | 3 |
| D08 | Internet naming & domain governance | .eu Regulation 874/2004 | 1 |
| D09 | Financial crime / AML transparency | Regulation 1781/2006 | 1 |
| D10 | Health products (medical devices) | MDR 2017/745 | 1 |
| D11 | Public administration & regulatory-agency governance | Lei 13.848/2019 (Brazil) | 1 |

## 2. Ambiguous assignments (documented)

| Instrument | Primary | Alternate | Why ambiguous |
|---|---|---|---|
| Social Climate Fund 2023/955 | D02 EU funds | D01 | climate-related social policy, but the title is a fund that amends the Common Provisions Regulation for EU funds; its institutional purpose is financing and payment control of Member State plans |
| CBAM 2023/956 | D03 Trade & customs | D01 | levy on imports with certificates and customs coordination (trade field), climate purpose |
| EUDR 2023/1115 | D01 Environment | D03 | deforestation objective with market-access/export rules |
| CSRD, Benchmarks, Taxonomy | D04 | D01 | financial/corporate-reporting law with environmental subject matter |
| .eu 874/2004 | D08 | D05 | domain-name registry rules vs digital governance |
| 1781/2006 | D09 | D04 | financial-sector transparency for AML/CFT |
| CDSM 2019/790 | D07 | D05 | copyright law with digital-platform duties |

## 3. Domain distribution in the **rank-eligible pool** (stratum S1)

| Level-1 domain | Rank-eligible laws | n |
|---|---|---:|
| D01 Environment & climate | ETS Directive; MSR Decision; ESR; European Climate Law | 4 |
| D02 EU funds & public finance | Social Climate Fund | 1 |

**Only two Level-1 domains are present among rank-eligible case-versions** (one, D01, if the alternate assignment of the Social Climate Fund is used). Level-2 sub-fields inside S1 are: carbon-market regulation (ETS, MSR), national climate-target allocation (ESR), climate-governance framework (Climate Law), climate-related social financing (SCF). These are sub-fields of climate policy, not distinct regulatory domains under the registered rule.

## 4. Classification procedure and independence

Assignments were derived from titles and, for the R3 laws, from the instrument's stated regulatory objective (Article 1) in the R3 `INSTRUMENTS` sheet. No count, rank, mechanism, configuration or architectural statement was consulted. The classification step is computed in `LOGS/scripts/build_ranking.py` before the ranking step and written to `CASE_DOMAIN_CLASSIFICATION.csv` (`classified_before_ranking` column).
