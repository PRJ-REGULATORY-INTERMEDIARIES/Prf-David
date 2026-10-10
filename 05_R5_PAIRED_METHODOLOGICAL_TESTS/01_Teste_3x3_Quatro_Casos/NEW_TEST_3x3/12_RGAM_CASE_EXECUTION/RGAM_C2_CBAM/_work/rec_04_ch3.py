from rgam_lib import *

# =============== ARTICLE 11 ===============
st("st.A11P1", "A11.P1", "position_defining",
   "Each Member State shall designate the competent authority to carry out the functions and duties under this Regulation and inform the Commission thereof.",
   "Each Member State shall designate the competent authority to carry out the functions and duties under this Regulation and inform the Commission thereof.")
st("st.A11P1S2", "A11.P1.sub2", "relation_bearing",
   "The Commission shall make available to the Member States a list of all competent authorities, publish it in the Official Journal and make it available in the CBAM registry.",
   "The Commission shall make available to the Member States a list of all competent authorities and publish that information in the Official Journal of the European Union and make that information available in the CBAM registry.")
st("st.A11P2", "A11.P2", "relation_bearing",
   "Competent authorities shall exchange any information that is essential or relevant to the exercise of their functions and duties under this Regulation.",
   "Competent authorities shall exchange any information that is essential or relevant to the exercise of their functions and duties under this Regulation.")
qr("qr.A11_DESIG", "st.A11P1", "A11.P1", "pd.MS", "pd.CA", "delegation_authorization", "Member State -> competent authority (to be designated)",
   "designate the competent authority to carry out the functions and duties under this Regulation", "assignment of functions and duties under the Regulation to a competent authority",
   "authorization_designation*", "obligation",
   "Each Member State shall designate the competent authority to carry out the functions and duties under this Regulation",
   tnote="residual function tag; N2 wording: the obligation to designate is constituted, the competent authority as an entity is not; the counterpart is a type-level position",
   mech="designation", instr="", cond="", epi="documented",
   authattr="Member State designates; the Regulation assigns the functions", discattr="choice of the authority left to each Member State (Article 11)",
   deps="pd.MS;pd.CA", gap="No designation of any competent authority is evidenced in W; the relation is a mandated expectation.",
   unc="unc.N2_DESIG")
qr("qr.A11_INFORM", "st.A11P1", "A11.P1", "pd.MS", "pd.COM", "information_reporting", "Member State -> Commission",
   "inform the Commission of the designation of its competent authority", "designation of the competent authority", "information_provision", "obligation",
   "Each Member State shall designate the competent authority to carry out the functions and duties under this Regulation and inform the Commission thereof.",
   mech="notification", cond="after designation", acls="INFO", asuff="sufficient", authattr="binding duty on each Member State", discattr="none stated",
   deps="pd.MS;pd.COM")
qr("qr.A11_LIST", "st.A11P1S2", "A11.P1.sub2", "pd.COM", "pd.MS", "information_reporting", "Commission -> Member States",
   "make available to the Member States a list of all competent authorities", "list of competent authorities", "information_provision", "obligation",
   "The Commission shall make available to the Member States a list of all competent authorities",
   mech="list", instr="INS-TYPE: list of competent authorities", cond="", acls="INFO", asuff="sufficient",
   authattr="binding duty on the Commission", discattr="none stated", deps="pd.COM;pd.MS")
na("na.A11_PUBLISH", "st.A11P1S2", "A11.P1.sub2", "pd.COM", "publish the list of competent authorities in the Official Journal of the European Union and make it available in the CBAM registry",
   "list of competent authorities", "information_provision", "obligation",
   "publish that information in the Official Journal of the European Union and make that information available in the CBAM registry",
   mech="publication", instr="pd.REGISTRY", nt="N0", eff="duty of the Commission to publish and make available the list",
   notc="no recipient named for the publication; no counterparty created", deriv="direct", deps="pd.COM;pd.REGISTRY")
qr("qr.A11_EXCHANGE", "st.A11P2", "A11.P2", "pd.CA", "pd.CA", "information_reporting", "competent authority -> other competent authorities",
   "exchange any information that is essential or relevant to the exercise of their functions and duties under this Regulation", "information relevant to functions and duties under the Regulation",
   "cooperation_coordination*", "obligation",
   "Competent authorities shall exchange any information that is essential or relevant to the exercise of their functions and duties under this Regulation.",
   tnote="origin and counterpart are the same position type (competent authorities of different Member States exchanging with one another); residual function tag",
   mech="information exchange", cond="", acls="INFO", asuff="sufficient", authattr="mutual duty of competent authorities", discattr="relevance and essentiality judged by the authorities",
   deps="pd.CA", gap="No competent authority is evidenced in W (N2 designation).")

# =============== ARTICLE 12 ===============
st("st.A12", "A12.P0", "relation_bearing",
   "In addition to its other tasks, the Commission shall assist the competent authorities in carrying out their functions and duties and coordinate their activities by supporting the exchange of, and issuing guidelines on, best practices, and by promoting exchange of information and cooperation between competent authorities and with the Commission.",
   "the Commission shall assist the competent authorities in carrying out their functions and duties under this Regulation and shall coordinate their activities")
qr("qr.A12_ASSIST", "st.A12", "A12.P0", "pd.COM", "pd.CA", "authority_control", "Commission -> competent authorities",
   "assist the competent authorities and coordinate their activities by supporting the exchange of best practices, issuing guidelines and promoting information exchange and cooperation",
   "functions and duties of the competent authorities under the Regulation", "cooperation_coordination*", "obligation",
   "the Commission shall assist the competent authorities in carrying out their functions and duties under this Regulation and shall coordinate their activities",
   tnote="nearest of the ten types: authority_control used for coordination; the provision states assistance, guidelines and promotion, not a binding directive power; residual function tag",
   mech="guidelines; support for best-practice exchange; promotion of information exchange", instr="INS-TYPE: guidelines",
   authattr="coordinating role of the Commission; no binding directive power stated", discattr="content and form of guidelines not specified",
   deps="pd.COM;pd.CA", unc="unc.A12_TYPE", gap="No competent authority is evidenced in W (N2 designation).")

# =============== ARTICLE 13 ===============
st("st.A13P1", "A13.P1", "assignment_bearing",
   "Information acquired by the competent authority or the Commission that is confidential by nature or provided on a confidential basis is covered by professional secrecy and shall not be disclosed without the express prior permission of the person or authority that provided it or by virtue of Union or national law.",
   "Such information shall not be disclosed by the competent authority or the Commission without the express prior permission of the person or authority that provided it or by virtue of Union or national law.")
st("st.A13P2", "A13.P2", "relation_bearing",
   "By derogation, the competent authorities and the Commission may share confidential information with each other, the customs authorities, the authorities in charge of administrative or criminal penalties and the European Public Prosecutor's Office for compliance and application of customs legislation; shared information remains under professional secrecy.",
   "the competent authorities and the Commission may share such information with each other, the customs authorities, the authorities in charge of administrative or criminal penalties, and the European Public Prosecutor’s Office")
