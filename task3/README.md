# React Redux Posts App

A simple React application that uses Redux Toolkit for state management and async API calls. The app fetches and displays posts from an API and allows users to add new posts via a form.

## Features

- **Redux Toolkit** for state management
- **Async API calls** using `createAsyncThunk`
- **Fetch and display posts** from a remote API
- **Add new posts** with a form component
- **Modern ES6+ syntax**

## Demo

> _Add a screenshot or GIF here if possible_

## Getting Started

### Prerequisites

- Node.js (v14+ recommended)
- npm (v6+ recommended)

### Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd <repo-folder>
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm start
   ```

4. Open [http://localhost:3000](http://localhost:3000) in your browser.

## Project Structure

```
src/
  app/
    store.js           # Redux store configuration
  components/
    PostForm.js        # Form to add new posts
    PostList.js        # Displays list of posts
    postSlice.js       # Redux slice for posts (async thunks & reducers)
  App.js               # Main app component
  index.js             # Entry point
```

## Usage

### Fetching Posts

- On app load, posts are fetched from [JSONPlaceholder](https://jsonplaceholder.typicode.com/posts) using an async thunk.
- Posts are displayed in the `PostList` component.

### Adding a Post

- Use the `PostForm` to submit a new post.
- The form dispatches an async thunk to add the post to the API and updates the Redux state.

## Redux Logic

- **Async Thunks:**  
  - `fetchPosts`: Fetches posts from the API.
  - `addPost`: Adds a new post via POST request.
- **Slice State:**  
  - `items`: Array of post objects.
  - `status`: Loading state (`idle`, `loading`, `succeeded`, `failed`).
  - `error`: Error message if API call fails.



## Customization

- You can change the API endpoint in `postSlice.js` by editing the `POSTS_URL` constant.
- Add more features (edit, delete, etc.) by extending the Redux slice and UI components.



