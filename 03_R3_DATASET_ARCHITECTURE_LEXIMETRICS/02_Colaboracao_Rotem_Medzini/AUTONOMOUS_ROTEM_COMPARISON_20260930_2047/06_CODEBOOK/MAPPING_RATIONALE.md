# MAPPING_RATIONALE (R06)

## 1. Three layers, kept separate (delta §6)

| Layer | Content | Where documented |
|---|---|---|
| **L1 — Rotem's conceptual architecture** | What she wrote in her reply (lines 6–20) | quotes in `ROTEM_CONCEPTUAL_OPERATIONAL_ALIGNMENT_MATRIX.csv` |
| **L2 — Rotem's documented codebook** | (a) UNREV + Chart Key (`UNREVISED_BASELINE`); (b) REV | `ROTEM_FIELD_DICTIONARY.csv` (86 REV variables), `CODEBOOK_VERSION_DIFF.md` |
| **L3 — Rotem's implemented workbook** | Columns and values actually present (CDI, LoA, LoI) | `01_BASELINES/BASELINE_ROTEM_WB_*.csv` |

A divergence between layers is classified first as `DOCUMENTATION_IMPLEMENTATION_GAP`. It is treated as a defect only after substantive analysis (R09). Chronology matters here: the workbook was last saved on 2 Sep and REV on 28 Sep (VERSION_MAP). L3 cannot be expected to implement L2(b).

## 2. Mapping rules used
1. **Attribution.** A field is attributed to Rotem only if it appears in L2 (with its ¶) or L3 (with sheet and column). Everything else in our child schema is labelled `PROPOSED` (`CONCEPTUAL_CROSSWALK.csv`).
2. **Granularity differences are named as such.** Where a child field is an *instance* of one of Rotem's categories (REGULATOR_ACTOR vs `regulator_context`), the relation is `INSTANCE_OF_CATEGORY` or `FINER_GRAIN`, not "missing in Rotem".
3. **No back-projection.** We do not say how Rotem *would* code a case under REV. Where we apply REV to a case, the value is `INTERPRETIVE_APPLICATION` and is ours.
4. **Embedded commentary excluded.** The critique inside the UNREV file (¶145–¶339) is not Rotem's text. Several of its recommendations (two linked tables; recognition as stages; derived obligation intensity; actor vs mechanism; sharper assurance/auditing/monitoring rules; `Position_in_governance_chain` as relational) **pre-date** this comparison. Their author is not established.

## 3. Corrections and ambiguities on *our* side (Igor's relational approach)

| # | Ambiguity or overclaim | Evidence | Correction adopted |
|---|---|---|---|
| C1 | Treating "legal basis for identifying an intermediary" as if it were Rotem's recognition variable, or as a competitor to it | Rotem l.14 (`INDIRECT_EVIDENCE_VIA_ROTEM_REPLY`; Igor's original comments are not on disk, I-004) | Separate concepts: identification basis = which clause of REV ¶27 (assign / recognize / rely upon) licenses inclusion; recognition = formal approval or selection pathway (regulation **of** the intermediary). Never merged |
| C2 | Presenting a "law × intermediary table", "orientation" or "modality" as our innovation | REV ¶22–¶24, ¶79 already contain INTERMEDIARY_MAP, orientation, contexts and intermediary_involvement | Our only candidate addition is **provision/event-level** granularity beneath her unit |
| C3 | Describing PILOT_03 as a "structural extraction pilot" with "two independent model passes" | I-009, I-014 | PILOT_03 = relational-coding pilot on 33 provisions of 10 pre-2007 acts. Passes A/B scripted. 19 human decisions on constructed disagreements |
| C4 | Using a broader intermediary concept (public bodies such as the EEA; insurers via structural reliance) without flagging the framework difference | R3 LAW × INTERMEDIARY (I-013); PILOT_03 H_009/H_010 vs REV ¶28 (I-017) | Reported as framework differences, in both directions: on public bodies our concept is broader than REV ¶31; on insurers it is narrower than REV ¶28 |
| C5 | Assuming provision-level excerpts are faithful | 16/16 blind-challenge excerpts are paraphrases (I-015) | Child layer stores verbatim spans from official texts only |
| C6 | Treating R4 defect statistics as evidence about relational coding | R4.2 fields come from a regex script (I-012) | R4 used only as a catalogue of risks for provision-level extraction |

## 4. What the crosswalk implies before any case is coded
- **Already covered by REV's row-level fields (not by our proposal):** unit, multi-valued contexts, orientation, involvement modality, functions, mechanisms, relevant provisions, rationale (partial).
- **Absent from REV at any level** (candidates to test, not conclusions):
  - (i) **event granularity:** which actor does what to whom under which provision;
  - (ii) **verbatim text spans;**
  - (iii) **legal effect as a separate field;**
  - (iv) **an explicit record of the ¶27 inclusion clause (identification basis);**
  - (v) **decision-level linkage of each code to its provision** (Rotem's rationale fields are value-specific for some variables only).

  R07–R10 test whether these add substantive information in real cases, and where they do not.