na("na.A13_SECRECY_CA", "st.A13P1", "A13.P1", "pd.CA", "disclose information that is confidential by nature or provided on a confidential basis, acquired in the course of performing duties",
   "confidential information", "information_provision", "prohibition",
   "Such information shall not be disclosed by the competent authority or the Commission without the express prior permission of the person or authority that provided it or by virtue of Union or national law.",
   mech="professional secrecy", cond="express prior permission of the provider or disclosure by virtue of Union or national law lifts the prohibition",
   cp="the person or authority that provided the information (permission-giver)", cps="IN_PROVISION", nt="N0",
   eff="constraint on competent authorities: obligation of professional secrecy", notc="not a relation; the permission-giver is identified as the source of the lifting condition",
   constraint="Y", deriv="direct", deps="pd.CA")
na("na.A13_SECRECY_COM", "st.A13P1", "A13.P1", "pd.COM", "disclose information that is confidential by nature or provided on a confidential basis, acquired in the course of performing duties",
   "confidential information", "information_provision", "prohibition",
   "Such information shall not be disclosed by the competent authority or the Commission without the express prior permission of the person or authority that provided it or by virtue of Union or national law.",
   mech="professional secrecy", cond="express prior permission of the provider or disclosure by virtue of Union or national law lifts the prohibition",
   cp="the person or authority that provided the information (permission-giver)", cps="IN_PROVISION", nt="N0",
   eff="constraint on the Commission: obligation of professional secrecy", notc="not a relation; the permission-giver is identified as the source of the lifting condition",
   constraint="Y", deriv="direct", deps="pd.COM")
qr("qr.A13_SHARE_CA", "st.A13P2", "A13.P2", "pd.CA", "pd.COM", "information_reporting", "competent authorities -> Commission, customs authorities, penalty authorities, EPPO",
   "share confidential information with the Commission, the customs authorities, the authorities in charge of administrative or criminal penalties and the European Public Prosecutor's Office for the purposes of ensuring compliance with obligations under the Regulation and the application of customs legislation",
   "confidential information", "cooperation_coordination*", "permission",
   "the competent authorities and the Commission may share such information with each other, the customs authorities, the authorities in charge of administrative or criminal penalties, and the European Public Prosecutor’s Office, for the purposes of ensuring compliance of persons with their obligations under this Regulation and the application of customs legislation",
   extra="pd.CUST;pd.PENAUTH;pd.EPPO", tnote="n-ary: the competent authority may share with the Commission, the customs authorities, penalty authorities and the EPPO; residual function tag",
   mech="derogation from professional secrecy", cond="purposes of ensuring compliance of persons with their obligations and the application of customs legislation; shared information remains under professional secrecy",
   acls="INFO", asuff="sufficient", authattr="permissive competence", discattr="discretionary ('may')", deps="pd.CA;pd.COM;pd.CUST;pd.PENAUTH;pd.EPPO")
qr("qr.A13_SHARE_COM", "st.A13P2", "A13.P2", "pd.COM", "pd.CA", "information_reporting", "Commission -> competent authorities, customs authorities, penalty authorities, EPPO",
   "share confidential information with the competent authorities, the customs authorities, the authorities in charge of administrative or criminal penalties and the European Public Prosecutor's Office for the purposes of ensuring compliance and the application of customs legislation",
   "confidential information", "cooperation_coordination*", "permission",
   "the competent authorities and the Commission may share such information with each other, the customs authorities, the authorities in charge of administrative or criminal penalties, and the European Public Prosecutor’s Office, for the purposes of ensuring compliance of persons with their obligations under this Regulation and the application of customs legislation",
   extra="pd.CUST;pd.PENAUTH;pd.EPPO", tnote="n-ary: the Commission may share with the competent authorities, the customs authorities, penalty authorities and the EPPO; residual function tag",
   mech="derogation from professional secrecy", cond="purposes of ensuring compliance of persons with their obligations and the application of customs legislation; shared information remains under professional secrecy",
   acls="INFO", asuff="sufficient", authattr="permissive competence", discattr="discretionary ('may')", deps="pd.COM;pd.CA;pd.CUST;pd.PENAUTH;pd.EPPO")

# =============== ARTICLE 14 ===============
st("st.A14P1", "A14.P1", "device_defining",
   "The Commission shall establish a CBAM registry of authorised CBAM declarants as a standardised electronic database containing data regarding the CBAM certificates of those declarants, and shall make the information in it available automatically and in real time to customs authorities and competent authorities.",
   "The Commission shall establish a CBAM registry of authorised CBAM declarants in the form of a standardised electronic database containing the data regarding the CBAM certificates of those authorised CBAM declarants.")
st("st.A14P2", "A14.P2;A14.P2.pta;A14.P2.ptb;A14.P2.ptc;A14.P2.ptd;A14.P3", "device_defining",
   "The registry shall contain accounts with information about each authorised CBAM declarant (name and contact, EORI number, CBAM account number, identification number, sale price, date of sale and date of surrender, repurchase or cancellation of certificates) and, in a separate section, information on registered operators and installations in third countries.",
   "The CBAM registry referred to in paragraph 1 shall contain accounts with information about each authorised CBAM declarant")
st("st.A14P4", "A14.P4", "relation_bearing",
   "Information in the CBAM registry is confidential, except names, addresses and contact information of operators and the location of installations in third countries; an operator may choose not to have its name, address and contact information made accessible to the public; the public information is made accessible by the Commission in an interoperable format.",
   "The public information in the CBAM registry shall be made accessible by the Commission in an interoperable format.")
st("st.A14P5", "A14.P5", "assignment_bearing",
   "The Commission shall publish yearly, for each Annex I good, the aggregated emissions embedded in the imported goods.",
   "The Commission shall publish, on a yearly basis, for each of the goods listed in Annex I, the aggregated emissions embedded in the imported goods.")
st("st.A14P6", "A14.P6", "assignment_bearing",
   "The Commission shall adopt implementing acts concerning the infrastructure and procedures of the CBAM registry, risk analysis (Article 15), databases, account data (Article 16), transmission of information on sale, repurchase and cancellation of certificates (Article 20) and the cross-check of information (Article 25(3)), under the examination procedure of Article 29(2).",
   "The Commission shall adopt implementing acts concerning the infrastructure and specific processes and procedures of the CBAM registry")
na("na.A14_ESTAB", "st.A14P1", "A14.P1", "pd.COM", "establish a CBAM registry of authorised CBAM declarants in the form of a standardised electronic database containing the data regarding the CBAM certificates of those declarants",
   "the CBAM registry", "implementation", "obligation",
   "The Commission shall establish a CBAM registry of authorised CBAM declarants in the form of a standardised electronic database",
   mech="electronic database", instr="pd.REGISTRY", nt="N2", eff="obligation of the Commission to establish the CBAM registry",
   notc="the registry (device) is not itself constituted by this wording (N2); no establishment is evidenced", deriv="direct", deps="pd.COM;pd.REGISTRY",
   epi="documented", unc="unc.DEV_REGISTRY")
qr("qr.A14_ACCESS", "st.A14P1", "A14.P1", "pd.COM", "pd.CUST", "information_reporting", "Commission -> customs authorities and competent authorities",
   "make the information in the CBAM registry available automatically and in real time to customs authorities and competent authorities", "information in the CBAM registry",
   "information_provision", "obligation",
   "The Commission shall make the information in the CBAM registry available automatically and in real time to customs authorities and competent authorities.",
   extra="pd.CA", mech="automatic real-time availability", instr="pd.REGISTRY", cond="", acls="INFO", asuff="sufficient",
   authattr="binding duty on the Commission", discattr="none stated", deps="pd.COM;pd.CUST;pd.CA;pd.REGISTRY", gap="Establishment of the CBAM registry is not evidenced (expectation).")
