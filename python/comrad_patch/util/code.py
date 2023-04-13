from typing import Callable
import types

from pyodide_dill import dill


def code_to_text(func: Callable) -> str:
    """
    This function will attempt to access the source and globals of an object and write the source for these.
    """
    parts = []
    for name, mod in dill.detect.globalvars(func).items():
        parts.append(dill.source.importable(mod, alias=name))

    parts.append(dill.source.getsource(func))

    return "\n".join(parts)


def text_to_code(text: str, function_name: str):
    # Evaluate the input string to define the function in the current namespace
    exec(text, globals())

    func = globals()[function_name]
    # Make sure the object is actually a function
    if not isinstance(func, types.FunctionType):
        raise ValueError("Input does not define a function")

    return func
