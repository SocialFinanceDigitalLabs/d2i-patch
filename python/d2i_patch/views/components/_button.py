from typing import Literal

from ._base import Component, TemplateString


class Button(Component):
    text: TemplateString
    action: str
    disabled = False
    variant: Literal["text", "contained", "outlined"] = "contained"
    start_icon: str = None
    end_icon: str = None

    def __init__(self, **data):
        if "action" not in data and "text" in data:
            data["action"] = data["text"]
        super().__init__(**data)

    class Config:
        arbitrary_types_allowed = True