qr("qr.A14_PUBLIC", "st.A14P4", "A14.P4", "pd.COM", "pd.PUBLIC", "information_reporting", "Commission -> the public",
   "make the public information in the CBAM registry (names, addresses and contact information of operators and the location of installations in third countries, except where an operator has opted out) accessible in an interoperable format",
   "public information in the CBAM registry", "information_provision", "obligation",
   "The public information in the CBAM registry shall be made accessible by the Commission in an interoperable format.",
   tnote="publicity relation; the public is named as recipient category in A14.P4 ('accessible to the public')", mech="public access in interoperable format", instr="pd.REGISTRY",
   cond="the operator has not chosen to withhold its name, address and contact information", acls="INFO", asuff="sufficient",
   authattr="binding duty on the Commission", discattr="operator opt-out narrows what is public", deps="pd.COM;pd.PUBLIC;pd.REGISTRY", gap="Establishment of the CBAM registry is not evidenced (expectation).",
   iunits="A14.P3")
na("na.A14P4_OPTOUT", "st.A14P4", "A14.P4", "pd.OPER", "choose not to have its name, address and contact information made accessible to the public",
   "public accessibility of operator contact data", "information_provision", "permission",
   "An operator may choose not to have its name, address and contact information made accessible to the public.",
   mech="opt-out choice", instr="pd.REGISTRY", nt="N3", eff="permission of the operator to withhold contact data from public access",
   notc="the provision names no addressee of the choice; no counterparty is created", deriv="direct", deps="pd.OPER;pd.REGISTRY")
na("na.A14P5_PUBLISH", "st.A14P5", "A14.P5", "pd.COM", "publish yearly, for each good listed in Annex I, the aggregated emissions embedded in the imported goods",
   "aggregated embedded emissions per Annex I good", "information_provision", "obligation",
   "The Commission shall publish, on a yearly basis, for each of the goods listed in Annex I, the aggregated emissions embedded in the imported goods.",
   mech="publication", nt="N0", eff="duty of the Commission to publish aggregated emissions", notc="no recipient named; no counterparty created", deriv="direct", deps="pd.COM")
na("na.A14P6_IMPL", "st.A14P6", "A14.P6", "pd.COM", "adopt implementing acts on the infrastructure and processes of the CBAM registry, the risk analysis of Article 15, the databases, account data (Article 16), transmission of information on sale, repurchase and cancellation of certificates (Article 20) and the cross-check of Article 25(3)",
   "implementing acts on the CBAM registry", "rule_making_standard_setting", "obligation",
   "The Commission shall adopt implementing acts concerning the infrastructure and specific processes and procedures of the CBAM registry",
   mech="implementing act under the examination procedure (Article 29(2))", instr="INS-TYPE: implementing act", nt="N0",
   eff="duty of the Commission to adopt implementing acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM")

# =============== ARTICLE 15 ===============
st("st.A15P1", "A15.P1", "assignment_bearing",
   "The Commission shall carry out risk-based controls on the data and transactions recorded in the CBAM registry to ensure there are no irregularities in the purchase, holding, surrender, repurchase and cancellation of CBAM certificates.",
   "The Commission shall carry out risk-based controls on the data and the transactions recorded in the CBAM registry")
st("st.A15P2", "A15.P2", "relation_bearing",
   "If the Commission identifies irregularities it shall inform the competent authorities concerned so that further investigations are carried out to correct them.",
   "it shall inform the competent authorities concerned so that further investigations are carried out in order to correct the identified irregularities")
na("na.A15_CONTROL", "st.A15P1", "A15.P1", "pd.COM", "carry out risk-based controls on the data and transactions recorded in the CBAM registry to ensure there are no irregularities in the purchase, holding, surrender, repurchase and cancellation of CBAM certificates",
   "data and transactions recorded in the CBAM registry", "monitoring", "obligation",
   "The Commission shall carry out risk-based controls on the data and the transactions recorded in the CBAM registry",
   mech="risk-based controls", instr="pd.REGISTRY", nt="N0", eff="duty of the Commission to run risk-based controls",
   notc="the provision names the data and transactions, not the persons whose conduct is controlled; no counterparty is created", deriv="direct", deps="pd.COM;pd.REGISTRY")
qr("qr.A15_INFORM", "st.A15P2", "A15.P2", "pd.COM", "pd.CA", "oversight_supervision", "Commission -> competent authorities concerned",
   "inform the competent authorities concerned of irregularities identified through the controls so that further investigations are carried out to correct them",
   "irregularities in the purchase, holding, surrender, repurchase and cancellation of CBAM certificates", "monitoring", "obligation",
   "it shall inform the competent authorities concerned so that further investigations are carried out in order to correct the identified irregularities",
   tnote="escalation of control findings to the competent authority; the investigating step is the competent authority's, but the provision states no investigation duty in terms",
   mech="information on irregularities", instr="", cond="the Commission identifies irregularities as a result of the controls under Article 15(1)",
   authattr="Commission escalates findings; investigative power of competent authorities is not stated in W", discattr="none stated", acls="INFO", asuff="sufficient",
   deps="pd.COM;pd.CA", gap="No competent authority is evidenced in W (N2 designation).", iunits="A15.P1")

# =============== ARTICLE 16 ===============
st("st.A16P1", "A16.P1;A16.P3", "relation_bearing",
   "The Commission shall assign each authorised CBAM declarant a unique CBAM account number, set up the account as soon as the authorisation of Article 17(1) is granted and notify the declarant.",
   "The Commission shall assign to each authorised CBAM declarant a unique CBAM account number.")
st("st.A16P2", "A16.P2", "relation_bearing",
   "Each authorised CBAM declarant shall be granted access to its account in the CBAM registry.",
   "Each authorised CBAM declarant shall be granted access to its account in the CBAM registry.")
st("st.A16P4", "A16.P4", "relation_bearing",
   "If the authorised CBAM declarant has ceased its economic activity or its authorisation has been revoked, the Commission shall close the account, provided the declarant has complied with all its obligations under the Regulation.",
   "the Commission shall close the account of that authorised CBAM declarant, provided that the authorised CBAM declarant has complied with all its obligations under this Regulation")
qr("qr.A16_ACCOUNT", "st.A16P1", "A16.P1;A16.P3", "pd.COM", "pd.ACD", "delegation_authorization", "Commission -> authorised CBAM declarant",
   "assign a unique CBAM account number, set up the account as soon as the authorisation is granted and notify the authorised CBAM declarant",
   "CBAM account in the CBAM registry", "implementation", "obligation",
   "The Commission shall set up the account as soon as the authorisation referred to in Article 17(1) is granted and shall notify the authorised CBAM declarant thereof.",
   mech="account assignment and notification", instr="pd.REGISTRY", cond="the authorisation referred to in Article 17(1) has been granted",
   authattr="Commission administers accounts; set-up is triggered by the competent authority's grant", discattr="none stated",
   deps="pd.COM;pd.ACD;pd.REGISTRY", gap="Establishment of the CBAM registry is not evidenced (expectation).", iunits="A17.P1")
