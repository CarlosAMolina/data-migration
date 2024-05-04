import csv
import typing as tp

from pathlib import Path
from database import SQLiteDatabase


def import_csv_directory(csv_directory_path_name: str, db_file_path_name: str):
    print("Start importing", csv_directory_path_name, "files to", db_file_path_name)
    csv_file_path_names = _get_csv_file_path_names_in_directory(csv_directory_path_name)
    db = SQLiteDatabase(db_file_path_name=db_file_path_name)
    for index, csv_file_path_name in enumerate(csv_file_path_names, 1):
        table_name = _get_table_name_from_csv_file_path_name(csv_file_path_name)
        print("Start table", f"{index}/{len(csv_file_path_names)}", table_name)
        print("Deleting db table data:", table_name)
        db.truncate_table(table_name)
        print("Importing", csv_file_path_name)
        column_names = db.get_table_column_names(table_name)
        rows = _get_csv_rows(csv_file_path_name)
        db.insert_rows(column_names, rows, table_name)


def _get_csv_file_path_names_in_directory(directory_path_name: str) -> tp.List[str]:
    directory_path = Path(directory_path_name)
    paths = [x for x in directory_path.iterdir() if x.is_file() and x.suffix == ".csv"]
    result = [str(path) for path in paths]
    return result


def _get_table_name_from_csv_file_path_name(csv_file_path_name: str) -> str:
    return Path(csv_file_path_name).stem


def _get_csv_rows(csv_file_path_name: str) -> tp.List[list]:
    with open(csv_file_path_name, newline="") as f:
        reader = csv.reader(f)
        next(reader)  # skip the headers
        result = [row for row in reader]
        return result
