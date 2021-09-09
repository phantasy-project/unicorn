# -*- coding: utf-8 -*-

# group of elements

C4_elements = (
"FE_ISRC1:DCH_D0695",
"FE_ISRC1:DCV_D0695",
"FE_SCS1:DCH_D0709",
"FE_SCS1:DCV_D0709",
"FE_SCS1:DCH_D0723",
"FE_SCS1:DCV_D0723",

"FE_LEBT:DCH_D0773",
"FE_LEBT:DCV_D0773",
"FE_LEBT:DCH_D0840",
"FE_LEBT:DCV_D0840",
"FE_LEBT:DCH_D0868",
"FE_LEBT:DCV_D0868",
"FE_LEBT:DCH_D0880",
"FE_LEBT:DCV_D0880",
"FE_LEBT:DCH_D0901",
"FE_LEBT:DCV_D0901",
"FE_LEBT:DCH_D0929",
"FE_LEBT:DCV_D0929",
)

C4S4_elements = (
"FE_LEBT:DCH_D0790",
"FE_LEBT:DCV_D0790",
"FE_LEBT:DCH_D0805",
"FE_LEBT:DCV_D0805",
"FE_LEBT:DCH_D0821",
"FE_LEBT:DCV_D0821",
"FE_LEBT:DCH_D0948",
"FE_LEBT:DCV_D0948",
"FE_LEBT:DCH_D0964",
"FE_LEBT:DCV_D0964",
"FE_LEBT:DCH_D0979",
"FE_LEBT:DCV_D0979",
"FE_LEBT:DCH_D0992",
"FE_LEBT:DCV_D0992",
)

# [i.name for i in lat if i.phy_type == 'Q10']
C9Q10_elements = (
"FE_MEBT:DCH_D1062",
"FE_MEBT:DCV_D1062",
"FE_MEBT:DCH_D1078",
"FE_MEBT:DCV_D1078",
"FE_MEBT:DCH_D1100",
"FE_MEBT:DCV_D1100",
"FE_MEBT:DCH_D1117",
"FE_MEBT:DCV_D1117",
)

# correctors attached to S1 solenoids
# [i.name for i in lat if i.phy_type == 'S1']
C_S1_elements = (
 'LS1_CA01:DCV1_D1132',
 'LS1_CA01:DCH1_D1132',
 'LS1_CA01:DCV2_D1146',
 'LS1_CA01:DCH2_D1146',
 'LS1_CA02:DCV1_D1165',
 'LS1_CA02:DCH1_D1165',
 'LS1_CA02:DCV2_D1180',
 'LS1_CA02:DCH2_D1180',
 'LS1_CA03:DCV1_D1199',
 'LS1_CA03:DCH1_D1199',
 'LS1_CA03:DCV2_D1214',
 'LS1_CA03:DCH2_D1214',
)