qr("qr.A16_ACCESS", "st.A16P2", "A16.P2;A16.P1;A14.P1", "pd.COM", "pd.ACD", "delegation_authorization", "Commission -> authorised CBAM declarant",
   "grant each authorised CBAM declarant access to its account in the CBAM registry", "access to the CBAM account", "implementation", "entitlement",
   "Each authorised CBAM declarant shall be granted access to its account in the CBAM registry.",
   mech="registry access", instr="pd.REGISTRY", cond="", deriv="derived",
   drule="A16.P2 is passive and names no grantor; A16.P1 and A16.P3 assign account set-up to the Commission and A14.P1 makes the Commission the establisher of the registry, so the Commission is the obligor of the entitlement (stated as an inference from those provisions).",
   authattr="entitlement of the authorised CBAM declarant", discattr="none stated", deps="pd.COM;pd.ACD;pd.REGISTRY", unc="unc.A16_PASSIVE",
   gap="Establishment of the CBAM registry is not evidenced (expectation).")
qr("qr.A16_CLOSE", "st.A16P4", "A16.P4", "pd.COM", "pd.ACD", "authority_control", "Commission -> authorised CBAM declarant",
   "close the account of the authorised CBAM declarant if it has ceased its economic activity or its authorisation has been revoked, provided it has complied with all its obligations under the Regulation",
   "closure of the CBAM account", "implementation", "obligation",
   "the Commission shall close the account of that authorised CBAM declarant, provided that the authorised CBAM declarant has complied with all its obligations under this Regulation",
   mech="account closure", instr="pd.REGISTRY", cond="ceased economic activity or revoked authorisation; the declarant has complied with all obligations under the Regulation",
   authattr="Commission closes the account subject to the compliance proviso", discattr="none stated", deps="pd.COM;pd.ACD;pd.REGISTRY")

# =============== ARTICLE 17 ===============
st("st.A17P1", "A17.P1;A17.P2;A17.P2.pta;A17.P2.ptb;A17.P2.ptc;A17.P2.ptd", "relation_bearing",
   "Where an application is submitted under Article 5, the competent authority of the Member State where the applicant is established shall grant the status of authorised CBAM declarant provided the four criteria of paragraph 2 are complied with; the status is recognised in all Member States.",
   "the competent authority in the Member State in which the applicant is established shall grant the status of authorised CBAM declarant provided that the criteria set out in paragraph 2 of this Article are complied with")
st("st.A17P1S2", "A17.P1.sub2", "relation_bearing",
   "Before granting the status, the competent authority shall conduct a consultation procedure via the CBAM registry involving the competent authorities in the other Member States and the Commission, not exceeding 15 working days.",
   "Before granting the status of authorised CBAM declarant, the competent authority shall conduct a consultation procedure on the application for an authorisation via the CBAM registry.")
st("st.A17P3", "A17.P3", "relation_bearing",
   "Where the criteria are not fulfilled or the applicant failed to provide the information of Article 5(5), the competent authority refuses the status; the decision gives reasons and information on the possibility to appeal.",
   "Such decision to refuse the status of authorised CBAM declarant shall provide the reasons for the refusal and include information on the possibility to appeal.")
st("st.A17P4", "A17.P4;A17.P4.pta;A17.P4.ptb;A17.P4.ptc;A17.P4.ptd", "assignment_bearing",
   "A decision granting the status shall be registered in the CBAM registry and contain name and contact, EORI number, CBAM account number and the guarantee required.",
   "A decision of the competent authority granting the status of authorised CBAM declarant shall be registered in the CBAM registry")
st("st.A17P5", "A17.P5;A17.P5.sub2", "relation_bearing",
   "The competent authority shall require a guarantee if the applicant was not established throughout the two preceding financial years; its amount is the aggregate value of the certificates the declarant would have to surrender for the imports reported under Article 5(5)(g); it is a bank guarantee payable at first demand by a financial institution operating in the Union or an equivalent guarantee.",
   "the competent authority shall require the provision of a guarantee if the applicant was not established throughout the two financial years preceding the year when the application in accordance with Article 5(1) was submitted")
st("st.A17P6", "A17.P6", "relation_bearing",
   "Where the guarantee does not ensure, or is no longer sufficient to ensure, the financial and operational capacity of the authorised CBAM declarant, the competent authority shall require it to choose between an additional guarantee and replacing the initial guarantee.",
   "it shall require the authorised CBAM declarant to choose between providing an additional guarantee or replacing the initial guarantee with a new guarantee")
st("st.A17P7", "A17.P7", "relation_bearing",
   "The competent authority shall release the guarantee immediately after 31 May of the second year in which the authorised CBAM declarant has surrendered CBAM certificates.",
   "The competent authority shall release the guarantee immediately after 31 May of the second year in which the authorised CBAM declarant has surrendered CBAM certificates in accordance with Article 22.")
st("st.A17P8", "A17.P8;A17.P8.pta;A17.P8.ptb;A17.P8.sub2;A17.P8.sub3", "relation_bearing",
   "The competent authority shall revoke the status where the declarant requests it, no longer meets the criteria or the guarantee conditions, or seriously or repeatedly infringed the surrender or quarterly-sufficiency obligations; before revoking it gives the declarant the possibility to be heard and consults the competent authorities of other Member States and the Commission (not exceeding 15 working days); the decision states reasons and the right to appeal.",
   "The competent authority shall revoke the status of authorised CBAM declarant where:")
st("st.A17P9", "A17.P9;A17.P9.pta;A17.P9.ptb", "assignment_bearing",
   "The competent authority shall register in the CBAM registry information on applicants whose application was refused and on persons whose status was revoked.",
   "The competent authority shall register in the CBAM registry information on:")
st("st.A17P10", "A17.P10;A17.P10.pta;A17.P10.ptb;A17.P10.ptc;A17.P10.ptd;A17.P10.pte;A17.P10.sub2", "assignment_bearing",
   "The Commission shall adopt, by implementing acts under the examination procedure of Article 29(2), the conditions for applying the criteria, the guarantee, the criteria of serious or repeated infringement, the consequences of revocation and the deadlines and format of the consultation procedure.",
   "The Commission shall adopt, by means of implementing acts, the conditions for:")
qr("qr.A17_GRANT", "st.A17P1", "A17.P1;A17.P2;A17.P2.pta;A17.P2.ptb;A17.P2.ptc;A17.P2.ptd;A5.P1", "pd.CA", "pd.APPL", "delegation_authorization", "competent authority -> applicant",
   "grant the status of authorised CBAM declarant on an application submitted under Article 5, provided that four criteria are complied with (no serious or repeated infringements in the five preceding years; financial and operational capacity demonstrated; established in the Member State; EORI number assigned); the status is recognised in all Member States",
   "status of authorised CBAM declarant", "authorization_designation*", "obligation",
   "the competent authority in the Member State in which the applicant is established shall grant the status of authorised CBAM declarant provided that the criteria set out in paragraph 2 of this Article are complied with",
   tnote="residual function tag; wording combines an obligation to grant with conditions (see HQ on norm type); 'recognised in all Member States' is passive and creates no further relation",
   mech="administrative decision on application", instr="INS-TYPE: decision granting status",
   cond="application submitted in accordance with Article 5; applicant established in the Member State of the competent authority; criteria of paragraph 2 complied with",
   authattr="competent authority holds the decisional power; status is recognised in all Member States", discattr="criteria fixed in paragraph 2; the capacity criterion (point (b)) requires an assessment by the competent authority; conditions to be specified by implementing acts (A17(10))",
   deps="pd.CA;pd.APPL", unc="unc.NT_A17", hq="hq.NORMTYPE_A17", gap="No competent authority or applicant instance is evidenced in W.",
   deriv="direct")
