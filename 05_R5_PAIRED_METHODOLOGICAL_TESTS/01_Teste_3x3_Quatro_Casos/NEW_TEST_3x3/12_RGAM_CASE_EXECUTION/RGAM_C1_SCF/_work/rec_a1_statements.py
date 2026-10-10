# Authored institutional statements (E) -- part 1: formal elements, Chapters I-II (Articles 1-6)
from reg import *

st('s_title', 'TITLE', 'scope',
   'Title and object clause: the act establishes a Social Climate Fund and amends Regulation (EU) 2021/1060.',
   'establishing a Social Climate Fund and amending Regulation (EU) 2021/1060')
st('s_cit1', 'CIT1', 'external_referencing',
   'Legal basis citation of Treaty articles (formal citation, not an enacted provision).',
   'Having regard to the Treaty on the Functioning of the European Union, and in particular Article 91(1), point (d), Article 192(1) and Article 194(2), and Article 322(1), point (a), thereof')

# ---- Article 1
st('s_a1p1', 'A1.P1', 'device_defining',
   'The Regulation establishes the Social Climate Fund for the period 2026 to 2032.',
   'This Regulation establishes the Social Climate Fund (the ‘Fund’) for the period from 2026 to 2032')
st('s_a1p2', 'A1.P2', 'relation_bearing',
   'The Fund provides financial support to Member States for measures and investments included in their Plans.',
   'The Fund shall provide financial support to Member States for the measures and investments included in their Social Climate Plans (the ‘Plans’)')
st('s_a1p3', 'A1.P3', 'scope',
   'Measures and investments supported by the Fund are to benefit vulnerable households, micro-enterprises and transport users.',
   'The measures and investments supported by the Fund shall benefit households, micro-enterprises and transport users, which are vulnerable and particularly affected by the inclusion of greenhouse gas emissions from buildings and road transport within the scope of Directive 2003/87/EC')

# ---- Article 2 (definitions; GAP-07)
st('s_a2_fa', 'A2.P0.pt4', 'definitional',
   "Definition of 'financial allocation' as non-repayable financial support under the Fund allocated or available to a Member State.",
   '‘financial allocation’ means non-repayable financial support under the Fund that is available for allocation, or that has been allocated, to a Member State')
st('s_a2_mt', ['A2.P0.pt5', 'A2.P0.pt6'], 'definitional',
   "Definitions of 'milestone' (qualitative achievement) and 'target' (quantitative achievement) measuring progress of a measure or investment.",
   '‘milestone’ means a qualitative achievement used to measure progress towards the achievement of a measure or an investment || ‘target’ means a quantitative achievement used to measure progress towards the achievement of a measure or investment')
st('s_a2_etc', 'A2.P0.pt3', 'definitional',
   "Definition of 'estimated total costs of the Plan'.",
   '‘estimated total costs of the Plan’ means the estimated total costs of the measures and investments included in the Plan')
st('s_a2_vh', 'A2.P0.pt10', 'position_defining',
   "Definition of the category 'vulnerable households'.",
   '‘vulnerable households’ means households in energy poverty or households, including low income and lower middle-income ones, that are significantly affected by the price impacts of the inclusion of greenhouse gas emissions from buildings within the scope of Directive 2003/87/EC and lack the means to renovate the building they occupy')
st('s_a2_vme', 'A2.P0.pt11', 'position_defining',
   "Definition of the category 'vulnerable micro-enterprises'.",
   '‘vulnerable micro-enterprises’ means micro-enterprises that are significantly affected by the price impacts of the inclusion of greenhouse gas emissions from buildings or road transport within the scope of Directive 2003/87/EC')
st('s_a2_vtu', 'A2.P0.pt12', 'position_defining',
   "Definition of the category 'vulnerable transport users'.",
   '‘vulnerable transport users’ means individuals and households in transport poverty, but also individuals and households, including low income and lower middle-income ones, that are significantly affected by the price impacts of the inclusion of greenhouse gas emissions from road transport within the scope of Directive 2003/87/EC')
st('s_a2_ext1', ['A2.P0.pt8', 'A2.P0.pt9'], 'external_referencing',
   "Definitions of 'household' and 'micro-enterprise' resting on definitions in other Union instruments.",
   '‘household’ means a private household as defined in Article 2, point (15), of Regulation (EU) 2019/1700 || ‘micro-enterprise’ means an enterprise that employs fewer than 10 persons and whose annual turnover or annual balance sheet does not exceed EUR 2 million, calculated in accordance with Articles 3 to 6 of Annex I to Commission Regulation (EU) No 651/2014')
