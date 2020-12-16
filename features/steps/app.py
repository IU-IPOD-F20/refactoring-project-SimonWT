import sys
from io import StringIO

from behave import *

from task_list.console import Console
from task_list.task_list_app import TaskListApp


@given("Created task list app")
def step_impl(context):
    context.out = StringIO()
    context.app = TaskListApp(Console(sys.stdin, context.out))


@when("Execute help command")
def step_impl(context):
    context.app.controller.process("help")
    context.help_msg = context.out.getvalue()


@when("Execute quit command")
def step_impl(context):
    try:
        context.app.controller.process("quit")
    except SystemExit as se:
        context.exit = se


@when("Execute show command")
def step_impl(context):
    context.app.controller.process("show")
    context.help_msg = context.out.getvalue()


@then("Get description of commands")
def step_impl(context):
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


@then("Quit from main app")
def step_impl(context):
    assert isinstance(context.exit, SystemExit)
    assert context.exit.code == 0


@then("Show nothing")
def step_impl(context):
    help_msg = """"""
    assert context.help_msg == help_msg
