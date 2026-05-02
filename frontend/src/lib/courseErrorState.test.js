import test from 'node:test';
import assert from 'node:assert/strict';

import { resolveCourseDetailErrorMessage } from './courseErrorState.js';

// --- 课程错误状态测试 ---

test('401 错误应提示先登录', () => {
  const message = resolveCourseDetailErrorMessage({ status: 401, message: 'Unauthorized' });
  assert.equal(message, '请先登录后再查看该课程。');
});

test('403 错误应提示无权限访问', () => {
  const message = resolveCourseDetailErrorMessage({ status: 403, message: 'Forbidden' });
  assert.equal(message, '你当前无权访问该课程。');
});

test('404 错误应提示课程不存在', () => {
  const message = resolveCourseDetailErrorMessage({ status: 404, message: 'Not found' });
  assert.equal(message, '未找到该课程。');
});

test('其他接口异常应提示稍后重试', () => {
  const message = resolveCourseDetailErrorMessage({ status: 500, message: 'Server error' });
  assert.equal(message, '课程详情加载失败，请稍后重试。');
});

test('无 error 对象应返回默认提示', () => {
  const message = resolveCourseDetailErrorMessage(null);
  assert.equal(message, '课程详情加载失败，请稍后重试。');
});

// --- 考试分数计算逻辑测试 ---

test('考试通过判断：分数 >= 及格线', () => {
  const passingScore = 60;
  const totalScore = 100;
  const threshold = totalScore * passingScore / 100;

  assert.equal(threshold, 60);
  assert.equal(50 >= threshold, false);
  assert.equal(60 >= threshold, true);
  assert.equal(80 >= threshold, true);
});

test('多选题答案标准化比较', () => {
  // 模拟后端排序后比较逻辑
  function checkAnswer(selected, correct) {
    return selected.split('').sort().join('') === correct.split('').sort().join('');
  }

  assert.equal(checkAnswer('AB', 'BA'), true);
  assert.equal(checkAnswer('AB', 'AB'), true);
  assert.equal(checkAnswer('ABC', 'CBA'), true);
  assert.equal(checkAnswer('A', 'AB'), false);
  assert.equal(checkAnswer('', ''), true);
});

test('单选题答案比较（大小写不敏感）', () => {
  function checkAnswer(selected, correct) {
    return selected.trim().toUpperCase() === correct.trim().toUpperCase();
  }

  assert.equal(checkAnswer('a', 'A'), true);
  assert.equal(checkAnswer('B', 'B'), true);
  assert.equal(checkAnswer('c', 'A'), false);
  assert.equal(checkAnswer('', 'A'), false);
});

// --- 考试进度计算 ---

test('答题进度百分比计算', () => {
  function calcProgress(answered, total) {
    if (total === 0) return 0;
    return Math.round((answered / total) * 100);
  }

  assert.equal(calcProgress(0, 10), 0);
  assert.equal(calcProgress(5, 10), 50);
  assert.equal(calcProgress(10, 10), 100);
  assert.equal(calcProgress(7, 10), 70);
  assert.equal(calcProgress(0, 0), 0);
});
