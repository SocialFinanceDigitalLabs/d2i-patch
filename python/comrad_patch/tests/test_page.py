from unittest.mock import MagicMock, PropertyMock

from comrad_patch.page import Page


def test_page_with_controller_object():
    controller = MagicMock()
    controller.export.return_value = {"next": "next page", "previous": None}
    type(controller).next = PropertyMock(return_value="next page")

    component = MagicMock()
    component.dict.return_value = {"name": "some component", "type": "NumberInput"}

    page = Page(name="index", components=[component], controller=controller)

    assert page.controller == controller
    assert page.name == "index"
    assert page.components[0] == component
    assert page.export() == {
        "name": "index",
        "components": [{"name": "some component", "type": "NumberInput"}],
        "controller": {"next": "next page", "previous": None},
    }


def test_page_with_string_controller():
    component = MagicMock()
    component.dict.return_value = {"name": "some component", "type": "NumberInput"}

    page = Page(name="index", components=[component], controller="next page")

    assert page.export() == {
        "name": "index",
        "components": [{"name": "some component", "type": "NumberInput"}],
        "controller": {"next": "next page", "previous": None},
    }


def test_page_with_dict_controller():
    component = MagicMock()
    component.dict.return_value = {"name": "some component", "type": "NumberInput"}

    page = Page(name="index", components=[component], controller={"next": "next page"})

    assert page.export() == {
        "name": "index",
        "components": [{"name": "some component", "type": "NumberInput"}],
        "controller": {"next": "next page", "previous": None},
    }
