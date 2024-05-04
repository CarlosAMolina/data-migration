## Introduction

Project to export and import database data.

## Run

### Export

```bash
python src/main.py $PATH_NAME_SQLITE_DB_FILE
```

A folder in the `/tmp/` path will be created with all the tables data exported as `.csv`.

### Import

The database tables must exist, this script only imports data, it does not create the tables.

```bash
python src/main.py $PATH_NAME_FOLDER_WITH_CSV_FILES $PATH_NAME_SQLITE_DB_FILE
```

The csv files data will be imported to the database file.

## References

[sqlite3](https://docs.python.org/3/library/sqlite3.html)
