import React from 'react';
import { Outlet, Link, useLocation, useNavigate } from 'react-router-dom';
import {
  BookOpen,
  Home,
  LogOut,
  MenuSquare,
  Moon,
  Sparkles,
  Sun,
  User,
} from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import { useTheme } from '../contexts/ThemeContext';
import styles from './MainLayout.module.css';

const navItems = [
  { path: '/', label: '总览', shortLabel: '首页', icon: Home },
  { path: '/courses', label: '课程中心', shortLabel: '课程', icon: BookOpen },
  { path: '/profile', label: '个人中心', shortLabel: '我的', icon: User },
];

const pageMeta = {
  '/': {
    title: '学习总览',
    subtitle: '把今天的学习目标、课程进度和练习入口收拢到一个更清晰的工作台。',
  },
  '/courses': {
    title: '课程中心',
    subtitle: '从基础到项目实战，按进度解锁内容，始终知道下一步学什么。',
  },
  '/profile': {
    title: '个人中心',
    subtitle: '查看你的成长曲线、学习徽章和账户信息。',
  },
};

const MainLayout = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { logout, user } = useAuth();
  const { theme, toggleTheme } = useTheme();

  const meta = pageMeta[location.pathname] || {
    title: '学习页面',
    subtitle: '继续你的 Python 学习旅程。',
  };

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  const isActive = (path) => {
    if (path === '/') {
      return location.pathname === '/';
    }
    return location.pathname.startsWith(path);
  };

  return (
    <div className={styles.appShell}>
      <aside className={styles.sidebar}>
        <div className={styles.brandPanel}>
          <div className={styles.brandMark}>Py</div>
          <div>
            <div className={styles.brandTitle}>PyMaster</div>
            <div className={styles.brandSubtitle}>Modern Python Learning Hub</div>
          </div>
        </div>

        <div className={styles.sidebarCard}>
          <div className={styles.sidebarEyebrow}>
            <Sparkles size={14} />
            学习导航
          </div>
          <nav className={styles.nav}>
            {navItems.map((item) => {
              const Icon = item.icon;
              return (
                <Link
                  key={item.path}
                  to={item.path}
                  className={`${styles.navLink} ${isActive(item.path) ? styles.navLinkActive : ''}`}
                >
                  <span className={styles.navIconWrap}>
                    <Icon className={styles.navIcon} />
                  </span>
                  <span className={styles.navText}>
                    <strong>{item.label}</strong>
                    <small>{item.path === '/' ? '今日重点' : item.path === '/courses' ? '分阶段学习' : '成长档案'}</small>
                  </span>
                </Link>
              );
            })}
          </nav>
        </div>

        <div className={styles.profileCard}>
          <div className={styles.userAvatar}>
            {user?.username?.charAt(0).toUpperCase() || 'U'}
          </div>
          <div className={styles.userMeta}>
            <strong>{user?.username || 'User'}</strong>
            <span>{user?.email || '准备继续学习'}</span>
          </div>
        </div>

        <button onClick={handleLogout} className={styles.logoutButton}>
          <LogOut size={16} />
          退出登录
        </button>
      </aside>

      <div className={styles.mainColumn}>
        <header className={styles.topBar}>
          <div className={styles.topBarInfo}>
            <span className={styles.mobileBadge}>
              <MenuSquare size={14} />
              {meta.title}
            </span>
            <h1>{meta.title}</h1>
          </div>

          <div className={styles.topBarActions}>
            <button
              onClick={toggleTheme}
              className={styles.themeButton}
              title={theme === 'light' ? '切换深色模式' : '切换浅色模式'}
            >
              {theme === 'light' ? <Moon size={18} /> : <Sun size={18} />}
            </button>
            <div className={styles.userPill}>
              <span className={styles.userPillAvatar}>
                {user?.username?.charAt(0).toUpperCase() || 'U'}
              </span>
              <span className={styles.userPillText}>{user?.username || 'User'}</span>
            </div>
          </div>
        </header>

        <main className={styles.contentArea}>
          <div className={styles.contentInner}>
            <Outlet />
          </div>
        </main>
      </div>

      <nav className={styles.mobileNav}>
        {navItems.map((item) => {
          const Icon = item.icon;
          return (
            <Link
              key={item.path}
              to={item.path}
              className={`${styles.mobileNavLink} ${isActive(item.path) ? styles.mobileNavLinkActive : ''}`}
            >
              <Icon size={18} />
              <span>{item.shortLabel}</span>
            </Link>
          );
        })}
      </nav>
    </div>
  );
};

export default MainLayout;