# [i.name for i in lat if i.phy_type == 'S2']
C_S2_elements = (
 'LS1_CB01:DCV1_D1235',
 'LS1_CB01:DCH1_D1235',
 'LS1_CB01:DCV2_D1255',
 'LS1_CB01:DCH2_D1255',
 'LS1_CB01:DCV3_D1275',
 'LS1_CB01:DCH3_D1275',
 'LS1_CB02:DCV1_D1299',
 'LS1_CB02:DCH1_D1299',
 'LS1_CB02:DCV2_D1319',
 'LS1_CB02:DCH2_D1319',
 'LS1_CB02:DCV3_D1339',
 'LS1_CB02:DCH3_D1339',
 'LS1_CB03:DCV1_D1363',
 'LS1_CB03:DCH1_D1363',
 'LS1_CB03:DCV2_D1383',
 'LS1_CB03:DCH2_D1383',
 'LS1_CB03:DCV3_D1403',
 'LS1_CB03:DCH3_D1403',
 'LS1_CB04:DCV1_D1426',
 'LS1_CB04:DCH1_D1426',
 'LS1_CB04:DCV2_D1446',
 'LS1_CB04:DCH2_D1446',
 'LS1_CB04:DCV3_D1466',
 'LS1_CB04:DCH3_D1466',
 'LS1_CB05:DCV1_D1490',
 'LS1_CB05:DCH1_D1490',
 'LS1_CB05:DCV2_D1510',
 'LS1_CB05:DCH2_D1510',
 'LS1_CB05:DCV3_D1530',
 'LS1_CB05:DCH3_D1530',
 'LS1_CB06:DCV1_D1554',
 'LS1_CB06:DCH1_D1554',
 'LS1_CB06:DCV2_D1574',
 'LS1_CB06:DCH2_D1574',
 'LS1_CB06:DCV3_D1594',
 'LS1_CB06:DCH3_D1594',
 'LS1_CB07:DCV1_D1618',
 'LS1_CB07:DCH1_D1618',
 'LS1_CB07:DCV2_D1637',
 'LS1_CB07:DCH2_D1637',
 'LS1_CB07:DCV3_D1657',
 'LS1_CB07:DCH3_D1657',
 'LS1_CB08:DCV1_D1681',
 'LS1_CB08:DCH1_D1681',
 'LS1_CB08:DCV2_D1701',
 'LS1_CB08:DCH2_D1701',
 'LS1_CB08:DCV3_D1721',
 'LS1_CB08:DCH3_D1721',
 'LS1_CB09:DCV1_D1745',
 'LS1_CB09:DCH1_D1745',
 'LS1_CB09:DCV2_D1765',
 'LS1_CB09:DCH2_D1765',
 'LS1_CB09:DCV3_D1785',
 'LS1_CB09:DCH3_D1785',
 'LS1_CB10:DCV1_D1809',
 'LS1_CB10:DCH1_D1809',
 'LS1_CB10:DCV2_D1829',
 'LS1_CB10:DCH2_D1829',
 'LS1_CB10:DCV3_D1849',
 'LS1_CB10:DCH3_D1849',
 'LS1_CB11:DCV1_D1872',
 'LS1_CB11:DCH1_D1872',
 'LS1_CB11:DCV2_D1892',
 'LS1_CB11:DCH2_D1892',
 'LS1_CB11:DCV3_D1912',
 'LS1_CB11:DCH3_D1912',
 'LS2_CC01:DCV1_D2723',
 'LS2_CC01:DCH1_D2723',
 'LS2_CC02:DCV1_D2762',
 'LS2_CC02:DCH1_D2762',
 'LS2_CC03:DCV1_D2802',
 'LS2_CC03:DCH1_D2802',
 'LS2_CC04:DCV1_D2842',
 'LS2_CC04:DCH1_D2842',
 'LS2_CC05:DCV1_D2882',
 'LS2_CC05:DCH1_D2882',
 'LS2_CC06:DCV1_D2922',
 'LS2_CC06:DCH1_D2922',
 'LS2_CC07:DCV1_D2961',
 'LS2_CC07:DCH1_D2961',
 'LS2_CC08:DCV1_D3001',
 'LS2_CC08:DCH1_D3001',
 'LS2_CC09:DCV1_D3041',
 'LS2_CC09:DCH1_D3041',
 'LS2_CC10:DCV1_D3081',
 'LS2_CC10:DCH1_D3081',
 'LS2_CC11:DCV1_D3121',
 'LS2_CC11:DCH1_D3121',
 'LS2_CC12:DCV1_D3161',
 'LS2_CC12:DCH1_D3161',
 'LS2_CD01:DCV1_D3211',
 'LS2_CD01:DCH1_D3211',
 'LS2_CD02:DCV1_D3273',
 'LS2_CD02:DCH1_D3273',
 'LS2_CD03:DCV1_D3336',
 'LS2_CD03:DCH1_D3336',
 'LS2_CD04:DCV1_D3398',
 'LS2_CD04:DCH1_D3398',
 'LS2_CD05:DCV1_D3460',
 'LS2_CD05:DCH1_D3460',
 'LS2_CD06:DCV1_D3522',
 'LS2_CD06:DCH1_D3522',
 'LS2_CD07:DCV1_D3584',
 'LS2_CD07:DCH1_D3584',
 'LS2_CD08:DCV1_D3646',
 'LS2_CD08:DCH1_D3646',
 'LS2_CD09:DCV1_D3708',
 'LS2_CD09:DCH1_D3708',
 'LS2_CD10:DCV1_D3770',
 'LS2_CD10:DCH1_D3770',
 'LS2_CD11:DCV1_D3832',
 'LS2_CD11:DCH1_D3832',
 'LS2_CD12:DCV1_D3894',
 'LS2_CD12:DCH1_D3894',
 'LS3_CD01:DCV1_D4358',
 'LS3_CD01:DCH1_D4358',
 'LS3_CD02:DCH1_D4420',
 'LS3_CD02:DCV1_D4420',
 'LS3_CD03:DCV1_D4482',
 'LS3_CD03:DCH1_D4482',
 'LS3_CD04:DCH1_D4544',
 'LS3_CD04:DCV1_D4544',
 'LS3_CD05:DCH1_D4606',
 'LS3_CD05:DCV1_D4606',
 'LS3_CD06:DCH1_D4669',
 'LS3_CD06:DCV1_D4669',
)

