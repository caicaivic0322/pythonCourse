import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Lock, Play, Sparkles } from 'lucide-react';
import api from '../api/axios';
import styles from './CourseList.module.css';

const CourseList = () => {
  const [courses, setCourses] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCourses = async () => {
      try {
        const response = await api.get('courses/');
        setCourses(response.data);
      } catch (error) {
        console.error('Failed to fetch courses:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchCourses();
  }, []);

  const isAllLocked = courses.length > 0 && courses.every((course) => course.is_locked);

  if (loading) {
    return <div className="loading-panel">课程目录加载中...</div>;
  }

  return (
    <div className="page-shell">
      <section className={`page-hero ${styles.hero}`}>
        <div>
          <span className="eyebrow">Learning Path</span>
          <h1 className="hero-title">课程中心</h1>
          <p className="hero-subtitle">
            每门课程都围绕清晰的章节结构展开。你可以快速看到哪些内容已完成、哪些内容尚未解锁，以及现在最适合继续的学习节点。
          </p>
        </div>
        <div className={styles.heroStat}>
          <span>可见课程</span>
          <strong>{courses.length}</strong>
          <p>课程按学习路径组织，保持从入门到实践的递进节奏。</p>
        </div>
      </section>

      {isAllLocked && (
        <div className={styles.warning}>
          <Sparkles size={18} />
          <span>你的账号正在等待管理员审核，暂时无法查看课程内容。</span>
        </div>
      )}

      <section className={styles.grid}>
        {courses.map((course, index) => (
          <article
            key={course.id}
            className={`${styles.card} surface-card ${course.is_locked ? styles.locked : ''}`}
            onClick={() => !course.is_locked && navigate(`/courses/${course.id}`)}
            style={{ animationDelay: `${index * 0.06}s` }}
          >
            <div className={styles.cover}>
              <div className={styles.coverGlow} />
              <span className={styles.coverBadge}>{course.is_locked ? '待解锁' : '开放中'}</span>
              <strong>{String(index + 1).padStart(2, '0')}</strong>
              <p>Python Course</p>
              {course.is_locked && (
                <div className={styles.lockOverlay}>
                  <Lock size={24} />
                </div>
              )}
            </div>

            <div className={styles.content}>
              <div className={styles.metaRow}>
                <span className="chip">{course.is_locked ? '未开放' : '立即进入'}</span>
              </div>
              <h2>{course.title}</h2>
              <p>{course.description}</p>
              <div className={styles.footer}>
                <span>{course.is_locked ? '需要先解锁权限' : '查看章节与练习'}</span>
                <span className={styles.actionIcon}>
                  {course.is_locked ? <Lock size={14} /> : <Play size={14} />}
                </span>
              </div>
            </div>
          </article>
        ))}
      </section>

      {courses.length === 0 && <div className="empty-panel">当前暂无课程。</div>}
    </div>
  );
};

export default CourseList;
