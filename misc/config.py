import os

class BotConfig:

    def get_token() -> str:
        token = os.environ.get('TOKEN')
        return token

class PostgresData:

    def get_db_name() -> str:
        database = os.environ.get('TEST_PSQL_DATABASE')
        return database
    
    def get_db_user() -> str:
        user = os.environ.get('TEST_PSQL_USER')
        return user
    
    def get_db_password() -> int:
        password = int(os.environ.get('TEST_PSQL_PASSWORD'))
        return password
    
    def get_db_host() -> str:
        host = os.environ.get('TEST_PSQL_HOST')
        return host
    
    def get_db_port() -> str:
        port = os.environ.get('TEST_PSQL_PORT')
        return port