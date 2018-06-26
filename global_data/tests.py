import unittest
from global_data.models import Year


class TestBase(unittest.TestCase):
    """
    Basic Models Tests - Anything
    """

    def testYear(self):
        """ Test year model result"""
        year = Year('2018', 'Test', True)
        self.assertTrue()
