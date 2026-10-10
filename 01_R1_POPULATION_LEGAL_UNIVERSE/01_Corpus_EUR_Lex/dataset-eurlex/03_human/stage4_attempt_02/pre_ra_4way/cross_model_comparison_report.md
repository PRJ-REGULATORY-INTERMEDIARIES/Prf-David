# Four-way pre-RA comparison — CELEX 32021R1119

Comparator version: 1.0.0. Methodology: locked v1.1.0. Universe: 90 frozen candidates.

This report is strictly descriptive. It treats Terra-R1, Terra-R2, Claude-R1, and Claude-R2 as symmetric independent replicas. It does not adjudicate, choose a winner, execute RA, execute a human gate, or lock a benchmark.

## Distributions directly recalculated from validated outputs

| indicador | Terra-R1 | Terra-R2 | Claude-R1 | Claude-R2 |
|---|---:|---:|---:|---:|
| positive | 0 | 2 | 3 | 3 |
| negative | 89 | 80 | 86 | 87 |
| conditional | 1 | 1 | 1 | 0 |
| insufficient_evidence | 0 | 7 | 0 | 0 |
| confidence=high | 89 | 71 | 55 | 76 |
| confidence=medium | 1 | 11 | 30 | 14 |
| confidence=low | 0 | 8 | 5 | 0 |
| I != null | 1 | 3 | 6 | 4 |
| C=YES | 1 | 3 | 6 | 4 |
| D=YES | 1 | 3 | 4 | 3 |

`screening_status` is analyzed separately from the principal substantive signature. `I != null` denotes a non-empty normalized I-label set and, under the current validator limitation, is not by itself proof of mediation.

## Pairwise metrics

| pair | relational agreement | κ relational | screening agreement | κ screening | A–E joint agreement | R agreement | I agreement | T agreement | mechanism agreement | full substantive signature | positive Jaccard | D=YES Jaccard |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Terra-R1 × Terra-R2 | 0.900 (90.0%) | 0.173 | 0.867 (86.7%) | 0.757 | 0.867 (86.7%) | 0.944 (94.4%) | 0.978 (97.8%) | 0.944 (94.4%) | 0.944 (94.4%) | 0.867 (86.7%) | 0.000 | 0.333 |
| Claude-R1 × Claude-R2 | 0.989 (98.9%) | 0.852 | 0.667 (66.7%) | 0.513 | 0.356 (35.6%) | 0.522 (52.2%) | 0.978 (97.8%) | 0.678 (67.8%) | 0.622 (62.2%) | 0.156 (15.6%) | 1.000 | 0.750 |
| Terra-R1 × Claude-R1 | 0.956 (95.6%) | 0.191 | 0.400 (40.0%) | 0.178 | 0.211 (21.1%) | 0.367 (36.7%) | 0.944 (94.4%) | 0.533 (53.3%) | 0.489 (48.9%) | 0.078 (7.8%) | 0.000 | 0.250 |
| Terra-R1 × Claude-R2 | 0.967 (96.7%) | 0.244 | 0.500 (50.0%) | 0.220 | 0.511 (51.1%) | 0.611 (61.1%) | 0.967 (96.7%) | 0.633 (63.3%) | 0.600 (60.0%) | 0.433 (43.3%) | 0.000 | 0.333 |
| Terra-R2 × Claude-R1 | 0.889 (88.9%) | 0.258 | 0.433 (43.3%) | 0.240 | 0.211 (21.1%) | 0.400 (40.0%) | 0.944 (94.4%) | 0.567 (56.7%) | 0.544 (54.4%) | 0.089 (8.9%) | 0.250 | 0.400 |
| Terra-R2 × Claude-R2 | 0.900 (90.0%) | 0.286 | 0.511 (51.1%) | 0.272 | 0.500 (50.0%) | 0.644 (64.4%) | 0.967 (96.7%) | 0.667 (66.7%) | 0.644 (64.4%) | 0.422 (42.2%) | 0.250 | 0.500 |

Cohen's kappa is calculated for nominal scalar/vector categories where meaningful: relational result, screening status, each A–E condition, the joint A–E vector, and primary mechanism. It is not imposed on actor-label sets or the composite signature. `NA` means expected agreement is 1 and kappa is undefined. The strong negative-class imbalance can inflate observed agreement and destabilize kappa, so neither is interpreted alone.

