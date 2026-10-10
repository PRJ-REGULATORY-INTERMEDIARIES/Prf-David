# R3 Method Pipeline

R3 used AI-assisted structured coding/review with researcher-controlled decisions and auditable legal evidence. Each stage had a defined input, analytical decision, output, and validation step.

| Stage | Input | Analytical decision | Output | Quality control |
|---|---|---|---|---|
| Fresh official sources | Known CELEX identifiers | Retrieve the original Official Journal act as adopted | Five preserved official-source files and manifests | Source authority, version, completeness, SHA-256 |
| Corpus validation | Fresh official PDFs | Reconstruct searchable legal corpora without substantive coding | Full, numbered, recital, operative, and article-index files | Page/text completeness, article and annex checks |
| Whole-instrument analysis | Validated corpora | Reconstruct each instrument before extracting actors | Five instrument profiles and memos | Objective, scope, obligations, governance components, structural logic |
| Actor inventory | Whole-instrument profiles and corpora | Register legal actors before assigning R/I/T roles | 89 LAW × ACTOR records | Identity, aliases, legal status, provision coverage |
| Candidate relations | Actor register and legal provisions | Reconstruct legally relevant actor relations | 56 relation candidates | R, possible I, T, object, output, and legal anchors |
| RIT adjudication | Candidate relations | Require an R–T relation, a distinct third actor, and a demonstrable mediating function | 24 direct R–T, 23 legal non-RIT, 9 supported intermediation relations | Boundary review, uncertainty log, targeted adjudication |
| Intermediary consolidation | Nine supported relations | Consolidate the same intermediary within each law while retaining relation multiplicity | 7 LAW × INTERMEDIARY units | Relation links and institutional-profile reconciliation |
| Mechanism coding | Supported relations and legal traces | Identify the elementary transformation performed by I | 10 mechanism events | Input–transformation–output trace; alternative mechanism test |
| Adversarial mechanism review | Ten event reconstructions | Reconstruct each event independently and challenge its code | 7 confirmed codes and 3 codebook-boundary findings | Rival-mechanism and ontology-boundary tests |
| Researcher adjudication | Boundary findings and full evidence | Retain three RIT relations and provisionally add `IMPLEMENTATION` rather than broaden `TRANSLATION` | Ten researcher-adjudicated events | Decision `R3-D08-IMPLEMENTATION`; unchanged historical record |
| Mechanism configuration | Ten adjudicated events | Distinguish single events, repetition across relations, and functional sequences within relations | 8 single-mechanism relations, 1 sequential relation, 1 edge | Four-part dependency test and legal evidence trace |
| Dataset architecture | All validated levels | Assign each dimension to its proper unit and map fields to research questions | Normalized ten-table proposal and David-facing view | Six real-case schema tests; variable-priority review |

## Clean reconstruction principle

The five instruments were reacquired from official EU sources and analyzed in a separate R3 workspace. Prior empirical coding was not used as ground truth. Later stages use only validated R3 outputs and preserve earlier records rather than overwriting them.

## Decision discipline

AI-assisted reconstruction and review produced auditable candidates. Material conceptual decisions remain identified by owner. In particular, `IMPLEMENTATION` is explicitly a provisional researcher decision. The package does not imply that it belongs to an existing published taxonomy.

## Current boundary

The pipeline ends with dataset architecture and proposal packaging. Regulatory capacities, outcomes, and broader architectural classifications have not been assigned.
