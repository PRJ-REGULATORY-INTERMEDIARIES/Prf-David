# G2 — Track A execution prompt (next independent iteration)

## Authorization boundary

This prompt may be used only after confirming the following G1B/G1C freeze remains intact:

- `COMMON_STATEMENT_REGISTER.csv` SHA-256: `417A35A361E44F8BECFBD8FC39B34738C026591C59B7E837FDDF292F9EF3E77F`.
- P03 primary source FE-001 SHA-256: `01D5BDB117B370AE9DAD7F3ABB151583A75519CBAD0E7808EFC9040C8D656888`.
- P04 primary source FE-003 SHA-256: `62AFB4DDCCAE5E7157590B1386040AA8D160701D7194DBD2F2403AC4B6781449`.
- Scope: P03 and P04 only, 20 common statements, with P04 Article 22(7) excluded.

If any controlling hash differs, stop and report `BLOCKED_SOURCE_INTEGRITY`. Do not change the common register, source files, historical PILOT_03 records, or frozen manifests.

## Task

Conduct **prospective V8-COMP-01 Track A only**: apply V8 relational leximetrics to the frozen common statement evidence **without** the additional eight-operation architectural reconstruction protocol.

1. Begin from `COMMON_STATEMENT_REGISTER.csv`; use the official HTML only to resolve a cited wording question, preserving the same scope.
2. Log every inferential step, source anchor, uncertainty, and stopping-rule decision.
3. Do not use historical PILOT_03 Model A/B classifications or human adjudications to fill gaps or predetermine a conclusion. They may be labeled reference material only after the independent Track A result is frozen.
4. Do not add P04 Article 22(7), new provisions, new laws, or inferred actors absent from the source without a registered amendment.
5. Evaluate against the predeclared criteria in `COMPARISON_EVALUATION_CRITERIA.md`: traceability, inferential defensibility/errors, unsupported relationship attribution, cross-level errors, structural clarification, uncertainty/stopping compliance, incremental value, and effort.
6. Save all Track A outputs and a Track A QA record; calculate hashes and declare Track A `FROZEN` before any Track B work begins.

## Prohibitions

- Do not execute or sketch Track B conclusions.
- Do not retrofit Track A using Track B.
- Do not commit, push, reset, switch branches, or modify protected historical artifacts.

## Required handoff

Report the frozen input hashes, each statement processed, each relationship accepted/rejected/deferred with reason, ambiguity treatment, evaluation metrics, effort record, and a clear statement that Track B remains unstarted.
