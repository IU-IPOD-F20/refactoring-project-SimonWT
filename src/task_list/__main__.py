import sys

from src.task_list.console import Console
from src.task_list.task_list_app import TaskListApp


def main():
    app = TaskListApp(Console(sys.stdin, sys.stdout))
    app.run()


if __name__ == "__main__":
    main()
