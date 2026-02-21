import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import api from '../api/axios';
import CodeRunner from '../components/CodeRunner';
import { ArrowLeft, CheckCircle, PlayCircle, FileText } from 'lucide-react';
import ReactMarkdown from 'react-markdown';
import remarkGfm from 'remark-gfm';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { atomDark } from 'react-syntax-highlighter/dist/esm/styles/prism';

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
        // 如果已经通过，直接显示状态
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
      
      // 检查是否所有题目都已作答
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
          
          if (!response.data.passed) {
             // 错题反馈：提示用户哪些题做错了
             // 由于后端目前只返回总分，我们暂时只能提示用户重试。
             // 如果需要更详细的反馈（如哪题错了），需要后端支持。
             // 暂时前端简单实现：显示一个 Alert 提示正确答案（仅供演示，实际应后端返回）
             // 更好的做法是：提交后，将正确答案高亮显示出来。
             
             // 为了用户体验，我们虽然不能从 API 拿到详细的对错列表（除非修改后端），
             // 但我们可以在这里手动把正确答案高亮出来，因为我们还没刷新页面，
             // 实际上前端并不知道正确答案是什么（正确答案在后端校验）。
             // 
             // 所以，我们修改后端返回的数据结构，让其返回正确答案列表，或者直接在前端显示“解析”。
             // 但这需要改后端。
             // 
             // 既然用户要求“及时提醒正确答案”，我们可以修改 MarkLessonCompleteView 返回详细的错题信息。
             // 现在先做个简单的：如果没过，提示看解析。
             
             // 为了快速满足需求，我们可以把 Explanation 提前下发给前端（目前已经在 lesson.quizzes 里了），
             // 只是之前只有点对了才弹。
             // 现在提交后，如果没过，我们可以把所有题目的解析展示出来，或者标记出错题。
             
             // 方案：提交后，强制显示所有题目的解析和正确答案。
          }
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

  if (loading) return <div className="text-white p-8">加载课程数据中...</div>;
  if (!lesson) return <div className="text-white p-8">未找到该课程。</div>;

  return (
    <div className="text-white max-w-4xl mx-auto space-y-8 pb-12">
      {/* Header */}
      <div className="flex items-center gap-4 mb-6">
        <button 
          onClick={() => navigate(-1)} 
          className="p-2 bg-slate-800 rounded-lg hover:bg-slate-700 transition-colors text-slate-400 hover:text-white"
        >
          <ArrowLeft size={20} />
        </button>
        <div>
          <span className="text-sm text-blue-400 font-bold uppercase tracking-wider">
            {lesson.lesson_type === 'code' ? '代码挑战' : 
             lesson.lesson_type === 'video' ? '视频课程' : 
             lesson.lesson_type === 'quiz' ? '测验' : '图文课程'}
          </span>
          <h1 className="text-3xl font-bold font-display">{lesson.title}</h1>
        </div>
      </div>

      {/* Content Area */}
      <div className="bg-slate-800 rounded-xl border border-slate-700 p-8 shadow-xl">
        {lesson.lesson_type === 'video' && lesson.video_url && (
          <div className="aspect-video bg-black rounded-lg mb-6 flex items-center justify-center relative overflow-hidden group cursor-pointer">
             {/* Placeholder for actual video player */}
             <div className="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex items-end p-6">
                <p className="text-white font-medium">视频播放器占位符: {lesson.video_url}</p>
             </div>
             <PlayCircle size={64} className="text-white opacity-80 group-hover:opacity-100 group-hover:scale-110 transition-all" />
          </div>
        )}

        {lesson.content && (
          <div className="prose prose-invert max-w-none mb-8">
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

        {/* 始终显示代码编辑器 */}
        {(lesson.lesson_type === 'text' || lesson.lesson_type === 'code') && (
          <div className="mt-8 border-t border-slate-700 pt-8">
            <h3 className="text-xl font-bold mb-4 flex items-center gap-2">
              <span className="text-green-400">⚡</span> 动手试一试
            </h3>
            <p className="text-slate-400 text-sm mb-4">
                光看不练假把式，快在下方编写代码验证你的想法吧！
            </p>
            <CodeRunner initialCode={lesson.code_challenge_prompt || `# ${lesson.title} - 练习区
# 请在下方编写你的代码
print('Hello, Python!')`} />
          </div>
        )}

        {/* 随堂测验区域 */}
        {lesson.quizzes && lesson.quizzes.length > 0 && (
            <div className="mt-12 bg-slate-700/30 p-6 rounded-xl border border-slate-700">
                <div className="flex items-center justify-between mb-6">
                    <h3 className="text-xl font-bold flex items-center gap-2 text-yellow-400">
                        <span className="text-2xl">📝</span> 随堂小测
                    </h3>
                    {quizResult && quizResult.passed && (
                        <div className="bg-green-500/20 text-green-400 px-3 py-1 rounded-full text-sm font-bold border border-green-500/50">
                            已通过 (得分: {quizResult.score})
                        </div>
                    )}
                </div>
                
                <div className="space-y-8">
                    {lesson.quizzes.map((quiz, qIdx) => (
                        <div key={quiz.id} className="space-y-4">
                            <p className="text-lg font-medium">
                                <span className="text-slate-400 mr-2">Q{qIdx + 1}.</span>
                                {quiz.question}
                            </p>
                            
                            <div className="space-y-2">
                                {[
                                    { key: 'A', text: quiz.option_a },
                                    { key: 'B', text: quiz.option_b },
                                    { key: 'C', text: quiz.option_c },
                                    { key: 'D', text: quiz.option_d }
                                ].map((option) => {
                                    const isSelected = quizAnswers[quiz.id] === option.key;
                                    const isSubmitted = !!quizResult;
                                    const isCorrect = option.key === quiz.correct_answer;
                                    
                                    // 样式逻辑
                                    let btnClass = "bg-slate-800 border-transparent hover:border-blue-500/50";
                                    
                                    // 提交后的状态显示
                                    if (isSubmitted) {
                                        if (isCorrect) {
                                            // 正确答案总是显示绿色
                                            btnClass = "bg-green-900/30 border-green-500 text-green-100";
                                        } else if (isSelected && !isCorrect) {
                                            // 选错了显示红色
                                            btnClass = "bg-red-900/30 border-red-500 text-red-100";
                                        } else {
                                            // 其他未选选项变暗
                                            btnClass = "bg-slate-800/50 border-transparent opacity-50";
                                        }
                                    } else if (isSelected) {
                                        // 提交前的选中状态
                                        btnClass = "bg-blue-600/30 border-blue-500 text-white";
                                    }
                                    
                                    return (
                                        <button 
                                            key={option.key}
                                            disabled={isSubmitted} // 提交后暂时禁用，只有点击重试（如果没过）才解开
                                            className={`w-full text-left p-4 rounded-lg transition-all border flex items-center gap-3 group ${btnClass} ${!isSubmitted ? 'hover:bg-slate-600' : 'cursor-default'}`}
                                            onClick={() => {
                                                if (isSubmitted) return;
                                                setQuizAnswers(prev => ({
                                                    ...prev,
                                                    [quiz.id]: option.key
                                                }));
                                            }}
                                        >
                                            <span className={`w-6 h-6 rounded-full flex items-center justify-center text-xs font-bold transition-colors ${
                                                isSubmitted && isCorrect ? 'bg-green-500 text-white' :
                                                isSubmitted && isSelected && !isCorrect ? 'bg-red-500 text-white' :
                                                isSelected ? 'bg-blue-500 text-white' : 'bg-slate-700 text-slate-400'
                                            }`}>
                                                {option.key}
                                            </span>
                                            {option.text}
                                            {isSubmitted && isCorrect && <span className="ml-auto text-green-400 text-sm font-bold">正确答案</span>}
                                            {isSubmitted && isSelected && !isCorrect && <span className="ml-auto text-red-400 text-sm font-bold">错误</span>}
                                        </button>
                                    );
                                })}
                            </div>
                            
                            {/* 解析区域 - 仅在提交后显示 */}
                            {quizResult && (
                                <div className={`mt-2 p-4 rounded-lg text-sm border ${quizAnswers[quiz.id] === quiz.correct_answer ? 'bg-green-900/20 border-green-900/50 text-green-200' : 'bg-red-900/20 border-red-900/50 text-red-200'}`}>
                                    <p className="font-bold mb-1">解析：</p>
                                    <p>{quiz.explanation}</p>
                                </div>
                            )}
                        </div>
                    ))}
                </div>
                
                {/* 提交结果区域 */}
                <div className="mt-8 pt-6 border-t border-slate-600 flex items-center justify-between">
                     <div className="text-sm">
                         {quizResult && !quizResult.passed && (
                             <span className="text-red-400 font-bold">{quizResult.message || `得分 ${quizResult.score}，未达到 50%，请重试！`}</span>
                         )}
                         {quizResult && quizResult.passed && (
                             <span className="text-green-400 font-bold">恭喜！您已掌握本节内容。</span>
                         )}
                         {!quizResult && (
                             <span className="text-slate-400">请完成所有题目后提交。</span>
                         )}
                     </div>
                     
                     {!quizResult?.passed && (
                         <button 
                            onClick={() => {
                                if (quizResult && !quizResult.passed) {
                                    // 如果已提交但未通过，点击重试时重置状态
                                    setQuizResult(null);
                                    // 可以在这里选择是否保留用户的答案，或者清空
                                    // setQuizAnswers({}); // 如果想清空答案
                                } else {
                                    handleQuizSubmit();
                                }
                            }}
                            disabled={submitting}
                            className={`px-6 py-2 rounded-lg font-bold transition-colors disabled:opacity-50 ${quizResult && !quizResult.passed ? 'bg-slate-700 hover:bg-slate-600 text-white' : 'bg-yellow-600 hover:bg-yellow-700 text-white'}`}
                         >
                            {submitting ? '提交中...' : (quizResult && !quizResult.passed ? '重试' : '提交答案')}
                         </button>
                     )}
                </div>
            </div>
        )}
      </div>

      {/* Footer Navigation */}
      <div className="flex justify-between items-center mt-8">
        <button 
            onClick={() => lesson.prev_lesson_id && navigate(`/lessons/${lesson.prev_lesson_id}`)}
            disabled={!lesson.prev_lesson_id}
            className={`px-6 py-3 rounded-lg font-bold transition-colors ${lesson.prev_lesson_id ? 'bg-slate-700 text-slate-300 hover:bg-slate-600' : 'bg-slate-800 text-slate-600 cursor-not-allowed'}`}
        >
            上一节
        </button>
        
        {/* Next Lesson Button - Only show if quiz passed (or no quizzes) */}
        {(!lesson.quizzes || lesson.quizzes.length === 0 || (quizResult && quizResult.passed)) ? (
            <button 
                onClick={handleNextLesson}
                className="px-6 py-3 bg-blue-600 text-white rounded-lg font-bold hover:bg-blue-700 transition-colors flex items-center gap-2 animate-bounce-short"
            >
                {lesson.next_lesson_id ? '下一节' : '完成本章'} <CheckCircle size={18} />
            </button>
        ) : (
            <div className="flex items-center gap-3 px-6 py-3 bg-slate-800 rounded-lg border border-slate-700 text-slate-500 cursor-not-allowed">
                <span className="text-sm">请先通过测验解锁</span>
                <CheckCircle size={18} />
            </div>
        )}
      </div>
    </div>
  );
};

export default LessonDetail;
