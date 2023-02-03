from ._base import Component


class TextField(Component):
    def __init__(
        self,
        id: str,
        title: str,
        input_props: dict = None,
        start_icon: str = None,
        end_icon: str = None,
    ):
        super().__init__(id=id)
        self.title = title
        self.input_props = input_props or {}
        self.start_icon = start_icon
        self.end_icon = end_icon
