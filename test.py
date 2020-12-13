from __future__ import annotations
from abc import ABC, abstractmethod
from task_list.task.task_list import TaskList
from typing import Dict, List
from task_list.console import Console
from task_list.task.simple_task import SimpleTask
import sys


class Command(ABC):
    def add(self, command_name: str, command: Command) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def name(self, parent_name: str) -> None:
        pass

    @abstractmethod
    def operation(self, task_list: TaskList, input_string: str) -> str:
        pass


class Leaf(Command):
    def __init__(self, arguments: List[str], console: Console) -> None:
        self.arguments = arguments
        self.console = console

    def operation(self, task_list: TaskList, input_string: str) -> str:
        pass

    def name(self, parent_name: str) -> None:
        name = parent_name + "".join([" <" + arg + ">" for arg in self.arguments])
        self.console.print(name)


class Composite(Command):
    def __init__(self, console: Console) -> None:
        self._children: Dict[str, Command] = dict()
        self.console = console

    def add(self, command_name: str, command: Command) -> None:
        self._children[command_name] = command

    def is_composite(self) -> bool:
        return True

    def operation(self, task_list: TaskList, input_string: str) -> str:
        parsed = input_string.split(" ", 1)
        command = parsed[0]
        rest = ""
        if len(parsed) > 1:
            rest = parsed[1]
        try:
            return self._children[command].operation(task_list, rest)
        except:
            self.console.print(f"I don't know what the command {command} is.")
            self.console.print()

    def name(self, parent_name: str = "") -> None:
        for child_command in self._children:
            self._children[child_command].name(parent_name + " " + child_command)


class AddProject(Leaf):
    def operation(self, task_list: TaskList, input_string: str) -> str:
        name = input_string.strip()
        if len(name) == 0:
            self.console.print("No input_string provided")
            return
        tasks = task_list.get_tasks()
        tasks[name] = []
        task_list.set_tasks(tasks)
        return


class AddTask(Leaf):
    def operation(self, task_list: TaskList, input_string: str) -> str:
        arguments = input_string.strip()
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

    def operation(self, task_list: TaskList, input_string: str) -> str:
        root_command.name()


class Show(Leaf):
    def operation(self, task_list: TaskList, input_string: str) -> str:
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

    def operation(self, task_list: TaskList, input_string: str) -> str:
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


### INIT ###

console = Console(sys.stdin, sys.stdout)

root_command = Composite(console)

add_command = Composite(console)
add_project = AddProject(["project name"], console)
add_task = AddTask(["project name", "task description"], console)
add_command.add("project", add_project)
add_command.add("task", add_task)
root_command.add("add", add_command)

show_command = Show([], console)
root_command.add("show", show_command)

check_command = Check(["task ID"], console, True)
root_command.add("check", check_command)

uncheck_command = Check(["task ID"], console, False)
root_command.add("uncheck", uncheck_command)

help_command = Help([], console, add_command)
root_command.add("help", help_command)

task_list = TaskList()

### BEHAVIOR ###

while True:
    command = console.input("> ")
    root_command.operation(task_list, command)
