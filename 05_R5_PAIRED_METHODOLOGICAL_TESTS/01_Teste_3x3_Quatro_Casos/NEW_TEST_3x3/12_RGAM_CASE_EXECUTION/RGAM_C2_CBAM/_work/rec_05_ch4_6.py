from rgam_lib import *

# =============== ARTICLE 20 ===============
st("st.A20P1", "A20.P1;A20.P4", "relation_bearing",
   "A Member State shall sell CBAM certificates on a common central platform to authorised CBAM declarants established in that Member State, at the price calculated in accordance with Article 21.",
   "A Member State shall sell CBAM certificates on a common central platform to authorised CBAM declarants established in that Member State.")
st("st.A20P2", "A20.P2;A20.P2.sub2;A20.P3", "device_defining",
   "The Commission shall establish and manage the common central platform following a joint procurement procedure between the Commission and the Member States; the Commission and the competent authorities have access to its information; information on sale, repurchase and cancellation of certificates is transferred to the CBAM registry at the end of each working day.",
   "The Commission shall establish and manage the common central platform following a joint procurement procedure between the Commission and the Member States.")
st("st.A20P5", "A20.P5", "relation_bearing",
   "The Commission shall ensure that each CBAM certificate is assigned a unique identification number on creation and shall register that number and the price and date of sale in the CBAM registry in the account of the purchasing authorised CBAM declarant.",
   "The Commission shall register the unique identification number and the price and date of sale of the CBAM certificate in the CBAM registry in the account of the authorised CBAM declarant purchasing that certificate.")
st("st.A20P6", "A20.P6", "assignment_bearing",
   "The Commission shall adopt delegated acts under Article 28 specifying the timing, administration and other aspects of the management of the sale and repurchase of CBAM certificates, seeking coherence with Commission Regulation (EU) No 1031/2010.",
   "The Commission shall adopt delegated acts in accordance with Article 28 supplementing this Regulation by further specifying the timing, administration and other aspects related to the management of the sale and repurchase of CBAM certificates")
na("na.A20_PLATFORM", "st.A20P2", "A20.P2;A20.P2.sub2;A20.P3", "pd.COM", "establish and manage the common central platform for the sale and repurchase of CBAM certificates following a joint procurement procedure between the Commission and the Member States",
   "the common central platform", "implementation", "obligation",
   "The Commission shall establish and manage the common central platform following a joint procurement procedure between the Commission and the Member States.",
   mech="joint procurement procedure; platform operation", instr="pd.PLATFORM", cond="", nt="N2",
   eff="obligation of the Commission to establish and manage the common central platform", notc="the platform (device) is not itself constituted by this wording (N2); no establishment is evidenced",
   deriv="direct", deps="pd.COM;pd.PLATFORM", epi="documented", unc="unc.DEV_PLATFORM")
qr("qr.A20_SELL", "st.A20P1", "A20.P1;A20.P4;A21.P1", "pd.MS", "pd.ACD", "contractual_exchange", "Member State -> authorised CBAM declarants established in that Member State",
   "sell CBAM certificates on the common central platform to authorised CBAM declarants established in that Member State, at the price calculated in accordance with Article 21",
   "CBAM certificates", "implementation", "obligation",
   "A Member State shall sell CBAM certificates on a common central platform to authorised CBAM declarants established in that Member State.",
   tnote="the seller is the Member State; the platform is an instrument (device), not a party", mech="sale on the common central platform at the Article 21 price", instr="pd.PLATFORM",
   cond="authorised CBAM declarants established in that Member State; price calculated in accordance with Article 21", authattr="Member State sells; the purchaser is an authorised CBAM declarant established there",
   discattr="price is not set by the Member State (Article 21); no discretion over the price stated", deps="pd.MS;pd.ACD;pd.PLATFORM", unc="unc.A20_INSTRUMENT",
   gap="Establishment of the common central platform is not evidenced (Article 20(2) is an N2 duty).", iunits="A21.P1")
qr("qr.A20_REGSALE", "st.A20P5", "A20.P5", "pd.COM", "pd.ACD", "information_reporting", "Commission -> authorised CBAM declarant (account of the purchaser)",
   "ensure that each CBAM certificate is assigned a unique identification number upon creation and register the number, the price and the date of sale in the CBAM registry in the account of the purchasing authorised CBAM declarant",
   "record of certificate purchases in the declarant's account", "implementation", "obligation",
   "The Commission shall register the unique identification number and the price and date of sale of the CBAM certificate in the CBAM registry in the account of the authorised CBAM declarant purchasing that certificate.",
   mech="registration in the declarant's account", instr="pd.REGISTRY", cond="a CBAM certificate is sold to an authorised CBAM declarant", acls="INFO", asuff="sufficient",
   authattr="Commission keeps the declarant's account of certificates", discattr="none stated", deps="pd.COM;pd.ACD;pd.REGISTRY")
na("na.A20P6_DELEG", "st.A20P6", "A20.P6", "pd.COM", "adopt delegated acts further specifying the timing, administration and other aspects of the management of the sale and repurchase of CBAM certificates, seeking coherence with Commission Regulation (EU) No 1031/2010",
   "delegated acts on certificate sale and repurchase", "rule_making_standard_setting", "obligation",
   "The Commission shall adopt delegated acts in accordance with Article 28 supplementing this Regulation by further specifying the timing, administration and other aspects related to the management of the sale and repurchase of CBAM certificates",
   mech="delegated act (Article 28)", instr="INS-TYPE: delegated act", nt="N0", eff="duty of the Commission to adopt delegated acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM")
ext("ext.REG1031", "st.A20P6;st.A21P1", "A20.P6;A21.P1", "Commission Regulation (EU) No 1031/2010 (timing, administration and other aspects of auctioning of greenhouse gas emission allowances)", "legal_instrument",
    "supplies_rule_or_standard", dependents="na.A21_PRICE;na.A20P6_DELEG", dep_kind="specifies", constitutive="Y",
    effect="The weekly price of CBAM certificates is the average of EU ETS allowance closing prices 'on the auction platform, in accordance with the procedures laid down in' the external Regulation; the price-formation procedure and the auction platform are undetermined within W.")

# =============== ARTICLE 21 ===============
st("st.A21P1", "A21.P1;A21.P1.sub2", "assignment_bearing",
   "The Commission shall calculate the price of CBAM certificates as the average of the closing prices of EU ETS allowances on the auction platform, in accordance with Regulation (EU) No 1031/2010, for each calendar week; for weeks without auctions the price is the average of the last week with auctions.",
   "The Commission shall calculate the price of CBAM certificates as the average of the closing prices of EU ETS allowances on the auction platform")
