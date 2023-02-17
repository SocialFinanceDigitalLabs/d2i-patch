import React, {useEffect} from "react";
import {Provider as ReduxProvider, useSelector} from 'react-redux';
import { createTheme, ThemeProvider } from "@mui/material/styles";
import Alert from '@mui/material/Alert';

import {LoadStatus} from "@sfdl/prpc";
import { Body, Loader, Container, theme as SFTheme } from "@sfdl/sf-mui-components";

import store from './app/store';

import {selectApiState} from "./features/api/apiSlice";
import {selectCurrentView, selectLoading} from "./features/view/viewSlice";
import ViewFactory from "./viewFactory";

import {useApi} from "./hooks/useApi";


const theme = createTheme(SFTheme);

const ReduxApp = () => {
  const api = useApi();
  const apiState = useSelector(selectApiState);
  const currentView = useSelector(selectCurrentView);
  const loading = useSelector(selectLoading);

  const ready = apiState === LoadStatus.READY;
  const error = apiState === LoadStatus.ERROR;

  useEffect(() => {
    if (ready) {
      api.init()
    }
  }, [api, ready])

  if (error) {
    return <Alert severity="error">Failed to load the API. Please refresh your page to try again.</Alert>
  } else if (loading || !currentView) {
    return <Loader type="cover" />
  } else {
    return <ViewFactory viewData={currentView} />
  }

}

const BodyWithState = () => {
  const apiState = useSelector(selectApiState);
  return (
    <Body title="D2I PATCH" chip={`API: ${apiState}`}>
      <ReduxApp />
    </Body>

  )
}

const App = () => {
  return (
    <ReduxProvider store={store}>
      <ThemeProvider theme={theme}>
        <Container>
          <BodyWithState />
        </Container>
      </ThemeProvider>
    </ReduxProvider>
  );
}

export default App;
