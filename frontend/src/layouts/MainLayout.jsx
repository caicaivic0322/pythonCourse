import React from 'react';
import { Outlet, Link, useLocation, useNavigate } from 'react-router-dom';
import { Home, BookOpen, Trophy, User, LogOut } from 'lucide-react';
import { useAuth } from '../context/AuthContext';

const MainLayout = () => {
  const location = useLocation();
  const { logout } = useAuth();
  const navigate = useNavigate();

  const isActive = (path) => location.pathname === path;

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className="min-h-screen bg-slate-900 text-slate-100 flex font-sans">
      {/* Sidebar */}
      <aside className="w-64 bg-slate-800 border-r border-slate-700 hidden md:flex flex-col">
        <div className="p-6 border-b border-slate-700">
          <h1 className="text-2xl font-bold font-display text-blue-400 flex items-center gap-2">
            <span className="text-3xl">🐍</span> PyMaster
          </h1>
          <p className="text-xs text-slate-400 mt-1">Level 1 Pythonista</p>
        </div>

        <nav className="flex-1 p-4 space-y-2">
          <Link 
            to="/" 
            className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-all ${isActive('/') ? 'bg-blue-600/20 text-blue-400' : 'hover:bg-slate-700 text-slate-400'}`}
          >
            <Home size={20} />
            <span className="font-medium">任务中心</span>
          </Link>
          
          <Link 
            to="/courses" 
            className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-all ${isActive('/courses') ? 'bg-blue-600/20 text-blue-400' : 'hover:bg-slate-700 text-slate-400'}`}
          >
            <BookOpen size={20} />
            <span className="font-medium">训练模块</span>
          </Link>

          <Link 
            to="/achievements" 
            className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-all ${isActive('/achievements') ? 'bg-blue-600/20 text-blue-400' : 'hover:bg-slate-700 text-slate-400'}`}
          >
            <Trophy size={20} />
            <span className="font-medium">成就勋章</span>
          </Link>
        </nav>

        <div className="p-4 border-t border-slate-700">
          <Link 
            to="/profile"
            className={`flex items-center gap-3 px-4 py-3 rounded-xl transition-all ${isActive('/profile') ? 'bg-blue-600/20 text-blue-400' : 'hover:bg-slate-700 text-slate-400'}`}
          >
            <User size={20} />
            <span className="font-medium">个人档案</span>
          </Link>
          <button 
            onClick={handleLogout}
            className="w-full flex items-center gap-3 px-4 py-3 text-red-400 hover:text-red-300 cursor-pointer transition-colors"
          >
            <LogOut size={20} />
            <span className="font-medium">退出任务</span>
          </button>
        </div>
      </aside>

      {/* Main Content */}
      <main className="flex-1 flex flex-col min-h-screen overflow-hidden">
        {/* Mobile Header */}
        <header className="md:hidden bg-slate-800 border-b border-slate-700 p-4 flex items-center justify-between">
          <h1 className="text-xl font-bold font-display text-blue-400">PyMaster</h1>
          <button className="p-2 text-slate-400">
            <User size={24} />
          </button>
        </header>

        {/* Scrollable Content Area */}
        <div className="flex-1 overflow-y-auto p-4 md:p-8 relative">
           {/* Gamified Background Elements */}
           <div className="absolute top-0 left-0 w-full h-full overflow-hidden pointer-events-none z-0 opacity-20">
              <div className="absolute top-10 left-10 w-64 h-64 bg-blue-600 rounded-full blur-[100px]"></div>
              <div className="absolute bottom-10 right-10 w-96 h-96 bg-purple-600 rounded-full blur-[120px]"></div>
           </div>

           <div className="relative z-10 max-w-7xl mx-auto">
            <Outlet />
           </div>
        </div>
      </main>
    </div>
  );
};


export default MainLayout;
