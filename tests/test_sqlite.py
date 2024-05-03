import unittest

import sqlite3

from src import sqlite


class TestSQLiteDatabase(unittest.TestCase):
    def test_get_table_names(self):
        con = sqlite3.connect(":memory:")
        con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
        con.execute("CREATE TABLE lang_2(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
        db = sqlite._SQLiteDatabase(connection=con)
        result = db.get_table_names()
        expected_result = ["lang", "lang_2"]
        self.assertEqual(expected_result, result)

    def test_get_table_data(self):
        con = sqlite3.connect(":memory:")
        con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
        with con:
            con.execute("INSERT INTO lang(name) VALUES(?)", ("Python",))
        db = sqlite._SQLiteDatabase(connection=con)
        result = db.get_table_data("lang")
        expected_result = [(1, "Python")]
        self.assertEqual(expected_result, result)

    def test_get_table_colum_namesdata(self):
        con = sqlite3.connect(":memory:")
        con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
        db = sqlite._SQLiteDatabase(connection=con)
        result = db.get_table_column_names("lang")
        expected_result = ["id", "name"]
        self.assertEqual(expected_result, result)
