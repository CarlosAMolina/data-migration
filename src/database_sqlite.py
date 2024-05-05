import sqlite3
import typing as tp

from database_types import Rows


class SQLiteDatabase:
    def __init__(self, connection: tp.Optional[sqlite3.Connection] = None, db_file_path_name: tp.Optional[str] = None):
        if all(arg is None for arg in [connection, db_file_path_name]):
            raise ValueError
        self._connection: sqlite3.Connection = (
            connection if db_file_path_name is None else sqlite3.connect(db_file_path_name)
        )

    def get_table_names(self) -> tp.List[str]:
        response = self._connection.execute("SELECT * FROM sqlite_master where type='table'")
        rows = response.fetchall()
        result = []
        for row in rows:
            table_name = row[1]
            result.append(table_name)
        return result

    def get_table_data(self, table_name: str) -> Rows:
        response = self._connection.execute(f"SELECT * FROM {table_name}")
        rows = response.fetchall()
        return rows

    def get_table_column_names(self, table_name: str) -> tp.List[str]:
        response = self._connection.execute(f"PRAGMA table_info({table_name})")
        rows = response.fetchall()
        result = [row[1] for row in rows]
        return result

    def insert_rows(self, column_names: tp.List[str], rows: tp.List[list], table_name: str):
        table_name_and_columns = "{}({})".format(table_name, ",".join(column_names))
        values_query = ",".join(["?"] * len(column_names))
        query = f"INSERT INTO {table_name_and_columns} VALUES({values_query})"
        with self._connection:
            self._connection.executemany(query, rows)

    def truncate_table(self, table_name: str):
        with self._connection:
            self._connection.execute(f"DELETE FROM {table_name}")
