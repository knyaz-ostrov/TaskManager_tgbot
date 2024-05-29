import lxml.etree as ET



FILE_PATH = 'data/data/bot_data.xml'
path_template = './/{}'
filter = '[@id="{}"]'



class BotMessageText:
    bot_data = ET.parse(FILE_PATH)
    category = 'text'
    path = path_template.format(category) + filter

    start           = bot_data.xpath(path.format('start'))[0].text
    add_task        = bot_data.xpath(path.format('add_task'))[0].text
    task_list_empty = bot_data.xpath(path.format('task_list_empty'))[0].text
    clear_tasks     = bot_data.xpath(path.format('clear_tasks'))[0].text
    task_created    = bot_data.xpath(path.format('task_created'))[0].text

    del bot_data, category, path



class BotCommands:
    bot_data = ET.parse(FILE_PATH)
    category = 'command'
    path = path_template.format(category) + filter

    add_task    = bot_data.xpath(path.format('add_task'))[0].text
    get_tasks   = bot_data.xpath(path.format('get_tasks'))[0].text
    clear_tasks = bot_data.xpath(path.format('clear_tasks'))[0].text

    del bot_data, category, path
