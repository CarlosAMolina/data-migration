## Introduction

Project to export and import database data.

## Run

### Export

A folder in the `/tmp/` path will be created with all the tables data exported as `.csv`.

#### SQLite

```bash
python src/main.py sqlite $PATH_NAME_SQLITE_DB_FILE
```

#### PostgreSQL

Update the [configuration file](src/config_postgresql.py).

```bash
python src/main.py postgresql
```

### Import

The database tables must exist, this script only imports data, it does not create the tables.

```bash
python src/main.py sqlite $PATH_NAME_FOLDER_WITH_CSV_FILES $PATH_NAME_SQLITE_DB_FILE
```

The csv files data will be imported to the database file.

## References

[sqlite3](https://docs.python.org/3/library/sqlite3.html)
