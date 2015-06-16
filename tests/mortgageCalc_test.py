#import unittest

def root(*path):
    return os.path.abspath(os.path.join(os.path.dirname(__file__), '..', *path))

import os
import sys
import unittest
from nose.tools import *

sys.path.insert(0, root('lib'))

print(sys.path)

from MortgageCalc import app
from MortgageCalc import core

class TestMortgageCalc(unittest.TestCase):

    def setUp(self):
        self.app = app.main()

    def test_app(self):
        assert_equal(True, True)

    def test_get_mortgage_schedule(self):
        result = core.get_mortgage_schedule(True, 270000, 4.9, 1, 12, 0.54, 12.0, 1261.01, 21600)
        expected = [{'pmt': 1261.01, 'intr_applied': 290.80999999999983, 'monthly_pmi_pmt': 11953.010000000002, 'month': 1,
                      'starting_balance': 237600.0, 'intr': 970.2000000000002, 'end_balance': 237309.19},
                     {'pmt': 1261.01, 'intr_applied': 291.9974741666665, 'monthly_pmi_pmt': 11953.010000000002, 'month': 2,
                      'starting_balance': 237309.19, 'intr': 969.0125258333335, 'end_balance': 237017.19252583332},
                     {'pmt': 1261.01, 'intr_applied': 293.1897971861805, 'monthly_pmi_pmt': 11953.010000000002, 'month': 3,
                      'starting_balance': 237017.19252583332, 'intr': 967.8202028138195, 'end_balance': 236724.00272864714},
                     {'pmt': 1261.01, 'intr_applied': 294.3869888580241, 'monthly_pmi_pmt': 11953.010000000002, 'month': 4,
                       'starting_balance': 236724.00272864714, 'intr': 966.6230111419759, 'end_balance': 236429.61573978912},
                     {'pmt': 1261.01, 'intr_applied': 295.58906906252764, 'monthly_pmi_pmt': 11953.010000000002, 'month': 5,
                       'starting_balance': 236429.61573978912, 'intr': 965.4209309374723, 'end_balance': 236134.0266707266},
                     {'pmt': 1261.01, 'intr_applied': 296.79605776119956, 'monthly_pmi_pmt': 11953.010000000002, 'month': 6,
                      'starting_balance': 236134.0266707266, 'intr': 964.2139422388004, 'end_balance': 235837.2306129654},
                     {'pmt': 1261.01, 'intr_applied': 298.0079749970579, 'monthly_pmi_pmt': 11953.010000000002, 'month': 7,
                      'starting_balance': 235837.2306129654, 'intr': 963.0020250029421, 'end_balance': 235539.22263796834},
                     {'pmt': 1261.01, 'intr_applied': 299.22484089496254, 'monthly_pmi_pmt': 11953.010000000002, 'month': 8,
                      'starting_balance': 235539.22263796834, 'intr': 961.7851591050375, 'end_balance': 235239.9977970734},
                     {'pmt': 1261.01, 'intr_applied': 300.44667566195017, 'monthly_pmi_pmt': 11953.010000000002, 'month': 9,
                      'starting_balance': 235239.9977970734, 'intr': 960.5633243380498, 'end_balance': 234939.55112141144},
                     {'pmt': 1261.01, 'intr_applied': 301.67349958756984, 'monthly_pmi_pmt': 11953.010000000002, 'month': 10,
                      'starting_balance': 234939.55112141144, 'intr': 959.3365004124302, 'end_balance': 234637.87762182386},
                     {'pmt': 1261.01, 'intr_applied': 302.9053330442191, 'monthly_pmi_pmt': 11953.010000000002, 'month': 11,
                      'starting_balance': 234637.87762182386, 'intr': 958.1046669557809, 'end_balance': 234334.97228877965},
                     {'pmt': 1261.01, 'intr_applied': 304.1421964874829, 'monthly_pmi_pmt': 11953.010000000002, 'month': 12,
                      'starting_balance': 234334.97228877965, 'intr': 956.8678035125171, 'end_balance': 234030.83009229216}
                    ]
        assert_equal(expected, result)

