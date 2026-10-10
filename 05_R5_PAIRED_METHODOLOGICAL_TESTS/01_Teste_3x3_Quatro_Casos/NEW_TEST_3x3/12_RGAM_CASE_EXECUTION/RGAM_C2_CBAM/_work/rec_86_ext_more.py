from rgam_lib import *

ext("ext.PARIS", "st.A1P1", "A1.P1", "Paris Agreement (goals referred to in the object clause of Article 1(1))", "legal_instrument",
    "other (goals cited in the object clause; the reference shows legal relevance only)", dependents="", dep_kind="qualifies", constitutive="N",
    effect="Cited as a goal supported by the CBAM; no relation or position of W depends on its content for constitution.")
ext("ext.UNFCCC", "st.A2P7", "A2.P7.ptd", "United Nations Framework Convention on Climate Change (communication of a long-term low greenhouse gas emissions development strategy)", "legal_instrument",
    "supplies_rule_or_standard", dependents="", dep_kind="conditions", constitutive="N",
    effect="One of the six exemption conditions refers to a communication to the UNFCCC; the condition is stated in W; the Convention's content is not needed to constitute any relation of W.")
ext("ext.UNIONLAW_ELEC", "st.A2P7", "A2.P7.pta;A2.P7.ptb;A2.P7.pte", "Union law in the field of electricity, renewable energy, energy, environment, competition and climate action, and Union electricity market legislation (as referred to in the exemption conditions)", "other_normative",
    "supplies_rule_or_standard", dependents="qr.A2P8_ASSESS", dep_kind="specifies", constitutive="N",
    effect="Specifies the content that the third country's agreement and domestic legislation must reflect for the exemption; the content of that Union law is not in W; the Commission's assessment relation itself is constituted in W.")
ext("ext.WTO", "st.A30P5", "A30.P5", "World Trade Organization law (compliance of a legislative proposal on export carbon leakage)", "other_normative",
    "supplies_rule_or_standard", dependents="qr.A30_REPORT5", dep_kind="conditions", constitutive="N",
    effect="Condition on the content of a possible legislative proposal; no relation of W depends on it for constitution.")
ext("ext.UN_LDC", "st.A30P2;st.A30P6;st.A30P8", "A30.P2.ptf;A30.P6.pta.ptvii;A30.P8", "United Nations identification of least developed countries (LDCs)", "administrative_act",
    "defines_term", dependents="", dep_kind="specifies", constitutive="N",
    effect="Defines the object of the assessment of effects on developing and least developed countries; no relation of W depends on it for constitution.")
ext("ext.THIRDLAW", "st.A9P2", "A9.P2", "Legislation of the country of origin relating to the carbon price and any rebate or other form of compensation (as referred to in the documentation required for the reduction)", "other_normative",
    "supplies_rule_or_standard", dependents="na.A9_RECORDS;na.A9_REDUCTION", dep_kind="conditions", constitutive="N",
    effect="Determines whether a carbon price was 'effectively paid' and what rebates exist; the third-country legislation is not part of W; the declarant's reduction permission and record-keeping duty are constituted in W.")
