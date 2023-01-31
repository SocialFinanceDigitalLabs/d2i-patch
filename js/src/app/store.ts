import { configureStore } from '@reduxjs/toolkit';
import apiReducer from '../features/api/apiSlice';
import modelReducer from '../features/model/modelSlice';
import viewReducer from '../features/view/viewSlice';
import errorReducer from '../features/error/errorSlice';

const store = configureStore({
  reducer: {
    api: apiReducer,
    view: viewReducer,
    model: modelReducer,
    error: errorReducer,
  },
});

export type AppDispatch = typeof store.dispatch
export default store;

