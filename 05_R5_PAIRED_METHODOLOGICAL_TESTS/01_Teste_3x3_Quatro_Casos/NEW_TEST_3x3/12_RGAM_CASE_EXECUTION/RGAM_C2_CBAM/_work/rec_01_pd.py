from rgam_lib import *

JUR = "European Union (Member States and Union institutions as referred to in W)"

# ---------------- POSITIONS: Union institutions (INSTANCE, named in the text) ----------------
pd("pd.COM", "POSITION", "the Commission (European Commission)", "INSTANCE", "A12.P0;A14.P1",
   "the Commission shall assist the competent authorities in carrying out their functions and duties under this Regulation",
   st="st.A12;st.A14P1", inst_src="A12.P0;A14.P1", mult="exactly_one", estab="NONE", constit="not_applicable",
   epi="documented")
pd("pd.EP", "POSITION", "the European Parliament", "INSTANCE", "A28.P3",
   "may be revoked at any time by the European Parliament or by the Council", st="st.A28P3",
   inst_src="A28.P3", mult="exactly_one", estab="NONE", constit="not_applicable", epi="documented")
pd("pd.COUNCIL", "POSITION", "the Council (of the European Union)", "INSTANCE", "A28.P3",
   "may be revoked at any time by the European Parliament or by the Council", st="st.A28P3",
   inst_src="A28.P3", mult="exactly_one", estab="NONE", constit="not_applicable", epi="documented")
pd("pd.UNION", "POSITION", "the Union (as party capable of concluding agreements with third countries)", "INSTANCE", "A2.P12",
   "The Union may conclude agreements with third countries or territories", st="st.A2P12",
   inst_src="A2.P12", mult="exactly_one", estab="NONE", constit="not_applicable", epi="documented")
pd("pd.EPPO", "POSITION", "the European Public Prosecutor's Office", "INSTANCE", "A13.P2",
   "the authorities in charge of administrative or criminal penalties, and the European Public Prosecutor’s Office",
   st="st.A13P2", inst_src="A13.P2", mult="exactly_one", estab="NONE", constit="not_applicable", epi="documented")
pd("pd.CBAMCOM", "POSITION", "the CBAM Committee", "INSTANCE", "A29.P1",
   "The Commission shall be assisted by the CBAM Committee", st="st.A29P1", inst_src="A29.P1", mult="exactly_one",
   estab="AMBIGUOUS", constit="not_applicable", epi="documented", hq="hq.NORMTYPE_BUNDLE", unc="unc.NT_COMMITTEE")

# ---------------- POSITIONS: type-level ----------------
pd("pd.MS", "POSITION", "Member State", "TYPE", "A11.P1", "Each Member State shall designate the competent authority",
   st="st.A11P1", mult="unspecified", estab="NONE", constit="not_applicable", epi="documented")
pd("pd.CA", "POSITION", "competent authority (designated by each Member State)", "TYPE", "A3.P0.pt13;A11.P1",
   "the authority designated by each Member State in accordance with Article 11", st="st.A3DEF_CA;st.A11P1",
   mult="other (the text refers to 'the competent authority' designated by each Member State; the number of authorities per Member State is not otherwise stated)",
   estab="N2", constit="not_constituted_obligation_only", epi="documented")
pd("pd.CUST", "POSITION", "customs authorities", "TYPE", "A3.P0.pt14",
   "the customs administrations of Member States as defined in Article 5, point (1), of Regulation (EU) No 952/2013",
   st="st.A3DEF_CUST", mult="unspecified", estab="NONE", constit="not_applicable", epi="documented", unc="unc.EXT_POS")
pd("pd.IMP", "POSITION", "importer", "TYPE", "A3.P0.pt15",
   "the person lodging a customs declaration for release for free circulation of goods in its own name and on its own behalf",
   st="st.A3DEF_IMP", mult="unspecified", estab="NONE", constit="not_applicable", epi="documented")
pd("pd.ICR", "POSITION", "indirect customs representative", "TYPE", "A5.P1;A32.P0",
   "Where such an importer appoints an indirect customs representative in accordance with Article 18 of Regulation (EU) No 952/2013",
   st="st.A5P1;st.A32", mult="unspecified", estab="NONE", constit="not_applicable", epi="documented", unc="unc.EXT_POS")
pd("pd.ACD", "POSITION", "authorised CBAM declarant", "TYPE", "A3.P0.pt17;A17.P1",
   "a person authorised by a competent authority in accordance with Article 17",
   st="st.A3DEF_ACD;st.A17P1", mult="unspecified", estab="COMPOUND", constit="conditionally_constituted", epi="documented",
   hq="hq.NORMTYPE_A17", unc="unc.NT_A17")
pd("pd.ELECNOM", "POSITION", "person to whom import capacity for electricity has been allocated through explicit capacity allocation and who nominates it", "TYPE",
   "A5.P4", "the person to whom capacity has been allocated for import and who nominates that capacity for import shall, for the purposes of this Regulation, be regarded as an authorised CBAM declarant",
   st="st.A5P4", mult="unspecified", estab="AMBIGUOUS", constit="not_applicable", epi="documented",
   hq="hq.NORMTYPE_BUNDLE", unc="unc.NT_DEEMING")
pd("pd.OTHERPERSON", "POSITION", "person other than an authorised CBAM declarant (importing or introducing goods)", "TYPE", "A25.P1;A26.P2",
   "any person other than an authorised CBAM declarant", st="st.A25P1;st.A26P2", mult="unspecified", estab="NONE",
   constit="not_applicable", epi="documented")
