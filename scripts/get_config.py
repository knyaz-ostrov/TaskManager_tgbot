import json


class GetConfig:
    def __init__(self) -> None:
        configs = None
        with open("misc/config.json", 'r') as file:
            configs = json.load(file)
        self.configs = configs



class GetBotConfig(GetConfig):
    def __init__(self) -> None:
        super().__init__()
        self.configs = self.configs["bot"]

    def get_token(self) -> str:
        token = self.configs["token"]
        return token
    

class GetDBConfig(GetConfig):
    def __init__(self) -> None:
        super().__init__()
        self.configs = self.configs["database"]

    def get_database(self) -> str:
        database = self.configs["database"]
        return database
    
    def get_user(self) -> str:
        user = self.configs["user"]
        return user
    
    def get_password(self) -> str:
        password = self.configs["password"]
        return password

    def get_host(self) -> str:
        host = self.configs["host"]
        return host
    
    def get_port(self) -> str:
        port = self.configs["port"]
        return port