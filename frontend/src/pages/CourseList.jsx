import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Lock } from 'lucide-react';
import api from '../api/axios';

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

  if (loading) {
    return <div className="text-white">加载训练模块中...</div>;
  }

  if (courses.length === 0) {
      return <div className="text-white text-center py-12">暂无课程数据，请联系管理员。</div>;
  }

  return (
    <div className="space-y-8">
      <h1 className="text-3xl font-bold font-display text-white">训练模块</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {courses.map((course) => (
          <div key={course.id} className={`bg-slate-800 rounded-xl border border-slate-700 p-6 transition-all ${course.is_locked ? 'opacity-60 cursor-not-allowed' : 'hover:border-blue-500/50 hover:-translate-y-1 cursor-pointer'}`}>
            <div className="h-40 bg-slate-700 rounded-lg mb-4 flex items-center justify-center text-4xl relative">
              {course.is_locked && (
                  <div className="absolute inset-0 bg-slate-900/60 flex items-center justify-center rounded-lg">
                      <Lock size={48} className="text-slate-400" />
                  </div>
              )}
              🐍
            </div>
            <h3 className="text-xl font-bold text-white mb-2">{course.title}</h3>
            <p className="text-slate-400 text-sm mb-4 line-clamp-2">{course.description}</p>
            <button 
              onClick={() => !course.is_locked && navigate(`/courses/${course.id}`)}
              disabled={course.is_locked}
              className={`w-full font-bold py-2 rounded-lg transition-colors ${course.is_locked ? 'bg-slate-700 text-slate-500 cursor-not-allowed' : 'bg-slate-700 hover:bg-blue-600 text-white'}`}
            >
              {course.is_locked ? '未解锁' : '开始任务'}
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CourseList;
