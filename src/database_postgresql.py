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
            response = conn.execute(
                "SELECT * FROM pg_catalog.pg_tables"
                " WHERE schemaname != 'pg_catalog' AND"
                " schemaname != 'information_schema';"
            )
            rows = response.fetchall()
        result = []
        for row in rows:
            table_name = row[1]
            result.append(table_name)
        return result

    def get_table_data(self, table_name: str) -> Rows:
        query = f"SELECT * FROM {config.SCHEMA}.{table_name}"
        with psycopg.connect(self._uri) as conn:
            response = conn.execute(query)
            rows = response.fetchall()
        return rows

    def get_table_column_names(self, table_name: str) -> Rows:
        query = (
            f"SELECT column_name FROM information_schema.columns WHERE table_name = '{table_name}'"
            " order by ordinal_position ASC;"
        )
        with psycopg.connect(self._uri) as conn:
            rows = conn.execute(query).fetchall()
        result = [row[0] for row in rows]
        return result
