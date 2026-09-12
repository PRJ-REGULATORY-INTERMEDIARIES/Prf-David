# Phase 02 — Corpus normalization

`scripts/normalize_corpus.py` parses each case's official ELI-structured
XHTML (BeautifulSoup, `lxml-xml`) and mechanically renders it to Markdown:
headings from title/chapter/article marker elements, body paragraphs
verbatim (whitespace collapsed, non-breaking spaces normalized to regular
spaces), two-column enumeration tables (numbered paragraphs, lettered/roman
sub-points, inline footnotes) flattened to "label + text" lines, and
genuine data tables (`class="oj-table"`, e.g. CBAM's CN-code lists)
converted to Markdown tables. No translation, summarization, paraphrasing,
or semantic labels were introduced; all numbering is the source's own text.

Two bugs were caught and fixed during this run before locking the corpus:

1. BeautifulSoup's `lxml-xml` parser returns the `class` attribute as a
   single string rather than a list (unlike its HTML mode), which silently
   broke a `set(...) & {...}` heading-class check — article/chapter
   headings were rendering as loose body text instead of `##`/`###`
   headings. Fixed with a `get_classes()` helper used everywhere a class
   set is checked.
2. `oj-enumeration-spacing` wrapper divs (used for the numbered intro
   lines of several annexes) were joining their two inline fragments with
   no separator, producing `"1.For the purpose..."`. Fixed to join with a
   single space.

Both fixes were verified by re-running `scripts/validate_corpus.py` (see
below) and by manual inspection of the affected annex text.

## Results

| case | articles | recitals | annexes | act_full.md | act_operative.md | act_recitals.md |
|---|---|---|---|---|---|---|
| case_01 | 14 | 40 | 0 | 64344 B / `3e6e719e...` | 31330 B / `1a398d89...` | 32374 B / `66ff98ba...` |
| case_02 | 36 | 82 | 6 | 169827 B / `e3db2574...` | 120166 B / `82e252e4...` | 48956 B / `cb4efa64...` |
| case_03 | 38 | 86 | 2 | 168670 B / `02486ca4...` | 100338 B / `cc92f49f...` | 67813 B / `a61b0be9...` |

(SHA256 truncated for readability; full values in each case's
`corpus/corpus_manifest.yaml`.)

## Validation

`scripts/validate_corpus.py` independently re-derives article/recital/annex
counts from the raw XHTML (`art_`/`rct_`/`anx_` element ids) and
cross-checks them against `corpus_manifest.yaml` and against the actual
heading/paragraph counts in the generated Markdown, and re-hashes every
file on disk against its manifest. **Result: PASSED — all cases, all
checks** (12 checks per case, 36 total, 0 failures).

State: `source_acquired → corpus_locked`.
