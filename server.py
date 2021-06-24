# from sanic import Sanic
# from sanic.response import json

# app = Sanic()

# @app.route("/")
# async def test(request):
#     return json({"hello": "world"})

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8000)

from sanic import Sanic
from sanic import response
from sanic.response import json
from sanic.log import logger
from functions.test_fc import *

app = Sanic("My First Sanic App")


# webapp path defined used route decorator
@app.route("/")
def run(request):
    return response.text("Hello World !")


@app.route("/getjson")
def run(request):
    return testHello()
    # return json({"hello": "world"})


@app.route('/items/<item>')
async def item_handler(request, item):
    return json({"item": item})
#    print('Item - {}'.format(item))

@app.get('/gettest')
async def get_test(request):
    return json({
        "name": "ratherz", 
        "firstName": "sopon", 
        "lastName": "Ngernsawang"
        })

@app.route("/post", methods =['POST'])
def on_post(request):
    print(request.json)
    try:
        return response.json({"content": request.json})
    except Exception as ex:
        import traceback
        logger.error(f"{traceback.format_exc()}")


# debug logs enabled with debug = True
app.run(host="localhost", port=5050, debug=True)
