from .. import app
from . import components as C


class View:
    def __init__(self, components):
        self.components = components


class PatchServer:
    def __init__(self, app: app.PatchApp):
        self._state = {}

        self._views = []
        for v in app.views:
            components = []
            for c in v.components:
                if c.type == "NumberField":
                    c = C.NumberField(id=c.name, title=c.description)
                elif c.type == "Button":
                    c = C.Button(text=c.text, action=c.action)
                elif c.type == "Chart":
                    c = C.Chart(code=c.code, function_name=c.function_name)
                elif c.type == "Paragraph":
                    c = C.Paragraph(text=c.text)
                else:
                    raise ValueError(c.type)
                components.append(c)

            self._views.append(View(components))

    def action(self, action, data):
        for v in self._views:
            response = self.view_action(v, action, data)
            if response:
                return response

    def view_action(self, view, action, data):
        if data:
            for c in view.components:
                if hasattr(c, "update"):
                    c.update(self._state, data)

        ready = [
            c.is_ready(self._state) for c in view.components if hasattr(c, "is_ready")
        ]
        if len(ready) > 0 and all(ready):
            return None

        return dict(
            view=dict(type="boxpage", components=tuple(view.components)),
            state=self._state,
        )
