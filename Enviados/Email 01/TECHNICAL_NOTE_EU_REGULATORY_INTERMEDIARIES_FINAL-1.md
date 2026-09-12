Technical Note  
Construction of a Researcher-Adjudicated R-I-T Dataset from Three EU Green-Transition Regulations

**Prepared for:** David Levi-Faur**Prepared by:** Igor Caires Machado**Date:** 8 September 2026

# Executive summary

**Purpose.** This technical note documents the construction of a compact, source-bounded dataset of regulatory actors, intermediaries, targets and intermediation mechanisms in three EU green-transition regulations. The final release is organised at four linked levels: act/regime, actor-in-role, intermediary function/mechanism, and relation-level legal evidence.

**Final analytical release.** The dataset contains 20 final regulatory episodes: 12 intermediated and 8 direct. It maps 31 case-specific actor-role records (6 R, 12 I and 13 T) and 13 intermediary-function records. The 12 intermediary actor-role records correspond to 11 distinct normalised intermediary labels across the combined sample, because customs authorities appear in both CBAM and EUDR.

**Regulations**

**Final relations**

**Intermediated**

**Direct**

**I actor-role records**

**I function records**

**3**

**20**

**12**

**8**

**12**

**13**

The final release excludes unresolved, insufficiently supported and non-supported candidates. All retained entries are linked to operative provisions of the focal legislation.

# 1\. Research objective and analytical architecture

The exercise operationalises the Regulator–Intermediary–Target (R-I-T) framework for EU legislation in the green transition. The central methodological choice is to preserve the relational nature of regulatory roles while producing a dataset that is useful for actor- and mechanism-centred comparative research.

Regulatory relationships are used as the primary coding and evidentiary units. They establish why a particular actor can be coded as a regulator (R), intermediary (I) or target (T) in a specific legal context. For substantive mapping, however, the principal analytical unit is the actor-in-role within an act or regulatory context. This avoids treating R, I or T as permanent organisational attributes.

-   Act / regime: the legal and institutional context.
-   Actor-in-role: the case-specific assignment of R, I or T.
-   Intermediary function / mechanism: what the intermediary does and how the function operates.
-   Regulatory relation / episode: the operative legal evidence supporting the role assignment.

# 2\. Case selection and legal sources

Three regulations were selected prospectively for relevance to the EU green transition, institutional diversity and feasibility of complete legal reading. Selection did not depend on known R-I-T results or expected intermediary counts.

**Case**

**CELEX**

**Regulation**

**Domain**

**Final relations (I / direct)**

1

32021R1119

European Climate Law

Climate governance

5 (3 / 2)

2

32023R0956

CBAM

Climate, trade and industrial decarbonisation

9 (5 / 4)

3

32023R1115

EUDR

Deforestation and supply-chain governance

6 (4 / 2)

Official EUR-Lex texts were used as the normative sources. The legal documents were acquired, normalised into stable machine-readable corpora, and frozen before substantive coding so that later transformations did not alter the source text.

# 3\. Step-by-step construction process

## Step 1 — Source acquisition and corpus freezing

The official English versions of the three regulations were retrieved from EUR-Lex. Presentation and navigation artefacts were removed, while article structure, paragraphs, points, annexes and source order were preserved. Stable source and corpus hashes were recorded before coding.

## Step 2 — Separation of operative and contextual text

The full legal act remained preserved, but operative provisions were treated as the primary evidentiary layer. Recitals were retained for contextual and purposive interpretation but were not allowed to generate a positive R-I-T relation on their own. A positive coding required an operative normative anchor.

## Step 3 — Source-bounded interpretive reading

The legal texts were read in full using structured, source-bounded computational reading procedures. The reader reconstructed regulatory episodes rather than classifying isolated keywords or actor mentions. Cross-references within each act were followed where needed to identify the complete mechanism.

## Step 4 — R–T reconstruction before intermediary classification

For each regulatory episode, the regulator/rule-maker and target/rule-taker were reconstructed first. Only after a defensible R–T architecture was established were materially involved third actors examined as potential intermediaries. This reduced actor-label bias and target/object confusion.

## Step 5 — Functional test for third actors

A third actor was classified as an intermediary only when the operative text supported a distinct, institutionally integrated regulatory function. The analysis distinguished intermediaries from co-regulators, parallel regulators, consulted actors, external information sources and instruments/systems.

## Step 6 — Broader treatment of intermediation orientation

The coding was recalibrated to recognise that intermediation need not always be target-facing. Three orientations were retained: target-facing, regulator-facing and bidirectional. Regulator-facing expertise, reporting or advice could count when legally integrated into the mechanism through which R seeks to affect T. Mere opinion, generic expertise or external influence remained insufficient.

## Step 7 — Researcher adjudication and rule calibration

Candidate relations and conceptual boundary cases were reviewed by the researcher. Decisions were used to refine general decision rules rather than to hard-code specific provisions. The final release retains only adjudicated direct or intermediated relations; unresolved and unsupported candidates were excluded.

## Step 8 — Transformation from relations to actor-in-role data

Accepted regulatory episodes were converted into an actor-in-role map. Actor names were normalised while preserving case context. Compound regulatory episodes were decomposed where necessary so that the same actor could appear in different roles or contexts without being assigned a permanent R, I or T identity.

## Step 9 — Harmonisation of intermediary mechanisms

Fine-grained intermediary functions were separated from the project's focal mechanism families. Reporting, certification, auditing and ranking/rating were kept as comparative mechanism families, while functions such as comitology, expert consultation, information transmission and scientific advice were retained as specific mechanism details and grouped as 'other' when they did not fit the four focal families.

