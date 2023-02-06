from ._base import Component


class DateSelect(Component):
    def __init__(self, id: str, title: str):
        super().__init__(id=id)
        self.title = title
