import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import api from '../api/axios';
import CodeRunner from '../components/CodeRunner';
import { ArrowLeft, CheckCircle, PlayCircle, FileText } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { atomDark } from 'react-syntax-highlighter/dist/esm/styles/prism';
import styles from './LessonDetail.module.css';

const LessonDetail = () => {
  const { id } = useParams();
  const [lesson, setLesson] = useState(null);
  const [loading, setLoading] = useState(true);
  const [quizAnswers, setQuizAnswers] = useState({});
  const [quizResult, setQuizResult] = useState(null);
  const [submitting, setSubmitting] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchLesson = async () => {
      try {
        setLoading(true);
        const response = await api.get(`courses/lessons/${id}/`);
        setLesson(response.data);
        if (response.data.user_progress && response.data.user_progress.is_completed) {
            setQuizResult({
                passed: true,
                score: response.data.user_progress.score,
                message: "您已完成本节课！"
            });
        }
      } catch (error) {
        console.error("Failed to fetch lesson:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchLesson();
    setQuizAnswers({});
    setQuizResult(null);
  }, [id]);

  const handleQuizSubmit = async () => {
      if (!lesson || !lesson.quizzes) return;
      
      if (Object.keys(quizAnswers).length < lesson.quizzes.length) {
          alert("请回答所有问题后再提交！");
          return;
      }

      setSubmitting(true);
      try {
          const response = await api.post(`courses/lessons/${id}/complete/`, {
              quiz_answers: quizAnswers
          });
          setQuizResult(response.data);
      } catch (error) {
          console.error("Failed to submit quiz:", error);
          alert("提交失败，请重试。");
      } finally {
          setSubmitting(false);
      }
  };

  const handleNextLesson = () => {
      if (lesson.next_lesson_id) {
          navigate(`/lessons/${lesson.next_lesson_id}`);
      } else {
          navigate(`/courses/${lesson.course_id}`);
      }
  };

  const getLessonTypeText = (type) => {
    switch(type) {
      case 'code': return '代码挑战';
      case 'video': return '视频课程';
      case 'quiz': return '测验';
      default: return '图文课程';
    }
  };

  const getOptionClass = (quiz, optionKey, isSubmitted) => {
    const isSelected = quizAnswers[quiz.id] === optionKey;
    const isCorrect = optionKey === quiz.correct_answer;
    
    if (isSubmitted) {
      if (isCorrect) return styles.quizOptionCorrect;
      if (isSelected && !isCorrect) return styles.quizOptionWrong;
      return `${styles.quizOptionDefault} ${styles.quizOptionDisabled}`;
    }
    if (isSelected) return styles.quizOptionSelected;
    return styles.quizOptionDefault;
  };

  const getMarkerClass = (quiz, optionKey, isSubmitted) => {
    const isSelected = quizAnswers[quiz.id] === optionKey;
    const isCorrect = optionKey === quiz.correct_answer;
    
    if (isSubmitted) {
      if (isCorrect) return styles.optionMarkerCorrect;
      if (isSelected) return styles.optionMarkerWrong;
      return styles.optionMarkerDefault;
    }
    if (isSelected) return styles.optionMarkerSelected;
    return styles.optionMarkerDefault;
  };

  if (loading) return <div className={styles.loading}>加载课程数据中...</div>;
  if (!lesson) return <div className={styles.notFound}>未找到该课程。</div>;

  return (
    <div className={styles.container}>
      <div className={styles.header}>
        <button 
          onClick={() => navigate(-1)} 
          className={styles.backButton}
        >
          <ArrowLeft size={20} />
        </button>
        <div className={styles.headerMeta}>
          <span className={styles.headerLabel}>
            {getLessonTypeText(lesson.lesson_type)}
          </span>
          <h1 className={styles.headerTitle}>{lesson.title}</h1>
        </div>
      </div>

      <div className={styles.contentArea}>
        {lesson.lesson_type === 'video' && lesson.video_url && (
          <div className={styles.videoContainer}>
             <div className={styles.videoOverlay}>
                <p className={styles.videoText}>视频播放器占位符: {lesson.video_url}</p>
             </div>
             <PlayCircle size={64} className={styles.videoIcon} />
          </div>
        )}

        {lesson.content && (
          <div className={styles.markdownContent}>
            <ReactMarkdown
              children={lesson.content}
              remarkPlugins={[remarkGfm]}
              components={{
                code({node, inline, className, children, ...props}) {
                  const match = /language-(\w+)/.exec(className || '')
                  return !inline && match ? (
                    <SyntaxHighlighter
                      {...props}
                      children={String(children).replace(/\n$/, '')}
                      style={atomDark}
                      language={match[1]}
                      PreTag="div"
                    />
                  ) : (
                    <code {...props} className={className}>
                      {children}
                    </code>
                  )
                }
              }}
            />
          </div>
        )}

        {(lesson.lesson_type === 'text' || lesson.lesson_type === 'code') && (
          <div className={styles.practiceSection}>
            <h3 className={styles.practiceTitle}>
              <span>⚡</span> 动手试一试
            </h3>
            <p className={styles.practiceHint}>
                光看不练假把式，快在下方编写代码验证你的想法吧！
            </p>
            <CodeRunner initialCode={lesson.code_challenge_prompt || `# ${lesson.title} - 练习区
# 请在下方编写你的代码
print('Hello, Python!')`} />
          </div>
        )}

        {lesson.quizzes && lesson.quizzes.length > 0 && (
            <div className={styles.quizSection}>
                <div className={styles.quizHeader}>
                    <h3 className={styles.quizTitle}>
                        <span className={styles.quizEmoji}>📝</span> 随堂小测
                    </h3>
                    {quizResult && quizResult.passed && (
                        <div className={styles.quizPassed}>
                            已通过 (得分: {quizResult.score})
                        </div>
                    )}
                </div>
                
                <div className={styles.quizList}>
                    {lesson.quizzes.map((quiz, qIdx) => (
                        <div key={quiz.id} className={styles.quizItem}>
                            <p className={styles.quizQuestion}>
                                <span className={styles.quizQuestionNum}>Q{qIdx + 1}.</span>
                                {quiz.question}
                            </p>
                            
                            <div className={styles.quizOptions}>
                                {[
                                    { key: 'A', text: quiz.option_a },
                                    { key: 'B', text: quiz.option_b },
                                    { key: 'C', text: quiz.option_c },
                                    { key: 'D', text: quiz.option_d }
                                ].map((option) => {
                                    const isSubmitted = !!quizResult;
                                    
                                    return (
                                        <button 
                                            key={option.key}
                                            disabled={isSubmitted}
                                            className={`${styles.quizOption} ${getOptionClass(quiz, option.key, isSubmitted)}`}
                                            onClick={() => {
                                                if (isSubmitted) return;
                                                setQuizAnswers(prev => ({
                                                    ...prev,
                                                    [quiz.id]: option.key
                                                }));
                                            }}
                                        >
                                            <span className={`${styles.optionMarker} ${getMarkerClass(quiz, option.key, isSubmitted)}`}>
                                                {option.key}
                                            </span>
                                            {option.text}
                                            {isSubmitted && option.key === quiz.correct_answer && <span className={`${styles.correctBadge} ${styles.correctText}`}>正确答案</span>}
                                            {isSubmitted && quizAnswers[quiz.id] === option.key && option.key !== quiz.correct_answer && <span className={`${styles.correctBadge} ${styles.wrongText}`}>错误</span>}
                                        </button>
                                    );
                                })}
                            </div>
                            
                            {quizResult && (
                                <div className={`${styles.explanation} ${quizAnswers[quiz.id] === quiz.correct_answer ? styles.explanationCorrect : styles.explanationWrong}`}>
                                    <p className={styles.explanationTitle}>解析：</p>
                                    <p>{quiz.explanation}</p>
                                </div>
                            )}
                        </div>
                    ))}
                </div>
                
                <div className={styles.quizFooter}>
                     <div className={styles.quizMessage}>
                         {quizResult && !quizResult.passed && (
                             <span className={styles.messageError}>{quizResult.message || `得分 ${quizResult.score}，未达到 50%，请重试！`}</span>
                         )}
                         {quizResult && quizResult.passed && (
                             <span className={styles.messageSuccess}>恭喜！您已掌握本节内容。</span>
                         )}
                         {!quizResult && (
                             <span className={styles.messageDefault}>请完成所有题目后提交。</span>
                         )}
                     </div>
                     
                     {!quizResult?.passed && (
                         <button 
                            onClick={() => {
                                if (quizResult && !quizResult.passed) {
                                    setQuizResult(null);
                                } else {
                                    handleQuizSubmit();
                                }
                            }}
                            disabled={submitting}
                            className={`${styles.quizButton} ${quizResult && !quizResult.passed ? styles.quizButtonRetry : styles.quizButtonSubmit}`}
                         >
                            {submitting ? '提交中...' : (quizResult && !quizResult.passed ? '重试' : '提交答案')}
                         </button>
                     )}
                </div>
            </div>
        )}
      </div>

      <div className={styles.footerNav}>
        <button 
            onClick={() => lesson.prev_lesson_id && navigate(`/lessons/${lesson.prev_lesson_id}`)}
            disabled={!lesson.prev_lesson_id}
            className={`${styles.navButton} ${styles.navButtonPrev}`}
        >
            上一节
        </button>
        
        {(!lesson.quizzes || lesson.quizzes.length === 0 || (quizResult && quizResult.passed)) ? (
            <button 
                onClick={handleNextLesson}
                className={`${styles.navButton} ${styles.navButtonNext}`}
            >
                {lesson.next_lesson_id ? '下一节' : '完成本章'} <CheckCircle size={18} />
            </button>
        ) : (
            <div className={styles.navButtonLocked}>
                <span>请先通过测验解锁</span>
                <CheckCircle size={18} />
            </div>
        )}
      </div>
    </div>
  );
};

export default LessonDetail;
