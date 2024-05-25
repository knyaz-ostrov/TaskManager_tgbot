import json

class GetBotCommands:
    def __init__(self) -> None:
        commands = None
        with open("bot_data/bot_commands.json", 'r') as file:
            commands = json.load(file)
        self.commands = commands

    def get_add_task_cmd(self) -> str:
        command = self.commands["add_task"]
        return command
    
    def get_get_tasks_cmd(self) -> str:
        command = self.commands["get_tasks"]
        return command
    
    def get_clear_task_cmd(self) -> str:
        command = self.commands["clear_tasks"]
        return command