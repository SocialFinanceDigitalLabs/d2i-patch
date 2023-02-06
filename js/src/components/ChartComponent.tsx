import React from "react";
import Plot from 'react-plotly.js';
import * as Plotly from "plotly.js";
import {ViewProps} from "../viewFactory";

export interface ChartComponentProps extends ViewProps {
  chart: string;
  chart_type: string;
}

const ChartComponent = (props: ChartComponentProps) => {
  if (props.chart_type === 'svg') {
    const data = atob(props.chart);
    console.log(data);
    return (
      <div className="content" dangerouslySetInnerHTML={{__html: data}}></div>
    )
  } else {
    const {data, layout} = JSON.parse(props.chart)
    return (
      <Plot data={data as Plotly.Data[]} layout={layout as Plotly.Layout}/>
    )
  }
}

export default ChartComponent;
