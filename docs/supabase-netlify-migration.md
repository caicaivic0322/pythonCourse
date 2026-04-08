# Supabase + Netlify 迁移指南

## 1. Supabase 初始化

1. 创建 Supabase 项目。
2. 打开 SQL Editor，执行 [20260316_init_pymaster.sql](file:///Users/caizhen/Desktop/Dev/Python_Course/supabase/migrations/20260316_init_pymaster.sql)。
3. 在 Authentication 中开启 Email/Password 登录。

## 2. 数据迁移建议

- 课程数据迁移到 `courses/chapters/lessons/quizzes` 四张表。
- 用户与进度写入 `profiles/user_course_progress/user_lesson_progress`。
- 考试数据写入 `exams`，考试作答记录写入 `exam_attempts`。

## 3. 考试题上传方式

在 Supabase `public.exams` 插入一条记录，关键字段：

- `title`
- `subject`
- `markdown_content`
- `published = true`

触发器会自动解析 `markdown_content`，并写入 `parsed_json`。

## 4. Markdown 模板示例

```md
# C++ 程序设计综合测试卷（Set 2）

考试时间：60分钟
满分：100分

## 单选题

### 1
题目：十进制数 100 转换成二进制数的结果是（　　）
A. 1100100
B. 1101000
C. 1011010
D. 1100010
答案：A
解析：100 的二进制是 1100100

### 2
题目：在 C++ 中，下列数据类型中占用内存最大的是（　　）
A. short
B. long long
C. char
D. long
答案：B
解析：long long 通常占用更多字节
```

## 5. Netlify 配置

本项目前端目录为 `frontend/`，需要在 Netlify 中设置：

- Base directory: `frontend`
- Build command: `npm run build`
- Publish directory: `dist`

并在 Netlify 环境变量中设置：

- `VITE_SUPABASE_URL`
- `VITE_SUPABASE_ANON_KEY`

可参考 [frontend/.env.example](file:///Users/caizhen/Desktop/Dev/Python_Course/frontend/.env.example)。

## 6. 前端关键改造点

- 认证从 Django Token 改为 Supabase Auth。
- 数据访问从 REST API 改为 Supabase JS 客户端查询。
- 新增考试中心页面：
  - [ExamList.jsx](file:///Users/caizhen/Desktop/Dev/Python_Course/frontend/src/pages/ExamList.jsx)
  - [ExamDetail.jsx](file:///Users/caizhen/Desktop/Dev/Python_Course/frontend/src/pages/ExamDetail.jsx)
