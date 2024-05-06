import psycopg2

from misc.config import PostgresData as pd

class DBShell:
    def __init__(self, username: str, user_id: int) -> None:
        self.username = username
        self.user_id = user_id
        self.connect = self.__connection()
    
    def __connection(self):
        connect = psycopg2.connect(
            database = pd.get_db_name(),
            user     = pd.get_db_user(),
            password = pd.get_db_password(),
            host     = pd.get_db_host(),
            port     = pd.get_db_port()
        )
        return connect
    
    def add_task(self, task: str):
        cur = self.connect.cursor()
        cur.execute(
            f"INSERT INTO tasks (username, user_id, task) VALUES ('{self.username}', {self.user_id}, '{task}')"
        )
        self.connect.commit()

    def get_tasks(self):
        cur = self.connect.cursor()
        cur.execute(f'SELECT task FROM tasks WHERE user_id = {self.user_id}')
        rows = cur.fetchall()
        tasks = [row[0] for row in rows]
        return tasks

    def clear_tasks(self):
        cur = self.connect.cursor()
        cur.execute(f'DELETE FROM tasks WHERE user_id = {self.user_id}')
        self.connect.commit()

    def __del__(self) -> None:
        self.connect.close()