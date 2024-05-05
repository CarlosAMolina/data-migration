import typing as tp

import psycopg

import config_postgresql as config

Rows = tp.List[tuple]


class PostgreSQLDatabase:
    def __init__(self):
        self._uri = "postgresql://{}:{}@{}:{}/{}".format(
            config.USER,
            config.PASSWORD,
            config.HOST,
            config.PORT,
            config.SCHEMA,
        )

    def get_table_names(self) -> tp.List[str]:
        with psycopg.connect(self._uri) as conn:
            rows = conn.execute(
                "SELECT * FROM pg_catalog.pg_tables"
                " WHERE schemaname != 'pg_catalog' AND"
                " schemaname != 'information_schema';"
            ).fetchall()
        result = []
        for row in rows:
            table_name = row[1]
            result.append(table_name)
        return result

    # TODO rm
    def test(self):
        with psycopg.connect(self._uri) as conn:
            print(
                conn.execute(
                    "SELECT * FROM pg_catalog.pg_tables"
                    " WHERE schemaname != 'pg_catalog' AND"
                    " schemaname != 'information_schema';"
                ).fetchall()
            )
            print(conn.execute("SELECT * FROM contacts.emails").fetchall())
