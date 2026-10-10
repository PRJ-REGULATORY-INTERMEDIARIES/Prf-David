# Authored institutional statements (E) -- part 2: Chapter III (Articles 7-21)
from reg import *

# ---- Article 7
st('s_a7p1', 'A7.P1', 'relation_bearing',
   'The Fund provides financial support to Member States to fund the measures and investments set out in their Plans.',
   'The Fund shall provide financial support to Member States to fund the measures and investments set out in their Plans')
st('s_a7p2a', 'A7.P2', 'relation_bearing',
   'Payment of financial support to each Member State is conditional upon that Member State achieving the milestones and targets in accordance with Article 8.',
   'Payment of financial support pursuant to paragraph 1 of this Article to each Member State shall be conditional upon that Member State achieving the milestones and targets for the measures and investments in accordance with Article 8 of this Regulation')
st('s_a7p2b', ['A7.P2'] + [f'A7.P2.pt{c}' for c in 'abcde'], 'assignment_bearing',
   "The milestones and targets are to be compatible with the Union's climate targets and Regulation (EU) 2021/1119 and cover energy efficiency, building renovation, mobility, emission reductions and reductions in vulnerable groups.",
   'Those milestones and targets shall be compatible with the Union’s climate targets and the objective set out in Regulation (EU) 2021/1119, and shall cover in particular:')
st('s_a7p3', 'A7.P3', 'assignment_bearing',
   "The Fund supports only measures and investments complying with the 'do no significant harm' principle of Article 17 of Regulation (EU) 2020/852.",
   'The Fund shall only support measures and investments which comply with the principle of ‘do no significant harm’ within the meaning of Article 17 of Regulation (EU) 2020/852')
st('s_a7p4', 'A7.P4', 'scope',
   'Measures and investments supported by the Fund are to reduce fossil fuel dependency and, where relevant, contribute to the European Pillar of Social Rights and to jobs.',
   'The measures and investments supported by the Fund shall reduce fossil fuel dependency')

# ---- Article 8
st('s_a8p1', ['A8.P1'] + [f'A8.P1.pt{c}' for c in 'abcdefg'], 'assignment_bearing',
   'A Member State may include in the estimated total costs of the Plan listed categories of measures and investments with lasting impacts, provided they principally target vulnerable households, micro-enterprises or transport users.',
   'The Member State may include in the estimated total costs of the Plan the following measures and investments with lasting impacts, provided they principally target vulnerable households, vulnerable micro-enterprises or vulnerable transport users and intend to:')
st('s_a8p1f', 'A8.P1.ptf', 'assignment_bearing',
   'Member States aim to ensure that support to zero-emission vehicles is prioritised in their Plans where affordable and deployable.',
   'Member States shall aim to ensure that where zero-emission vehicles are an affordable and deployable solution, support to such vehicles is prioritised in their Plans')
st('s_a8p2a', 'A8.P2', 'assignment_bearing',
   'Member States may include in the estimated total costs the costs of measures providing direct income support to vulnerable households and transport users; such support is temporary and decreases over time.',
   'Member States may include in the estimated total costs of the Plans the costs of measures providing direct income support to vulnerable households and vulnerable transport users to reduce the impact of the increase in road transport and heating fuel prices')
st('s_a8p2b', 'A8.P2', 'assignment_bearing',
   'Costs of temporary direct income support may not represent more than 37.5 % of the estimated total costs of the Plan.',
   'The costs of measures providing temporary direct income support shall not represent more than 37,5 % of the estimated total costs of the Plan')
st('s_a8p2c', 'A8.P2', 'assignment_bearing',
   'Member States may provide temporary direct income support if their Plans contain measures or investments aimed at the same vulnerable groups under Article 8(1); support is limited to the direct impact of the inclusion of buildings and road transport in the ETS.',
   'Member States may provide temporary direct income support if their Plans contain measures or investments aimed at those vulnerable households and vulnerable transport users in accordance with Article 8(1) of this Regulation')
st('s_a8p3a', 'A8.P3', 'assignment_bearing',
   'Member States may include in the estimated total costs the costs of technical assistance for management of the Fund and achievement of its objectives.',
   'Member States may include in the estimated total costs of the Plans the costs of technical assistance')
