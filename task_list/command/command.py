from __future__ import annotations
from abc import ABC, abstractmethod
from task_list.task.task_list import TaskList


class Command(ABC):
    @abstractmethod
    def execute(self, task_list: TaskList, arguments: str) -> None:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def get_command(self) -> str:
        pass
