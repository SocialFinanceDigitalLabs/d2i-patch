import json
from unittest.mock import MagicMock

from comrad_patch import Application


def test_app_add_pages():
    page1 = MagicMock()
    page2 = MagicMock()

    app = Application()
    app.add_page(page1)
    app.add_page(page2)

    assert len(app.pages) == 2


def test_app_export():
    page = MagicMock()
    page.export.return_value = {
        "name": "index",
        "components": [{"name": "some component", "type": "NumberInput"}],
        "controller": {"next": "next page", "previous": None},
    }
    app = Application()
    app.add_page(page)

    assert app.export() == {
        "pages": [
            {
                "name": "index",
                "components": [{"name": "some component", "type": "NumberInput"}],
                "controller": {"next": "next page", "previous": None},
            }
        ]
    }


def test_app_yaml():
    page = MagicMock()
    page.export.return_value = {
        "name": "Mocked page",
    }
    app = Application()
    app.add_page(page)

    result = app.yaml()
    expected_result = "pages:\n- name: Mocked page\n"
    assert result == expected_result


def test_json():
    page = MagicMock()
    page.export.return_value = {
        "name": "Mocked page",
    }
    app = Application()
    app.add_page(page)

    result = app.json()
    expected_result = json.dumps({"pages": [{"name": "Mocked page"}]}, indent=4)
    assert result == expected_result
