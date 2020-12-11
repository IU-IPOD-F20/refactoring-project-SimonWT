from task_list.command.command import Command
from task_list.task.task_list import TaskList


class ShowCommand(Command):
    def __init__(self, console) -> None:
        self.command = "show"
        self.console = console

    def execute(self, task_list: TaskList, arguments: str) -> None:
        for project, tasks in task_list.get_tasks().items():
            self.console.print(project)
            for task in tasks:
                self.console.print(task.display())
            self.console.print()

    def name(self) -> str:
        return self.command

    def get_command(self) -> str:
        return self.command
