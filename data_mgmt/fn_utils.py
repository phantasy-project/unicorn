# -*- coding: utf-8 -*-

from xlwt import XFStyle


UNIT_MAP_DEFAULT = {
    "I": "A",
    "V": "V",
    "ANG": "T.m",
    "B": "T",
    "G": "T/m",
}

def make_fn_name(ename, phy_field, eng_field, flag_p2e):
    """Make function name (e.g. 'ENAME_I_to_B') from:

    ename     : str, element name
    phy_field : str, physics field name
    eng_field : str, engineering field name
    flag_p2e  : bool, convert value from phy to eng (T) or eng to phy (F)

    Returns: tuple of (func-name, from-field, to-field)
    """
    f_field = phy_field if flag_p2e else eng_field
    t_field = eng_field if flag_p2e else phy_field
    return "{}_{}_to_{}".format(ename, f_field, t_field), f_field, t_field


def make_fn_desc(phy_field, eng_field, flag_p2e, **kws):
    """Make function description, e.g. 'I(A) to B(T)'
    """
    f_phy, f_eng = phy_field.upper(), eng_field.upper()
    unit_map = kws.get('unit_map', UNIT_MAP_DEFAULT)
    if flag_p2e:
        return "{f_phy}({f_phy_u}) to {f_eng}({f_eng_u})".format(
                    f_phy=f_phy, f_phy_u=unit_map.get(f_phy, ''),
                    f_eng=f_eng, f_eng_u=unit_map.get(f_eng, ''),
                )
    else:
        return "{f_eng}({f_eng_u}) to {f_phy}({f_phy_u})".format(
                    f_phy=f_phy, f_phy_u=unit_map.get(f_phy, ''),
                    f_eng=f_eng, f_eng_u=unit_map.get(f_eng, ''),
                )


def flip_data_str_signs(data):
    """Flip the signs of data string, e.g. '1 2 3' --> '-1 -2 -3'
    """
    return ' '.join([str(-float(i)) for i in data.split()])


def make_row(ename, phy_field, eng_field, flag_p2e,
             code, params, xdata, ydata, desc=None,
             color='white'):
    """Make row for xlwt.
    """
    name, f_field, t_field = make_fn_name(ename, phy_field, eng_field, flag_p2e)
    desc = make_fn_desc(phy_field, eng_field, flag_p2e) if desc is None else desc

    return (name, ename, f_field, t_field, desc, params, code, xdata, ydata), color


def write_row(sheet, row_content, row=0, col0=0, style=None):
    """Write row into 'sheet' with 'row_content' at 'row'-th row from 'col0'.
    """
    style = XFStyle() if style is None else style
    sheet.col(0).width = 300*20
    sheet.col(1).width = 200*20
    sheet.col(2).width = 320*20
    sheet.col(3).width = 256*20
    for col, label in enumerate(row_content, col0):
        sheet.row(row).height_mismatch = True
        sheet.row(row).height = 24*20
        sheet.write(row, col, label, style)

