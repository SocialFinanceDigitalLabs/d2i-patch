import json

from ..util.json import PatchEncoder


def redirect():
    pass


def json_response(obj):
    return json.loads(json.dumps(obj, cls=PatchEncoder))
