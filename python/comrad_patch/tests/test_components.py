import matplotlib.pyplot as plt

from comrad_patch.components import Button, ButtonBar, Chart, NumberInput, TextInput


def test_button():
    button = Button("some text", "submit")

    assert button.text == "some text"
    assert button.action == "submit"
    assert button.type == "Button"


def test_button_with_handler():
    func = lambda x: x * 2
    button = Button("some text", handler=func)
    assert button.text == "some text"
    assert button.handler == func
    assert button.type == "Button"


def test_button_nbar():
    func = lambda x: x * 2
    button1 = Button("some text", "submit")
    button2 = Button("some text", handler=func)
    button_bar = ButtonBar([button1, button2])
    assert len(button_bar.buttons) == 2


def test_number_input():
    number_input = NumberInput("number input name", "some details", True)
    assert number_input.name == "number input name"
    assert number_input.description == "some details"
    assert number_input.required == True


def test_text_input():
    text_input = TextInput("text input name", True)
    assert text_input.name == "text input name"
    assert text_input.required == True


def test_chart():
    T = 3

    def children_in_care(entered_care, in_care, left_care):
        # creates chart that will be used for the app
        fig, ax = plt.subplots()

        labels = [
            "Number of children who entered care",
            "Number of children in care",
            "Number of children who left care",
        ]
        counts = [entered_care * T, in_care, left_care]

        ax.bar(labels, counts)

        ax.set_ylabel("Number of children")
        ax.set_title("Children in, entering and leaving care by year")

    chart = Chart(generator=children_in_care)

    assert chart.function_name == "children_in_care"
    assert type(chart.code) == str
