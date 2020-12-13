import sys
from io import StringIO

from behave import *

from task_list.console import Console
from task_list.task_list_app import TaskListApp


@given("Created task list app")
def step_impl(context):
    context.out = StringIO()
    context.app = TaskListApp(Console(sys.stdin, context.out))


@when("execute help command")
def step_impl(context):
    context.app.controller.process("help")
    context.help_msg = context.out.getvalue()


@then("get description of commands")
def step_impl(context):
    print(context.help_msg)
    help_msg = """Commands:
  quit
  show
  add project <project name>
  add task <project name> <task description>
  check <task ID>
  uncheck <task ID>
  help
"""
    assert context.help_msg == help_msg
