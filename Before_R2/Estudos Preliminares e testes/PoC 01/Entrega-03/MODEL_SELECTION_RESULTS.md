# Model Selection Results

**Status: not yet run.** This file is a placeholder, kept deliberately
separate from `MODEL_SELECTION_PROTOCOL.md` so that, once results exist, it
is visible that the protocol was not retrofitted to match them.

To be filled in only after:
1. Tier 0 anchor checks pass (see `MODEL_SELECTION_PROTOCOL.md`).
2. Igor has hand-adjudicated the Tier 1 held-out set independently.
3. `scripts/model_selection_experiment.py --tier 1` has been run against
   the confirmed, priced model(s).

## Template for when results exist

```
## Run metadata
- Date:
- Model(s) tested:
- Model snapshot(s) (pinned):
- Prompt version:
- Schema version:
- Tier 0 anchor checks: PASS / FAIL (detail)
- Adversarial context test result: PASS / FAIL (detail)

## Tier 1 scorecard (n = ??)
| Criterion | Weight | Model A score | Model B score |
|---|---:|---:|---:|
| ... | ... | ... | ... |
| **Weighted total** | 100% | | |

## Decision
Winning model: ...
Tie declared: YES/NO
Rationale:

## Known failure modes observed
(quote specific disagreements/hallucinations found, do not summarize away)
```
