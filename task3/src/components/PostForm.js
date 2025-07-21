import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
import { addPost } from './postSlice';

export default function PostForm() {
  const [title, setTitle] = useState('');
  const [body, setBody] = useState('');
  const dispatch = useDispatch();

  const onSubmit = (e) => {
    e.preventDefault();
    if (title && body) {
      dispatch(addPost({ title, body, userId: 1 }));
      setTitle('');
      setBody('');
    }
  };

  return (
    <form onSubmit={onSubmit} style={{ marginBottom: 20 }}>
      <input
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Title"
        required
        style={{ display: 'block', marginBottom: 8, width: 300 }}
      />
      <textarea
        value={body}
        onChange={(e) => setBody(e.target.value)}
        placeholder="Body"
        required
        style={{ display: 'block', marginBottom: 8, width: 300, height: 80 }}
      />
      <button type="submit">Add Post</button>
    </form>
  );
} 