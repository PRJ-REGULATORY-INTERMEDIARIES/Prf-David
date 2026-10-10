from rgam_lib import *

# =====================================================================
# HUMAN REVIEW QUEUE (machine columns only)
# =====================================================================
hq("hq.NORMTYPE_BUNDLE", "HQ-NORMTYPE", "pd.CBAMCOM;pd.ELECNOM;pd.VERIF;na.A5P4_DEEM;na.A18P1_STATUS",
   "Three provisions state a status or body without an establishing verb: A29(1) ('The Commission shall be assisted by the CBAM Committee. That committee shall be a committee within the meaning of Regulation (EU) No 182/2011'), A5(4) (the person ... 'shall ... be regarded as an authorised CBAM declarant') and A18(1) (any person accredited ... 'shall be an accredited verifier for the purpose of this Regulation'). Are these N1 (direct constitution of the entity or status), N2, N3 or N4, or a deeming/recognition outside N1-N4 that constitutes nothing in the entity itself?",
   "(a) N1: the provision directly constitutes the committee / the deemed status / the verifier status. (b) Deeming or recognition of a status that arises elsewhere (external accreditation, external comitology Regulation), constituting no entity. (c) N0 ordinary norm.",
   "Keep the norm type AMBIGUOUS, record no N1 constitution of any entity, keep epistemic status 'documented' for the positions and the two assignments.",
   "The classification decides whether these positions are 'constituted_by_N1' (legal_constitution_evidenced) or only documented; drafting cues in a translated text are not inferred (RGAM-DR-13).")
hq("hq.NORMTYPE_A17", "HQ-NORMTYPE", "pd.ACD;qr.A17_GRANT",
   "A17(1): 'the competent authority ... shall grant the status of authorised CBAM declarant provided that the criteria ... are complied with'. Is this compound wording (N2/N3 obligation or competence to grant, with N4 condition on the effect of the status) and does the authorised-declarant position become constituted only by the grant decision rather than by the Regulation?",
   "(a) COMPOUND: obligation/competence to grant (N2/N3) with a conditional constitution of the status (N4). (b) N3 competence only. (c) N4 conditional constitution.",
   "Record COMPOUND, constitution 'conditionally_constituted', epistemic 'documented'; no N1 constitution of the position.",
   "The reading determines whether any authorised CBAM declarant position is constituted by the Regulation itself; consequential for position status and for the S AUTH.")
hq("hq.ACCOUNT_APPEAL", "HQ-ACCOUNT", "qr.A17_REFUSE;qr.A17_REVOKE;qr.A19_DECIDE;qr.A26_IMPOSE_ACD;qr.A26_IMPOSE_OTHER;qr.A35_PENALTY",
   "Six decisions of competent authorities must state reasons and give information on the possibility or right to appeal (A17(3), A17(8) third subparagraph, A19(5) third subparagraph, A26(4)(f), A35(5)(e)), but no forum, procedure, questioning or assessment capacity or consequence is identified in W. Is any of these relations ANSWERABILITY, or do they remain INFO with indeterminate sufficiency?",
   "(a) ANSWERABILITY: reasons plus a stated right to appeal constitute a duty to justify towards an affected person with a questioning capacity. (b) INFO with sufficiency indeterminate: no identifiable actor-forum relation. (c) NONE: reasons are ordinary administrative-law content.",
   "Code INFO, sufficiency 'indeterminate', missing elements recorded (forum, assessment capacity, consequences); do not assert accountability.",
   "RGAM-DR-17: an assertion of accountability with no identifiable forum, duty or channel is insufficient evidence for any type; the legal forum is governed by law outside W.")
hq("hq.DIRECTION_A9", "HQ-DIRECTION", "qr.A9_CERT;qr.ANX4_ELEC_CERT",
   "A9(2): 'The information ... shall be certified by a person that is independent from the authorised CBAM declarant' and Annex IV point 5(e): 'the fulfilment of the above criteria is certified by an accredited verifier, who shall receive at least monthly interim reports'. Both sentences are passive on who must obtain the certification and who supplies the reports. Is the origin the authorised CBAM declarant (obligor) with governance direction from the certifier to the declarant's documentation?",
   "(a) origin = authorised CBAM declarant; counterpart = certifier. (b) origin = certifier; counterpart = declarant. (c) not a qualified relation (certification condition only).",
   "Origin = authorised CBAM declarant (grammatical and purposive subject), governance direction from the certifier; keep as a relation of type verification_assurance and mark the direction as a provisional choice.",
   "RGAM-DR-15 direction convention: origin is the legal subject of the statement; the text does not state it.")
