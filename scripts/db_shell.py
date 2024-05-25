import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from scripts.config import GetDBConfig

class PSQLConnect:
    def __init__(self) -> None:
        self.db_configs = GetDBConfig()
        connectection = self.__connection()
        self.connect, self.cursor = connectection[0], connectection[1]

    def __connection(self) -> tuple:
        connect = psycopg2.connect(
            user     = self.db_configs.get_user(),
            password = self.db_configs.get_password(),
            host     = self.db_configs.get_host(),
            port     = self.db_configs.get_port()
        )
        connect.autocommit = True
        connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connect.cursor()

        return connect, cursor
    
    def __del__(self) -> None:
        self.cursor.close()
        self.connect.close()



class DBConnect(PSQLConnect):
    def __init__(self) -> None:
        self.db_configs = GetDBConfig()
        connection = self.__connection()
        self.connect, self.cursor = connection[0], connection[1]

    def __connection(self) -> tuple:
        connect = psycopg2.connect(
            database = self.db_configs.get_database(),
            user     = self.db_configs.get_user(),
            password = self.db_configs.get_password(),
            host     = self.db_configs.get_host(),
            port     = self.db_configs.get_port()
        )
        connect.autocommit = True
        connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = connect.cursor()

        return connect, cursor



class DBRecreator(PSQLConnect):
    def __init__(self) -> None:
        super().__init__()
        self.__drop_db()
        self.__create_db()
        self.__create_table()

    def __drop_db(self) -> None:
        request = f'DROP DATABASE IF EXISTS "{self.db_configs.get_db_name()}"'
        self.cursor.execute(request)

    def __create_db(self) -> None:
        request = (
            f'CREATE DATABASE "{self.db_configs.get_db_name()}"  \n'
            '   WITH                                \n'
            f'  OWNER = {self.db_configs.get_db_user()}          \n'
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
        with psycopg2.connect(
            database = self.db_configs.get_database(),
            user     = self.db_configs.get_user(),
            password = self.db_configs.get_password(),
            host     = self.db_configs.get_host(),
            port     = self.db_configs.get_port()
        ) as connect:
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

            with connect.cursor() as cursor:
                cursor.execute(request)

            connect.commit()



class DBMethods(DBConnect):
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
        tasks = [row[0] for row in rows]
        
        return tasks
    
    def clear_tasks(self) -> None:
        request = f'DELETE FROM tasks WHERE user_id = {self.user_id}'
        self.cursor.execute(request)