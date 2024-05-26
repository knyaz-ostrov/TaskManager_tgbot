from scripts.db_shell import DBRecreator

def main():
    confirm = input('Вы действительно хотите выполнить пересоздание БД? [Y/N]: ').lower()
    if confirm == 'y':
        DBRecreator()

if __name__ == '__main__':
    main()