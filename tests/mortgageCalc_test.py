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
        expected = ""
        assert_equal(expected, result)

