from src.task_list.command.command import Command
from src.task_list.task.task_list import TaskList
from src.task_list.task.simple_task import SimpleTask


class AddTaskCommand(Command):
    def __init__(self, console) -> None:
        self.command = "add task"
        self.console = console
        self.arguments = ["project name", "task description"]

    def execute(self, task_list: TaskList, arguments: str) -> None:
        arguments = arguments.strip()
        args = arguments.split(" ", 1)
        if len(args) < 2:
            self.console.print("No arguments provided")
            return
        project = args[0]
        description = args[1]
        tasks = task_list.get_tasks()

        project_tasks = tasks.get(project)
        if project_tasks is None:
            self.console.print(f"Could not find a project with the name {project}.")
            self.console.print()
            return
        new_task = SimpleTask(task_list.next_id(), description, False)
        # print("new task", new_task)
        project_tasks.append(new_task)
        tasks[project] = project_tasks
        task_list.set_tasks(tasks)
        return

    def name(self) -> str:
        return self.command + "".join([" <" + arg + ">" for arg in self.arguments])

    def get_command(self) -> str:
        return self.command
