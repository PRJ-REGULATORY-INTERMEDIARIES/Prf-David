from rgam_lib import *

# CIT1 names the legal basis of the act: external reference (formal provision, GAP-01)
st("st.CIT1", "CIT1", "external_referencing",
   "The act is adopted having regard to the Treaty on the Functioning of the European Union, in particular Article 192(1) (legal basis).",
   "Having regard to the Treaty on the Functioning of the European Union, and in particular Article 192(1) thereof,")
ext("ext.TFEU192", "st.CIT1", "CIT1", "Treaty on the Functioning of the European Union, Article 192(1) (legal basis of the Regulation)", "legal_instrument",
    "other (legal basis cited in the enacting formula; the reference shows legal relevance only)", dependents="", dep_kind="qualifies", constitutive="N",
    effect="Cited as legal basis; no relation or position of W depends on its content for constitution; not retrieved.")

SCREEN = {}
def S(u, rel, tag, note):
    SCREEN[u] = (rel, tag, note)

S("TITLE", "No", "final/formal", "Title and type of the act (object stated in the title: establishing a carbon border adjustment mechanism); used for the W declaration only; no governance statement derived.")
S("PREAMBLE_ADDRESS", "No", "final/formal", "Identification of the enacting authority; no governance statement.")
S("CIT2", "No", "final/formal", "Formal citation of the Commission proposal; procedural record of enactment; no rule relied on by any statement.")
S("CIT3", "No", "final/formal", "Formal citation of transmission to national parliaments; procedural record of enactment.")
S("CIT4", "No", "final/formal", "Formal citation of an advisory opinion; procedural record of enactment; the referenced opinion is a procedural document, not a source of a rule relied on by any statement.")
S("CIT5", "No", "final/formal", "Formal citation of an advisory opinion; procedural record of enactment; the referenced opinion is a procedural document, not a source of a rule relied on by any statement.")
S("CIT6", "No", "final/formal", "Formal citation of the ordinary legislative procedure; procedural record of enactment.")
S("WHEREAS", "No", "final/formal", "Introductory formula to the recitals; no governance statement.")
S("ENACT", "No", "final/formal", "Adoption formula; no governance statement.")
S("FINAL.SIG1", "No", "final/formal", "Signatory block (Parliament); no governance statement.")
S("FINAL.SIG2", "No", "final/formal", "Signatory block (Council); no governance statement.")

for ch, name in [("CHI", "Chapter I heading"), ("CHII", "Chapter II heading"), ("CHIII", "Chapter III heading"), ("CHIV", "Chapter IV heading"), ("CHV", "Chapter V heading"),
                 ("CHVI", "Chapter VI heading"), ("CHVII", "Chapter VII heading"), ("CHVIII", "Chapter VIII heading"), ("CHIX", "Chapter IX heading"),
                 ("CHX", "Chapter X heading"), ("CHXI", "Chapter XI heading")]:
    S(ch, "No", "heading", name + ": editorial structure; headings are never evidence of architectural membership and no statement is derived.")

