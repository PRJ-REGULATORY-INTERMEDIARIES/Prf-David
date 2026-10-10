# The Legal Universe: Six Parameters for Discussion (U1–U6)

**Prepared for:** discussion with David Levi-Faur
**Date:** 9 October 2026 | **Status:** discussion note. It records no decision and attributes none.
**Workstream:** EU Regulatory Data Scoping — choosing, on documented evidence, the source of EU legislation for the dataset of regulatory governance architectures.

## Why this is on the table now

Before we compare candidate sources of EU legislation, we have to say what the source must be able to deliver: which acts, from when, in which versions. If we leave that open and look at the sources first, "sufficient coverage" ends up meaning whatever the preferred source happens to cover.

So we need an **envelope**: a deliberately wide statement of the legal universe that any candidate source is tested against. The envelope is not the final universe and it is not the sample. It only has to be wide enough that the eventual universe will fall inside it.

Three decisions stay separate throughout:

| Decision | Question | When |
|---|---|---|
| Source | Which infrastructure supplies texts and metadata? | This workstream |
| Legal universe | Which acts are eligible in principle? | Envelope now; final definition later |
| Cases | Which acts are coded intensively when the framework is applied? | Later, in the sampling protocol |

For each parameter below, the note separates **what the source decision needs now** from **what can wait for sampling**.

*A caution on facts.* Statements about EU legal publishing in this note come from general knowledge of the field. None was checked against the sources in this phase, and each should be verified before it is relied on.

## Summary

| | Parameter | Needed now for source selection | Can wait for sampling |
|---|---|---|---|
| U1 | Types of legal acts | Are non-legislative acts (delegated, implementing) inside? Is soft law inside? | Which act types are actually sampled |
| U2 | Temporal coverage | Earliest date; cut-off date; adopted-in-period or in-force-at-date | Period strata; number of acts per period |
| U3 | Material scope | Whether the envelope is all-domain or sector-bound; if sector-bound, by which classification | Which sectors are compared |
| U4 | Territory and normative levels | Whether national implementing measures must come from the same source | Which Member States, if any |
| U5 | Languages and document versions | Which language(s) the source must supply | — |
| U6 | Legal status and change over time | Which versions must be retrievable: original, consolidated, full history; repealed acts in or out | Which version of each sampled act is coded |

**U6 and U1 carry the most weight for the source decision.** U3 can stay wide at almost no cost.

---

## U1 — Types of legal acts

**What is at stake.** Whether the universe stops at legislative acts or follows the chain into the acts adopted under them.

| Option | Content | Consequence for the research | Consequence for the source |
|---|---|---|---|
| A | Regulations and directives adopted as legislative acts | Smallest and cleanest universe. Architectures are observed as designed by the legislator; what is specified later, in acts adopted under delegated or implementing powers, is not observed | Any general legislative source is likely to suffice |
| B | A, plus decisions and delegated and implementing acts | Delegation chains become traceable from the basic act to the acts that operationalise it. The universe grows substantially, and most of the growth is technical | The source must distinguish act types reliably in its metadata and link each non-legislative act to its basic act |
| C | B, plus non-binding instruments (recommendations, guidelines, communications) and, possibly, international agreements | Captures steering that operates outside binding law. Boundaries of the universe become hard to draw | No single source is likely to hold this material consistently; a multi-source design becomes unavoidable |

**Needed now.** Whether delegated and implementing acts are inside the envelope, and whether soft law is.
**Can wait.** How many acts of each type are sampled, and whether basic acts are sampled together with the acts adopted under them.
**Question for discussion.** Does applying the framework require reading the acts adopted under a basic act, or is the basic act the unit of observation?

## U2 — Temporal coverage

**What is at stake.** How far back the universe reaches, where it stops, and whether "period" refers to adoption or to being in force.