### Condition-specific agreement and kappa

| pair | A agreement / κ | B agreement / κ | C agreement / κ | D agreement / κ | E agreement / κ | joint A–E agreement / κ |
|---|---:|---:|---:|---:|---:|---:|
| Terra-R1 × Terra-R2 | 0.889 / 0.791 | 0.889 / 0.794 | 0.900 / 0.171 | 0.900 / 0.171 | 0.922 / 0.000 | 0.867 / 0.757 |
| Claude-R1 × Claude-R2 | 0.722 / 0.483 | 0.733 / 0.474 | 0.967 / 0.712 | 0.978 / 0.740 | 0.767 / 0.000 | 0.356 / 0.269 |
| Terra-R1 × Claude-R1 | 0.489 / 0.028 | 0.733 / 0.482 | 0.933 / 0.236 | 0.956 / 0.322 | 0.767 / 0.000 | 0.211 / 0.077 |
| Terra-R1 × Claude-R2 | 0.589 / 0.148 | 0.711 / 0.388 | 0.967 / 0.389 | 0.978 / 0.492 | 1.000 / NA | 0.511 / 0.204 |
| Terra-R2 × Claude-R1 | 0.511 / 0.120 | 0.711 / 0.476 | 0.867 / 0.247 | 0.889 / 0.297 | 0.689 / -0.129 | 0.211 / 0.089 |
| Terra-R2 × Claude-R2 | 0.578 / 0.200 | 0.678 / 0.383 | 0.900 / 0.329 | 0.911 / 0.363 | 0.922 / 0.000 | 0.500 / 0.237 |

## Within-family stability

The majority class and rare positives are separated below. Negative-set overlap describes stability of the dominant class; positive-set overlap describes stability of rare affirmative findings.

| family pair | negatives A/B | negative intersection/union | negative Jaccard | positives A/B | positive intersection/union | positive Jaccard |
|---|---:|---:|---:|---:|---:|---:|
| Terra-R1 × Terra-R2 | 89/80 | 80/89 | 0.899 | 0/2 | 0/2 | 0.000 |
| Claude-R1 × Claude-R2 | 86/87 | 86/87 | 0.989 | 3/3 | 3/3 | 1.000 |

For Terra-R1 × Terra-R2, dominant-negative stability is 0.899 by negative-set Jaccard, while rare-positive stability is 0.000. For Claude-R1 × Claude-R2, the corresponding values are 0.989 and 1.000. These are descriptive profiles, not rankings.

## Cross-family pairs

| pair | relational agreement / κ | full signature agreement | positives intersection/union | positive Jaccard | D=YES intersection/union | D=YES Jaccard |
|---|---:|---:|---:|---:|---:|---:|
| Terra-R1 × Claude-R1 | 0.956 / 0.191 | 0.078 | 0/3 | 0.000 | 1/4 | 0.250 |
| Terra-R1 × Claude-R2 | 0.967 / 0.244 | 0.433 | 0/3 | 0.000 | 1/3 | 0.333 |
| Terra-R2 × Claude-R1 | 0.889 / 0.258 | 0.089 | 1/4 | 0.250 | 2/5 | 0.400 |
| Terra-R2 × Claude-R2 | 0.900 / 0.286 | 0.422 | 1/4 | 0.250 | 2/4 | 0.500 |

## Empirical union of positive candidates

The positive union was recalculated directly from the four validated outputs and contains **4** candidates. Every one is marked for the future human gate under rule 1; no ID was hardcoded.

### CAND2-11BF388480EA

Location: Article 3, paragraph 4, line 220

> 4. In the context of enhancing the role of science in the field of climate policy, each Member State is invited to establish a national climate advisory body, responsible for providing expert scientific advice on climate policy to the relevant national authorities as prescribed by the Member State concerned. Where a Member State decides to establish such an advisory body, it shall inform the EEA thereof.

| coder | relational result | R | I | T | A–E | primary mechanism |
|---|---|---|---|---|---|---|
| Terra-R1 | negative | union | ∅ | member states | YES/YES/NO/NO/YES | standard_setting |
| Terra-R2 | positive | member state | national climate advisory body | relevant national authorities | YES/YES/YES/YES/YES | information_transmission |
| Claude-R1 | negative | eea | ∅ | member state (that decides to establish a national climate advisory body) | YES/YES/NO/NO/YES | information_transmission |
| Claude-R2 | negative | eea | ∅ | member state (that decides to establish a national climate advisory body) | YES/YES/NO/NO/YES | information_transmission |

