from src.task_list.command.command import Command
from src.task_list.task.task_list import TaskList


class HelpCommand(Command):
    def __init__(self, command_list, console) -> None:
        self.command = "help"
        self.command_list = command_list
        self.console = console

    def execute(self, task_list: TaskList, arguments: str) -> None:
        self.console.print("Commands:")
        for command in self.command_list:
            self.console.print("  " + command.name())

    def name(self) -> str:
        return self.command

    def get_command(self) -> str:
        return self.command