hq("hq.EXTDEP_COMITOLOGY", "HQ-EXTDEP", "qr.A29_ASSIST;pd.CBAMCOM;ext.REG182",
   "The control exercised through the examination procedure (A29(2): 'Article 5 of Regulation (EU) No 182/2011 shall apply') is defined outside W. Should the CBAM Committee relation be kept at the nearest relation type (representation_participation) with the substantive control undetermined, or should it be typed as oversight once the external Regulation is consulted by the reviewer?",
   "(a) representation_participation (participation of Member State representatives in the Commission's implementing procedure). (b) oversight_supervision (binding control over draft implementing acts). (c) undetermined.",
   "Keep representation_participation with an explicit type note; the control effect is undetermined within W; ARCH-04 stays INDETERMINATE.",
   "Constitutive dependency on an unresolved external reference (RGAM-DR-20); no external retrieval is authorised (GAP-04).")
hq("hq.EXTDEP_MARKETCOUPLING", "HQ-EXTDEP", "qr.A2P10_DEL;ext.REG2015_1222",
   "A2(10) lets the Commission exclude third countries from 'Union market coupling', a notion defined by reference to Regulation (EU) 2015/1222. Is the relation between the Commission and the third country (authority_control) correctly stated, given that the mechanism of exclusion is external to W?",
   "(a) authority_control as coded. (b) delegation_authorization. (c) not a qualified relation until the external mechanism is known.",
   "Keep as coded, epistemic 'documented' (down-coded), outside the I2 coupling set of ARCH-05.",
   "Constitutive dependency on an unresolved external reference (RGAM-DR-20).")
hq("hq.EXTDEP_ACCRED", "HQ-EXTDEP", "ext.REG2018_2067;ext.REG765_NAB;pd.VERIF;pd.NAB;qr.A8_ENSURE;qr.A10_VERIFY;qr.A18_ACCREDIT;qr.ANX6_PRINC;qr.ANX6_REPORT;qr.ANX4_ELEC_CERT",
   "The status of 'accredited verifier' (A18(1)) and of the 'national accreditation body' (A3(32)) arises from accreditation and appointment under Implementing Regulation (EU) 2018/2067 and Regulation (EC) No 765/2008. May the verifier-related relations be retained at 'documented' with their constitution undetermined, and is ARCH-02 correctly INDETERMINATE?",
   "(a) retain at documented with constitutive dependency recorded. (b) treat the relations as legal_constitution_evidenced because A8(1), A10(5)(b), A18(2) and Annex VI state them directly. (c) drop the verifier relations from S.",
   "Retain at documented; ARCH-02 INDETERMINATE.",
   "Constitutive dependency on an unresolved external reference (RGAM-DR-20, RGAM-DR-25).")
hq("hq.EXTDEP_UCC", "HQ-EXTDEP", "ext.UCC_ORIGIN;ext.UCC_PERSONS;ext.UCC_PROCESSING;ext.UCC_SURVEIL;ext.REG515;pd.CUST;pd.ICR;pd.IMP",
   "The customs authorities, the customs declarant, the indirect customs representative, the customs procedures that trigger special reporting rules, the customs surveillance mechanism and the mutual-assistance regime referred to in A25(5) are constituted or defined by Regulation (EU) No 952/2013 and Regulation (EC) No 515/97, outside W. Is it acceptable to code the relations that name them at 'documented' with the external constitution undetermined, and to code no relation from the 'mutatis mutandis' reference of A25(5)?",
   "(a) as coded. (b) code the customs relations at legal_constitution_evidenced because the roles are stated in A3, A25 and A33. (c) include a mutual-assistance relation derived from A25(5).",
   "Retain at documented where the EXT is listed on the record; no relation is derived from A25(5).",
   "Constitutive dependency on unresolved external references (RGAM-DR-20); no external retrieval (GAP-04).")
