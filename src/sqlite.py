import csv
import sqlite3
import typing as tp


def main():
    db_file = "/tmp/contacts.test.sqlite3"
    db = _SQLiteDatabase(db_file=db_file)
    table_names = db.get_table_names()
    for index, table_name in enumerate(table_names, 1):
        print(f"Init table {index}/{len(table_names)}", table_name)
        rows = db.get_table_data(table_name)
        colum_names = db.get_table_column_names(table_name)
        _export_rows_to_csv(colum_names, rows, table_name)


_Rows = tp.List[tuple]


class _SQLiteDatabase:
    def __init__(self, connection: tp.Optional[sqlite3.Connection] = None, db_file: tp.Optional[str] = None):
        if all(arg is None for arg in [connection, db_file]):
            raise ValueError
        self._connection: sqlite3.Connection = connection if db_file is None else sqlite3.connect(db_file)

    def get_table_names(self) -> tp.List[str]:
        response = self._connection.execute("SELECT * FROM sqlite_master where type='table'")
        rows = response.fetchall()
        result = []
        for row in rows:
            table_name = row[1]
            result.append(table_name)
        return result

    def get_table_data(self, table_name: str) -> _Rows:
        response = self._connection.execute(f"SELECT * FROM {table_name}")
        rows = response.fetchall()
        return rows

    def get_table_column_names(self, table_name: str) -> tp.List[str]:
        response = self._connection.execute(f"PRAGMA table_info({table_name})")
        response = response.fetchall()
        result = [row[1] for row in response]
        return result


def _export_rows_to_csv(headers: tp.List[str], rows: _Rows, table_name: str):
    "https://docs.python.org/3/library/csv.html"
    file_path_name = f"/tmp/{table_name}.csv"
    with open(file_path_name, "w", newline="") as csvfile:
        spamwriter = csv.writer(
            csvfile,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
        )
        spamwriter.writerow(headers)
        for row in rows:
            spamwriter.writerow(row)


if __name__ == "__main__":
    main()
