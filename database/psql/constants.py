"""
Модуль для хранения констант.
"""
from typing import Final


# Путь к директории с SQL-файлами.
_SQL_FILES_PATH: Final = "database/queries/"

# Полные пути к каждому SQL-файлу.
## Административные SQL-запросы.
CREATE_DATABASE_SQL: Final = _SQL_FILES_PATH + "create_database.sql"
DROP_DATABASE_SQL: Final   = _SQL_FILES_PATH + "drop_database.sql"
CREATE_TABLE_SQL: Final    = _SQL_FILES_PATH + "create_table.sql"
## Рядовые SQL-Запросы.
ADD_TASK_SQL: Final        = _SQL_FILES_PATH + "add_task.sql"
GET_TASKS_SQL: Final       = _SQL_FILES_PATH + "get_tasks.sql"
CLEAR_TASKS_SQL: Final     = _SQL_FILES_PATH + "clear_tasks.sql"


# Имена объектов в БД.
USERNAME: Final = "username"
USER_ID: Final  = "user_id"
TASK: Final     = "task"

# Названия административных параметров в БД.
USER: Final             = "user"
DATABASE: Final         = "database"
PASSWORD: Final         = "password"
PORT: Final             = "port"
HOST: Final             = "host"

# Путь к конфигурационному файлу.
CONFIG_FILE_PATH: Final = "configs/database.json"