hq("hq.EXTDEP_PENALTY", "HQ-EXTDEP", "ext.DIR87_PEN;ext.DIR87_FREE;ext.REG1031;ext.NATLAW;qr.A26_SECURE;na.A26_LIABLE_ACD;na.A26_LIABLE_OTHER;na.A31_ADJUST;na.A21_PRICE",
   "The penalty amount (A26(1)-(2)), the free-allocation adjustment (A31(1)), the price base (A21(1)) and the means of recovery (A26(5)) rest on Directive 2003/87/EC, Regulation (EU) No 1031/2010 and national law. Is it correct to keep the corresponding assignments and relations at 'documented' with the amounts undetermined?",
   "(a) as coded. (b) legal_constitution_evidenced because the existence of the duty is in W and only the amount is external.",
   "Keep 'documented' for the penalty-related assignments; the amount, extent and means are recorded as undetermined in the EXT effect.",
   "Constitutive dependency on unresolved external references for amounts and means (RGAM-DR-20).")
hq("hq.EXTDEP_SCOPE", "HQ-EXTDEP", "ext.REG1186;ext.DELREG2446;ext.REG2658;ext.REG2021_947;ext.UCC_ORIGIN",
   "The de minimis thresholds (A2(3)), the definitions of intrinsic value and military activities, the CN codes of Annex I and the addressee of the A30(8) annual reporting are defined externally. Are the absence-dependent claims that touch them (necessary stage, substitutability) correctly left UNDETERMINED?",
   "(a) UNDETERMINED as coded. (b) ASSERTED_WITHIN_DECLARED_CORPUS because the thresholds only narrow the derogations.",
   "Keep UNDETERMINED.",
   "Absence-dependent claims touching constitutive external dependencies are undetermined or limited to the declared corpus (RGAM-DR-22).")
hq("hq.XREF_BUNDLE", "HQ-XREF", "qr.A2P8_ASSESS;na.A7P7_IMPL;qr.A17_REVOKE",
   "Three internal cross-references are ambiguous: A2(7)(c) refers to 'the conditions set out in points (d) and (e)' (points of the same paragraph, the latter referring back to the roadmap of point (c)); A7(7)(a) refers to evidence 'for the purpose of paragraph 2 that are listed in points 5 and 6 of Annex IV' (points 5 and 6 serve paragraphs 3 and 4 of Article 7); A17(8)(b) refers to 'the criteria set out in paragraph 2 or 6' (paragraph 6 states a guarantee sufficiency condition, not criteria). Which referents are meant?",
   "(a) A2(7)(c): points (d) and (e) of paragraph 7; A7(7)(a): paragraphs 3 and 4; A17(8)(b): the criteria of paragraph 2 and the guarantee condition of paragraph 6. (b) literal readings.",
   "Follow reading (a); the readings do not alter any record's relation type, direction or status.",
   "Internal cross-reference resolved within W with an ambiguity (GAP-03; RGAM-DR-20).")
hq("hq.TEMPORAL", "HQ-OTHER", "arch.TRANSITION;sc.TRANSITION;na.A32_LIMIT;qr.A35_REPORT",
   "The temporal reference was chosen by the executor from the act's own Article 36(2) as 2026-01-01, the date on which all staged application dates have been reached. At that date the transitional regime of Articles 32-35 is bounded (period until 31 December 2025; the Q4 2025 report is still due). Is this reference acceptable, and how should the transitional S be recorded for the reference that the coordinator prefers?",
   "(a) 2026-01-01 as chosen; transitional norms in_force with a validity note. (b) a reference inside the transitional period (2024), at which Articles 5, 10, 14, 16, 17 and the 2026 group would be not_yet_applicable. (c) report the profile for two references.",
   "Keep 2026-01-01; norms of Articles 32-35 recorded in_force with an explicit validity note; no status asserted for other dates.",
   "RGAM-DR-04 requires a declared reference; the choice changes the legal-status profile of the instrument (consequential).")
