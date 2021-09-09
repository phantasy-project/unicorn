# -*- coding: utf-8 -*-

from fn_utils import flip_data_str_signs
from fn_utils import get_aris_data


# C4
C4_xdata = "0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 5.5 6"
C4_ydata = "2.17E-04 4.34E-04 6.51E-04 8.69E-04 1.09E-03 1.31E-03 1.52E-03 1.74E-03 1.96E-03 2.18E-03 2.40E-03 2.61E-03"

# C1 !!!need data!!! use C4 temporarily
C1_xdata = C4_xdata
C1_ydata = C4_ydata

# C2 !!!need data!!! use C4 temporarily
C2_xdata = C4_xdata
C2_ydata = C4_ydata

# C3 !!!need data!!! use C4 temporarily
C3_xdata = C4_xdata
C3_ydata = C4_ydata

# C4S4
C4S4_xdata = C4_xdata
C4S4_ydata = "1.61E-04 3.23E-04 4.86E-04 6.48E-04 8.10E-04 9.73E-04 1.14E-03 1.30E-03 1.46E-03 1.62E-03 1.79E-03 1.95E-03"

# C9Q10
C9Q10_xdata = "5 10 15 20 25 30 35 40 45"
C9Q10_ydata = "9.10E-04 1.85E-03 2.80E-03 3.77E-03 4.75E-03 5.73E-03 6.71E-03 7.69E-03 8.67E-03"

# C_S1 !!!need data!!! use C9Q10 temporarily
C_S1_xdata = C9Q10_xdata
C_S1_ydata = C9Q10_ydata

# C_S2 !!!need data!!! use C9Q10 temporarily
C_S2_xdata = C9Q10_xdata
C_S2_ydata = C9Q10_ydata

# H3 !!!need data!!! use C9Q10 temporarily
H3_xdata = C9Q10_xdata
H3_ydata = C9Q10_ydata

# H1 !!!need data!!! use H3 temporarily
H1_xdata = H3_xdata
H1_ydata = H3_ydata

# S4
S4_xdata = "20 40 60 80 100 120 140 160 180 200 220 240 260 280 300"
S4_ydata = "-0.0580025822 -0.1161043395 -0.1742150116 -0.2323199102 -0.2904142629 -0.3484930598 -0.4065498774 -0.4645751634 -0.5225515915 -0.5804477477 -0.6381945325 -0.695612072 -0.7522088229 -0.8071705002 -0.8600727249"

# S1 !!!need data!!! use S4 temporarily
S1_xdata = S4_xdata
S1_ydata = S4_ydata

# S2 !!!need data!!! use S4 temporarily
S2_xdata = S4_xdata
S2_ydata = S4_ydata

# Q8
Q8_xdata = "5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105 110 115 120 125 130 135 140 145 150 155 160 165 170 175 180 185 190 195"
Q8_ydata = "7.22E-01 1.4620182 2.2147799 2.9789081 3.74636465 4.5141563 5.2823165 6.0503965 6.818065 7.5852735 8.3515665 9.116546 9.879853 10.641093 11.3996425 12.154415 12.90472 13.6492715 14.387268 15.115826 15.8311425 16.5290995 17.206694 17.853351 18.4489535 18.9707085 19.4555835 19.9028745 20.316784 20.699379 21.0560485 21.387474 21.6947125 21.979232 22.243236 22.490041 22.7214665 22.9390785 23.1430245"

# Q9
Q9_xdata = "5 10 15 20 25 30 35 40 45 50 55 60 65 70 75 80 85 90 95 100 105 110 115 120 125 130 135 140 145 150 155 160 165 170 175 180 185 190 195"
_Q9_ydata = "0.72550564 1.4696342 2.2217468 2.9855075 3.7537958 4.5232289 5.2926941 6.0623996 6.8318876 7.6010907 8.3698891 9.1379508 9.9049769 10.670703 11.434844 12.197023 12.956649 13.712886 14.465165 15.212488 15.954278 16.688388 17.412428 18.12207 18.815421 19.485131 20.125557 20.706961 21.231033 21.718338 22.168227 22.586361 22.98009 23.344792 23.68743 24.006866 24.302281 24.580829 24.840906"
Q9_ydata = flip_data_str_signs(_Q9_ydata)

# Q1 !!!need data!!! use Q8 temporarily
Q1_xdata = Q8_xdata
Q1_ydata = Q8_ydata

Q1_xdata_ = Q1_xdata
Q1_ydata_ = flip_data_str_signs(Q1_ydata)

# Q2 !!!need data!!! use Q8 temporarily
Q2_xdata = Q8_xdata
Q2_ydata = Q8_ydata

Q2_xdata_ = Q2_xdata
Q2_ydata_ = flip_data_str_signs(Q2_ydata)

# Q3 !!!need data!!! use Q8 temporarily
Q3_xdata = Q8_xdata
Q3_ydata = Q8_ydata

# Q4 !!!need data!!! use Q8 temporarily
Q4_xdata = Q8_xdata
Q4_ydata = Q8_ydata

# Q5 !!!need data!!! use Q8 temporarily
Q5_xdata = Q8_xdata
Q5_ydata = Q8_ydata

# Q6 !!!need data!!! use Q8 temporarily
Q6_xdata = Q8_xdata
Q6_ydata = Q8_ydata

Q6_xdata_ = Q6_xdata
Q6_ydata_ = flip_data_str_signs(Q6_ydata)

#ARIS
QUAD_FSQ1_xdata, QUAD_FSQ1_ydata = get_aris_data('QUAD_FSQ1')
QUAD_FSQ2_xdata, QUAD_FSQ2_ydata = get_aris_data('QUAD_FSQ2')
QUAD_FSQ5_xdata, QUAD_FSQ5_ydata = get_aris_data('QUAD_FSQ5')
BEND_FSD1_SCD1_xdata, BEND_FSD1_SCD1_ydata = get_aris_data('BEND_FSD1_SCD1')
BEND_FSD1_SCD2_xdata, BEND_FSD1_SCD2_ydata = get_aris_data('BEND_FSD1_SCD2')
SEXT_FSQ2_xdata, SEXT_FSQ2_ydata = get_aris_data('SEXT_FSQ2')
SEXT_FSQ5_xdata, SEXT_FSQ5_ydata = get_aris_data('SEXT_FSQ5')
OCT_FSQ2_xdata, OCT_FSQ2_ydata = get_aris_data('OCT_FSQ2')
OCT_FSQ5_xdata, OCT_FSQ5_ydata = get_aris_data('OCT_FSQ5')