st("st.A21P2", "A21.P2", "assignment_bearing",
   "The Commission shall publish the average price on its website or in another appropriate manner on the first working day of the following calendar week; it applies from the first working day following publication to the first working day of the following calendar week.",
   "The Commission shall publish the average price, as referred to in the second subparagraph of paragraph 1, on its website or in any other appropriate manner")
st("st.A21P3", "A21.P3", "assignment_bearing",
   "The Commission is empowered to adopt implementing acts on the application of the price-calculation methodology and the practical arrangements for publishing the price, under the examination procedure of Article 29(2).",
   "The Commission is empowered to adopt implementing acts on the application of the methodology provided for in paragraph 1 of this Article to calculate the average price of CBAM certificates")
na("na.A21_PRICE", "st.A21P1", "A21.P1;A21.P1.sub2", "pd.COM", "calculate the price of CBAM certificates as the average of the closing prices of EU ETS allowances on the auction platform for each calendar week",
   "weekly price of CBAM certificates", "implementation", "obligation",
   "The Commission shall calculate the price of CBAM certificates as the average of the closing prices of EU ETS allowances on the auction platform",
   mech="weekly averaging of auction closing prices", instr="INS-TYPE: auction platform (external)", cond="for each calendar week; weeks without auctions take the average of the last week in which auctions took place",
   nt="N0", eff="duty of the Commission to calculate the price", notc="no recipient named; no counterparty created", deriv="direct", deps="pd.COM", ext="ext.REG1031")
na("na.A21_PUBLISH", "st.A21P2", "A21.P2", "pd.COM", "publish the average price on its website or in another appropriate manner on the first working day of the following calendar week",
   "weekly price of CBAM certificates", "information_provision", "obligation",
   "The Commission shall publish the average price, as referred to in the second subparagraph of paragraph 1, on its website or in any other appropriate manner",
   mech="publication", cond="first working day of the following calendar week", nt="N0", eff="duty of the Commission to publish the price", notc="no recipient named; no counterparty created", deriv="direct", deps="pd.COM")
na("na.A21P3_IMPL", "st.A21P3", "A21.P3", "pd.COM", "adopt implementing acts on the application of the price-calculation methodology and the practical arrangements for publication",
   "implementing acts on certificate price", "rule_making_standard_setting", "competence",
   "The Commission is empowered to adopt implementing acts on the application of the methodology provided for in paragraph 1 of this Article to calculate the average price of CBAM certificates",
   mech="implementing act under the examination procedure (Article 29(2))", instr="INS-TYPE: implementing act", nt="N3", eff="competence of the Commission to adopt implementing acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM")

# =============== ARTICLE 22 ===============
st("st.A22P1", "A22.P1", "assignment_bearing",
   "By 31 May each year (first in 2027 for 2026) the authorised CBAM declarant shall surrender via the CBAM registry the number of CBAM certificates corresponding to the declared and verified embedded emissions; the Commission removes surrendered certificates from the registry; the declarant ensures the required number is available on its account.",
   "the authorised CBAM declarant shall surrender via the CBAM registry a number of CBAM certificates that corresponds to the embedded emissions declared in accordance with Article 6(2), point (c), and verified in accordance with Article 8")
st("st.A22P2", "A22.P2", "assignment_bearing",
   "The authorised CBAM declarant shall ensure that the number of CBAM certificates on its account at the end of each quarter corresponds to at least 80 % of the embedded emissions, determined by reference to default values, in all goods imported since the beginning of the calendar year.",
   "at the end of each quarter corresponds to at least 80 % of the embedded emissions, determined by reference to default values")
st("st.A22P3", "A22.P3;A22.P3.sub2;A22.P3.sub3", "relation_bearing",
   "Where the Commission finds that the certificates on a declarant's account do not meet the quarterly requirement it informs, via the CBAM registry, the competent authority of the Member State where the declarant is established; the competent authority notifies the declarant to ensure a sufficient number within one month and registers the notification and the response in the registry.",
   "it shall inform, via the CBAM registry, the competent authority of the Member State where the authorised CBAM declarant is established")
na("na.A22_SURRENDER", "st.A22P1", "A22.P1", "pd.ACD", "surrender via the CBAM registry by 31 May of each year the number of CBAM certificates corresponding to the embedded emissions declared under Article 6(2)(c) and verified under Article 8 for the preceding calendar year, and ensure that the required number of certificates is available on its account",
   "CBAM certificates corresponding to declared and verified embedded emissions", "implementation", "obligation",
   "the authorised CBAM declarant shall surrender via the CBAM registry a number of CBAM certificates that corresponds to the embedded emissions declared in accordance with Article 6(2), point (c), and verified in accordance with Article 8",
   mech="surrender (offsetting of certificates) via the CBAM registry", instr="pd.REGISTRY", cond="by 31 May of each year, for the first time in 2027 for the year 2026", nt="N0",
   eff="duty of the authorised CBAM declarant to surrender certificates", notc="the provision does not name the recipient of the surrender; no counterparty is created (the Commission's removal of surrendered certificates is a separate assignment)",
   deriv="direct", deps="pd.ACD;pd.REGISTRY", unc="unc.A22_RECIPIENT")
na("na.A22_REMOVE", "st.A22P1", "A22.P1", "pd.COM", "remove surrendered CBAM certificates from the CBAM registry", "surrendered CBAM certificates", "implementation", "obligation",
   "The Commission shall remove surrendered CBAM certificates from the CBAM registry.", mech="registry operation", instr="pd.REGISTRY", cond="certificates surrendered by an authorised CBAM declarant",
   nt="N0", eff="duty of the Commission to remove surrendered certificates", notc="no recipient/counterparty named; the declarant is the surrendering party but the provision frames removal as a registry operation", deriv="direct", deps="pd.COM;pd.REGISTRY")
na("na.A22_QUARTERLY", "st.A22P2", "A22.P2", "pd.ACD", "ensure that the number of CBAM certificates on its account at the end of each quarter corresponds to at least 80 % of the embedded emissions, determined by reference to default values, in all goods imported since the beginning of the calendar year",
   "sufficiency of certificates on the account", "implementation", "obligation",
   "The authorised CBAM declarant shall ensure that the number of CBAM certificates on its account in the CBAM registry at the end of each quarter corresponds to at least 80 % of the embedded emissions",
   mech="quarterly holding threshold", instr="pd.REGISTRY", cond="end of each quarter; goods imported since the beginning of the calendar year", nt="N0",
   eff="duty of the authorised CBAM declarant to hold a minimum number of certificates", notc="no counterparty named for the duty itself (monitoring is assigned in A22(3))", deriv="direct", deps="pd.ACD;pd.REGISTRY")