st('s_a8p3b', 'A8.P3', 'assignment_bearing',
   'Costs of technical assistance are up to 2.5 % of the estimated total costs of the Plan.',
   'The costs of such technical assistance shall be up to 2,5 % of the estimated total costs of the Plan')

# ---- Article 9
st('s_a9p1', 'A9.P1', 'assignment_bearing',
   'Member States may include in the Plans support provided through public or private entities other than the vulnerable groups, provided those entities carry out measures ultimately benefitting vulnerable households, micro-enterprises or transport users.',
   'Member States may include in the Plans support provided through public or private entities other than vulnerable households, vulnerable micro-enterprises and vulnerable transport users, provided that those entities carry out measures and investments ultimately benefitting vulnerable households, vulnerable micro-enterprises or vulnerable transport users')
st('s_a9p2', 'A9.P2', 'relation_bearing',
   'Member States provide statutory and contractual safeguards to ensure that the entire benefit is passed on to vulnerable households, micro-enterprises or transport users.',
   'Member States shall provide for the necessary statutory and contractual safeguards to ensure that the entire benefit is passed on to the vulnerable households, vulnerable micro-enterprises or vulnerable transport users')

# ---- Article 10
st('s_a10p1a', 'A10.P1', 'scope',
   'A maximum amount of EUR 65 000 000 000 for 2026-2032 is made available, in accordance with Articles 10a(8b), 30d(3) and 30d(4) of Directive 2003/87/EC, for implementation of the Fund; it constitutes external assigned revenue under the Financial Regulation.',
   'A maximum amount of EUR 65 000 000 000 for the period from 1 January 2026 to 31 December 2032 in current prices shall be made available, in accordance with Articles 10a(8b), 30d(3) and 30d(4) of Directive 2003/87/EC, for implementation of the Fund')
st('s_a10p1b', 'A10.P1', 'scope',
   'If the emission trading system under Chapter IVa of Directive 2003/87/EC is postponed until 2028 under Article 30k of that Directive, the maximum amount is EUR 54 600 000 000.',
   'Where the emission trading system established in accordance with Chapter IVa of Directive 2003/87/EC is postponed until 2028 pursuant to Article 30k of that Directive, the maximum amount to be made available to the Fund shall be EUR 54 600 000 000')
st('s_a10p2', 'A10.P2', 'procedural',
   'By derogation from Article 22(2) of the Financial Regulation, commitment appropriations are made available automatically at the start of each financial year from 1 January 2026.',
   'commitment appropriations covering the relevant maximum amount referred to in paragraph 1 of this Article shall be made available automatically at the beginning of each financial year, starting from 1 January 2026')
st('s_a10p3', 'A10.P3', 'assignment_bearing',
   'The amounts may also cover preparatory, monitoring, control, audit, evaluation and other technical and administrative expenses incurred by the Commission for management of the Fund.',
   'all other technical and administrative assistance expenses incurred by the Commission for the management of the Fund')

# ---- Article 11
st('s_a11p1a', 'A11.P1', 'relation_bearing',
   'Resources allocated to Member States under shared management may, at their request, be transferred to the Fund subject to the conditions of Regulation (EU) 2021/1060.',
   'Resources allocated to Member States under shared management may, at their request, be transferred to the Fund subject to the conditions set out in the relevant provisions of Regulation (EU) 2021/1060')
st('s_a11p1b', 'A11.P1', 'assignment_bearing',
   'The Commission implements the transferred resources directly in accordance with Article 62(1), first subparagraph, point (a) of the Financial Regulation.',
   'The Commission shall implement those resources directly in accordance with Article 62(1), first subparagraph, point (a), of Regulation (EU, Euratom) 2018/1046')
st('s_a11p1c', 'A11.P1', 'relation_bearing',
   'The transferred resources are used exclusively for the benefit of the Member State concerned.',
   'Those resources shall be used exclusively for the benefit of the Member State concerned')
