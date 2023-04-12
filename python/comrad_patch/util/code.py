from base64 import b64decode, b64encode
from typing import Callable

from pyodide_dill import dill


def code_to_text(func: Callable) -> str:
    """
    This function will attempt to access the source and globals of an object and write the source for these.
    """
    func_in_bytes = dill.dumps(func, recurse=True)
    return b64encode(func_in_bytes).decode()


def text_to_code(text: str):
    return dill.loads(b64decode(text.encode()))
