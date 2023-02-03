import logging

logger = logging.getLogger(__name__)


class BoxPage(Component):
    def __init__(self, *components, id: str = None):
        super().__init__(id=id)
        self.components = components


class SidebarPage(Component):
    def __init__(self, sidebar: list[Component], main: list[Component], id: str = None):
        super().__init__(id=id)
        self.sidebar = sidebar
        self.main = main
