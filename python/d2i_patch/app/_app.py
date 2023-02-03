from typing import List

from ._base import BaseComponent
from ._view import View


class PatchApp(BaseComponent):
    name: str
    views: List[View]

    def __init__(self, name: str, views: List[View], **kwargs):
        if name:
            kwargs["name"] = name
        if views:
            kwargs["views"] = views
        super().__init__(**kwargs)