# [i.name for i in lat if i.phy_type == 'C2']
C2_elements = (
 'LS1_BTS:DCV_D1937',
 'LS1_BTS:DCH_D1937',
 'LS1_BTS:DCV_D1964',
 'LS1_BTS:DCH_D1964',
 'LS1_BTS:DCV_D1997',
 'LS1_BTS:DCH_D1997',
 'LS1_BTS:DCV_D2024',
 'LS1_BTS:DCH_D2024',
 'LS1_BTS:DCV_D2061',
 'LS1_BTS:DCH_D2061',
 'LS1_BTS:DCV_D2114',
 'LS1_BTS:DCH_D2114',
 'FS1_CSS:DCV_D2189',
 'FS1_CSS:DCH_D2189',
 'FS1_CSS:DCV_D2210',
 'FS1_CSS:DCH_D2210',
 'FS1_CSS:DCV_D2257',
 'FS1_CSS:DCH_D2257',
 'FS1_CSS:DCV_D2276',
 'FS1_CSS:DCH_D2276',
 'FS1_CSS:DCV_D2351',
 'FS1_CSS:DCH_D2351',
 'FS1_CSS:DCV_D2367',
 'FS1_CSS:DCH_D2367',
 'FS1_CSS:DCV_D2381',
 'FS1_CSS:DCH_D2381',
 'FS1_BMS:DCV_D2507',
 'FS1_BMS:DCH_D2507',
 'FS1_BMS:DCV_D2534',
 'FS1_BMS:DCH_D2534',
 'FS1_BMS:DCV_D2584',
 'FS1_BMS:DCH_D2584',
 'FS1_BMS:DCV_D2640',
 'FS1_BMS:DCH_D2640',
 'FS1_BMS:DCV_D2662',
 'FS1_BMS:DCH_D2662',
 'FS1_BMS:DCV_D2688',
 'FS1_BMS:DCH_D2688',
 'FS2_BTS:DCV_D3930',
 'FS2_BTS:DCH_D3930',
 'FS2_BTS:DCV_D3945',
 'FS2_BTS:DCH_D3945',
 'FS2_BTS:DCV_D3962',
 'FS2_BTS:DCH_D3962',
 'FS2_BMS:DCV_D4146',
 'FS2_BMS:DCH_D4146',
 'FS2_BMS:DCV_D4161',
 'FS2_BMS:DCH_D4161',
 'FS2_BMS:DCV_D4213',
 'FS2_BMS:DCH_D4213',
 'FS2_BMS:DCV_D4281',
 'FS2_BMS:DCH_D4281',
 'LS3_BTS:DCH_D4709',
 'LS3_BTS:DCV_D4709',
 'LS3_BTS:DCV_D4750',
 'LS3_BTS:DCH_D4750',
 'LS3_BTS:DCV_D4779',
 'LS3_BTS:DCH_D4779',
 'LS3_BTS:DCH_D4841',
 'LS3_BTS:DCV_D4841',
 'LS3_BTS:DCV_D4903',
 'LS3_BTS:DCH_D4903',
 'LS3_BTS:DCH_D4965',
 'LS3_BTS:DCV_D4965',
 'LS3_BTS:DCH_D5027',
 'LS3_BTS:DCV_D5027',
 'LS3_BTS:DCH_D5089',
 'LS3_BTS:DCV_D5089',
 'LS3_BTS:DCV_D5151',
 'LS3_BTS:DCH_D5151',
 'LS3_BTS:DCV_D5213',
 'LS3_BTS:DCH_D5213',
 'LS3_BTS:DCH_D5275',
 'LS3_BTS:DCV_D5275',
 'LS3_BTS:DCV_D5337',
 'LS3_BTS:DCH_D5337',
 'LS3_BTS:DCH_D5389',
 'LS3_BTS:DCV_D5389',
 'LS3_BTS:DCH_D5428',
 'LS3_BTS:DCV_D5428',
 'BDS_BTS:DCH_D5563',
 'BDS_BTS:DCV_D5563',
)