hq("hq.INTEGRATION_ARCH01", "HQ-INTEGRATION", "arch.LIFECYCLE;sc.AUTH;sc.CERTMKT;sc.ENFORCE",
   "ARCH-01 (authorisation, certificate lifecycle, review and enforcement) is assessed INTEGRATED within the declared corpus on the basis of explicit cross-reference couplings (A16(3), A17(8), A19(5)-(6), A20-A24, A22(3)). Do the couplings meet the I2 warrant and is the I3 consequence (differentiated allocation of decision power) attributable to the whole rather than a re-description of the inventory?",
   "(a) INTEGRATED as assessed. (b) OVERLAPPING_OR_PARTIALLY_INTEGRATED (the authorisation S couples to the rest only through two links). (c) INDETERMINATE.",
   "INTEGRATED within the declared corpus, provisional; the I2/I3 thresholds are unvalidated.",
   "Every INTEGRATED outcome is queued (RGAM-DR-28).")
hq("hq.INTEGRATION_ARCH05", "HQ-INTEGRATION", "arch.SCOPEMGMT;sc.SCOPE",
   "ARCH-05 (third-country listing and conditional electricity exemption) is assessed INTEGRATED on the basis of the conditions of A2(7)-(11), although no listed third country is evidenced (point 2 of Annex III is a placeholder). Is a norm-only arrangement an architecture for the purposes of the S->A warrant?",
   "(a) INTEGRATED as assessed (dependencies are expectations, never gates). (b) INDETERMINATE for lack of any evidenced instance.",
   "INTEGRATED within the declared corpus, provisional.",
   "Every INTEGRATED outcome is queued (RGAM-DR-28).")
hq("hq.OVERLAP_ARCH07", "HQ-OVERLAP", "arch.WHOLE",
   "ARCH-07 (the Regulation as a whole) is assessed OVERLAPPING_OR_PARTIALLY_INTEGRATED: the integrated core overlaps with the delegation, verification and operator S through source-supported references, while the transitional, circumvention and reporting S are not coupled to the core by qualified relations. Is the overlap source-supported and is the outcome appropriate rather than DISTINGUISHABLE or INDETERMINATE?",
   "(a) OVERLAPPING_OR_PARTIALLY_INTEGRATED as assessed. (b) INDETERMINATE (unresolved constitutive external dependencies). (c) SEVERAL_DISTINGUISHABLE.",
   "OVERLAPPING_OR_PARTIALLY_INTEGRATED, provisional.",
   "Every OVERLAPPING outcome is queued (RGAM-DR-28).")
hq("hq.GAP_BUNDLE", "HQ-GAP", "prop.CENT_AUTH;prop.PUBPRIV_VERIF;qr.A12_ASSIST;qr.A28_CONSULT",
   "Protocol gaps encountered and handled conservatively: (1) the mapping of the ten architectural dimensions to the families F1-F5 is not stated in the allowed sources (provisional assignment by listing order); (2) unit conventions for annex tables, annex sections and unnumbered subparagraphs are not stated (GAP-01 convention used and logged); (3) residual function tags used for assignments that fit no listed function (GAP-05); (4) the template's 'six questions' are not operative (GAP-06); (5) relation types applied at the nearest type with a type note (coordination, committee assistance, certification, protective release). Please confirm or correct.",
   "(a) as handled. (b) other family mapping or unit conventions supplied by the coordinator.",
   "Keep the provisional handling; no new vocabulary was created.",
   "RGAM-DR-32: any gap encountered is logged and queued.")

# =====================================================================
# UNCERTAINTY LOG
# =====================================================================
unc("unc.TEMPORAL_REFERENCE", "OTHER", "", "A36.P1;A36.P2;A36.P2.pta;A36.P2.ptb;A32.P0",
    "The temporal reference (2026-01-01) was selected by the executor from the application dates of Article 36(2); the neutral metadata state no repeal-related information. All legal statuses are recorded for that reference only.",
    "All norms recorded in_force at 2026-01-01 with a validity note stating the application group; Articles 32-35 recorded in_force with a note on their bounded scope.",
    "Legal-status profile is reference-dependent; no status is asserted for other dates.", "ESCALATED_TO_HQ")
