# R3 Dataset Proposal for Regulatory Intermediation in EU Climate Regulation

## 1. Why I rebuilt the pilot

I rebuilt the five-instrument pilot to clarify both its empirical foundations and its analytical architecture. The earlier difficulty was not simply a need for more coding. The project brought together whole-instrument characteristics, actors, institutional attributes, regulatory relations, intermediary functions, mechanisms, and possible higher-order capacities. These dimensions were relevant, but they did not have the same unit of analysis or evidentiary status. Treating them as parallel columns in one spreadsheet risked obscuring the sequence by which a legal text supports a claim about intermediation.

R3 therefore used an independent clean reconstruction from fresh official EU legal sources. The objective was not to reproduce earlier results. It was to build a new provenance chain from official act to validated corpus, whole-instrument profile, actor universe, relation adjudication, intermediary unit, mechanism event, and mechanism configuration. Earlier analytical records were excluded as empirical inputs. At each stage, the outputs were frozen before the next analytical layer began.

This process has produced a proposal that is simultaneously more modest and more useful. It is more modest because the five cases are treated as a pilot rather than a population study. It is more useful because each observation now has a defined analytical unit, legal basis, and place in a relational dataset.

## 2. What changed methodologically

The central methodological change was to replace immediate intermediary classification with staged reconstruction.

First, each instrument was reconstructed as a whole: its objective, regulatory object, target classes, principal authorities, obligations, governance components, and structural logic. Second, all legally relevant actors were registered before R, I, or T roles were assigned. Third, candidate regulatory relations were reconstructed provision by provision. Fourth, every candidate passed a three-condition RIT test: an identifiable R–T regulatory relationship, a distinct institutionalized third actor, and a demonstrable mediating function connecting that actor to the R–T relationship.

Only relations passing that test entered the positive intermediation universe. The same intermediary within one law was then consolidated into a LAW × INTERMEDIARY unit, while its several relations remained separate. Mechanisms were coded one level lower, as elementary transformations within supported relations. Each event was traced through input, mediated object, transformation, output, recipient, and connection to the R–T relation. Mechanism labels were then challenged through an independent adversarial review. Finally, mechanism configurations were reconstructed only after the elementary events had been adjudicated.

The sequence is therefore:

`whole instrument → actors → relations → RIT adjudication → LAW × INTERMEDIARY → mechanism events → configurations`

This sequence matters because institutional attributes, mechanisms, and configurations no longer compete as if they were alternative descriptions of the same thing.

## 3. Main question

The proposed dataset is organized around this question:

> How are regulatory intermediation mechanisms organized and combined across actors and regulatory relations in EU climate regulation, and what regulatory capacities do these configurations appear designed to provide?

The question contains two analytically distinct components. RQ-A asks how mechanisms are organized and combined. The current pilot answers this descriptively. RQ-B asks what regulatory capacities those configurations may provide. The dataset is designed to make that question analyzable, but it does not answer it in advance.

This distinction is intended to prevent a theoretical expectation about capacity from determining how elementary mechanisms are coded.

## 4. Proposed dataset architecture

The proposal distinguishes seven substantive levels.

`LAW` describes the instrument as a whole. `LAW × ACTOR` records the institutional universe before role adjudication. `LAW × INTERMEDIARY` characterizes a legally supported intermediary in a particular law. `R–I–T RELATION` records who regulates whom through whom and concerning what object. `MECHANISM EVENT` records the elementary transformation performed by I. `MECHANISM CONFIGURATION` records how one or more events are organized within a supported relation. `REGULATORY CAPACITY` is reserved as a future derived layer.

Evidence and decision provenance cut across these levels. Evidence records show which legal text supports which coded claim. Decision records show how initial coding, adversarial review, and researcher adjudication produced a final value.

The central proposal is that not all dimensions have the same analytical status. Institutional attributes characterize the intermediary. Relations identify regulatory positions. Mechanisms characterize transformations. Configurations characterize relationships among mechanism events. Capacities, if retained theoretically, must be derived from configurations through explicit rules and alternatives. Governance outcomes require evidence beyond legal design.

