import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from data.scripts.config import PSQLConfig



class PSQL:
    def __init__(self) -> None:
        self.db_configs = PSQLConfig()
        data = {
            'user': self.db_configs.user,
            'password': self.db_configs.password,
            'host': self.db_configs.host,
            'port': self.db_configs.port
        }
        self.connection(data)

    def connection(self, data) -> None:
        connect = psycopg2.connect(**data)
        connect.autocommit = True
        connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        self.connect, self.cursor = connect, connect.cursor()

    def drop_db(self) -> None:
        request = f'DROP DATABASE IF EXISTS "{self.db_configs.database}"'
        self.cursor.execute(request)

    def create_db(self) -> None:
        request = (
            f'CREATE DATABASE "{self.db_configs.database}"  \n'
            '   WITH                                \n'
            f'  OWNER = {self.db_configs.user}          \n'
            '   ENCODING = \'UTF8\'                 \n'
            '   LC_COLLATE = \'Russian_Russia.1251\'\n'
            '   LC_CTYPE = \'Russian_Russia.1251\'  \n'
            '   LOCALE_PROVIDER = \'libc\'          \n'
            '   TABLESPACE = pg_default             \n'
            '   CONNECTION LIMIT = -1               \n'
            '   IS_TEMPLATE = False;'
        )
        self.cursor.execute(request)

    def __del__(self) -> None:
        self.cursor.close()
        self.connect.close()



class Database(PSQL):
    def __init__(self) -> None:
        self.db_configs = PSQLConfig()
        data = {
            'database': self.db_configs.database,
            'user': self.db_configs.user,
            'password': self.db_configs.password,
            'host': self.db_configs.host,
            'port': self.db_configs.port
        }
        self.connection(data)

    def create_table(self) -> None:
        request = (
        'CREATE TABLE IF NOT EXISTS public.tasks        \n'
        '(                                              \n'
        '   username text COLLATE pg_catalog."default", \n'
        '   user_id bigint,                             \n'
        '   task text COLLATE pg_catalog."default"      \n'
        ')                                              \n\n'

        'TABLESPACE pg_default;                         \n\n'

        'ALTER TABLE IF EXISTS public.tasks             \n'
        '   OWNER to postgres;'
        )
        self.cursor.execute(request)



class DBActions(Database):
    def __init__(self, username: str, user_id: int) -> None:
        super().__init__()
        self.username, self.user_id = username, user_id

    def add_task(self, task: str) -> None:
        request = f"INSERT INTO tasks (username, user_id, task) VALUES ('{self.username}', {self.user_id}, '{task}')"
        self.cursor.execute(request)

    def get_tasks(self) -> list:
        request = f'SELECT task FROM tasks WHERE user_id = {self.user_id}'
        self.cursor.execute(request)
        rows = self.cursor.fetchall()
        return [row[0] for row in rows]

    def clear_tasks(self) -> None:
        request = f'DELETE FROM tasks WHERE user_id = {self.user_id}'
        self.cursor.execute(request)
