from .get_data.xml import GetXML



class GetBotData(GetXML):
    def __init__(self) -> None:
        path = 'data/data/bot_data.xml'
        super().__init__(path)
        del path
        self.bot_data = self.data
        del self.data



class GetBotMessageText(GetBotData):
    def __init__(self) -> None:
        super().__init__()
        self.bot_message_text = self.bot_data
        del self.bot_data
        self.path = './/BotMessageText/text[@id="{}"]'

    def get_start_message(self) -> str:
        text = self.bot_message_text.xpath(self.path.format('start'))[0].text
        return text

    def get_add_task_message(self) -> str:
        text = self.bot_message_text.xpath(self.path.format('add_task'))[0].text
        return text

    def get_task_list_empty_message(self) -> str:
        text = self.bot_message_text.xpath(self.path.format('task_list_empty'))[0].text
        return text

    def get_clear_tasks_message(self) -> str:
        text = self.bot_message_text.xpath(self.path.format('clear_tasks'))[0].text
        return text

    def get_task_created_message(self) -> str:
        text = self.bot_message_text.xpath(self.path.format('task_created'))[0].text
        return text



class GetBotCommands(GetBotData):
    def __init__(self) -> None:
        super().__init__()
        self.bot_commands = self.bot_data
        del self.bot_data
        self.path = './/BotCommands/command[@id="{}"]'

    def get_add_task_command(self) -> str:
        command = self.bot_commands.xpath(self.path.format('add_task'))[0].text
        return command

    def get_get_tasks_command(self) -> str:
        command = self.bot_commands.xpath(self.path.format('get_tasks'))[0].text
        return command

    def get_clear_tasks_command(self) -> str:
        command = self.bot_commands.xpath(self.path.format('clear_tasks'))[0].text
        return command