No adjudication is made for this candidate.

### CAND2-465FC96778A7

Location: Article 8, paragraph 3, point b, line 314

> - (b) reports of the EEA, the Advisory Board and the Commission’s Joint Research Centre;

| coder | relational result | R | I | T | A–E | primary mechanism |
|---|---|---|---|---|---|---|
| Terra-R1 | negative | ∅ | ∅ | ∅ | NO/NO/NO/NO/YES | none_or_direct |
| Terra-R2 | insufficient_evidence | ∅ | ∅ | ∅ | UNCLEAR/UNCLEAR/UNCLEAR/UNCLEAR/NO | none_or_direct |
| Claude-R1 | positive | commission | advisory board; commission's joint research centre; eea | member states | YES/YES/YES/YES/YES | monitoring_supervision |
| Claude-R2 | positive | commission | advisory board; commission's joint research centre; eea | member states | YES/YES/YES/YES/YES | monitoring_supervision |

No adjudication is made for this candidate.

### CAND2-88A2261C68DE

Location: Article 8, paragraph 4, line 319

> 4. The EEA shall assist the Commission in the preparation of the assessments referred to in Articles 6 and 7, in accordance with its annual work programme.

| coder | relational result | R | I | T | A–E | primary mechanism |
|---|---|---|---|---|---|---|
| Terra-R1 | negative | union | ∅ | eea | YES/YES/NO/NO/YES | none_or_direct |
| Terra-R2 | positive | commission | eea | member states | YES/YES/YES/YES/YES | monitoring_supervision |
| Claude-R1 | positive | commission | eea | member states | YES/YES/YES/YES/YES | monitoring_supervision |
| Claude-R2 | positive | commission | eea | member states | YES/YES/YES/YES/YES | monitoring_supervision |

No adjudication is made for this candidate.

### CAND2-27E84BD23730

Location: Article 13, point b, line 400

> - (b) in paragraph 4, the first subparagraph is replaced by the following: ‘The Commission, assisted by the Energy Union Committee referred to in point (b) of Article 44(1), shall adopt implementing acts to set out the structure, format, technical details and process for the information referred to in paragraphs 1 and 2 of this Article, including a methodology for the reporting on the phasing out of energy subsidies, in particular for fossil fuels, pursuant to point (d) of Article 25.’;

| coder | relational result | R | I | T | A–E | primary mechanism |
|---|---|---|---|---|---|---|
| Terra-R1 | conditional | commission | energy union committee | ∅ | YES/UNCLEAR/YES/YES/YES | standard_setting |
| Terra-R2 | conditional | commission | energy union committee | ∅ | YES/UNCLEAR/YES/YES/YES | standard_setting |
| Claude-R1 | positive | commission | energy union committee | member states | YES/YES/YES/YES/YES | delegated_implementation |
| Claude-R2 | positive | commission | energy union committee | member states | YES/YES/YES/YES/YES | standard_setting |

No adjudication is made for this candidate.

## Prepared future human-gate queue

Rules 1–7 plus the reproducible rule-10 audit sample currently mark **21** candidates. The audit sample contains 8 candidates selected from otherwise untriggered unanimous negatives. Its SHA-256 ranking seed is `14247a36cdaf03030cde50e5ffc6a11627d78dd33a0bd45b7b3fbb3d879e42fa`. Rules 8–9 depend on a future RA and therefore cannot yet be evaluated. Marking a row is queue preparation only; no human gate was executed.

## Interpretive boundary

The full substantive signature excludes screening status and all free prose, including `actor.role`, action, object, evidence wording, notes, interpretive note, and confidence. Explicit actor aliases are auditable in `actor_label_aliases.yaml`; unlisted non-trivial labels remain distinct. Provenance limitations are documented separately and prevent causal attribution of cross-family differences.

As quatro codificações são réplicas independentes. As diferenças observadas caracterizam perfis distintos de reconstrução e abstenção, não estabelecem superioridade causal de uma família de modelos.
