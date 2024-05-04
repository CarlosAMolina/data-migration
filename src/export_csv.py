from pathlib import Path
import csv
import datetime
import typing as tp

from database import Rows
from database import SQLiteDatabase


def export_to_csv(db_file_path_name: str):
    print("Start exporting database:", db_file_path_name)
    if not Path(db_file_path_name).exists():
        raise FileExistsError(db_file_path_name)
    directory_export_path_name = _DirectoryNameGenerator().get_directory_path_name(db_file_path_name)
    print("Start creating directory:", directory_export_path_name)
    Path(directory_export_path_name).mkdir()
    db = SQLiteDatabase(db_file_path_name=db_file_path_name)
    table_names = db.get_table_names()
    for index, table_name in enumerate(table_names, 1):
        print(f"Start table {index}/{len(table_names)}", table_name)
        rows = db.get_table_data(table_name)
        colum_names = db.get_table_column_names(table_name)
        csv_file_path_name = "{}/{}.csv".format(directory_export_path_name, table_name)
        print("Exporting table to", csv_file_path_name)
        _export_rows_to_csv(colum_names, rows, csv_file_path_name)


class _DirectoryNameGenerator:
    def get_directory_path_name(self, db_file_path_name: str) -> str:
        db_file_name = self._get_db_file_name_from_path_name(db_file_path_name)
        return "/tmp/{}-{}".format(db_file_name, self._str_date_time_for_name)

    def _get_db_file_name_from_path_name(self, db_file_path_name: str) -> str:
        return Path(db_file_path_name).name

    @property
    def _str_date_time_for_name(self) -> str:
        return datetime.datetime.now().strftime("%Y%m%d%H%M%S")


def _export_rows_to_csv(headers: tp.List[str], rows: Rows, csv_file_path_name: str):
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