qr("qr.A17_CONSULT", "st.A17P1S2", "A17.P1.sub2", "pd.CA", "pd.CA", "representation_participation", "competent authority of the applicant's Member State -> competent authorities of other Member States and Commission",
   "conduct a consultation procedure on the application via the CBAM registry before granting the status, involving the competent authorities in the other Member States and the Commission, not exceeding 15 working days",
   "applications for the status of authorised CBAM declarant", "cooperation_coordination*", "obligation",
   "The consultation procedure shall involve the competent authorities in the other Member States and the Commission and shall not exceed 15 working days.",
   extra="pd.COM", tnote="origin and counterpart are the same position type (competent authorities of different Member States); the Commission is an additional party; residual function tag",
   mech="consultation procedure via the CBAM registry", instr="pd.REGISTRY", cond="before granting the status of authorised CBAM declarant",
   authattr="consultation does not by wording bind the deciding competent authority", discattr="the deciding authority's treatment of consultation responses is not stated",
   deps="pd.CA;pd.COM;pd.REGISTRY", gap="No competent authority is evidenced in W; the registry is an expectation.", unc="unc.CONSULT_EFFECT")
qr("qr.A17_REFUSE", "st.A17P3", "A17.P3", "pd.CA", "pd.APPL", "delegation_authorization", "competent authority -> applicant",
   "refuse the status of authorised CBAM declarant where the criteria are not fulfilled or the applicant has failed to provide the information listed in Article 5(5); the refusal decision provides the reasons and information on the possibility to appeal",
   "refusal of the status of authorised CBAM declarant", "authorization_designation*", "obligation",
   "Such decision to refuse the status of authorised CBAM declarant shall provide the reasons for the refusal and include information on the possibility to appeal.",
   tnote="residual function tag; refusal decision", mech="reasoned refusal decision with information on appeal", instr="INS-TYPE: decision refusing status",
   cond="criteria of Article 17(2) not fulfilled, or the information listed in Article 5(5) not provided",
   authattr="competent authority refuses (binding decision)", discattr="assessment of fulfilment of criteria by the competent authority",
   acls="INFO", asuff="indeterminate", amiss="the provision states reasons and 'information on the possibility to appeal' but identifies no appeal forum, no questioning capacity, no assessment capacity and no consequence; no actor-forum relation is evidenced",
   deps="pd.CA;pd.APPL", unc="unc.APPEAL_FORUM", hq="hq.ACCOUNT_APPEAL", iunits="A17.P1")
na("na.A17_REGDEC", "st.A17P4", "A17.P4;A17.P9", "pd.CA", "register the decision granting the status of authorised CBAM declarant in the CBAM registry, containing name and contact information, EORI number, CBAM account number and the guarantee required",
   "decision granting status", "information_provision", "obligation",
   "A decision of the competent authority granting the status of authorised CBAM declarant shall be registered in the CBAM registry",
   mech="registration in the CBAM registry", instr="pd.REGISTRY", cond="a decision granting the status has been taken", nt="N0",
   eff="duty to register grant decisions", notc="no counterparty named for the registration", deriv="derived",
   drule="A17.P4 is passive ('shall be registered'); the registrant is taken to be the competent authority whose decision it is, which is consistent with A17.P9 and A5.P4 second subparagraph where the competent authority registers in the CBAM registry.",
   deps="pd.CA;pd.REGISTRY", unc="unc.A17P4_PASSIVE")
qr("qr.A17_GUARANTEE", "st.A17P5", "A17.P5;A17.P5.sub2", "pd.CA", "pd.APPL", "authority_control", "competent authority -> applicant",
   "require the provision of a guarantee (bank guarantee payable at first demand by a financial institution operating in the Union, or an equivalent guarantee) in the amount of the aggregate value of the certificates the declarant would have to surrender for the imports reported under Article 5(5)(g)",
   "guarantee supporting the financial and operational capacity criterion", "implementation", "obligation",
   "the competent authority shall require the provision of a guarantee if the applicant was not established throughout the two financial years preceding the year when the application in accordance with Article 5(1) was submitted",
   mech="guarantee requirement", instr="INS-TYPE: guarantee (bank guarantee or equivalent)", cond="the applicant was not established throughout the two financial years preceding the year of the application",
   authattr="competent authority imposes the requirement and fixes the amount", discattr="amount computed by a stated formula; equivalence of 'another form of guarantee' judged by the competent authority",
   deps="pd.CA;pd.APPL")
qr("qr.A17_GUARANTEE2", "st.A17P6", "A17.P6", "pd.CA", "pd.ACD", "authority_control", "competent authority -> authorised CBAM declarant",
   "require the authorised CBAM declarant to choose between providing an additional guarantee or replacing the initial guarantee where the guarantee does not ensure, or is no longer sufficient to ensure, its financial and operational capacity",
   "adequacy of the guarantee", "implementation", "obligation",
   "it shall require the authorised CBAM declarant to choose between providing an additional guarantee or replacing the initial guarantee with a new guarantee in accordance with paragraph 5",
   mech="guarantee adequacy review", instr="INS-TYPE: guarantee", cond="the competent authority establishes that the guarantee does not ensure, or is no longer sufficient to ensure, the declarant's capacity",
   authattr="competent authority requires; declarant chooses between two remedies", discattr="sufficiency finding by the competent authority", deps="pd.CA;pd.ACD")
qr("qr.A17_RELEASE", "st.A17P7", "A17.P7", "pd.CA", "pd.ACD", "beneficiary_protective", "competent authority -> authorised CBAM declarant",
   "release the guarantee immediately after 31 May of the second year in which the authorised CBAM declarant has surrendered CBAM certificates", "release of the guarantee",
   "implementation", "obligation",
   "The competent authority shall release the guarantee immediately after 31 May of the second year in which the authorised CBAM declarant has surrendered CBAM certificates in accordance with Article 22.",
   tnote="nearest type: protective of the declarant's interest in release of security", mech="release", instr="INS-TYPE: guarantee",
   cond="31 May of the second year in which the declarant has surrendered certificates under Article 22", authattr="binding duty on the competent authority", discattr="none stated",
   deps="pd.CA;pd.ACD")
qr("qr.A17_REVOKE", "st.A17P8", "A17.P8;A17.P8.pta;A17.P8.ptb;A17.P8.sub2;A17.P8.sub3", "pd.CA", "pd.ACD", "authority_control", "competent authority -> authorised CBAM declarant",
   "revoke the status where the declarant requests it, no longer meets the criteria of paragraph 2 or the guarantee condition of paragraph 6, or has been involved in a serious or repeated infringement of the surrender obligation (Article 22(1)) or the quarterly sufficiency obligation (Article 22(2)); give the declarant the possibility to be heard; state the reasons and information on the right to appeal",
   "revocation of the status of authorised CBAM declarant", "enforcement", "obligation",
   "The competent authority shall revoke the status of authorised CBAM declarant where:",
   mech="revocation decision after hearing and consultation", instr="INS-TYPE: decision revoking status",
   cond="(a) request by the declarant, or (b) criteria no longer met, or serious or repeated infringement of Article 22(1) or (2); possibility to be heard; consultation procedure; reasons and information about the right to appeal",
   authattr="competent authority revokes (binding decision) once a ground is met", discattr="'serious or repeated' infringement to be specified by implementing acts (A17(10)(c))",
   acls="INFO", asuff="indeterminate", amiss="reasons, a hearing and 'information about the right to appeal' are stated, but no appeal forum, assessment capacity or consequence is identified; no actor-forum relation is evidenced",
   deps="pd.CA;pd.ACD", unc="unc.APPEAL_FORUM;unc.XREF_BUNDLE", hq="hq.ACCOUNT_APPEAL;hq.XREF_BUNDLE")
