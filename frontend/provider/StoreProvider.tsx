"use client"

import { store } from "@/lib/store";
import React from "react";
import { Provider } from "react-redux";

type Children = {
  children: React.ReactNode;
};

const StoreProvider = ({ children }: Children) => {
  return <Provider store={store}>{children}</Provider>;
};

export default StoreProvider;