st('s_a2_ext2', ['A2.P0.pt7', 'A2.P0.pt13', 'A2.P0.pt15', 'A2.P0.pt16', 'A2.P0.pt17', 'A2.P0.pt18', 'A2.P0.pt19'], 'external_referencing',
   'Definitions of energy-related and vehicle terms resting on definitions in other Union instruments.',
   'means energy from renewable sources as defined in Article 2, second subparagraph, point (1), of Directive (EU) 2018/2001 || means an active customer as defined in Article 2, point (8), of Directive (EU) 2019/944 || as defined in Article 3(1), point (m), of Regulation (EU) 2019/631')

# ---- Article 3
st('s_a3p1', 'A3.P1', 'scope',
   'General objective of the Fund: contribute to a socially fair transition towards climate neutrality by addressing social impacts of including buildings and road transport in Directive 2003/87/EC.',
   'The general objective of the Fund shall be to contribute to a socially fair transition towards climate neutrality by addressing the social impacts of the inclusion of greenhouse gas emissions from buildings and road transport within the scope of Directive 2003/87/EC')
st('s_a3p2', 'A3.P2', 'scope',
   'Specific objectives of the Fund: support vulnerable households, micro-enterprises and transport users through temporary direct income support and measures and investments.',
   'The specific objectives of the Fund shall be to support vulnerable households, vulnerable micro-enterprises and vulnerable transport users, through temporary direct income support and through measures and investments')

# ---- Article 4
st('s_a4p1a', 'A4.P1', 'relation_bearing',
   'Each Member State submits its Plan to the Commission.',
   'Each Member State shall submit to the Commission its Plan')
st('s_a4p1b', 'A4.P1', 'assignment_bearing',
   'The Plan contains a coherent set of existing or new national measures and investments addressing carbon-pricing impacts on vulnerable households, micro-enterprises and transport users.',
   'The Plan shall contain a coherent set of existing or new national measures and investments to address the impact of carbon pricing on vulnerable households, vulnerable micro-enterprises and vulnerable transport users')
st('s_a4p2', 'A4.P2', 'assignment_bearing',
   'Each Member State ensures consistency between its Plan and its updated integrated national energy and climate plan under Regulation (EU) 2018/1999.',
   'Each Member State shall ensure consistency between its Plan and its updated integrated national energy and climate plan referred to in Article 14(2) of Regulation (EU) 2018/1999')
st('s_a4p3', 'A4.P3', 'assignment_bearing',
   'The Plan may include national measures providing temporary direct income support to vulnerable households and transport users.',
   'The Plan may include national measures providing temporary direct income support to vulnerable households and vulnerable transport users')
st('s_a4p4', ['A4.P4', 'A4.P4.pta', 'A4.P4.ptb'], 'assignment_bearing',
   'The Plan includes national and, where relevant, local and regional measures and investments in accordance with Article 8 to renovate buildings, decarbonise heating and cooling, and increase zero- and low-emission mobility.',
   'The Plan shall include national and, where relevant, local and regional measures and investments, in accordance with Article 8, to:')
st('s_a4p5', 'A4.P5', 'assignment_bearing',
   'A Member State with an existing national emission trading system or carbon tax may include existing mitigation measures in the Plan if they comply with the Regulation.',
   'the national measures already in place to mitigate social impacts and challenges may be included in the Plan provided that they comply with this Regulation')

# ---- Article 5
st('s_a5p1a', 'A5.P1', 'relation_bearing',
   'Each Member State submits its Plan to the Commission following a public consultation with local and regional authorities, economic and social partners, civil society organisations, youth organisations and other stakeholders.',
   'Each Member State shall submit a Plan to the Commission following a public consultation with local and regional authorities, representatives of economic and social partners, relevant civil society organisations, youth organisations and other stakeholders')
st('s_a5p1b', 'A5.P1', 'procedural',
   "The consultation is conducted in accordance with Article 10 of Regulation (EU) 2018/1999 and the Member State's national legal framework.",
   'Each Member State shall conduct that consultation in accordance with the requirements of Article 10 of Regulation (EU) 2018/1999 and in compliance with that Member State’s national legal framework')
st('s_a5p2', ['A5.P2', 'A5.P2.pta', 'A5.P2.ptb'], 'assignment_bearing',
   'Each Member State includes in its Plan a summary of the consultation held and of how stakeholder input is reflected in the Plan.',
   'Each Member State shall include in its Plan a summary of:')
