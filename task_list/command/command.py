from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, List

from task_list.task.task_list import TaskList
from task_list.console import Console


class Command(ABC):
    @abstractmethod
    def name(self, parent_name: str) -> None:
        pass

    @abstractmethod
    def execute(self, task_list: TaskList, input_string: str) -> str:
        pass


class Leaf(Command):
    def __init__(self, arguments: List[str], console: Console) -> None:
        self.arguments = arguments
        self.console = console

    def execute(self, task_list: TaskList, input_string: str) -> str:
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

    def execute(self, task_list: TaskList, input_string: str) -> str:
        parsed = input_string.split(" ", 1)
        command = parsed[0]
        rest = ""
        if len(parsed) > 1:
            rest = parsed[1]

        if command in self._children:
            return self._children[command].execute(task_list, rest)
        else:
            self.console.print(f"I don't know what the command {command} is.")
            self.console.print()
            return

    def name(self, parent_name: str = "") -> None:
        for child_command in self._children:
            self._children[child_command].name(parent_name + " " + child_command)
