from __future__ import annotations
from abc import ABC, abstractmethod
from task.task_list import TaskList
from typing import Dict, List
from console import Console
import sys

class Command(ABC):

    def add(self, command_name: str, command: Command) -> None:
        pass

    def is_composite(self) -> bool:
        return False

    @abstractmethod
    def name(self, parent_name: str ) -> None:
        pass

    @abstractmethod
    def operation(self, task_list: TaskList, input_string: str) -> str:
        pass


class Leaf(Command):

    def __init__(self, arguments: List[str] , console: Console) -> None:
        self.arguments = arguments
        self.console = console

    def operation(self, task_list: TaskList, input_string: str) -> str:
        pass

    def name(self, parent_name: str ) -> None:
        name = parent_name + "".join([" <" + arg + ">" for arg in self.arguments])
        self.console.print(name)

class Composite(Command):
    def __init__(self) -> None:
        self._children: Dict[str, Command] = dict()

    def add(self, command_name: str, command: Command) -> None:
        self._children[command_name] = command

    def is_composite(self) -> bool:
        return True

    def operation(self, task_list: TaskList, input_string: str) -> str:
        parsed = input_string.split(" ", 1)
        command = parsed[0]
        rest = parsed[1]
        return self._children[command].operation(task_list, rest)

    def name(self, parent_name: str = "" ) -> None:
        for child_command, child in self._children:
            child.name(parent_name + " " + child_command)


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

class Help(Command):
    def __init__(self, arguments: List[str], console: Console, root_command: Command) -> None:
        self.arguments = arguments
        self.console = console
        self.root_command = root_command

    def operation(self, task_list: TaskList, input_string: str) -> str:
        root_command.name()

console = Console(sys.stdin, sys.stdout)

root_command = Composite()

add_command = Composite()
add_project = AddProject(["project name"], console)
add_task = AddTask(["project name", "task description"], console)
add_command.add("project", add_project)
add_command.add("task", add_task)

root_command.add("add", add_command)

help_command = Help([], console, add_command)
root_command.add("help", help_command)

