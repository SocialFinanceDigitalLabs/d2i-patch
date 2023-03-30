from ._page import Page
from .exceptions import PatchException


class Application:
    def __init__(self) -> None:
        self.session: dict = {"view": None}
        self.pages: list[Page] = []

    def add_page(self, page: Page):
        self.pages.append(page)

    def run(self):
        if not self.pages:
            raise PatchException("you must create a view first")
        self.session["view"] = self.pages[0].view.name