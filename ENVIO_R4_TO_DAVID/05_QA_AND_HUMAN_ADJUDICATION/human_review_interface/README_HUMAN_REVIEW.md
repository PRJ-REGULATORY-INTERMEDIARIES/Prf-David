# R4.2B Human Review Interface

This folder is a separate manual-review package. It does not modify the original Luna extraction or the original 90-row QA sample.

## Use

1. Open `R4_2B_HUMAN_REVIEW_PANEL.html` in a standard browser.
2. Review the full frozen legal provision against the Luna extraction.
3. Answer only extraction-fidelity questions: actor, action, object, counterpart, recipient, source pointer, excerpt and structural ambiguity.
4. Do not decide regulator, intermediary or target status, and do not classify mechanisms.
5. Use **Save locally** to persist decisions in the browser's local storage.
6. After completing the review, use **Export CSV** and/or **Export JSON** and preserve the exported file as the researcher-reviewed record.

## Files

- `R4_2B_HUMAN_REVIEW_WORKING.csv` â€” 90-row working dataset with full source provision and adjacent context.
- `R4_2B_HUMAN_REVIEW_PANEL.html` â€” self-contained local interface; no server or external resources required.

The working dataset starts with all human decision fields blank and all rows `PENDING`. The default reviewer display is `Igor Caires Machado`, but a row is not marked reviewed until the required choices are explicitly completed.

The legal text comes only from the frozen R4.1 processing corpus. The original truncated Luna excerpt remains separately visible and is not silently replaced.