import uuid


def _uid_factory():
    return uuid.uuid4().hex


class BaseComponent:
    def __init__(self, type: str, id: str = None):
        self.type = type
        self.id = id or _uid_factory()

    def __json__(self):
        return dict(id=self.id, type=self.type)
