import base64
import inspect
import io

import matplotlib as mpl

from ._base import BaseComponent

mpl.use("Agg")


class Chart(BaseComponent):
    def __init__(self, code: str, function_name: str, **kwargs):
        super().__init__("Chart", **kwargs)

        context = {}
        exec(code, context)
        self._func = context[function_name]
        self._args = inspect.getfullargspec(self._func)

    def update(self, state, data):
        fig = self._func({**state, **data})
        buf = io.BytesIO()
        fig.savefig(buf, format="svg")
        fig_data = buf.getvalue()
        state[self.id] = {
            "type": "svg",
            "data": base64.b64encode(fig_data).decode("utf-8"),
        }

    def __json__(self):
        return dict(id=self.id, type="chart")
