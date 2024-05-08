import os

class BotConfig:

    def get_token() -> str:
        token = os.environ.get('STaskMgr_tgbot_BOT_TOKEN')
        return token

class PostgresData:

    def get_db_name() -> str:
        database = os.environ.get('STaskMgr_tgbot_DB_DATABASE')
        return database
    
    def get_db_user() -> str:
        user = os.environ.get('STaskMgr_tgbot_DB_USER')
        return user
    
    def get_db_password() -> int:
        password = int(os.environ.get('STaskMgr_tgbot_DB_PASSWORD'))
        return password
    
    def get_db_host() -> str:
        host = os.environ.get('STaskMgr_tgbot_DB_HOST')
        return host
    
    def get_db_port() -> str:
        port = os.environ.get('STaskMgr_tgbot_DB_PORT')
        return port