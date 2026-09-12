# RA 4-way report — dataset-eurlex, stage4_attempt_02

**Corpus:** Regulation (EU) 2021/1119, CELEX 32021R1119 · **Methodology:** v1.1.0 (frozen)
**Universe:** 90 candidates, frozen · **Package:** blind four-way (`Coder A`–`Coder D`, cryptographically randomized order)
**Adjudicator role:** Reference Adjudication (RA) — independent, not a vote

This report describes the RA's own product. It does not identify which provider, model or
family produced any of Coder A–D, and it does not treat agreement counts as a truth rule.

## 1. Volume

- Candidates processed: **90 / 90** — every candidate was adjudicated from the corpus and
  codebook, not only the ones where the four proposals disagreed.
- Records valid (schema + `validate_relational_logic`): **90 / 90**, after five structural
  corrections described in `RA_4way_validation_log.md` (all `screening_status` only; zero
  mechanical corrections; zero substantive corrections).

## 2. Final distribution

| `relational_result` | n |
|---|---|
| `negative` | 89 |
| `insufficient_evidence` | 1 |
| `conditional` | 0 |
| `positive` | 0 |

| `confidence` | n |
|---|---|
| `high` | 59 |
| `medium` | 30 |
| `low` | 1 |
| `not_assessed` | 0 |

- `I != null`: **5** (all five have `condition_C = YES`)
- `condition_D = YES`: **0**
- `relational_result = positive`: **0**

Per `KNOWN_LIMITATIONS_V1_1.md`, the five `I != null` records are a v1.1.0 structural
artefact: `validate_reference_logic.py` forces `I` to be populated whenever `condition_C =
YES`, regardless of `condition_D`. In all five, the RA determined `condition_D = NO` and
recorded, in each record's own `notes`, that the actor placed in `I` was adjudicated
non-mediating. `I != null` is therefore not read here as a finding of intermediation; the
informative counts are `condition_D = YES` and `relational_result = positive`, both zero.

**Mechanisms of positive relations:** not applicable — the RA found no `positive` candidate
in the frozen universe. The dominant `primary_mechanism` across the 90 records is
`none_or_direct` (31), consistent with an act whose relations are, on independent
re-derivation, overwhelmingly dyadic (Union institutions ↔ Member States) rather than
triadic.

## 3. Relationship between RA and the four proposals

Measured on `relational_result`, over all 90 candidates:

| RA matches how many of the 4 proposals | candidates |
|---|---|
| 4 / 4 | 79 |
| 3 / 4 | 7 |
| 2 / 4 | 0 |
| 1 / 4 | 3 |
| 0 / 4 (RA diverges from all four) | 1 |

The single 0/4 case is `CAND2-27E84BD23730` (Article 13, point (b)): two proposals read
`conditional`, two read `positive`, and the RA — reconstructing the relation independently
before consulting any proposal — reached `negative`. This is the clearest instance in the
dataset of the protocol's governing rule that agreement is not adjudication: neither the 2/4
nor the 2/4 pattern was adopted, and the RA's reasoning is recorded in full in
`RA_4way_adjudication_notes.json` and summarized in §4 below.

Numeric agreement was also not treated as sufficient reason to skip re-derivation on the 79
four-way-matching candidates: several of them were only **partially** adopted from every
proposal (identical `relational_result`, but the RA's own R/I/T reconstruction differed from
some or all four proposals' labels — see `relationship_to_coder_*` in the adjudication
notes for each record).

## 4. The four provisions requiring explicit reasoning

None of the four was adjudicated `positive`. Full reasoning, including the internal same-act
context used, the source-bounded limit identified, and why each competing interpretation was
rejected, is in `RA_4way_adjudication_notes.json`; this section summarizes the ratio
decidendi for each.

### Article 3(4) — national climate advisory body (`CAND2-11BF388480EA`)

`negative`, `direct_relationship` → recorded as `candidate` in the validated file per the
structural-limitation note below · A/B/C/D/E = YES/YES/NO/NO/YES · confidence `medium`.

