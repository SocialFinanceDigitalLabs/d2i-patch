class TextField:
    def __init__(
        self,
        title: str,
        id: str,
        input_props: dict = None,
        start_icon: str = None,
        end_icon: str = None,
    ):
        self._type = "TextField"
        self.id = id
        self.title = title
        self.input_props = input_props or {}
        self.start_icon = start_icon
        self.end_icon = end_icon

    def update(self, state, data):
        state[self.id] = data.get(self.id)

    def is_ready(self, state):
        return state.get(self.id) is not None

    def __json__(self):
        return dict(
            type=self._type,
            id=self.id,
            title=self.title,
            input_props=self.input_props,
            start_icon=self.start_icon,
            end_icon=self.end_icon,
        )


class NumberField(TextField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.input_props = (dict(inputMode="numeric", pattern=r"[0-9]+(\.[0-9]+)?"),)

    def update(self, state, data):
        state[self.id] = data.get(self.id)
        if state[self.id] is not None:
            state[self.id] = float(state[self.id])