| Option | Content | Consequence for the research | Consequence for the source |
|---|---|---|---|
| A | Acts adopted since the Lisbon Treaty entered into force (December 2009) | One stable typology of acts throughout. No long-run comparison | Least demanding: recent acts are the best structured and documented |
| B | Acts adopted since an earlier institutional milestone (for instance the single-market programme or Maastricht) | Allows comparison across institutional periods. Act types and procedures change within the period and need a concordance | Older acts may lack structural markup or be available only as scanned text; quality must be tested by period |
| C | The whole history of Community and Union law | Full longitudinal reach | Most demanding on completeness, formats and language availability for early decades |

A second choice cuts across the first:

- **Flow:** all acts *adopted* within the period, whatever happened to them later.
- **Stock:** all acts *in force* on a reference date, whenever adopted.

A stock universe describes the architecture standing on a given day but drops everything repealed or replaced, which distorts any reading of change over time. A flow universe keeps the history but includes acts that no longer apply. The two make different demands on a source (see U6).

**Needed now.** The earliest date, a fixed cut-off date, and flow versus stock.
**Can wait.** Period strata and the number of acts drawn from each.
**Question for discussion.** Is change in regulatory architectures over time part of what the dataset should show, or is the aim a cross-section?

## U3 — Material scope and regulatory sectors

**What is at stake.** Whether the universe is all of EU law or a set of regulatory sectors.

| Option | Content | Consequence for the research | Consequence for the source |
|---|---|---|---|
| A | All policy domains | Nothing is excluded in advance; sector comparisons are designed later | The source must be general. No subject classification is needed to delimit the universe |
| B | A predefined set of sectors | Sharper focus; results speak to those sectors only | The universe has to be delimited by some subject classification (thesaurus descriptors, directory codes, legal basis). That classification becomes a requirement on the source, and its quality becomes part of what we assess |
| C | Acts selected because they establish or use intermediaries | Maximises relevance to the substantive question | Cannot define a universe in advance: knowing which acts qualify presupposes the coding. This is a sampling criterion, not a universe criterion |

**Needed now.** Only whether the envelope is all-domain. An all-domain envelope costs the source assessment almost nothing and keeps every later option open.
**Can wait.** The choice and number of sectors; any theory-driven selection of acts.
**Question for discussion.** Is there a reason to restrict the *universe* by sector, as distinct from choosing sectors at the sampling stage?

## U4 — Territorial scope and normative levels

**What is at stake.** Whether the universe is Union-level law only, and which levels of Union law it contains.

| Option | Content | Consequence for the research | Consequence for the source |
|---|---|---|---|
| A | Union secondary law only | The architecture as written at Union level. For directives, national design choices are not observed | One Union-level source can suffice |
| B | A, plus the record of which national measures transpose each directive (the link, not the text) | Shows where national implementation exists without reading it | The source must expose transposition links, or a second source must |
| C | A, plus the texts of national implementing measures for selected Member States | Observes intermediaries created or designated nationally | No single source; national repositories differ in language, format and coverage. A different study in scale |

Two further level questions: whether **primary law** (the Treaties) belongs to the universe or serves only as context, and whether **international agreements** are included.

**Needed now.** Whether national implementing texts must be obtainable from the selected infrastructure. If not, this parameter does not constrain the source choice.
**Can wait.** Which Member States and which directives, if national measures are studied at all.
**Question for discussion.** Where directives leave the designation of intermediaries to Member States, is the Union-level text sufficient for the framework's purposes?

## U5 — Languages and document versions

**What is at stake.** Which language version is read, and in which document form.

| Option | Content | Consequence for the research | Consequence for the source |
|---|---|---|---|
| A | English only | Simplest; consistent with the English texts used in the project's earlier rounds. All language versions are equally authentic, so English-only is a practical choice, not a legal one. English texts of early acts are later translations | Any source with English coverage |
| B | English, with one or two further languages available for checking ambiguous provisions | Lets a coder resolve doubts against another authentic version | The source must supply aligned versions of the same act and identify them unambiguously |
| C | All official languages | Needed only for multilingual or computational designs | Highest demand on completeness; availability varies with accession dates |

"Document version" also means **form**: the published Official Journal text, a structured format with machine-readable articles and annexes, or a rendered page. Structured formats make provision-level citation reproducible; published forms carry the legal authority. Ideally the source offers both and links them.

