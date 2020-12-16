import sys

from task_list.console import Console
from task_list.app import TaskListApp


def main():
    app = TaskListApp(Console(sys.stdin, sys.stdout))
    app.run()


if __name__ == "__main__":
    main()
