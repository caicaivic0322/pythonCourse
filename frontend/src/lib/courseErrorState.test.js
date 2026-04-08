import test from 'node:test';
import assert from 'node:assert/strict';

import { resolveCourseDetailErrorMessage } from './courseErrorState.js';

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
