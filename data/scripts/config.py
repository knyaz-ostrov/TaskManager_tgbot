import json



FILE_PATH = 'data/data/config.json'



class BotConfig:
    with open(FILE_PATH) as file:
        bot_config = json.load(file)['bot']

    token = bot_config['token']
    del bot_config



class PSQLConfig:
    with open(FILE_PATH) as file:
        psql_config = json.load(file)['postgresql']

    database = psql_config['database']
    user     = psql_config['user']
    password = psql_config['password']
    host     = psql_config['host']
    port     = psql_config['port']
    del psql_config
