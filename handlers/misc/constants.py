"""
Модуль для хранения констант.
"""
from typing import Final


# Путь к XML-файлу.
FILE_PATH: Final        = "data/data.xml"
# Шаблон для xpath.
XPATH_TEMPLATE: Final   = """.//{}[@id="{}"]"""
# Название тега.
MESSAGE: Final          = "message"
# Атрибуты id тега message.
START: Final            = "start"
ADD_TASK: Final         = "add_task"
TASK_LIST_EMPTY: Final  = "task_list_empty"
CLEAR_TASKS: Final      = "clear_tasks"
TASK_CREATED: Final     = "task_created"

# Команды бота.
CMD_ADD_TASK: Final     = "add"
CMD_GET_TASKS: Final    = "tsk"
CMD_CLEAR_TASKS: Final  = "clr"

# Константы для лог-сообщений.
LOG_TEMPLATE: Final     = """[%s] Func: %s | User: (%s, %d), Message: "%s...\""""
LOG_TYPE_HANDLER: Final = "HANDLER"
LOG_MESSAGE_LEN: Final = 10
