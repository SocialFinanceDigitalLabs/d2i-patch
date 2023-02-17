import React, { Suspense } from "react";
import ErrorComponent from "./components/ErrorComponent";

export interface ViewProps {
  id: string;
  type: string;
}

export interface ViewFactoryProps {
  viewData: ViewProps;
}

const components: Record<string, any> = {}

const ViewFactory = (props: ViewFactoryProps) => {
  const {viewData} = props;

  const C = components[viewData.type];
  if (C) {
    if (C instanceof Function) {
      return <C key={viewData.id} {...viewData} />
    } else {
      return <Suspense><C key={viewData.id} {...viewData} /></Suspense>
    }
  } else {
    return <ErrorComponent text={`Missing component: ${viewData.type}`}/>
  }
}

export const RenderList = (props: any) => {
  const {children} = props;
  const Wrap = props.wrap ? props.wrap : React.Fragment;
  return (
    <>
    { children && children.map((componentProps: ViewProps) => {
      return (<Wrap key={componentProps.id}><ViewFactory viewData={componentProps} /></Wrap>)
    })}
    </>
  )
}

export const registerComponent = (name: string, component: any) : void => {
  components[name] = component;
}

export default ViewFactory
