from d2i_patch.server.components import Fragment


def test_fragment():
    data = dict(
        type="Fragment",
        components=[
            dict(type="paragraph", text="Hello, world!"),
        ],
    )

    fragment = Fragment.parse_obj(data)
    assert fragment.components[0].text == "Hello, world!"
