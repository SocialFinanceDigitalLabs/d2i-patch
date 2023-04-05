from abc import ABC, abstractmethod, abstractproperty
from typing import Any, Iterable

from ..util.components import is_component_complete
from ._model import Model
from ._request import Request
from ._session import Session


class Component(ABC):
    @abstractmethod
    def render(self, request: Request, session: Session, model: Model) -> Any:
        """render the component"""
        raise NotImplementedError


class BoundComponent(Component):
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

    @abstractproperty
    def components(self) -> Iterable[Component]:
        """return the components contained in this component"""
        raise NotImplementedError

    def update(self, request: Request, session: Session, model: Model) -> Any:
        for c in self.components:
            try:
                c.update(request, session, model)
            except AttributeError:
                pass

    @property
    def complete(self) -> bool:
        return all(is_component_complete(c) for c in self.components)
