from typing import Any, Mapping


class Request:
    def __init__(self, page: str = None, data: Mapping[str, Any] = None) -> None:
        self._page = page or "index"
        self._data = data or {}

    @property
    def page(self) -> str:
        """the page to be displayed"""
        return self._page

    @property
    def data(self) -> Mapping[str, Any]:
        """the data to be displayed"""
        return self._data


class ForwardedRequest(Request):
    """A request that has been forwarded to another page."""

    def __init__(self, request: Request, page: str = None) -> None:
        super().__init__(page=page or request.page, data=request.data)
