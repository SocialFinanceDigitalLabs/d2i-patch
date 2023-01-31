import React from "react";
import Plot from 'react-plotly.js';
import * as Plotly from "plotly.js";
import {ViewProps} from "../viewFactory";

export interface ChartComponentProps extends ViewProps {
  chart: string;
}

const ChartComponent = (props: ChartComponentProps) => {
  const {data, layout} = JSON.parse(props.chart)
  return (
    <Plot data={data as Plotly.Data[]} layout={layout as Plotly.Layout}/>
  )
}

export default ChartComponent;
