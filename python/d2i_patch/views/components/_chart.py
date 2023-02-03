from ._base import Component


class Chart(Component):
    def __init__(
        self,
        renderer: Callable[["DemandModellingState", "..."], go.Figure],
        render_args: dict = None,
        **kwargs
    ):
        super().__init__(**kwargs)
        self.__renderer = renderer
        self.__render_args = render_args or {}

    @property
    def chart(self):
        try:
            chart = self.__renderer(self.__state, **self.__render_args)
        except:
            logger.exception("Error rendering chart")
            chart = placeholder("Error rendering chart")
        if isinstance(chart, go.Figure):
            chart = plotly.io.to_json(chart, pretty=False)
        else:
            raise ValueError("Renderer must return a plotly.graph_objects.Figure")
        return chart
