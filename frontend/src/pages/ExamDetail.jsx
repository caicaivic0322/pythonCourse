import React, { useCallback, useEffect, useRef, useState } from 'react';
import { useNavigate, useParams } from 'react-router-dom';
import { ArrowLeft, CheckCircle2, Clock3, XCircle } from 'lucide-react';
import { getExamDetail, startExam, submitExamAttempt } from '../lib/dataService';
import styles from './ExamDetail.module.css';

const OPTION_KEYS = ['A', 'B', 'C', 'D'];

const ExamDetail = () => {
  const navigate = useNavigate();
  const { id } = useParams();
  const [exam, setExam] = useState(null);
  const [answers, setAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [submitting, setSubmitting] = useState(false);
  const [result, setResult] = useState(null);
  const [timeLeft, setTimeLeft] = useState(null);
  const timerRef = useRef(null);

  useEffect(() => {
    const load = async () => {
      try {
        const data = await getExamDetail(id);
        setExam(data);
        setTimeLeft(data.duration_minutes * 60);
        await startExam(id); // 创建/续考试记录
      } catch (err) {
        console.error('加载考试失败', err);
      } finally {
        setLoading(false);
      }
    };
    load();
  }, [id]);

  // 倒计时
  useEffect(() => {
    if (timeLeft === null || timeLeft <= 0 || result) return;
    timerRef.current = setInterval(() => {
      setTimeLeft((prev) => {
        if (prev <= 1) {
          clearInterval(timerRef.current);
          return 0;
        }
        return prev - 1;
      });
    }, 1000);
    return () => clearInterval(timerRef.current);
  }, [timeLeft, result]);

  const formatTime = useCallback((seconds) => {
    const m = Math.floor(seconds / 60);
    const s = seconds % 60;
    return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`;
  }, []);

  // 构建选项列表
  const buildOptions = useCallback((q) => {
    return OPTION_KEYS
      .filter((key) => q[`option_${key.toLowerCase()}`])
      .map((key) => ({ key, text: q[`option_${key.toLowerCase()}`] }));
  }, []);

  const questions = exam?.questions || [];

  const handleSelect = (questionNumber, key) => {
    if (result) return;
    setAnswers((prev) => ({ ...prev, [String(questionNumber)]: key }));
  };

  const handleSubmit = async () => {
    const unanswered = questions.filter(
      (q) => !answers[String(q.question_number)]
    );
    if (unanswered.length > 0) {
      const proceed = window.confirm(
        `还有 ${unanswered.length} 道题未作答，确定提交吗？`
      );
      if (!proceed) return;
    }

    setSubmitting(true);
    try {
      const data = await submitExamAttempt(id, answers);
      setResult(data);
      clearInterval(timerRef.current);
    } catch (err) {
      alert(err.message || '提交失败，请重试');
    } finally {
      setSubmitting(false);
    }
  };

  if (loading) return <div className="loading-panel">试卷加载中...</div>;
  if (!exam) {
    return (
      <div className="page-shell">
        <section className={`page-hero ${styles.hero}`}>
          <button type="button" onClick={() => navigate('/exams')} className={styles.backButton}>
            <ArrowLeft size={16} /> 返回考试中心
          </button>
          <h1 className="hero-title">试卷未找到</h1>
          <p className="hero-subtitle">该考试可能尚未发布或已被移除。</p>
        </section>
      </div>
    );
  }

  const progressPct = questions.length > 0
    ? Math.round((Object.keys(answers).length / questions.length) * 100)
    : 0;

  return (
    <div className="page-shell">
      <section className={`page-hero ${styles.hero}`}>
        <button type="button" onClick={() => navigate('/exams')} className={styles.backButton}>
          <ArrowLeft size={16} /> 返回考试中心
        </button>
        <h1 className="hero-title">{exam.title}</h1>
        <div className={styles.examMeta}>
          <span><Clock3 size={14} /> {exam.duration_minutes} 分钟</span>
          <span>满分 {exam.total_score} 分</span>
          <span>{exam.question_count} 题</span>
          {!result && (
            <span className={`${styles.timer} ${timeLeft <= 300 ? styles.timerWarn : ''}`}>
              ⏱ {formatTime(timeLeft)}
            </span>
          )}
        </div>
        {!result && (
          <div className={styles.progressBar}>
            <div className={styles.progressFill} style={{ width: `${progressPct}%` }} />
            <span className={styles.progressLabel}>已答 {Object.keys(answers).length}/{questions.length}</span>
          </div>
        )}
      </section>

      {result && (
        <section className={`${styles.resultBanner} surface-card`}>
          <div className={styles.resultScore}>
            <span className={styles.scoreNumber}>{result.score}</span>
            <span className={styles.scoreUnit}>/ {exam.total_score} 分</span>
          </div>
          <div className={styles.resultMeta}>
            {result.is_passed ? (
              <span className={styles.passed}><CheckCircle2 size={16} /> 通过</span>
            ) : (
              <span className={styles.failed}><XCircle size={16} /> 未通过</span>
            )}
            <span>答对 {result.correctCount}/{result.totalQuestions} 题</span>
          </div>
        </section>
      )}

      <section className={styles.questionList}>
        {questions.map((q) => {
          const qNum = String(q.question_number);
          const selected = answers[qNum];
          const options = buildOptions(q);
          // 提交后从 result 中找对应题目的结果
          const qResult = result?.questions?.find(
            (r) => r.question === q.question
          );

          return (
            <article key={q.id} className={`${styles.questionCard} surface-card`}>
              <h2>
                {q.question_number}. {q.question}
                <span className={styles.questionType}>
                  {q.question_type === 'single_choice' ? '单选' :
                   q.question_type === 'multiple_choice' ? '多选' : '判断'}
                </span>
              </h2>
              <div className={styles.options}>
                {options.map((opt) => {
                  let optClass = styles.option;
                  if (qResult) {
                    if (opt.key === qResult.answer) optClass += ` ${styles.optionCorrect}`;
                    if (opt.key === selected && opt.key !== qResult.answer) optClass += ` ${styles.optionWrong}`;
                  } else if (opt.key === selected) {
                    optClass += ` ${styles.optionSelected}`;
                  }
                  return (
                    <button
                      type="button"
                      key={opt.key}
                      className={optClass}
                      onClick={() => handleSelect(q.question_number, opt.key)}
                      disabled={Boolean(result)}
                    >
                      <span className={styles.optKey}>{opt.key}</span>
                      <span>{opt.text}</span>
                      {qResult && opt.key === qResult.answer && <CheckCircle2 size={14} className={styles.optIcon} />}
                      {qResult && opt.key === selected && opt.key !== qResult.answer && <XCircle size={14} className={styles.optIcon} />}
                    </button>
                  );
                })}
              </div>
              {qResult && (
                <div className={styles.explainBlock}>
                  <strong>解析：</strong>{qResult.explanation || '暂无解析'}
                </div>
              )}
            </article>
          );
        })}
      </section>

      {!result && (
        <section className={`${styles.footer} surface-card`}>
          <button
            type="button"
            className="primary-button"
            onClick={handleSubmit}
            disabled={submitting}
          >
            {submitting ? '提交中...' : '提交试卷'}
          </button>
        </section>
      )}
    </div>
  );
};

export default ExamDetail;
