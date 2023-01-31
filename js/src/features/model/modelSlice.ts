import {createSlice} from '@reduxjs/toolkit'


export const modelSlice = createSlice({
  name: 'model',
  initialState: {
    model: {},
  },
  reducers: {
    setCurrentState: (state, action) => {
      state.model = action.payload;
    },
    updateStateProperty: (state, action) => {
      const model = state.model as any;
      model[action.payload.property] = action.payload.value;
    }
  },
})

export const selectStateProperty = (property: string) => (state: any) => state.model.model[property];
export const selectModel = (state: any) => state.model.model;
export const { setCurrentState, updateStateProperty } = modelSlice.actions
export default modelSlice.reducer
