from src.task_list.command.command import Command
from src.task_list.task.task_list import TaskList


class UncheckCommand(Command):
    command = "uncheck"
    def __init__(self, console) -> None:
        # self.command = "uncheck"
        self.console = console
        self.arguments = ["task ID"]

    def execute(self, task_list: TaskList, arguments: str) -> None:
        task_id = arguments.strip()
        if len(task_id) == 0:
            self.console.print("No arguments provided")
            return
        id_ = int(task_id)
        tasks_ = task_list.get_tasks()
        done = False
        for project, tasks in tasks_.items():
            for task in tasks:
                if task.id == id_:
                    task.set_done(done)
                    task_list.set_tasks(tasks_)
                    return
        self.console.print(f"Could not find a task with an ID of {id_}")
        self.console.print()

    def name(self) -> str:
        return self.command + "".join([" <" + arg + ">" for arg in self.arguments])

    def get_command(self) -> str:
        return self.command
