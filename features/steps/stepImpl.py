import requests
from behave import *

from RestAPIValidation import apiValidations
from RestAPIValidation.apiValidations import AssuredAPIurl, AssuredAPIheader, AssuredAPIpayLoad
from utilities.resources import *
from Payload.payLoad import addBookPayload

@given('the Book details which needs to be added to Library')
def step_impl(context):
    context.url = AssuredAPIurl()
    context.headers = AssuredAPIheader()
    context.payLoad = AssuredAPIpayLoad()


@when('we execute the AddBook PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url, json=context.payLoad , headers=context.headers, )


@then('book is successfully added')
def step_impl(context):
    print(context.response.json())
    response_json = context.response.json()
    context.bookId = response_json['ID']
    print(context.bookId)
    assert response_json["Msg"] == "successfully added"


@given('the Book details with {isbn} and {aisle}')
def step_impl(context,isbn,aisle):
    context.url = ApiResources.endpoint+ ApiResources.addBook
    # context.url = 'http://216.10.245.166'+ ApiResources.addBook
    context.headers = {"Content-Type": "application/json"}
    from Payload.payLoad import addBookPayload
    context.payLoad = addBookPayload(isbn, aisle);


@given('I have github auth credentials')
def step_impl(context):

    context.se = requests.session()
    context.se.auth = auth = ('rahulshettyacademy', "hello")


@when(u'I hit getRepo API of github')
def step_impl(context):
    context.response = context.se.get(ApiResources.githubRepo)


@then(u'status code of response should be {statusCode:d}')
def step_impl(context,statusCode):
    print(context.response.status_code)
    assert context.response.status_code == statusCode