qr("qr.A22_INFORM", "st.A22P3", "A22.P3", "pd.COM", "pd.CA", "information_reporting", "Commission -> competent authority of the Member State where the declarant is established",
   "inform, via the CBAM registry, the competent authority where it finds that the number of certificates in a declarant's account does not comply with the quarterly obligation", "non-compliance with the quarterly certificate holding obligation",
   "monitoring", "obligation",
   "Where the Commission finds that the number of CBAM certificates in the account of an authorised CBAM declarant does not comply with the obligations pursuant to paragraph 2, it shall inform, via the CBAM registry, the competent authority of the Member State where the authorised CBAM declarant is established.",
   mech="notification via the CBAM registry", instr="pd.REGISTRY", cond="the Commission finds that the number of CBAM certificates in the account does not comply with Article 22(2)", acls="INFO", asuff="sufficient",
   authattr="Commission finding triggers competent-authority action", discattr="Commission determines non-compliance", deps="pd.COM;pd.CA;pd.REGISTRY", gap="No competent authority is evidenced in W.")
qr("qr.A22_NOTIFY", "st.A22P3", "A22.P3.sub2;A22.P3.sub3", "pd.CA", "pd.ACD", "authority_control", "competent authority -> authorised CBAM declarant",
   "notify the authorised CBAM declarant of the need to ensure a sufficient number of CBAM certificates in its account within one month of notification, and register the notification and the declarant's response in the CBAM registry",
   "sufficiency of certificates on the account", "enforcement", "obligation",
   "The competent authority shall notify the authorised CBAM declarant of the need to ensure a sufficient number of CBAM certificates in its account within one month of such notification.",
   mech="notification with one-month period; registration of notification and response", instr="pd.REGISTRY",
   cond="the Commission has informed the competent authority under Article 22(3) first subparagraph", authattr="competent authority notifies and fixes a one-month period", discattr="none stated",
   deps="pd.CA;pd.ACD;pd.REGISTRY", gap="No competent authority is evidenced in W.", iunits="A22.P3")

# =============== ARTICLE 23 ===============
st("st.A23P1", "A23.P1;A23.P2;A23.P3", "relation_bearing",
   "Where an authorised CBAM declarant so requests, the Member State where it is established shall repurchase the excess CBAM certificates remaining on its account after surrender, limited to one third of the certificates purchased in the previous calendar year, at the price paid at the time of purchase.",
   "Where an authorised CBAM declarant so requests, the Member State where that authorised CBAM declarant is established shall repurchase the excess CBAM certificates remaining on the account of the declarant in the CBAM registry")
st("st.A23P1S2", "A23.P1.sub2", "relation_bearing",
   "The Commission shall repurchase the excess CBAM certificates through the common central platform on behalf of the Member State where the declarant is established; the declarant shall submit the repurchase request by 30 June of each year during which certificates were surrendered.",
   "The Commission shall repurchase the excess CBAM certificates through the common central platform referred to in Article 20 on behalf of the Member State where the authorised CBAM declarant is established.")
qr("qr.A23_REPURCHASE", "st.A23P1", "A23.P1;A23.P2;A23.P3", "pd.MS", "pd.ACD", "contractual_exchange", "Member State where the declarant is established -> authorised CBAM declarant",
   "repurchase, on the declarant's request, the excess CBAM certificates remaining on its account after surrender, limited to one third of the certificates purchased during the previous calendar year, at the price paid by the declarant at the time of purchase",
   "excess CBAM certificates", "implementation", "obligation",
   "Where an authorised CBAM declarant so requests, the Member State where that authorised CBAM declarant is established shall repurchase the excess CBAM certificates remaining on the account of the declarant in the CBAM registry",
   mech="repurchase at purchase price, capped at one third of previous-year purchases", instr="pd.PLATFORM",
   cond="the declarant requests the repurchase; certificates are in excess after surrender under Article 22; cap of one third of the previous calendar year's purchases",
   authattr="Member State is obliged to repurchase on request within the cap", discattr="none stated", deps="pd.MS;pd.ACD;pd.PLATFORM", gap="Establishment of the common central platform is not evidenced.", iunits="A23.P1.sub2")
qr("qr.A23_REQUEST", "st.A23P1S2", "A23.P1.sub2;A23.P1", "pd.ACD", "pd.MS", "contractual_exchange", "authorised CBAM declarant -> Member State where it is established",
   "submit the repurchase request by 30 June of each year during which CBAM certificates were surrendered", "request for repurchase of excess certificates", "implementation", "obligation",
   "The authorised CBAM declarant shall submit the repurchase request by 30 June of each year during which CBAM certificates were surrendered.",
   mech="repurchase request", cond="by 30 June of each year during which CBAM certificates were surrendered", deriv="derived",
   drule="A23.P1.sub2 states the declarant's duty to submit the request without naming its addressee; A23.P1 makes the Member State where the declarant is established the obligor on 'such request' ('Where an authorised CBAM declarant so requests, the Member State ... shall repurchase'), so the request is addressed to that Member State.",
   authattr="the request is a condition of the repurchase duty", discattr="none stated", deps="pd.ACD;pd.MS", unc="unc.A23_REQUEST_ADDRESSEE")
qr("qr.A23_COMBEHALF", "st.A23P1S2", "A23.P1.sub2", "pd.COM", "pd.MS", "delegation_authorization", "Commission -> Member State (acting on its behalf)",
   "repurchase the excess CBAM certificates through the common central platform on behalf of the Member State where the authorised CBAM declarant is established",
   "excess CBAM certificates", "implementation", "obligation",
   "The Commission shall repurchase the excess CBAM certificates through the common central platform referred to in Article 20 on behalf of the Member State where the authorised CBAM declarant is established.",
   gdir="Member State -> Commission (the Commission acts as agent for the Member State's repurchase duty)", tnote="the textual obligor is the Commission; the Member State is the principal on whose behalf it acts",
   mech="repurchase through the common central platform", instr="pd.PLATFORM", cond="the declarant has requested repurchase", authattr="Commission acts for the Member State; the legal source of the agency is the Regulation itself",
   discattr="none stated", deps="pd.COM;pd.MS;pd.PLATFORM", gap="Establishment of the common central platform is not evidenced.")

