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
        self.connect.commit()
        self.cursor.close()
        self.connect.close()