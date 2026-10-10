# PILOT_03_REPORT

## Gate

`PILOT_03_AWAITING_HUMAN_ADJUDICATION`

The pilot is intentionally stopped before human adjudication. No final reliability gate, ontology gate or production authorization is claimed.

## Scope

- Calibration: 5 acts and 17 frozen PILOT_02 source provisions.
- Blind challenge: 5 additional acts and 16 official-source provisions.
- Model A/B: 33 candidate rows per pass, with 19 disagreement cells across the compared fields.
- The two passes are model-independent source-first passes, not human coders.

## Frozen design decisions

Binary A→B is primitive; R–I–T is derived; intermediary is a relational position; Device/Instrument is autonomous; direct and derived relationship type are separate; action is verbatim plus normalized.

## Challenge logic

The blind cases are drawn from already assessed material and were selected for boundary pressure: testing laboratories, national regulatory authorities, IP-enforcement intermediaries, collecting societies and standardization committees. The selection was purposive, not a convenience sample and not a corpus expansion.

## What remains open

Human review must adjudicate direct-edge versus composite readings, function/mechanism boundaries, device coding, direct versus derived relationship type, and conditional intermediary status. The response template preserves `BOTH_IN_PART`, `NEITHER` and `UNRESOLVED`.

## Reproducibility

Source provisions, model passes, comparison, preregistered RIT rules, blank human packet and issue register are stored in this folder. The generator is `99_REPRODUCIBILITY/build_pilot03.py`.
