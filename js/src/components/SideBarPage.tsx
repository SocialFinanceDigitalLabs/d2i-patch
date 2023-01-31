import React from "react";
import { Block } from "@sfdl/sf-mui-components";

import ViewFactory, {ViewProps} from "../viewFactory";
import { Box, Grid } from "@mui/material";
import { DashboardGridItem } from "./SideBarPage.styles";

interface SideBarPageProps extends ViewProps {
  sidebar: [ViewProps];
  main: [ViewProps]
}

const SideBarPage = (props: SideBarPageProps) => {
  return (
    <Box flexGrow={1}>
      <Grid container>
        <Grid xs={5} item style={DashboardGridItem}>
          { props.sidebar && props.sidebar.map((componentProps) => {
            return <Block key={componentProps.id} spacing="blockLarge"><ViewFactory viewData={componentProps} /></Block>
          })}
        </Grid>
        <Grid item xs={7} style={DashboardGridItem}>
          { props.main && props.main.map((componentProps) => {
            return <Block key={componentProps.id} spacing="blockLarge"><ViewFactory viewData={componentProps} /></Block>
          })}
        </Grid>
      </Grid>
    </Box>
  )
}

export default SideBarPage;
