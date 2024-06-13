"""
Модуль для выполнения пересоздания БД PostgreSQL.
"""
from database import PSQLAdmin


def main() -> None:
    """
    Запрашивает подтверждение о выполнении процесса пересоздания БД, удаляет БД, создаёт БД и
    таблицы.
    
    :return:
    """
    confirm = input("Вы действительно хотите выполнить пересоздание БД? [Y/N]: ").lower()
    if confirm != 'y':
        return

    admin = PSQLAdmin()
    admin.drop_database()
    admin.create_database()
    admin.create_table()


if __name__ == '__main__':
    main()
