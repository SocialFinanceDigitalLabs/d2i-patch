from ._base import Component


class FileUpload(Component):
    def __init__(self, id: str, title: str, action: str):
        super().__init__(id=id)
        self.title = title
        self.action = action
