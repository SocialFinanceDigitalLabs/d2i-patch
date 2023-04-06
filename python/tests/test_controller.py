from unittest.mock import MagicMock, Mock, PropertyMock

from comrad.server import DefaultController


def test_default_controller_no_logic():
    class TestView:
        pass

    view = TestView()

    # Test view has no logic - so controller just returns the view
    ctrl = DefaultController(view, "next_view")
    assert ctrl.do(None, None, None) == view


def test_default_controller_incomplete():
    view = MagicMock()
    type(view).complete = PropertyMock(return_value=False)

    # View returns incomplete - so controller returns the view
    ctrl = DefaultController(view, "next_view")
    assert ctrl.do(None, None, None) == view

    view.update.assert_called_once()


def test_default_controller_complete():
    view = MagicMock()
    type(view).complete = PropertyMock(return_value=True)

    # View returns complete - so controller returns a redirectview
    ctrl = DefaultController(view, "next_view")
    assert ctrl.do(None, None, None).redirect == "next_view"

    view.update.assert_called_once()
