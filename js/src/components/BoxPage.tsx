import {Box} from "@mui/material";
import { Block } from "@sfdl/sf-mui-components";

import ViewFactory, {ViewProps} from "../viewFactory";

interface BoxPageProps extends ViewProps {
  components: [any];
}

const BoxPage = (props: BoxPageProps) => {
  return (
    <Box flexGrow={1}>
      { props.components && props.components.map((componentProps, ix) => {
        return <Block key={componentProps.id || ix} spacing="blockLarge"><ViewFactory viewData={componentProps} /></Block>
      })}
    </Box>
  )
}

export default BoxPage;
