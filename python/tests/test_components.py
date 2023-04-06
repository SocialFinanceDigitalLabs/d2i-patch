from comrad.server.components import Fragment


def test_fragment():
    fragment = Fragment([])
    assert fragment.render(None, None, None) == {
        "complete": True,
        "type": "Fragment",
        "components": tuple(),
    }
