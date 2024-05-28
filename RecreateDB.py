from database.db_shell import PSQL, Database



def recreate_db() -> None:
    psql = PSQL()
    psql.drop_db()
    psql.create_db()
    Database().create_table()



def main():
    confirm = input('Вы действительно хотите выполнить пересоздание БД? [Y/N]: ').lower()
    if confirm == 'y':
        recreate_db()



if __name__ == '__main__':
    main()