# =============== ARTICLE 24 ===============
st("st.A24", "A24.P0", "relation_bearing",
   "On 1 July each year the Commission shall cancel, without compensation, any CBAM certificates purchased during the year before the previous calendar year that remain in an authorised CBAM declarant's account.",
   "On 1 July of each year, the Commission shall cancel any CBAM certificates that were purchased during the year before the previous calendar year and that remained in the account of an authorised CBAM declarant in the CBAM registry.")
st("st.A24S2", "A24.P0.sub2", "relation_bearing",
   "Where the number of certificates to be surrendered is contested in a pending dispute in a Member State, the Commission shall suspend the cancellation to the extent of the disputed amount; the competent authority shall communicate relevant information to the Commission without delay.",
   "the Commission shall suspend the cancellation of the CBAM certificates to the extent corresponding to the disputed amount")
qr("qr.A24_CANCEL", "st.A24", "A24.P0", "pd.COM", "pd.ACD", "authority_control", "Commission -> authorised CBAM declarant (account holder)",
   "cancel, without compensation, on 1 July of each year, CBAM certificates purchased during the year before the previous calendar year that remain in the declarant's account in the CBAM registry",
   "cancellation of expired CBAM certificates", "implementation", "obligation",
   "On 1 July of each year, the Commission shall cancel any CBAM certificates that were purchased during the year before the previous calendar year and that remained in the account of an authorised CBAM declarant in the CBAM registry.",
   mech="cancellation without compensation", instr="pd.REGISTRY", cond="1 July of each year; certificates purchased during the year before the previous calendar year and remaining in the declarant's account",
   authattr="Commission cancels by operation of the provision", discattr="none stated", deps="pd.COM;pd.ACD;pd.REGISTRY")
qr("qr.A24_SUSPEND", "st.A24S2", "A24.P0.sub2", "pd.COM", "pd.ACD", "authority_control", "Commission -> authorised CBAM declarant (account holder)",
   "suspend the cancellation of CBAM certificates to the extent corresponding to the disputed amount where the number of certificates to be surrendered is contested in a pending dispute in a Member State",
   "suspension of cancellation of CBAM certificates", "implementation", "obligation",
   "the Commission shall suspend the cancellation of the CBAM certificates to the extent corresponding to the disputed amount",
   mech="suspension", instr="pd.REGISTRY", cond="the number of certificates to be surrendered is contested in a pending dispute in a Member State",
   authattr="Commission suspends by operation of the provision", discattr="none stated", deps="pd.COM;pd.ACD;pd.REGISTRY", unc="unc.A24_DISPUTE_FORUM",
   gap="The forum of the 'pending dispute' is not identified in W.")
qr("qr.A24_CAINFO", "st.A24S2", "A24.P0.sub2", "pd.CA", "pd.COM", "information_reporting", "competent authority -> Commission",
   "communicate without delay any relevant information to the Commission where the number of CBAM certificates to be surrendered is contested in a pending dispute", "information relevant to the suspension of cancellation",
   "information_provision", "obligation",
   "The competent authority of the Member State where the authorised CBAM declarant is established shall communicate without delay any relevant information to the Commission.",
   mech="communication", cond="the number of certificates to be surrendered is contested in a pending dispute in a Member State", acls="INFO", asuff="sufficient",
   authattr="binding duty on the competent authority", discattr="none stated", deps="pd.CA;pd.COM", gap="No competent authority is evidenced in W.")

# =============== ARTICLE 25 ===============
st("st.A25P1", "A25.P1", "assignment_bearing",
   "The customs authorities shall not allow the importation of goods by any person other than an authorised CBAM declarant.",
   "The customs authorities shall not allow the importation of goods by any person other than an authorised CBAM declarant.")
st("st.A25P2", "A25.P2", "relation_bearing",
   "The customs authorities shall periodically and automatically, in particular by means of the surveillance mechanism established pursuant to Article 56(5) of Regulation (EU) No 952/2013, communicate to the Commission specific information on goods declared for importation (EORI number and CBAM account number of the authorised CBAM declarant, eight-digit CN code, quantity, country of origin, date of the customs declaration and customs procedure).",
   "The customs authorities shall periodically and automatically")
st("st.A25P3", "A25.P3", "relation_bearing",
   "The Commission shall communicate the information of paragraph 2 to the competent authority of the Member State where the authorised CBAM declarant is established and shall, for each declarant, cross-check it with the data in the CBAM registry.",
   "The Commission shall communicate the information referred to in paragraph 2 of this Article to the competent authority of the Member State where the authorised CBAM declarant is established")
st("st.A25P4", "A25.P4", "relation_bearing",
   "The customs authorities may communicate, in accordance with Article 12(1) of Regulation (EU) No 952/2013, confidential information acquired in the course of their duties to the Commission and to the competent authority of the Member State that granted the status of authorised CBAM declarant.",
   "The customs authorities may communicate, in accordance with Article 12(1) of Regulation (EU) No 952/2013, confidential information")
st("st.A25P5", "A25.P5", "external_referencing",
   "Regulation (EC) No 515/97 shall apply mutatis mutandis to this Regulation.",
   "Regulation (EC) No 515/97 shall apply mutatis mutandis to this Regulation.")
st("st.A25P6", "A25.P6", "assignment_bearing",
   "The Commission is empowered to adopt implementing acts defining the scope of information and the periodicity, timing and means for the communication under paragraph 2, under the examination procedure of Article 29(2).",
   "The Commission is empowered to adopt implementing acts defining the scope of information and the periodicity, timing and means for communicating that information pursuant to paragraph 2 of this Article.")
na("na.A25_PROHIB", "st.A25P1", "A25.P1", "pd.CUST", "allow the importation of goods by any person other than an authorised CBAM declarant", "importation of goods", "enforcement", "prohibition",
   "The customs authorities shall not allow the importation of goods by any person other than an authorised CBAM declarant.",
   mech="customs control", instr="INS-TYPE: customs declaration (external)", cond="", cp="person other than an authorised CBAM declarant", cps="IN_PROVISION", nt="N0",
   eff="constraint on customs authorities: importation by persons other than authorised CBAM declarants is not to be allowed", notc="not a relation; the persons concerned are the object of the constraint",
   constraint="Y", deriv="direct", deps="pd.CUST;pd.OTHERPERSON", ext="ext.UCC_PERSONS", iunits="A4.P0")
