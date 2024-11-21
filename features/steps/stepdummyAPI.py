import time

import requests
from behave import given,when, then


from RestAPIValidation.dummyvaliadtion import DummyAPIurl, DummyAPIheader, DummyAPIwrongurl


@given('Getting the url header of dummy api')
def precondtion(context):
    context.url=DummyAPIurl()
    context.headers=DummyAPIheader()
@given('Getting the wrong url of dummy api')
def precondtion(context):
    context.url=DummyAPIwrongurl()
    context.headers=DummyAPIheader()
@when('sending the call to the server')
def calling_data(context):
    context.response = requests.get(context.url, headers=context.headers)

@then('validating the response status as {statusCode:d}')
def retrieve_data(context, statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode

@then('validating the response message as {userID:d}')
def re_data(context, userID):
    time.sleep(10)
    print(context.response.text)
    # assert context.response.text=="Hey ya! Great to see you here. Btw, nothing is configured for this request path. Create a rule and start building a mock API."
    print(context.response.text)
    data=context.response.json()
    # response_json = simplejson.loads(context.response.text)
    UserID=data[0]['userId']
    assert UserID == userID