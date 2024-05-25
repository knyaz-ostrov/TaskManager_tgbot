import lxml.etree as et

class GetBotMessageText:
    def __init__(self) -> None:
        self.root = et.parse("bot_data/bot_message_text.xml")

    def get_start_message(self) -> str:
        text = self.root.xpath(""".//text[@id="start"]""")[0].text
        return text
    
    def get_add_task_message(self) -> str:
        text = self.root.xpath(""".//text[@id="add_task"]""")[0].text
        return text
    
    def get_task_list_empty_message(self) -> str:
        text = self.root.xpath(""".//text[@id="task_list_empty"]""")[0].text
        return text
    
    def get_clear_tasks_message(self) -> str:
        text = self.root.xpath(""".//text[@id="clear_tasks"]""")[0].text
        return text
    
    def get_task_created_message(self) -> str:
        text = self.root.xpath(""".//text[@id="task_created"]""")[0].text
        return text
    
class GetBotCommands:
    def __init__(self) -> None:
        self.root = et.parse("misc/data.xml")