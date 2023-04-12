from comrad_patch.controller import Controller


def test_controller_with_only_previous_page():
    controller = Controller(previous="previous page")
    assert controller.previous == "previous page"
    assert controller.next == None


def test_controller_with_only_next_page():
    controller = Controller(next="next page")
    assert controller.next == "next page"
    assert controller.previous == None


def test_controller_with_both_previous_and_next_page():
    controller = Controller(next="next page", previous="previous page")
    assert controller.next == "next page"
    assert controller.previous == "previous page"
