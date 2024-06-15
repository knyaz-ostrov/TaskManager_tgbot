"""
Базовый модуль для работы с PostgreSQL.
"""
from typing import List, Tuple, Optional

import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from database.psql.config import Config


class PSQL:
    """
    Класс с базовыми методами для работы с PostgreSQL.
    """
    def __init__(self) -> None:
        self._configs = Config()

        self.__conn = None
        self.__cursor = None

    def __del__(self) -> None:
        self.__disconnect()

    def __disconnect(self) -> None:
        """
        Метод закрытия подключения.
        
        :return:
        """
        if self.__conn is not None:
            self.__cursor.close()
            self.__conn.close()

    def _connection(self, data: dict[str: str]) -> None:
        """
        Метод для подключения к PostgreSQL.
        
        :param data: Словарь с параметрами для подключения.
        :return:
        """
        self.__disconnect()

        connect = psycopg2.connect(**data)
        connect.autocommit = True
        connect.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

        self.__conn, self.__cursor = connect, connect.cursor()

    def _connect_to_db(self) -> None:
        """
        Метод для подключения к БД.
        
        :return:
        """
        self._connection(self._configs.db_connect)

    def _query(self, file_path: str, format_objects: dict[str: str | int] | tuple = None) -> None:
        """
        Метод для чтения sql-запроса из файла .sql и его выполнения.
        
        :param file_path: Путь к sql-файлу.
        :return:
        """
        with open(file_path, encoding='UTF-8') as file:
            request = file.read()

        if format_objects is not None:
            self.__cursor.execute(request % format_objects)
        else:
            self.__cursor.execute(request)

    def _fetchall(self) -> Optional[List[Tuple]]:
        """
        Метод для возвращения всех строк из запроса.
        
        :return: Список с кортежами или None, если ничего не найдено.
        """
        return self.__cursor.fetchall()
