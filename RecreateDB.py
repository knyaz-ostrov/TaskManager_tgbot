from database.db_shell import PSQL, Database



def main() -> None:
    confirm = input('Вы действительно хотите выполнить пересоздание БД? [Y/N]: ').lower()
    if confirm != 'y':
        return
    
    psql = PSQL()
    psql.drop_db()
    psql.create_db()
    Database().create_table()


if __name__ == '__main__':
    main()
