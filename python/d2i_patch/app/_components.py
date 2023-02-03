from typing import Callable, Literal, Optional, Union

from d2i_patch.util.code import code_to_text
from pydantic import BaseModel


class NumberField(BaseModel):
    type: Literal["NumberField"] = "NumberField"
    name: str
    description: Optional[str] = None

    def __init__(
        self, name: Optional[str] = None, description: Optional[str] = None, **kwargs
    ):
        if name:
            kwargs["name"] = name
        if description:
            kwargs["description"] = description
        super().__init__(**kwargs)


class Paragraph(BaseModel):
    type: Literal["Paragraph"] = "Paragraph"
    text: str

    def __init__(self, text: Optional[str] = None, **kwargs):
        if text:
            kwargs["text"] = text
        super().__init__(**kwargs)


class Button(BaseModel):
    type: Literal["Button"] = "Button"
    text: str
    action: str = None

    def __init__(self, text: Optional[str] = None, **kwargs):
        if text:
            kwargs["text"] = text
        super().__init__(**kwargs)


class Chart(BaseModel):
    type: Literal["Chart"] = "Chart"
    code: Optional["str"] = None

    def __init__(self, generator: Callable = None, **kwargs):
        super().__init__(**kwargs)
        self.set_generator(generator)

    def set_generator(self, value):
        if value:
            self.code = code_to_text(value)


Component = Union[Paragraph, Button, NumberField, Chart]
