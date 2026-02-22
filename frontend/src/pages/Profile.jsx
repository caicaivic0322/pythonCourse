import React, { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { useAuth } from '../contexts/AuthContext';
import { User, Mail, Calendar } from 'lucide-react';
import styles from './Profile.module.css';
import api from '../api/axios';

const Profile = () => {
  const { user } = useAuth();
  const [stats, setStats] = useState({ xp: 0, badges: 0, courses_learned: 0, study_hours: 0 });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchStats = async () => {
      try {
        const response = await api.get('users/stats/');
        setStats(response.data);
      } catch (error) {
        console.error("Failed to fetch user stats:", error);
      } finally {
        setLoading(false);
      }
    };

    if (user) {
      fetchStats();
    }
  }, [user]);

  // 计算等级 (每 500 XP 升一级)
  const level = Math.floor(stats.xp / 500) + 1;
  const nextLevelXp = level * 500;
  const progress = ((stats.xp % 500) / 500) * 100;

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <h1 className={styles.title}>个人中心</h1>
        <p className={styles.subtitle}>查看和管理你的账户信息</p>
      </div>

      <div className={styles.grid}>
        <motion.div 
          className={styles.profileCard}
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.5 }}
        >
          <div className={styles.avatar}>
            {user?.username?.charAt(0).toUpperCase() || 'U'}
          </div>
          <h2 className={styles.userName}>{user?.username || 'User'}</h2>
          <p className={styles.userLevel}>Level {level} Pythonista</p>
          
          <div className={styles.levelProgress}>
            <div className={styles.progressBar}>
              <div className={styles.progressFill} style={{ width: `${progress}%` }}></div>
            </div>
            <span className={styles.xpText}>{stats.xp} / {nextLevelXp} XP</span>
          </div>
          
          <div className={styles.infoList}>
            <div className={styles.infoItem}>
              <User size={16} className={styles.infoIcon} />
              <span>ID: {user?.user_id || user?.id || '-'}</span>
            </div>
            <div className={styles.infoItem}>
              <Mail size={16} className={styles.infoIcon} />
              <span>{user?.email || '未设置邮箱'}</span>
            </div>
            {/* <div className={styles.infoItem}>
              <Calendar size={16} className={styles.infoIcon} />
              <span>加入时间: 2024-01-01</span>
            </div> */}
          </div>
        </motion.div>

        <div className={styles.statsSection}>
          <motion.div 
            className={styles.statsGrid}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.1 }}
          >
            <div className={styles.statBox}>
              <div className={`${styles.statValue} ${styles.statBlue}`}>{stats.xp}</div>
              <div className={styles.statLabel}>经验值</div>
            </div>
            <div className={styles.statBox}>
              <div className={`${styles.statValue} ${styles.statGreen}`}>{stats.courses_learned}</div>
              <div className={styles.statLabel}>参与课程</div>
            </div>
            <div className={styles.statBox}>
              <div className={`${styles.statValue} ${styles.statPurple}`}>{stats.study_hours}h</div>
              <div className={styles.statLabel}>学习时长</div>
            </div>
            <div className={styles.statBox}>
              <div className={`${styles.statValue} ${styles.statOrange}`}>{stats.badges}</div>
              <div className={styles.statLabel}>获得勋章</div>
            </div>
          </motion.div>

          <motion.div 
            className={styles.badgesCard}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            <h3 className={styles.badgesTitle}>获得勋章</h3>
            <div className={styles.badgesGrid}>
              {stats.badges > 0 ? (
                 Array.from({ length: stats.badges }).map((_, index) => (
                  <div key={index} className={styles.badgeItem}>
                    <div className={styles.badgeEmoji}>🏅</div>
                    <div className={styles.badgeName}>课程勋章</div>
                  </div>
                 ))
              ) : (
                <div className={styles.noBadges}>暂无勋章，快去完成课程吧！</div>
              )}
            </div>
          </motion.div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
