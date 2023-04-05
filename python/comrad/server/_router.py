from abc import ABC, abstractmethod
from typing import Iterable, Tuple

from ._model import Model
from ._page import Page
from ._request import Request
from ._session import Session

DEFAULT_PAGE_NAME = "index"


class Router(ABC):
    @abstractmethod
    def get_page(
        self,
        request: Request,
        session: Session,
        model: Model,
    ) -> Page:
        raise NotImplementedError


class DefaultRouter(Router):
    """
    The default router is a name-based router that routes based on the
    page name in the request or the default page name if no page name.
    """

    def __init__(
        self, pages: Iterable[Page], default_page_name=DEFAULT_PAGE_NAME
    ) -> None:
        self._pages = tuple(pages)
        self._default_page_name = default_page_name
        self._page_index = {p.name: p for p in self._pages}

    @property
    def pages(self) -> Tuple[Page]:
        return self._pages

    def get_page(self, request: Request, session, model) -> Page:
        page_name = request.page or self._default_page_name
        return self.get_page_by_name(page_name)

    def get_page_by_name(self, page_name: str) -> Page:
        return self._page_index[page_name]
