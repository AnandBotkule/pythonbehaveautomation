import requests
import json

from Payload.payLoad import addBookPayload
from utilities.resources import ApiResources

def AssuredAPIurl():
    url = 'http://216.10.245.166'+ ApiResources.addBook
    return url

def AssuredAPIheader():
    headers = {"Content-Type": "application/json"}
    return headers

def AssuredAPIpayLoad():
    payLoad = addBookPayload("maewsddfppt","4452")
    return payLoad












