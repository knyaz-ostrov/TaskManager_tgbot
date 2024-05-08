import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from misc.config import PostgresData as pd

class DBShell:
    def __init__(self, username: str, user_id: int) -> None:
        self.username = username
        self.user_id = user_id
        connection = self.__connection()
        self.connect, self.cursor = connection[0], connection[1]
    
    def __connection(self):
        connect = psycopg2.connect(
            database = pd.get_db_name(),
            user     = pd.get_db_user(),
            password = pd.get_db_password(),
            host     = pd.get_db_host(),
            port     = pd.get_db_port()
        )
        connect.autocommit = True
        connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connect.cursor()

        return connect, cursor
    
    def add_task(self, task: str):
        self.cursor.execute(
            f"INSERT INTO tasks (username, user_id, task) VALUES ('{self.username}', {self.user_id}, '{task}')"
        )

    def get_tasks(self):
        self.cursor.execute(f'SELECT task FROM tasks WHERE user_id = {self.user_id}')
        rows = self.cursor.fetchall()
        tasks = [row[0] for row in rows]

        return tasks

    def clear_tasks(self):
        self.cursor.execute(f'DELETE FROM tasks WHERE user_id = {self.user_id}')

    def __del__(self) -> None:
        self.cursor.close()
        self.connect.close()



class DBCreator:

    def __init__(self) -> None:
        connection = self.__connection()
        self.connect, self.cursor = connection[0], connection[1]
        self.__drop_db()
        self.__create_db()
        self.__create_table()

    def __connection(self):
        connection = psycopg2.connect(
            user     = pd.get_db_user(),
            password = pd.get_db_password(),
            host     = pd.get_db_host(),
            port     = pd.get_db_port()
        )
        connection.autocommit = True
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connection.cursor()

        return connection, cursor

    def __drop_db(self) -> None:
        request = f'DROP DATABASE IF EXISTS "{pd.get_db_name()}"'
        self.cursor.execute(request)

    def __create_db(self) -> None:
        request = (
            f'CREATE DATABASE "{pd.get_db_name()}"  \n'
            '   WITH                                \n'
            f'  OWNER = {pd.get_db_user()}          \n'
            '   ENCODING = \'UTF8\'                 \n'
            '   LC_COLLATE = \'Russian_Russia.1251\'\n'
            '   LC_CTYPE = \'Russian_Russia.1251\'  \n'
            '   LOCALE_PROVIDER = \'libc\'          \n'
            '   TABLESPACE = pg_default             \n'
            '   CONNECTION LIMIT = -1               \n'
            '   IS_TEMPLATE = False;'
        )
        self.cursor.execute(request)

    def __create_table(self) -> None:
        connect = psycopg2.connect(
            database = pd.get_db_name(),
            user     = pd.get_db_user(),
            password = pd.get_db_password(),
            host     = pd.get_db_host(),
            port     = pd.get_db_port()
        )
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
        cursor = connect.cursor()
        cursor.execute(request)
        connect.commit()
        cursor.close()
        connect.close()

    def __del__(self) -> None:
        self.cursor.close()
        self.connect.close()