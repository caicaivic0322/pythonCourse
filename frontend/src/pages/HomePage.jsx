import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Code, Trophy, Clock, BookOpen, ArrowRight } from 'lucide-react';
import api from '../api/axios';
import styles from './HomePage.module.css';

const HomePage = () => {
  const [currentCourse, setCurrentCourse] = useState(null);
  const [currentLesson, setCurrentLesson] = useState(null);
  const [stats, setStats] = useState({ xp: 0, badges: 0, courses_learned: 0, study_hours: 0 });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProgress = async () => {
      try {
        // Fetch stats
        const statsRes = await api.get('users/stats/');
        setStats(statsRes.data);

        const response = await api.get('courses/');
        const courses = response.data;
        
        // 优先找到第一个【已解锁】且【未完成】的课程
        let activeCourse = courses.find(c => !c.is_locked && !c.is_completed);
        
        // 如果都完成了（或者没有符合条件的），就显示最后一个已解锁的课程（即当前进度最远的）
        if (!activeCourse) {
            activeCourse = [...courses].reverse().find(c => !c.is_locked) || courses[0];
        }
        
        if (activeCourse) {
            const detailRes = await api.get(`courses/${activeCourse.id}/`);
            const courseDetail = detailRes.data;
            setCurrentCourse(courseDetail);
            
            let foundLesson = null;
            let totalLessons = 0;
            let completedLessons = 0;

            if (courseDetail.chapters) {
                for (const chapter of courseDetail.chapters) {
                    if (chapter.lessons) {
                        for (const lesson of chapter.lessons) {
                            totalLessons++;
                            if (lesson.is_completed) {
                                completedLessons++;
                            } else if (!foundLesson && !lesson.is_locked) {
                                foundLesson = lesson;
                            }
                        }
                    }
                }
            }
            
            setCurrentLesson(foundLesson);
            courseDetail.progress = totalLessons > 0 ? Math.round((completedLessons / totalLessons) * 100) : 0;
        }

      } catch (error) {
        console.error("Failed to fetch progress:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchProgress();
  }, []);

  if (loading) {
    return (
      <div className={styles.loading}>
        <div className={styles.spinner}></div>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <motion.div 
        className={styles.welcome}
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <h1 className={styles.welcomeTitle}>欢迎回来！👋</h1>
        <p className={styles.welcomeSubtitle}>继续你的 Python 学习之旅</p>
      </motion.div>

      <div className={styles.statsGrid}>
        <motion.div 
          className={styles.statCard}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.1 }}
        >
          <div className={`${styles.statIcon} ${styles.statIconBlue}`}>
            <Code size={24} />
          </div>
          <div className={styles.statInfo}>
            <div className={styles.statValue}>{stats.xp}</div>
            <div className={styles.statLabel}>经验值</div>
          </div>
        </motion.div>

        <motion.div 
          className={styles.statCard}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.2 }}
        >
          <div className={`${styles.statIcon} ${styles.statIconGreen}`}>
            <Trophy size={24} />
          </div>
          <div className={styles.statInfo}>
            <div className={styles.statValue}>{stats.badges}</div>
            <div className={styles.statLabel}>获得勋章</div>
          </div>
        </motion.div>

        <motion.div 
          className={styles.statCard}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.3 }}
        >
          <div className={`${styles.statIcon} ${styles.statIconPurple}`}>
            <BookOpen size={24} />
          </div>
          <div className={styles.statInfo}>
            <div className={styles.statValue}>{stats.courses_learned}</div>
            <div className={styles.statLabel}>学习课程</div>
          </div>
        </motion.div>

        <motion.div 
          className={styles.statCard}
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5, delay: 0.4 }}
        >
          <div className={`${styles.statIcon} ${styles.statIconOrange}`}>
            <Clock size={24} />
          </div>
          <div className={styles.statInfo}>
            <div className={styles.statValue}>{stats.study_hours}h</div>
            <div className={styles.statLabel}>学习时长</div>
          </div>
        </motion.div>
      </div>

      <motion.section 
        className={styles.section}
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5, delay: 0.5 }}
      >
        <div className={styles.sectionHeader}>
          <h2 className={styles.sectionTitle}>继续学习</h2>
          <Link to="/courses" className={styles.sectionLink}>
            查看全部 <ArrowRight size={14} />
          </Link>
        </div>

        {currentCourse ? (
          <Link 
            to={currentLesson ? `/lessons/${currentLesson.id}` : `/courses/${currentCourse.id}`} 
            className={styles.currentCourse}
          >
            <div className={styles.courseImage}>
              🐍
            </div>
            <div className={styles.courseContent}>
              <div className={styles.courseMeta}>
                <span className={styles.courseBadge}>进行中</span>
                <span className={styles.courseChapter}>第 {currentCourse.order} 章</span>
              </div>
              <h3 className={styles.courseTitle}>
                {currentLesson ? currentLesson.title : currentCourse.title}
              </h3>
              <p className={styles.courseDesc}>{currentCourse.description}</p>
              <div className={styles.courseProgress}>
                <div className={styles.progressBar}>
                  <div 
                    className={styles.progressFill} 
                    style={{ width: `${currentCourse.progress}%` }}
                  ></div>
                </div>
                <span className={styles.progressText}>{currentCourse.progress}%</span>
              </div>
            </div>
          </Link>
        ) : (
          <div className={styles.emptyState}>
            <div className={styles.emptyIcon}>📚</div>
            <p className={styles.emptyText}>暂无进行中的课程</p>
            <Link to="/courses" className={styles.emptyLink}>
              浏览课程 <ArrowRight size={16} />
            </Link>
          </div>
        )}
      </motion.section>
    </div>
  );
};

export default HomePage;