# [i.name for i in lat if i.phy_type == 'C1']
C1_elements = (
 'FS1_BBS:DCV_D2412',
 'FS1_BBS:DCH_D2412',
 'FS1_BBS:DCV_D2476',
 'FS1_BBS:DCH_D2476',
)

# [i.name for i in lat if i.phy_type in ('SOL_S4', 'SOL_S4b')]
S4_elements = (
"FE_SCS1:SOLR_D0704",
"FE_LEBT:SOLR_D0787",
"FE_LEBT:SOLR_D0802",
"FE_LEBT:SOLR_D0818",
"FE_LEBT:SOLR_D0951",
"FE_LEBT:SOLR_D0967",
"FE_LEBT:SOLR_D0982",
"FE_LEBT:SOLR_D0995",
)

# [i.name for i in lat if i.phy_type == 'SOL_S1']
S1_elements = (
"LS1_CA01:SOL1_D1132",
"LS1_CA01:SOL2_D1146",
"LS1_CA02:SOL1_D1165",
"LS1_CA02:SOL2_D1180",
"LS1_CA03:SOL1_D1199",
"LS1_CA03:SOL2_D1214",
)

# [i.name for i in lat if i.phy_type == 'SOL_S2']
S2_elements = (
 'LS1_CB01:SOL1_D1235',
 'LS1_CB01:SOL2_D1255',
 'LS1_CB01:SOL3_D1275',
 'LS1_CB02:SOL1_D1299',
 'LS1_CB02:SOL2_D1319',
 'LS1_CB02:SOL3_D1339',
 'LS1_CB03:SOL1_D1363',
 'LS1_CB03:SOL2_D1383',
 'LS1_CB03:SOL3_D1403',
 'LS1_CB04:SOL1_D1426',
 'LS1_CB04:SOL2_D1446',
 'LS1_CB04:SOL3_D1466',
 'LS1_CB05:SOL1_D1490',
 'LS1_CB05:SOL2_D1510',
 'LS1_CB05:SOL3_D1530',
 'LS1_CB06:SOL1_D1554',
 'LS1_CB06:SOL2_D1574',
 'LS1_CB06:SOL3_D1594',
 'LS1_CB07:SOL1_D1618',
 'LS1_CB07:SOL2_D1637',
 'LS1_CB07:SOL3_D1657',
 'LS1_CB08:SOL1_D1681',
 'LS1_CB08:SOL2_D1701',
 'LS1_CB08:SOL3_D1721',
 'LS1_CB09:SOL1_D1745',
 'LS1_CB09:SOL2_D1765',
 'LS1_CB09:SOL3_D1785',
 'LS1_CB10:SOL1_D1809',
 'LS1_CB10:SOL2_D1829',
 'LS1_CB10:SOL3_D1849',
 'LS1_CB11:SOL1_D1872',
 'LS1_CB11:SOL2_D1892',
 'LS1_CB11:SOL3_D1912',
 'LS2_CC01:SOL1_D2723',
 'LS2_CC02:SOL1_D2762',
 'LS2_CC03:SOL1_D2802',
 'LS2_CC04:SOL1_D2842',
 'LS2_CC05:SOL1_D2882',
 'LS2_CC06:SOL1_D2922',
 'LS2_CC07:SOL1_D2961',
 'LS2_CC08:SOL1_D3001',
 'LS2_CC09:SOL1_D3041',
 'LS2_CC10:SOL1_D3081',
 'LS2_CC11:SOL1_D3121',
 'LS2_CC12:SOL1_D3161',
 'LS2_CD01:SOL1_D3211',
 'LS2_CD02:SOL1_D3273',
 'LS2_CD03:SOL1_D3336',
 'LS2_CD04:SOL1_D3398',
 'LS2_CD05:SOL1_D3460',
 'LS2_CD06:SOL1_D3522',
 'LS2_CD07:SOL1_D3584',
 'LS2_CD08:SOL1_D3646',
 'LS2_CD09:SOL1_D3708',
 'LS2_CD10:SOL1_D3770',
 'LS2_CD11:SOL1_D3832',
 'LS2_CD12:SOL1_D3894',
 'LS3_CD01:SOL1_D4358',
 'LS3_CD02:SOL1_D4420',
 'LS3_CD03:SOL1_D4482',
 'LS3_CD04:SOL1_D4544',
 'LS3_CD05:SOL1_D4606',
 'LS3_CD06:SOL1_D4669',
)