st('s_a11p2a', 'A11.P2', 'relation_bearing',
   'Member States may request in their Plans submitted under Article 4(1) the transfer of up to 15 % of their maximum annual financial allocation to funds under shared management under Regulation (EU) 2021/1060.',
   'Member States may request in their Plans submitted in accordance with Article 4(1) of this Regulation for the transfer of up to 15 % of their maximum annual financial allocation to the funds under shared management provided for in Regulation (EU) 2021/1060')
st('s_a11p2b', 'A11.P2', 'procedural',
   'Transferred resources are transferred by Member States through amendment of one or more programmes (excluding Interreg programmes) in accordance with Article 26a of Regulation (EU) 2021/1060 and implemented under the receiving funds rules.',
   'Resources shall be transferred by Member States through the amendment of one or more programmes, except for programmes under the European territorial cooperation goal (Interreg), in accordance with Article 26a of Regulation (EU) 2021/1060')
st('s_a11p3a', 'A11.P3', 'relation_bearing',
   'Member States may entrust the managing authorities of the cohesion policy programmes under Regulation (EU) 2021/1060 with the implementation of measures and investments benefitting from the Fund.',
   'Member States may entrust the managing authorities of the cohesion policy programmes under Regulation (EU) 2021/1060 with the implementation of measures and investments benefitting from the Fund')
st('s_a11p3b', 'A11.P3', 'assignment_bearing',
   'Member States state in their Plans their intention to entrust those authorities.',
   'Member States shall state their intention to thus entrust those authorities in their Plans')
st('s_a11p3c', 'A11.P3', 'procedural',
   'Existing management and control systems of Member States, as notified to the Commission, are deemed to comply with the requirements of the Regulation.',
   'the existing management and control systems put in place by Member States, as notified to the Commission, shall be deemed to comply with the requirements of this Regulation')
st('s_a11p4a', 'A11.P4', 'assignment_bearing',
   'Member States may include in their Plans, as part of the estimated total costs, payments for additional technical support under Regulation (EU) 2021/240 and the cash contribution to the Member State compartment under Regulation (EU) 2021/523.',
   'Member States may include in their Plans, as part of the estimated total costs, the payments for additional technical support pursuant to Article 7 of Regulation (EU) 2021/240 and the amount of the cash contribution for the purpose of the Member State compartment pursuant to the relevant provisions of Regulation (EU) 2021/523')
st('s_a11p4b', 'A11.P4', 'assignment_bearing',
   'Those costs do not exceed 4 % of the maximum financial allocation for the Plan.',
   'Those costs shall not exceed 4 % of the maximum financial allocation for the Plan')

# ---- Article 12
st('s_a12', 'A12.P0', 'assignment_bearing',
   'The Commission implements the Fund under direct management in accordance with rules adopted under Article 322 TFEU, in particular Regulations (EU, Euratom) 2018/1046 and (EU, Euratom) 2020/2092.',
   'The Fund shall be implemented by the Commission under direct management in accordance with the relevant rules adopted pursuant to Article 322 TFEU')

# ---- Article 13
st('s_a13p1', 'A13.P1', 'scope',
   'Support under the Fund is additional to support under other Union funds, programmes and instruments, and may be combined with them if the same cost is not covered.',
   'Support under the Fund shall be additional to the support provided under other Union funds, programmes and instruments')
st('s_a13p2', 'A13.P2', 'scope',
   'Support from the Fund, including temporary direct income support, is additional and does not substitute recurring national budgetary expenditure.',
   'Support from the Fund, including temporary direct income support referred to in Article 4(3), shall be additional and shall not substitute recurring national budgetary expenditure')
st('s_a13p3', 'A13.P3', 'scope',
   'For technical assistance, administrative costs directly linked to implementation of the Plan are not recurring national budgetary expenditure.',
   'administrative costs directly linked to the implementation of the Plan shall not be considered as recurring national budgetary expenditure')

# ---- Article 14
st('s_a14p1', 'A14.P1', 'scope',
   'The maximum financial allocation is calculated for each Member State in accordance with Article 10 and as specified in Annexes I and II.',
   'The maximum financial allocation shall be calculated for each Member State in accordance with Article 10 and as specified in Annexes I and II')
