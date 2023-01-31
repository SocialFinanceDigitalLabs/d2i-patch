import React from "react";
import { Block } from "@sfdl/sf-mui-components";
import {RenderList, ViewProps} from "../viewFactory";

export interface FragmentComponentProps extends ViewProps {
  components: [any];
  padded?: boolean;
}

const FragmentComponent = (props: FragmentComponentProps) => {
  const wrap = props.padded ? Block : undefined;
  return (
      <RenderList wrap={wrap}>{props.components}</RenderList>
  )

}

export default FragmentComponent;
