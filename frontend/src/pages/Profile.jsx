import React, { useState, useEffect } from 'react';
import { Mail, User } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import styles from './Profile.module.css';
import api from '../api/axios';

const Profile = () => {
  const { user } = useAuth();
  const [stats, setStats] = useState({ xp: 0, badges: 0, courses_learned: 0, study_hours: 0 });

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await api.get('users/stats/');
        setStats(response.data);
      } catch (error) {
        console.error('Failed to fetch user stats:', error);
      }
    };

    if (user) {
      fetchStats();
    }
  }, [user]);

  const level = Math.floor(stats.xp / 500) + 1;
  const nextLevelXp = level * 500;
  const progress = ((stats.xp % 500) / 500) * 100;

  return (
    <div className="page-shell">
      <section className={`page-hero ${styles.hero}`}>
        <div>
          <span className="eyebrow">Profile</span>
          <h1 className="hero-title">成长中心</h1>
          <p className="hero-subtitle">
            这里展示你的等级、经验值、参与课程和徽章情况，让成长路径从抽象的“学过了”变成可见的进展。
          </p>
        </div>

        <div className={styles.levelCard}>
          <span>当前等级</span>
          <strong>Lv.{level}</strong>
          <p>{stats.xp} XP / {nextLevelXp} XP</p>
        </div>
      </section>

      <section className={styles.layout}>
        <aside className={`${styles.profileCard} surface-card`}>
          <div className={styles.avatar}>
            {user?.username?.charAt(0).toUpperCase() || 'U'}
          </div>
          <h2>{user?.username || 'User'}</h2>
          <p className={styles.userLevel}>Level {level} Pythonista</p>

          <div className={styles.levelProgress}>
            <div className={styles.progressTrack}>
              <div className={styles.progressFill} style={{ width: `${progress}%` }} />
            </div>
            <span>{stats.xp} / {nextLevelXp} XP</span>
          </div>

          <div className={styles.infoList}>
            <div className={styles.infoItem}>
              <User size={16} />
              <span>ID: {user?.user_id || user?.id || '-'}</span>
            </div>
            <div className={styles.infoItem}>
              <Mail size={16} />
              <span>{user?.email || '未设置邮箱'}</span>
            </div>
          </div>
        </aside>

        <div className={styles.mainSection}>
          <div className={styles.statsGrid}>
            <div className={`${styles.statBox} surface-card`}>
              <div className="metric-value">{stats.xp}</div>
              <div className={styles.statLabel}>经验值</div>
            </div>
            <div className={`${styles.statBox} surface-card`}>
              <div className="metric-value">{stats.courses_learned}</div>
              <div className={styles.statLabel}>参与课程</div>
            </div>
            <div className={`${styles.statBox} surface-card`}>
              <div className="metric-value">{stats.study_hours}h</div>
              <div className={styles.statLabel}>学习时长</div>
            </div>
            <div className={`${styles.statBox} surface-card`}>
              <div className="metric-value">{stats.badges}</div>
              <div className={styles.statLabel}>获得勋章</div>
            </div>
          </div>

          <section className={`${styles.badgesCard} surface-card`}>
            <div className={styles.badgesHeader}>
              <div>
                <h3 className="section-title">获得勋章</h3>
                <p className="section-subtitle">完成课程与阶段目标后，你的成果会集中展示在这里。</p>
              </div>
            </div>

            <div className={styles.badgesGrid}>
              {stats.badges > 0 ? (
                Array.from({ length: stats.badges }).map((_, index) => (
                  <div key={index} className={styles.badgeItem}>
                    <div className={styles.badgeEmoji}>🏅</div>
                    <div className={styles.badgeName}>课程勋章 #{index + 1}</div>
                  </div>
                ))
              ) : (
                <div className="empty-panel">暂无勋章，先去完成一门课程。</div>
              )}
            </div>
          </section>
        </div>
      </section>
    </div>
  );
};

export default Profile;
