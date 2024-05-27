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
        item = 'token'
        value = self.bot_configs[item]
        return value



class GetDBConfig(GetConfig):
    def __init__(self) -> None:
        super().__init__()
        category = 'database'
        self.db_configs = self.get_category(category)

    def get_database(self) -> str:
        item = 'database'
        value = self.db_configs[item]
        return value

    def get_user(self) -> str:
        item = 'user'
        value = self.db_configs[item]
        return value

    def get_password(self) -> str:
        item = 'password'
        value = self.db_configs[item]
        return value

    def get_host(self) -> str:
        item = 'host'
        value = self.db_configs[item]
        return value

    def get_port(self) -> str:
        item = 'port'
        value = self.db_configs[item]
        return value