from sanic.response import json

def testHello() :
    return json({"test": "TRest"})