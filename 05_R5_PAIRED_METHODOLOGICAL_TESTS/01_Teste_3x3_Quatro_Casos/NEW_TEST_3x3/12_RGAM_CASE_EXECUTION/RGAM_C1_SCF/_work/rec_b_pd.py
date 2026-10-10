# Authored positions and devices (P)
from reg import *

pd('p_fund', 'DEVICE', 'Social Climate Fund (the ‘Fund’)', 'INSTANCE', 'exactly_one', 'N1', 'constituted_by_N1',
   'legal_constitution_evidenced', ['A1.P1'],
   'This Regulation establishes the Social Climate Fund (the ‘Fund’) for the period from 2026 to 2032',
   inst_src=['A1.P1'],
   devid="Singled out by name ('the Social Climate Fund') and by its establishing norm (A1.P1, direct establishment for 2026-2032).",
   devfn="Operator: implemented by the Commission under direct management (A12.P0). Bounded function: provides financial support to Member States for measures and investments in their Plans (A1.P2, A7.P1). Governing rules: Chapter II-IV and Annexes I-V.",
   devclass='DEV', ind=['A1.P2', 'A7.P1', 'A12.P0', 'A29.P1', 'A29.P2', 'FIN.BIND'],
   sts=['s_a1p1', 's_a1p2', 's_a7p1', 's_a12', 's_a29p1', 's_a29p2', 's_finbind'], unc=['u_fund_origin'])

pd('p_com', 'POSITION', 'the Commission (European Commission)', 'INSTANCE', 'exactly_one', 'NONE', 'not_applicable',
   'documented', ['A4.P1'], 'Each Member State shall submit to the Commission its Plan', inst_src=['A4.P1'],
   sts=['s_a4p1a'])
pd('p_ms', 'POSITION', 'Member State', 'TYPE', 'other (each Member State; 27 Member States named in the Annex II table rows)',
   'NONE', 'not_applicable', 'documented', ['A4.P1'], 'Each Member State shall submit to the Commission its Plan',
   jur=JUR_MS, ind=[f'ANX2.pt{i}' for i in range(6, 33)], sts=['s_a4p1a', 's_anx2'], unc=['u_annex2_inst'])
pd('p_ep', 'POSITION', 'the European Parliament', 'INSTANCE', 'exactly_one', 'NONE', 'not_applicable', 'documented',
   ['A25.P1'], 'simultaneously and on equal terms to the European Parliament and the Council without undue delay',
   inst_src=['A25.P1'], sts=['s_a25p1'])
pd('p_council', 'POSITION', 'the Council', 'INSTANCE', 'exactly_one', 'NONE', 'not_applicable', 'documented',
   ['A25.P1'], 'simultaneously and on equal terms to the European Parliament and the Council without undue delay',
   inst_src=['A25.P1'], sts=['s_a25p1'])
pd('p_epcom', 'POSITION', 'the competent committees of the European Parliament', 'TYPE', 'unspecified', 'NONE',
   'not_applicable', 'documented', ['A25.P3'], 'The competent committees of the European Parliament may invite the Commission',
   sts=['s_a25p3', 's_a26p1'], ind=['A26.P1'])
pd('p_eesc', 'POSITION', 'the European Economic and Social Committee', 'INSTANCE', 'exactly_one', 'NONE',
   'not_applicable', 'documented', ['A27.P1'],
   'the European Economic and Social Committee and the Committee of the Regions with an evaluation report',
   inst_src=['A27.P1'], sts=['s_a27p1a', 's_a27p3'], ind=['A27.P3'])
pd('p_cor', 'POSITION', 'the Committee of the Regions', 'INSTANCE', 'exactly_one', 'NONE', 'not_applicable', 'documented',
   ['A27.P1'], 'the European Economic and Social Committee and the Committee of the Regions with an evaluation report',
   inst_src=['A27.P1'], sts=['s_a27p1a', 's_a27p3'], ind=['A27.P3'])