st('s_a14p2', 'A14.P2', 'assignment_bearing',
   'Each Member State may submit a request up to its maximum financial allocation to implement its Plan.',
   'Each Member State may submit a request up to its maximum financial allocation to implement its Plan')

# ---- Article 15
st('s_a15', 'A15.P0', 'assignment_bearing',
   'Member States contribute at least 25 % of the estimated total costs of their Plans.',
   'Member States shall contribute at least to 25 % of the estimated total costs of their Plans')

# ---- Article 16
st('s_a16p1a', 'A16.P1', 'relation_bearing',
   'The Commission assesses the Plan and any amendment submitted under Article 18 for compliance with the Regulation.',
   'The Commission shall assess the Plan and, where applicable, any amendment to that Plan submitted by a Member State in accordance with Article 18, for compliance with this Regulation')
st('s_a16p1b', 'A16.P1', 'relation_bearing',
   'In the assessment the Commission acts in close cooperation with the Member State concerned.',
   'When carrying out that assessment, the Commission shall act in close cooperation with the Member State concerned')
st('s_a16p1c', 'A16.P1', 'relation_bearing',
   'The Commission may make observations or seek additional information within two months from submission of the Plan.',
   'The Commission may make observations or seek additional information within two months from the date of submission of the Plan by the Member State')
st('s_a16p1d1', 'A16.P1', 'relation_bearing',
   'The Member State provides the requested additional information.',
   'The Member State shall provide the requested additional information')
st('s_a16p1d2', 'A16.P1', 'assignment_bearing',
   'The Member State may revise the Plan if needed, including after its submission.',
   'may revise the Plan if needed, including after the submission of the Plan')
st('s_a16p1e', 'A16.P1', 'relation_bearing',
   'The Member State and the Commission may agree to extend the assessment deadline by a reasonable period if necessary.',
   'The Member State and the Commission may agree to extend the deadline for assessment by a reasonable period if necessary')
st('s_a16p2', 'A16.P2', 'relation_bearing',
   'The Commission assesses whether transfers requested in accordance with Article 11 meet the objectives of the Regulation.',
   'The Commission shall assess whether transfers requested in accordance with Article 11 meet the objectives of this Regulation')
st('s_a16p3', ['A16.P3', 'A16.P3.pta', 'A16.P3.pta.pti', 'A16.P3.pta.ptii', 'A16.P3.pta.ptiii', 'A16.P3.ptb', 'A16.P3.ptb.pti',
              'A16.P3.ptb.ptii', 'A16.P3.ptb.ptiii', 'A16.P3.ptb.ptiv', 'A16.P3.ptc', 'A16.P3.ptc.pti', 'A16.P3.ptc.ptii',
              'A16.P3.ptc.ptiii', 'A16.P3.ptd'], 'relation_bearing',
   'The Commission assesses relevance, effectiveness, efficiency and coherence of the Plan against listed criteria, taking account of the challenges and financial allocation of the Member State.',
   'The Commission shall assess the relevance, effectiveness, efficiency and coherence of the Plan, taking into account the specific challenges and the financial allocation of the Member State, as follows:')
st('s_a16_ext1', 'A16.P3.pta.pti', 'external_referencing',
   "Relevance criterion refers to challenges identified in the Commission's assessments under Articles 9(3), 13, 29 and 34 of Regulation (EU) 2018/1999.",
   'challenges identified in the assessments of the Commission of the update of the concerned Member State’s integrated national energy and climate plan and of its progress pursuant to Article 9(3), and Articles 13 and 29 of Regulation (EU) 2018/1999')
st('s_a16_ext2', 'A16.P3.ptb.ptiii', 'external_referencing',
   'Effectiveness criterion refers to compliance with the energy efficiency Directive (recast), Directive (EU) 2018/2001, a Regulation on alternative fuels infrastructure, Directive 2009/33/EC and Directive 2010/31/EU.',
   'consistent and compliant with the requirements of the Directive of the European Parliament and of the Council on energy efficiency (recast), Directive (EU) 2018/2001, the Regulation of the European Parliament and of the Council on the deployment of alternative fuels infrastructure')
