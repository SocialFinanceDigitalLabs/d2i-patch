from typing import Callable

from pyodide_dill import dill


def code_to_text(func: Callable) -> str:
    """
    This function will attempt to access the source and globals of an object and write the source for these.
    """
    value = ""
    for name, mod in dill.detect.globalvars(func).items():
        value += dill.source.importable(mod, alias=name)

    value += "\n"
    value += dill.source.getsource(func)
    value += f"\n{func.__name__}"

    value = "\n".join(["" if line.isspace() else line for line in value.splitlines()])
    return value