pd('p_olaf', 'POSITION', 'OLAF', 'INSTANCE', 'exactly_one', 'NONE', 'not_applicable', 'documented', ['A21.P2.pte'],
   'to expressly authorise the Commission, OLAF, the Court of Auditors', inst_src=['A21.P2.pte'],
   sts=['s_a21p2e1', 's_anx3_6b'], ind=['ANX3.pt6.ptb'], unc=['u_ext_bodies'])
pd('p_eca', 'POSITION', 'the Court of Auditors', 'INSTANCE', 'exactly_one', 'NONE', 'not_applicable', 'documented',
   ['A21.P2.pte'], 'to expressly authorise the Commission, OLAF, the Court of Auditors', inst_src=['A21.P2.pte'],
   sts=['s_a21p2e1', 's_anx3_6b'], ind=['ANX3.pt6.ptb'], unc=['u_ext_bodies'])
pd('p_eppo', 'POSITION', 'the EPPO (European Public Prosecutor’s Office)', 'INSTANCE', 'exactly_one', 'NONE',
   'not_applicable', 'documented', ['A21.P2.pte'],
   'in respect of those Member States participating in enhanced cooperation pursuant to Regulation (EU) 2017/1939, the EPPO',
   inst_src=['A21.P2.pte'], sts=['s_a21p2e1', 's_anx3_6b'], ind=['ANX3.pt6.ptb'], unc=['u_ext_bodies'])
pd('p_vh', 'POSITION', 'vulnerable households', 'TYPE', 'unspecified', 'NONE', 'not_applicable', 'documented',
   ['A2.P0.pt10'], '‘vulnerable households’ means households in energy poverty', ind=['A2.P0.pt1', 'A2.P0.pt8'],
   sts=['s_a2_vh', 's_a9p2'], unc=['u_ext_category'])
pd('p_vme', 'POSITION', 'vulnerable micro-enterprises', 'TYPE', 'unspecified', 'NONE', 'not_applicable', 'documented',
   ['A2.P0.pt11'], '‘vulnerable micro-enterprises’ means micro-enterprises that are significantly affected',
   ind=['A2.P0.pt9'], sts=['s_a2_vme', 's_a9p2'], unc=['u_ext_category'])
pd('p_vtu', 'POSITION', 'vulnerable transport users', 'TYPE', 'unspecified', 'NONE', 'not_applicable', 'documented',
   ['A2.P0.pt12'], '‘vulnerable transport users’ means individuals and households in transport poverty',
   ind=['A2.P0.pt2'], sts=['s_a2_vtu', 's_a9p2'])
pd('p_finrec', 'POSITION', 'final recipients of the financial allocations', 'TYPE', 'unspecified', 'NONE',
   'not_applicable', 'documented', ['A21.P2.pte'],
   'to impose obligations on all final recipients of the financial allocations paid for implementing the measures and investments included in the Plan',
   sts=['s_a21p2e2'], unc=['u_recip_overlap'])
pd('p_recip', 'POSITION', 'recipients of support from the Fund', 'TYPE', 'unspecified', 'NONE', 'not_applicable',
   'documented', ['A23.P2'], 'The recipients of support from the Fund shall be informed of the origin of those funds',
   ind=['A24.P3'], sts=['s_a23p2a', 's_a23p2b', 's_a24p3b'], unc=['u_recip_overlap'])
pd('p_implauth', 'POSITION', 'authorities entrusted with the implementation of the Plan (implementing authorities)', 'TYPE',
   'one_or_more', 'N2', 'not_constituted_obligation_only', 'documented', ['ANX3.pt1.pta'],
   'the designation of the authorities entrusted with the implementation of the Plan', jur=JUR_MS,
   ind=['ANX3.pt4.pta'], sts=['s_anx3_1a', 's_anx3_4a', 's_anx3_4b'], unc=['u_unresolved_authorities'])