st('s_a16_ext3', 'A16.P3.pta.ptii', 'external_referencing',
   'Relevance criterion refers to the do-no-significant-harm objectives of Article 17 of Regulation (EU) 2020/852.',
   'do not significantly harm environmental objectives within the meaning of Article 17 of Regulation (EU) 2020/852')

# ---- Article 17
st('s_a17p1', 'A17.P1', 'relation_bearing',
   'On the basis of the Article 16 assessment, the Commission decides on the Plan of a Member State by implementing act within five months of submission under Article 4(1).',
   'On the basis of the assessment carried out in accordance with Article 16, the Commission shall decide on the Plan of a Member State, by means of an implementing act, no later than five months from the date of the submission of that Plan pursuant to Article 4(1)')
st('s_a17p2', ['A17.P2'] + [f'A17.P2.pt{c}' for c in 'abcdef'], 'relation_bearing',
   'Where the assessment is positive, the implementing act sets out the measures and investments, estimated total costs, milestones and targets, the maximum financial allocation and instalments, the national contribution, monitoring arrangements, indicators and access to data.',
   'Where the Commission gives a positive assessment of a Plan, the implementing act referred to in paragraph 1 shall set out:')
st('s_a17p3a', ['A17.P3', 'A17.P3.pta', 'A17.P3.ptb', 'A17.P3.ptd'], 'relation_bearing',
   'The financial allocation equals the lower of the maximum financial allocation and the estimated total costs minus national contribution where the Plan complies satisfactorily with Article 16(3) criteria; no allocation if it does not.',
   'The maximum financial allocation referred to in paragraph 2, point (b), of this Article shall be determined on the basis of the estimated total costs of the Plan proposed by the Member State, as assessed by reference to the criteria set out in Article 16(3)')
st('s_a17p3c', 'A17.P3.ptc', 'relation_bearing',
   'Where weaknesses in internal control systems are identified, the Commission may require additional measures to be included in the Plan and achieved before the first payment.',
   'the assessment identifies weaknesses in the internal control systems, the Commission may require that additional measures to address those weaknesses be included in the Plan and be achieved by the Member State before the first payment')
st('s_a17p4a', 'A17.P4', 'relation_bearing',
   'Where the assessment is negative, the decision includes the reasons for the negative assessment.',
   'Where the Commission gives a negative assessment of a Plan, the decision referred to in paragraph 1 shall include the reasons for that negative assessment')
st('s_a17p4b', 'A17.P4', 'relation_bearing',
   'The Member State resubmits the Plan after taking into account the Commission assessment.',
   'The Member State shall resubmit the Plan, after taking into account the assessment of the Commission')

# ---- Article 18
st('s_a18p1a', 'A18.P1', 'relation_bearing',
   'A Member State submits an amended Plan to the Commission where the Plan is no longer achievable or needs significant adjustment because of objective circumstances.',
   'the Member State concerned shall submit an amended Plan to the Commission in order to include the necessary and duly justified changes')
st('s_a18p1b', 'A18.P1', 'assignment_bearing',
   'Member States may request technical support in accordance with Article 11(4) for preparing the amended Plan.',
   'Member States may request technical support, in accordance with Article 11(4), for the preparation of the amended Plan')
st('s_a18p2', 'A18.P2', 'relation_bearing',
   'The Commission assesses the amended Plan in accordance with Article 16.',
   'The Commission shall assess the amended Plan in accordance with Article 16')
st('s_a18p3', 'A18.P3', 'relation_bearing',
   'On a positive assessment of an amended Plan the Commission adopts, within three months of submission, a decision by implementing act setting out reasons.',
   'Where the Commission gives a positive assessment of the amended Plan, it shall in accordance with Article 17(1) adopt a decision setting out the reasons for its positive assessment, by means of an implementing act')
st('s_a18p4a', 'A18.P4', 'relation_bearing',
   'On a negative assessment the Commission rejects the amended Plan within the period of paragraph 3.',
   'it shall reject the amended Plan within the period referred to in paragraph 3')
st('s_a18p4b', 'A18.P4', 'relation_bearing',
   'Before rejection the Commission gives the Member State the possibility to present observations within three months of communication of the assessment.',
   'after having given the Member State concerned the possibility to present its observations within three months from the date of the communication of the Commission’s assessment of the amended Plan')
