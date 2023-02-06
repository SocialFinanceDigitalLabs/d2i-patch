class View:
    def __init__(self):
        self.components = []

    def action(self, action, data):
        input_components = [c for c in self.components if hasattr(c, "update")]
        if len(input_components) == 0:
            return None
