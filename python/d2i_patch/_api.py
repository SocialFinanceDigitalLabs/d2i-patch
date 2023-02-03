from prpc_python import RpcApp

from ._controller import PatchController
from .views.util import json_response

app = RpcApp("D2I PATCH")
controller = PatchController()


@app.call
def reset():
    global controller
    controller = PatchController()


@app.call
def action(action, data=None):
    return json_response(controller.action(action, data))
