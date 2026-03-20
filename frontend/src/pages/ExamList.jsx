import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Clock3, FileText, Trophy } from 'lucide-react';
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
          <p className="hero-subtitle">考试模块正在迁回当前 Django 后端，课程学习主链路已经恢复，考试功能会在后续版本补齐。</p>
        </div>
      </section>

      <section className={styles.grid}>
        {exams.map((exam) => (
          <Link key={exam.id} to={`/exams/${exam.id}`} className={`${styles.card} surface-card`}>
            <h2>{exam.title}</h2>
            <div className={styles.metaRow}>
              <span><Clock3 size={14} /> {exam.duration_minutes || exam.parsed_json?.duration_minutes || 60} 分钟</span>
              <span><Trophy size={14} /> {exam.total_score || exam.parsed_json?.total_score || 100} 分</span>
              <span><FileText size={14} /> {exam.question_count} 题</span>
            </div>
            <p>{exam.subject || '综合测试'}</p>
          </Link>
        ))}
      </section>

      {exams.length === 0 && <div className="empty-panel">暂时没有可用试卷。当前版本已切回 Django 后端，考试功能正在补齐中。</div>}
    </div>
  );
};

export default ExamList;
