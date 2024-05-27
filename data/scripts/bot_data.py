from .data_types.xml import XML



class BotData(XML):
    def __init__(self) -> None:
        file_path = 'data/data/bot_data.xml'
        super().__init__(file_path)



class BotMessageText(BotData):
    def __init__(self) -> None:
        super().__init__()
        self.category = 'text'

    def get_start(self) -> str:
        filter_value = 'start'
        text = self.get_item(self.category, filter_value)
        return text

    def get_add_task(self) -> str:
        filter_value = 'add_task'
        text = self.get_item(self.category, filter_value)
        return text

    def get_task_list_empty(self) -> str:
        filter_value = 'task_list_empty'
        text = self.get_item(self.category, filter_value)
        return text

    def get_clear_tasks(self) -> str:
        filter_value = 'clear_tasks'
        text = self.get_item(self.category, filter_value)
        return text

    def get_task_created(self) -> str:
        filter_value = 'task_created'
        text = self.get_item(self.category, filter_value)
        return text



class BotCommands(BotData):
    def __init__(self) -> None:
        super().__init__()
        self.category = 'command'

    def get_add_task(self) -> str:
        filter_value = 'add_task'
        text = self.get_item(self.category, filter_value)
        return text

    def get_get_tasks(self) -> str:
        filter_value = 'get_tasks'
        text = self.get_item(self.category, filter_value)
        return text

    def get_clear_tasks(self) -> str:
        filter_value = 'clear_tasks'
        text = self.get_item(self.category, filter_value)
        return text