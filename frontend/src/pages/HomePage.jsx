import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { ArrowRight, BookOpen, Clock3, Code2, Trophy } from 'lucide-react';
import api from '../api/axios';
import styles from './HomePage.module.css';

const statItems = [
  { key: 'xp', label: '经验值', icon: Code2, suffix: '' },
  { key: 'badges', label: '获得勋章', icon: Trophy, suffix: '' },
  { key: 'courses_learned', label: '参与课程', icon: BookOpen, suffix: '' },
  { key: 'study_hours', label: '学习时长', icon: Clock3, suffix: 'h' },
];

const HomePage = () => {
  const [currentCourse, setCurrentCourse] = useState(null);
  const [currentLesson, setCurrentLesson] = useState(null);
  const [stats, setStats] = useState({ xp: 0, badges: 0, courses_learned: 0, study_hours: 0 });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProgress = async () => {
      try {
        const statsRes = await api.get('users/stats/');
        setStats(statsRes.data);

        const response = await api.get('courses/');
        const courses = response.data;

        let activeCourse = courses.find((course) => !course.is_locked && !course.is_completed);

        if (!activeCourse) {
          activeCourse = [...courses].reverse().find((course) => !course.is_locked) || courses[0];
        }

        if (activeCourse) {
          const detailRes = await api.get(`courses/${activeCourse.id}/`);
          const courseDetail = detailRes.data;
          setCurrentCourse(courseDetail);

          let foundLesson = null;
          let totalLessons = 0;
          let completedLessons = 0;

          courseDetail.chapters?.forEach((chapter) => {
            chapter.lessons?.forEach((lesson) => {
              totalLessons += 1;
              if (lesson.is_completed) {
                completedLessons += 1;
              } else if (!foundLesson && !lesson.is_locked) {
                foundLesson = lesson;
              }
            });
          });

          setCurrentLesson(foundLesson);
          courseDetail.progress = totalLessons > 0 ? Math.round((completedLessons / totalLessons) * 100) : 0;
        }
      } catch (error) {
        console.error('Failed to fetch progress:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchProgress();
  }, []);

  if (loading) {
    return <div className="loading-panel">正在整理你的学习面板...</div>;
  }

  return (
    <div className="page-shell">
      <section className={`page-hero ${styles.hero}`}>
        <div className={styles.heroContent}>
          <span className="eyebrow">Today Focus</span>
          <h1 className="hero-title">学习总览</h1>
          <p className="hero-subtitle">
            这里是你的总览工作台。查看成长数据、快速继续当前课程，并把学习和练习安排在同一个清晰的界面里。
          </p>
          <div className={styles.heroActions}>
            <Link to={currentLesson ? `/lessons/${currentLesson.id}` : '/courses'} className="primary-button">
              {currentLesson ? '继续当前课程' : '浏览课程'}
              <ArrowRight size={18} />
            </Link>
            <Link to="/courses" className="secondary-button">查看学习路径</Link>
          </div>
        </div>

        <div className={styles.heroAside}>
          <div className={styles.heroStatLabel}>本周学习状态</div>
          <div className={styles.heroStatValue}>{stats.study_hours}h</div>
          <p className={styles.heroStatText}>累计学习时长配合经验值和课程进度，帮助你持续追踪节奏。</p>
        </div>
      </section>

      <section className={styles.statsGrid}>
        {statItems.map((item, index) => {
          const Icon = item.icon;
          return (
            <div
              key={item.key}
              className={`${styles.statCard} surface-card`}
              style={{ animationDelay: `${0.08 * index}s` }}
            >
              <div className={styles.statIcon}>
                <Icon size={20} />
              </div>
              <div>
                <div className="metric-value">
                  {stats[item.key]}
                  {item.suffix}
                </div>
                <div className={styles.statLabel}>{item.label}</div>
              </div>
            </div>
          );
        })}
      </section>

      <section className={styles.learningGrid}>
        <div className={`${styles.mainPanel} surface-card`}>
          <div className={styles.panelHeader}>
            <div>
              <h2 className="section-title">继续学习</h2>
              <p className="section-subtitle">系统已为你定位到最适合继续推进的课程节点。</p>
            </div>
            <Link to="/courses" className={styles.inlineLink}>
              全部课程
              <ArrowRight size={16} />
            </Link>
          </div>

          {currentCourse ? (
            <Link
              to={currentLesson ? `/lessons/${currentLesson.id}` : `/courses/${currentCourse.id}`}
              className={styles.coursePanel}
            >
              <div className={styles.courseVisual}>
                <span className={styles.courseVisualBadge}>进行中</span>
                <strong>Chapter {currentCourse.order}</strong>
                <span>Python Path</span>
              </div>

              <div className={styles.courseBody}>
                <div className={styles.courseMeta}>
                  <span className="chip">课程进度 {currentCourse.progress}%</span>
                  {currentLesson && <span className="chip">下一节 {currentLesson.title}</span>}
                </div>
                <h3>{currentLesson ? currentLesson.title : currentCourse.title}</h3>
                <p>{currentCourse.description}</p>
                <div className={styles.progressRow}>
                  <div className={styles.progressTrack}>
                    <div className={styles.progressFill} style={{ width: `${currentCourse.progress}%` }} />
                  </div>
                  <span>{currentCourse.progress}%</span>
                </div>
              </div>
            </Link>
          ) : (
            <div className="empty-panel">当前还没有可继续的课程，去课程中心看看吧。</div>
          )}
        </div>

        <aside className={`${styles.sidePanel} surface-card`}>
          <h2 className="section-title">学习建议</h2>
          <p className="section-subtitle">保持轻量但连续的节奏，比单次高强度更容易形成稳定习惯。</p>
          <div className={styles.tipList}>
            <div className={styles.tipItem}>
              <span className={styles.tipIndex}>01</span>
              <p>先完成当前未锁定课程，再进入自由练习区复现关键代码。</p>
            </div>
            <div className={styles.tipItem}>
              <span className={styles.tipIndex}>02</span>
              <p>把测验当作复盘工具，优先关注错题解释，而不是只追求一次通过。</p>
            </div>
            <div className={styles.tipItem}>
              <span className={styles.tipIndex}>03</span>
              <p>学习时间不必很长，但建议固定时段，形成可重复的输入节奏。</p>
            </div>
          </div>
        </aside>
      </section>
    </div>
  );
};

export default HomePage;
