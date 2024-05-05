import sys

from export_csv import export_to_csv

from export_csv import export_to_csv_postgresql
from import_csv import import_csv_directory

from enum import Enum


class DB_TYPE(Enum):
    SQLITE = "sqlite"
    POSTGRESQL = "postgresql"


def main():
    if len(sys.argv) < 2:
        _raise_incorrect_args()
    db_type = sys.argv[1]
    if db_type == DB_TYPE.SQLITE:
        if len(sys.argv) == 3:
            db_file_path_name = sys.argv[2]
            export_to_csv(db_file_path_name)
        elif len(sys.argv) == 4:
            csv_directory_path_name = sys.argv[2]
            db_file_path_name = sys.argv[3]
            import_csv_directory(csv_directory_path_name, db_file_path_name)
        else:
            _raise_incorrect_args()
    elif db_type == DB_TYPE.POSTGRESQL:
        export_to_csv_postgresql()
    else:
        _raise_incorrect_args()


def _raise_incorrect_args():
    raise ValueError("Incorrect args")


if __name__ == "__main__":
    main()
