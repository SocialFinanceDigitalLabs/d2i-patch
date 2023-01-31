const DashboardGridItem = {
  height: "80vh",
  overflowY: "auto" as "auto", //this weirdness is because TS lacks type expansion support for overflowY. It will expand to string, which is invalid for this property
};

export { DashboardGridItem };