import React from "react";

import {ViewProps} from "../viewFactory";
import {Alert, Typography} from "@mui/material";
import { Block, DateSelect } from "@sfdl/sf-mui-components";
import {useDispatch, useSelector} from "react-redux";
import {selectStateProperty, updateStateProperty} from "../../features/model/modelSlice";
import {isoToDateObj, dateObjToIso} from "../../utils/dates";
import {DateObj} from "@sfdl/sf-mui-components/dist/types/components/inputs/dateselect/DateSelect";
import {selectErrorsForProperty} from "../../features/error/errorSlice";

export interface DateSelectComponentProps extends ViewProps {
  title: string;
}

const DateSelectComponent = (props: DateSelectComponentProps) => {
  const dispatch = useDispatch();
  const value = useSelector(selectStateProperty(props.id));
  const error = useSelector(selectErrorsForProperty(props.id));

  const dateObj = value ? isoToDateObj(value) : {day: "", month: "", year: ""};

  const onChange = (value: DateObj) => {
    dispatch(updateStateProperty({property: props.id, value: dateObjToIso(value)}))
  }

  return (
    <>
      <Typography variant="subtitle2">{props.title}</Typography>
      { error && (
        <Block><Alert severity="error">{error}</Alert></Block>
      )}
      <DateSelect day={dateObj.day} month={dateObj.month} year={dateObj.year} onChange={onChange} />
    </>
  )

}

export default DateSelectComponent;