pd('p_signauth', 'POSITION', 'authority or authorities responsible for signing the management declaration', 'TYPE',
   'one_or_more', 'N2', 'not_constituted_obligation_only', 'documented', ['ANX3.pt1.ptb'],
   'the designation of the authority or authorities responsible for signing the management declaration accompanying the payment requests',
   jur=JUR_MS, ind=['ANX3.pt1.ptc'], sts=['s_anx3_1b', 's_anx3_1c'], unc=['u_unresolved_authorities'])
pd('p_auditbody', 'POSITION', 'body or bodies carrying out audits of systems and operations', 'TYPE', 'one_or_more',
   'N2', 'not_constituted_obligation_only', 'documented', ['ANX3.pt5.pta'],
   'the designation of the body or bodies which will carry out the audits of systems and operations', jur=JUR_MS,
   ind=['ANX3.pt5.ptb', 'ANX3.pt5.ptc'], sts=['s_anx3_5a', 's_anx3_5b'], unc=['u_unresolved_authorities'])
pd('p_manauth', 'POSITION', 'managing authorities of the cohesion policy programmes under Regulation (EU) 2021/1060', 'TYPE',
   'one_or_more', 'NONE', 'not_applicable', 'documented', ['A11.P3'],
   'the managing authorities of the cohesion policy programmes under Regulation (EU) 2021/1060', jur=JUR_MS,
   sts=['s_a11p3a'], unc=['u_manauth_ext'])
pd('p_natauth', 'POSITION', 'national authorities (of the Member State concerned)', 'TYPE', 'unspecified', 'NONE',
   'not_applicable', 'documented', ['A23.P3'], 'joint communication activities with the national authorities',
   jur=JUR_MS, sts=['s_a23p3b'])
pd('p_repoff', 'POSITION', 'representation offices of the European Parliament and of the Commission in the Member State concerned',
   'TYPE', 'unspecified', 'NONE', 'not_applicable', 'documented', ['A23.P3'],
   'the representation offices of the European Parliament and of the Commission in the Member State concerned',
   jur=JUR_MS, sts=['s_a23p3b'])
pd('p_lra', 'POSITION', 'local and regional authorities', 'TYPE', 'unspecified', 'NONE', 'not_applicable', 'documented',
   ['A5.P1'], 'public consultation with local and regional authorities', jur=JUR_MS, sts=['s_a5p1a'])
pd('p_socpart', 'POSITION', 'representatives of economic and social partners', 'TYPE', 'unspecified', 'NONE',
   'not_applicable', 'documented', ['A5.P1'], 'representatives of economic and social partners', jur=JUR_MS,
   sts=['s_a5p1a'])
pd('p_cso', 'POSITION', 'relevant civil society organisations', 'TYPE', 'unspecified', 'NONE', 'not_applicable',
   'documented', ['A5.P1'], 'relevant civil society organisations', jur=JUR_MS, sts=['s_a5p1a'])
pd('p_youth', 'POSITION', 'youth organisations', 'TYPE', 'unspecified', 'NONE', 'not_applicable', 'documented',
   ['A5.P1'], 'youth organisations', jur=JUR_MS, sts=['s_a5p1a'])
pd('p_stake', 'POSITION', 'other stakeholders', 'TYPE', 'unspecified', 'NONE', 'not_applicable', 'documented',
   ['A5.P1'], 'other stakeholders', jur=JUR_MS, sts=['s_a5p1a'], unc=['u_open_category'])
pd('p_perfsys', 'DEVICE', 'performance reporting system of the Commission', 'INSTANCE', 'unspecified', 'NONE',
   'not_applicable', 'documented', ['A24.P3'], 'The performance reporting system of the Commission shall ensure',
   inst_src=['A24.P3'],
   devid="Singled out as 'the performance reporting system of the Commission' (A24.P3); not constituted by this Regulation.",
   devfn="Bounded function: ensures that data for monitoring implementation of activities and results are collected efficiently, effectively and in a timely manner (A24.P3). Operator: the Commission (possessive 'of the Commission'). No governing rules stated within W.",
   devclass='BORDERLINE_INS-TYPE', sts=['s_a24p3a'], unc=['u_perfsys_dev'], hq=['hq_dev_perfsys'])
