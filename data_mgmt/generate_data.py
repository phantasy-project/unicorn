# -*- coding: utf-8 -*-

from fn_utils import make_fn_name, make_fn_desc
from fn_utils import make_row, flip_data_str_signs
from fn_utils import write_row

from fn_data import C1_xdata, C1_ydata
from fn_data import C2_xdata, C2_ydata
from fn_data import C4_xdata, C4_ydata
from fn_data import C4S4_xdata, C4S4_ydata
from fn_data import C9Q10_xdata, C9Q10_ydata
from fn_data import C_S1_xdata, C_S1_ydata
from fn_data import C_S2_xdata, C_S2_ydata

from fn_data import S1_xdata, S1_ydata
from fn_data import S2_xdata, S2_ydata
from fn_data import S4_xdata, S4_ydata

from fn_data import H3_xdata, H3_ydata

from fn_data import Q1_xdata, Q1_ydata
from fn_data import Q1_xdata_, Q1_ydata_
from fn_data import Q2_xdata, Q2_ydata
from fn_data import Q2_xdata_, Q2_ydata_
from fn_data import Q3_xdata, Q3_ydata
from fn_data import Q6_xdata, Q6_ydata
from fn_data import Q6_xdata_, Q6_ydata_
from fn_data import Q8_xdata, Q8_ydata
from fn_data import Q9_xdata, Q9_ydata

from fn_templates import fn_prop, fn_prop_reversed
from fn_templates import fn_quad, fn_quad_reversed, fn_quad_

from fn_egroups import C1_elements, C2_elements, C4_elements, C4S4_elements, \
                       C_S1_elements, C_S2_elements, C9Q10_elements

from fn_egroups import Q1_elements, Q1_elements_, Q2_elements, Q2_elements_, Q3_elements, \
                       Q6_elements, Q6_elements_, Q8_elements, Q9_elements

from fn_egroups import S1_elements, S2_elements, S4_elements

from fn_egroups import H3_elements


def make_rows_COR_SOL(ename, k, xdata, ydata,
                      params="x,k", phy_field="TM", eng_field="I",
                      dtype="COR", **kws):
    #
    # make rows for correctors and solenoieds
    # key argu: k_ to define "-" k if not -k.
    # for cor:
    #   k,(x,y)data are defined for 'V',
    #   'H' data could be got by flipping the signs.
    #
    if 'DCH' in ename and dtype == "COR":
        k = kws.get('k_', -k)
        ydata = flip_data_str_signs(ydata)
    code_e2p = fn_prop.format(k=k)
    code_p2e = fn_prop_reversed.format(k=k)
    row_e2p = make_row(ename, phy_field, eng_field, False,
                       code_e2p, params, xdata, ydata, **kws)
    row_p2e = make_row(ename, phy_field, eng_field, True,
                       code_p2e, params, ydata, xdata, **kws)
    return [row_e2p, row_p2e]


def make_rows_QUAD(ename, xdata, ydata,
                   params="x,x1,a1,b1,c1,a2,b2,c2",
                   phy_field="B2", eng_field="I", **kws):
    #
    # make rows for quads
    #
    x1 = kws.pop('x1')
    x1r = kws.pop('x1r')
    a1 = kws.pop('a1')
    b1 = kws.pop('b1')
    c1 = kws.pop('c1')
    a2 = kws.pop('a2')
    b2 = kws.pop('b2')
    c2 = kws.pop('c2')
    polarity = kws.pop('polarity', 1)
    if polarity == 1:
        code_e2p = fn_quad.format(x1=x1, a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2)
    else:
        code_e2p = fn_quad_.format(x1=x1, a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2)
    row_e2p = make_row(ename, phy_field, eng_field, False,
                       code_e2p, params, xdata, ydata, **kws)
    if x1r is None:
        row_p2e = None
    else:
        code_p2e = fn_quad_reversed.format(x1=x1r, a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2)
        row_p2e = make_row(ename, phy_field, eng_field, True,
                           code_p2e, params, ydata, xdata, **kws)
    return [row_e2p, row_p2e]


##############################################################################

all_rows = []
COLOR_COR = "light_yellow"
COLOR_SOL = "light_turquoise"
COLOR_QUAD = "light_orange"
COLOR_SEXT = 'teal'

###

k_C1 = 4.835e-5
for e in C1_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_C1, xdata=C1_xdata, ydata=C1_ydata, color=COLOR_COR))

k_C2 = 4.232e-4
k_C2_ = -1.970e-4
for e in C2_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_C2, xdata=C2_xdata, ydata=C2_ydata, color=COLOR_COR,
                                      k_=k_C2_))

k_C4 = 3.484e-4
for e in C4_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_C4, xdata=C4_xdata, ydata=C4_ydata, color=COLOR_COR))

k_C4S4 = 2.598e-4
for e in C4S4_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_C4S4, xdata=C4S4_xdata, ydata=C4S4_ydata, color=COLOR_COR))

k_C9Q10 = 0.950e-4
for e in C9Q10_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_C9Q10, xdata=C9Q10_xdata, ydata=C9Q10_ydata, color=COLOR_COR))

k_C_S1 = 1.554e-3
for e in C_S1_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_C_S1, xdata=C_S1_xdata, ydata=C_S1_ydata, color=COLOR_COR))

k_C_S2 = 2.900e-3
for e in C_S2_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_C_S2, xdata=C_S2_xdata, ydata=C_S2_ydata, color=COLOR_COR))

###

