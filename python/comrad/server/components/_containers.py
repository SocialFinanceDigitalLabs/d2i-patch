from typing import Iterable

from .. import Component, ContainerComponent

#
# Container and Layout components
#


class Fragment(ContainerComponent):
    """
    A fragment is a container component that does not render a container element.
    """

    pass


class BoxPage(ContainerComponent):
    """
    The box page is a layout component that renders the child components in a, well, box... This is the
    standard 'full page' layout.
    """

    pass


class SidebarPage(ContainerComponent):
    """
    The sidebar page is a layout component that renders the child components in a sidebar and main
    content area. The sidebar is fixed and the main content scrolls.
    """

    def __init__(self, sidebar: Iterable[Component], main: Iterable[Component]) -> None:
        super().__init__(tuple(self.sidebar + self.main))
        self.sidebar = tuple(sidebar)
        self.main = tuple(main)


class Expando(ContainerComponent):
    """
    The expando component is a container component that renders the child components in a collapsible
    expando.
    """

    def __init__(self, title: str, components: Iterable[Component]) -> None:
        super().__init__(tuple(components))
        self.title = title
