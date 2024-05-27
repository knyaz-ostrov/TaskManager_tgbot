from .get_data.xml import GetXML



class GetBotData(GetXML):
    def __init__(self) -> None:
        file_path = 'data/data/bot_data.xml'
        super().__init__(file_path)
        self.item_pattern = './/{}[@id="{}"]'



class GetBotMessageText(GetBotData):
    def __init__(self) -> None:
        super().__init__()
        item_type = 'text'
        self.item_pattern = self.item_pattern.format(item_type, '{}')

    def get_start_message(self) -> str:
        item = 'start'
        item_path = self.item_pattern.format(item)
        text = self.get_item(item_path)
        return text

    def get_add_task_message(self) -> str:
        item = 'add_task'
        item_path = self.item_pattern.format(item)
        text = self.get_item(item_path)
        return text

    def get_task_list_empty_message(self) -> str:
        item = 'task_list_empty'
        item_path = self.item_pattern.format(item)
        text = self.get_item(item_path)
        return text

    def get_clear_tasks_message(self) -> str:
        item = 'clear_tasks'
        item_path = self.item_pattern.format(item)
        text = self.get_item(item_path)
        return text

    def get_task_created_message(self) -> str:
        item = 'task_created'
        item_path = self.item_pattern.format(item)
        text = self.get_item(item_path)
        return text



class GetBotCommands(GetBotData):
    def __init__(self) -> None:
        super().__init__()
        item_type = 'command'
        self.item_pattern = self.item_pattern.format(item_type, '{}')

    def get_add_task_command(self) -> str:
        item = 'add_task'
        item_path = self.item_pattern.format(item)
        command = self.get_item(item_path)
        return command

    def get_get_tasks_command(self) -> str:
        item = 'get_tasks'
        item_path = self.item_pattern.format(item)
        command = self.get_item(item_path)
        return command

    def get_clear_tasks_command(self) -> str:
        item = 'clear_tasks'
        item_path = self.item_pattern.format(item)
        command = self.get_item(item_path)
        return command