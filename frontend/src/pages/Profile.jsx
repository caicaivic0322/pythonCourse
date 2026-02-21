import React from 'react';
import { useAuth } from '../context/AuthContext';
import { User, Mail, Award, Clock } from 'lucide-react';

const Profile = () => {
  const { user } = useAuth();

  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-4xl font-bold font-display text-blue-400 mb-2">个人档案</h1>
        <p className="text-slate-400">查看你的冒险记录与成就。</p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
        {/* Profile Card */}
        <div className="md:col-span-1 bg-slate-800 rounded-xl border border-slate-700 p-6 flex flex-col items-center text-center">
            <div className="w-24 h-24 bg-slate-700 rounded-full flex items-center justify-center mb-4 border-4 border-blue-500/20">
                <span className="text-4xl">🐍</span>
            </div>
            <h2 className="text-2xl font-bold text-white mb-1">{user?.username || 'Python Explorer'}</h2>
            <p className="text-slate-400 text-sm mb-6">Level 1 Pythonista</p>
            
            <div className="w-full space-y-4 text-left">
                <div className="flex items-center gap-3 text-slate-300 p-3 bg-slate-900/50 rounded-lg">
                    <User size={18} className="text-blue-400" />
                    <span className="text-sm">ID: {user?.id || 'Unknown'}</span>
                </div>
                <div className="flex items-center gap-3 text-slate-300 p-3 bg-slate-900/50 rounded-lg">
                    <Mail size={18} className="text-purple-400" />
                    <span className="text-sm">{user?.email || 'No Email'}</span>
                </div>
                <div className="flex items-center gap-3 text-slate-300 p-3 bg-slate-900/50 rounded-lg">
                    <Clock size={18} className="text-green-400" />
                    <span className="text-sm">加入时间: 2023-10-01</span>
                </div>
            </div>
        </div>

        {/* Stats & Achievements */}
        <div className="md:col-span-2 space-y-6">
            {/* Stats */}
            <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
                <div className="bg-slate-800 p-4 rounded-xl border border-slate-700 text-center">
                    <div className="text-3xl font-bold text-yellow-400 mb-1">500</div>
                    <div className="text-xs text-slate-400 uppercase tracking-wider">总 XP</div>
                </div>
                <div className="bg-slate-800 p-4 rounded-xl border border-slate-700 text-center">
                    <div className="text-3xl font-bold text-blue-400 mb-1">4</div>
                    <div className="text-xs text-slate-400 uppercase tracking-wider">完成课程</div>
                </div>
                <div className="bg-slate-800 p-4 rounded-xl border border-slate-700 text-center">
                    <div className="text-3xl font-bold text-green-400 mb-1">12</div>
                    <div className="text-xs text-slate-400 uppercase tracking-wider">代码挑战</div>
                </div>
                <div className="bg-slate-800 p-4 rounded-xl border border-slate-700 text-center">
                    <div className="text-3xl font-bold text-purple-400 mb-1">3</div>
                    <div className="text-xs text-slate-400 uppercase tracking-wider">获得勋章</div>
                </div>
            </div>

            {/* Badges */}
            <div className="bg-slate-800 rounded-xl border border-slate-700 p-6">
                <h3 className="text-xl font-bold text-white mb-4 flex items-center gap-2">
                    <Award className="text-yellow-400" /> 最近获得的勋章
                </h3>
                <div className="grid grid-cols-2 sm:grid-cols-4 gap-4">
                     <div className="bg-slate-900/50 p-4 rounded-lg flex flex-col items-center text-center hover:bg-slate-700 transition-colors cursor-pointer">
                        <div className="text-3xl mb-2">🌱</div>
                        <div className="font-bold text-sm text-slate-200">初出茅庐</div>
                     </div>
                     <div className="bg-slate-900/50 p-4 rounded-lg flex flex-col items-center text-center hover:bg-slate-700 transition-colors cursor-pointer">
                        <div className="text-3xl mb-2">🔥</div>
                        <div className="font-bold text-sm text-slate-200">连续打卡</div>
                     </div>
                     <div className="bg-slate-900/50 p-4 rounded-lg flex flex-col items-center text-center hover:bg-slate-700 transition-colors cursor-pointer">
                        <div className="text-3xl mb-2">🐛</div>
                        <div className="font-bold text-sm text-slate-200">Bug 猎手</div>
                     </div>
                </div>
            </div>
        </div>
      </div>
    </div>
  );
};

export default Profile;