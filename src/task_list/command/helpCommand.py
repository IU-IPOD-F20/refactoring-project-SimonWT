from command.command import Command

class HelpCommand(Command):
    def __init__(self, command_list, console) -> None:
        self.command = "help"
        self.command_list = command_list
        self.console = console
    
    def execute(self) -> None:
        self.console.print("Commands:")
        for command in self.command_list:
            self.console.print("  " + command.name())

    def name(self) -> str:
        return self.command