st('s_a18p5a', 'A18.P5', 'assignment_bearing',
   'By 15 March 2029 each Member State assesses the appropriateness of its Plan in view of the actual direct effects of the ETS inclusion of buildings and road transport.',
   'each Member State shall assess the appropriateness of its Plan in view of the actual direct effects of the inclusion of greenhouse gas emissions from buildings and road transport within the scope of Directive 2003/87/EC')
st('s_a18p5b', 'A18.P5', 'relation_bearing',
   'The assessments are submitted to the Commission together with the integrated national energy and climate progress reports under Article 17 of Regulation (EU) 2018/1999.',
   'Those assessments shall be submitted to the Commission together with the integrated national energy and climate progress reports pursuant to Article 17 of Regulation (EU) 2018/1999')
st('s_a18p6', 'A18.P6', 'relation_bearing',
   'Minor adjustments (below 5 % of a target) and clerical corrections are notified by the Member State to the Commission.',
   'a Member State shall notify such changes to the Commission')

# ---- Article 19
st('s_a19p1', 'A19.P1', 'relation_bearing',
   'After a positive decision under Article 17 the Commission concludes with the Member State an agreement constituting an individual legal commitment under the Financial Regulation for 2026-2032.',
   'it shall in due time conclude an agreement with the Member State concerned constituting an individual legal commitment within the meaning of Regulation (EU, Euratom) 2018/1046 for the period 2026-2032')
st('s_a19p2', 'A19.P2', 'procedural',
   'Budgetary commitments may be based on global commitments and broken down into annual instalments.',
   'Budgetary commitments may be based on global commitments and, where appropriate, may be broken down into annual instalments spread over several years')

# ---- Article 20
st('s_a20p1a', 'A20.P1', 'relation_bearing',
   'Payments of financial allocations to the Member State are made upon achievement of the agreed milestones and targets as approved under Article 17, subject to availability of funding.',
   'Payments of financial allocations under this Article to the Member State shall be made upon achievement of the relevant agreed milestones and targets indicated in the Plan, as approved in accordance with Article 17, and subject to the availability of funding')
st('s_a20p1b', 'A20.P1', 'relation_bearing',
   'Upon achievement the Member State submits to the Commission a duly reasoned payment request once or twice a year, by 31 July or 31 December.',
   'Upon such achievement, the Member State shall submit to the Commission a duly reasoned payment request')
st('s_a20p2', 'A20.P2', 'relation_bearing',
   'Upon receiving a payment request the Commission assesses whether the milestones and targets set in the Article 17 decision have been satisfactorily achieved.',
   'Upon receiving a payment request from a Member State, the Commission shall assess whether the relevant milestones and targets set out in the Commission decision referred to in Article 17 have been satisfactorily achieved')
st('s_a20p3', 'A20.P3', 'relation_bearing',
   'On a positive assessment of a payment request the Commission adopts an individual decision authorising disbursement in accordance with the Financial Regulation, subject to availability of funding and equal treatment of Member States, within two to three months after the deadline.',
   'Where the Commission makes a positive assessment of an individual payment request, it shall adopt an individual decision authorising the disbursement of the financial allocation in accordance with Regulation (EU, Euratom) 2018/1046, subject to the availability of funding and ensuring the equal treatment of Member States')
st('s_a20p4a', 'A20.P4', 'relation_bearing',
   'Where milestones and targets are not satisfactorily achieved, payment of the proportional part of the financial allocation is suspended until they are achieved.',
   'the payment of the part of the financial allocation proportional to the unachieved target or milestone shall be suspended')
st('s_a20p4b', 'A20.P4', 'relation_bearing',
   'The Member State may present observations within one month of the communication of the Commission assessment.',
   'The Member State may present its observations within one month of the communication of the Commission’s assessment')
st('s_a20p5', 'A20.P5', 'procedural',
   'By derogation from Article 116(2) of the Financial Regulation the payment deadline runs from communication of the disbursement decision or of the lifting of a suspension.',
   'By way of derogation from Article 116(2) of Regulation (EU, Euratom) 2018/1046, the payment deadline shall start running from the date of the communication of the Commission’s decision authorising the disbursement')
