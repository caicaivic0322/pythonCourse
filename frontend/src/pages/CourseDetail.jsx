import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Lock, CheckCircle, PlayCircle, FileText } from 'lucide-react';
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
        console.log("Fetching course with ID:", id);
        const response = await api.get(`courses/${id}/`);
        console.log("Course data:", response.data);
        setCourse(response.data);
      } catch (error) {
        console.error("Failed to fetch course:", error);
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
    if (lesson.lesson_type === 'code') return '</>';
    if (lesson.lesson_type === 'video') return <PlayCircle size={18} />;
    return <FileText size={18} />;
  };

  const getLessonIconClass = (lesson) => {
    if (lesson.is_completed) return styles.lessonIconCompleted;
    if (lesson.is_locked) return styles.lessonIconLocked;
    if (lesson.lesson_type === 'code') return styles.lessonIconCode;
    return styles.lessonIconDefault;
  };

  const getLessonTypeText = (type) => {
    switch(type) {
      case 'code': return '代码挑战';
      case 'video': return '视频课程';
      case 'quiz': return '测验';
      default: return '图文课程';
    }
  };

  if (loading) return <div className={styles.loading}>加载任务数据中...</div>;
  if (!course) return <div className={styles.notFound}>未找到该任务。</div>;

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <div className={styles.headerInfo}>
          <h1>{course.title}</h1>
          <p>{course.description}</p>
        </div>
        <div className={styles.xpBadge}>
          <span className={styles.xpLabel}>XP 奖励</span>
          <span className={styles.xpValue}>+500 XP</span>
        </div>
      </div>

      <div className={styles.chapterList}>
        {(!course.chapters || course.chapters.length === 0) && (
            <div className={styles.chapterEmpty}>该任务暂无章节。</div>
        )}
        {course.chapters && course.chapters.map((chapter) => (
          <div key={chapter.id} className={styles.chapterCard}>
            <div className={styles.chapterHeader}>
              <h2 className={styles.chapterTitle}>{chapter.title}</h2>
              <span className={styles.chapterBadge}>第 {chapter.order} 章</span>
            </div>
            <div className={styles.chapterContent}>
              {(!chapter.lessons || chapter.lessons.length === 0) && (
                  <div className={styles.lessonEmpty}>本章暂无课程。</div>
              )}
              {chapter.lessons && chapter.lessons.map((lesson) => (
                <div 
                  key={lesson.id} 
                  onClick={() => !lesson.is_locked && navigate(`/lessons/${lesson.id}`)}
                  className={`${styles.lessonItem} ${lesson.is_locked ? styles.locked : ''}`}
                >
                  <div className={styles.lessonLeft}>
                    <div className={`${styles.lessonIcon} ${getLessonIconClass(lesson)}`}>
                      {getLessonIcon(lesson)}
                    </div>
                    <div>
                      <h3 className={styles.lessonTitle}>{lesson.title}</h3>
                      <span className={styles.lessonMeta}>
                          {getLessonTypeText(lesson.lesson_type)}
                          {lesson.is_completed && <span className={styles.lessonCompleted}>已完成</span>}
                      </span>
                    </div>
                  </div>
                  
                  {!lesson.is_locked && (
                      <span className={styles.lessonAction}>
                        {lesson.is_completed ? '复习 →' : '开始 →'}
                      </span>
                  )}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      <div className={styles.practiceSection}>
        <h2 className={styles.practiceTitle}>自由练习区</h2>
        <CodeRunner />
      </div>
    </div>
  );
};

export default CourseDetail;
