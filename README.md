# PyMaster - Python 编程训练营 🐍

PyMaster 是一个现代化的、游戏化的 Python 学习平台，专为初学者和 GESP 考级学生设计。通过互动式课程、实时代码挑战和项目实战，帮助学员掌握 Python 编程技能。

## 🌟 核心功能

- **📚 体系化课程**：覆盖 GESP 1-4 级考级内容，以及《Head First Python》实战项目。
- **💻 互动式代码运行器**：内置基于 Monaco Editor 的代码编辑器，支持在浏览器中编写和运行 Python 代码。
- **📝 随堂测验与挑战**：每节课配备选择题和代码填空挑战，实时反馈学习成果。
- **🔒 闯关解锁机制**：必须通过当前课程/小节的测验才能解锁下一阶段，确保知识掌握。
- **🏆 游戏化激励**：学习过程中获得 XP 经验值和勋章（界面展示），提升学习动力。
- **🚀 实战项目驱动**：包含构建 Web 应用的完整实战课程，强调 "Learning by Doing"。

## 🛠️ 技术栈

### 后端 (Backend)
- **框架**：Django 5.0 + Django REST Framework
- **数据库**：SQLite (开发环境)
- **特性**：
  - RESTful API 设计
  - 课程/章节/小节/测验的数据模型设计
  - 用户进度追踪与评分系统
  - 自动化数据填充脚本 (`seed_gesp_courses.py`)

### 前端 (Frontend)
- **框架**：React 18 + Vite
- **UI 库**：Tailwind CSS + Framer Motion
- **图标**：Lucide React
- **代码编辑器**：@monaco-editor/react
- **Markdown 渲染**：react-markdown + react-syntax-highlighter
- **特性**：
  - 响应式设计，适配桌面与移动端
  - 沉浸式学习体验
  - 实时状态管理与路由控制

## 🚀 快速开始

### 1. 克隆项目

```bash
git clone https://github.com/caicaivic0322/pythonCourse.git
cd pythonCourse
```

### 2. 后端设置

进入 backend 目录：

```bash
cd backend
```

创建并激活虚拟环境：

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# venv\Scripts\activate   # Windows
```

安装依赖：

```bash
pip install -r requirements.txt
```

迁移数据库并填充初始数据：

```bash
python manage.py migrate
python seed_gesp_courses.py  # 填充课程数据
```

创建超级用户（可选）：

```bash
python manage.py createsuperuser
```

启动服务器：

```bash
python manage.py runserver
```

后端服务将在 `http://localhost:8000` 运行。

### 3. 前端设置

打开新的终端窗口，进入 frontend 目录：

```bash
cd frontend
```

安装依赖：

```bash
npm install
```

启动开发服务器：

```bash
npm run dev
```

前端应用将在 `http://localhost:5173` 运行。

## 📖 课程结构

1.  **GESP 1级**：Python 初识、变量、数据类型、输入输出。
2.  **GESP 2级**：运算符、条件判断、循环结构。
3.  **GESP 3级**：列表、元组、字符串操作。
4.  **GESP 4级**：函数、字典、模块。
5.  **Python 实战：Web 开发入门**：基于《Head First Python》，构建 vsearch Web 应用。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

MIT License
