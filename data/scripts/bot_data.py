"""
Модуль для текста, который используется в функционале бота.
"""
import lxml.etree as ET


FILE_PATH = 'data/data/bot_data.xml'
XPATH_TEMPLATE = './/{}'
XPATH_FILTER = '[@id="{}"]'


class BotMessageText:
    """
    Класс для хранения текстовых сообщений отправляемых ботом.
    """
    bot_data = ET.parse(FILE_PATH)
    category = 'text'
    path = XPATH_TEMPLATE.format(category) + XPATH_FILTER

    start           = bot_data.xpath(path.format('start'))[0].text
    add_task        = bot_data.xpath(path.format('add_task'))[0].text
    task_list_empty = bot_data.xpath(path.format('task_list_empty'))[0].text
    clear_tasks     = bot_data.xpath(path.format('clear_tasks'))[0].text
    task_created    = bot_data.xpath(path.format('task_created'))[0].text

    del bot_data, category, path


class BotCommands:
    """
    Класс для хранения команд, которые принимает бот.
    """
    bot_data = ET.parse(FILE_PATH)
    category = 'command'
    path = XPATH_TEMPLATE.format(category) + XPATH_TEMPLATE

    add_task    = bot_data.xpath(path.format('add_task'))[0].text
    get_tasks   = bot_data.xpath(path.format('get_tasks'))[0].text
    clear_tasks = bot_data.xpath(path.format('clear_tasks'))[0].text

    del bot_data, category, path