pd("pd.OPER", "POSITION", "operator (of an installation in a third country)", "TYPE", "A3.P0.pt31;A10.P1",
   "any person who operates or controls an installation in a third country", st="st.A3DEF_OPER;st.A10P1", mult="unspecified",
   estab="NONE", constit="not_applicable", epi="documented")
pd("pd.VERIF", "POSITION", "accredited verifier", "TYPE", "A18.P1;A18.P2",
   "shall be an accredited verifier for the purpose of this Regulation", st="st.A18P1;st.A18P2", mult="unspecified",
   estab="AMBIGUOUS", constit="not_applicable", epi="documented", hq="hq.NORMTYPE_BUNDLE", unc="unc.NT_VERIF")
pd("pd.NAB", "POSITION", "national accreditation body", "TYPE", "A3.P0.pt32;A18.P2",
   "a national accreditation body as appointed by each Member State pursuant to Article 4(1) of Regulation (EC) No 765/2008",
   st="st.A3DEF_NAB;st.A18P2", mult="unspecified", estab="NONE", constit="not_applicable", epi="documented",
   unc="unc.EXT_POS")
pd("pd.3C", "POSITION", "third country or territory", "TYPE", "A3.P0.pt7;A2.P8",
   "a country or territory outside the customs territory of the Union", st="st.A3DEF_3C;st.A2P8", mult="unspecified",
   estab="NONE", constit="not_applicable", epi="documented")
pd("pd.INDEP", "POSITION", "independent person certifying carbon-price documentation", "TYPE", "A9.P2",
   "certified by a person that is independent from the authorised CBAM declarant and from the authorities of the country of origin",
   st="st.A9P2", mult="unspecified", estab="NONE", constit="not_applicable", epi="documented")
pd("pd.PENAUTH", "POSITION", "authorities in charge of administrative or criminal penalties", "TYPE", "A13.P2",
   "the authorities in charge of administrative or criminal penalties", st="st.A13P2", mult="unspecified", estab="NONE",
   constit="not_applicable", epi="documented")
pd("pd.PUBLIC", "POSITION", "the public (recipient category of publicly accessible registry information)", "TYPE", "A14.P4",
   "An operator may choose not to have its name, address and contact information made accessible to the public",
   st="st.A14P4", mult="unspecified", estab="NONE", constit="not_applicable", epi="documented")
pd("pd.AFFECTED", "POSITION", "party affected by, or benefiting from, a circumvention practice", "TYPE", "A27.P4",
   "any party that has been affected by, or has benefited from, any of the situations referred to in paragraph 2",
   st="st.A27P4", mult="unspecified", estab="NONE", constit="not_applicable", epi="documented")
pd("pd.INTERESTED", "POSITION", "interested party other than directly affected or benefiting parties (e.g. environmental organisations, NGOs)", "TYPE", "A27.P4",
   "Interested parties other than directly affected or benefited parties, such as environmental organisations and non-governmental organisations",
   st="st.A27P4", mult="unspecified", estab="NONE", constit="not_applicable", epi="documented")
pd("pd.MSEXPERTS", "POSITION", "experts designated by each Member State (consulted on delegated acts)", "TYPE", "A28.P5",
   "consult experts designated by each Member State", st="st.A28P5", mult="unspecified", estab="NONE", constit="not_applicable",
   epi="documented")

# ---------------- DEVICES ----------------
pd("pd.REGISTRY", "DEVICE", "the CBAM registry", "TYPE", "A14.P1;A14.P2;A14.P3;A14.P4",
   "The Commission shall establish a CBAM registry of authorised CBAM declarants in the form of a standardised electronic database",
   st="st.A14P1;st.A14P2", mult="exactly_one", estab="N2",
   dev_id="Singled out by name: 'the CBAM registry' (a CBAM registry of authorised CBAM declarants in the form of a standardised electronic database; separate section for third-country operators and installations, A14(3))",
   dev_fn="Operator: the Commission (A14(1), A14(6)); governing rules: contents of accounts (A14(2)), confidentiality and public access (A14(4)), controls (A15), account rules (A16); bounded function: registering declarants, operators and installations and the certificates of each declarant",
   dev_class="DEV", constit="not_constituted_obligation_only", epi="documented", unc="unc.DEV_REGISTRY")
pd("pd.PLATFORM", "DEVICE", "the common central platform for the sale and repurchase of CBAM certificates", "TYPE", "A20.P1;A20.P2;A20.P3",
   "The Commission shall establish and manage the common central platform following a joint procurement procedure between the Commission and the Member States",
   st="st.A20P1;st.A20P2", mult="exactly_one", estab="N2",
   dev_id="Singled out by name: 'the common central platform' (A20(1)-(3))",
   dev_fn="Operator: the Commission, which establishes and manages it (A20(2)); bounded function: sale (A20(1)), repurchase (A23(1) second subparagraph) and transfer of transaction information to the CBAM registry (A20(3)); access for the Commission and competent authorities (A20(2) second subparagraph)",
   dev_class="DEV", constit="not_constituted_obligation_only", epi="documented", unc="unc.DEV_PLATFORM")

pd("pd.APPL", "POSITION", "applicant for the status of authorised CBAM declarant (importer or indirect customs representative)", "TYPE", "A5.P1;A5.P2",
   "the indirect customs representative shall submit the application for an authorisation", st="st.A5P1;st.A5P2",
   mult="unspecified", estab="NONE", constit="not_applicable", epi="documented")
