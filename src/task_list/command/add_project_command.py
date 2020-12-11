from src.task_list.command.command import Command
from src.task_list.task.task_list import TaskList


class AddProjectCommand(Command):
    def __init__(self, console) -> None:
        self.command = "add project"
        self.console = console
        self.arguments = ["project name"]

    def execute(self, task_list: TaskList, arguments: str) -> None:
        name = arguments.strip()
        if len(name) == 0:
            self.console.print("No arguments provided")
            return
        tasks = task_list.get_tasks()
        tasks[name] = []
        task_list.set_tasks(tasks)
        return

    def name(self) -> str:
        return self.command + "".join([" <" + arg + ">" for arg in self.arguments])

    def get_command(self) -> str:
        return self.command
