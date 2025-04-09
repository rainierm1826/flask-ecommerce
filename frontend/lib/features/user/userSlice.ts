import { createSlice } from "@reduxjs/toolkit";

export const userSlice = createSlice({
  name: "user",
  initialState: {
    user: null,
    loading: false,
  },
  reducers: {
    setUser: (state, action) => {
      state.user = action.payload;
    },
    setLoading: (state, action) => {
      state.loading = action.payload;
    },
    setLogout: (state) => {
      state.user = null;
    },
  },
});

export const {setUser, setLoading, setLogout} = userSlice.actions
export default userSlice.reducer