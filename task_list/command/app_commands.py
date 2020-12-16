from typing import List

from task_list.command.command import Command, Leaf
from task_list.task.task_list import TaskList
from task_list.console import Console
from task_list.task.simple_task import SimpleTask


class AddProject(Leaf):
    def execute(self, task_list: TaskList, input_string: str) -> str:
        name = input_string.strip()
        if len(name) == 0:
            self.console.print("No input_string provided")
            return
        tasks = task_list.get_tasks()
        tasks[name] = []
        task_list.set_tasks(tasks)
        return


class AddTask(Leaf):
    def execute(self, task_list: TaskList, input_string: str) -> str:
        args = input_string.strip().split(" ", 1)
        if len(args) < 2:
            self.console.print("No arguments provided")
            return
        project = args[0]
        description = args[1]
        tasks = task_list.get_tasks()

        project_tasks = tasks.get(project)
        if project_tasks is None:
            self.console.print(f"Could not find a project " f"with the name {project}.")
            self.console.print()
            return
        new_task = SimpleTask(task_list.next_id(), description, False)
        project_tasks.append(new_task)
        tasks[project] = project_tasks
        return


class Help(Leaf):
    def __init__(
        self, arguments: List[str], console: Console, root_command: Command
    ) -> None:
        self.arguments = arguments
        self.console = console
        self.root_command = root_command

    def execute(self, task_list: TaskList, input_string: str) -> str:
        self.console.print("Commands:")
        self.root_command.name("  ")


class Show(Leaf):
    def execute(self, task_list: TaskList, input_string: str) -> str:
        for project, tasks in task_list.get_tasks().items():
            self.console.print(project)
            for task in tasks:
                self.console.print(task.display())
            self.console.print()


class Check(Leaf):
    def __init__(
        self, arguments: List[str], console: Console, is_done: bool = True
    ) -> None:
        self.arguments = arguments
        self.console = console
        self.is_done = is_done

    def execute(self, task_list: TaskList, input_string: str) -> str:
        task_id = input_string.strip()
        if len(task_id) == 0:
            self.console.print("No arguments provided")
            return
        id_ = int(task_id)
        tasks_ = task_list.get_tasks()
        done = self.is_done
        for project, tasks in tasks_.items():
            for task in tasks:
                if task.id == id_:
                    task.set_done(done)
                    task_list.set_tasks(tasks_)
                    return
        self.console.print(f"Could not find a task with an ID of {id_}")
        self.console.print()


class Quit(Leaf):
    def execute(self, task_list: TaskList, input_string: str) -> str:
        quit(0)
