import {createSlice} from '@reduxjs/toolkit'


export const errorSlice = createSlice({
  name: 'view',
  initialState: {
    errors: {}
  },
  reducers: {
    setErrors: (state, action) => {
      state.errors = action.payload;
    },
  },
})

export const selectErrorsForProperty = (property: string) => (state: any) => state.error.errors[property];
export const { setErrors } = errorSlice.actions
export default errorSlice.reducer
