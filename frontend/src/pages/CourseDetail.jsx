import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Lock, CheckCircle, PlayCircle, FileText } from 'lucide-react';
import api from '../api/axios';
import CodeRunner from '../components/CodeRunner';

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

  if (loading) return <div className="text-white">加载任务数据中...</div>;
  if (!course) return <div className="text-white">未找到该任务。</div>;

  return (
    <div className="text-white max-w-4xl mx-auto space-y-8">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-4xl font-bold font-display text-blue-400 mb-2">{course.title}</h1>
          <p className="text-slate-400">{course.description}</p>
        </div>
        <div className="bg-slate-800 p-4 rounded-xl border border-slate-700">
          <span className="text-sm text-slate-400 block mb-1">XP 奖励</span>
          <span className="text-2xl font-bold text-yellow-400">+500 XP</span>
        </div>
      </div>

      <div className="space-y-6">
        {(!course.chapters || course.chapters.length === 0) && (
            <div className="text-slate-400">该任务暂无章节。</div>
        )}
        {course.chapters && course.chapters.map((chapter) => (
          <div key={chapter.id} className="bg-slate-800 rounded-xl border border-slate-700 overflow-hidden">
            <div className="bg-slate-700/50 p-4 border-b border-slate-700 flex justify-between items-center">
              <h2 className="text-xl font-bold text-white">{chapter.title}</h2>
              <span className="text-xs bg-blue-500/20 text-blue-400 px-2 py-1 rounded">第 {chapter.order} 章</span>
            </div>
            <div className="p-4 space-y-4">
              {(!chapter.lessons || chapter.lessons.length === 0) && (
                  <div className="text-slate-500 italic text-sm">本章暂无课程。</div>
              )}
              {chapter.lessons && chapter.lessons.map((lesson) => (
                <div 
                  key={lesson.id} 
                  onClick={() => !lesson.is_locked && navigate(`/lessons/${lesson.id}`)}
                  className={`flex items-center justify-between bg-slate-900/50 p-4 rounded-lg transition-all cursor-pointer group ${lesson.is_locked ? 'opacity-60 cursor-not-allowed' : 'hover:bg-slate-700'}`}
                >
                  <div className="flex items-center gap-4">
                    <div className={`w-10 h-10 rounded-full flex items-center justify-center text-lg relative ${
                        lesson.is_completed ? 'bg-green-500/20 text-green-400' :
                        lesson.is_locked ? 'bg-slate-800 text-slate-500' : 
                        lesson.lesson_type === 'code' ? 'bg-purple-500/20 text-purple-400' : 'bg-blue-500/20 text-blue-400'
                    }`}>
                      {lesson.is_locked ? <Lock size={18} /> : 
                       lesson.is_completed ? <CheckCircle size={18} /> :
                       lesson.lesson_type === 'code' ? '</>' : 
                       lesson.lesson_type === 'video' ? <PlayCircle size={18} /> : <FileText size={18} />}
                    </div>
                    <div>
                      <h3 className={`font-bold transition-colors ${lesson.is_locked ? 'text-slate-500' : 'text-slate-200 group-hover:text-white'}`}>{lesson.title}</h3>
                      <span className="text-xs text-slate-500 capitalize flex items-center gap-2">
                          {lesson.lesson_type === 'code' ? '代码挑战' : 
                           lesson.lesson_type === 'video' ? '视频课程' : 
                           lesson.lesson_type === 'quiz' ? '测验' : '图文课程'}
                           
                           {lesson.is_completed && <span className="text-green-500 font-bold">已完成</span>}
                      </span>
                    </div>
                  </div>
                  
                  {!lesson.is_locked && (
                      <button className="text-slate-400 hover:text-white group-hover:translate-x-1 transition-all">
                        {lesson.is_completed ? '复习 →' : '开始 →'}
                      </button>
                  )}
                </div>
              ))}
            </div>
          </div>
        ))}
      </div>

      <div className="mt-8">
        <h2 className="text-2xl font-bold font-display text-white mb-4">自由练习区</h2>
        <CodeRunner />
      </div>
    </div>
  );
};

export default CourseDetail;
