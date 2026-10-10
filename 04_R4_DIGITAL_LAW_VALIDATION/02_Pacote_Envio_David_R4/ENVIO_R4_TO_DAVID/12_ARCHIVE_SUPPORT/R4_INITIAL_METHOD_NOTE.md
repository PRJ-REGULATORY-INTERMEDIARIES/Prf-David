# R4 Initial Method Note

**Status:** baseline package prepared; STOP condition reached  
**Date:** 2026-09-25  
**Scope:** R3 baseline reconstruction and R4 methodological setup only

## 1. What was inherited from R3

R4 inherits the R3 relational architecture: `LAW`, `LAW × ACTOR`, `LAW × INTERMEDIARY`, regulatory relations, mechanism events, mechanism configurations, legal evidence and decision provenance. R3 treats regulatory intermediation as a relation rather than a permanent property of an organization. The inherited intermediation gate requires an identifiable R–T relationship, an institutionally distinct third actor, and a demonstrable mediating function.

R3 also inherited the separation of actor, legal action, regulatory function, mechanism, institutional technology, legal effect and systemic effect. Its mechanism trace is organized as input → mediated object → transformation → output → recipient → regulatory relevance. Negative relations and the substantive-zero law remain visible rather than being discarded.

The R3 freeze contains nine operational mechanisms—`TRANSMISSION`, `AGGREGATION`, `REPRESENTATION`, `TRANSLATION`, `INTERPRETATION`, `EVALUATION_ASSESSMENT`, `CLASSIFICATION_RANKING`, `MONITORING` and `VERIFICATION`—plus the researcher-added provisional `IMPLEMENTATION` mechanism. The latter is frozen as an inherited empirical decision under `R3-D08-IMPLEMENTATION`; it is not treated as a generally validated taxonomy or as a category attributed to David Levi-Faur.

## 2. What is frozen for the initial R4 test

The following are frozen and cannot be silently changed during initial digital analysis:

- units of analysis and parent–child table relationships;
- R, I and T role criteria;
- the three-condition intermediation gate;
- the mechanism vocabulary, including provisional `IMPLEMENTATION`;
- the distinction between mechanism and institutional technology;
- confidence and uncertainty as visible fields rather than forced classifications;
- legal evidence and decision provenance as separate layers;
- negative, direct and zero cases;
- independence from Rotem Medzini’s coding until the independent R4 dataset is locked.

An apparent digital-law mismatch must first be recorded as a codebook-gap or transportability finding. It must not be repaired by changing R3 retrospectively.

## 3. Authoritative R3 decisions and provenance limits

The R3 technical note identifies a freeze date of 2026-09-21 and reports 5 laws, 89 LAW × ACTOR records, 56 adjudicated relations, 9 supported intermediation relations, 7 LAW × INTERMEDIARY units and 10 mechanism events. The human decision `R3-D08-IMPLEMENTATION` is the final material conceptual decision located for the inherited mechanism layer.

The available R3 package is external to the target repository’s commit `27ba3e4`. The workbook is a human-facing package and declares that normalized linked R3 tables remain the analytical source of truth. Separate normalized tables, phase manifests, validation scripts and granular historical model logs were not located in the audited locations. This is an open provenance limitation, not permission to reconstruct missing records.

The target repository also contained 12 staged R2.1 additions under `WORK_2_1/PILOT_R2_1/`. They were preserved and excluded from R3 authority. No R3 source file was modified.

## 4. Human–AI division of labor

### Human-final tasks

The researcher retains final authority over theory, research design, the unit of analysis, intermediary criteria, mechanism taxonomy, ambiguous R–I–T classifications, adjudication, codebook changes and cross-domain conclusions. Human review is mandatory for low-confidence cases, role overlap, cross-provision reconstruction, mechanism overlap, codebook gaps, model disagreement and any decision that would alter the frozen architecture.

### Luna High tasks

Under the governing protocol, Luna High is the first-line model for low-inference, repetitive and structured operations: inventory, metadata, CELEX checks, source registration, segmentation, explicit actor/reference extraction, normalization, deduplication and schema QA. Luna outputs remain proposals where interpretation is required.

### Terra High tasks

Terra High is required when substantive inference is necessary: complex legal reading, R/I/T distinction, intermediary identification, mechanism identification or classification, nested or hybrid arrangements, delegation, assurance, certification, auditing, monitoring architecture, role overlap and difficult adjudication support.

### Hybrid tasks

The intended sequence is `Luna High → Terra High → Human Adjudication`. Extraction must remain separate from interpretation. Every substantive record must preserve legal evidence, AI proposal, confidence, human status and final decision in distinct fields.

The present setup run was executed in the Codex runtime. The exact Luna/Terra variant was not exposed to this environment, so the execution log records that fact rather than retrospectively labeling the work as Luna or Terra. No model escalation occurred in this setup phase.

## 5. Digital corpus registered

The fixed cases are:

- `D1_GDPR` — CELEX `32016R0679`;
- `D2_DSA` — CELEX `32022R2065`;
- `D3_AI_ACT` — CELEX `32024R1689`.

The official EUR-Lex URLs, English language and registration metadata are recorded in `R4_DIGITAL_CORPUS_REGISTER.csv`. The texts were not downloaded, hashed or substantively analyzed in this phase. Therefore, the register is a source-registration artifact, not a completed legal corpus.

## 6. What cannot yet be concluded

This phase does not establish any digital intermediary, R–I–T relation, mechanism, mechanism chain, cross-domain difference, variable recommendation or codebook change. It does not compare R4 with Rotem Medzini’s independent coding. It does not establish that the R3 workbook fully recovers the missing normalized source tables or historical model provenance.

## 7. Next R4 phase — exact proposed scope

After human review of this baseline package, the next phase should:

1. acquire fresh official EUR-Lex texts for the three registered CELEX acts;
2. record exact source version, language, retrieval timestamp, legal status and SHA-256 in per-case manifests;
3. verify text completeness and create source/corpus provenance copies;
4. run structural and schema QA only;
5. stop before substantive actor, R–I–T or mechanism coding unless separately authorized.

Substantive extraction and interpretation should begin only in a later authorized phase, with Rotem’s coding remaining outside the independent R4 context until the R4 dataset is reviewed, adjudicated, versioned and frozen.

## 8. Stop condition

The initial R4 baseline package is complete. The project must now stop and await human review and explicit authorization for the next phase.

## Post-Initial Baseline Enrichment

**Date:** 2026-09-26

The complete R3 historical archive became available after R4.0 and was integrated under `R4.1B` as read-only historical provenance. The initial provenance limitation concerning unavailable normalized R3 tables and granular decision logs was resolved for the supplied `PRJ-DAVID-R3.zip` archive, with the original limitation retained in the baseline manifest for chronological transparency.

Project communications were archived under `R4.1C`. The communications archive is complete with documented gaps: secondary references remain distinct from original communications, and no missing message was reconstructed by inference.

No substantive digital coding was performed during `R4.1B` or `R4.1C`. Digital structural extraction, digital R–I–T coding and digital mechanism coding remain not started.
