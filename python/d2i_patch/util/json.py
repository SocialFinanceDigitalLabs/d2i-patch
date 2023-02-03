from json import JSONEncoder

from ..util.date import format_date


class PatchEncoder(JSONEncoder):
    def default(self, obj):
        try:
            obj = obj.__json__()
        except AttributeError:
            pass

        try:
            obj = format_date(obj)
        except AttributeError:
            pass

        return obj
