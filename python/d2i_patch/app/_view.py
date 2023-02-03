from typing import List

from pydantic import BaseModel

from ._components import Component


class View(BaseModel):
    name: str = None
    components: List[Component]