**Needed now.** The language or languages the source must supply, and whether provision-level structure is required.
**Can wait.** Nothing of substance.
**Question for discussion.** Is a second language needed as a check on interpretation?

## U6 — Legal status, amendments, consolidations and repeals

**What is at stake.** Which text of an act is "the act" for our purposes. An act as adopted, the same act after twenty amendments, and its current consolidated version can describe different architectures.

| Option | Content | Consequence for the research | Consequence for the source |
|---|---|---|---|
| A | The act as originally adopted | Each act read as the legislator first designed it. Later redesign is invisible unless amending acts are sampled as acts in their own right | Least demanding; the published original is the authoritative text |
| B | The version in force on a reference date | The architecture as it stands on that date. Consolidated texts are editorial compilations and, as generally understood, not themselves legally authoritative; they can lag behind recent amendments | The source must supply consolidated versions with dates, and make clear which amendments each incorporates |
| C | The full history: original, each amending act, each consolidated version | Change in an architecture can be traced step by step. Multiplies the units to be coded | Most demanding: every version retrievable as a distinct, dated object, with amendment links as data |

Related choices: whether **repealed and expired acts** are in the universe (required for a flow universe under U2; excluded by definition from a stock universe), and how **corrigenda** are treated.

**Needed now.** Which of A, B or C the source must be able to support. This sets the versioning requirement, which is the hardest requirement to meet and the one most likely to separate candidate sources.
**Can wait.** For each sampled act, which version is actually coded.
**Question for discussion.** Is the object of study the architecture *as enacted* or the architecture *as in force*? If both matter, the source must support the full history.

---

## How the parameters interact

- **U2 and U6 are one decision seen from two sides.** A stock universe implies consolidated versions and excludes repealed acts; a flow universe implies original texts and includes them.
- **U1 option B needs links between acts.** Following delegation from a basic act to the acts adopted under it depends on the source recording that relation.
- **U3 option B makes a classification scheme part of the source requirement**, which U3 option A avoids.
- **U4 options B and C almost certainly require more than one source**, whatever is chosen for Union-level law.
- **Width is cheap for the source decision and expensive for coding.** A wide envelope commits us only to testing sources against it. It does not commit the project to coding everything inside it.

## What the workstream needs from the discussion

A position, however provisional, on five points:

1. Are delegated and implementing acts inside the envelope? Is soft law? (U1)
2. What is the earliest date, and is the universe a flow or a stock? (U2)
3. Must national implementing measures come from the same infrastructure? (U4)
4. Which language or languages? (U5)
5. Original texts, texts in force, or full version history? (U6)

U3 can be left as "all domains" for the envelope unless there is a reason to restrict it.

Whatever is agreed will be recorded with its date as a provisional envelope, before any source is assessed. If the final universe later falls outside it, the coverage assessment is repeated and the change is documented.

## Notes for the workstream

- **Numbering.** These six parameters follow the list set for this brief. They differ from the provisional U1–U6 in `SOURCE_SELECTION_FRAMEWORK_v0_1.md`, which had no parameter for territory and normative levels, split languages from legal status differently, and counted intended reuse as U6. The framework needs realigning in its next version; it was not edited here.

| This brief | Framework v0.1 |
|---|---|
| U1 Types of acts | U1 |
| U2 Temporal coverage | U2 |
| U3 Material scope | U5 |
| U4 Territory and normative levels | — (absent) |
| U5 Languages and document versions | U3 |
| U6 Legal status and change | U4 |
| — (kept as a separate parameter, "intended reuse") | U6 |

- **Intended reuse** (internal analysis, redistribution of texts, public deposit of derived data) still has to be stated before sources are assessed, because the reuse requirement is tested against it. It is a project decision, not a question about the legal universe, and is left out of this brief.
- **Terminology.** "The framework" is the conceptual framework of the manuscript. The project's procedures for applying it are an operationalisation of that framework. Nothing in this note alters them.