qr("qr.A25_COMM", "st.A25P2", "A25.P2", "pd.CUST", "pd.COM", "information_reporting", "customs authorities -> Commission",
   "periodically and automatically communicate to the Commission specific information on goods declared for importation (EORI number and CBAM account number of the authorised CBAM declarant, eight-digit CN code, quantity, country of origin, date of the customs declaration and customs procedure)",
   "information on goods declared for importation", "information_provision", "obligation",
   "The customs authorities shall periodically and automatically",
   mech="automatic communication, in particular by means of the surveillance mechanism established pursuant to Article 56(5) of Regulation (EU) No 952/2013", instr="INS-TYPE: surveillance mechanism (external)",
   cond="goods declared for importation", acls="INFO", asuff="sufficient", authattr="binding duty on the customs authorities", discattr="scope and periodicity to be defined by implementing acts (A25(6))",
   deps="pd.CUST;pd.COM", ext="ext.UCC_SURVEIL", gap="The surveillance mechanism and the customs authorities' own constitution are external to W.")
qr("qr.A25_COM2CA", "st.A25P3", "A25.P3", "pd.COM", "pd.CA", "information_reporting", "Commission -> competent authority of the Member State where the declarant is established",
   "communicate the information received from the customs authorities to the competent authority of the Member State where the authorised CBAM declarant is established", "information on goods declared for importation",
   "information_provision", "obligation",
   "The Commission shall communicate the information referred to in paragraph 2 of this Article to the competent authority of the Member State where the authorised CBAM declarant is established",
   mech="communication", cond="information received under Article 25(2)", acls="INFO", asuff="sufficient", authattr="binding duty on the Commission", discattr="none stated", deps="pd.COM;pd.CA",
   gap="No competent authority is evidenced in W.", iunits="A25.P2")
na("na.A25_CROSSCHECK", "st.A25P3", "A25.P3", "pd.COM", "cross-check, for each authorised CBAM declarant, the information received from the customs authorities with the data in the CBAM registry pursuant to Article 14",
   "information on goods declared for importation against registry data", "verification_assurance", "obligation",
   "for each CBAM declarant, cross-check that information with the data in the CBAM registry pursuant to Article 14",
   mech="cross-check", instr="pd.REGISTRY", cond="information received under Article 25(2)", nt="N0", eff="duty of the Commission to cross-check customs information against registry data",
   notc="the cross-check is an operation on records; the declarants whose data are checked are not addressees of a communication", deriv="direct", deps="pd.COM;pd.REGISTRY", iunits="A25.P2")
qr("qr.A25_CONF", "st.A25P4", "A25.P4", "pd.CUST", "pd.COM", "information_reporting", "customs authorities -> Commission and the competent authority that granted the status",
   "communicate, in accordance with Article 12(1) of Regulation (EU) No 952/2013, confidential information acquired in the course of performing their duties, or provided on a confidential basis, to the Commission and the competent authority of the Member State that granted the status of authorised CBAM declarant",
   "confidential information", "cooperation_coordination*", "permission",
   "The customs authorities may communicate, in accordance with Article 12(1) of Regulation (EU) No 952/2013, confidential information",
   extra="pd.CA", tnote="residual function tag; the competent authority is an additional party", mech="communication under the external confidentiality rule", instr="",
   cond="confidential information acquired in the course of performing their duties or provided on a confidential basis", acls="INFO", asuff="sufficient",
   authattr="permissive competence", discattr="discretionary ('may')", deps="pd.CUST;pd.COM;pd.CA", ext="ext.UCC_SURVEIL", gap="Article 12(1) of Regulation (EU) No 952/2013 is external to W.")
ext("ext.UCC_SURVEIL", "st.A25P2;st.A25P4", "A25.P2;A25.P4;A33.P2", "Regulation (EU) No 952/2013 (Union Customs Code): Art. 56(5) (surveillance mechanism), Art. 12(1) (customs confidentiality)", "legal_instrument",
    "supplies_rule_or_standard", dependents="qr.A25_COMM;qr.A25_CONF;qr.A33_COMM", dep_kind="conditions", constitutive="Y",
    effect="The surveillance mechanism through which customs information is communicated and the confidentiality rule governing its transmission are external; the content and legal basis of the transmission channel are undetermined within W.")
ext("ext.REG515", "st.A25P5", "A25.P5", "Council Regulation (EC) No 515/97 (mutual assistance between administrative authorities of the Member States and cooperation with the Commission on customs and agricultural matters)", "legal_instrument",
    "supplies_rule_or_standard", dependents="st.A25P5", dep_kind="specifies", constitutive="Y",
    effect="'Shall apply mutatis mutandis' imports an unknown set of mutual-assistance relations from an external instrument; no such relation is coded; claims about mutual assistance among administrative authorities and the Commission are undetermined within W.")
na("na.A25P6_IMPL", "st.A25P6", "A25.P6", "pd.COM", "adopt implementing acts defining the scope of information and the periodicity, timing and means for communicating the customs information under paragraph 2",
   "implementing acts on customs information", "rule_making_standard_setting", "competence",
   "The Commission is empowered to adopt implementing acts defining the scope of information and the periodicity, timing and means for communicating that information pursuant to paragraph 2 of this Article.",
   mech="implementing act under the examination procedure (Article 29(2))", instr="INS-TYPE: implementing act", nt="N3", eff="competence of the Commission to adopt implementing acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM")

# =============== ARTICLE 26 ===============
st("st.A26P1", "A26.P1", "assignment_bearing",
   "An authorised CBAM declarant who fails to surrender by 31 May the number of CBAM certificates corresponding to the emissions embedded in goods imported in the preceding calendar year shall be held liable for a penalty identical to the excess emissions penalty of Article 16(3) of Directive 2003/87/EC, increased under Article 16(4) of that Directive, for each certificate not surrendered.",
   "An authorised CBAM declarant who fails to surrender, by 31 May of each year, the number of CBAM certificates that corresponds to the emissions embedded in goods imported during the preceding calendar year shall be held liable for the payment of a penalty.")
st("st.A26P2", "A26.P2", "assignment_bearing",
   "A person other than an authorised CBAM declarant who introduces goods into the customs territory without complying with the obligations under the Regulation shall be held liable for a penalty, effective, proportionate and dissuasive, of three to five times the penalty of paragraph 1 for each certificate not surrendered.",
   "that person shall be held liable for the payment of a penalty")
