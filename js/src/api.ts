import queryString from "query-string";
import { IAPI, APITransport, APICallback, LoadStatus, createApi } from "@sfdl/prpc";
import store from './app/store';
import {setApiState} from "./features/api/apiSlice";
import {setCurrentView, setLoading} from "./features/view/viewSlice";
import {setCurrentState} from "./features/model/modelSlice";
import {setErrors} from "./features/error/errorSlice";

const appName = "cs_demand_model.rpc:app";
const defaultNativePackages = ['numpy', 'pandas'];
const defaultPackages = ['cs-demand-model[pyodide]']

const dispatch = store.dispatch;

type T2Response = {
  view: unknown,
  state: unknown,
  errors?: unknown
}


const initApi = async (callback: APICallback): Promise<IAPI> => {
  const parsed = queryString.parse(window.location.search);
  const apiConfig: any = {
    options: { appName }
  };
  if (parsed.url) {
    apiConfig.transport = APITransport.WEB;
    apiConfig.options.url = parsed.url;
  } else {
    apiConfig.transport = APITransport.PYODIDE;
    apiConfig.options.nativePackages = defaultNativePackages;
    apiConfig.options.packages = parsed.packages ? parsed.packages : defaultPackages;
  }
  return await createApi(apiConfig, callback);
};

const apiStatusCallback = (payload: any) => {
  if (payload !== LoadStatus.READY) {
    // We don't fire ready since we need to make sure we are ready too
    store.dispatch(setApiState(payload));
  }
};

const apiCallCallback = (response: T2Response) => {
  dispatch(setCurrentView(response.view))
  dispatch(setErrors(response.errors || {}));
  dispatch(setCurrentState(response.state))
}


class API {
  api?: IAPI = undefined;

  constructor() {
    initApi(apiStatusCallback).then((api) => {
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

export default new API();
