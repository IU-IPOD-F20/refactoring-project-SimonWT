from task_list.command.quite_command import QuitCommand
from task_list.command.help_command import HelpCommand
from task_list.command.add_project_command import AddProjectCommand
from task_list.command.show_command import ShowCommand
from task_list.command.add_task_command import AddTaskCommand
from task_list.command.check_command import CheckCommand
from task_list.command.uncheck_command import UncheckCommand
from task_list.controller import Controller

from task_list.task.task_list import TaskList

class TaskListApp():
    def __init__(self, console):
        self.console = console
        task_list = TaskList()
        quite = QuitCommand()
        add_project = AddProjectCommand(console)
        add_task = AddTaskCommand(console)
        check = CheckCommand(console)
        uncheck = UncheckCommand(console)
        show = ShowCommand(console)
        command_list = [quite, show, add_project, add_task, check, uncheck]
        helpe = HelpCommand(command_list, console)
        command_list.append(helpe)
        self.controller = Controller(command_list, task_list, console)

    def run(self):
        while True: 
            command = self.console.input("> ")
            self.controller.process(command)
    

