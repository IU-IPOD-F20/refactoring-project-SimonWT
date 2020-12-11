from behave import *


@given("we have behave installed")
def step_impl(context):
    pass


@when('we implement a test with "{thing}"')
def step_impl(context, thing):
    assert True is not False


@then('behave will test it for us with "{other_thing}"!')
def step_impl(context, other_thing):
    assert context.failed is False
