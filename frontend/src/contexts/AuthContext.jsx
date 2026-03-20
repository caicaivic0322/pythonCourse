/* eslint-disable react-refresh/only-export-components */
import { createContext, useState, useContext, useEffect } from 'react';
import {
  getCurrentUserData,
  getStoredUser,
  hasStoredToken,
  loginWithUsernameOrEmail,
  registerUser,
  signOut,
} from '../lib/dataService';

const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const initialUser = getStoredUser();
  const [user, setUser] = useState(initialUser);
  const [loading, setLoading] = useState(hasStoredToken() && !initialUser);

  useEffect(() => {
    if (!hasStoredToken()) {
      return;
    }

    const initAuth = async () => {
      const currentUser = await getCurrentUserData();
      setUser(currentUser);
      setLoading(false);
    };
    initAuth();
  }, []);

  const login = async (identifier, password) => {
    const session = await loginWithUsernameOrEmail(identifier, password);
    setUser(session.user);
    return session.user;
  };

  const register = async (username, email, password) => {
    const session = await registerUser(username, email, password);
    setUser(session.user);
    return session.user;
  };

  const logout = async () => {
    await signOut();
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, login, register, logout, loading }}>
      {!loading && children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
}