The normalized dataset therefore consists of linked tables rather than one master spreadsheet. The workbook in this package is a human-facing view, not the analytical source of truth.

## 5. What the five-case pilot currently shows

The pilot contains five legal instruments and 89 LAW × ACTOR records. It reconstructs 56 adjudicated regulatory relations. Of these, 24 are direct R–T relations, 23 are legally relevant but do not satisfy the RIT test, and 9 are supported intermediation relations. This negative baseline is important: the procedure does not presume that every third actor mentioned in a regulatory arrangement is an intermediary.

The nine supported relations consolidate into seven LAW × INTERMEDIARY units and contain ten mechanism events. The observed event distribution is four `VERIFICATION`, three `EVALUATION_ASSESSMENT`, and three `IMPLEMENTATION` events. These are counts within the five-case pilot and should not be interpreted as estimates of prevalence in EU climate regulation.

Eight supported relations contain one mechanism event. One relation contains two distinct events connected by one legally supported dependency: `VERIFICATION → EVALUATION_ASSESSMENT`. The first event checks systems and operations against applicable rules and audit standards; its findings and identified weaknesses become inputs to a subsequent analysis of weaknesses and corrective action.

The three `IMPLEMENTATION` events are different. The same LAW × INTERMEDIARY unit—public or private implementing entities—appears in three separate relations involving vulnerable households, vulnerable micro-enterprises, and vulnerable transport users. The mechanism repeats independently across target-specific relations. It is not a sequence.

One instrument, CELEX `32015D1814`, contains no supported intermediary, intermediation relation, mechanism event, or configuration. The dataset records this as a substantive zero, not as missing data.

## 6. Mechanism coding

The original operational vocabulary contained nine mechanisms in three provisional families: articulation (`TRANSMISSION`, `AGGREGATION`, `REPRESENTATION`), information treatment (`TRANSLATION`, `INTERPRETATION`, `EVALUATION_ASSESSMENT`, `CLASSIFICATION_RANKING`), and regulatory reliability (`MONITORING`, `VERIFICATION`). The family structure remains a working organization rather than an empirically validated taxonomy.

Initial event coding produced seven confirmed mechanisms and three unresolved events. The unresolved events concerned legally structured implementation and material benefit delivery. During adversarial review, they reached a codebook boundary. Their dominant transformation was not the conversion of legal, scientific, technical, or regulatory content into a different register, so placing them under `TRANSLATION` would have broadened that mechanism beyond its stated definition.

I therefore made a researcher decision: retain the three relations as supported intermediation and provisionally add `IMPLEMENTATION` as a tenth elementary mechanism. `IMPLEMENTATION` describes a formally assigned intermediary converting a legally structured programme, authorized measure, entitlement, intervention, or resources into concrete action or delivery toward a target.

This decision is recorded as `R3-D08-IMPLEMENTATION`. It is not attributed to you, and it is not presented as part of an established published taxonomy. `IMPLEMENTATION` remains `FAMILY_UNASSIGNED_PROVISIONAL`; no fourth family has been created. The original unresolved values, the adversarial codebook-boundary finding, the researcher decision, and the final code are all preserved.

## 7. Why LAW × INTERMEDIARY remains useful

LAW × INTERMEDIARY remains the most useful human-facing comparative unit because it combines institutional identity with attributes such as formal status, institutionalization, participation, separation from the target, independence, orientation, output legal effect, and accountability. It provides a stable way to compare intermediaries without making the actor or the mechanism the sole object of analysis.

However, the unit should function as a parent rather than a flat row containing all information. One intermediary may participate in several relations, face different target classes, and perform several events. The proposed view therefore groups child relation rows under each LAW × INTERMEDIARY and nests mechanism events within each relation. Institutional attributes are shown once at parent level; R, T, regulatory object, mechanism, and configuration remain at their correct lower levels.

