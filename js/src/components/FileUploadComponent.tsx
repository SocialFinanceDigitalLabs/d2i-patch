import React from "react";

import {ViewProps} from "../viewFactory";
import {useSelector} from "react-redux";
import {selectStateProperty} from "../../features/model/modelSlice";
import { Upload as Uploader } from "@sfdl/sf-mui-components";
import {useApi} from "../../hooks/api";

export interface FileUploadComponentProps extends ViewProps {
  title: string,
  action: string,
}

const FileUploadComponent = (props: FileUploadComponentProps) => {
  const api = useApi();
  const fileList = useSelector(selectStateProperty("files"))
  const onUploadReady = (files: any) => {
    console.log("onUploadReady", files);

    api.call(props.action, files)
  }
  // const fileList =
  return (
    <>
      <Uploader label={props.title} onUploadReady={onUploadReady} fileList={fileList}/>
    </>
  )

}

export default FileUploadComponent;
