import uuid
from typing import Any, Dict, Optional

from pydantic import BaseModel, Field
from pydantic.fields import ModelField


def _uid_factory():
    return uuid.uuid4().hex


class TestComponent(Component):
    name: str

    # def __init__(self, id=None, type_name=None):
    #     if id is None:
    #         id = uuid.uuid4().hex
    #     try:
    #         self.id = id
    #     except AttributeError:
    #         # If we override the ID property in the component
    #         pass
    #
    #     if type_name is None:
    #         type_name = type(self).__name__.lower()
    #     self.type = type_name
    #
    # def __json__(self):
    #     props = [p for p in dir(self) if not p.startswith("_")]
    #     return {p: getattr(self, p) for p in props}
    #
