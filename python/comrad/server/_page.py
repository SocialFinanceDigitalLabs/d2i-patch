from abc import ABC, abstractmethod

from ._controller import Controller
from ._model import Model
from ._request import Request
from ._session import Session
from ._view import View


class Page(ABC):
    @property
    @abstractmethod
    def name(self) -> str:
        """the name of this page"""
        raise NotImplementedError

    @abstractmethod
    def do(self, request: Request, session: Session, model: Model) -> View:
        """do the page"""
        raise NotImplementedError


class MVCPage(Page):
    def __init__(self, name: str, controller: Controller, view: View) -> None:
        self._name = name
        self._controller = controller
        self._view = view

    @property
    def name(self) -> str:
        return self._name

    def do(self, request: Request, session: Session, model: Model) -> View:
        return self._controller.do(request, session, model)
