import base64
import inspect
import io

import matplotlib as mpl

mpl.use("Agg")

from matplotlib import pyplot as plt


class Chart:
    def __init__(self, code: str, function_name: str):

        context = {}
        exec(code, context)

        self._func = context[function_name]
        self._args = inspect.getfullargspec(self._func)
        self._state = {}

    def update(self, state, data):
        self._state = state

    def __json__(self):
        fig = self._func(**self._state)
        buf = io.BytesIO()
        fig.savefig(buf, format="svg")
        data = buf.getvalue()

        return dict(
            type="chart",
            chart_type="svg",
            chart=base64.b64encode(data).decode("utf-8"),
        )