unc("unc.TRANSITIONAL_TEMPORAL", "OTHER", "", "A32.P0;A35.P1;A36.P2",
    "Articles 32-35 apply to the transitional period 1 October 2023 to 31 December 2025; at the 2026-01-01 reference only the last quarterly report (Q4 2025, due one month after the quarter end under A35(1)) remains due, by arithmetic on dates stated in W.",
    "Recorded in_force with a validity note; epistemic status follows the general rule; no status asserted for later dates.",
    "Relations of Articles 32-35 and ARCH-03.", "ESCALATED_TO_HQ")
unc("unc.A2P8_STATE", "OTHER", "", "ANX3.pt2.P1;A2.P8",
    "Point 2 of Annex III contains only a bracketed placeholder; no third country or territory is listed for the electricity exemption, so the reporting and assessment relations of A2(8) are constituted as norms with no evidenced instance.",
    "Relations recorded with a support-gap report; dependencies are expectations, never gates.", "SC-SCOPE and ARCH-05 hold as norm-level arrangements only.")
unc("unc.A2P10_EXT", "EXTERNAL_DEPENDENCY", "", "A2.P10;A3.P0.pt11",
    "The 'Union market coupling' from which the Commission may exclude third countries is defined by external Regulation (EU) 2015/1222.",
    "Relation recorded as stated; epistemic status down-coded to documented; left out of the I2 set of ARCH-05.", "qr.A2P10_DEL.", "ESCALATED_TO_HQ")
unc("unc.A4_CONVERSE", "DRAFTING_CUE", "", "A4.P0",
    "A4 is worded positively ('only by an authorised CBAM declarant'); it is recorded as a prohibition on persons other than authorised declarants, as the restrictive effect of the exclusivity wording.",
    "Recorded as NA with modality prohibition and constraint_only Y; the reading is stated, not inferred beyond the wording.", "na.A4_PROHIB; HQ not required (A25(1) states the prohibition for customs authorities in terms).")
unc("unc.A6_RECIPIENT", "SOURCE_AMBIGUITY", "", "A6.P1;A6.P3;A6.P4;A6.P5;A9.P1",
    "A6(1), the special reporting rules of A6(3)-(5) and the claim of A9(1) state the declarant's acts without naming the recipient of the CBAM declaration; later provisions attribute review of declarations (A19) but do not say to whom the declaration is addressed.",
    "Recorded as NAs without a counterparty; no counterparty is invented; the review relations of A19 are coded separately.", "The declaration is not coded as a relation to any authority.")
unc("unc.A22_RECIPIENT", "SOURCE_AMBIGUITY", "", "A22.P1",
    "A22(1) states that the declarant shall 'surrender via the CBAM registry' but does not name the recipient of the surrender; the Commission removes surrendered certificates as a registry operation.",
    "Recorded as two NAs (surrender; removal) with no counterparty created.", "No surrender relation is coded.")
unc("unc.A7P5_PURPOSIVE", "OTHER", "", "A7.P5;A10.P6",
    "Record-keeping duties name the verifiers, the Commission and the competent authority as those whom the records are to enable to verify or review (purposive clauses), without stating a communication to them.",
    "Recorded as NAs; the purposive clause is kept in the conditions field; no QR is created from it.", "Relations between record-keepers and reviewers are carried by A8, A19 and A10 instead.")
unc("unc.A8_DIRECTION", "DIRECTION", "", "A8.P1;ANX6.pt1.P1;ANX6.pt2.P1",
    "Textual direction follows the obligor (the declarant ensures verification) while the governance work flows from the verifier to the declarant's declaration; Annex VI states the verifier's duties without naming the verified party (taken by cross-reference to A8(1) and A10(5)(b)).",
    "Both directions recorded (textual and governance); Annex VI relations marked derived with the rule stated.", "qr.A8_ENSURE, qr.ANX6_PRINC, qr.ANX6_REPORT.")
