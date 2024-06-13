"""
Модуль для текста, который используется в функционале бота.
"""
import lxml.etree as ET

from handlers.misc.constants import FILE_PATH, XPATH_TEMPLATE, MESSAGE, START, ADD_TASK,\
    TASK_LIST_EMPTY, CLEAR_TASKS, TASK_CREATED


class MessageText():
    """
    Класс для получения текста сообщения, которое нужно отправить.
    """
    def __init__(self) -> None:
        self.__bot_data = ET.parse(FILE_PATH)

    def __getter(self, attr_id: str) -> str:
        """
        Метод для поиска и получения текста из XML-объекта по атрибуту id.
        
        :param attr_id: Значение атрибута.
        :return: Текст объекта.
        """
        return self.__bot_data.xpath(XPATH_TEMPLATE.format(MESSAGE, attr_id))[0].text

    @property
    def start(self) -> str:
        """
        Стартовое сообщение.
        
        :return:
        """
        return self.__getter(START)

    @property
    def add_task(self) -> str:
        """
        Добавить задачу.
        
        :return:
        """
        return self.__getter(ADD_TASK)

    @property
    def task_list_empty(self) -> str:
        """
        Список задач пустой.
        
        :return:
        """
        return self.__getter(TASK_LIST_EMPTY)

    @property
    def clear_tasks(self) -> str:
        """
        Список задач очищен.
        
        :return:
        """
        return self.__getter(CLEAR_TASKS)

    @property
    def task_created(self) -> str:
        """
        Задача создана.
        
        :return:
        """
        return self.__getter(TASK_CREATED)
