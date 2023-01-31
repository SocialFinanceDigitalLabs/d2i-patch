import React from "react";

import {ViewProps} from "../viewFactory";
import {Typography, Select, MenuItem, Alert} from "@mui/material";
import {useDispatch, useSelector} from "react-redux";
import {selectModel, selectStateProperty, updateStateProperty} from "../../features/model/modelSlice";
import { Block } from "@sfdl/sf-mui-components";
import {selectErrorsForProperty} from "../../features/error/errorSlice";
import {useApi} from "../../hooks/api";

export interface SelectComponentProps extends ViewProps {
  title: string;
  options: [{ value: string; label: string }];
  auto_action?: string;
}

const SelectComponent = (props: SelectComponentProps) => {
  const dispatch = useDispatch();
  const value = useSelector(selectStateProperty(props.id));
  const error = useSelector(selectErrorsForProperty(props.id));
  const model = useSelector(selectModel);
  const api = useApi();

  const onChange = (event: any) => {
    const value = event.target.value;
    dispatch(updateStateProperty({property: props.id, value: value}))
    if (props.auto_action) {
      const newModel = {...model};
      newModel[props.id] = value;
      api.call(props.auto_action, newModel);
    }
  }

  console.log("VALUE", value);

  return (
    <>
      <Typography variant="subtitle2">{props.title}</Typography>
      { error && (
        <Block><Alert severity="error">{error}</Alert></Block>
      )}
      <Select onChange={onChange} value={value || props.options[0]}>
        { props.options && props.options.map(({label, value}) => (
          <MenuItem key={value} value={value}>{label}</MenuItem>
        ))}
      </Select>
    </>
  )

}

export default SelectComponent;