# [i.name for i in lat if i.phy_type in ('QUAD_Q8', 'QUAD_Q10')]
Q8_elements = (
"FE_MEBT:Q_D1057",
"FE_MEBT:Q_D1062",
"FE_MEBT:Q_D1074",
"FE_MEBT:Q_D1078",
"FE_MEBT:Q_D1095",
"FE_MEBT:Q_D1100",
"FE_MEBT:Q_D1113",
"FE_MEBT:Q_D1117",
)

# [i.name for i in lat if i.phy_type == 'QUAD_Q9']
Q9_elements = (
"FE_MEBT:Q_D1060",
"FE_MEBT:Q_D1076",
"FE_MEBT:Q_D1098",
"FE_MEBT:Q_D1115",
)

# [i.name for i in lat if i.phy_type == 'QUAD_Q1' and i.get_field('B2').polarity == 1]
Q1_elements = (
 'LS1_BTS:QH_D1942',
 'LS1_BTS:QH_D1969',
 'LS1_BTS:QH_D2002',
 'LS1_BTS:QH_D2029',
 'LS1_BTS:QH_D2073',
 'LS1_BTS:QH_D2126',
 'FS1_CSS:QH_D2194',
 'FS1_CSS:QH_D2215',
 'FS1_CSS:QV_D2254',
 'FS1_CSS:QV_D2272',
 'FS1_CSS:QH_D2356',
 'FS1_CSS:QV_D2372',
 'FS1_BTS:Q_D2445',
 'FS1_BMS:QH_D2515',
 'FS1_BMS:QH_D2590',
 'FS1_BMS:QH_D2645',
 'FS1_BMS:QH_D2666',
 'FS1_BMS:QH_D2693',
 'FS2_BTS:QH_D3934',
 'FS2_BTS:QH_D3955',
 # unchecked
 'FS2_BMS:QH_D4151',
 'FS2_BMS:QH_D4172',
 'FS2_BMS:QH_D4218',
 'FS2_BMS:QH_D4286',
 'LS3_BTS:QH_D4718',
 'LS3_BTS:QH_D4760',
 'LS3_BTS:QH_D4783',
 'LS3_BTS:QH_D4845',
 'LS3_BTS:QH_D4907',
 'LS3_BTS:QH_D4969',
 'LS3_BTS:QH_D5031',
 'LS3_BTS:QH_D5093',
 'LS3_BTS:QH_D5155',
 'LS3_BTS:QH_D5218',
 'LS3_BTS:QH_D5280',
 'LS3_BTS:QH_D5342',
 'LS3_BTS:QH_D5393',
 'LS3_BTS:QH_D5432',
 'BDS_BTS:QH_D5471',
 'BDS_BTS:QH_D5509',
 'BDS_BTS:QH_D5559',
 'BDS_BTS:Q_D5599',
)

