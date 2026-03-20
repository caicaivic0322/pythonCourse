import api from '../api/axios';

const sessionKey = 'pymaster_auth';

function readSession() {
  const raw = localStorage.getItem(sessionKey);
  return raw ? JSON.parse(raw) : null;
}

function writeSession(session) {
  localStorage.setItem(sessionKey, JSON.stringify(session));
}

function clearStoredSession() {
  localStorage.removeItem(sessionKey);
  localStorage.removeItem('token');
}

function normalizeUser(user) {
  if (!user) return null;
  return {
    ...user,
    user_id: user.user_id || user.id,
  };
}

function getErrorMessage(error, fallback) {
  return (
    error?.response?.data?.detail ||
    error?.response?.data?.username?.[0] ||
    error?.response?.data?.email?.[0] ||
    error?.response?.data?.password?.[0] ||
    error?.message ||
    fallback
  );
}

export async function loginWithUsernameOrEmail(identifier, password) {
  try {
    const { data } = await api.post('users/login/', {
      username: identifier,
      password,
    });

    localStorage.setItem('token', data.token);

    const meResponse = await api.get('users/me/');
    const user = normalizeUser(meResponse.data);

    writeSession({
      token: data.token,
      user,
    });

    return { token: data.token, user };
  } catch (error) {
    throw new Error(getErrorMessage(error, '用户名或密码错误'));
  }
}

export async function registerUser(username, email, password) {
  try {
    await api.post('users/register/', {
      username,
      email,
      password,
    });
  } catch (error) {
    throw new Error(getErrorMessage(error, '注册失败，请稍后重试'));
  }

  return loginWithUsernameOrEmail(username, password);
}

export async function getCurrentUserData() {
  const token = localStorage.getItem('token');
  if (!token) return null;

  try {
    const { data } = await api.get('users/me/');
    const user = normalizeUser(data);
    writeSession({ token, user });
    return user;
  } catch {
    clearStoredSession();
    return null;
  }
}

export async function signOut() {
  clearStoredSession();
}

export async function getUserStats() {
  try {
    const { data } = await api.get('users/stats/');
    return data;
  } catch (error) {
    throw new Error(getErrorMessage(error, '获取学习统计失败'));
  }
}

export async function getCourses() {
  try {
    const { data } = await api.get('courses/');
    return data;
  } catch (error) {
    throw new Error(getErrorMessage(error, '获取课程列表失败'));
  }
}

export async function getCourseDetail(_userId, courseId) {
  try {
    const { data } = await api.get(`courses/${courseId}/`);
    return data;
  } catch (error) {
    throw new Error(getErrorMessage(error, '获取课程详情失败'));
  }
}

export async function getLessonDetail(_userId, lessonId) {
  try {
    const { data } = await api.get(`courses/lessons/${lessonId}/`);
    return data;
  } catch (error) {
    throw new Error(getErrorMessage(error, '获取课时内容失败'));
  }
}

export async function submitLessonQuiz(_userId, lessonId, quizAnswers) {
  try {
    const { data } = await api.post(`courses/lessons/${lessonId}/complete/`, {
      quiz_answers: quizAnswers,
    });
    return data;
  } catch (error) {
    throw new Error(getErrorMessage(error, '提交测验失败'));
  }
}

export async function getPublishedExams() {
  return [];
}

export async function getExamDetail() {
  return null;
}

export async function submitExamAttempt() {
  throw new Error('考试中心暂未接入当前 Django 后端');
}

export function getStoredUser() {
  return normalizeUser(readSession()?.user);
}
