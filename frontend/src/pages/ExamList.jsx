import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Clock3, FileText, Trophy, CheckCircle2 } from 'lucide-react';
import { getPublishedExams } from '../lib/dataService';
import styles from './ExamList.module.css';

const ExamList = () => {
  const [exams, setExams] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const load = async () => {
      try {
        const data = await getPublishedExams();
        setExams(data);
      } finally {
        setLoading(false);
      }
    };
    load();
  }, []);

  if (loading) return <div className="loading-panel">试卷加载中...</div>;

  return (
    <div className="page-shell">
      <section className={`page-hero ${styles.hero}`}>
        <div>
          <span className="eyebrow">Exam Center</span>
          <h1 className="hero-title">考试中心</h1>
          <p className="hero-subtitle">选择一场考试来检验你的 Python 学习成果，每场考试限时完成，提交后即时出分。</p>
        </div>
      </section>

      <section className={styles.grid}>
        {exams.map((exam) => (
          <Link key={exam.id} to={`/exams/${exam.id}`} className={`${styles.card} surface-card`}>
            <div className={styles.cardHeader}>
              <h2>{exam.title}</h2>
              {exam.has_attempted && <span className={styles.badge}><CheckCircle2 size={12} /> 已完成</span>}
            </div>
            <div className={styles.metaRow}>
              <span><Clock3 size={14} /> {exam.duration_minutes} 分钟</span>
              <span><Trophy size={14} /> {exam.total_score} 分</span>
              <span><FileText size={14} /> {exam.question_count} 题</span>
            </div>
            {exam.description && <p>{exam.description}</p>}
            {exam.best_score !== null && (
              <p className={styles.bestScore}>历史最佳：{exam.best_score} 分</p>
            )}
          </Link>
        ))}
      </section>

      {exams.length === 0 && (
        <div className="empty-panel">暂无可用考试，请稍后再来。</div>
      )}
    </div>
  );
};

export default ExamList;
