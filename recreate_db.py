"""
Модуль для выполнения пересоздания БД PostgreSQL.
"""
from database.db_shell import PSQL, Database
from constants import CONFIRMATION_OF_DATABASE_RECREATION



def main() -> None:
    """
    Запрашивает подтверждение о выполнении процесса пересоздания БД, удаляет БД, создаёт БД и
    таблицы.
    
    :return:
    """
    confirm = input(CONFIRMATION_OF_DATABASE_RECREATION).lower()
    if confirm != 'y':
        return

    psql = PSQL()
    psql.drop_db()
    psql.create_db()
    Database().create_table()


if __name__ == '__main__':
    main()
