from command.command import Command

class QuitCommand(Command):
    def __init__(self) -> None:
        self.command = "quit"
    
    def execute(self) -> None:
        quit()

    def name(self) -> str:
        return self.command #+ (" <" + s + ">" for arg in self.arguments)