REC = {
1: "context: Green Deal and zero-pollution strategy; no record created (recital)",
2: "context: Paris Agreement and Glasgow Climate Pact; external instruments mentioned only in a recital, no EXT created (DR-07)",
3: "context: Green Deal and climate objectives",
4: "context: Union 2030 reduction commitment",
5: "context: European Climate Law mentioned only in a recital; no EXT created from a recital alone",
6: "context: scientific basis (IPCC reports)",
7: "context: existing Union climate legislation (EU ETS and related regulations); no record created",
8: "context: rationale concerning emissions embedded in imports",
9: "context: description of carbon leakage; interpretive aid for Article 1",
10: "context: CBAM as part of the Fit for 55 package",
11: "context: existing carbon-leakage mechanisms (free allocation); interpretive aid for Article 1(3)",
12: "context: CBAM replaces existing mechanisms; phasing-in rationale; no record created",
13: "context: rationale for pathway to extend scope; no record created",
14: "context: incentive effect on third-country producers",
15: "context: equivalence of carbon cost and compatibility with WTO law",
16: "context: rationale for the exclusion of linked systems; cited only as interpretive aid for Article 2(4) and 2(6); no record created",
17: "context: outermost regions and island States to be considered in a future revision",
18: "context: offshore structures; recital refers to Commission implementing powers but the operative assignment is in A2.P2 second subparagraph; no record created from the recital",
19: "context: scope of gases and rationale for indirect emissions and Annex II; interpretive aid for Articles 3 and 7",
20: "context: shared objective of the EU ETS and the CBAM",
21: "context: differences between the EU ETS and the CBAM",
22: "context: specific features of the CBAM certificate system; interpretive aid for Articles 20-24",
23: "context: rationale for weekly averaged certificate prices; interpretive aid for Article 21",
24: "context: rationale for limits on trading and carry-forward and for repurchase; interpretive aid for Articles 23 and 24",
25: "context: rationale for a declarative system and timing; interpretive aid for Articles 6 and 22",
26: "context: rationale for penalties; interpretive aid for Article 26",
27: "context: identification of goods by CN codes; Regulation (EEC) No 2658/87 named only in a recital; EXT is created from Annex I, not from the recital",
28: "context: goods reflect EU ETS activities",
29: "context: non-discrimination rationale for the scope",
30: "context: selection of sectors; external delegated decision named only in a recital",
31: "context: criteria for selecting goods",
32: "context: sectors identified by cumulated emissions",
33: "context: sectors not addressed at this stage",
34: "context: organic chemicals excluded; technical rationale",
35: "context: refinery products excluded; technical rationale",
36: "context: aluminium products included; rationale",
37: "context: hydrogen included; rationale",
38: "context: certain downstream products included to avoid circumvention; rationale",
39: "context: products with low emissions not initially covered; rationale",
40: "context: electricity included in scope; rationale",
41: "context: de minimis rationale; interpretive aid for Article 2(3)",
42: "context: rationale for prior authorisation of importers; interpretive aid for Articles 4, 5 and 17",
43: "context: role of customs authorities; operative assignments are in Articles 25 and 33; no record created from the recital",
44: "context: transitional-period information role of customs authorities; operative assignment is in Article 33(1)",
45: "context: declarative system; first declaration timing; interpretive aid for Article 6",
46: "context: carbon price reduction; interpretive aid for Article 9",
47: "context: verification by accredited verifiers; external Regulations named only in a recital; EXT created from Articles 18 and 8, not from the recital",
48: "context: registration of operators and opt-out from public access; interpretive aid for Articles 10 and 14",
49: "context: weekly price and Commission's calculation and publication task; operative assignments are in Article 21",
50: "context: validity of certificates, resale and quarterly accumulation; interpretive aid for Articles 22-24",
51: "context: electricity specificities; interpretive aid for Article 7(3) and Annex IV",
52: "context: strict conditions for actual electricity emissions; interpretive aid for Annex IV point 5",
53: "context: Commission action on circumvention; operative assignments are in Article 27",
54: "context: Energy Community and Association Agreement parties' decarbonisation commitments",
55: "context: integration of third-country electricity markets and market coupling",
56: "context: rationale for the electricity exemption until 2030 and its withdrawal; interpretive aid for Article 2(7)-(9)",
57: "context: transitional period rationale and last report timing; interpretive aid for Articles 32-35",
58: "context: Commission support to competent authorities; operative assignment is in Article 12",
59: "context: Commission management of the CBAM registry; operative assignment is in Articles 14-16",
60: "context: common central platform and Commission facilitation of information exchange; operative assignments are in Articles 19 and 20",
61: "context: Commission risk-based controls and review of declarations; operative assignments are in Articles 15 and 19",
62: "context: states that the Commission's preliminary calculation is indicative and that no right of appeal or other remedial measure should be possible against it; cited only as an evidence note for Article 19(4); no record created from the recital",
63: "context: Member State reviews and sharing of conclusions via the registry; interpretive aid for Article 19",
64: "context: Member States responsible for establishing and collecting revenues",
65: "context: Commission evaluation and reporting; interpretive aid for Article 30",
66: "context: monitoring of circumvention practices; interpretive aid for Article 27",
67: "context: aim of extending the scope by 2030; interpretive aid for Article 30",
68: "context: Commission biennial reports; interpretive aid for Article 30",
69: "context: exceptional events in third countries; interpretive aid for Article 30(7)",
70: "context: dialogue with third countries",
71: "context: Commission engagement with third countries and technical assistance",
72: "context: Climate Club; no operative provision in W creates it",
73: "context: Union financial support to least developed countries",
74: "context: Union support and own resource; no operative provision in W creates it",
75: "context: data-protection regulations named only in a recital; no EXT created from a recital alone",
76: "context: Regulation (EC) No 515/97 named in a recital; the operative reference is in A25.P5 where the EXT is recorded",
77: "context: delegated powers listing; operative assignments are in Articles 2(10), 2(11), 18(3), 20(6), 27(6) and 28",
78: "context: consultation on delegated acts",
79: "context: implementing powers and Regulation (EU) No 182/2011; operative provisions are in Article 29",
80: "context: protection of financial interests",
81: "context: subsidiarity and proportionality",
82: "context: entry into force rationale; operative provision is Article 36",
}
for n, note in REC.items():
    S("REC%d" % n, "No", "recital-context-only", "Recital (RGAM-DR-07): interpretive context only; " + note + ".")

