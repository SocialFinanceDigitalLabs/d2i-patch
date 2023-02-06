class Button:
    #
    # text: TemplateString
    # action: str
    # disabled = False
    # variant: Literal["text", "contained", "outlined"] = "contained"
    # start_icon: str = None
    # end_icon: str = None

    def __init__(self, text: str, action: str):
        self.id = action
        self.text = text
        self.action = action

    def __json__(self):
        return dict(
            type="button",
            id=self.id,
            text=self.text,
            action=self.action,
        )
