"""
Модуль для совершения административных действий в PostgreSQL.
"""
from database.psql.psql import PSQL
from database.psql.constants import USER, DATABASE
from database.sesh.constants import CREATE_DATABASE_SQL, DROP_DATABASE_SQL, CREATE_TABLE_SQL


class PSQLAdmin(PSQL):
    """
    Класс для выполнения административных методов.
    """
    def __connect_to_psql(self) -> None:
        """
        Метод для подключения к PSQL.
        
        :return:
        """
        self._connection(self._configs.psql_connect)

    def create_database(self) -> None:
        """
        Метод для создания базы данных.
        
        :return:
        """
        self.__connect_to_psql()

        self._query(CREATE_DATABASE_SQL, {DATABASE: self._configs.database,
                   USER: self._configs.user})

    def drop_database(self) -> None:
        """
        Метод для удаления базы данных.
        
        :return:
        """
        self.__connect_to_psql()

        self._query(DROP_DATABASE_SQL, {DATABASE: self._configs.database})

    def create_table(self) -> None:
        """
        Метод для создания таблицы в БД.
        
        :return:
        """
        self._connect_to_db()

        self._query(CREATE_TABLE_SQL, {USER: self._configs.user})
