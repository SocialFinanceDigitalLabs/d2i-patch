from d2i_patch.app import *
from d2i_patch.views.components._button import TemplateString
from matplotlib import pyplot as plt


def _test_encoder(obj):
    if isinstance(obj, TemplateString):
        return f"Kaj: {obj.value}"
    return obj


def plot_function():
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot([1, 2, 3], [2, 3, 4], color="blue")
    return fig


def test_to_json():
    view = View(
        components=[
            Paragraph("Hello"),
            Button("World"),
            Chart(plot_function),
        ]
    )

    doc = view.json()

    new_view = View.parse_raw(doc)

    assert new_view == view

    assert len(new_view.components) == len(view.components)

    assert new_view.components[0].text == "Hello"
    assert new_view.components[1].text == "World"

    my_globals = {}
    exec(new_view.components[2].code, my_globals)

    assert my_globals["plot_function"].__name__ == "plot_function"
