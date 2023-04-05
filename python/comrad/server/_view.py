from abc import ABC, abstractmethod

from ._model import Model
from ._request import Request
from ._session import Session
from .components import ContainerComponent


class View(ABC):
    @abstractmethod
    def render(self, request: Request, session: Session, model: Model):
        """render the view"""
        raise NotImplementedError


class RedirectView(View):
    def __init__(self, page: str) -> None:
        self.__redirect = page

    @property
    def redirect(self) -> str:
        """redirect to another page"""
        return self.__redirect


class ComponentView(View):
    def __init__(self, component: ContainerComponent) -> None:
        self.__component = component

    def update(self, request: Request, session: Session, model: Model):
        self.__component.update(request, session, model)

    @property
    def complete(self) -> bool:
        return self.__component.complete

    def render(self, request: Request, session: Session, model: Model):
        return self.__component.render(request, session, model)
