import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Play, Code, Star, Lock } from 'lucide-react';
import { motion } from 'framer-motion';
import api from '../api/axios';

const HomePage = () => {
  const [currentCourse, setCurrentCourse] = useState(null);
  const [currentLesson, setCurrentLesson] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchProgress = async () => {
      try {
        const response = await api.get('courses/');
        const courses = response.data;
        
        // Find the first unlocked but not fully completed course
        // Or the last accessed course (not implemented in backend yet, so we infer)
        // Simple logic: Find the first unlocked course that is not 100% complete
        // Since we don't have percentage in list API, we'll pick the first unlocked one for now
        // A better API would be 'current_progress' endpoint.
        
        // For now, let's just pick the first unlocked course
        const activeCourse = courses.find(c => !c.is_locked) || courses[0];
        
        if (activeCourse) {
            // Fetch course details to find current lesson
            const detailRes = await api.get(`courses/${activeCourse.id}/`);
            const courseDetail = detailRes.data;
            setCurrentCourse(courseDetail);
            
            // Find first uncompleted lesson
            let foundLesson = null;
            let totalLessons = 0;
            let completedLessons = 0;

            if (courseDetail.chapters) {
                for (const chapter of courseDetail.chapters) {
                    if (chapter.lessons) {
                        for (const lesson of chapter.lessons) {
                            totalLessons++;
                            if (lesson.is_completed) {
                                completedLessons++;
                            } else if (!foundLesson && !lesson.is_locked) {
                                foundLesson = lesson;
                            }
                        }
                    }
                }
            }
            
            // If all completed, maybe point to the last one or just say done
            setCurrentLesson(foundLesson);
            courseDetail.progress = totalLessons > 0 ? Math.round((completedLessons / totalLessons) * 100) : 0;
        }

      } catch (error) {
        console.error("Failed to fetch progress:", error);
      } finally {
        setLoading(false);
      }
    };
    fetchProgress();
  }, []);

  return (
    <div className="space-y-8">
      {/* Hero Section */}
      <section className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-blue-600 to-indigo-600 p-8 md:p-12 shadow-2xl">
        <div className="relative z-10 max-w-2xl">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.5 }}
          >
            <h1 className="text-4xl md:text-5xl font-bold font-display mb-4 text-white">
              欢迎归队, 见习学员! 🚀
            </h1>
            <p className="text-blue-100 text-lg mb-8">
              你的任务：掌握 Python 语言，解锁数字宇宙的奥秘。
              立即开始你的训练模块。
            </p>
            <Link 
              to="/courses"
              className="inline-flex items-center gap-2 bg-white text-blue-600 font-bold py-3 px-8 rounded-xl hover:bg-blue-50 transition-transform hover:scale-105 shadow-lg"
            >
              <Play size={20} fill="currentColor" />
              开始任务
            </Link>
          </motion.div>
        </div>
        
        {/* Decorative Code Snippet */}
        <div className="absolute right-0 top-1/2 -translate-y-1/2 translate-x-1/4 opacity-20 rotate-12 pointer-events-none hidden md:block">
          <pre className="text-xs md:text-sm font-mono bg-black p-6 rounded-lg text-green-400">
            {`def mission_start():
    print("Initializing...")
    skills = []
    while True:
        learn()
        skills.append("Python")
        if "Python" in skills:
            print("Mission Complete!")
            break`}
          </pre>
        </div>
      </section>

      {/* Stats / Progress */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 shadow-lg">
          <div className="flex items-center gap-4 mb-2">
            <div className="p-3 bg-blue-500/20 text-blue-400 rounded-lg">
              <Code size={24} />
            </div>
            <h3 className="text-lg font-bold text-slate-200">经验值 (XP)</h3>
          </div>
          <p className="text-3xl font-display font-bold text-white">1,250 <span className="text-sm text-slate-500 font-sans font-normal">/ 5,000</span></p>
          <div className="w-full bg-slate-700 h-2 rounded-full mt-4 overflow-hidden">
            <div className="bg-blue-500 h-full w-1/4 rounded-full"></div>
          </div>
        </div>

        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 shadow-lg">
          <div className="flex items-center gap-4 mb-2">
            <div className="p-3 bg-yellow-500/20 text-yellow-400 rounded-lg">
              <Star size={24} />
            </div>
            <h3 className="text-lg font-bold text-slate-200">获得勋章</h3>
          </div>
          <div className="flex gap-2 mt-2">
            <div className="w-10 h-10 rounded-full bg-slate-700 border border-slate-600 flex items-center justify-center text-xl" title="First Code">🥉</div>
            <div className="w-10 h-10 rounded-full bg-slate-700 border border-slate-600 flex items-center justify-center text-xl grayscale opacity-50" title="Loop Master">🥈</div>
            <div className="w-10 h-10 rounded-full bg-slate-700 border border-slate-600 flex items-center justify-center text-xl grayscale opacity-50" title="Function Wizard">🥇</div>
          </div>
        </div>

        <div className="bg-slate-800 p-6 rounded-xl border border-slate-700 shadow-lg">
          <div className="flex items-center gap-4 mb-2">
            <div className="p-3 bg-purple-500/20 text-purple-400 rounded-lg">
              <Lock size={24} />
            </div>
            <h3 className="text-lg font-bold text-slate-200">待解锁</h3>
          </div>
          <p className="text-xl font-medium text-white mt-1">进阶循环</p>
          <p className="text-sm text-slate-400 mt-1">完成 "While 循环" 以解锁。</p>
        </div>
      </div>

      {/* Quick Access to Current Course */}
      <section>
        <h2 className="text-2xl font-bold font-display text-white mb-6">当前目标</h2>
        {currentCourse ? (
            <Link to={currentLesson ? `/lessons/${currentLesson.id}` : `/courses/${currentCourse.id}`} className="block bg-slate-800 rounded-xl border border-slate-700 overflow-hidden flex flex-col md:flex-row hover:border-blue-500/50 transition-colors group cursor-pointer">
              <div className="bg-slate-700 w-full md:w-48 h-32 md:h-auto flex items-center justify-center text-6xl">
                🐍
              </div>
              <div className="p-6 flex-1">
                <div className="flex justify-between items-start mb-2">
                  <span className="bg-green-500/20 text-green-400 text-xs font-bold px-2 py-1 rounded uppercase tracking-wider">进行中</span>
                  <span className="text-slate-400 text-sm">第 {currentCourse.order} 章</span>
                </div>
                <h3 className="text-xl font-bold text-white mb-2 group-hover:text-blue-400 transition-colors">
                    {currentLesson ? `继续学习：${currentLesson.title}` : currentCourse.title}
                </h3>
                <p className="text-slate-400 mb-4">{currentCourse.description}</p>
                <div className="flex items-center gap-4">
                  <div className="flex-1 bg-slate-700 h-2 rounded-full overflow-hidden">
                    <div className="bg-green-500 h-full rounded-full" style={{ width: `${currentCourse.progress}%` }}></div>
                  </div>
                  <span className="text-sm font-bold text-white">{currentCourse.progress}%</span>
                </div>
              </div>
            </Link>
        ) : (
            <div className="text-slate-400 bg-slate-800 p-6 rounded-xl border border-slate-700">
                暂无进行中的课程，去<Link to="/courses" className="text-blue-400 hover:underline">课程列表</Link>看看吧！
            </div>
        )}
      </section>
    </div>
  );
};

export default HomePage;
