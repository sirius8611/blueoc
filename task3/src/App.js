import './App.css';
import PostForm from './components/PostForm';
import PostList from './components/PostList';

function App() {
  return (
    <div className="App" style={{ padding: 32 }}>
      <h1>Add post</h1>
      <PostForm />
      <h1>Posts</h1>
      <PostList />
    </div>
  );
}

export default App;
