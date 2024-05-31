import json



FILE_PATH = 'data/data/config.json'



class BotConfig:
    with open(FILE_PATH) as file:
        __bot_config = json.load(file)['bot']

    token = __bot_config['token']



class PSQLConfig:
    with open(FILE_PATH) as file:
        __psql_config = json.load(file)['postgresql']

    database = __psql_config['database']
    user     = __psql_config['user']
    password = __psql_config['password']
    host     = __psql_config['host']
    port     = __psql_config['port']
