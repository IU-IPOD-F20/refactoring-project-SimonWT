from task_list.task.task_list import TaskList
from task_list.command.app_commands import AddProject, AddTask, Show, Help, Check
from task_list.command.command import Composite

class TaskListApp:
    def __init__(self, console):
        self.console = console
    
        self.root_command = Composite(console)

        add_command = Composite(console)
        add_project = AddProject(["project name"], console)
        add_task = AddTask(["project name", "task description"], console)
        add_command.add("project", add_project)
        add_command.add("task", add_task)
        self.root_command.add("add", add_command)

        show_command = Show([], console)
        self.root_command.add("show", show_command)

        check_command = Check(["task ID"], console, True)
        self.root_command.add("check", check_command)

        uncheck_command = Check(["task ID"], console, False)
        self.root_command.add("uncheck", uncheck_command)

        help_command = Help([], console, self.root_command)
        self.root_command.add("help", help_command)

        self.task_list = TaskList()


    def run(self):
        while True:
            command = self.console.input("> ")
            self.root_command.operation(self.task_list, command)
