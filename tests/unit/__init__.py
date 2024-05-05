import pathlib
import sys

current_directory_path = pathlib.Path(__file__).parent.absolute()
main_project_path = current_directory_path.parent.parent
src_directory_path = main_project_path.joinpath("src")
sys.path.append(str(src_directory_path))
