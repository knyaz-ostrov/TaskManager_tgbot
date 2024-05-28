from .data_types.json import JSON



class Config(JSON):
    def __init__(self) -> None:
        file_path = 'data/data/config.json'
        super().__init__(file_path)



class BotConfig(Config):
    def __init__(self) -> None:
        super().__init__()
        self.category = 'bot'

    def get_token(self) -> str:
        item_key = 'token'
        item = self.get_item(self.category, item_key)
        return item



class PSQLConfig(Config):
    def __init__(self) -> None:
        super().__init__()
        self.category = 'postgresql'

    def get_psql_data(self) -> dict:
        psql_data = {
            'user': self.get_user(),
            'password': self.get_password(),
            'host': self.get_host(),
            'port': self.get_port()
        }
        return psql_data

    def get_db_data(self) -> dict:
        db_data = self.get_psql_data()
        db_data['database'] = self.get_database()
        return db_data

    def get_database(self) -> str:
        item_key = 'database'
        item = self.get_item(self.category, item_key)
        return item

    def get_user(self) -> str:
        item_key = 'user'
        item = self.get_item(self.category, item_key)
        return item

    def get_password(self) -> str:
        item_key = 'password'
        item = self.get_item(self.category, item_key)
        return item

    def get_host(self) -> str:
        item_key = 'host'
        item = self.get_item(self.category, item_key)
        return item

    def get_port(self) -> str:
        item_key = 'port'
        item = self.get_item(self.category, item_key)
        return item