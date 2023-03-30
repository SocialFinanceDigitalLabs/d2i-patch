from ._page import Page
from .exceptions import PatchException


class Application:
    def __init__(self) -> None:
        self.pages: list[Page] = []

    def add_page(self, page: Page):
        self.pages.append(page)

    def handle_request(self, request, session, model):

        # Get page from router
        page = self.router.get_page(request, session, model)

        # Let controller do its thing and capture any internal redirects
        while page:
            view = page.controller.do(request, session, model)

            try:
                page = self.router.get_page_by_name(view.redirect)
            except AttributeError:
                page = None

        # Render and return the response
        return view.render(request, session, model)
