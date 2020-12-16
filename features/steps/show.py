from behave import *


@when("Execute show command")
def step_impl(context):
    context.app.controller.process(f"add project kek")
    context.app.controller.process("show")
    context.help_msg = context.out.getvalue()


@then("Show nothing")
def step_impl(context):
    help_msg = """"""
    assert context.help_msg == help_msg
