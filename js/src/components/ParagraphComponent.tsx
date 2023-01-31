import React from "react";
import { Typography } from "@mui/material";
import {ViewProps} from "../viewFactory";

export interface ParagraphComponentProps extends ViewProps {
  text: string;
  strong: boolean;
}

const ParagraphComponent = (props: ParagraphComponentProps) => {
  const Wrapper = props.strong ? (props: any) => (<strong>{props.children}</strong>) : React.Fragment;
  return (
    <Typography>
        <Wrapper>
        {props.text}
        </Wrapper>
    </Typography>
  )
}

export default ParagraphComponent;
