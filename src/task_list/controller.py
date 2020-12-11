from task_list.command.command import Command

class Controller():
    def __init__(self, command_list, task_list, console) -> None:
        self.command_list = command_list
        self.console = console
        self.task_list = task_list
    

    def process(self, input_string: str) -> None:
        for command in self.command_list:
            if (input_string.startswith(command.get_command())):
                args = input_string.replace(command.command, "")
                command.execute(self.task_list, args)
                return
        input_command = input_string.split(" ", 1)[0]
        self.console.print(f"I don't know what the command {input_command} is.")
        self.console.print()
