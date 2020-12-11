from typing import Dict, List
from task_list.task.task import Task


class TaskList:
    def __init__(self):
        self.tasks: Dict[str, List[Task]] = dict()
        self.last_id: int = 0

    def get_tasks(self) -> Dict:
        return self.tasks

    def set_tasks(self, tasks: Dict) -> None:
        self.tasks = tasks

    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id
