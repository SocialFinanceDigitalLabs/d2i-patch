from typing import Dict, List, Optional

from ._base import Component


class Select(Component):
    def __init__(
        self,
        id: str,
        title: str,
        options: List[Dict[str, str]],
        auto_action: Optional[str] = None,
    ):
        super().__init__(id=id)
        self.title = title
        self.options = options or []
        self.auto_action = auto_action
