from abc import ABC, abstractmethod, abstractproperty
from typing import Any, Iterable

from ..util.components import is_component_complete


class Component(ABC):
    @abstractmethod
    def render(self, request, session, model) -> Any:
        """render the component"""
        raise NotImplementedError


class BoundComponent(ABC):
    """
    A component that is bound to a model.
    """

    @abstractmethod
    def update(self, request, session, model) -> Any:
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

    def update(self, request, session, model) -> Any:
        for c in self.components:
            try:
                c.update(request, session, model)
            except AttributeError:
                pass

    @property
    def complete(self) -> bool:
        return all(is_component_complete(c) for c in self.components)