st('s_a5p3', 'A5.P3', 'relation_bearing',
   'For the purposes of Article 16(3) the Commission assesses whether the Plan was developed in consultation with stakeholders in accordance with paragraph 1.',
   'the Commission shall assess whether the Plan has been developed in consultation with stakeholders in accordance with paragraph 1 of this Article')
st('s_a5p4', 'A5.P4', 'relation_bearing',
   'The Commission supports Member States by providing examples of good practices of consultations on the Plans in accordance with Article 6(4).',
   'The Commission shall support Member States by providing examples of good practices of consultations on the Plans in accordance with Article 6(4)')

# ---- Article 6
st('s_a6p1', ['A6.P1'] + [f'A6.P1.pt{c}' for c in 'abcdefghijklmnopq'], 'assignment_bearing',
   'The Plan sets out listed elements (a) to (q): concrete measures, accompanying measures, financing information, estimates of price effects, identification of vulnerable groups, definitions, criteria for income support, milestones and targets, costs, national contribution, do-no-significant-harm explanation, monitoring arrangements, consultation summary, anti-fraud system explanation, geographic and gender considerations.',
   'The Plan shall set out the following elements:')
st('s_a6p1h', 'A6.P1.pth', 'procedural',
   'The Plan contains envisaged milestones, targets and an indicative timetable for implementation to be completed by 31 July 2032.',
   'envisaged milestones, targets and an indicative comprehensive timetable for the implementation of the measures and investments to be completed by 31 July 2032')
st('s_a6p1m', 'A6.P1.ptm', 'procedural',
   'The Plan contains the arrangements for effective monitoring and implementation, including milestones, targets and the common indicators of Annex IV.',
   'the arrangements for the effective monitoring and implementation of the Plan by the Member State concerned, in particular of the proposed milestones and targets, the relevant common indicators referred to in Annex IV')
st('s_a6p1o', 'A6.P1.pto', 'procedural',
   "The Plan contains an explanation of the Member State's system to prevent, detect and correct fraud, corruption and conflicts of interests and avoid double funding.",
   'an explanation of the Member State’s system to prevent, detect and correct fraud, corruption and conflicts of interests when using the financial allocation provided under the Fund')
st('s_a6p2', 'A6.P2', 'assignment_bearing',
   'The Plan may include technical assistance actions.',
   'The Plan may include technical assistance actions necessary for the effective administration and implementation of the measures and investments')
st('s_a6p3', ['A6.P3'] + [f'A6.P3.pt{c}' for c in 'abcdef'], 'assignment_bearing',
   "The Plan is to be consistent with the information and commitments under six listed plans and programmes (Pillar Action Plan, cohesion programmes, recovery and resilience plan, building renovation plan, integrated national energy and climate plan, territorial just transition plans).",
   'The Plan shall be consistent with the information included in and the commitments made by the Member State under the following:')
st('s_a6p4a', 'A6.P4', 'assignment_bearing',
   'During preparation of the Plans the Commission organises an exchange of good practices.',
   'the Commission shall organise an exchange of good practices, including on cost-effective measures and investments to be included in the Plans')
st('s_a6p4b', 'A6.P4', 'assignment_bearing',
   'Member States may request technical support under the ELENA facility or the Technical Support Instrument.',
   'Member States may request technical support under the European Local ENergy Assistance (ELENA) facility, established by an Agreement between the Commission and the European Investment Bank in 2009, or under the Technical Support Instrument established by Regulation (EU) 2021/240')
st('s_a6p5', 'A6.P5', 'relation_bearing',
   "The Commission provides technical guidance to Member States on compliance of measures and investments with the 'do no significant harm' principle.",
   'the Commission shall provide technical guidance to the Member States, tailored to the scope of the Fund, on the compliance of measures and investments with the principle of ‘do no significant harm’')
st('s_a6p6', 'A6.P6', 'relation_bearing',
   'To assist Member States the Commission provides a common value to be considered as an estimate for the carbon price.',
   'the Commission shall provide a common value to be considered as an estimate for the carbon price resulting from the inclusion of greenhouse gas emissions from buildings, road transport and additional sectors within the scope of Directive 2003/87/EC')
st('s_a6p7', 'A6.P7', 'assignment_bearing',
   'Each Member State uses the template set out in Annex V for the Plan.',
   'Each Member State shall use the template set out in Annex V for the Plan')