st("st.A26P3", "A26.P3", "assignment_bearing",
   "The payment of the penalty does not release the authorised CBAM declarant from the obligation to surrender the outstanding number of CBAM certificates in a given year.",
   "The payment of the penalty shall not release the authorised CBAM declarant from the obligation to surrender the outstanding number of CBAM certificates in a given year.")
st("st.A26P4", "A26.P4;A26.P4.pta;A26.P4.ptb;A26.P4.ptc;A26.P4.ptd;A26.P4.pte;A26.P4.ptf", "relation_bearing",
   "If the competent authority determines, including in light of the Commission's preliminary calculations, that a declarant failed to surrender or that a person introduced goods without complying, it imposes the penalty and notifies the declarant or person of the conclusion, reasons, amount, due date, action to pay and the right to appeal.",
   "the competent authority shall impose the penalty pursuant to paragraph 1 or 2 of this Article, as applicable")
st("st.A26P5", "A26.P5", "relation_bearing",
   "Where the penalty has not been paid by the due date, the competent authority shall secure payment by all means available to it under the national law of the Member State concerned.",
   "the competent authority shall secure payment of that penalty by all means available to it under the national law of the Member State concerned")
st("st.A26P6", "A26.P6", "relation_bearing",
   "Member States shall communicate the decisions on penalties to the Commission and register the final payment in the CBAM registry.",
   "Member States shall communicate the decisions on penalties referred to in paragraphs 1 and 2 to the Commission and shall register the final payment referred to in paragraph 5 in the CBAM registry.")
na("na.A26_LIABLE_ACD", "st.A26P1", "A26.P1", "pd.ACD", "be held liable for the payment of a penalty where it fails to surrender by 31 May the number of CBAM certificates corresponding to the emissions embedded in goods imported during the preceding calendar year, for each certificate not surrendered",
   "penalty for failure to surrender certificates", "enforcement", "obligation",
   "An authorised CBAM declarant who fails to surrender, by 31 May of each year, the number of CBAM certificates that corresponds to the emissions embedded in goods imported during the preceding calendar year shall be held liable for the payment of a penalty.",
   mech="monetary penalty; amount identical to the excess emissions penalty of Article 16(3) of Directive 2003/87/EC increased under Article 16(4)", instr="INS-TYPE: penalty",
   cond="failure to surrender by 31 May the number of certificates corresponding to embedded emissions of the preceding calendar year", nt="N0",
   eff="liability of the authorised CBAM declarant to a penalty", notc="the penalty's recipient and imposing authority are identified in A26(4)-(5); the amount depends on an external provision",
   deriv="direct", deps="pd.ACD", ext="ext.DIR87_PEN", epi="documented", unc="unc.A26_AMOUNT_EXT")
na("na.A26_LIABLE_OTHER", "st.A26P2", "A26.P2", "pd.OTHERPERSON", "be held liable for the payment of a penalty where it introduces goods into the customs territory without complying with the obligations under the Regulation: an effective, proportionate and dissuasive amount from three to five times the penalty of paragraph 1 for each certificate not surrendered",
   "penalty for introducing goods without complying with the Regulation", "enforcement", "obligation",
   "that person shall be held liable for the payment of a penalty",
   mech="monetary penalty; three to five times the paragraph 1 penalty", instr="INS-TYPE: penalty",
   cond="a person other than an authorised CBAM declarant introduces goods into the customs territory of the Union without complying with the obligations under the Regulation; the amount depends on duration, gravity, scope, intentional nature and repetition of non-compliance and the person's level of cooperation with the competent authority",
   nt="N0", eff="liability of the person to a penalty", notc="the amount depends on the paragraph 1 amount, which depends on an external provision", deriv="direct", deps="pd.OTHERPERSON", ext="ext.DIR87_PEN", epi="documented", unc="unc.A26_AMOUNT_EXT")
na("na.A26P3_SURRENDER", "st.A26P3", "A26.P3", "pd.ACD", "surrender the outstanding number of CBAM certificates notwithstanding payment of the penalty", "outstanding CBAM certificates", "enforcement", "obligation",
   "The payment of the penalty shall not release the authorised CBAM declarant from the obligation to surrender the outstanding number of CBAM certificates in a given year.",
   mech="continuing obligation", cond="a penalty has been paid", nt="N0", eff="continuation of the surrender duty after payment of a penalty", notc="no counterparty named", deriv="direct", deps="pd.ACD")
qr("qr.A26_IMPOSE_ACD", "st.A26P4", "A26.P4;A26.P4.pta;A26.P4.ptb;A26.P4.ptc;A26.P4.ptd;A26.P4.pte;A26.P4.ptf;A26.P1", "pd.CA", "pd.ACD", "authority_control", "competent authority -> authorised CBAM declarant",
   "impose the penalty of paragraph 1 and notify the declarant of the conclusion of non-compliance, the reasons, the amount, the due date, the action to take to pay and the right to appeal",
   "penalty for failure to surrender certificates", "enforcement", "obligation",
   "the competent authority shall impose the penalty pursuant to paragraph 1 or 2 of this Article, as applicable",
   mech="administrative penalty decision with notification", instr="INS-TYPE: penalty decision",
   cond="the competent authority determines, including in light of the Commission's preliminary calculations, that the declarant failed to comply with the obligation to surrender certificates (A26(1))",
   deriv="derived", drule="A26.P4 identifies the competent authority as imposer and the declarant as notified party; the penalty and its trigger are in A26.P1 (internal cross-reference resolved within W).",
   authattr="competent authority imposes the penalty (binding decision)", discattr="the penalty amount follows paragraph 1; no range for discretion is stated for ACD penalties",
   acls="INFO", asuff="indeterminate", amiss="reasons and 'the right ... to appeal' are notified but no appeal forum, assessment capacity or consequence is identified in W",
   deps="pd.CA;pd.ACD", unc="unc.APPEAL_FORUM", hq="hq.ACCOUNT_APPEAL", ext="ext.DIR87_PEN", epi="documented", iunits="A19.P4")