qr("qr.A17_REVOKE_CONSULT", "st.A17P8", "A17.P8.sub2", "pd.CA", "pd.CA", "representation_participation", "competent authority of the declarant's Member State -> competent authorities of other Member States and Commission",
   "conduct a consultation procedure on the possible revocation, involving the competent authorities in the other Member States and the Commission, not exceeding 15 working days",
   "possible revocation of the status of authorised CBAM declarant", "cooperation_coordination*", "obligation",
   "The consultation procedure shall involve the competent authorities in the other Member States and the Commission and shall not exceed 15 working days.",
   extra="pd.COM", tnote="origin and counterpart are the same position type (competent authorities of different Member States); the Commission is an additional party; residual function tag",
   mech="consultation procedure", cond="before revoking the status", authattr="consultation does not by wording bind the deciding competent authority",
   discattr="the treatment of consultation responses is not stated", deps="pd.CA;pd.COM", unc="unc.CONSULT_EFFECT", gap="No competent authority is evidenced in W.")
na("na.A17_REGISTER_REFUSED", "st.A17P9", "A17.P9;A17.P9.pta;A17.P9.ptb", "pd.CA", "register in the CBAM registry information on applicants whose application has been refused and on persons whose status has been revoked",
   "refusals and revocations", "information_provision", "obligation",
   "The competent authority shall register in the CBAM registry information on:",
   mech="registration in the CBAM registry", instr="pd.REGISTRY", nt="N0", eff="duty of the competent authority to register refusals and revocations",
   notc="no counterparty named for the registration", deriv="direct", deps="pd.CA;pd.REGISTRY")
na("na.A17P10_IMPL", "st.A17P10", "A17.P10;A17.P10.pta;A17.P10.ptb;A17.P10.ptc;A17.P10.ptd;A17.P10.pte;A17.P10.sub2", "pd.COM",
   "adopt, by implementing acts, the conditions for applying the criteria of paragraph 2, the guarantee, the criteria of serious or repeated infringement, the consequences of revocation and the deadlines and format of the consultation procedure",
   "implementing acts on authorisation", "rule_making_standard_setting", "obligation",
   "The Commission shall adopt, by means of implementing acts, the conditions for:",
   mech="implementing act under the examination procedure (Article 29(2))", instr="INS-TYPE: implementing act", nt="N0",
   eff="duty of the Commission to adopt implementing acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM")

# =============== ARTICLE 18 ===============
st("st.A18P1", "A18.P1", "position_defining",
   "Any person accredited in accordance with Implementing Regulation (EU) 2018/2067 for a relevant group of activities shall be an accredited verifier for the purpose of this Regulation; the Commission is empowered to adopt implementing acts identifying relevant groups of activities by aligning qualifications with the groups listed in Annex I to that Regulation.",
   "Any person accredited in accordance with Implementing Regulation (EU) 2018/2067 for a relevant group of activities shall be an accredited verifier for the purpose of this Regulation.")
st("st.A18P2", "A18.P2", "relation_bearing",
   "A national accreditation body may, on request, accredit a person to be a verifier for the purpose of this Regulation where it considers, on the basis of the documentation submitted, that the person has the capacity to apply the Annex VI verification principles when verifying embedded emissions under Articles 8 and 10.",
   "A national accreditation body may, on request, accredit a person to be a verifier for the purpose of this Regulation")
st("st.A18P3", "A18.P3", "assignment_bearing",
   "The Commission is empowered to adopt delegated acts under Article 28 specifying the conditions for granting accreditation, control and oversight of accredited verifiers, withdrawal of accreditation, and mutual recognition and peer evaluation of accreditation bodies.",
   "The Commission is empowered to adopt delegated acts in accordance with Article 28 in order to supplement this Regulation by specifying the conditions for granting of accreditation")
na("na.A18P1_STATUS", "st.A18P1", "A18.P1", "pd.VERIF", "be an accredited verifier for the purpose of the Regulation, where accredited in accordance with Implementing Regulation (EU) 2018/2067 for a relevant group of activities",
   "status of accredited verifier", "authorization_designation*", "declaratory",
   "Any person accredited in accordance with Implementing Regulation (EU) 2018/2067 for a relevant group of activities shall be an accredited verifier for the purpose of this Regulation.",
   mech="recognition of external accreditation for the purposes of the Regulation", instr="INS-TYPE: accreditation under Implementing Regulation (EU) 2018/2067",
   cond="accredited in accordance with Implementing Regulation (EU) 2018/2067 for a relevant group of activities", nt="AMBIGUOUS",
   eff="status of accredited verifier for the purposes of this Regulation, stated by the provision; whether this is N1 direct designation or a definitional extension of an external accreditation is not resolved",
   notc="does not constitute the accreditation itself, which arises under the external Regulation", deriv="direct", deps="pd.VERIF", epi="documented",
   unc="unc.NT_VERIF", hq="hq.NORMTYPE_BUNDLE")
na("na.A18P1_IMPL", "st.A18P1", "A18.P1", "pd.COM", "adopt implementing acts identifying relevant groups of activities by aligning the qualifications of an accredited verifier with the groups of activities listed in Annex I to Implementing Regulation (EU) 2018/2067",
   "implementing acts on groups of activities for verifiers", "rule_making_standard_setting", "competence",
   "The Commission is empowered to adopt implementing acts to identify relevant groups of activities",
   mech="implementing act under the examination procedure (Article 29(2))", instr="INS-TYPE: implementing act", nt="N3",
   eff="competence of the Commission to adopt implementing acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM")
qr("qr.A18_ACCREDIT", "st.A18P2", "A18.P2", "pd.NAB", "pd.VERIF", "delegation_authorization", "national accreditation body -> person accredited as verifier",
   "accredit, on request, a person to be a verifier for the purpose of the Regulation where it considers, on the basis of the documentation submitted, that the person has the capacity to apply the Annex VI verification principles when verifying embedded emissions pursuant to Articles 8 and 10",
   "accreditation of verifiers", "authorization_designation*", "permission",
   "A national accreditation body may, on request, accredit a person to be a verifier for the purpose of this Regulation",
   tnote="residual function tag; the counterpart is the type-level position of accredited verifier (the person requesting accreditation)", mech="accreditation on request", instr="INS-TYPE: accreditation",
   cond="request by a person; documentation submitted; capacity to apply the Annex VI principles considered present",
   authattr="national accreditation body holds the accrediting power ('may')", discattr="discretionary assessment ('where it considers')",
   deps="pd.NAB;pd.VERIF", ext="ext.REG765_NAB", gap="National accreditation bodies are constituted by external appointment (Regulation (EC) No 765/2008); no body or accredited person is evidenced in W.")
