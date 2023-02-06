from .. import app as A
from . import PatchServer
from . import components as C


class BootstrapServer:
    def __init__(self):
        self.state = {}

    def action(self, action, data):
        if "app" in self.state:
            app = self.state["app"]
            return app.action(action, data)

        elif data and "app" in data:
            app_data = A.PatchApp.parse_raw(data["app"])
            self.state["app"] = PatchServer(app_data)
            return self.state["app"].action(action, data)

        return dict(
            view=dict(
                type="boxpage",
                components=[
                    C.Paragraph(
                        text="Welcome to d2i-patch. Please upload an app.json file."
                    ),
                    C.TextField(id="app", title="App JSON"),
                    C.Button(text="Upload", action="upload"),
                ],
            ),
            state=self.state,
        )
