import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from courses.models import Course, Chapter, Lesson

# 1. Clear existing data to avoid duplicates/conflicts during development
print("正在清理旧数据...")
Course.objects.all().delete()

# 2. Create Course (Chinese)
course, created = Course.objects.get_or_create(
    title="Python 基础：发射台",
    description="迈向 Python 编程世界的第一步。",
    defaults={'order': 1}
)
print(f"创建课程: {course.title}")

# 3. Chapter 1: Mission Briefing (Chinese)
ch1, _ = Chapter.objects.get_or_create(
    course=course, 
    title="任务简报：初识 Python", 
    defaults={'order': 1}
)

# Lesson 1.1: What is Python?
Lesson.objects.create(
    chapter=ch1, 
    title="什么是 Python？", 
    content="""
## 什么是 Python？

Python 是一种**强大且易于学习**的编程语言。它就像是编程界的“瑞士军刀”，无所不能！

### 为什么选择 Python？
- **简单易读**：代码像英语一样直观，非常适合初学者。
- **应用广泛**：从网站开发（YouTube, Instagram）到人工智能（ChatGPT），再到数据分析，Python 无处不在。
- **社区强大**：拥有庞大的开发者社区，遇到问题很容易找到答案。

### 我们的任务
在本课程中，你将扮演一名“代码学员”，通过完成一个个任务，掌握 Python 的核心技能，最终获得“Python 大师”勋章！
    """,
    lesson_type='text',
    order=1
)

# Lesson 1.2: First Script
Lesson.objects.create(
    chapter=ch1, 
    title="你的第一个脚本", 
    content="""
## Hello, World!

在编程界，有一个悠久的传统：学习任何新语言的第一步，都是让电脑说出 "Hello, World!"。

### 怎么做？
在 Python 中，我们使用 `print()` 函数来在屏幕上显示内容。

**语法：**
```python
print("你要显示的内容")
```

注意：
1. `print` 全部小写。
2. 内容必须放在括号 `()` 里。
3. 文字内容（字符串）必须用引号 `""` 或 `''` 包裹。

### 试一试
在下方的代码编辑器中，输入 `print('Hello, Python!')` 并点击运行。
    """,
    lesson_type='code',
    order=2
)

# 4. Chapter 2: Variables (Chinese)
ch2, _ = Chapter.objects.get_or_create(
    course=course, 
    title="数据仓库：变量与数据类型", 
    defaults={'order': 2}
)

# Lesson 2.1: Variables Concept
Lesson.objects.create(
    chapter=ch2, 
    title="变量：数据的盒子", 
    content="""
## 什么是变量？

想象你在搬家，你会把东西放进**盒子**里，并在盒子上写上标签（比如“书”、“衣服”）。

在 Python 中，**变量**就是这样的盒子。
- **变量名**：就是盒子上的标签。
- **值**：就是盒子里的东西。

### 创建变量
在 Python 中，创建变量非常简单，只需要用 `=` 号：

```python
score = 100
player_name = "CodeMaster"
```

这里，我们创建了一个叫 `score` 的变量，里面装着数字 `100`；还创建了一个叫 `player_name` 的变量，里面装着文字 `"CodeMaster"`。

### 变量命名规则
1. 只能包含字母、数字和下划线 `_`。
2. **不能以数字开头**。
3. 区分大小写（`Score` 和 `score` 是两个不同的变量）。
4. 建议使用**下划线命名法**（例如 `my_score`），让名字更易读。
    """,
    lesson_type='text',
    order=1
)

# Lesson 2.2: Data Types
Lesson.objects.create(
    chapter=ch2, 
    title="数据类型：盒子里装什么？", 
    content="""
## 常见的数据类型

Python 中的“盒子”（变量）可以装各种不同类型的东西。每种类型都有它的用途和特性。

### 1. 整数 (Integer / int)
**定义**：没有小数点的数字。可以正数、负数或零。
**特性**：Python 的整数**没有大小限制**（只要内存够大）。这与 C++ 的 `int` 不同，你不需要担心溢出问题！
**用途**：计数、年龄、等级、积分等。

```python
age = 12
xp = 500
temperature = -5
huge_number = 99999999999999999999999999  # 在 Python 中完全没问题！
```

---

### 2. 浮点数 (Float)
**定义**：带有小数点的数字。
**特性**：基于 IEEE 754 标准的双精度浮点数（类似于 C++ 的 `double`）。
**注意**：存在精度问题（例如 `0.1 + 0.2` 可能不完全等于 `0.3`），在处理金钱时需小心。
**用途**：价格、身高、重量、精确计算等。

```python
height = 1.75
price = 9.99
pi = 3.14159
```

---

### 3. 字符串 (String / str)
**定义**：一串文本字符。
**特性**：Python 字符串是**不可变**的（Immutable）。一旦创建，就不能修改其中的某个字符。支持 Unicode，可以包含中文、Emoji 等。
**规则**：必须用单引号 `'` 或双引号 `"` 包裹。

```python
name = "Alice"
message = 'Mission Start!'
dialogue = "他说：'你好！'"  # 引号可以嵌套
emoji = "🐍"
```

---

### 4. 布尔值 (Boolean / bool)
**定义**：逻辑真假值。
**特性**：实际上是整数的子类，`True` 等于 `1`，`False` 等于 `0`（虽然不建议这样混用）。
**值**：只有两个值 `True`（真）或 `False`（假）。
**注意**：首字母必须大写！这与 C++ 的 `true/false` 不同。

```python
is_game_over = False
has_key = True
```

### 动态类型 (Dynamic Typing)
Python 是**动态类型**语言。这意味着你不需要像 C++ 那样声明变量类型（如 `int a = 10;`）。
变量的类型取决于它当前指向的值，而且可以随时改变！

```python
x = 10      # x 是整数
print(type(x))
x = "Hello" # 现在 x 变成了字符串！Python 不会报错。
print(type(x))
```
这一点非常灵活，但也意味着你需要自己清楚变量里装的是什么。


### 动手时刻
在下一节课中，我们将通过代码来亲自操作这些数据类型！
    """,
    lesson_type='text',
    order=2
)

# Lesson 2.3: Variables Practice
Lesson.objects.create(
    chapter=ch2, 
    title="实战：定义你的角色", 
    content="""
## 任务目标

定义几个变量来描述你的游戏角色。

请在代码编辑器中完成以下任务：
1. 创建一个变量 `hero_name`，赋值为你的名字（字符串）。
2. 创建一个变量 `level`，赋值为 `1`（整数）。
3. 创建一个变量 `is_active`，赋值为 `True`（布尔值）。
4. 最后，使用 `print()` 打印出 `hero_name`。
    """,
    lesson_type='code',
    order=3
)

print("中文课程数据填充完成！")
