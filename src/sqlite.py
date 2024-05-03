import sqlite3
import typing as tp


def main():
    db_file = "/tmp/contacts.test.sqlite3"
    db = _SQLiteDatabase(db_file=db_file)
    table_names = db.get_table_names()
    for index, table_name in enumerate(table_names, 1):
        print(f"{index}/{len(table_names)}", table_name)
        rows = _get_table_data(db._connection, table_name)
        print(rows)


class _SQLiteDatabase:
    def __init__(self, connection: sqlite3.Connection = None, db_file: str = None):
        if all(arg is None for arg in [connection, db_file]):
            raise ValueError
        self._connection = connection if db_file is None else sqlite3.connect(db_file)

    def get_table_names(self) -> tp.List[str]:
        response = self._connection.execute("SELECT * FROM sqlite_master where type='table'")
        rows = response.fetchall()
        result = []
        for row in rows:
            table_name = row[1]
            result.append(table_name)
        return result


def _get_table_data(connection: sqlite3.Connection, table_name: str) -> tp.List[tuple]:
    response = connection.execute(f"SELECT * FROM {table_name}")
    rows = response.fetchall()
    return rows


if __name__ == "__main__":
    main()
