from task_list.task.task_list import TaskList
from task_list.command.app_commands import AddProject, AddTask, Show, Help, Check, Quit
from task_list.command.command import Composite
from task_list.controller import Controller

from task_list.singleton import SingletonMeta


class TaskListApp(metaclass=SingletonMeta):
    def __init__(self, console):
        self.console = console

        root_command = Composite(console)

        quit_command = Quit([], console)
        root_command.add("quit", quit_command)

        show_command = Show([], console)
        root_command.add("show", show_command)

        add_command = Composite(console)
        add_project = AddProject(["project name"], console)
        add_task = AddTask(["project name", "task description"], console)
        add_command.add("project", add_project)
        add_command.add("task", add_task)
        root_command.add("add", add_command)

        check_command = Check(["task ID"], console, True)
        root_command.add("check", check_command)

        uncheck_command = Check(["task ID"], console, False)
        root_command.add("uncheck", uncheck_command)

        help_command = Help([], console, root_command)
        root_command.add("help", help_command)

        task_list = TaskList()

        self.controller = Controller(root_command, task_list)

    def run(self):
        while True:
            command = self.console.input("> ")
            self.controller.process(command)
