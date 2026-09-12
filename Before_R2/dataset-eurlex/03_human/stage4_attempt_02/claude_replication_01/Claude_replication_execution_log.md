# Claude Replication Execution Log — claude_replication_01

Stage: 4 (independent reference construction), cross-model replication
Scope: operational execution record only. **No substantive comparison between
Claude-R1 and Claude-R2 is performed or contained in this document. No
agreement statistic is computed. No adjudication is performed. No coding was
altered as part of producing this log.**

## 1. Timeline

| Event | Timestamp (UTC) |
|---|---|
| Manifests created | 2026-09-07T17:45:43Z |
| Claude-R1 context spawned | 2026-09-07T17:48:08Z |
| Claude-R1 context closed | 2026-09-07T18:18:23Z |
| Claude-R2 context spawned | 2026-09-07T18:18:46Z |
| Claude-R2 context closed | 2026-09-07T18:58:24Z |

Claude-R2 was spawned only after Claude-R1's context was fully closed. Each
was a separate, memoryless subagent invocation; neither invocation shared
conversational memory with the other or with the orchestrating session.
No summary, statistic, or decision derived from Claude-R1 was placed in the
Claude-R2 prompt.

## 2. Model and effort symmetry

| | Claude-R1 | Claude-R2 |
|---|---|---|
| Provider | Anthropic | Anthropic |
| Model | Claude Sonnet 5 (claude-sonnet-5) | Claude Sonnet 5 (claude-sonnet-5) |
| Reasoning/effort | default, no override | default, no override |
| Agent scaffold | general-purpose subagent | general-purpose subagent |

Identical model and effort confirmed for both contexts.

## 3. Input symmetry

| | Claude-R1 | Claude-R2 |
|---|---|---|
| Coding input file | R1_coding_input.json | R2_coding_input.json |
| Coding input SHA-256 | 813b984c5e80aa03c98bc4399f40644c7d802eedd45f55a2d7a9a787a82d0b38 | 813b984c5e80aa03c98bc4399f40644c7d802eedd45f55a2d7a9a787a82d0b38 |
| Corpus | 02_corpus/act.md (CELEX 32021R1119) | same |
| Corpus SHA-256 | b24a02ea241ca631b606660bb48bb5a2222b29f849c4e4552fb99f871b2e8fd4 | same |
| Codebook | methodology/v1.1.0/codebook.md | same |
| Codebook SHA-256 | c160e153907a786c04070cb09f6e9baa11de709a4432a5f89ebe375a8a7eb472 | same |
| Reference schema | methodology/v1.1.0/reference_coding_schema.json | same |
| Reference schema SHA-256 | abbc4325a5e749cf31836fb24314c27ed22061d6e6539fb435fce8236d5ad2ec | same |
| Validation script | validate_reference_logic.py | same |
| Validation script SHA-256 | b502413da838f1b447ab67b49fe073ab0a1d6a076fe86a9298d9d4a021ff998d | same |

R1_coding_input.json and R2_coding_input.json are byte-identical (same
SHA-256) and contain the same 90 candidate_id values in the same order,
confirmed prior to spawning either context.

## 4. Candidate-count and candidate-ID symmetry (operational only)

- Claude-R1 processed exactly 90 candidates (Claude_R1_output.json: 90
  records, 90 unique candidate_id values).
- Claude-R2 processed exactly 90 candidates (Claude_R2_output.json: 90
  records, 90 unique candidate_id values).
- No candidate was added or removed by either replicate: the set of 90
  candidate_id values in Claude_R1_output.json is identical to the set of 90
  candidate_id values in Claude_R2_output.json (verified by set comparison,
  orchestrator-side, on candidate_id strings only).
- Ordering note (operational, not substantive): Claude-R2's record order
  matches the frozen input order exactly. Claude-R1's record order does not
  match the frozen input order (same set of 90 IDs, different sequence).
  Order was not a frozen constraint in the source manifests; this is recorded
  for transparency and requires no action.

## 5. Schema symmetry and structural validation

- Both outputs use the same reference_coding_schema.json (v1.1.0) and the
  same required-field set (29 keys per record; `secondary_dimensions`
  optional).
- Orchestrator-side check: 0/90 Claude-R1 records and 0/90 Claude-R2 records
  have a missing required key or an undeclared extra key.
- Claude-R1 self-reported validation (Claude_R1_validation_log.md): 90/90
  records valid against reference_coding_schema.json and
  validate_reference_logic.py; 0 schema errors; 0 relational-logic errors.
- Claude-R2 self-reported validation (Claude_R2_validation_log.md): 90/90
  records valid against reference_coding_schema.json and
  validate_reference_logic.py; 0 schema errors; 0 relational-logic errors;
  1 mechanical correction logged (population of the `I` field to match an
  already-recorded condition_C=YES determination for one candidate — logged
  in Claude_R2_validation_log.md; not a substantive re-judgment).
- Both replicates validate structurally.

## 6. Isolation compliance

- Claude-R1 confirmed (self-report) that no file listed in its prohibited-
  file section was opened.
- Claude-R2 confirmed (self-report) that no forbidden file's *content* was
  opened; it disclosed, for transparency, that a directory listing (`ls`) of
  `claude_replication_01/` surfaced the *filenames* of Claude-R1's outputs
  and the shared manifest before it began writing its own outputs — no file
  content was read. All of those filenames were already explicitly named in
  Claude-R2's own prohibited-file list, so no information not already known
  to that context was gained.
- The orchestrating session did not open the content of any Terra/OpenAI
  output, any RA artifact, any stage4_attempt_01 file, any G0/G1/G2 output,
  or strings.yaml at any point in this replication. Their filenames were
  visible in directory listings taken to locate the project and to avoid
  path collisions; content was never accessed.

## 7. Explicit non-actions

This replication did not, and will not as part of this log:
- compare Claude-R1 × Claude-R2 substantively;
- compare Claude × Terra;
- run an RA (adjudication) process;
- run a human gate;
- run Stage 5;
- run G0, G1, or G2;
- alter the codebook;
- alter the candidate universe;
- compute inter-coder agreement;
- select or imply a "better" replicate.

## 8. Conclusion

Both Claude-R1 and Claude-R2 were executed as independent, isolated,
memoryless subagent contexts over the identical frozen 90-candidate universe,
using the same model, effort, corpus, codebook, and schema. Both produced
structurally valid, fully preserved raw and validated outputs. No Terra/
OpenAI, RA, benchmark, or G0/G1/G2 material was accessed. No substantive
comparison has been performed.
