export function resolveCourseDetailErrorMessage(error) {
  if (error?.status === 401) {
    return '请先登录后再查看该课程。';
  }

  if (error?.status === 403) {
    return '你当前无权访问该课程。';
  }

  if (error?.status === 404) {
    return '未找到该课程。';
  }

  return '课程详情加载失败，请稍后重试。';
}
