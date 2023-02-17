import { IAPI, LoadStatus, createApi, APIConfig } from "@sfdl/prpc";
import store from './app/store';
import {setApiState} from "./features/api/apiSlice";
import {setCurrentView, setLoading} from "./features/view/viewSlice";
import {setCurrentState} from "./features/model/modelSlice";
import {setErrors} from "./features/error/errorSlice";

const dispatch = store.dispatch;

type PatchApiResponse = {
  view: unknown,
  state: unknown,
  errors?: unknown
}

const apiStatusCallback = (payload: any) => {
  if (payload !== LoadStatus.READY) {
    // We don't fire ready since we need to make sure we are ready too
    store.dispatch(setApiState(payload));
  }
};

const apiCallCallback = (response: PatchApiResponse) => {
  dispatch(setCurrentView(response.view))
  dispatch(setCurrentState(response.state || {}))
  dispatch(setErrors(response.errors || {}));
}


export class API {
  api?: IAPI = undefined;

  constructor(apiConfig: APIConfig) {
    createApi(apiConfig, apiStatusCallback).then((api) => {
      this.api = api;
      dispatch(setApiState(LoadStatus.READY));
    }).catch((reason) => {
      dispatch(setApiState(LoadStatus.ERROR));
    })
  }

  init = () => {
    if (!this.api) {
      dispatch(setApiState(LoadStatus.ERROR));
      throw new Error("API is not in READY state");
    }
    this.api.call("action", {action: "init"}).then(apiCallCallback).catch((reason) => {
      dispatch(setApiState(LoadStatus.ERROR));
    })
  }

  call(action: string, data: {}) {
    if (!this.api) {
      dispatch(setApiState(LoadStatus.ERROR));
      throw new Error("API is not in READY state");
    }
    dispatch(setLoading(true))
    this.api.call("action", {action, data}).then(apiCallCallback).catch((reason) => {
      dispatch(setCurrentView({id: "error", type: "error", text: reason.message}))
    })
  }


}
