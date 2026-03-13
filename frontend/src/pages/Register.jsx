import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { ArrowRight, BadgeCheck, ShieldCheck } from 'lucide-react';
import { useAuth } from '../contexts/AuthContext';
import styles from './Register.module.css';

const Register = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);
  const { register } = useAuth();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');
    setLoading(true);
    try {
      await register(username, email, password);
      navigate('/');
    } catch (err) {
      console.error('Register error:', err);
      setError('注册失败，请稍后重试');
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
            <div className={styles.logoSubtitle}>Create your learning profile</div>
          </div>
        </div>

        <div className={styles.heroCopy}>
          <span className="eyebrow">Get Started</span>
          <h1>创建一个轻量、清爽、专注学习进度的 Python 账号。</h1>
          <p>注册后即可进入课程中心，按章节解锁内容、积累经验值，并在练习区即时运行代码。</p>
        </div>

        <div className={styles.featureList}>
          <div className={styles.featureCard}>
            <BadgeCheck size={18} />
            <span>持续记录学习进展</span>
          </div>
          <div className={styles.featureCard}>
            <ShieldCheck size={18} />
            <span>统一账号与课程权限</span>
          </div>
        </div>
      </section>

      <section className={styles.panel}>
        <div className={styles.formCard}>
          <div className={styles.formHeader}>
            <span className="eyebrow">New Account</span>
            <h2>创建账号</h2>
            <p>只需几步，开始你的 Python 学习路线。</p>
          </div>

          {error && <div className={styles.error}>{error}</div>}

          <form className={styles.form} onSubmit={handleSubmit}>
            <div className={styles.field}>
              <label htmlFor="username" className={styles.label}>用户名</label>
              <input
                id="username"
                type="text"
                className={styles.input}
                placeholder="设置你的用户名"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                required
              />
            </div>

            <div className={styles.field}>
              <label htmlFor="email" className={styles.label}>邮箱</label>
              <input
                id="email"
                type="email"
                className={styles.input}
                placeholder="name@example.com"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>

            <div className={styles.field}>
              <label htmlFor="password" className={styles.label}>密码</label>
              <input
                id="password"
                type="password"
                className={styles.input}
                placeholder="创建安全密码"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
              />
            </div>

            <button type="submit" className={styles.submitButton} disabled={loading}>
              {loading ? '注册中...' : '创建并进入平台'}
              {!loading && <ArrowRight size={18} />}
            </button>
          </form>

          <p className={styles.footer}>
            已有账号？
            <Link to="/login" className={styles.link}> 直接登录</Link>
          </p>
        </div>
      </section>
    </div>
  );
};

export default Register;