This design makes it possible to compare intermediary characteristics while preserving the structure necessary to answer how intermediation occurs.

## 8. How mechanisms combine

The pilot distinguishes three ideas that can otherwise be confused.

First, a single-mechanism relation contains one elementary event. Eight of the nine supported relations have this structure. Second, a sequential configuration contains distinct events whose functional relation is legally evidenced. The audit-body relation has one such sequence: verification findings and identified weaknesses feed a separate evaluation of weaknesses and corrective actions. Third, repeated mechanism use occurs when the same intermediary performs the same mechanism in different relations. The three implementation relations have this structure.

Repeated use across target classes is not a chain. A chain or sequence exists only within a relation when the output or finding of one event becomes a meaningful input to another. The dataset represents this through a separate edge table rather than by inferring order from textual proximity or conceptual similarity.

## 9. What this dataset can answer now

The current pilot can identify which actors function as intermediaries in the selected laws; which elementary mechanisms they perform; how mechanisms are distributed across the observed intermediary types; when multiple mechanisms occur in one relation; when a functional sequence is legally supported; when one intermediary repeats a mechanism across target relations; and how these structures vary descriptively across the five instruments.

It can also demonstrate the value of negative cases. Direct R–T and legal non-RIT relations make the positive intermediation universe contestable rather than assumed. The substantive-zero law demonstrates that the schema can represent absence without manufacturing records.

Most importantly, the pilot validates the proposed relational architecture. A new researcher with the schema and properly coded data could reconstruct the observed distribution and combination of mechanisms from legal evidence and decision provenance.

## 10. What it cannot answer yet

The pilot does not establish population frequencies for EU climate regulation. It does not support causal inference, robust statistical associations between institutional attributes and mechanism types, or validation of latent dimensions. The observed ten events cannot establish that the mechanism vocabulary is exhaustive.

The legal texts support analysis of designed regulatory roles and transformations, not observed effects. The data do not demonstrate improved compliance, enforcement, legitimacy, trust, effectiveness, or other governance outcomes.

The pilot also does not validate higher-order regulatory capacities. Mechanism labels and configurations should not be treated as capacity labels by implication. Nor does the proposal establish a typology of Regulatory Intermediation Architecture.

## 11. Proposed next theoretical layer

A later theoretical phase could ask whether recurrent mechanism configurations appear designed to provide higher-order regulatory capacities. Ideas previously considered by the researcher include `Knowing`, `Assuring`, and `Steering`, but these remain candidates rather than codes or endorsed categories.

The schema reserves a capacity table requiring an explicit derivation rule, empirical basis, theoretical basis, alternative interpretation, confidence, and researcher adjudication. This separation is intended to prevent circularity: a configuration would not count as a capacity merely because a particular mechanism appears in it.

Before proceeding, the project needs conceptual guidance on which capacities are theoretically meaningful, the unit to which a capacity claim should attach, and the evidence threshold required to derive such a claim.

## 12. Questions for David

1. **Unit architecture:** Does the distinction between LAW × INTERMEDIARY, regulatory relation, mechanism event, and mechanism configuration capture the levels you think the dataset should distinguish?
2. **Mechanism level:** Is the current definition of an elementary mechanism at the right level of abstraction for the project?
3. **IMPLEMENTATION:** I provisionally added `IMPLEMENTATION` after three supported relations did not fit the original mechanism vocabulary without stretching `TRANSLATION`. Do you think implementation belongs at mechanism level, or should those cases be conceptualized differently?
4. **Dataset orientation:** Does this architecture move sufficiently from coding-driven classification toward research-question-oriented data design?
5. **Capacity layer:** Do you think the next theoretical step should be to derive higher-order regulatory capacities from mechanism configurations, and if so, which capacities are theoretically most important to distinguish?

These questions concern the proposed conceptual model rather than asking you to adjudicate individual records. The package is intended to make the empirical reconstruction, researcher decisions, and remaining theoretical choices visible enough for that discussion.
