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

class TestMortgageCalc(unittest.TestCase):

    def setUp(self):
        self.app = app.main()

    def test_app(self):
        assert_equal(True, True)

