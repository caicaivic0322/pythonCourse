import React from 'react';
import { motion } from 'framer-motion';
import { useAuth } from '../contexts/AuthContext';
import { User, Mail, Calendar } from 'lucide-react';
import styles from './Profile.module.css';

const Profile = () => {
  const { user } = useAuth();

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
          <p className={styles.userLevel}>Level 1 Pythonista</p>
          
          <div className={styles.infoList}>
            <div className={styles.infoItem}>
              <User size={16} className={styles.infoIcon} />
              <span>ID: {user?.id || '-'}</span>
            </div>
            <div className={styles.infoItem}>
              <Mail size={16} className={styles.infoIcon} />
              <span>{user?.email || '未设置邮箱'}</span>
            </div>
            <div className={styles.infoItem}>
              <Calendar size={16} className={styles.infoIcon} />
              <span>加入时间: 2024-01-01</span>
            </div>
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
              <div className={`${styles.statValue} ${styles.statBlue}`}>1,250</div>
              <div className={styles.statLabel}>经验值</div>
            </div>
            <div className={styles.statBox}>
              <div className={`${styles.statValue} ${styles.statGreen}`}>4</div>
              <div className={styles.statLabel}>完成课程</div>
            </div>
            <div className={styles.statBox}>
              <div className={`${styles.statValue} ${styles.statPurple}`}>12</div>
              <div className={styles.statLabel}>代码挑战</div>
            </div>
            <div className={styles.statBox}>
              <div className={`${styles.statValue} ${styles.statOrange}`}>3</div>
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
              <div className={styles.badgeItem}>
                <div className={styles.badgeEmoji}>🌱</div>
                <div className={styles.badgeName}>初出茅庐</div>
              </div>
              <div className={styles.badgeItem}>
                <div className={styles.badgeEmoji}>🔥</div>
                <div className={styles.badgeName}>连续打卡</div>
              </div>
              <div className={styles.badgeItem}>
                <div className={styles.badgeEmoji}>🐛</div>
                <div className={styles.badgeName}>Bug猎手</div>
              </div>
              <div className={styles.badgeItem}>
                <div className={styles.badgeEmoji}>🚀</div>
                <div className={styles.badgeName}>初学者</div>
              </div>
            </div>
          </motion.div>
        </div>
      </div>
    </div>
  );
};

export default Profile;
