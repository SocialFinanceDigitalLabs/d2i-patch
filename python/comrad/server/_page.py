from typing import Callable, Iterable, Mapping, Union

from ..components import Component
from ._controller import Controller, DefaultController
from ._view import View


class Page:
    def __init__(
        self,
        name: str,
        controller: Union[Controller, Mapping, str],
        components: Iterable[Component] = None,
    ) -> None:
        self.__name = name
        self.__view = View(name=name, components=components)

        if isinstance(controller, str):
            controller = DefaultController(self.__view, next=controller)
        elif isinstance(controller, Mapping):
            controller = DefaultController(self.__view, **controller)

        self.__controller = controller

    @property
    def controller(self) -> Controller:
        """the controller for this page"""
        return self.__controller

    @property
    def view(self) -> View:
        """the view for this page"""
        return self.__view

    @property
    def name(self) -> str:
        """the name of this page"""
        return self.__name