st('s_a20p6', 'A20.P6', 'relation_bearing',
   'If milestones and targets are not satisfactorily achieved within nine months of suspension, the Commission reduces the financial allocation proportionately after giving the Member State the possibility to present observations within two months.',
   'the Commission shall reduce the amount of the financial allocation proportionately after having given the Member State the possibility to present its observations within two months from the communication of its conclusions')
st('s_a20p7a', 'A20.P7', 'relation_bearing',
   'If no tangible progress is made within 15 months of conclusion of the agreements, the Commission terminates the agreements and decommits the allocation.',
   'the Commission shall terminate those agreements and shall decommit the amount of the financial allocation without prejudice to Article 14(3) of Regulation (EU, Euratom) 2018/1046')
st('s_a20p7b', 'A20.P7', 'relation_bearing',
   'The termination decision is taken after the Member State has had the possibility to present observations within two months of the Commission assessment of no tangible progress.',
   'The Commission shall take a decision on the termination of those agreements after having given the Member State the possibility to present its observations within a period of two months of the communication of the assessment by the Commission that no tangible progress has been made')
st('s_a20p8', 'A20.P8', 'procedural',
   'All payments are made by 31 December 2033.',
   'All payments shall be made by 31 December 2033')
st('s_a20p9', 'A20.P9', 'relation_bearing',
   'If assigned revenue is insufficient to cover payment requests in a round, the Commission pays Member States pro rata and gives priority to delayed payments in the next round.',
   'the Commission shall pay the Member States on a pro-rata basis determined as a share of the payment availabilities to the total approved payments')
st('s_a20p10', 'A20.P10', 'relation_bearing',
   'The Commission allocates to Member States amounts corresponding to appropriations unused by 31 December 2033 in accordance with distribution rules under Article 30d(5) of Directive 2003/87/EC.',
   'the Commission shall allocate to Member States the amounts corresponding to any appropriations that are unused by 31 December 2033 in accordance with the rules for distribution of allowances defined under Article 30d(5) of Directive 2003/87/EC')

# ---- Article 21
st('s_a21p1a', 'A21.P1', 'assignment_bearing',
   'Member States, as beneficiaries of Fund funds, take all appropriate measures to protect the financial interests of the Union and ensure use of financial allocations complies with applicable Union and national law.',
   'The Member States, when implementing the Plans, as beneficiaries of funds under the Fund, shall take all the appropriate measures to protect the financial interests of the Union')
st('s_a21p1b1', 'A21.P1', 'assignment_bearing',
   'Member States provide an effective and efficient internal control system as further set out in Annex III.',
   'the Member States shall provide an effective and efficient internal control system as further set out in Annex III')
st('s_a21p1b2', 'A21.P1', 'assignment_bearing',
   'Member States provide for the recovery of amounts wrongly paid or incorrectly used.',
   'the recovery of amounts wrongly paid or incorrectly used')
st('s_a21p1c', 'A21.P1', 'assignment_bearing',
   'Member States may rely on their regular national budget management systems.',
   'Member States may rely on their regular national budget management systems')
st('s_a21p2', 'A21.P2', 'procedural',
   'The Article 19 agreements provide for listed obligations of Member States.',
   'The agreements referred to in Article 19 shall provide for the following obligations of the Member States:')
st('s_a21p2a', 'A21.P2.pta', 'assignment_bearing',
   'Obligation of Member States to regularly check that the financing has been properly used and measures properly implemented.',
   'to regularly check that the financing provided has been properly used in accordance with all applicable rules')
st('s_a21p2b', 'A21.P2.ptb', 'assignment_bearing',
   'Obligation of Member States to take measures to prevent, detect and correct fraud, corruption and conflicts of interests and to take legal action to recover misappropriated funds.',
   'to take appropriate measures to prevent, detect and correct fraud, corruption, and conflicts of interests as defined in Article 61 of Regulation (EU, Euratom) 2018/1046')
