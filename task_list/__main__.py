import sys

from console import Console
from task_list_app import TaskListApp


def main():
    app = TaskListApp(Console(sys.stdin, sys.stdout))
    app.run()


if __name__ == "__main__":
    main()
