from typing import Iterable

from ._model import Model
from ._page import Page
from ._request import ForwardedRequest, Request
from ._router import Router
from ._session import Session


class Application:
    def __init__(self, router: Router) -> None:
        self.router = router

    def handle_request(
        self,
        request: Request,
        session: Session,
        model: Model,
    ):

        # Get page from router
        page = self.router.get_page(request, session, model)

        # Let controller do its thing and capture any internal redirects
        while page:
            view = page.do(request, session, model)

            try:
                page = self.router.get_page(
                    ForwardedRequest(request, page=view.redirect),
                    session,
                    model,
                )
            except AttributeError:
                page = None

        # Render and return the response
        return view.render(request, session, model)