S("ANX3.pt1", "No", "heading", "Annex III point 1 heading; headings are never evidence; the list content is screened in the following units.")
S("ANX3.pt2", "No", "heading", "Annex III point 2 heading; headings are never evidence; its content is the placeholder unit that follows.")
S("ANX4.pt1", "No", "heading", "Annex IV point 1 heading ('Definitions'); editorial structure.")
S("ANX4.pt2", "No", "heading", "Annex IV point 2 heading; editorial structure.")
S("ANX4.pt3", "No", "heading", "Annex IV point 3 heading; editorial structure.")
S("ANX4.pt4", "No", "heading", "Annex IV point 4 heading; editorial structure.")
S("ANX4.pt4.1", "No", "heading", "Annex IV point 4.1 heading; editorial structure.")
S("ANX4.pt4.2", "No", "heading", "Annex IV point 4.2 heading; editorial structure.")
S("ANX4.pt4.2.1", "No", "heading", "Annex IV point 4.2.1 heading; editorial structure.")
S("ANX4.pt4.2.2", "No", "heading", "Annex IV point 4.2.2 heading; editorial structure.")
S("ANX4.pt4.3", "No", "heading", "Annex IV point 4.3 heading; editorial structure.")
S("ANX4.pt5", "No", "heading", "Annex IV point 5 heading; editorial structure.")
S("ANX4.pt6", "No", "heading", "Annex IV point 6 heading; editorial structure.")
S("ANX4.pt7", "No", "heading", "Annex IV point 7 heading; editorial structure.")
S("ANX5.pt2", "No", "heading", "Annex V point 2 heading; editorial structure; the content of the point is screened in the following units.")
S("ANX6.pt1", "No", "heading", "Annex VI point 1 heading ('Principles of verification'); editorial structure.")
S("ANX6.pt2", "No", "heading", "Annex VI point 2 heading ('Content of a verification report'); editorial structure.")
for u in ["ANX4.pt2.P2", "ANX4.pt2.P5", "ANX4.pt3.P2", "ANX4.pt3.P4"]:
    S(u, "No", "substantive-rule-without-governance-structure", "Formula image (alt text 'Formula') in the Annex IV calculation method; the equation content is not representable in the source text; it assigns no duty or relation and is declared in the W exclusions and uncertainty log.")
