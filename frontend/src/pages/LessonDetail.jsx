import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import CodeRunner from '../components/CodeRunner';
import { ArrowLeft, CheckCircle, PlayCircle } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { useAuth } from '../contexts/AuthContext';
import { getLessonDetail, submitLessonQuiz } from '../lib/dataService';
import styles from './LessonDetail.module.css';

const blockKeywords = ['def', 'if', 'elif', 'else', 'for', 'while', 'try', 'except', 'finally', 'with', 'class', 'match', 'case'];
const dedentKeywords = new Set(['elif', 'else', 'except', 'finally', 'case']);
const inlineBlockEndToken = '__INLINE_BLOCK_END__';

const splitTopLevelStatements = (text) => {
  const statements = [];
  let current = '';
  let inSingleQuote = false;
  let inDoubleQuote = false;
  let parenthesesDepth = 0;
  let bracketDepth = 0;
  let braceDepth = 0;

  for (let index = 0; index < text.length; index += 1) {
    const char = text[index];
    const previousChar = text[index - 1];

    if (char === "'" && !inDoubleQuote && previousChar !== '\\') {
      inSingleQuote = !inSingleQuote;
    } else if (char === '"' && !inSingleQuote && previousChar !== '\\') {
      inDoubleQuote = !inDoubleQuote;
    } else if (!inSingleQuote && !inDoubleQuote) {
      if (char === '(') parenthesesDepth += 1;
      if (char === ')') parenthesesDepth = Math.max(parenthesesDepth - 1, 0);
      if (char === '[') bracketDepth += 1;
      if (char === ']') bracketDepth = Math.max(bracketDepth - 1, 0);
      if (char === '{') braceDepth += 1;
      if (char === '}') braceDepth = Math.max(braceDepth - 1, 0);
    }

    if (
      char === ';' &&
      !inSingleQuote &&
      !inDoubleQuote &&
      parenthesesDepth === 0 &&
      bracketDepth === 0 &&
      braceDepth === 0
    ) {
      if (current.trim()) {
        statements.push(current.trim());
      }
      current = '';
      continue;
    }

    current += char;
  }

  if (current.trim()) {
    statements.push(current.trim());
  }

  return statements;
};

const findTopLevelColonIndex = (text) => {
  let inSingleQuote = false;
  let inDoubleQuote = false;
  let parenthesesDepth = 0;
  let bracketDepth = 0;
  let braceDepth = 0;

  for (let index = 0; index < text.length; index += 1) {
    const char = text[index];
    const previousChar = text[index - 1];

    if (char === "'" && !inDoubleQuote && previousChar !== '\\') {
      inSingleQuote = !inSingleQuote;
    } else if (char === '"' && !inSingleQuote && previousChar !== '\\') {
      inDoubleQuote = !inDoubleQuote;
    } else if (!inSingleQuote && !inDoubleQuote) {
      if (char === '(') parenthesesDepth += 1;
      if (char === ')') parenthesesDepth = Math.max(parenthesesDepth - 1, 0);
      if (char === '[') bracketDepth += 1;
      if (char === ']') bracketDepth = Math.max(bracketDepth - 1, 0);
      if (char === '{') braceDepth += 1;
      if (char === '}') braceDepth = Math.max(braceDepth - 1, 0);
    }

    if (
      char === ':' &&
      !inSingleQuote &&
      !inDoubleQuote &&
      parenthesesDepth === 0 &&
      bracketDepth === 0 &&
      braceDepth === 0
    ) {
      return index;
    }
  }

  return -1;
};

const startsWithBlockKeyword = (text) => blockKeywords.some((keyword) => new RegExp(`^${keyword}\\b`).test(text.trim()));

const expandInlinePythonStatement = (statement) => {
  const trimmedStatement = statement.trim();
  if (!startsWithBlockKeyword(trimmedStatement)) {
    return [trimmedStatement];
  }

  const colonIndex = findTopLevelColonIndex(trimmedStatement);
  if (colonIndex === -1 || colonIndex === trimmedStatement.length - 1) {
    return [trimmedStatement];
  }

  const head = trimmedStatement.slice(0, colonIndex + 1).trimEnd();
  const tail = trimmedStatement.slice(colonIndex + 1).trim();

  if (!tail) {
    return [head];
  }

  return [head, ...splitTopLevelStatements(tail).flatMap(expandInlinePythonStatement), inlineBlockEndToken];
};

const extractQuestionSuffix = (text) => {
  const patterns = [
    /(.*?)(\s+会输出吗？)$/u,
    /(.*?)(\s+最后输出？)$/u,
    /(.*?)(\s+输出？)$/u,
    /(.*?)(\s+执行后.+)$/u,
    /(.*?)(\s+的结果是？)$/u,
    /(.*?)(\s+的值是？)$/u,
    /(.*?)(\s+外部访问.+？)$/u,
  ];

  for (const pattern of patterns) {
    const match = text.match(pattern);
    if (match) {
      return {
        code: match[1].trim(),
        suffix: match[2].trim(),
      };
    }
  }

  return {
    code: text.trim(),
    suffix: '',
  };
};

