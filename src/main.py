import sys

from database_postgresql import PostgreSQLDatabase  # TODO rm
from export_csv import export_to_csv
from import_csv import import_csv_directory


def main():
    if len(sys.argv) == 2:
        db_file_path_name = sys.argv[1]
        export_to_csv(db_file_path_name)
    elif len(sys.argv) == 3:
        csv_directory_path_name = sys.argv[1]
        db_file_path_name = sys.argv[2]
        import_csv_directory(csv_directory_path_name, db_file_path_name)
    else:
        raise ValueError("Incorrect args")


if __name__ == "__main__":
    # main() # TODO uncomment
    PostgreSQLDatabase().test()  # TODO rm
