"""
Модуль для рядовых действий в БД.
"""
from database.psql.psql import PSQL
from database.psql.constants import ADD_TASK_SQL, GET_TASKS_SQL, CLEAR_TASKS_SQL, USERNAME,\
    USER_ID, TASK


class PSQLUser(PSQL):
    """
    Класс для работы с данными в БД.
    """
    def __init__(self, username: str, user_id: int) -> None:
        super().__init__()

        self._username, self._user_id = username, user_id

        self._connect_to_db()

    def add_task(self, task: str) -> None:
        """
        Метод добавляет задачу в таблицу.
        
        :param task: Название задачи.
        :return:
        """
        self.query(ADD_TASK_SQL, {USERNAME: self._username, USER_ID: self._user_id, TASK: task})

    def get_tasks(self) -> list[str]:
        """
        Метод для получения списка задач юзера.
        
        :return:
        """
        self.query(GET_TASKS_SQL, {USER_ID: self._user_id})
        rows = self._fetchall()

        return [row[0] for row in rows]

    def clear_tasks(self) -> None:
        """
        Метод для удаления всех задач юзера из БД.
        
        :return:
        """
        self.query(CLEAR_TASKS_SQL, {USER_ID: self._user_id})
