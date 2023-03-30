import importlib
import importlib.machinery
import importlib.util
import sys


def new_module(mod_name):

    spec = importlib.machinery.ModuleSpec(mod_name, None)
    return importlib.util.module_from_spec(spec)


def create_module(mod_name, object_list):

    mod = new_module(mod_name)
    for obj in object_list:
        setattr(mod, obj.__name__, obj)

    sys.modules[mod_name] = mod
    return mod


def test_create_module():
    def my_func():
        pass

    create_module("my_module", [my_func])

    import my_module

    assert my_module.my_func == my_func
