from typing import Any, Dict


class Model:
    """
    The model is an object that is serialized and forwarded to the client application.
    It is used to store data that is needed by the client application, such as field values or validation errors.

    All values stored in the Model should be JSON-serializable.
    """

    def __init__(self) -> None:
        self.__data = {}
        self.__errors = {}

    @property
    def data(self) -> Dict[str, Any]:
        return self.__data

    @property
    def errors(self) -> Dict[str, Any]:
        return self.__errors