na("na.A18P3_DELEG", "st.A18P3", "A18.P3", "pd.COM", "adopt delegated acts specifying the conditions for granting accreditation, the control and oversight of accredited verifiers, withdrawal of accreditation and mutual recognition and peer evaluation of accreditation bodies",
   "delegated acts on accreditation of verifiers", "rule_making_standard_setting", "competence",
   "The Commission is empowered to adopt delegated acts in accordance with Article 28 in order to supplement this Regulation by specifying the conditions for granting of accreditation",
   mech="delegated act (Article 28)", instr="INS-TYPE: delegated act", nt="N3",
   eff="competence of the Commission to adopt delegated acts", notc="does not constitute the content of the acts; 'control and oversight of accredited verifiers' is an object of the acts, no controlling party is named",
   deriv="direct", deps="pd.COM")

# =============== ARTICLE 19 ===============
st("st.A19P1", "A19.P1;A19.P2;A19.P2.sub2", "relation_bearing",
   "The Commission has the oversight role in the review of CBAM declarations; it may review declarations in accordance with a review strategy including risk factors, within the period ending with the fourth year after the year in which they should have been submitted; the review may verify the information in the declaration and in verification reports on the basis of customs information (Article 25), other evidence and any audit deemed necessary, including at the premises of the authorised CBAM declarant.",
   "The Commission shall have the oversight role in the review of CBAM declarations.")
st("st.A19P2S3", "A19.P2.sub3", "relation_bearing",
   "The Commission shall communicate the initiation and the results of the review to the competent authority of the Member State where the declarant is established, via the CBAM registry.",
   "The Commission shall communicate the initiation and the results of the review to the competent authority of the Member State where the CBAM declarant is established, via the CBAM registry.")
st("st.A19P2S4", "A19.P2.sub4", "relation_bearing",
   "The competent authority of the Member State where the declarant is established may also review a CBAM declaration within the same period and shall communicate the initiation and results of a review to the Commission via the CBAM registry.",
   "The competent authority of the Member State where the authorised CBAM declarant is established may also review a CBAM declaration within the period referred to in the first subparagraph of this paragraph.")
st("st.A19P3", "A19.P3", "assignment_bearing",
   "The Commission shall periodically set out specific risk factors and points for attention, based on a risk analysis of the implementation of the CBAM at Union level, taking into account registry information, customs data, controls under Article 15(2) and Article 25 and other sources.",
   "The Commission shall periodically set out specific risk factors and points for attention, based on a risk analysis in relation to the implementation of the CBAM at Union level")
st("st.A19P3S2", "A19.P3.sub2", "relation_bearing",
   "The Commission shall facilitate the exchange of information with competent authorities about fraudulent activities and the penalties imposed in accordance with Article 26.",
   "The Commission shall also facilitate the exchange of information with competent authorities about fraudulent activities and the penalties imposed in accordance with Article 26.")
st("st.A19P4", "A19.P4", "relation_bearing",
   "Where a declarant fails to submit a declaration or the Commission considers on review that the declared number of certificates is incorrect, the Commission assesses the declarant's obligations on the information at its disposal and establishes a preliminary calculation of the certificates that should have been surrendered, which it provides to competent authorities for indicative purposes and without prejudice to the definitive calculation by the competent authority of the Member State where the declarant is established.",
   "The Commission shall provide to competent authorities such a preliminary calculation, for indicative purposes and without prejudice to the definitive calculation established by the competent authority of the Member State where the authorised CBAM declarant is established.")
st("st.A19P5", "A19.P5;A19.P5.sub2;A19.P5.sub3", "relation_bearing",
   "Where the competent authority concludes that the declared number of certificates is incorrect or that no declaration was submitted, it determines the number that should have been surrendered taking into account the Commission's information, notifies the declarant of its decision and requests surrender of the additional certificates within one month; the decision states reasons and information about the right to appeal and is notified via the CBAM registry.",
   "it shall determine the number of CBAM certificates which should have been surrendered by the authorised CBAM declarant, taking into account the information submitted by the Commission")
st("st.A19P5S4", "A19.P5.sub4", "relation_bearing",
   "Where, after receiving the Commission's preliminary calculation, the competent authority decides not to take any action, it shall inform the Commission via the CBAM registry.",
   "the competent authority shall inform the Commission accordingly, via the CBAM registry")
st("st.A19P6", "A19.P6", "relation_bearing",
   "Where the competent authority concludes that the number of certificates surrendered exceeds the number that should have been surrendered, it shall inform the Commission without delay and the excess certificates shall be repurchased in accordance with Article 23.",
   "it shall inform the Commission without delay. The CBAM certificates surrendered in excess shall be repurchased in accordance with Article 23.")
qr("qr.A19_REVIEW", "st.A19P1", "A19.P1;A19.P2;A19.P2.sub2", "pd.COM", "pd.ACD", "oversight_supervision", "Commission -> authorised CBAM declarant",
   "review CBAM declarations in accordance with a review strategy including risk factors, within the period ending with the fourth year after the year in which they should have been submitted, by verifying the information in the declaration and in verification reports on the basis of customs information, other evidence and any audit deemed necessary, including at the declarant's premises",
   "CBAM declarations and verification reports", "monitoring", "permission",
   "The Commission may review CBAM declarations, in accordance with a review strategy, including risk factors, within the period ending with the fourth year after the year during which the CBAM declarations should have been submitted.",
   tnote="the oversight role is stated as an obligation-like status in A19.P1 ('shall have the oversight role'); the review itself is permissive (A19.P2 'may'); the permission modality is recorded",
   mech="review strategy; audit, including at the premises of the authorised CBAM declarant", instr="INS-TYPE: CBAM declaration; verification report",
   cond="within the period ending with the fourth year after the year in which the declaration should have been submitted",
   authattr="Commission holds the oversight role in the review of declarations; may audit at the declarant's premises", discattr="review strategy and risk factors set by the Commission; the audit is performed where 'deemed necessary'",
   deps="pd.COM;pd.ACD", iunits="A25.P2")
qr("qr.A19_REVIEW_INFO", "st.A19P2S3", "A19.P2.sub3", "pd.COM", "pd.CA", "information_reporting", "Commission -> competent authority of the Member State where the declarant is established",
   "communicate the initiation and the results of the review to the competent authority of the Member State where the declarant is established, via the CBAM registry", "initiation and results of review",
   "information_provision", "obligation",
   "The Commission shall communicate the initiation and the results of the review to the competent authority of the Member State where the CBAM declarant is established, via the CBAM registry.",
   mech="communication via the CBAM registry", instr="pd.REGISTRY", cond="a review by the Commission under Article 19(2)", acls="INFO", asuff="sufficient",
   authattr="binding duty on the Commission", discattr="none stated", deps="pd.COM;pd.CA;pd.REGISTRY", gap="No competent authority is evidenced in W.")
qr("qr.A19_CAREVIEW", "st.A19P2S4", "A19.P2.sub4", "pd.CA", "pd.ACD", "oversight_supervision", "competent authority -> authorised CBAM declarant",
   "review a CBAM declaration within the period referred to in the first subparagraph", "CBAM declarations", "monitoring", "permission",
   "The competent authority of the Member State where the authorised CBAM declarant is established may also review a CBAM declaration within the period referred to in the first subparagraph of this paragraph.",
   mech="review of declaration", instr="INS-TYPE: CBAM declaration", cond="within the period ending with the fourth year after the year in which the declaration should have been submitted",
   authattr="competent authority of the declarant's Member State may review ('may')", discattr="discretionary; no review strategy specified for the competent authority", deps="pd.CA;pd.ACD",
   gap="No competent authority is evidenced in W.")
