# -*- coding: utf-8 -*-

import pickle
import codecs
import xlrd
import numpy as np
import sys


DATA_X_COL_IDX = 4
DATA_Y_COL_IDX = 5


def pickle_obj(obj, coding='base64'):
    """Pickle object into string for being a REST parameter.
    """
    return codecs.encode(pickle.dumps(obj), coding).decode()


class UnicornData(object):
    """Parsing data from external xlsx file.
   
    Examples
    --------
    >>> f = 'data.xlsx'
    >>> data = UnicornData(f)
    >>> for f in data.functions:
    >>>     client.create(**f)
    >>> # client is an AdminClient instance
    >>>
    """
    def __init__(self, xlsx_file):
        try:
            book = xlrd.open_workbook(xlsx_file)
        except:
            print("Open xlsx file failed.")
            sys.exit(1)
        self.sheet = book.sheet_by_index(0)
        self.ncols, self.nrows = self.sheet.ncols, self.sheet.nrows
        self.header = [x.value for x in self.sheet.row(0)]
        self.functions = self.generate_functions()
        
    def generate_functions(self):
        for ridx in range(1, self.nrows):
            row = [v.value for v in self.sheet.row(ridx)]

            x_raw = row[DATA_X_COL_IDX]
            row[DATA_X_COL_IDX] = pickle_obj(
                    np.array([float(v) for v in x_raw.split()]))

            y_raw = row[DATA_Y_COL_IDX]
            row[DATA_Y_COL_IDX] = pickle_obj(
                    np.array([float(v) for v in y_raw.split()]))
            f = dict(zip(self.header, row))
            yield f
            
        
        