st('s_a21p2c', ['A21.P2.ptc', 'A21.P2.ptc.pti', 'A21.P2.ptc.ptii'], 'relation_bearing',
   'Obligation of Member States to accompany a payment request by a management declaration and a summary of audits.',
   'to accompany a payment request by: || a management declaration that the financial allocations were used for its intended purpose || a summary of the audits carried out in accordance with internationally accepted audit standards')
st('s_a21p2d', ['A21.P2.ptd', 'A21.P2.ptd.pti', 'A21.P2.ptd.ptii', 'A21.P2.ptd.ptiii', 'A21.P2.ptd.ptiv'], 'assignment_bearing',
   'Obligation of Member States to collect, record and store in an electronic system and ensure access to standardised data categories (final recipients, contractors and subcontractors, beneficial owners, list of measures and investments).',
   'to collect, record and store in an electronic system and ensure access to the following standardised categories of data:')
st('s_a21p2e1', 'A21.P2.pte', 'relation_bearing',
   'Obligation of Member States to expressly authorise the Commission, OLAF, the Court of Auditors and, for participating Member States, the EPPO, to exert their rights under Article 129(1) of the Financial Regulation.',
   'to expressly authorise the Commission, OLAF, the Court of Auditors and, in respect of those Member States participating in enhanced cooperation pursuant to Regulation (EU) 2017/1939, the EPPO, to exert their rights as provided for in Article 129(1) of Regulation (EU, Euratom) 2018/1046')
st('s_a21p2e2', 'A21.P2.pte', 'relation_bearing',
   'Obligation of Member States to impose obligations on all final recipients and other persons or entities involved in implementation to expressly authorise the same bodies and impose similar obligations.',
   'to impose obligations on all final recipients of the financial allocations paid for implementing the measures and investments included in the Plan')
st('s_a21p2f', 'A21.P2.ptf', 'assignment_bearing',
   'Obligation of Member States to keep records in accordance with Article 132 of the Financial Regulation.',
   'to keep records in accordance with Article 132 of Regulation (EU, Euratom) 2018/1046')
st('s_a21p2g', ['A21.P2.cont1', 'A21.P2.cont1.pta', 'A21.P2.cont1.ptb', 'A21.P2.cont1.ptc'], 'procedural',
   'Contractor and subcontractor information is required only above the Union procurement thresholds of Directive 2014/24/EU and, for subcontractors, only at first level, where recorded and above EUR 50 000.',
   'The information referred to in point (d)(ii) of the first subparagraph of this Article shall be required only where the value of public procurement is greater than the Union thresholds set out in Article 4 of Directive 2014/24/EU')
st('s_a21p3a', 'A21.P3', 'assignment_bearing',
   'Personal data are processed by Member States and by the Commission for discharge, audit and control proceedings and information, communication and visibility activities, in accordance with Regulations (EU) 2016/679 or (EU) 2018/1725.',
   'Personal data as referred to in paragraph 2, point (d), of this Article shall be processed by Member States and by the Commission for the purpose, and corresponding duration, of discharge, audit and control proceedings, and information, communication and visibility activities')
st('s_a21p3b', 'A21.P3', 'assignment_bearing',
   'In the discharge procedure under Article 319 TFEU the Fund is subject to reporting under the integrated financial and accountability reporting of Article 247 of the Financial Regulation, separately in the annual management and performance report.',
   'the Fund shall be subject to reporting under the integrated financial and accountability reporting referred to in Article 247 of Regulation (EU, Euratom) 2018/1046')
st('s_a21p4a', 'A21.P4', 'relation_bearing',
   'The Article 19 agreements provide for the right of the Commission to reduce proportionately the support and recover amounts due, in cases of uncorrected fraud, corruption or conflict of interests or serious breach of an obligation; the Commission respects proportionality.',
   'The agreements referred to in Article 19 shall also provide for the right of the Commission to reduce proportionately the support under the Fund and recover any amount due to the Union budget')
st('s_a21p4b', 'A21.P4', 'relation_bearing',
   'The Commission gives the Member State the opportunity to present observations before the reduction is made.',
   'The Commission shall give the Member State the opportunity to present its observations before the reduction is made')