unc("unc.A9_DIRECTION", "DIRECTION", "", "A9.P2;ANX4.pt5.pte",
    "Passive certification sentences do not state who must obtain the certification or supply the interim reports.",
    "Origin assigned to the declarant; governance direction recorded; queued.", "qr.A9_CERT, qr.ANX4_ELEC_CERT.", "ESCALATED_TO_HQ")
unc("unc.ANX4_DEADLINE", "OTHER", "", "ANX4.pt4.3.P3",
    "The Commission's duty to adopt an implementing act by 30 June 2025 falls before the 2026-01-01 reference date; whether the act was adopted is a layer-X fact that is not collected.",
    "Norm recorded in_force with epistemic status documented; fulfilment not assessed.", "na.ANX4_IMPLACT.")
unc("unc.ANX4_ELEC_ADDRESSEE", "SOURCE_AMBIGUITY", "", "ANX4.pt5.P1;ANX4.pt6.P1;ANX4.pt7.P2",
    "Annex IV points 5-7 let declarants apply actual emissions or region-specific values on demonstration without naming the addressee of the demonstration; point 7 uses the plural 'declarants' without defining a position other than the authorised CBAM declarant.",
    "Recorded as permissive NAs of the authorised CBAM declarant; no counterparty created.", "na.ANX4_ELEC_ACTUAL, na.ANX4_IND_ACTUAL, na.ANX4_REGION.")
unc("unc.ANX4_PASSIVE", "DIRECTION", "", "ANX4.pt4.3.P2",
    "The establishment of the alternative default value is stated passively ('shall be established'); the Commission is the recipient of the demonstration and the only default-value setter named in Annex IV.",
    "Relation recorded from the third country to the Commission; establishment not coded as a separate duty.", "qr.ANX4_3C.")
unc("unc.APPEAL_FORUM", "ACCOUNTABILITY_SUFFICIENCY", "", "A17.P3;A17.P8.sub3;A19.P5.sub3;A26.P4.ptf;A35.P5.pte",
    "Reasons and information on a right to appeal are stated without an identified forum, procedure or consequence.",
    "Classified INFO with sufficiency indeterminate; missing elements recorded.", "Accountability profile of SC-AUTH, SC-ENFORCE, SC-TRANSITION.", "ESCALATED_TO_HQ")
unc("unc.CONSULT_EFFECT", "COUPLING_THRESHOLD", "", "A17.P1.sub2;A17.P8.sub2;A28.P5",
    "Consultation provisions do not state the effect of the consultation on the deciding authority or on the Commission.",
    "Coded as representation_participation relations with the effect unspecified.", "Coupling strength of the consultation relations is not inferred.")
unc("unc.DEV_REGISTRY", "DEV_THRESHOLD", "", "A14.P1;A14.P2;A14.P3;A14.P4",
    "The CBAM registry meets identity and operator/governing-rule/bounded-function criteria (device) but is created by an N2 duty of the Commission; its establishment is not evidenced.",
    "Coded DEV, not constituted_by_N1; relations using it carry a support-gap report.", "All relations whose instrument is the registry.")
unc("unc.DEV_PLATFORM", "DEV_THRESHOLD", "", "A20.P2;A20.P3",
    "The common central platform meets the device criteria but is created by an N2 duty of the Commission; its establishment is not evidenced.",
    "Coded DEV, not constituted_by_N1; relations using it carry a support-gap report.", "Relations whose instrument is the platform.")
unc("unc.EXT_POS", "EXTERNAL_DEPENDENCY", "", "A3.P0.pt14;A3.P0.pt32;A5.P1;A32.P0",
    "Positions named by W but constituted or defined externally: customs authorities, indirect customs representative, national accreditation body.",
    "Coded as type-level positions with external dependency recorded; epistemic status documented.", "pd.CUST, pd.ICR, pd.NAB and relations using them.", "ESCALATED_TO_HQ")
unc("unc.N2_DESIG", "OTHER", "", "A11.P1",
    "The competent authority is designated by each Member State under an N2 obligation; no designation is evidenced and the counterpart of the designation relation is a type-level position.",
    "Relation coded with epistemic status documented; the support gap is stated.", "qr.A11_DESIG and all relations whose party is the competent authority.")
