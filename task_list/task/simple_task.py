from task_list.task.task import Task


class SimpleTask(Task):
    def __init__(self, id_: int, description: str, done: bool) -> None:
        self.id = id_
        self.description = description
        self.done = done

    def set_done(self, done: bool) -> None:
        self.done = done

    def is_done(self) -> bool:
        return self.done

    def display(self) -> str:
        return f" [{'x' if self.is_done() else ' '}] " f"{self.id}: {self.description}"
