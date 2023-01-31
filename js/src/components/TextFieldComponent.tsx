import React from "react";
import Icon from '@mui/material/Icon';
import InputAdornment from '@mui/material/InputAdornment';

import {ViewProps} from "../viewFactory";
import {Typography, TextField, Alert} from "@mui/material";
import {useDispatch, useSelector} from "react-redux";
import {selectStateProperty, updateStateProperty} from "../../features/model/modelSlice";
import { Block } from "@sfdl/sf-mui-components";
import {selectErrorsForProperty} from "../../features/error/errorSlice";

export interface TextFieldComponentProps extends ViewProps {
  input_props: any;
  title: string;
  start_icon?: string;
  end_icon?: string;
}

const TextFieldComponent = (props: TextFieldComponentProps) => {
  const dispatch = useDispatch();
  const value = useSelector(selectStateProperty(props.id));
  const error = useSelector(selectErrorsForProperty(props.id));
  const onChange = (event: any) => {
    const value = event.target.value;
    dispatch(updateStateProperty({property: props.id, value: value}))
  }

  const InputProps: any = {}
  if (props.start_icon) {
    InputProps['startAdornment'] = (
      <InputAdornment position="start">
        <Icon>{props.start_icon}</Icon>
      </InputAdornment>
    )
  }
  if (props.end_icon) {
    InputProps['endAdornment'] = (
      <InputAdornment position="end">
        <Icon>{props.end_icon}</Icon>
      </InputAdornment>
    )
  }

  console.log("StartIcon", InputProps)

  return (
    <>
      <Typography variant="subtitle2">{props.title}</Typography>
      { error && (
        <Block><Alert severity="error">{error}</Alert></Block>
      )}
      <TextField value={value || ""} InputProps={InputProps} inputProps={props.input_props}  onChange={onChange}/>
    </>
  )

}

export default TextFieldComponent;
