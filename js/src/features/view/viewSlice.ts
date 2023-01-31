import {createSlice} from '@reduxjs/toolkit'


export const viewSlice = createSlice({
  name: 'view',
  initialState: {
    currentView: null,
    loading: false,
  },
  reducers: {
    setCurrentView: (state, action) => {
      state.currentView = action.payload;
      state.loading = false;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
  },
})

export const selectCurrentView = (state: any) => state.view.currentView
export const selectLoading = (state: any) => state.view.loading
export const { setCurrentView, setLoading } = viewSlice.actions
export default viewSlice.reducer
