from typing import List

from ._base import Component


class Fragment(Component):
    components: List[Component]
    padded: bool = False
