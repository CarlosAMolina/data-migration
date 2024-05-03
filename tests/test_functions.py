import unittest

from src import functions


class TestFunctions(unittest.TestCase):
    def test_sum_int_returns_expected_result(self):
        self.assertEqual(2, functions.sum_int(1, 1))
