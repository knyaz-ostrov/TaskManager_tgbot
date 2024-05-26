from .get_data.json import GetJSON



class GetConfig(GetJSON):
    def __init__(self) -> None:
        path = 'data/data/config.json'
        super().__init__(path)



class GetBotConfig(GetConfig):
    def __init__(self) -> None:
        super().__init__()
        category = 'bot'
        self.bot_configs = self.get_category(category)

    def get_token(self) -> str:
        token = self.bot_configs['token']
        return token



class GetDBConfig(GetConfig):
    def __init__(self) -> None:
        super().__init__()
        category = 'database'
        self.db_configs = self.get_category(category)

    def get_database(self) -> str:
        database = self.db_configs['database']
        return database

    def get_user(self) -> str:
        user = self.db_configs['user']
        return user

    def get_password(self) -> str:
        password = self.db_configs['password']
        return password

    def get_host(self) -> str:
        host = self.db_configs['host']
        return host

    def get_port(self) -> str:
        port = self.db_configs['port']
        return port