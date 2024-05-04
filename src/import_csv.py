import typing as tp

from pathlib import Path


def import_csv_directory(csv_directory_path_name: str, db_file_path_name: str):
    print("Start importing", csv_directory_path_name, "files to", db_file_path_name)
    csv_files = _get_csv_files_in_directory(csv_directory_path_name)
    print(len(csv_files), csv_files)


def _get_csv_files_in_directory(directory_path_name: str) -> tp.List[str]:
    directory_path = Path(directory_path_name)
    paths = [x for x in directory_path.iterdir() if x.is_file() and x.suffix == ".csv"]
    result = [str(path) for path in paths]
    return result
