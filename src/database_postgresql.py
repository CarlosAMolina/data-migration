import typing as tp

import psycopg

from database_types import Rows
import config_postgresql as config


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

    def get_table_data(self, table_name: str) -> Rows:
        with psycopg.connect(self._uri) as conn:
            return conn.execute(f"SELECT * FROM {config.SCHEMA}.{table_name}").fetchall()
