from __future__ import annotations
from abc import ABC, abstractmethod

class Task(ABC):
    @abstractmethod
    def set_done(self, done: bool) -> None:
        pass

    @abstractmethod
    def is_done(self) -> bool:
        pass

    @abstractmethod
    def display(self) -> str:
        pass
