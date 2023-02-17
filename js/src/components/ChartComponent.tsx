import React from "react";
import Plot from 'react-plotly.js';
import * as Plotly from "plotly.js";
import {ViewProps} from "../viewFactory";
import { useSelector } from "react-redux";
import { selectStateProperty } from "features/model/modelSlice";
import ErrorComponent from "./ErrorComponent";

export interface ChartComponentProps extends ViewProps {
  chart: string;
  chart_type: string;
}

const ChartComponent = (props: ChartComponentProps) => {
  const chartData = useSelector(selectStateProperty(props.id));
  if (chartData) {
    const {type, data} = chartData;
    if (type === 'svg') {
      const chartData = atob(data);
      return (
        <div className="content" dangerouslySetInnerHTML={{__html: chartData}}></div>
      )
    } else {
      const {chartData, layout} = JSON.parse(data)
      return (
        <Plot data={chartData as Plotly.Data[]} layout={layout as Plotly.Layout}/>
      )
    }
  } else {
    return (
      <ErrorComponent text="No chart data..."/>
    )

  }
}

export default ChartComponent;
