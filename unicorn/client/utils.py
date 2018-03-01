# -*- coding: utf-8 -*-

from __future__ import print_function
from __future__ import unicode_literals

from requests.adapters import HTTPAdapter
import pickle
import codecs


class MyAdapter(HTTPAdapter):
    pass
    #def init_poolmanager(self, connections, maxsize, block=False, **kws):
    #    self.pool


def make_response(r):
    if r.ok:
        return r.json()
    else:
        #r.raise_for_status()
        return {'status': r.ok, 'code': r.status_code}


def pickle_obj(obj, coding='base64'):
    """Pickle object into string for being a REST parameter.
    """
    return codecs.encode(pickle.dumps(obj), coding).decode()
