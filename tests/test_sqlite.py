import unittest

import sqlite3

from src import sqlite


class TestFunctions(unittest.TestCase):
    def test_get_table_names(self):
        con = sqlite3.connect(":memory:")
        con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
        result = sqlite._get_table_names(con)
        expected_result = ["lang"]
        self.assertEqual(expected_result, result)