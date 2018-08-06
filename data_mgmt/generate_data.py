# -*- coding: utf-8 -*-

from fn_utils import make_fn_name, make_fn_desc
from fn_utils import make_row, flip_data_str_signs
from fn_utils import write_row

from fn_data import C4_xdata, C4_ydata
from fn_data import C4S4_xdata, C4S4_ydata
from fn_data import C9Q10_xdata, C9Q10_ydata
from fn_data import C_S1_xdata, C_S1_ydata
from fn_data import S4_xdata, S4_ydata
from fn_data import S1_xdata, S1_ydata
from fn_data import Q8_xdata, Q8_ydata
from fn_data import Q9_xdata, Q9_ydata

from fn_templates import fn_prop, fn_prop_reversed
from fn_templates import fn_quad, fn_quad_reversed

from fn_egroups import C4_elements, C4S4_elements, C9Q10_elements, C_S1_elements
from fn_egroups import S4_elements, S1_elements, Q8_elements, Q9_elements


def make_rows_COR_SOL(ename, k, xdata, ydata,
                      params="x,k", phy_field="ANG", eng_field="I",
                      dtype="COR"):
    #
    # make rows for correctors and solenoieds
    #
    # for cor:
    #   k,(x,y)data are defined for 'V',
    #   'H' data could be got by flipping the signs.
    #
    if 'DCH' in ename and dtype == "COR":
        k = -k
        ydata = flip_data_str_signs(ydata)
    code_e2p = fn_prop.format(k=k)
    code_p2e = fn_prop_reversed.format(k=k)
    row_e2p = make_row(ename, phy_field, eng_field, False,
                       code_e2p, params, xdata, ydata)
    row_p2e = make_row(ename, phy_field, eng_field, True,
                       code_p2e, params, ydata, xdata)
    return [row_e2p, row_p2e]


def make_rows_QUAD(ename, xdata, ydata,
                   params="x,x1,a1,b1,c1,a2,b2,c2",
                   phy_field="G", eng_field="I", **kws):
    #
    # make rows for quads
    #
    x1 = kws.get('x1')
    x1r = kws.get('x1r')
    a1 = kws.get('a1')
    b1 = kws.get('b1')
    c1 = kws.get('c1')
    a2 = kws.get('a2')
    b2 = kws.get('b2')
    c2 = kws.get('c2')
    code_e2p = fn_quad.format(x1=x1, a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2)
    code_p2e = fn_quad_reversed.format(x1=x1r, a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2)
    row_e2p = make_row(ename, phy_field, eng_field, False,
                       code_e2p, params, xdata, ydata)
    row_p2e = make_row(ename, phy_field, eng_field, True,
                       code_p2e, params, ydata, xdata)
    return [row_e2p, row_p2e]


##############################################################################

all_rows = []

k_C4 = 3.484e-4
for e in C4_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_C4, xdata=C4_xdata, ydata=C4_ydata))

k_C4S4 = 2.598e-4
for e in C4S4_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_C4S4, xdata=C4S4_xdata, ydata=C4S4_ydata))

k_C9Q10 = 0.950e-4
for e in C9Q10_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_C9Q10, xdata=C9Q10_xdata, ydata=C9Q10_ydata))

k_C_S1 = 1.554e-3
for e in C_S1_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_C_S1, xdata=C_S1_xdata, ydata=C_S1_ydata))

k_S4 = -2.89e-3
for e in S4_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_S4, xdata=S4_xdata, ydata=S4_ydata,
                                      phy_field="B", eng_field="I", dtype="SOL"))

k_S1 = -7.431e-2
for e in S1_elements:
    all_rows.extend(make_rows_COR_SOL(e, k=k_S1, xdata=S1_xdata, ydata=S1_ydata,
                                      phy_field="B", eng_field="I", dtype="SOL"))


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
        x1=x1, x1r=x1r, a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2))


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
        x1=x1, x1r=x1r, a1=a1, b1=b1, c1=c1, a2=a2, b2=b2, c2=c2))


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
book.save('unicorn-data-new.xlsx')
