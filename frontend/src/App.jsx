import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { AuthProvider } from './context/AuthContext';
import MainLayout from './layouts/MainLayout';
import HomePage from './pages/HomePage';
import CourseList from './pages/CourseList';
import CourseDetail from './pages/CourseDetail';
import LessonDetail from './pages/LessonDetail';
import Login from './pages/Login';
import Register from './pages/Register';
import Profile from './pages/Profile';
import PrivateRoute from './components/PrivateRoute';

function App() {
  return (
    <Router>
      <AuthProvider>
        <Routes>
          <Route path="/" element={<PrivateRoute><MainLayout /></PrivateRoute>}>
            <Route index element={<HomePage />} />
            <Route path="courses" element={<CourseList />} />
            <Route path="courses/:id" element={<CourseDetail />} />
            <Route path="lessons/:id" element={<LessonDetail />} />
            <Route path="profile" element={<Profile />} />
          </Route>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
        </Routes>
      </AuthProvider>
    </Router>
  );
}

export default App;
