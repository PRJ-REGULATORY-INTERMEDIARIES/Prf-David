# Human review evidence book — G4 Step 2A

## Frozen primary evidence

The common evidence is the frozen 20-row statement register, hash `417A35A361E44F8BECFBD8FC39B34738C026591C59B7E837FDDF292F9EF3E77F`: six statements for P03, Directive 91/263/EEC (CELEX 31991L0263), and fourteen for P04, Regulation (EC) No 874/2004 (CELEX 32004R0874). The official legal HTML source versions are recorded and hashed in the Step 2A freeze manifest. The per-item cards reproduce only the legal excerpts attached to that item; statement IDs and anchors are retained.

The full evidence text is in `HUMAN_ADJUDICATION_MASTER.csv`, column `exact_frozen_evidence`. The priority subset is repeated in `HUMAN_ADJUDICATION_P1.csv`; the remaining items are in `HUMAN_ADJUDICATION_LOWER_PRIORITY.csv`. This avoids replacing exact item-level evidence with paraphrase in this guide.

## Review universe and boundaries

- 28 existing Step 1 human-review queue items: 7 P1, 14 P2, 7 P3.
- 13 provisional Step 2A correspondence groups, without any presumption of equivalence.
- 41 unique review items in the master register. The priority file contains the 7 P1 claim items and 2 separately labelled correspondence items that depend on P1 review. The lower-priority file contains the other 32 items.
- Five material external-evidence dependencies remain outside the frozen input: `R-P03-04`, `CL-P03-02`, `CL-P03-03`, `R-P04-05`, and `CL-P04-02`. Their possible reliance is represented in separate context fields and does not make the external material frozen evidence.
- Borderline claims `CL-P04-04` and `CL-P04-07` remain identified as borderline in the inherited Step 1 scope records; they are not promoted to confirmed claims by this package.
- The two `STEP0_DERIVED` core units remain explicitly derived analytical constructs, not original experimental claims.
- Article 22(7) of P04 is outside this selected statement-level comparison scope; no new evidence or claim from it is added here.

## Separation of records

`HUMAN_REVIEW_IDENTITY_KEY.csv` is restricted and maps anonymized review IDs to source units, original claim IDs, cell identifiers and correspondence groups. Do not provide it to blinded reviewers. The reviewer-facing files contain no source-cell labels in the identity fields. Historical analytical text is supplied only as the proposition requiring review; it is not primary evidence and does not predetermine the legal answer.

No reviewer decisions, confidence ratings, justifications, identities, or dates have been populated. The two dependent correspondence items are identified by their pre-existing package flag; no substantive conclusion is implied.