unc("unc.NATLAW_EXT", "EXTERNAL_DEPENDENCY", "", "A26.P5",
    "Recovery of unpaid penalties relies on 'all means available ... under the national law of the Member State concerned'.",
    "Relation recorded; means undetermined; national law is not part of W.", "qr.A26_SECURE.", "ESCALATED_TO_HQ")
unc("unc.NT_A17", "DRAFTING_CUE", "", "A17.P1",
    "Compound wording: an obligation to grant with conditions.", "Recorded COMPOUND and queued.", "pd.ACD constitution; qr.A17_GRANT.", "ESCALATED_TO_HQ")
unc("unc.NT_COMMITTEE", "DRAFTING_CUE", "", "A29.P1;A29.P2",
    "The CBAM Committee is named and typed ('a committee within the meaning of Regulation (EU) No 182/2011') without an establishing verb; its effect is defined externally.",
    "Entity not constituted; relation typed at the nearest type.", "pd.CBAMCOM; qr.A29_ASSIST.", "ESCALATED_TO_HQ")
unc("unc.NT_DEEMING", "DRAFTING_CUE", "", "A5.P4",
    "Deeming wording ('shall ... be regarded as an authorised CBAM declarant').", "Recorded AMBIGUOUS and queued.", "na.A5P4_DEEM; pd.ELECNOM.", "ESCALATED_TO_HQ")
unc("unc.NT_VERIF", "DRAFTING_CUE", "", "A18.P1",
    "Recognition wording ('shall be an accredited verifier for the purpose of this Regulation').", "Recorded AMBIGUOUS and queued.", "na.A18P1_STATUS; pd.VERIF.", "ESCALATED_TO_HQ")
unc("unc.UCC_ICR", "EXTERNAL_DEPENDENCY", "", "A5.P1;A5.P2;A32.P0",
    "The indirect customs representative is defined by reference to Article 18 of Regulation (EU) No 952/2013.", "Position coded with external dependency recorded.", "Relations whose party is the indirect customs representative.")
unc("unc.A10_CA_MULTI", "OTHER", "", "A10.P8",
    "A10(8) combines notification, consultation and subsequent information of the competent authorities in three sentences.", "Coded as one relation with the three steps stated.", "qr.A10_DEREG_CA.")
unc("unc.A12_TYPE", "OTHER", "", "A12.P0",
    "Coordination, assistance and guidelines fit none of the ten relation types exactly.", "Coded authority_control with a type note and a residual function tag; no new type created.", "qr.A12_ASSIST.")
unc("unc.A16_PASSIVE", "DIRECTION", "", "A16.P2;A16.P1;A14.P1",
    "A16(2) is passive; the grantor of access is taken to be the Commission through A16(1), A16(3) and A14(1).", "Recorded as derived with the rule stated.", "qr.A16_ACCESS.")
unc("unc.A17P4_PASSIVE", "DIRECTION", "", "A17.P4;A17.P9",
    "A17(4) is passive about who registers the grant decision.", "Taken to be the competent authority; recorded as derived.", "na.A17_REGDEC.")
unc("unc.A20_INSTRUMENT", "OTHER", "", "A20.P1;A20.P4",
    "The platform is the instrument of the sale and not a party; the purchase side (the declarant) is a party and the seller is the Member State.", "Platform recorded as instrument (DEV).", "qr.A20_SELL.")
unc("unc.A23_REQUEST_ADDRESSEE", "SOURCE_AMBIGUITY", "", "A23.P1;A23.P1.sub2",
    "The addressee of the repurchase request is not named in A23(1) second subparagraph.", "Taken to be the Member State where the declarant is established, recorded as derived.", "qr.A23_REQUEST.")
unc("unc.A24_DISPUTE_FORUM", "SOURCE_AMBIGUITY", "", "A24.P0.sub2",
    "The 'pending dispute in a Member State' has no identified forum.", "No forum position is created.", "qr.A24_SUSPEND.")
