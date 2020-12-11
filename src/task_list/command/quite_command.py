from task_list.command.command import Command
from task_list.task.task_list import TaskList

class QuitCommand(Command):
    def __init__(self) -> None:
        self.command = "quit"
    
    def execute(self, task_list: TaskList, arguments: str) -> None:
        quit()

    def name(self) -> str:
        return self.command #+ (" <" + s + ">" for arg in self.arguments)

    def get_command(self) -> str:
        return self.command