qr("qr.A26_IMPOSE_OTHER", "st.A26P4", "A26.P4;A26.P4.pta;A26.P4.ptb;A26.P4.ptc;A26.P4.ptd;A26.P4.pte;A26.P4.ptf;A26.P2", "pd.CA", "pd.OTHERPERSON", "authority_control", "competent authority -> person other than an authorised CBAM declarant",
   "impose the penalty of paragraph 2 and notify the person of the conclusion of non-compliance, the reasons, the amount, the due date, the action to take to pay and the right to appeal",
   "penalty for introducing goods without complying with the Regulation", "enforcement", "obligation",
   "that a person has introduced goods into the customs territory of the Union without complying with the obligations under this Regulation as set out in paragraph 2 of this Article",
   mech="administrative penalty decision with notification", instr="INS-TYPE: penalty decision",
   cond="the competent authority determines that the person introduced goods into the customs territory of the Union without complying with the obligations under the Regulation (A26(2))",
   deriv="derived", drule="A26.P4 identifies the competent authority as imposer and, 'where paragraph 2 applies', the person as notified party; the penalty and its trigger are in A26.P2 (internal cross-reference resolved within W).",
   authattr="competent authority imposes the penalty (binding decision)", discattr="amount within three to five times the paragraph 1 penalty according to stated factors",
   acls="INFO", asuff="indeterminate", amiss="reasons and the right to appeal are notified but no appeal forum, assessment capacity or consequence is identified in W",
   deps="pd.CA;pd.OTHERPERSON", unc="unc.APPEAL_FORUM", hq="hq.ACCOUNT_APPEAL", ext="ext.DIR87_PEN", epi="documented")
qr("qr.A26_SECURE", "st.A26P5", "A26.P5;A26.P4.ptd", "pd.CA", "pd.ACD", "authority_control", "competent authority -> person liable for the penalty",
   "secure payment of the penalty by all means available under the national law of the Member State concerned where it has not been paid by the due date", "enforcement of unpaid penalties",
   "enforcement", "obligation",
   "the competent authority shall secure payment of that penalty by all means available to it under the national law of the Member State concerned",
   extra="pd.OTHERPERSON", tnote="n-ary: the person liable is either the authorised CBAM declarant (paragraph 1) or the other person (paragraph 2)", mech="recovery by means available under national law",
   cond="the penalty has not been paid by the due date referred to in paragraph 4, point (d)", deriv="direct", authattr="competent authority enforces by national-law means; the means are not specified in W",
   discattr="choice of means left to national law", deps="pd.CA;pd.ACD;pd.OTHERPERSON", ext="ext.NATLAW", gap="The enforcement means are those of national law, outside W.", epi="documented", unc="unc.NATLAW_EXT")
ext("ext.NATLAW", "st.A26P5", "A26.P5", "national law of the Member State concerned (means available to the competent authority to secure payment of penalties)", "other_normative",
    "supplies_rule_or_standard", dependents="qr.A26_SECURE", dep_kind="constitutes", constitutive="Y",
    effect="The means of enforcing payment are those of national law, which is not part of W and is not retrieved; claims about the enforceability of penalties are undetermined within W.")
ext("ext.DIR87_PEN", "st.A26P1;st.A26P2", "A26.P1;A26.P2", "Directive 2003/87/EC, Article 16(3) (excess emissions penalty) and Article 16(4) (increase)", "legal_instrument",
    "supplies_rule_or_standard", dependents="na.A26_LIABLE_ACD;na.A26_LIABLE_OTHER;qr.A26_IMPOSE_ACD;qr.A26_IMPOSE_OTHER", dep_kind="specifies", constitutive="Y",
    effect="The amount of the penalty (and, through paragraph 2, of the higher penalty) is defined by external provisions; the amount is undetermined within W.")
qr("qr.A26_COMM", "st.A26P6", "A26.P6", "pd.MS", "pd.COM", "information_reporting", "Member State -> Commission",
   "communicate the decisions on penalties referred to in paragraphs 1 and 2 to the Commission", "decisions on penalties", "information_provision", "obligation",
   "Member States shall communicate the decisions on penalties referred to in paragraphs 1 and 2 to the Commission",
   mech="communication", cond="decisions on penalties under Article 26(1) and (2)", acls="INFO", asuff="sufficient", authattr="binding duty on Member States", discattr="none stated", deps="pd.MS;pd.COM")
na("na.A26P6_REGISTER", "st.A26P6", "A26.P6", "pd.MS", "register the final payment of penalties in the CBAM registry", "final payment of penalties", "information_provision", "obligation",
   "shall register the final payment referred to in paragraph 5 in the CBAM registry",
   mech="registration in the CBAM registry", instr="pd.REGISTRY", cond="final payment referred to in paragraph 5", nt="N0", eff="duty of Member States to register final payment", notc="no counterparty named for the registration", deriv="direct", deps="pd.MS;pd.REGISTRY")

# =============== ARTICLE 27 ===============
st("st.A27P1", "A27.P1;A27.P3", "assignment_bearing",
   "The Commission shall take action, based on relevant and objective data, to address practices of circumvention of this Regulation, and shall continuously monitor the situation at Union level with a view to identifying such practices, including through market surveillance or any relevant source such as submissions by and reporting from civil society organisations.",
   "The Commission shall take action in accordance with this Article, based on relevant and objective data, to address practices of circumvention of this Regulation.")
st("st.A27P2", "A27.P2;A27.P2.pta;A27.P2.ptb", "definitional",
   "Practices of circumvention are defined as a change in the pattern of trade in goods stemming from a practice, process or work without sufficient due cause or economic justification other than to avoid, wholly or partially, obligations under the Regulation, including slightly modifying goods to fall under CN codes not listed in Annex I or artificially splitting shipments below the Article 2(3) threshold.",
   "Practices of circumvention shall be defined as a change in the pattern of trade in goods")
st("st.A27P4", "A27.P4", "relation_bearing",
   "A Member State or any party affected by, or benefiting from, a circumvention practice may notify the Commission; interested parties other than directly affected or benefited parties, such as environmental organisations and non-governmental organisations, that find concrete evidence may also notify the Commission.",
   "A Member State or any party that has been affected by, or has benefited from, any of the situations referred to in paragraph 2 may notify the Commission")
st("st.A27P5", "A27.P5", "relation_bearing",
   "The notification states reasons and includes relevant data and statistics; the Commission shall initiate an investigation where notified by a Member State or an affected, benefited or other interested party meeting these requirements, or where it determines an investigation is necessary; it may be assisted by competent authorities and customs authorities, shall conclude within nine months from notification and shall notify all competent authorities where an investigation has been initiated.",
   "The Commission shall initiate an investigation into a claim of circumvention either where it has been notified by a Member State, or by an affected, benefited or other interested party")
