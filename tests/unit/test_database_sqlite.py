import unittest

import sqlite3

from src.database_sqlite import SQLiteDatabase


class TestSQLiteDatabase(unittest.TestCase):
    def test_get_table_names(self):
        con = sqlite3.connect(":memory:")
        con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
        con.execute("CREATE TABLE lang_2(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
        db = SQLiteDatabase(connection=con)
        result = db.get_table_names()
        expected_result = ["lang", "lang_2"]
        self.assertEqual(expected_result, result)

    def test_get_table_data(self):
        con = sqlite3.connect(":memory:")
        con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
        with con:
            con.execute("INSERT INTO lang(name) VALUES(?)", ("Python",))
        db = SQLiteDatabase(connection=con)
        result = db.get_table_data("lang")
        expected_result = [(1, "Python")]
        self.assertEqual(expected_result, result)

    def test_get_table_colum_namesdata(self):
        con = sqlite3.connect(":memory:")
        con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
        db = SQLiteDatabase(connection=con)
        result = db.get_table_column_names("lang")
        expected_result = ["id", "name"]
        self.assertEqual(expected_result, result)

    def test_insert_rows(self):
        con = sqlite3.connect(":memory:")
        con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
        db = SQLiteDatabase(connection=con)
        table_name = "lang"
        column_names = ["id", "name"]
        rows = [[1, "a"], [2, "b"]]
        result = db.insert_rows(column_names, rows, table_name)
        result = db.get_table_data(table_name)
        expected_result = [(1, "a"), (2, "b")]
        self.assertEqual(expected_result, result)

    def test_truncate_table(self):
        con = sqlite3.connect(":memory:")
        con.execute("CREATE TABLE lang(id INTEGER PRIMARY KEY, name VARCHAR UNIQUE)")
        with con:
            con.execute("INSERT INTO lang(name) VALUES(?)", ("Python",))
        db = SQLiteDatabase(connection=con)
        table_name = "lang"
        result = db.get_table_data(table_name)
        expected_result = [(1, "Python")]
        self.assertEqual(expected_result, result)
        db.truncate_table(table_name)
        result = db.get_table_data(table_name)
        expected_result = []
        self.assertEqual(expected_result, result)
