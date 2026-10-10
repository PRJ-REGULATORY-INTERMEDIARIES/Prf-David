# Validation protocol

Supersedes `GOLD_STANDARD_VALIDATION.md` in terminology and scope (that file
is kept, unmodified, for the record). Two changes: "gold standard" is
replaced by **pilot reference sample** — the earlier term implied a
finality this small, non-random sample cannot support; and this document
separates **Stage A validation** (done) from **Stage B validation**
(scoped, not done).

## Stage A validation — done
Method and result unchanged from `GOLD_STANDARD_VALIDATION.md`: for one
article per act, every paragraph was read manually, without regex, and
marked for whether it substantively concerns an intermediation relationship
(not merely whether it repeats an anchor term). That reading — the **pilot
reference sample**, not a gold standard — was then compared against
`codebook_screen.py`'s output on the same paragraphs.

**Result (35 judged units):** precision 100% (33/33), recall 94.3% (33/35),
F1 97.1%. Both misses share one cause: the paragraph describes the same
relationship from the regulator's or the target's side, without repeating
the intermediary's own name. Full detail, including both misses quoted in
full: `GOLD_STANDARD_VALIDATION.md`.

**Scope limits, stated plainly:** the sample is small, non-random (the
richest article per act, not a random draw), and tests only whether Stage A
correctly flags paragraphs that concern *some* intermediation content — not
whether the mechanism assigned is the right one, and not recall outside the
four coded articles.

## Stage B validation — scoped, not yet done
The relationship-level coding in `data/rit_coded_sample_v2.csv` (9 R-I-T
relationships) has **not** been independently checked by a second coder.
This is the correct next validation step, not a gap to paper over:

1. A second coder (human or NLP-assisted) independently applies
   `RIT_CODEBOOK.md` to the same four articles, blind to the first coder's
   `rit_coded_sample_v2.csv`.
2. Compare `R_actor`/`I_actor`/`T_actor` identification and
   `intermediary_validated` decisions between coders.
3. Compute inter-coder agreement (proportion agreement at minimum; Cohen's
   kappa where the category counts support it).
4. Adjudicate disagreements explicitly, and revise `RIT_CODEBOOK.md` where
   the disagreement reveals an ambiguous instruction, not just a careless
   read.

This has not been run — nine relationships coded by one person is a
plausibility demonstration of the architecture, not a validated dataset.
Treating it as validated without this step would repeat, at the relationship
level, the same overclaiming that the `screening_confidence` renaming was
meant to fix at the paragraph level.

## Why precision/recall alone cannot validate Stage B
Stage A validation asks a binary question (paragraph flagged correctly or
not) that precision/recall/F1 fit naturally. Stage B coding is not binary —
it assigns roles, chain structure, and multiple attributes per relationship.
Inter-coder agreement (not a single precision/recall number) is the right
instrument once a second coder is available; computing precision/recall for
Stage B before that would understate how much judgment each row required.
