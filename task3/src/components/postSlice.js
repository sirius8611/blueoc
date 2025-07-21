import { createSlice, createAsyncThunk } from '@reduxjs/toolkit';
import axios from 'axios';
import { nanoid } from '@reduxjs/toolkit';

const POSTS_URL = 'https://jsonplaceholder.typicode.com/posts';

export const fetchPosts = createAsyncThunk('posts/fetchPosts', async () => {
  const response = await axios.get(POSTS_URL);
  return response.data;
});

export const addPost = createAsyncThunk('posts/addPost', async (newPost) => {
  const response = await axios.post(POSTS_URL, newPost);
  if (response.data.id === 101) {
    response.data.id = nanoid();
  }
  return response.data;
});

const postSlice = createSlice({
  name: 'posts',
  initialState: { items: [], status: 'idle', error: null },
  reducers: {},
  extraReducers: (builder) => {
    builder
      .addCase(fetchPosts.pending, (state) => { state.status = 'loading'; })
      .addCase(fetchPosts.fulfilled, (state, action) => {
        state.status = 'succeeded';
        state.items = action.payload;
      })
      .addCase(fetchPosts.rejected, (state, action) => {
        state.status = 'failed';
        state.error = action.error.message;
      })
      .addCase(addPost.fulfilled, (state, action) => {
        state.items.unshift(action.payload);
      });
  },
});

export default postSlice.reducer; 