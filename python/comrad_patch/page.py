from typing import Optional, Iterable, Mapping, Union

from .components import Component
from .controller import Controller


class Page:
    def __init__(
        self,
        name: str,
        components: Iterable[Component],
        controller: Union[Controller, Mapping, str, None] = None,
    ) -> None:
        self.__name = name
        self.__components = components

        if isinstance(controller, str):
            controller = Controller(next=controller)
        elif isinstance(controller, Mapping):
            controller = Controller(**controller)

        self.__controller = controller

    @property
    def controller(self) -> Optional[Controller]:
        """the controller for this page"""
        return self.__controller

    @property
    def name(self) -> str:
        """the name of this page"""
        return self.__name

    @property
    def components(self) -> Iterable[Component]:
        """the name of this page"""
        return self.__components

    def export(self) -> dict:
        """returns a dict representation of the page"""
        return {
            "name": self.__name,
            "components": [component.dict() for component in self.__components],
            "controller": self.__controller.export() if self.__controller else None,
        }
