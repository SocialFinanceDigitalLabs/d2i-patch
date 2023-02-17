class Button:
    def __init__(self, text: str, action: str):
        self.id = action
        self.text = text
        self.action = action

    def __json__(self):
        return dict(
            type="Button",
            id=self.id,
            text=self.text,
            action=self.action,
        )
