# dataset-eurlex-cleanroom

A ground-up, clean-room rebuild of a three-case EU regulatory-intermediation
dataset. This project is a sibling of `../dataset-eurlex`, not a continuation
of it — see [CLEAN-ROOM RULE](#clean-room-rule) below.

## Scientific purpose

Map regulatory intermediation across three fixed EU regulations, at the
level of the **regulatory relationship** (R → I → T), using a four-level
analytical architecture (act/regime, actor-in-role, intermediary
function/mechanism, regulatory relation/episode). See
`methodology/METHODOLOGY_LOCK.md` (once locked) for the full conceptual
apparatus.

## The three cases (fixed, closed set)

| case | CELEX | act |
|---|---|---|
| case_01 | 32021R1119 | Regulation (EU) 2021/1119 — European Climate Law |
| case_02 | 32023R0956 | Regulation (EU) 2023/956 — Carbon Border Adjustment Mechanism (CBAM) |
| case_03 | 32023R1115 | Regulation (EU) 2023/1115 — Deforestation-Free Products Regulation (EUDR) |

Full registry: [`config/case_registry.yaml`](config/case_registry.yaml).

## Clean-room rule

**Previous empirical results are forbidden inputs.** This project must not
read or import, from `../dataset-eurlex`, any relation datasets, actor-role
datasets, LLM outputs, researcher adjudications, relation counts,
case-specific coding decisions, benchmark files, or uncertainty decisions.

The previous project may only inform this one at the level of **general**
methodological lessons, theoretical references, and infrastructure
patterns (e.g. directory layout, manifest/hashing conventions) — never
case-specific empirical content. See `AGENTS.md` for the operational
version of this rule.

## Directory structure

```
config/         case registry, project-wide configuration
methodology/    METHODOLOGY_LOCK, codebook, coding/actor-role schemas,
                mechanism taxonomy (created once, then frozen)
prompts/        locked primary/secondary/adjudication prompts
cases/
  case_0N/
    source/     act_official.xhtml + source_manifest.yaml (per-case)
    corpus/     act_full.md, act_operative.md, act_recitals.md,
                corpus_manifest.yaml
    primary/    context-isolated primary reader outputs
    secondary/  blind secondary review + cross-review outputs
    human/      human adjudication workbook + decisions
dataset/        assembled cross-case dataset (post cross-review)
scripts/        acquisition, normalization, validation, dataset-build code
tests/          automated checks for the scripts above
logs/           dated phase logs (what was run, when, with what result)
```

## Pipeline state

Current state: **`corpus_locked`** — see [`logs/STATE.md`](logs/STATE.md)
for the full state machine and gate history. The project stops after
corpus normalization and does not proceed to methodology lock or any
coding run without explicit researcher instruction.

## Reproducing acquisition + normalization

```bash
python scripts/acquire_source.py      # downloads the 3 acts from EUR-Lex/CELLAR
python scripts/normalize_corpus.py    # builds act_full/operative/recitals.md
python scripts/validate_corpus.py     # cross-checks hashes and structural counts
```

Source acquisition uses CELEX-based content negotiation directly against
the EUR-Lex / Publications Office CELLAR repository (`Accept:
application/xhtml+xml`), which returns the official Official Journal
XHTML rendition of each act (ELI-structured, CONVEX-generated) — not the
eur-lex.europa.eu website's HTML page. The script refuses to write any
file if the resolved host or content type is not an official EUR-Lex /
Publications Office source.
