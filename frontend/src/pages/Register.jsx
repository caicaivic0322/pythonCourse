import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

const Register = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await register(username, email, password);
      navigate('/');
    } catch (err) {
      setError('注册失败。用户名可能已被占用。');
    }
  };

  return (
    <div className="min-h-screen bg-slate-900 flex items-center justify-center p-4">
      <div className="bg-slate-800 p-8 rounded-xl shadow-2xl border border-slate-700 w-full max-w-md">
        <h1 className="text-3xl font-bold font-display text-white mb-6 text-center">新兵注册</h1>
        {error && (
          <div className="bg-red-500/20 border border-red-500 text-red-400 p-3 rounded-lg mb-4 text-center">
            {error}
          </div>
        )}
        <form className="space-y-4" onSubmit={handleSubmit}>
          <div>
            <label className="block text-slate-400 text-sm font-bold mb-2">用户名</label>
            <input 
              type="text" 
              className="w-full bg-slate-700 border border-slate-600 rounded-lg p-3 text-white focus:outline-none focus:border-blue-500 transition-colors" 
              placeholder="请选择一个用户名"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
            />
          </div>
          <div>
            <label className="block text-slate-400 text-sm font-bold mb-2">邮箱</label>
            <input 
              type="email" 
              className="w-full bg-slate-700 border border-slate-600 rounded-lg p-3 text-white focus:outline-none focus:border-blue-500 transition-colors" 
              placeholder="请输入你的邮箱"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
          </div>
          <div>
            <label className="block text-slate-400 text-sm font-bold mb-2">密码</label>
            <input 
              type="password" 
              className="w-full bg-slate-700 border border-slate-600 rounded-lg p-3 text-white focus:outline-none focus:border-blue-500 transition-colors" 
              placeholder="请创建密码"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <button className="w-full bg-green-600 hover:bg-green-700 text-white font-bold py-3 rounded-lg transition-all transform hover:scale-105 mt-4">
            注册
          </button>
        </form>
        <p className="text-center text-slate-500 mt-6 text-sm">
          已经是学员了? <Link to="/login" className="text-blue-400 hover:text-blue-300 font-bold">在此登录</Link>
        </p>
      </div>
    </div>
  );
};

export default Register;
