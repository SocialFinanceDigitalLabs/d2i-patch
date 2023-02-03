from typing import List

from ._base import Component
from ._button import Button


class ButtonBar(Component):
    buttons: List[Button]
