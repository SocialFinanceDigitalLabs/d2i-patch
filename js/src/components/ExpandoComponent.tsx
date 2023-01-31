import React from "react";
import { Expando } from "@sfdl/sf-mui-components";
import { PaddedBox } from "pages/Pages.styles";
import { Block } from "@sfdl/sf-mui-components";
import {RenderList, ViewProps} from "../viewFactory";

export interface ExpandoComponentProps extends ViewProps {
  components: [any];
  title: string;
}

const ExpandoComponent = (props: ExpandoComponentProps) => {

  return (
    <PaddedBox>
      <Expando title={props.title} id={props.id}>
        <RenderList wrapper={Block}>{props.components}</RenderList>
      </Expando>
    </PaddedBox>
  )

}

export default ExpandoComponent;
