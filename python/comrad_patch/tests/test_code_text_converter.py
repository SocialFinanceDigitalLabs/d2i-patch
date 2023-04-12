import matplotlib
import matplotlib.pyplot as plt
from pydantic import BaseModel

from comrad_patch.util.code import code_to_text, text_to_code

GLOBAL_VAR = 3


class DummyModel(BaseModel):
    a: int
    b: str


def simple_method(a, b):
    return a * b


def method_with_global_vars(a, b):
    return a * b * GLOBAL_VAR


def method_with_imports(a: int, b: str) -> DummyModel:
    return DummyModel(a=a, b=b)


def method_with_chilren_chart(entered_care, in_care, left_care):
    # creates chart that will be used for the app
    fig, ax = plt.subplots()

    labels = [
        "Number of children who entered care",
        "Number of children in care",
        "Number of children who left care",
    ]
    counts = [entered_care, in_care, left_care]

    ax.bar(labels, counts)

    ax.set_ylabel("Number of children")
    ax.set_title("Children in, entering and leaving care by year")

    return fig


def test_simple_method():
    func_string = code_to_text(simple_method)
    func = text_to_code(func_string)
    res = func(2, 3)
    assert res == 6


def test_method_with_global_vars():
    func_string = code_to_text(method_with_global_vars)
    func = text_to_code(func_string)
    res = func(2, 3)
    assert res == 18


def test_method_with_imports():
    func_string = code_to_text(method_with_imports)
    func = text_to_code(func_string)
    res = func(2, "this is a string")
    assert res.a == 2
    assert res.b == "this is a string"


def test_method_with_chart():
    func_string = code_to_text(method_with_chilren_chart)
    func = text_to_code(func_string)
    res = func(30, 40, 50)
    assert type(res) == matplotlib.figure.Figure
