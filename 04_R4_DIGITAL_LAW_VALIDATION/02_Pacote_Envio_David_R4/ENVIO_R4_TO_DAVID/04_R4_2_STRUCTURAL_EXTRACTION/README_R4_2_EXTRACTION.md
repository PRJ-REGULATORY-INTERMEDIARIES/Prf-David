# 04 — R4.2 structural extraction

The artifacts produced when the 1,404 records were extracted.

**`R4_2_METHOD_NOTE.md`** sets out the extraction method and the unit of analysis.
**`R4_2_AI_EXTRACTION_RUN_SUMMARY.csv`** records the extraction run itself, and
**`R4_2_SOURCE_COVERAGE_REPORT.csv`** shows how much of each instrument the extraction covers.

Four registers capture what was found across the corpus rather than per record:
**`R4_DIGITAL_ACTOR_CANDIDATE_REGISTER.csv`** (candidate actors),
**`R4_LEGAL_ACTION_REGISTER.csv`** (legal actions),
**`R4_LEGAL_DEFINITION_REGISTER.csv`** (definitions given in the instruments) and
**`R4_CROSS_REFERENCE_REGISTER.csv`** (cross-references between provisions). These are useful if
you want to see the vocabulary the digital corpus actually uses before any theoretical coding.

**`R4_STRUCTURAL_AMBIGUITY_LOG.csv`** records ambiguities the extractor flagged at the time, and
**`R4_2_HUMAN_QA_SAMPLE.csv`** is the initial sample drawn for human checking.

A caution when reading these: the extraction stage is descriptive and pre-theoretical. It does
not classify regulators, intermediaries or targets, and the later validation stages showed that
several of its fields need repair before they can support that classification.

```text
RIT_CODING             = NOT_STARTED
MECHANISM_CODING       = NOT_STARTED
ROTEM_CODING_CONSULTED = NO
R4_3                   = NOT_STARTED
CORPUS_WIDE_REPAIR     = NOT_EXECUTED
```
