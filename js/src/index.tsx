import React, { lazy, Suspense } from "react";
import ReactDOM from "react-dom/client";
import { Loader } from "@sfdl/sf-mui-components";
import { registerStandardComponents } from "standardComponents";

const root = ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement
);

const App = lazy(() => {
  return import("./App");
});

registerStandardComponents();

root.render(
  <React.StrictMode>
    <Suspense fallback={<Loader type="cover" />}>
      <App />
    </Suspense>
  </React.StrictMode>
);