st("st.A27P6", "A27.P6", "assignment_bearing",
   "Where the Commission has sufficient reasons to believe that slight-modification circumvention is occurring in one or more Member States by way of an established pattern, it is empowered to adopt delegated acts under Article 28 to amend the Annex I list by adding the relevant slightly modified products.",
   "it is empowered to adopt delegated acts in accordance with Article 28 to amend the list of goods in Annex I")
na("na.A27_ACTION", "st.A27P1", "A27.P1;A27.P3", "pd.COM", "take action, based on relevant and objective data, to address practices of circumvention and continuously monitor the situation at Union level with a view to identifying them",
   "practices of circumvention", "monitoring", "obligation",
   "The Commission shall take action in accordance with this Article, based on relevant and objective data, to address practices of circumvention of this Regulation.",
   mech="monitoring, market surveillance, use of submissions from civil society organisations", cond="", nt="N0", eff="duty of the Commission to address and monitor circumvention",
   notc="no addressee of the monitoring is named; civil society organisations appear as an information source, not as a party", deriv="direct", deps="pd.COM")
qr("qr.A27_NOTIFY_MS", "st.A27P4", "A27.P4", "pd.MS", "pd.COM", "information_reporting", "Member State -> Commission",
   "notify the Commission if confronted with practices of circumvention", "notification of circumvention practices", "information_provision", "permission",
   "A Member State or any party that has been affected by, or has benefited from, any of the situations referred to in paragraph 2 may notify the Commission",
   mech="notification (reasons and data per paragraph 5)", cond="the Member State is confronted with practices of circumvention", acls="INFO", asuff="sufficient",
   authattr="permissive; notification triggers the Commission's duty to investigate if A27(5) requirements are met", discattr="the notifier decides whether to notify", deps="pd.MS;pd.COM", iunits="A27.P5")
qr("qr.A27_NOTIFY_AFF", "st.A27P4", "A27.P4", "pd.AFFECTED", "pd.COM", "information_reporting", "party affected by or benefiting from circumvention -> Commission",
   "notify the Commission if confronted with practices of circumvention", "notification of circumvention practices", "information_provision", "permission",
   "A Member State or any party that has been affected by, or has benefited from, any of the situations referred to in paragraph 2 may notify the Commission",
   mech="notification (reasons and data per paragraph 5)", cond="the party has been affected by, or has benefited from, a situation of circumvention", acls="INFO", asuff="sufficient",
   authattr="permissive; notification triggers the Commission's duty to investigate if A27(5) requirements are met", discattr="the notifier decides whether to notify", deps="pd.AFFECTED;pd.COM", iunits="A27.P5")
qr("qr.A27_NOTIFY_INT", "st.A27P4", "A27.P4", "pd.INTERESTED", "pd.COM", "information_reporting", "interested party -> Commission",
   "notify the Commission of practices of circumvention where concrete evidence has been found", "notification of circumvention practices", "information_provision", "permission",
   "Interested parties other than directly affected or benefited parties, such as environmental organisations and non-governmental organisations, which find concrete evidence of practices of circumvention may also notify the Commission.",
   mech="notification (reasons and data per paragraph 5)", cond="the interested party finds concrete evidence of practices of circumvention", acls="INFO", asuff="sufficient",
   authattr="permissive; notification triggers the Commission's duty to investigate if A27(5) requirements are met", discattr="the notifier decides whether to notify", deps="pd.INTERESTED;pd.COM", iunits="A27.P5")
qr("qr.A27_INVESTIGATE", "st.A27P5", "A27.P5", "pd.COM", "pd.AFFECTED", "oversight_supervision", "Commission -> notifying parties (Member State, affected or benefited party, interested party)",
   "initiate an investigation into a claim of circumvention where notified by a Member State or by an affected, benefited or other interested party in a notification that states reasons and includes relevant data and statistics, or where the Commission itself determines an investigation is necessary, and conclude the investigation within nine months from the date of notification",
   "investigation of claims of circumvention", "monitoring", "obligation",
   "The Commission shall initiate an investigation into a claim of circumvention either where it has been notified by a Member State, or by an affected, benefited or other interested party",
   extra="pd.MS;pd.INTERESTED", tnote="n-ary: the notifying parties are the Member State, the affected or benefited party and the other interested party; the investigated conduct belongs to no named position, so no party under investigation is recorded",
   mech="investigation; nine-month limit", cond="notification meeting the requirements of paragraph 5, or the Commission's own determination that an investigation is necessary",
   authattr="the Commission is obliged to initiate where requirements are met and holds the investigation", discattr="the Commission decides whether the requirements are met and whether an own-initiative investigation is 'necessary'",
   deps="pd.COM;pd.AFFECTED;pd.MS;pd.INTERESTED", unc="unc.A27_PARTIES")
qr("qr.A27_ASSIST", "st.A27P5", "A27.P5", "pd.COM", "pd.CA", "information_reporting", "Commission -> competent authorities (and customs authorities)",
   "notify all competent authorities where an investigation has been initiated; may be assisted by the competent authorities and customs authorities in carrying out the investigation",
   "investigations of circumvention", "cooperation_coordination*", "obligation",
   "Where an investigation has been initiated, the Commission shall notify all competent authorities.",
   extra="pd.CUST", tnote="residual function tag; combines a notification duty towards competent authorities with an assistance permission involving competent and customs authorities",
   mech="notification; assistance", cond="an investigation has been initiated; assistance is permissive ('may be assisted')", acls="INFO", asuff="sufficient",
   authattr="binding notification duty; assistance is permissive", discattr="the Commission chooses whether to be assisted", deps="pd.COM;pd.CA;pd.CUST")
na("na.A27P6_DELEG", "st.A27P6", "A27.P6", "pd.COM", "adopt delegated acts to amend the list of goods in Annex I by adding the relevant slightly modified products referred to in paragraph 2, point (a), for anti-circumvention purposes",
   "delegated acts amending Annex I", "rule_making_standard_setting", "competence",
   "it is empowered to adopt delegated acts in accordance with Article 28 to amend the list of goods in Annex I",
   mech="delegated act (Article 28)", instr="INS-TYPE: delegated act",
   cond="the Commission has sufficient reasons to believe, taking into account relevant data, reports and statistics, that circumvention of the kind in paragraph 2, point (a), is occurring in one or more Member States by way of an established pattern",
   nt="N3", eff="competence of the Commission to adopt delegated acts", notc="does not constitute the content of the acts", deriv="direct", deps="pd.COM")
