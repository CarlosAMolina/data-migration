from pathlib import Path
import csv
import datetime
import sqlite3
import sys
import typing as tp


def main():
    if len(sys.argv) < 2:
        raise ValueError("No db file path name provided")
    db_file_path_name = sys.argv[1]
    _export(db_file_path_name)


def _export(db_file_path_name: str):
    print("Init export database:", db_file_path_name)
    if not Path(db_file_path_name).exists():
        raise FileExistsError(db_file_path_name)
    directory_export_path_name = _DirectoryNameGenerator().get_directory_path_name(db_file_path_name)
    print("Init create directory:", directory_export_path_name)
    Path(directory_export_path_name).mkdir()
    db = _SQLiteDatabase(db_file_path_name=db_file_path_name)
    table_names = db.get_table_names()
    for index, table_name in enumerate(table_names, 1):
        print(f"Init table {index}/{len(table_names)}", table_name)
        rows = db.get_table_data(table_name)
        colum_names = db.get_table_column_names(table_name)
        csv_file_path_name = "{}/{}.csv".format(directory_export_path_name, table_name)
        print("Export table to", csv_file_path_name)
        _export_rows_to_csv(colum_names, rows, csv_file_path_name)


_Rows = tp.List[tuple]


class _DirectoryNameGenerator:
    def get_directory_path_name(self, db_file_path_name: str) -> str:
        db_file_name = self._get_db_file_name_from_path_name(db_file_path_name)
        return "/tmp/{}-{}".format(db_file_name, self._str_date_time_for_name)

    def _get_db_file_name_from_path_name(self, db_file_path_name: str) -> str:
        return Path(db_file_path_name).name

    @property
    def _str_date_time_for_name(self) -> str:
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


class _SQLiteDatabase:
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

    def get_table_data(self, table_name: str) -> _Rows:
        response = self._connection.execute(f"SELECT * FROM {table_name}")
        rows = response.fetchall()
        return rows

    def get_table_column_names(self, table_name: str) -> tp.List[str]:
        response = self._connection.execute(f"PRAGMA table_info({table_name})")
        response = response.fetchall()
        result = [row[1] for row in response]
        return result


def _export_rows_to_csv(headers: tp.List[str], rows: _Rows, csv_file_path_name: str):
    "https://docs.python.org/3/library/csv.html"
    with open(csv_file_path_name, "w", newline="") as csvfile:
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
