import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { ArrowRight, BookOpenCheck, Sparkles } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import styles from './Login.module.css';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { login } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      await login(username, password);
      navigate('/');
    } catch (err) {
      console.error('Login error:', err);
      setError('用户名或密码错误');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className={styles.shell}>
      <section className={styles.showcase}>
        <div className={styles.brand}>
          <div className={styles.logoIcon}>Py</div>
          <div>
            <div className={styles.logoText}>PyMaster</div>
            <div className={styles.logoSubtitle}>Modern Python Learning Hub</div>
          </div>
        </div>

        <div className={styles.heroCopy}>
          <span className="eyebrow">Python Learning</span>
          <h1>把课程、练习和测验收进一个更清晰的学习空间。</h1>
          <p>
            登录后直接回到你的学习总览，继续课程、查看成长进度，并在代码练习区马上开始动手。
          </p>
        </div>

        <div className={styles.featureList}>
          <div className={styles.featureCard}>
            <BookOpenCheck size={18} />
            <span>阶段式课程路径</span>
          </div>
          <div className={styles.featureCard}>
            <Sparkles size={18} />
            <span>练习与测验一体化</span>
          </div>
        </div>
      </section>

      <section className={styles.panel}>
        <div className={styles.formCard}>
          <div className={styles.formHeader}>
            <span className="eyebrow">Welcome Back</span>
            <h2>登录账号</h2>
            <p>继续你上一次的学习进度。</p>
          </div>

          {error && <div className={styles.error}>{error}</div>}

          <form className={styles.form} onSubmit={handleSubmit}>
            <div className={styles.field}>
              <label htmlFor="username" className={styles.label}>用户名</label>
              <input
                id="username"
                type="text"
                className={styles.input}
                placeholder="例如 py_learner"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>

            <div className={styles.field}>
              <label htmlFor="password" className={styles.label}>密码</label>
              <input
                id="password"
                type="password"
                className={styles.input}
                placeholder="输入你的密码"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>

            <button type="submit" className={styles.submitButton} disabled={loading}>
              {loading ? '登录中...' : '进入学习空间'}
              {!loading && <ArrowRight size={18} />}
            </button>
          </form>

          <p className={styles.footer}>
            还没有账号？
            <Link to="/register" className={styles.link}> 创建新账号</Link>
          </p>
        </div>
      </section>
    </div>
  );
};

export default Login;
