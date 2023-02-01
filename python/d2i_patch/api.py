from prpc_python import RpcApp


class T2DemandModellingSession:
    def __init__(self):
        self.state = DemandModellingState()
        self.views = {
            "datastore": views.DataStoreView(),
            "charts": views.ChartsView(),
        }

    @property
    def current_view(self):
        if self.state.datastore is None:
            return self.views["datastore"]
        else:
            return self.views["charts"]

    def action(self, action, data=None):
        if action != "init":
            self.state = self.current_view.action(action, self.state, data)

        return dict(
            view=self.current_view.render(self.state),
            state=dict(
                start_date=self.state.start_date,
                end_date=self.state.end_date,
                prediction_end_date=self.state.prediction_end_date,
                step_size=self.state.step_days,
                files=self.state.files,
                chart_filter=self.state.chart_filter,
                **self.state.costs,
                **self.state.cost_proportions,
                **self.state.adjustments,
            ),
            errors=self.state.errors,
        )


app = RpcApp("CS Demand Model")
dm_session = T2DemandModellingSession()


@app.call
def reset():
    global dm_session
    dm_session = T2DemandModellingSession()


@app.call
def action(action, data=None):
    return json_response(dm_session.action(action, data))