unc("unc.A26_AMOUNT_EXT", "EXTERNAL_DEPENDENCY", "", "A26.P1;A26.P2",
    "Penalty amounts rest on Article 16(3)-(4) of Directive 2003/87/EC.", "Assignments recorded at documented; amount undetermined.", "na.A26_LIABLE_ACD, na.A26_LIABLE_OTHER.", "ESCALATED_TO_HQ")
unc("unc.A27_PARTIES", "OTHER", "", "A27.P5",
    "The investigated conduct belongs to no named position; the investigation relation is recorded towards the notifying parties.", "No party under investigation is created.", "qr.A27_INVESTIGATE; ARCH-06.")
unc("unc.A28_PASSIVE", "DIRECTION", "", "A28.P1;A28.P2;A28.P3",
    "The conferral clause is passive; the grantors are taken to be the European Parliament and the Council through their opposition and revocation powers.", "Recorded as derived.", "qr.A28_CONFER.")
unc("unc.A30_ASSESS_MS", "OTHER", "", "A30.P6.ptb;A30.P6.ptb.pti;A30.P6.ptb.ptiv",
    "The Commission assesses Member State administration as part of a report to the legislators; the assessment object (Member States) is not the addressee.", "Recorded as an oversight relation with a type note; no corrective power asserted.", "qr.A30_ASSESS_MS.")
unc("unc.A30_STAKEHOLDERS", "OTHER", "", "A30.P1",
    "'Relevant stakeholders' is not a defined category.", "No position or counterparty created.", "na.A30_COLLECT.")
unc("unc.A31_EXT", "EXTERNAL_DEPENDENCY", "", "A31.P1;A31.P2",
    "The extent of free allocation under Article 10a of Directive 2003/87/EC determines the adjustment.", "Assignment recorded at documented; extent undetermined.", "na.A31_ADJUST.")
unc("unc.CBAM_REGIME", "OTHER", "", "A1.P1",
    "The 'CBAM' as the regime established by A1(1) is neither a position nor a device (it has no operator or bounded function of its own); it is not coded as a PD.", "Not coded; the regime is the object of the instrument.", "No record.")
unc("unc.FORMULA_IMAGES", "SOURCE_AMBIGUITY", "", "ANX4.pt2.P2;ANX4.pt2.P5;ANX4.pt3.P2;ANX4.pt3.P4",
    "Four equations of Annex IV are formula images in the source file and cannot be represented as text; the variables are defined in the adjacent legend tables, which are in W.", "Declared as an exclusion in W_DECLARATION; the legend tables are included in st.ANX4METH.", "No record depends on the equation content.")
unc("unc.ANNEX_UNIT_CONVENTION", "PROTOCOL_GAP", "", "ANX1.TBL1;ANX4.pt2.TBL1;ANX3.pt1.pt-1",
    "The data dictionary gives annex point ids but not conventions for goods tables (ANX{n}.TBL{k}), legend tables, unnumbered paragraphs (P{k}) or enumerations without labels (pt-{k}).", "Convention used and logged (GAP-01).", "Unit ids of annex tables and enumerations.", "ESCALATED_TO_HQ")
unc("unc.FAMILY_MAPPING", "PROTOCOL_GAP", "", "A1.P1",
    "The mapping of the ten architectural dimensions to families F1-F5 is not stated in the allowed sources.", "Provisional assignment by listing order; logged.", "PROPERTY_REGISTER.property_family.", "ESCALATED_TO_HQ")

unc("unc.XREF_BUNDLE", "SOURCE_AMBIGUITY", "", "A2.P7.ptc;A7.P7.pta;A17.P8.ptb",
    "Three internal cross-references are ambiguous: A2(7)(c) ('points (d) and (e)'), A7(7)(a) ('paragraph 2 ... points 5 and 6 of Annex IV') and A17(8)(b) ('paragraph 2 or 6').",
    "Resolved within W by the most coherent reading (paragraph 7 points (d)-(e); paragraphs 3 and 4 of Article 7; criteria of paragraph 2 and guarantee condition of paragraph 6) and queued; no record's type, direction or status depends on the choice.",
    "qr.A2P8_ASSESS, na.A7P7_IMPL, qr.A17_REVOKE.", "ESCALATED_TO_HQ")