k_S4 = -2.89e-3
for e in S4_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_S4, xdata=S4_xdata, ydata=S4_ydata,
                                      phy_field="B", eng_field="I", dtype="SOL", color=COLOR_SOL))

k_S1 = -7.431e-2
for e in S1_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_S1, xdata=S1_xdata, ydata=S1_ydata,
                                      phy_field="B", eng_field="I", dtype="SOL", color=COLOR_SOL))

k_S2 = -8.115e-2
for e in S2_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_S2, xdata=S2_xdata, ydata=S2_ydata,
                                      phy_field="B", eng_field="I", dtype="SOL", color=COLOR_SOL))

###

# Q1
x1 = 244.370393236,
x1r = None
a1 = 0
b1 = 0.118585750045
c1 = 0
a2 = -16.6039297722
b2 = 0.254477251076
c2 = -0.000278044118257
for e in Q1_elements:
    row_e2p, _ = make_rows_QUAD(e, xdata=Q1_xdata, ydata=Q1_ydata,
                                x1=x1, x1r=x1r, a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2, color=COLOR_QUAD)
    _, row_p2e = make_rows_COR_SOL(e, k=b1, xdata=Q1_ydata, ydata=Q1_xdata, phy_field="B2", eng_field="I",
                                   dtype='QUAD', color=COLOR_QUAD)
    all_rows.extend([row_e2p, row_p2e])
for e in Q1_elements_:
    row_e2p, _ = make_rows_QUAD(e, xdata=Q1_xdata_, ydata=Q1_ydata_,
                                x1=x1, x1r=x1r, a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2,
                                polarity=-1, color=COLOR_QUAD)
    _, row_p2e = make_rows_COR_SOL(e, k=-b1, xdata=Q1_ydata, ydata=Q1_xdata, phy_field="B2", eng_field="I",
                                   dtype='QUAD', color=COLOR_QUAD)
    all_rows.extend([row_e2p, row_p2e])

# Q2
k_Q2 = 0.1061
for e in Q2_elements:
    all_rows.extend(make_rows_COR_SOL(
        e, k=k_Q2, xdata=Q2_xdata, ydata=Q2_ydata,
        phy_field="B2", eng_field="I", dtype='QUAD', color=COLOR_QUAD))
for e in Q2_elements_:
    all_rows.extend(make_rows_COR_SOL(
        e, k=-k_Q2, xdata=Q2_xdata_, ydata=Q2_ydata_,
        phy_field="B2", eng_field="I", dtype='QUAD', color=COLOR_QUAD))

# Q3
k_Q3 = -0.10373
for e in Q3_elements:
    all_rows.extend(make_rows_COR_SOL(
        e, k=k_Q3, xdata=Q3_xdata, ydata=Q3_ydata,
        phy_field="B2", eng_field="I", dtype='QUAD', color=COLOR_QUAD))

# Q6
k_Q6 = 0.05018
for e in Q6_elements:
    all_rows.extend(make_rows_COR_SOL(
        e, k=k_Q6, xdata=Q6_xdata, ydata=Q6_ydata,
        phy_field="B2", eng_field="I", dtype='QUAD', color=COLOR_QUAD))
for e in Q6_elements_:
    all_rows.extend(make_rows_COR_SOL(
        e, k=-k_Q6, xdata=Q6_xdata_, ydata=Q6_ydata_,
        phy_field="B2", eng_field="I", dtype='QUAD', color=COLOR_QUAD))

# Q8
x1 = 89.6413014892835
x1r = 13.645592213
a1 = 0
b1 = 0.150213016296429
c1 = 0.0000224379963267202
a2 = -5.11759906727964
b2 = 0.264392506827174
c2 = -0.000614430771940742
for e in Q8_elements:
    all_rows.extend(make_rows_QUAD(e, xdata=Q8_xdata, ydata=Q8_ydata,
        x1=x1, x1r=x1r, a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2, color=COLOR_QUAD))

# Q9
x1 = 106.83602341739
x1r = -16.2642546626
a1 = 0
b1 = -0.151630162046015
c1 = -0.00000566773110230994
a2 = 7.29509238929589
b2 = -0.288196315595088
c2 = 0.00063347134006815
for e in Q9_elements:
    all_rows.extend(make_rows_QUAD(e, xdata=Q9_xdata, ydata=Q9_ydata,
        x1=x1, x1r=x1r, a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2, color=COLOR_QUAD))

# H3
k_H3 = -5.48
for e in H3_elements:
    all_rows.extend(make_rows_COR_SOL(
        e, k=k_H3, xdata=H3_xdata, ydata=H3_ydata,
        phy_field="B3", eng_field="I", dtype='SEXT', color=COLOR_SEXT))

##############################################################################
# write to xlsx

from xlwt import Workbook
from xlwt import XFStyle, easyxf, Pattern, Style

# new workbook
book = Workbook(encoding='utf-8')
# new sheet
sheet1 = book.add_sheet('Functions')

# header
header = ('name', 'ename', 'from_field', 'to_field', 'description', 'args', 'code', 'data_x', 'data_y')

# write header
header_style = easyxf('font: name Arial, bold True, color red, height 240; borders: bottom thin;')

write_row(sheet1, header, 0, style=header_style)

# write all rows into sheet1
for idx, r in enumerate(all_rows, 1):
    row_content, color = r
    style, pattern = XFStyle(), Pattern()
    pattern.pattern = Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = Style.colour_map[color]
    style.pattern = pattern
    write_row(sheet1, row_content, idx, style=style)

# save as a file
book.save('unicorn-data-new-1.xlsx')