qr("qr.A19_CAINFO", "st.A19P2S4", "A19.P2.sub4", "pd.CA", "pd.COM", "information_reporting", "competent authority -> Commission",
   "communicate the initiation and the results of a review of a CBAM declaration to the Commission, via the CBAM registry", "initiation and results of review",
   "information_provision", "obligation",
   "The competent authority shall communicate the initiation and the results of a review to the Commission, via the CBAM registry.",
   mech="communication via the CBAM registry", instr="pd.REGISTRY", cond="a review by the competent authority under Article 19(2)", acls="INFO", asuff="sufficient",
   authattr="binding duty on the competent authority", discattr="none stated", deps="pd.CA;pd.COM;pd.REGISTRY")
na("na.A19_RISK", "st.A19P3", "A19.P3", "pd.COM", "periodically set out specific risk factors and points for attention based on a risk analysis of the implementation of the CBAM at Union level, taking into account registry information, customs data and other sources",
   "risk factors for review of declarations", "monitoring", "obligation",
   "The Commission shall periodically set out specific risk factors and points for attention, based on a risk analysis in relation to the implementation of the CBAM at Union level",
   mech="risk analysis", instr="pd.REGISTRY", nt="N0", eff="duty of the Commission to set risk factors", notc="the recipients of the risk factors are not named; no counterparty is created", deriv="direct", deps="pd.COM;pd.REGISTRY")
qr("qr.A19_FRAUD", "st.A19P3S2", "A19.P3.sub2", "pd.COM", "pd.CA", "information_reporting", "Commission -> competent authorities",
   "facilitate the exchange of information with competent authorities about fraudulent activities and the penalties imposed in accordance with Article 26", "information on fraudulent activities and penalties",
   "cooperation_coordination*", "obligation",
   "The Commission shall also facilitate the exchange of information with competent authorities about fraudulent activities and the penalties imposed in accordance with Article 26.",
   tnote="residual function tag; exchange facilitation", mech="information exchange", cond="", acls="INFO", asuff="sufficient", authattr="binding duty on the Commission", discattr="none stated",
   deps="pd.COM;pd.CA")
qr("qr.A19_ASSESS", "st.A19P4", "A19.P4", "pd.COM", "pd.ACD", "oversight_supervision", "Commission -> authorised CBAM declarant",
   "assess the obligations of the authorised CBAM declarant on the basis of the information at its disposal and establish a preliminary calculation of the total number of CBAM certificates that should have been surrendered, at the latest by 31 December of the year following the year in which the declaration should have been submitted, or by 31 December of the fourth year following the year in which an incorrect declaration was submitted",
   "preliminary calculation of certificates to be surrendered", "monitoring", "obligation",
   "the Commission shall assess the obligations under this Regulation of that authorised CBAM declarant on the basis of the information at its disposal",
   mech="assessment and preliminary calculation", instr="INS-TYPE: preliminary calculation", cond="the declarant fails to submit a CBAM declaration under Article 6, or the Commission considers on review that the declared number of certificates is incorrect",
   authattr="Commission assessment is indicative only: it is provided for indicative purposes and without prejudice to the definitive calculation by the competent authority", discattr="Commission determines on available information",
   deps="pd.COM;pd.ACD", iunits="A19.P2;A6.P1")
qr("qr.A19_PRELIM", "st.A19P4", "A19.P4", "pd.COM", "pd.CA", "information_reporting", "Commission -> competent authority",
   "provide to the competent authority the preliminary calculation of the number of CBAM certificates that should have been surrendered, for indicative purposes and without prejudice to the definitive calculation established by the competent authority of the Member State where the declarant is established",
   "preliminary calculation of certificates to be surrendered", "information_provision", "obligation",
   "The Commission shall provide to competent authorities such a preliminary calculation, for indicative purposes and without prejudice to the definitive calculation established by the competent authority of the Member State where the authorised CBAM declarant is established.",
   mech="communication of preliminary calculation", instr="INS-TYPE: preliminary calculation", cond="a preliminary calculation has been established under Article 19(4)", acls="INFO", asuff="sufficient",
   authattr="the Commission's input is non-binding on the competent authority (indicative; without prejudice to the definitive calculation)", discattr="competent authority retains the definitive calculation",
   deps="pd.COM;pd.CA")
qr("qr.A19_DECIDE", "st.A19P5", "A19.P5;A19.P5.sub2;A19.P5.sub3", "pd.CA", "pd.ACD", "authority_control", "competent authority -> authorised CBAM declarant",
   "determine the number of CBAM certificates that should have been surrendered, taking into account the information submitted by the Commission; notify the declarant of its decision and request surrender of the additional certificates within one month; state the reasons and information about the right to appeal and notify the decision via the CBAM registry",
   "number of CBAM certificates to be surrendered", "enforcement", "obligation",
   "it shall determine the number of CBAM certificates which should have been surrendered by the authorised CBAM declarant, taking into account the information submitted by the Commission",
   mech="administrative decision; notification via the CBAM registry; one-month period to surrender", instr="INS-TYPE: decision on number of certificates; pd.REGISTRY",
   cond="the competent authority concludes that the declared number is incorrect or that no declaration was submitted under Article 6",
   authattr="competent authority holds the definitive determination; the Commission's input is taken into account but not binding", discattr="determination of the number by the competent authority; decision whether to act after the Commission's preliminary calculation is for the competent authority (A19(5) fourth subparagraph)",
   acls="INFO", asuff="indeterminate", amiss="reasons and 'information about the right to appeal' are stated, but no appeal forum, assessment capacity or consequence is identified in W",
   deps="pd.CA;pd.ACD;pd.REGISTRY", unc="unc.APPEAL_FORUM", hq="hq.ACCOUNT_APPEAL")
qr("qr.A19_NOACTION", "st.A19P5S4", "A19.P5.sub4", "pd.CA", "pd.COM", "information_reporting", "competent authority -> Commission",
   "inform the Commission, via the CBAM registry, where after receiving the preliminary calculation it decides not to take any action", "decision not to act on the preliminary calculation",
   "information_provision", "obligation",
   "the competent authority shall inform the Commission accordingly, via the CBAM registry",
   mech="communication via the CBAM registry", instr="pd.REGISTRY", cond="the competent authority, after receiving the preliminary calculation, decides not to take any action", acls="INFO", asuff="sufficient",
   authattr="binding duty on the competent authority; no duty to justify the decision is stated", discattr="none stated", deps="pd.CA;pd.COM;pd.REGISTRY")
qr("qr.A19_EXCESS", "st.A19P6", "A19.P6;A23.P1", "pd.CA", "pd.COM", "information_reporting", "competent authority -> Commission",
   "inform the Commission without delay where the number of CBAM certificates surrendered exceeds the number that should have been surrendered", "excess surrender of certificates",
   "information_provision", "obligation",
   "it shall inform the Commission without delay",
   mech="notification", cond="the competent authority concludes that the number surrendered exceeds the number that should have been surrendered", acls="INFO", asuff="sufficient",
   authattr="binding duty on the competent authority", discattr="none stated", deps="pd.CA;pd.COM", deriv="direct", iunits="A23.P1")
