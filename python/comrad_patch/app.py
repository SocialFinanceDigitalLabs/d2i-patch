from .page import Page
import yaml


class Application:
    def __init__(self) -> None:
        self.__pages: list[Page] = []

    def add_page(self, page: Page):
        self.__pages.append(page)

    @property
    def pages(self) -> list[Page]:
        """the pages of this app"""
        return self.__pages

    def export(self):
        return {"pages": [page.export() for page in self.__pages]}

    def yaml(self):
        obj_representation = self.export()
        return yaml.safe_dump(obj_representation, sort_keys=False)