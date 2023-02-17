import { APIConfig, APITransport } from "@sfdl/prpc";
import queryString from "query-string";
import {API} from "../api";

const appName = "d2i_patch.api:app";
const defaultNativePackages = ['numpy', 'pandas'];
const defaultPackages = ['d2i_patch[pyodide]']


const getApiConfig = (): APIConfig => {
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
  return apiConfig;
}

let api: API;

const useApi = () => {
  if (!api) {
    api = new API(getApiConfig());
  }
  return api;
}

export { useApi }