The paragraph has two limbs; only the second binds. The advisory body's own function
("providing expert scientific advice ... to the relevant national authorities as prescribed
by the Member State concerned") is advice without a documented mediating function
(codebook §6), and its establishment is an invitation, not an obligation. Article 3(3) —
read as internal context — confirms the body is a source of work product ("take into
account, where available, the work of the national climate advisory bodies"), not a
regulatory intermediary. The only binding element is the direct notification duty running
from the Member State to the EEA; R is the EEA, T is the Member States, and there is no
third actor in that relation (`condition_C = NO`). The body's composition and powers are
left to national law, absent from the corpus — recorded as a limit in
`additional_context_required`, though it does not change the outcome, since the binding limb
is independently legible.

### Article 8(3)(b) — reports of the EEA, the Advisory Board and the JRC (`CAND2-465FC96778A7`)

`negative` · A/B/C/D/E = YES/YES/**YES**/NO/YES · confidence `medium`.

R is the Commission (chapeau of Article 8(3)). T is the Member States, reconstructed from
same-act context — Article 6(1)(a), 7(1)(a) and 7(2), all internal cross-references the
corpus itself supplies — not imported from outside. `condition_C = YES`: the EEA and the
Advisory Board are distinct from the Commission and from the Member States (the JRC is not,
being expressly the Commission's own body). `condition_D = NO`: point (b) is one item in a
closed five-item evidentiary list (Member State information, EEA/Advisory Board/JRC reports,
statistics, IPCC/IPBES reports, investment information); treating (b) as intermediation would
symmetrically require treating the IPCC as a regulatory intermediary of Union climate policy
under point (d), which is untenable. Article 3(2)(b) and Article 8(4) confirm both bodies
stand on the regulator's side, supplying inputs, not facing the Member States.

### Article 8(4) — the EEA assisting the Commission (`CAND2-88A2261C68DE`)

`negative`, `direct_relationship` → recorded as `candidate`, same structural-limitation
reason as above · A/B/C/D/E = YES/YES/NO/NO/YES · confidence `medium`.

On the face of the sentence, R is the Commission (owner and conductor of the Article 6/7
assessments, per "the Commission shall assess" in both articles) and T is the EEA, the actor
under the "shall assist" obligation. Read the other way — Commission assessing Member
States with the EEA as a candidate intermediary — `condition_D` is still `NO`: assisting R in
preparing R's own act is a service on the regulator's side, not mediation between R and T.
Nothing in the act gives the EEA a power, duty or communication channel toward the Member
States; Article 7(2) attributes recommendations to the Commission alone. Confidence is
`medium` specifically because the reading of "assist" is acknowledged as materially
contestable, even though the result is not.

### Article 13, point (b) — Commission "assisted by" the Energy Union Committee (`CAND2-27E84BD23730`)

`negative`, `direct_relationship` → recorded as `candidate`, same structural-limitation
reason · A/B/C/D/E = YES/YES/**YES**/NO/YES · confidence `medium`. **RA diverges from all
four proposals** (two `conditional`, two `positive` — see §3).

R is the Commission alone ("the Commission ... shall adopt implementing acts"). T is the
Member States — reconstructed *without* importing the external Article 17(1)–(2) of
Regulation (EU) 2018/1999 that the text cross-references, by using instead Article 7(3)(b)
of this same Regulation ("the Member State concerned shall set out, in its ... progress
report submitted in accordance with Article 17 of Regulation (EU) 2018/1999...") together
with the wording Article 13 itself inserts into Article 17(2)(a) ("information on the
progress ... set out in the integrated national energy and climate plan"). `condition_C =
YES` (the Committee is named and distinct); `condition_D = NO`: the corpus states only that
the Commission "shall adopt" and is "assisted by" the Committee, giving the Committee no
power, function or communication toward the Member States. The Committee's comitology
identity depends on Article 44(1)(b) of Regulation (EU) 2018/1999, not reproduced here —
recorded in `additional_context_required` — but this does not make `condition_D` unclear:
the supplied text affirmatively places the Committee on the regulator's side regardless of
what the absent comitology procedure says, so `condition_E = YES` and the result is
`negative`, not `conditional`. Even on the (rejected) imported reading, the Committee is
composed of Member State representatives and so would not be analytically distinct from T
either — no positive triad is available on any reading the corpus supports.

## 5. Structural-limitation corrections (screening_status only)

Five records — the four above plus `CAND2-AB84F16B6A72` (Recital 37) — were adjudicated with
a distinct-but-non-mediating third actor (`condition_C = YES`, `condition_D = NO`) inside an
otherwise direct R→T relation. `validate_reference_logic.py` simultaneously forbids a
populated `I` under `screening_status = direct_relationship` and requires a populated `I`
whenever `condition_C = YES` — a combination v1.1.0 has no vocabulary for. Only
`screening_status` was moved to the neutral `candidate` value in the validated file; no
condition, actor, mechanism, confidence or `relational_result` was altered for any of the
five. Full detail in `RA_4way_validation_log.md` §3.

## 6. Human gate

Queue size: **22 of 90 candidates** (`RA_human_gate_queue.csv`), built from
`RA_4WAY_PROTOCOL.md`'s ten inclusion rules, applied to the four blind proposals and to the
RA's own decision — never to a majority pattern. The queue is **prepared, not executed**:
`researcher_decision`, `researcher_final_result` and `researcher_note` are present and
empty in every row.

Rule-hit tally across the 22 queued candidates (a candidate may hit more than one rule):

| rule | description | hits |
|---|---|---|
| r5 | divergence in `relational_result` among the four proposals | 11 |
| r7 | R/I/T divergence in a non-unanimously-negative case | 10 |
| r10 | reproducible random audit sample of unanimous negatives | 9 |
| r3 | `insufficient_evidence` in any proposal | 7 |
| r6 | divergence in normalized `I` labels | 6 |
| r4 | `condition_D = YES` in any proposal | 5 |
| r1 | `positive` in any proposal | 4 |
| r9 | RA diverges from all proposals or from the largest agreement grouping | 4 |
| r2 | `conditional` in any proposal | 2 |
| r8 | RA `confidence = low` | 1 |

The rule-10 audit sample (9 candidates, unanimous-negative-with-no-other-trigger pool = 77
eligible) was drawn reproducibly: a SHA-256 seed over the four source validated-output
digests (sorted) and protocol version `1.0.0`, then a per-candidate SHA-256 ranking over that
seed, taking the lowest 9 — the same method specified in `RA_4WAY_PROTOCOL.md` for the
pre-RA comparator, applied here at the RA stage since the RA product is what the queue must
finally reflect.

## 7. Status

```
RA_completed: true
RA_validated: true
human_gate_prepared: true
human_gate_executed: false
benchmark_locked: false
experiment_started: false
```

No provider, model or family identity was disclosed anywhere in this report or in any
artifact it describes. No file under `ra_4way_private/` was opened while producing it.
