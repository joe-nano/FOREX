from Pattern.CounterDbTp import CounterDbTp

import pytest

@pytest.fixture
def ctdbptp_object():
    '''Returns CounterDbTp object'''

    c = CounterDbTp(
                        start='2019-02-21 22:00:00',
                        trend_i='2018-12-11 22:00:00',
                        pair='GBP_AUD',
                        timeframe='H12',
                        SL=1.84637,
                        TP=1.81196,
                        SR=1.84218,
                        type='short')

    return c
'''
def test_set_1stbounce(ctdbptp_object):

    ctdbptp_object.set_1stbounce()


def test_set_2ndbounce(ctdbptp_object):

    ctdbptp_object.set_2ndbounce()
'''

def test_init_feats(ctdbptp_object):

    ctdbptp_object.init_feats()

def test_init_trend_feats(ctdbptp_object):

    ctdbptp_object.set_1stbounce()
    ctdbptp_object.init_trend_feats()