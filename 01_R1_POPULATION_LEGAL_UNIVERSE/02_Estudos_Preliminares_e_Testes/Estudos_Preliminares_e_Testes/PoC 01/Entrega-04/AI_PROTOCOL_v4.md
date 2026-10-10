# AI protocol v4

The model is an assisted interpretive coder, never the final authority.

## Stages

- **A2:** semantic candidate detection on one provision, complementary to
  lexical Stage A1;
- **B1:** architecture reconstruction without assigning R/I/T;
- **B2:** independent answers to the five-condition relational test;
- **C:** individual institutional attributes for already-positive
  relationships.

Every stage uses a strict JSON Schema. Evidence must be verbatim and present
in the supplied legal package. Abstention is valid when evidence is missing.
The package is corpus-constrained and the model may request one specific
additional provision; unresolved or repeated requests go to human review.

## Repetition and provenance

Each unit is run three times. Substantive disagreement on verdict, actor
identity or mechanism routes the unit to review. Each log row records provider,
model id, operational snapshot, reasoning setting, prompt/schema versions,
timestamp, input/output hashes and token usage.

The v4 dry-run log contains 201 schema-valid records: 20 units × A2/B1/B2 ×
three runs, plus seven inherited positive relationships × C × three runs. It
contains placeholders, not findings. The live OpenAI attempt could not start
generation because the project had no remaining API credits.

## Promotion rule

No AI output is merged into `candidate_adjudications_v4.csv` or
`rit_relationships_v4.csv`. A researcher must inspect evidence, adjudicate the
case independently, and record `ai_assisted=1` and a precise `ai_run_ref` if
an AI proposal informs a later authoritative row.

The model may not code effectiveness, legitimacy, trust, polycentricity,
autonomy index or accountability index.
