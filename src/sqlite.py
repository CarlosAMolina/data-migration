import sqlite3
import typing as tp

def main():
    db_file = "/tmp/contacts.test.sqlite3"
    connection = sqlite3.connect(db_file)
    cursor = connection.cursor()
    table_names = _get_tables(cursor)
    for index, table_name in enumerate(table_names, 1):
        print(f"{index}/{len(table_names)}", table_name)

def _get_tables(cursor: sqlite3.Cursor) -> tp.List[str]:
    response = cursor.execute("SELECT * FROM sqlite_master where type='table'")
    rows = response.fetchall()
    result = []
    for row in rows:
        table_name = row[1]
        result.append(table_name)
    return result

if __name__ == "__main__":
    main()
