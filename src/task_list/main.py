from command.quiteCommand import QuitCommand
from command.helpCommand import HelpCommand
from console import Console
import sys 

console = Console(sys.stdin, sys.stdout)

quite = QuitCommand()
helpe = HelpCommand([quite], console)

while True:
    print("kek")
    helpe.execute()
    quite.execute()
    