# (-) Q1_elements
# [i.name for i in lat if i.phy_type == 'QUAD_Q1' and i.get_field('B2').polarity == -1]
Q1_elements_ = (
 'LS1_BTS:QV_D1950',
 'LS1_BTS:QV_D1976',
 'LS1_BTS:QV_D2013',
 'LS1_BTS:QV_D2042',
 'LS1_BTS:QV_D2066',
 'LS1_BTS:QV_D2118',
 'FS1_CSS:QV_D2202',
 'FS1_CSS:QV_D2220',
 'FS1_CSS:QH_D2260',
 'FS1_CSS:QH_D2280',
 'FS1_CSS:QH_D2362',
 'FS1_CSS:QH_D2377',
 'FS1_BTS:Q_D2409',
 'FS1_BTS:Q_D2413',
 'FS1_BMS:QV_D2511',
 'FS1_BMS:QV_D2539',
 'FS1_BMS:QV_D2563',
 'FS1_BMS:QV_D2597',
 'FS1_BMS:QV_D2654',
 'FS1_BMS:QV_D2679',
 'FS1_BMS:QV_D2698',
 'FS2_BTS:QV_D3940',
 'FS2_BTS:QV_D3950',
 # unchecked
 'FS2_BMS:QV_D4156',
 'FS2_BMS:QV_D4166',
 'FS2_BMS:QV_D4226',
 'FS2_BMS:QV_D4296',
 'LS3_BTS:QV_D4713',
 'LS3_BTS:QV_D4755',
 'LS3_BTS:QV_D4806',
 'LS3_BTS:QV_D4868',
 'LS3_BTS:QV_D4930',
 'LS3_BTS:QV_D4992',
 'LS3_BTS:QV_D5054',
 'LS3_BTS:QV_D5116',
 'LS3_BTS:QV_D5178',
 'LS3_BTS:QV_D5240',
 'LS3_BTS:QV_D5302',
 'LS3_BTS:QV_D5364',
 'LS3_BTS:QV_D5408',
 'LS3_BTS:QV_D5440',
 'BDS_BTS:QV_D5479',
 'BDS_BTS:QV_D5501',
 'BDS_BTS:QV_D5552',
)

# Q2
# [i.name for i in lat if i.phy_type == 'QUAD_Q2' and i.get_field('B2').polarity == 1]
Q2_elements = (
'FS1_BTS:Q_D2421',
'FS2_BTS:Q_D4000',
)

# (-) Q2
# [i.name for i in lat if i.phy_type == 'QUAD_Q2' and i.get_field('B2').polarity == -1]
Q2_elements_ = (
'FS1_BTS:Q_D2453',
'BDS_BTS:Q_D5609',
)

# (-) Q3
# [i.name for i in lat if i.phy_type == 'QUAD_Q3'and i.get_field('B2').polarity == -1]
Q3_elements_ = (
'FS2_BTS:Q_D3994',
)

# Q6
# [i.name for i in lat if i.phy_type == 'QUAD_Q6' and i.get_field('B2').polarity == 1]
Q6_elements = (
'FS1_BBS:QH_D2416',
'FS1_BBS:QH_D2472',
)

