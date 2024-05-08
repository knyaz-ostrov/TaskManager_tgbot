class BotMessageText:
    # START_MESSAGE = 'Привет! Это простой менеджер задач.\n\nКоманды:\n/add - Создать новую задачу\n/tsk - Вывести текущий список задач\n/clr - Очистить свой список задач'
    START_MESSAGE = (
        'Привет! Это простой менеджер задач.    \n\n'
        'Команды:                               \n'
        '   /add - Создать новую задачу         \n'
        '   /tsk - Вывести текущий список задач \n'
        '   /clr - Очистить свой список задач'
    )
    ADD_TASK = 'Напиши название новой задачи'
    TASK_LIST_EMPTY = 'Список задач пуст.'
    CLEAR_TASKS = 'Список задач очищен.'
    TASK_CREATED = 'Задача создана!'

class BotCommands:
    ADD_TASK = 'add'
    GET_TASKS = 'tsk'
    CLEAR_TASKS = 'clr'