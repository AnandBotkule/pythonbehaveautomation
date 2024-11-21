Feature: Validation of the API

  Scenario: positive scenario's of API
    Given Getting the url header of dummy api
    When sending the call to the server
    Then validating the response status as 200
    Then validating the response message as 1

  Scenario: Negative scenario's of API
    Given Getting the wrong url of dummy api
    When sending the call to the server
    Then validating the response status as 404