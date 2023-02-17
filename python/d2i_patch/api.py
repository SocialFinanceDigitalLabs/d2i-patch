import logging
import time

from prpc_python import RpcApp

from .server import PatchServer
from .server._bootstrap import BootstrapServer
from .server.util import json_response

app = RpcApp("D2I PATCH")
server = BootstrapServer()

log = logging.getLogger(__name__)


@app.call
def action(action, data=None):
    log.debug("Action: %s; Data: %s", action, data)
    try:
        return json_response(server.action(action, data))
    except Exception as e:
        log.exception("Error in action: %s", e)
        raise e
