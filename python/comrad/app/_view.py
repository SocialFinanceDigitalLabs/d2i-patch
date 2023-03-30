class View:
    def render(self, request, session, model):
        """render the view"""
        pass


class RedirectView:
    def __init__(self, page: str) -> None:
        self.__redirect = page

    @property
    def redirect(self) -> str:
        """redirect to another page"""
        return self.__redirect
