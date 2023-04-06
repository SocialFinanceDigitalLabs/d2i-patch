from abc import ABC, abstractmethod

from ._view import RedirectView, View


class Controller(ABC):
    @abstractmethod
    def do(self, request, session, model) -> View:
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
        try:
            self.__view.update(request, session, model)
        except AttributeError:
            pass

        try:
            if self.__view.complete:
                return RedirectView(self.__next)
        except AttributeError:
            pass

        return self.__view
