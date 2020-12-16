from task_list.task.simple_task import SimpleTask


class DeadlineTask(SimpleTask):
    def __init__(self, id_: int, description: str, done: bool):
        super().__init__()
        self.deadline = None

    def set_deadline(deadline: str) -> None:
        self.dedaline = deadline
