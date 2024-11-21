

from Payload.payLoad import addBookPayload
from utilities.resources import ApiResources

def DummyAPIurl():
    url = ApiResources.endpoint1+ ApiResources.getpost
    return url

def DummyAPIheader():
    headers = {"Content-Type": "application/json"}
    return headers
def DummyAPIwrongurl():
    url = ApiResources.endpointwrong+ ApiResources.getpost
    return url