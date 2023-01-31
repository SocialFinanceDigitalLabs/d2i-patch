import React from "react";
import {Alert} from "@mui/material";

export interface ErrorComponentProps {
  text: string;
}

const ErrorComponent = (props: ErrorComponentProps) => {
  const text = props.text ? props.text : "An error occurred."
  return <Alert severity="error">{text}</Alert>
}

export default ErrorComponent;