const looksLikeCodeQuestion = (text) => {
  const normalizedText = text.trim();
  const statementCount = splitTopLevelStatements(normalizedText).length;

  return (
    statementCount > 1 &&
    /^[A-Za-z_({[\-"'0-9]/.test(normalizedText) &&
    /(?:=|print\(|input\(|def\s+\w+|if\s+|for\s+|while\s+|class\s+)/.test(normalizedText)
  );
};

const formatQuizQuestion = (question) => {
  const normalizedQuestion = (question || '').replace(/\r\n/g, '\n').trim();
  if (!normalizedQuestion || !looksLikeCodeQuestion(normalizedQuestion)) {
    return null;
  }

  const { code: codeText, suffix } = extractQuestionSuffix(normalizedQuestion);
  const statements = splitTopLevelStatements(codeText).flatMap(expandInlinePythonStatement);

  let indentLevel = 0;
  const lines = statements.reduce((formattedLines, statement) => {
    if (statement === inlineBlockEndToken) {
      indentLevel = Math.max(indentLevel - 1, 0);
      return formattedLines;
    }

    const trimmedStatement = statement.trim();
    const keyword = trimmedStatement.split(/\s+/)[0];

    if (dedentKeywords.has(keyword)) {
      indentLevel = Math.max(indentLevel - 1, 0);
    }

    const line = `${'    '.repeat(indentLevel)}${trimmedStatement}`;
    if (startsWithBlockKeyword(trimmedStatement) && trimmedStatement.endsWith(':')) {
      indentLevel += 1;
    }

    formattedLines.push(line);
    return formattedLines;
  }, []);

  return {
    code: lines.join('\n'),
    suffix,
  };
};

const LessonDetail = () => {
  const { user } = useAuth();
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
        if (!user?.id) return;
        const response = await getLessonDetail(user.id, id);
        setLesson(response);
        if (response.user_progress?.is_completed) {
          setQuizResult({
            passed: true,
            score: response.user_progress.score,
            message: '您已完成本节课。',
          });
        }
      } catch (error) {
        console.error('Failed to fetch lesson:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchLesson();
    setQuizAnswers({});
    setQuizResult(null);
  }, [id, user?.id]);

  const handleQuizSubmit = async () => {
    if (!lesson?.quizzes) return;

    if (Object.keys(quizAnswers).length < lesson.quizzes.length) {
      alert('请回答所有问题后再提交。');
      return;
    }

    setSubmitting(true);
    try {
      const response = await submitLessonQuiz(user.id, id, quizAnswers);
      setQuizResult(response);
    } catch (error) {
      console.error('Failed to submit quiz:', error);
      alert('提交失败，请重试。');
    } finally {
      setSubmitting(false);
    }
  };

  const handleNextLesson = () => {
    if (lesson?.next_lesson_id) {
      navigate(`/lessons/${lesson.next_lesson_id}`);
    } else if (lesson?.course_id) {
      navigate(`/courses/${lesson.course_id}`);
    }
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

  if (loading) return <div className="loading-panel">课时内容加载中...</div>;
  if (!lesson) return <div className="empty-panel">未找到该课时。</div>;

  const hasQuiz = Boolean(lesson.quizzes && lesson.quizzes.length > 0);
  const canGoNext = !hasQuiz || Boolean(quizResult);
  const renderNavigationActions = () => (
    <div className={styles.navActions}>
      <button
        type="button"
        onClick={() => lesson.prev_lesson_id && navigate(`/lessons/${lesson.prev_lesson_id}`)}
        disabled={!lesson.prev_lesson_id}
        className="secondary-button"
      >
        上一节
      </button>

      <button
        type="button"
        onClick={handleNextLesson}
        disabled={!canGoNext}
        className="primary-button"
      >
        {lesson.next_lesson_id ? '下一节' : '完成本章'}
        <CheckCircle size={18} />
      </button>

      {!canGoNext && (
        <div className={styles.lockHint}>请先提交测验，再进入下一节。</div>
      )}
    </div>
  );

  return (
    <div className="page-shell">
      <section className={`page-hero ${styles.hero}`}>
        <div className={styles.heroLead}>
          <div className={styles.heroTopRow}>
            <button onClick={() => navigate(-1)} className={styles.backButton}>
              <ArrowLeft size={18} />
              返回上一页
            </button>
            <span className="eyebrow">{getLessonTypeText(lesson.lesson_type)}</span>
          </div>
          <h1 className={`hero-title ${styles.lessonTitle}`}>{lesson.title}</h1>
        </div>

        <div className={styles.heroMeta}>
          <span className="chip">课时类型 {getLessonTypeText(lesson.lesson_type)}</span>
          {lesson.user_progress?.is_completed && <span className="chip">已完成</span>}
        </div>
      </section>

      <section className="page-grid-two">
        <div className={styles.mainColumn}>
          <article className={`${styles.contentCard} surface-card`}>
            {lesson.lesson_type === 'video' && lesson.video_url && (
              <div className={styles.videoContainer}>
                <PlayCircle size={72} className={styles.videoIcon} />
                <p>视频地址：{lesson.video_url}</p>
              </div>
            )}

            {lesson.content && (
              <div className={styles.markdownContent}>
                <ReactMarkdown
                  children={lesson.content}
                  remarkPlugins={[remarkGfm]}
                  components={{
                    code({ inline, className, children, ...props }) {
                      return inline ? (
                        <code {...props} className={className}>
                          {children}
                        </code>
                      ) : (
                        <pre>
                          <code {...props} className={className}>
                            {children}
                          </code>
                        </pre>
                      );
                    },
                  }}
                />
              </div>
            )}
          </article>

          {(lesson.lesson_type === 'text' || lesson.lesson_type === 'code') && (
            <section className={`${styles.practiceCard} surface-card`}>
              <h2 className="section-title">动手试一试</h2>
              <p className="section-subtitle">在当前课时里直接写代码验证思路，而不是只停留在阅读层面。</p>
              <div className={styles.runnerWrap}>
                <CodeRunner
                  initialCode={lesson.code_challenge_prompt || `# ${lesson.title}\nprint('Hello, Python!')`}
                />
              </div>
            </section>
          )}

          {lesson.quizzes && lesson.quizzes.length > 0 && (
            <section className={`${styles.quizCard} surface-card`}>
              <div className={styles.quizHeader}>
                <div>
                  <h2 className="section-title">随堂小测</h2>
                  <p className="section-subtitle">完成所有题目后提交，系统会立即显示结果和题目解析。</p>
                </div>
                {quizResult?.passed && <span className={styles.quizPassed}>已通过 · {quizResult.score} 分</span>}
              </div>

              <div className={styles.quizList}>
                {lesson.quizzes.map((quiz, qIdx) => {
                  const isSubmitted = Boolean(quizResult);
                  const formattedQuestion = formatQuizQuestion(quiz.question);
                  return (
                    <div key={quiz.id} className={styles.quizItem}>
                      <div className={styles.quizQuestion}>
                        <span className={styles.quizQuestionNumber}>Q{qIdx + 1}.</span>
                        {formattedQuestion ? (
                          <div className={styles.quizQuestionBody}>
                            <pre className={styles.quizQuestionCode}>{formattedQuestion.code}</pre>
                            {formattedQuestion.suffix && <span className={styles.quizQuestionSuffix}>{formattedQuestion.suffix}</span>}
                          </div>
                        ) : (
                          <span>{quiz.question}</span>
                        )}
                      </div>
                      <div className={styles.quizOptions}>
                        {[
                          { key: 'A', text: quiz.option_a },
                          { key: 'B', text: quiz.option_b },
                          { key: 'C', text: quiz.option_c },
                          { key: 'D', text: quiz.option_d },
                        ].map((option) => (
                          <button
                            key={option.key}
                            type="button"
                            disabled={isSubmitted}
                            className={`${styles.quizOption} ${getOptionClass(quiz, option.key, isSubmitted)}`}
                            onClick={() => {
                              if (isSubmitted) return;
                              setQuizAnswers((prev) => ({ ...prev, [quiz.id]: option.key }));
                            }}
                          >
                            <span className={styles.optionMarker}>{option.key}</span>
                            <span className={styles.optionText}>{option.text}</span>
                            {isSubmitted && option.key === quiz.correct_answer && (
                              <span className={styles.answerBadge}>正确答案</span>
                            )}
                          </button>
                        ))}
                      </div>

                      {quizResult && (
                        <div className={styles.explanation}>
                          <strong>解析</strong>
                          <p>{quiz.explanation}</p>
                        </div>
                      )}
                    </div>
                  );
                })}
              </div>

              <div className={styles.quizFooter}>
                <div className={styles.quizMessage}>
                  {quizResult?.passed && '恭喜，你已经掌握本节内容。'}
                  {quizResult && !quizResult.passed && (quizResult.message || `得分 ${quizResult.score}，请重试。`)}
                  {!quizResult && '完成全部题目后再提交。'}
                </div>

                {!quizResult?.passed && (
                  <button
                    type="button"
                    onClick={() => {
                      if (quizResult && !quizResult.passed) {
                        setQuizResult(null);
                      } else {
                        handleQuizSubmit();
                      }
                    }}
                    disabled={submitting}
                    className="primary-button"
                  >
                    {submitting ? '提交中...' : quizResult && !quizResult.passed ? '重新作答' : '提交答案'}
                  </button>
                )}
              </div>
            </section>
          )}

          <section className={`${styles.inlineNavCard} surface-card`}>
            <div className={styles.inlineNavHeader}>
              <h2 className="section-title">章节切换</h2>
              <p className="section-subtitle">答题完成后可直接在这里切换上一节或下一节。</p>
            </div>
            {renderNavigationActions()}
          </section>
        </div>

        <aside className={styles.sideColumn}>
          <div className={`${styles.navCard} surface-card`}>
            <h2 className="section-title">学习导航</h2>
            <p className="section-subtitle">可随时回到上一节；测验提交后可直接进入下一节。</p>
            {renderNavigationActions()}
          </div>
        </aside>
      </section>
    </div>
  );
};

export default LessonDetail;
