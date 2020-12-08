from __future__ import annotations
from abc import ABC, abstractmethod

class Command(ABC):
   
    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def name(self) -> str:
        pass
        # return self.command + (" <" + s + ">" for arg in self.arguments)