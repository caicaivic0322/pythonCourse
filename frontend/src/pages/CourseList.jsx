import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Lock, Play } from 'lucide-react';
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
        console.error("Failed to fetch courses:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchCourses();
  }, []);

  // 检查是否所有课程都被锁定（除了 GESP 1，或者如果未批准则全部锁定）
  // 实际上后端现在会返回 is_locked=True 给未批准的用户
  const isAllLocked = courses.length > 0 && courses.every(c => c.is_locked);
  
  if (loading) {
    return <div className={styles.loading}>加载中...</div>;
  }

  return (
    <div className={styles.container}>
      {isAllLocked && (
        <div className={styles.approvalWarning}>
          ⚠️ 您的账号正在等待管理员审核，暂时无法查看课程内容。
        </div>
      )}

      <div className={styles.header}>
        <div>
          <h1 className={styles.title}>课程中心</h1>
          <p className={styles.subtitle}>选择一门课程开始学习</p>
        </div>
      </div>

      <div className={styles.grid}>
        {courses.map((course, index) => (
          <motion.div
            key={course.id}
            className={`${styles.card} ${course.is_locked ? styles.locked : ''}`}
            onClick={() => !course.is_locked && navigate(`/courses/${course.id}`)}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.3, delay: index * 0.1 }}
          >
            <div className={styles.image}>
              🐍
              {course.is_locked && (
                <div className={styles.lockOverlay}>
                  <div className={styles.lockIcon}>
                    <Lock size={24} />
                  </div>
                </div>
              )}
            </div>
            <div className={styles.content}>
              <h3 className={styles.cardTitle}>{course.title}</h3>
              <p className={styles.cardDesc}>{course.description}</p>
              <div className={styles.cardFooter}>
                <span className={styles.lessonCount}>
                  {course.is_locked ? '未解锁' : '开始学习'}
                </span>
                <span className={`${styles.startBtn} ${course.is_locked ? styles.startBtnDisabled : ''}`}>
                  {course.is_locked ? <Lock size={14} /> : <Play size={14} />}
                </span>
              </div>
            </div>
          </motion.div>
        ))}
      </div>

      {courses.length === 0 && (
        <div className={styles.empty}>暂无课程</div>
      )}
    </div>
  );
};

export default CourseList;
