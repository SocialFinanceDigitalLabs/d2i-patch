from abc import ABC, abstractmethod

from ..util.components import is_component_complete
from ._view import RedirectView, View


class Controller(ABC):
    @abstractmethod
    def do(self, request, session, model):
        """do next step: render the view or redirect to another view"""
        raise NotImplementedError


class DefaultController(Controller):
    """
    Default controller that updates all components in a view or redirects to the 'next' view.

    """

    def __init__(self, view: View, next: str):
        self.__view = view
        self.__next = next

    def do(self, request, session, model) -> View:
        components = self.__view.components
        for c in components:
            try:
                c.update(request, session, model)
            except AttributeError:
                pass

        if all(is_component_complete(c) for c in self.components):
            return RedirectView(self.__next)

        return self.__view
