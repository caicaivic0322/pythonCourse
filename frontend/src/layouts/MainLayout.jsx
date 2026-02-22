import React from 'react';
import { Outlet, Link, useLocation, useNavigate } from 'react-router-dom';
import { Home, BookOpen, Award, User, LogOut, Sun, Moon } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import { useTheme } from '../contexts/ThemeContext';
import styles from './MainLayout.module.css';

const MainLayout = () => {
  const location = useLocation();
  const { logout, user } = useAuth();
  const { theme, toggleTheme } = useTheme();
  const navigate = useNavigate();

  const isActive = (path) => location.pathname === path;

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <div className={styles.container}>
      <aside className={styles.sidebar}>
        <div className={styles.logoSection}>
          <div className={styles.logo}>
            <div className={styles.logoIcon}>🐍</div>
            <div>
              <div className={styles.logoText}>PyMaster</div>
              <div className={styles.logoSubtitle}>Python 学习平台</div>
            </div>
          </div>
        </div>

        <nav className={styles.nav}>
          <Link 
            to="/" 
            className={`${styles.navLink} ${isActive('/') ? styles.navLinkActive : ''}`}
          >
            <Home className={styles.navIcon} />
            <span>首页</span>
          </Link>
          
          <Link 
            to="/courses" 
            className={`${styles.navLink} ${isActive('/courses') ? styles.navLinkActive : ''}`}
          >
            <BookOpen className={styles.navIcon} />
            <span>课程中心</span>
          </Link>

          <Link 
            to="/achievements" 
            className={`${styles.navLink} ${isActive('/achievements') ? styles.navLinkActive : ''}`}
          >
            <Award className={styles.navIcon} />
            <span>成就</span>
          </Link>
        </nav>

        <div className={styles.bottomSection}>
          <Link 
            to="/profile"
            className={`${styles.navLink} ${isActive('/profile') ? styles.navLinkActive : ''}`}
          >
            <User className={styles.navIcon} />
            <span>个人中心</span>
          </Link>
          
          <div className={styles.userInfo}>
            <div className={styles.userAvatar}>
              {user?.username?.charAt(0).toUpperCase() || 'U'}
            </div>
            <span className={styles.userName}>{user?.username || 'User'}</span>
          </div>
          
          <button 
            onClick={handleLogout}
            className={styles.logoutBtn}
          >
            <LogOut size={16} />
            <span>退出登录</span>
          </button>
        </div>
      </aside>

      <main className={styles.mainContent}>
        <header className={styles.topBar}>
          <div className={styles.topBarLeft}>
            <span className={styles.breadcrumb}>
              PyMaster / <span className={styles.breadcrumbActive}>
                {location.pathname === '/' ? '首页' : 
                 location.pathname === '/courses' ? '课程中心' :
                 location.pathname === '/profile' ? '个人中心' : ''}
              </span>
            </span>
          </div>
          <div className={styles.topBarRight}>
            <button 
              onClick={toggleTheme}
              className={styles.themeToggle}
              title={theme === 'light' ? '切换深色模式' : '切换浅色模式'}
            >
              {theme === 'light' ? <Moon size={18} /> : <Sun size={18} />}
            </button>
          </div>
        </header>

        <div className={styles.contentArea}>
          <div className={styles.contentWrapper}>
            <Outlet />
          </div>
        </div>
      </main>
    </div>
  );
};

export default MainLayout;
