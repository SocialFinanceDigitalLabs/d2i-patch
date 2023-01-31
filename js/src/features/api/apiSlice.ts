import {createSlice} from '@reduxjs/toolkit'
import {LoadStatus} from "@sfdl/prpc";

export type ApiState = {
  state: LoadStatus
}

export const apiSlice = createSlice({
  name: 'api',
  initialState: {
    state: LoadStatus.IDLE,
  } as ApiState,
  reducers: {
    setApiState: (state, action) => {
      state.state = action.payload as LoadStatus;
    },
  },
})

export const selectApiState = (state: any) => state.api.state
export const { setApiState } = apiSlice.actions
export default apiSlice.reducer