# [i.name for i in lat if i.phy_type == 'QUAD_Q6' and i.get_field('B2').polarity == -1]
Q6_elements_ = (
'FS1_BBS:QV_D2424',
'FS1_BBS:QV_D2463'
)

# H3
# [i.name for i in lat if i.phy_type == 'H3' and i.get_field('B3').polarity == -1]
H3_elements_ = (
'FS1_BBS:S_D2419',
'FS1_BBS:S_D2469',
)

# H1
# [i.name for i in lat if i.phy_type == 'H1' and i.get_field('B3').polarity == 1]
H1_elements = (
'FS2_BBS:S_D4007',
'FS2_BBS:S_D4098',
)

# (-) H1
# [i.name for i in lat if i.phy_type == 'H1' and i.get_field('B3').polarity == -1]
H1_elements_ = (
'FS2_BBS:S_D4000',
'FS2_BBS:S_D4106',
'BDS_BBS:S_D5606',
'BDS_BBS:S_D5703',
)

# C3
# [i.name for i in lat if i.phy_type == 'C3']
C3_elements = (
 'FS2_BBS:DCV_D4010',
 'FS2_BBS:DCH_D4010',
 'FS2_BBS:DCV_D4055',
 'FS2_BBS:DCH_D4055',
 'FS2_BBS:DCV_D4096',
 'FS2_BBS:DCH_D4096',
 'BDS_BTS:DCV_D5467',
 'BDS_BTS:DCH_D5467',
 'BDS_BTS:DCV_D5496',
 'BDS_BTS:DCH_D5496',
)

# Q4
# [i.name for i in lat if i.phy_type == 'QUAD_Q4']
Q4_elements = (
 'FS2_BBS:QH_D3996',
 'FS2_BBS:QH_D4014',
 'FS2_BBS:QH_D4092',
 'FS2_BBS:QH_D4109',
)

# (-) Q5
# [i.name for i in lat if i.phy_type == 'QUAD_Q5' and i.get_field('B2').polarity == -1]
Q5_elements_ = (
'FS2_BBS:QV_D4004',
'FS2_BBS:QV_D4102',
)

# ARIS
# BEND_FSD1, SCD1
BEND_FSD1_SCD1_elements = (
 'FS_F1S1:DV_D1064',
)
# BEND_FSD1, SCD2
BEND_FSD1_SCD2_elements = (
 'FS_F1S1:DV_D1108',
)

# QUAD_FSQ1, WIQ1
QUAD_FSQ1_elements = (
 'FS_F1S1:Q_D1013',
)

# QUAD_FSQ2, WIQ2,3
QUAD_FSQ2_elements = (
 'FS_F1S1:Q_D1024',
 'FS_F1S1:Q_D1035',
)

# QUAD_FSQ5, WIQ4,5,7
QUAD_FSQ5_elements = (
 'FS_F1S1:Q_D1137',
 'FS_F1S1:Q_D1148',
 'FS_F1S1:Q_D1170',
)

# SEXT_FSQ2, WIQ2,3
SEXT_FSQ2_elements = (
 'FS_F1S1:S_D1024',
 'FS_F1S1:S_D1035',
)

# SEXT_FSQ5, WIQ4,5,7
SEXT_FSQ5_elements = (
 'FS_F1S1:S_D1137',
 'FS_F1S1:S_D1148',
 'FS_F1S1:S_D1170',
)

# OCT_FSQ2, WIQ2,3
OCT_FSQ2_elements = (
 'FS_F1S1:OCT_D1024',
 'FS_F1S1:OCT_D1035',
)

# OCT_FSQ5, WIQ4,5,7
OCT_FSQ5_elements = (
 'FS_F1S1:OCT_D1137',
 'FS_F1S1:OCT_D1148',
 'FS_F1S1:OCT_D1170',
)
