from scripts.db_shell import DBCreator

def main():
    confirm = input('Вы действительно хотите выполнить пересоздание БД? [Y/N]: ').lower()
    if confirm == 'y':
        DBCreator()

if __name__ == '__main__':
    main()