import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { CheckCircle, FileText, Lock, PlayCircle, Sparkles } from 'lucide-react';
import api from '../api/axios';
import CodeRunner from '../components/CodeRunner';
import styles from './CourseDetail.module.css';

const CourseDetail = () => {
  const { id } = useParams();
  const [course, setCourse] = useState(null);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchCourse = async () => {
      try {
        const response = await api.get(`courses/${id}/`);
        setCourse(response.data);
      } catch (error) {
        console.error('Failed to fetch course:', error);
      } finally {
        setLoading(false);
      }
    };

    if (id) {
      fetchCourse();
    }
  }, [id]);

  const getLessonIcon = (lesson) => {
    if (lesson.is_locked) return <Lock size={18} />;
    if (lesson.is_completed) return <CheckCircle size={18} />;
    if (lesson.lesson_type === 'video') return <PlayCircle size={18} />;
    return <FileText size={18} />;
  };

  const getLessonTypeText = (type) => {
    switch (type) {
      case 'code':
        return '代码挑战';
      case 'video':
        return '视频课程';
      case 'quiz':
        return '测验';
      default:
        return '图文课程';
    }
  };

  const totalLessons = course?.chapters?.reduce((sum, chapter) => sum + (chapter.lessons?.length || 0), 0) || 0;
  const completedLessons = course?.chapters?.reduce(
    (sum, chapter) => sum + (chapter.lessons?.filter((lesson) => lesson.is_completed).length || 0),
    0
  ) || 0;
  const progress = totalLessons > 0 ? Math.round((completedLessons / totalLessons) * 100) : 0;

  if (loading) return <div className="loading-panel">课程详情加载中...</div>;
  if (!course) return <div className="empty-panel">未找到该课程。</div>;

  return (
    <div className="page-shell">
      <section className={`page-hero ${styles.hero}`}>
        <div>
          <span className="eyebrow">Course Detail</span>
          <h1 className={`hero-title ${styles.courseTitle}`}>{course.title}</h1>
          <p className="hero-subtitle">{course.description}</p>
          <div className={styles.heroMeta}>
            <span className="chip">章节 {course.chapters?.length || 0}</span>
            <span className="chip">课时 {totalLessons}</span>
            <span className="chip">完成度 {progress}%</span>
          </div>
        </div>

        <div className={styles.rewardCard}>
          <span>课程奖励</span>
          <strong>+500 XP</strong>
          <p>完成课程与测验后可积累经验值，形成持续反馈。</p>
        </div>
      </section>

      <section className="page-grid-two">
        <div className={styles.chapterList}>
          {(!course.chapters || course.chapters.length === 0) && (
            <div className="empty-panel">该课程暂无章节。</div>
          )}

          {course.chapters?.map((chapter) => (
            <article key={chapter.id} className={`${styles.chapterCard} surface-card`}>
              <div className={styles.chapterHeader}>
                <div>
                  <span className="eyebrow">Chapter {chapter.order}</span>
                  <h2>{chapter.title}</h2>
                </div>
                <span className={styles.chapterCount}>{chapter.lessons?.length || 0} 节</span>
              </div>

              <div className={styles.lessonList}>
                {(!chapter.lessons || chapter.lessons.length === 0) && (
                  <div className="empty-panel">本章暂无课程。</div>
                )}

                {chapter.lessons?.map((lesson) => (
                  <button
                    key={lesson.id}
                    type="button"
                    onClick={() => !lesson.is_locked && navigate(`/lessons/${lesson.id}`)}
                    className={`${styles.lessonItem} ${lesson.is_locked ? styles.locked : ''}`}
                  >
                    <div className={styles.lessonLeft}>
                      <span className={`${styles.lessonIcon} ${lesson.is_completed ? styles.done : ''}`}>
                        {getLessonIcon(lesson)}
                      </span>
                      <div className={styles.lessonText}>
                        <strong>{lesson.title}</strong>
                        <span>
                          {getLessonTypeText(lesson.lesson_type)}
                          {lesson.is_completed && ' · 已完成'}
                        </span>
                      </div>
                    </div>

                    <span className={styles.lessonAction}>
                      {lesson.is_locked ? '未解锁' : lesson.is_completed ? '复习' : '开始'}
                    </span>
                  </button>
                ))}
              </div>
            </article>
          ))}
        </div>

        <aside className={styles.sideColumn}>
          <div className={`${styles.summaryCard} surface-card`}>
            <div className={styles.summaryTop}>
              <Sparkles size={18} />
              学习建议
            </div>
            <p>先完成未锁定课时，再到自由练习区把关键代码重写一遍，学习效率会明显更高。</p>
            <div className={styles.summaryMetric}>
              <strong>{progress}%</strong>
              <span>当前课程完成度</span>
            </div>
          </div>

          <div className={`${styles.practiceSection} surface-card`}>
            <h2 className="section-title">自由练习区</h2>
            <p className="section-subtitle">不离开课程页面，直接验证知识点和代码片段。</p>
            <div className={styles.runnerWrap}>
              <CodeRunner />
            </div>
          </div>
        </aside>
      </section>
    </div>
  );
};

export default CourseDetail;
