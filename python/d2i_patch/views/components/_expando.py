from ._base import Component


class Expando(Component):
    def __init__(self, *components: Component, title: str, id: str = None):
        super().__init__(id=id)
        self.title = title
        self.components = components