## Step 10 — Data cleaning and quality assurance

Duplicate and inconsistent actor labels were normalised; internal review columns and provisional statuses were removed; article-level legal anchors were standardised; and concise evidence summaries were rechecked against the frozen normative sources. A working CSV that had suffered delimiter/quoting corruption was not treated as an authoritative source; accepted decisions were reconstructed from intact validation records and revalidated against the frozen legal corpora before final export.

# 4\. Final coding rules

**Rule**

**Operational meaning**

Relational roles

R, I and T are case- and context-specific roles, not permanent attributes of organisations.

Positive evidence

A positive R-I-T classification requires an operative normative anchor in the focal act.

Intermediary threshold

A third actor must perform a distinct, institutionally integrated function within the R–T regulatory mechanism.

Regulator-facing intermediation

Direct I→T action is not required if the intermediary function is legally integrated into the process through which R regulates or assesses T.

External influence

Mere opinion, lobbying, generic expertise or information availability is not intermediation by itself.

Actor/object distinction

Reports, databases, plans, methodologies and information systems are treated as instruments or objects unless the legally relevant actor behind them is identifiable.

Recitals

Recitals may support interpretation but cannot independently generate a positive relationship.

# 5\. Final dataset structure

The final workbook contains a public-facing analytical structure with no unresolved-case sheet, internal reviewer notes or provisional adjudication fields.

-   **OVERVIEW:** Study scope, final counts and analytical conventions.
-   **ACT\_SUMMARY:** One row per act with relation and intermediary counts.
-   **ACTOR\_ROLE\_MAP:** One row per case × normalised actor × role.
-   **INTERMEDIARY\_MAP:** One row per intermediary actor × function/mechanism within a case.
-   **RELATION\_EVIDENCE:** One row per final regulatory episode, with R/I/T, action, mechanism and article-level evidence anchor.
-   **DATA\_DICTIONARY:** Definitions of the principal fields and interpretive rules.

The Excel workbook is the integrated deliverable. Three companion CSV files are also provided for relation-level data, the actor-role map and the intermediary map.

# 6\. Descriptive results of the three-case dataset

Across the three regulations, 20 final regulatory episodes were retained: 12 intermediated and 8 direct. The actor-role layer contains 31 records: 6 regulator roles, 12 intermediary roles and 13 target roles.

Among intermediary actor-role records, seven are regulator-facing, four are bidirectional and one is target-facing. The intermediary-function table contains 13 function records because the Scientific Advisory Board performs two analytically distinct functions in the European Climate Law.

**Case**

**Final relations**

**Intermediated**

**Direct**

**Intermediary actor-role records**

European Climate Law

5

3

2

3

CBAM

9

5

4

5

EUDR

6

4

2

4

**Total**

**20**

**12**

**8**

**12**

## 6.1 Intermediary mechanisms

The mechanism-family layer contains 13 intermediary-function records: 3 reporting, 2 certification, 1 auditing and 7 'other' functions. No ranking/rating instance was retained in the three focal acts. The 'other' category deliberately preserves institutionally integrated functions such as comitology, expert consultation, scientific advice and border-information transmission rather than forcing them into an ill-fitting focal family.

## 6.2 Examples of intermediary architectures

-   European Climate Law: EEA and the Scientific Advisory Board provide reports and assessment inputs integrated into Commission evaluation of Member State climate progress.
-   CBAM: accredited verifiers independently verify embedded-emissions declarations; national accreditation bodies accredit the verifiers; customs authorities connect border control with the compliance-information system.
-   EUDR: customs authorities connect product release with due-diligence information; substantiated concerns create a formal reporting channel into competent-authority enforcement; FLEGT licensing is incorporated as recognised evidence of legality.

# 7\. Scope and interpretation

This is a deliberately small, theory-calibrated three-case dataset. The counts should not be interpreted as population estimates of the prevalence of intermediation across EU green-transition legislation. The acts differ in size, institutional density and regulatory design. The dataset is best used as a transparent pilot for refining the coding architecture, testing the portability of the mechanism taxonomy and designing subsequent large-N collection.

The relation-evidence layer remains essential even though the substantive mapping is actor-centred: it preserves the legal basis for each role and prevents organisations from being classified as 'intermediaries' solely because of their institutional reputation.

# 8\. Core references and legal sources

-   Abbott, K. W., Levi-Faur, D., & Snidal, D. (2017). Theorizing Regulatory Intermediaries: The RIT Model. The ANNALS of the American Academy of Political and Social Science, 670(1), 14–35. https://doi.org/10.1177/0002716216688272
-   Abbott, K. W., Levi-Faur, D., & Snidal, D. (2017). Enriching the RIT Framework. The ANNALS of the American Academy of Political and Social Science, 670(1), 280–288. https://doi.org/10.1177/0002716217694593
-   European Parliament, Council and Commission. Interinstitutional Agreement of 22 December 1998 on common guidelines for the quality of drafting of Community legislation, Guideline 10.
-   Regulation (EU) 2021/1119 — European Climate Law. CELEX 32021R1119. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32021R1119
-   Regulation (EU) 2023/956 — Carbon Border Adjustment Mechanism. CELEX 32023R0956. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R0956
-   Regulation (EU) 2023/1115 — Deforestation-Free Products Regulation. CELEX 32023R1115. https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32023R1115

**Release status:** Final cleaned three-case research dataset prepared for external sharing. No unresolved or provisional coding records are included.