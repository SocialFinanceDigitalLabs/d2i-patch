import React from "react";
import { Button, Icon } from "@mui/material";
import {ViewProps} from "../viewFactory";
import {useApi} from "../../hooks/api";
import {useSelector} from "react-redux";
import {selectModel} from "../../features/model/modelSlice";

export interface ButtonProps extends ViewProps {
  text: string,
  variant?: "text" | "contained" | "outlined" | undefined,
  action: string,
  disabled? : boolean,
  start_icon?: string;
  end_icon?: string;
}

const ButtonComponent = (props: ButtonProps) => {
  const { text, variant, action, disabled} = props;
  const model = useSelector(selectModel);
  const api = useApi();

  const onClick = () => {
    api.call(action, model);
  }

  const startIcon = props.start_icon ? <Icon>{props.start_icon}</Icon> : undefined;
  const endIcon = props.end_icon ? <Icon>{props.end_icon}</Icon> : undefined;

  return (
    <Button variant={variant || "contained"} onClick={onClick} disabled={disabled}
      startIcon={startIcon} endIcon={endIcon}
    >
      { text }
    </Button>
  )

}

export default ButtonComponent;
