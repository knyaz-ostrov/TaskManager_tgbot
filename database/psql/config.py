"""
Модуль для чтения параметров конфигурации из JSON-файла.
"""
import json

from database.psql.constants import CONFIG_FILE_PATH, USER, PASSWORD, PORT, HOST, DATABASE


class Config:
    """
    Класс для определения переменных с конфигурационными данными.
    """
    def __init__(self) -> None:
        with open(CONFIG_FILE_PATH, encoding='UTF-8') as file:
            self.__config = json.load(file)

    @property
    def psql_connect(self) -> dict[str: str]:
        """
        Данные для подключения к psql.
        
        :return: Словарь с параметрами.
        """
        return {
            USER    : self.user,
            PASSWORD: self.password,
            HOST    : self.host,
            PORT    : self.port,
        }

    @property
    def db_connect(self) -> dict[str: str]:
        """
        Данные для подключения к БД.
        
        :return: Словарь с параметрами.
        """
        data = self.psql_connect
        data[DATABASE] = self.database

        return data

    @property
    def user(self) -> str:
        """
        Юзернейм.
        """
        return self.__config.get(USER)

    @property
    def password(self) -> str:
        """
        Пароль.
        """
        return self.__config.get(PASSWORD)

    @property
    def host(self) -> str:
        """
        Хост.
        """
        return self.__config.get(HOST)

    @property
    def port(self) -> str:
        """
        Порт.
        """
        return self.__config.get(PORT)

    @property
    def database(self) -> str:
        """
        БД.
        """
        return self.__config.get(DATABASE)
