from abc import ABC, abstractmethod, abstractproperty
from typing import Any, Callable, Iterable

from ..util.components import is_component_complete
from ._model import Model
from ._request import Request
from ._session import Session


class Component:
    def __init__(self, type_name: str = None) -> None:
        if type_name is None:
            type_name = type(self).__name__
        self.type = type_name

    def render(self, request: Request, session: Session, model: Model) -> Any:
        props = [
            p
            for p in dir(self)
            if not p.startswith("_") and not isinstance(getattr(self, p), (Callable,))
        ]
        return {p: getattr(self, p) for p in props}


class BoundComponent(Component, ABC):
    """
    A component that is bound to a model.
    """

    @abstractmethod
    def update(self, request: Request, session: Session, model: Model) -> Any:
        """for bound components, update the model"""
        raise NotImplementedError

    @abstractproperty
    def complete(self) -> bool:
        """for bound components, return True if the component is complete"""
        raise NotImplementedError


class ContainerComponent(BoundComponent):
    """
    A component that contains other components.
    """

    def __init__(self, components: Iterable[Component], type_name: str = None) -> None:
        super().__init__(type_name=type_name)
        self.__components = tuple(components)

    @property
    def components(self) -> Iterable[Component]:
        """return the components contained in this component"""
        return self.__components

    def update(self, request: Request, session: Session, model: Model) -> Any:
        """Calls update on all contained components."""
        for c in self.components:
            try:
                c.update(request, session, model)
            except AttributeError:
                pass

    @property
    def complete(self) -> bool:
        """Returns True if all contained components are complete (or are not bound)."""
        return all(is_component_complete(c) for c in self.components)
