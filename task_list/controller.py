from task_list.command.command import Command
from task_list.task.task_list import TaskList


class Controller:
    def __init__(self, root_command: Command, task_list: TaskList):
        self.root_command = root_command
        self.task_list = task_list

    def process(self, user_input):
        self.root_command.operation(self.task_list, user_input)
