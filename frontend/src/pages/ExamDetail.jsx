import React, { useEffect, useMemo, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { ArrowLeft, CheckCircle2 } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import { getExamDetail, submitExamAttempt } from '../lib/dataService';
import styles from './ExamDetail.module.css';

const options = ['A', 'B', 'C', 'D'];

const ExamDetail = () => {
  const { user } = useAuth();
  const navigate = useNavigate();
  const { id } = useParams();
  const [exam, setExam] = useState(null);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [result, setResult] = useState(null);

  useEffect(() => {
    const load = async () => {
      try {
        const data = await getExamDetail(id);
        setExam(data);
      } finally {
        setLoading(false);
      }
    };
    load();
  }, [id]);

  const parsedExam = useMemo(() => exam?.parsed_json || { questions: [] }, [exam]);

  const submit = async () => {
    if (!user?.id) return;
    if ((parsedExam.questions || []).length !== Object.keys(answers).length) {
      alert('请先完成全部题目');
      return;
    }
    const data = await submitExamAttempt(user.id, id, answers, parsedExam);
    setResult(data);
  };

  if (loading) return <div className="loading-panel">试卷加载中...</div>;
  if (!exam) {
    return (
      <div className="page-shell">
        <section className={`page-hero ${styles.hero}`}>
          <button type="button" onClick={() => navigate('/exams')} className={styles.backButton}>
            <ArrowLeft size={16} />
            返回考试中心
          </button>
          <h1 className="hero-title">考试功能暂未开放</h1>
          <p className="hero-subtitle">当前站点已切回 Django 后端，考试模块还在迁移中。课程学习、课时和测验功能已经可以正常使用。</p>
        </section>
      </div>
    );
  }

  return (
    <div className="page-shell">
      <section className={`page-hero ${styles.hero}`}>
        <button type="button" onClick={() => navigate('/exams')} className={styles.backButton}>
          <ArrowLeft size={16} />
          返回考试中心
        </button>
        <h1 className="hero-title">{parsedExam.title || exam.title}</h1>
        <p className="hero-subtitle">考试时间：{parsedExam.duration_minutes || exam.duration_minutes || 60} 分钟 · 满分：{parsedExam.total_score || exam.total_score || 100} 分</p>
      </section>

      <section className={styles.questionList}>
        {(parsedExam.questions || []).map((question, index) => (
          <article key={index} className={`${styles.questionCard} surface-card`}>
            <h2>{index + 1}. {question.question}</h2>
            <div className={styles.options}>
              {options.map((key) => {
                const option = question.options?.find((item) => item.key === key);
                if (!option) return null;
                const selected = answers[String(index + 1)] === key;
                return (
                  <button
                    type="button"
                    key={key}
                    className={`${styles.option} ${selected ? styles.optionSelected : ''}`}
                    onClick={() => setAnswers((prev) => ({ ...prev, [String(index + 1)]: key }))}
                    disabled={Boolean(result)}
                  >
                    <span>{key}</span>
                    <span>{option.text}</span>
                    {result && key === question.answer && <CheckCircle2 size={14} />}
                  </button>
                );
              })}
            </div>
            {result && (
              <div className={styles.explainBlock}>
                <strong>解析：</strong>{question.explanation || '暂无解析'}
              </div>
            )}
          </article>
        ))}
      </section>

      <section className={`${styles.footer} surface-card`}>
        {result ? (
          <div className={styles.result}>
            得分 {result.score}，答对 {result.correctCount}/{result.totalQuestions}
          </div>
        ) : (
          <button type="button" className="primary-button" onClick={submit}>提交试卷</button>
        )}
      </section>
    </div>
  );
};

export default ExamDetail;
