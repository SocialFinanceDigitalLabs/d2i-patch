import React from "react";

import {
  DualButton,
} from "@sfdl/sf-mui-components";
import ViewFactory, {ViewProps} from "../viewFactory";
import {ButtonProps} from "./ButtonComponent";

export interface ButtonBarProps extends ViewProps {
  buttons: Array<ButtonProps>;
}

const ButtonBarComponent = (props: ButtonBarProps) => {
  const { buttons } = props;

  const Container = buttons.length > 1 ? DualButton : React.Fragment;

  return (
    <Container>
      { buttons && buttons.map((buttonProps) => <ViewFactory key={buttonProps.id} viewData={buttonProps} />)}
    </Container>
  )

}

export default ButtonBarComponent;