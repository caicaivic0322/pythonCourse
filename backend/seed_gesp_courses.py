import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from courses.models import Course, Chapter, Lesson, Quiz

def create_lesson(**kwargs):
    """
    Helper function to update or create a lesson.
    This prevents duplicate lessons and ensures content is updated.
    It also clears existing quizzes for the lesson to avoid duplicates.
    """
    chapter = kwargs.get('chapter')
    title = kwargs.get('title')
    defaults = {k: v for k, v in kwargs.items() if k not in ['chapter', 'title']}
    
    lesson, created = Lesson.objects.update_or_create(
        chapter=chapter,
        title=title,
        defaults=defaults
    )
    
    # Clear existing quizzes to prevent duplication when re-seeding
    # This ensures we always have the latest set of quizzes defined in this script
    lesson.quizzes.all().delete()
    return lesson

print("正在更新课程数据...")
# Course.objects.all().delete()  <-- Commented out to preserve user progress

# ==========================================
# Course 1: GESP 1级 - 编程启蒙
# ==========================================
print("正在创建 GESP 1级 课程...")
c1, _ = Course.objects.get_or_create(
    title="GESP 1级：编程启蒙",
    description="专为零基础设计的 Python 入门课程。涵盖变量、数据类型、输入输出、运算符、分支结构与循环基础。结合 GESP 一级考点，帮助学生轻松迈入编程大门。",
    defaults={'order': 1}
)

# --- 第1章：初识 Python ---
ch1, _ = Chapter.objects.get_or_create(course=c1, title="第1章：初识 Python 与变量", defaults={'order': 1})

# 1.1 什么是 Python
l1_1 = create_lesson(
    chapter=ch1, title="1.1 什么是 Python？", order=1, lesson_type='text',
    code_challenge_prompt="# 请在下方编写代码，输出 Hello GESP\nprint('Hello GESP')",
    content="""# 1.1 什么是 Python？

## 1. 概念讲解
Python 是一种高级编程语言，就像我们用英语和电脑交流一样。它由荷兰人 Guido van Rossum（吉多·范罗苏姆）发明。

### 为什么选择 Python？
- **简单易学**：语法接近英语，没有复杂的符号。
- **功能强大**：可以用来做网站、人工智能、数据分析、自动化脚本等。
- **解释型语言**：写完代码可以直接运行，不需要像 C++ 那样先编译成机器码。

## 2. 核心特性（GESP 考点）
1.  **解释型**：Python 代码由解释器逐行翻译执行。
2.  **文件扩展名**：Python 源代码文件的后缀名是 `.py`。
3.  **区分大小写**：`Print` 和 `print` 是不一样的，Python 只有 `print`。

## 3. 第一个程序
在编程界，大家学习新语言的第一个程序通常是输出 "Hello, World!"。

```python
print("Hello, World!")
```

- `print` 是 Python 的**函数**，意思是“打印”或“输出”。
- `()` 里面放我们要输出的内容。
- `""` 双引号表示里面的是**字符串**（文本）。

## 4. 易错点与考点
- **错误 1**：使用中文符号。
    - ❌ `print（"Hello"）` （使用了中文括号）
    - ✅ `print("Hello")` （必须是英文括号）
- **错误 2**：忘记引号。
    - ❌ `print(Hello)` （Python 会以为 Hello 是一个变量）
    - ✅ `print("Hello")`
- **考点**：Python 程序的文件后缀是什么？（答案：`.py`）

## 5. 小练习
尝试修改代码，输出你自己的名字，例如：`print("我是小明")`。
"""
)

Quiz.objects.create(
    lesson=l1_1,
    question="Python 源代码文件的后缀名是什么？",
    option_a=".python",
    option_b=".py",
    option_c=".pt",
    option_d=".txt",
    correct_answer="B",
    explanation="Python 文件的标准后缀名是 .py。"
)

Quiz.objects.create(
    lesson=l1_1,
    question="下列哪个是正确的 Python 输出语句？",
    option_a="Print('Hello')",
    option_b="print('Hello')",
    option_c="print（'Hello'）",
    option_d="output('Hello')",
    correct_answer="B",
    explanation="Python 区分大小写，函数名是 print（小写），且必须使用英文括号。"
)

Quiz.objects.create(
    lesson=l1_1,
    question="Python 语言的设计者是？",
    option_a="Bill Gates",
    option_b="Steve Jobs",
    option_c="Guido van Rossum",
    option_d="Elon Musk",
    correct_answer="C",
    explanation="Guido van Rossum（吉多·范罗苏姆）在 1989 年圣诞节期间发明了 Python。"
)

Quiz.objects.create(
    lesson=l1_1,
    question="Python 是一种什么类型的语言？",
    option_a="编译型",
    option_b="解释型",
    option_c="汇编语言",
    option_d="机器语言",
    correct_answer="B",
    explanation="Python 是解释型语言，代码在运行时由解释器逐行翻译。"
)

Quiz.objects.create(
    lesson=l1_1,
    question="在 Python 中，单行注释使用什么符号？",
    option_a="//",
    option_b="/*",
    option_c="#",
    option_d="--",
    correct_answer="C",
    explanation="Python 使用 # 符号进行单行注释。"
)

Quiz.objects.create(
    lesson=l1_1,
    question="Python 的交互式提示符通常是？",
    option_a="...",
    option_b=">>>",
    option_c="$",
    option_d="%",
    correct_answer="B",
    explanation="Python Shell 的标准提示符是 >>>。"
)

Quiz.objects.create(
    lesson=l1_1,
    question="下列哪个不是 Python 的特点？",
    option_a="简单易学",
    option_b="免费开源",
    option_c="运行速度最快",
    option_d="跨平台",
    correct_answer="C",
    explanation="Python 的运行速度通常比 C/C++ 慢，但开发效率高。"
)

Quiz.objects.create(
    lesson=l1_1,
    question="Python 3.x 和 Python 2.x 兼容吗？",
    option_a="完全兼容",
    option_b="不完全兼容",
    option_c="完全一样",
    option_d="Python 2 是 Python 3 的升级版",
    correct_answer="B",
    explanation="Python 3 做出了不向后兼容的改进（如 print 函数化）。"
)

Quiz.objects.create(
    lesson=l1_1,
    question="print('Hello') 中的引号可以使用？",
    option_a="单引号",
    option_b="双引号",
    option_c="三引号",
    option_d="以上都可以",
    correct_answer="D",
    explanation="Python 字符串可以使用单引号、双引号或三引号。"
)

Quiz.objects.create(
    lesson=l1_1,
    question="判断题：Python 代码必须编译成 .exe 文件才能运行。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，Python 是解释型语言，可以直接运行源码 (.py)。"
)

# 1.2 变量与命名
l1_2 = create_lesson(
    chapter=ch1, title="1.2 变量与命名规则", order=2, lesson_type='text',
    code_challenge_prompt="# 定义一个变量 score，赋值为 100，并打印出来\nscore = 100\nprint(score)",
    content="""# 1.2 变量与命名规则

## 1. 什么是变量？
变量就像一个**盒子**，用来装数据。我们可以给这个盒子贴上标签（变量名），通过标签找到里面的数据。

```python
score = 100
name = "Alice"
```
- `score` 是变量名。
- `=` 是**赋值运算符**，意思是把右边的 `100` 放进左边的 `score` 盒子里。
- `100` 是变量的值。

## 2. 变量命名规则（GESP 重点考点）
给变量起名字必须遵守规则，否则程序会报错。

1.  **组成字符**：只能包含**字母**（a-z, A-Z）、**数字**（0-9）和**下划线**（_）。
2.  **开头限制**：**不能以数字开头**。
3.  **关键字**：不能使用 Python 的保留字（如 `if`, `else`, `for`, `print`, `class` 等）。
4.  **大小写敏感**：`Score` 和 `score` 是两个不同的变量。

## 3. 示例辨析
| 变量名 | 是否合法 | 原因 |
| :--- | :--- | :--- |
| `name` | ✅ | 合法 |
| `user_1` | ✅ | 合法 |
| `_score` | ✅ | 合法（下划线开头允许） |
| `2name` | ❌ | **数字不能开头** |
| `my-name` | ❌ | **不能包含减号**（只能用下划线） |
| `if` | ❌ | **关键字**不能用 |
| `MyName` | ✅ | 合法（但推荐用小写加下划线 `my_name`） |

## 4. 变量的多重赋值
Python 允许同时给多个变量赋值：
```python
a = b = 10  # a 和 b 都是 10
x, y = 1, 2 # x 是 1，y 是 2
```
**交换变量的值**（Python 特有技巧）：
```python
a = 1
b = 2
a, b = b, a  # 现在 a=2, b=1
```

## 5. 易错点
- **混淆 `=` 和 `==`**：
    - `=` 是赋值（把右边给左边）。
    - `==` 是判断相等（比较左右两边是否一样）。
"""
)

Quiz.objects.create(
    lesson=l1_2,
    question="下列哪个变量名是**错误**的？",
    option_a="student_1",
    option_b="_age",
    option_c="3days",
    option_d="total_score",
    correct_answer="C",
    explanation="变量名不能以数字开头，所以 3days 是错误的。"
)

Quiz.objects.create(
    lesson=l1_2,
    question="执行 a, b = 10, 20 后，a 的值是多少？",
    option_a="10",
    option_b="20",
    option_c="30",
    option_d="报错",
    correct_answer="A",
    explanation="这是解包赋值，a 对应第一个值 10。"
)

Quiz.objects.create(
    lesson=l1_2,
    question="下列哪个变量名是合法的？",
    option_a="2nd_place",
    option_b="my-variable",
    option_c="class",
    option_d="user_name",
    correct_answer="D",
    explanation="数字不能开头，不能用减号，不能用关键字。user_name 是合法的。"
)

Quiz.objects.create(
    lesson=l1_2,
    question="在 Python 中，变量名区分大小写吗？",
    option_a="区分",
    option_b="不区分",
    option_c="看操作系统",
    option_d="只区分首字母",
    correct_answer="A",
    explanation="Python 是大小写敏感的语言，Name 和 name 是两个变量。"
)

Quiz.objects.create(
    lesson=l1_2,
    question="x = 5; y = 10; x = y; 执行后 x 的值是？",
    option_a="5",
    option_b="10",
    option_c="15",
    option_d="0",
    correct_answer="B",
    explanation="把 y 的值赋给 x，x 变成了 10。"
)

Quiz.objects.create(
    lesson=l1_2,
    question="下列哪个是 Python 的保留字（关键字）？",
    option_a="variable",
    option_b="print",
    option_c="if",
    option_d="string",
    correct_answer="C",
    explanation="if 是条件判断的关键字，不能用作变量名。"
)

Quiz.objects.create(
    lesson=l1_2,
    question="name = 'Alice'，name 的数据类型是？",
    option_a="int",
    option_b="float",
    option_c="str",
    option_d="bool",
    correct_answer="C",
    explanation="带引号的是字符串 (str)。"
)

Quiz.objects.create(
    lesson=l1_2,
    question="如果在赋值前使用变量 print(a)，会发生什么？",
    option_a="输出空",
    option_b="输出 0",
    option_c="报错 NameError",
    option_d="自动创建变量",
    correct_answer="C",
    explanation="变量必须先赋值（定义）才能使用。"
)

Quiz.objects.create(
    lesson=l1_2,
    question="变量名可以包含空格吗？",
    option_a="可以",
    option_b="不可以",
    option_c="只能在中间",
    option_d="只能在末尾",
    correct_answer="B",
    explanation="变量名中间不能有空格，通常用下划线代替。"
)

Quiz.objects.create(
    lesson=l1_2,
    question="判断题：Python 的变量不需要声明类型，可以直接赋值。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，Python 是动态类型语言。"
)

# 1.3 基本数据类型
l1_3 = create_lesson(
    chapter=ch1, title="1.3 基本数据类型", order=3, lesson_type='text',
    code_challenge_prompt="# 将字符串 '123' 转换为整数，加上 10 之后输出\ns = '123'\numn = int(s)\nprint(umn + 10)",
    content="""# 1.3 基本数据类型

## 1. 四大基本类型
Python 中常用的数据类型有四种：

1.  **整数 (int)**：没有小数点的数字。
    - 例如：`1`, `100`, `-5`, `0`
2.  **浮点数 (float)**：带小数点的数字。
    - 例如：`3.14`, `2.0`, `-0.5`
    - 注意：`2` 是整数，`2.0` 是浮点数。
3.  **字符串 (str)**：用引号括起来的文本。
    - 例如：`"Hello"`, `'Python'`, `"123"`
    - 注意：`"123"` 是字符串，不是数字。
4.  **布尔值 (bool)**：只有两个值，真或假。
    - 例如：`True` (真), `False` (假)
    - 注意：首字母必须**大写**。

## 2. 类型查询与转换
- **查询类型**：使用 `type()` 函数。
  ```python
  print(type(10))    # <class 'int'>
  print(type(3.14))  # <class 'float'>
  ```
- **类型转换**：
  ```python
  int("10")    # 字符串转整数 -> 10
  float("10")  # 整数转浮点 -> 10.0
  str(123)     # 整数转字符串 -> "123"
  int(3.9)     # 浮点转整数 -> 3 (直接丢弃小数，不四舍五入！)
  ```

## 3. 易错点与考点
- **考点**：`int(3.9)` 的结果是 `3`，而不是 `4`。Python 转换整数时是**向下取整**（截断小数）。
- **考点**：字符串相加是拼接。
  ```python
  print("10" + "20")  # 输出 "1020"
  print(10 + 20)      # 输出 30
  ```
- **易错**：`True` 和 `False` 必须大写，`true` 是错误的。
"""
)

Quiz.objects.create(
    lesson=l1_3,
    question="执行 int(5.9) 的结果是？",
    option_a="5",
    option_b="6",
    option_c="5.9",
    option_d="报错",
    correct_answer="A",
    explanation="int() 函数将浮点数转换为整数时，会直接去掉小数部分（向下取整）。"
)

Quiz.objects.create(
    lesson=l1_3,
    question="type(3.0) 的结果是？",
    option_a="int",
    option_b="float",
    option_c="str",
    option_d="bool",
    correct_answer="B",
    explanation="带小数点的数字类型是浮点数 (float)。"
)

Quiz.objects.create(
    lesson=l1_3,
    question="int(3.14) 的结果是？",
    option_a="3",
    option_b="4",
    option_c="3.14",
    option_d="报错",
    correct_answer="A",
    explanation="int() 转换浮点数时直接截断小数部分。"
)

Quiz.objects.create(
    lesson=l1_3,
    question="float(5) 的结果是？",
    option_a="5",
    option_b="5.0",
    option_c="5.00",
    option_d="报错",
    correct_answer="B",
    explanation="整数转浮点数会加上小数点。"
)

Quiz.objects.create(
    lesson=l1_3,
    question="str(123) 的结果是？",
    option_a="123",
    option_b="'123'",
    option_c="123.0",
    option_d="[1, 2, 3]",
    correct_answer="B",
    explanation="整数转为字符串。"
)

Quiz.objects.create(
    lesson=l1_3,
    question="type(True) 返回的是？",
    option_a="int",
    option_b="bool",
    option_c="str",
    option_d="float",
    correct_answer="B",
    explanation="True 和 False 是布尔类型 (bool)。"
)

Quiz.objects.create(
    lesson=l1_3,
    question="'10' + '20' 的结果是？",
    option_a="30",
    option_b="1020",
    option_c="'30'",
    option_d="'1020'",
    correct_answer="D",
    explanation="字符串相加是拼接操作。"
)

Quiz.objects.create(
    lesson=l1_3,
    question="int('10') + 5 的结果是？",
    option_a="15",
    option_b="'105'",
    option_c="105",
    option_d="报错",
    correct_answer="A",
    explanation="先将字符串 '10' 转为整数 10，再加 5。"
)

Quiz.objects.create(
    lesson=l1_3,
    question="bool(0) 的结果是？",
    option_a="True",
    option_b="False",
    option_c="0",
    option_d="None",
    correct_answer="B",
    explanation="在 Python 中，数字 0 被视为 False。"
)

Quiz.objects.create(
    lesson=l1_3,
    question="判断题：Python 中的字符串可以用单引号或双引号括起来。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，两者等价。"
)

# 1.4 输入与输出
l1_4 = create_lesson(
    chapter=ch1, title="1.4 输入与输出", order=4, lesson_type='code',
    code_challenge_prompt="# 编写一个程序，输入你的名字，然后输出 '你好, 名字'\nname = input()\nprint('你好,', name)",
    content="""# 1.4 输入与输出

## 1. 输出：print()
我们已经用过 `print()`，现在来看看它的进阶用法。

- **输出多个内容**：用逗号 `,` 隔开，默认会用空格连接。
  ```python
  print("Hello", "World")  # 输出：Hello World
  ```
- **指定分隔符 (`sep`)**：
  ```python
  print("a", "b", "c", sep="-")  # 输出：a-b-c
  ```
- **指定结尾符 (`end`)**：默认 `print` 完会换行，可以修改。
  ```python
  print("Hello", end="*")
  print("World")
  # 输出：Hello*World (没有换行)
  ```

## 2. 输入：input()
程序需要和用户交互，使用 `input()` 获取键盘输入。

```python
name = input("请输入你的名字：")
print("你好", name)
```

**重要考点**：
`input()` 函数接收到的内容，**永远是字符串 (str) 类型**！
如果你输入的是数字，并想用来计算，必须先转换类型。

```python
# ❌ 错误做法
age = input("请输入年龄：")
print(age + 1)  # 报错！字符串不能和数字相加

# ✅ 正确做法
age_str = input("请输入年龄：")
age = int(age_str)  # 转换为整数
print(age + 1)
```

或者一步到位：
```python
age = int(input("请输入年龄："))
```

## 3. 格式化输出 (f-string)
这是最方便的输出方式，在字符串前加 `f`，在大括号 `{}` 里放变量。

```python
name = "Alice"
score = 98
print(f"学生 {name} 的分数是 {score}")
# 输出：学生 Alice 的分数是 98
```
"""
)

Quiz.objects.create(
    lesson=l1_4,
    question="如果用户输入 10，代码 a = input() 执行后，a 的类型是？",
    option_a="int",
    option_b="str",
    option_c="float",
    option_d="bool",
    correct_answer="B",
    explanation="input() 函数永远返回字符串类型，即使输入的是数字。"
)

Quiz.objects.create(
    lesson=l1_4,
    question="print('A', 'B', sep='*') 的输出结果是？",
    option_a="A B",
    option_b="AB",
    option_c="A*B",
    option_d="A,B",
    correct_answer="C",
    explanation="sep 参数指定了分隔符为 *。"
)

Quiz.objects.create(
    lesson=l1_4,
    question="print('Hello', end=' ') 的作用是？",
    option_a="报错",
    option_b="输出 Hello 后不换行，而是加一个空格",
    option_c="输出 Hello 后加两个空格",
    option_d="清空屏幕",
    correct_answer="B",
    explanation="end 参数指定输出结束时的字符，默认为换行符 \\n。"
)

Quiz.objects.create(
    lesson=l1_4,
    question="x = input('Enter: '); 如果输入 5，x * 2 的结果是？",
    option_a="10",
    option_b="'55'",
    option_c="5",
    option_d="报错",
    correct_answer="B",
    explanation="input 返回字符串 '5'，'5' * 2 是字符串重复，结果 '55'。"
)

Quiz.objects.create(
    lesson=l1_4,
    question="name='Bob'; age=10; f'{name} is {age}' 的结果？",
    option_a="'Bob is 10'",
    option_b="'name is age'",
    option_c="'{Bob} is {10}'",
    option_d="报错",
    correct_answer="A",
    explanation="f-string 会替换 {} 中的变量值。"
)

Quiz.objects.create(
    lesson=l1_4,
    question="print(1, 2, 3) 默认输出什么？",
    option_a="123",
    option_b="1,2,3",
    option_c="1 2 3",
    option_d="1\\n2\\n3",
    correct_answer="C",
    explanation="print 多个参数默认用空格分隔。"
)

Quiz.objects.create(
    lesson=l1_4,
    question="想要输入一个整数，应该怎么写？",
    option_a="input(int())",
    option_b="int(input())",
    option_c="input()",
    option_d="str(input())",
    correct_answer="B",
    explanation="先获取字符串输入，再转换为整数。"
)

Quiz.objects.create(
    lesson=l1_4,
    question="input() 函数执行时，程序会？",
    option_a="继续执行下一行",
    option_b="暂停等待用户输入",
    option_c="自动输入随机数",
    option_d="退出",
    correct_answer="B",
    explanation="input() 是阻塞的，直到用户按下回车键。"
)

Quiz.objects.create(
    lesson=l1_4,
    question="print('a', 'b', sep='') 的输出是？",
    option_a="a b",
    option_b="ab",
    option_c="a,b",
    option_d="a\\nb",
    correct_answer="B",
    explanation="sep='' 表示分隔符为空字符串，即紧挨着输出。"
)

Quiz.objects.create(
    lesson=l1_4,
    question="判断题：print() 函数只能输出一个变量。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，print 可以接受任意多个参数。"
)

# --- 第2章：运算符与表达式 ---
ch2, _ = Chapter.objects.get_or_create(course=c1, title="第2章：运算符与表达式", defaults={'order': 2})

# 2.1 算术运算符
l2_1 = create_lesson(
    chapter=ch2, title="2.1 算术运算符", order=1, lesson_type='text',
    code_challenge_prompt="# 计算 10 除以 3 的商（整数）和余数\na = 10\nb = 3\nprint(f'商: {a // b}, 余数: {a % b}')",
    content="""# 2.1 算术运算符

## 1. 基本运算符
Python 的数学运算非常直观：
- `+` 加
- `-` 减
- `*` 乘
- `/` 除（结果总是浮点数，如 `4/2` 结果是 `2.0`）

## 2. 特殊运算符（GESP 必考）
这三个运算符是考试的重点：

1.  **整除 (`//`)**：只保留整数部分，向下取整。
    ```python
    print(5 // 2)   # 2
    print(-5 // 2)  # -3 (注意！向下取整，-2.5 变成 -3)
    ```
2.  **取模/求余 (`%`)**：计算余数。
    ```python
    print(5 % 2)    # 1 (5除以2商2余1)
    print(10 % 3)   # 1
    ```
    *用途：判断奇偶数（`x % 2 == 0` 是偶数），取个位数（`x % 10`）。*
3.  **幂运算 (`**`)**：计算乘方。
    ```python
    print(2 ** 3)   # 2的3次方 = 8
    print(3 ** 2)   # 9
    ```

## 3. 复合赋值运算符
`+=`, `-=`, `*=`, `/=` 等。
```python
a = 10
a += 5  # 等同于 a = a + 5
print(a) # 15
```

## 4. 易错点
- 除法 `/` 永远返回 `float`。
- 负数整除 `//` 是向小取整（往负无穷方向），不是简单的去掉小数。

## 5. 取模的常见应用
取模 `%` 不只是求余数，它经常用于判断规律。

### 判断奇偶
```python
if x % 2 == 0:
    print("偶数")
else:
    print("奇数")
```

### 取个位数
```python
n = 123
print(n % 10)  # 3
```

### 判断能否整除
```python
if n % 3 == 0:
    print("能被 3 整除")
```

## 6. 运算结果类型
```python
print(type(10 + 3))  # int
print(type(10 / 2))  # float
print(type(10 // 3)) # int
```

只要使用 `/`，结果就是浮点数，即使看起来刚好整除。

## 7. 小练习
给定一个三位数 `n = 456`：
1. 输出个位数
2. 输出十位数
3. 判断它是否能被 3 整除
"""
)

Quiz.objects.create(
    lesson=l2_1,
    question="表达式 7 % 3 的结果是？",
    option_a="2",
    option_b="1",
    option_c="2.33",
    option_d="0",
    correct_answer="B",
    explanation="7 除以 3 商 2 余 1。"
)

Quiz.objects.create(
    lesson=l2_1,
    question="表达式 2 ** 3 的结果是？",
    option_a="6",
    option_b="5",
    option_c="8",
    option_d="9",
    correct_answer="C",
    explanation="2 的 3 次方等于 2 * 2 * 2 = 8。"
)

Quiz.objects.create(
    lesson=l2_1,
    question="10 // 3 的结果是？",
    option_a="3.33",
    option_b="3",
    option_c="4",
    option_d="1",
    correct_answer="B",
    explanation="// 是整除运算符，只保留整数部分。"
)

Quiz.objects.create(
    lesson=l2_1,
    question="3 * (2 + 1) 的结果是？",
    option_a="9",
    option_b="7",
    option_c="6",
    option_d="5",
    correct_answer="A",
    explanation="括号优先级最高，先算 2+1=3，再算 3*3=9。"
)

Quiz.objects.create(
    lesson=l2_1,
    question="a = 5; a += 1; a 的值是？",
    option_a="5",
    option_b="6",
    option_c="1",
    option_d="报错",
    correct_answer="B",
    explanation="a += 1 等同于 a = a + 1。"
)

Quiz.objects.create(
    lesson=l2_1,
    question="10 / 2 的结果类型是？",
    option_a="int",
    option_b="float",
    option_c="str",
    option_d="bool",
    correct_answer="B",
    explanation="除法 / 的结果永远是浮点数。"
)

Quiz.objects.create(
    lesson=l2_1,
    question="-5 // 2 的结果是？",
    option_a="-2",
    option_b="-3",
    option_c="-2.5",
    option_d="2",
    correct_answer="B",
    explanation="整除是向下取整，-2.5 向下取整为 -3。"
)

Quiz.objects.create(
    lesson=l2_1,
    question="哪个运算符用于计算余数？",
    option_a="/",
    option_b="//",
    option_c="%",
    option_d="#",
    correct_answer="C",
    explanation="% 是取模（求余）运算符。"
)

Quiz.objects.create(
    lesson=l2_1,
    question="2 ** 3 ** 2 的结果是？",
    option_a="64",
    option_b="512",
    option_c="4096",
    option_d="报错",
    correct_answer="B",
    explanation="幂运算是从右向左结合的，先算 3**2=9，再算 2**9=512。"
)

Quiz.objects.create(
    lesson=l2_1,
    question="判断题：Python 中 1/2 的结果是 0。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，Python 3 中 / 是真除法，结果是 0.5。"
)

# 2.2 比较与逻辑运算符
l2_2 = create_lesson(
    chapter=ch2, title="2.2 比较与逻辑运算符", order=2, lesson_type='text',
    code_challenge_prompt="# 判断一个数是否在 10 到 20 之间（包含 10 和 20）\nnum = 15\nis_between = 10 <= num <= 20\nprint(is_between)",
    content="""# 2.2 比较与逻辑运算符

## 1. 比较运算符
比较的结果是布尔值：`True` 或 `False`。
- `==` 等于（注意是两个等号！）
- `!=` 不等于
- `>` 大于
- `<` 小于
- `>=` 大于等于
- `<=` 小于等于

**Python 特性**：支持链式比较。
```python
x = 15
print(10 < x < 20)  # True (等同于 x > 10 and x < 20)
```

## 2. 逻辑运算符
用于组合多个条件。
1.  **and (与)**：两边都为真，结果才为真。（并且）
    - `True and True` -> `True`
    - `True and False` -> `False`
2.  **or (或)**：只要有一边为真，结果就为真。（或者）
    - `False or True` -> `True`
    - `False or False` -> `False`
3.  **not (非)**：取反。
    - `not True` -> `False`

## 3. 短路运算（难点）
- `a and b`：如果 `a` 是假，直接返回 `a`，不看 `b`。
- `a or b`：如果 `a` 是真，直接返回 `a`，不看 `b`。

```python
print(0 and 100)  # 输出 0 (因为0是假)
print(1 or 100)   # 输出 1 (因为1是真)
```

## 4. 闰年判断案例
判断 `year` 是否为闰年：
1. 能被 4 整除 但 不能被 100 整除。
2. 或者 能被 400 整除。

```python
(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
```
"""
)

Quiz.objects.create(
    lesson=l2_2,
    question="not (10 > 5) 的结果是？",
    option_a="True",
    option_b="False",
    option_c="10",
    option_d="5",
    correct_answer="B",
    explanation="10 > 5 是 True，not True 结果是 False。"
)

Quiz.objects.create(
    lesson=l2_2,
    question="True or False 的结果是？",
    option_a="True",
    option_b="False",
    option_c="Error",
    option_d="None",
    correct_answer="A",
    explanation="or 运算符只要有一个为真，结果即为真。"
)

Quiz.objects.create(
    lesson=l2_2,
    question="5 != 5 的结果是？",
    option_a="True",
    option_b="False",
    option_c="5",
    option_d="报错",
    correct_answer="B",
    explanation="5 等于 5，所以 5 不等于 5 是假。"
)

Quiz.objects.create(
    lesson=l2_2,
    question="10 >= 10 的结果是？",
    option_a="True",
    option_b="False",
    option_c="10",
    option_d="None",
    correct_answer="A",
    explanation="大于或等于，只要满足其一即为真。"
)

Quiz.objects.create(
    lesson=l2_2,
    question="False and True 的结果是？",
    option_a="True",
    option_b="False",
    option_c="None",
    option_d="Error",
    correct_answer="B",
    explanation="and 运算符要求两边都为真，结果才为真。"
)

Quiz.objects.create(
    lesson=l2_2,
    question="not False 的结果是？",
    option_a="True",
    option_b="False",
    option_c="0",
    option_d="1",
    correct_answer="A",
    explanation="not 是取反操作。"
)

Quiz.objects.create(
    lesson=l2_2,
    question="1 < 2 < 3 的结果是？",
    option_a="True",
    option_b="False",
    option_c="Error",
    option_d="1",
    correct_answer="A",
    explanation="链式比较，等同于 1 < 2 and 2 < 3。"
)

Quiz.objects.create(
    lesson=l2_2,
    question="if x == 5: 中的 == 能换成 = 吗？",
    option_a="可以",
    option_b="不可以",
    option_c="有时候可以",
    option_d="看版本",
    correct_answer="B",
    explanation="不可以，= 是赋值，== 是比较。"
)

Quiz.objects.create(
    lesson=l2_2,
    question="'a' == 'a' 的结果是？",
    option_a="True",
    option_b="False",
    option_c="'a'",
    option_d="报错",
    correct_answer="A",
    explanation="字符串内容相同，比较结果为真。"
)

Quiz.objects.create(
    lesson=l2_2,
    question="判断题：not (True or False) 的结果是 False。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，True or False 是 True，not True 是 False。"
)

# 2.3 运算符优先级
l2_3 = create_lesson(
    chapter=ch2, title="2.3 运算符优先级", order=3, lesson_type='text',
    code_challenge_prompt="# 计算表达式：2 + 3 * 4 > 10\nresult = 2 + 3 * 4 > 10\nprint(result)",
    content="""# 2.3 运算符优先级

当一个式子里有多种运算时，谁先谁后？

## 1. 优先级排行榜（从高到低）
1.  `()` **括号**：最牛，想先算谁就括谁。
2.  `**` **幂运算**：2 ** 3。
3.  `*`, `/`, `//`, `%` **乘除类**。
4.  `+`, `-` **加减类**。
5.  `>`, `<`, `==` **比较类**。
6.  `not`
7.  `and`
8.  `or`

**口诀**：
**括号最大幂第二，乘除加减再比较，非与或门排最后。**

## 2. 案例分析
```python
result = 2 + 3 * 4 > 10 and 5 < 2
```
解析步骤：
1. 先算乘法：`3 * 4 = 12` -> `2 + 12 > 10 and 5 < 2`
2. 再算加法：`2 + 12 = 14` -> `14 > 10 and 5 < 2`
3. 再算比较：
   - `14 > 10` 是 `True`
   - `5 < 2` 是 `False`
   - -> `True and False`
4. 最后算逻辑：`True and False` -> `False`

## 3. 建议
虽然有优先级规则，但写代码时**建议多用括号**，让代码更易读，也不容易出错。
例如：`(2 + 3) * 4` 显然比 `2 + 3 * 4` 意图更明确（如果你的本意是先加）。

## 4. 同级运算顺序
大多数同级运算从左到右：

```python
print(10 - 3 - 2)  # 5
```

先算 `10 - 3 = 7`，再算 `7 - 2 = 5`。

但幂运算 `**` 比较特殊，通常从右往左结合：

```python
print(2 ** 3 ** 2)  # 512
```

先算 `3 ** 2 = 9`，再算 `2 ** 9 = 512`。

## 5. 布尔表达式里更要加括号
```python
is_valid = (age >= 12 and score >= 60) or is_vip
```

括号能让读代码的人马上看懂你的判断意图。

## 6. 易错点
- `and` 优先级高于 `or`
- `not` 优先级高于 `and`
- 比较运算会先于逻辑运算完成
- 不确定时就加括号

## 7. 小练习
手算并用 Python 验证：
1. `2 + 3 * 4`
2. `(2 + 3) * 4`
3. `True or False and False`
4. `not (3 > 2)`
"""
)

Quiz.objects.create(
    lesson=l2_3,
    question="2 + 3 * 2 的结果是？",
    option_a="10",
    option_b="8",
    option_c="7",
    option_d="12",
    correct_answer="B",
    explanation="乘法优先级高于加法，先算 3*2=6，再加 2 得 8。"
)

Quiz.objects.create(
    lesson=l2_3,
    question="1 + 2 * 3 - 4 的结果是？",
    option_a="5",
    option_b="3",
    option_c="9",
    option_d="0",
    correct_answer="B",
    explanation="先算乘法 2*3=6，再算加减 1+6-4=3。"
)

Quiz.objects.create(
    lesson=l2_3,
    question="(1 + 2) * 3 的结果是？",
    option_a="9",
    option_b="7",
    option_c="6",
    option_d="5",
    correct_answer="A",
    explanation="括号改变优先级，先算加法 1+2=3，再算 3*3=9。"
)

Quiz.objects.create(
    lesson=l2_3,
    question="True or False and False 的结果是？",
    option_a="True",
    option_b="False",
    option_c="Error",
    option_d="None",
    correct_answer="A",
    explanation="and 优先级高于 or，先算 False and False -> False，再算 True or False -> True。"
)

Quiz.objects.create(
    lesson=l2_3,
    question="not True and False 的结果是？",
    option_a="True",
    option_b="False",
    option_c="Error",
    option_d="None",
    correct_answer="B",
    explanation="not 优先级最高，not True -> False，False and False -> False。"
)

Quiz.objects.create(
    lesson=l2_3,
    question="2 ** 3 * 2 的结果是？",
    option_a="16",
    option_b="64",
    option_c="12",
    option_d="32",
    correct_answer="A",
    explanation="幂运算优先级高于乘法，2**3=8，8*2=16。"
)

Quiz.objects.create(
    lesson=l2_3,
    question="10 % 3 + 1 的结果是？",
    option_a="2",
    option_b="1",
    option_c="0",
    option_d="4",
    correct_answer="A",
    explanation="取模优先级高于加法，10%3=1，1+1=2。"
)

Quiz.objects.create(
    lesson=l2_3,
    question="哪个运算符优先级最低？",
    option_a="+",
    option_b="*",
    option_c="or",
    option_d="and",
    correct_answer="C",
    explanation="逻辑或 or 的优先级在常见运算符中是最低的。"
)

Quiz.objects.create(
    lesson=l2_3,
    question="判断题：乘除法的优先级相同，从左到右计算。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，同级运算符从左到右。"
)

# --- 第3章：决策与分支 ---
ch3, _ = Chapter.objects.get_or_create(course=c1, title="第3章：决策与分支", defaults={'order': 3})

# 3.1 if 结构
l3_1 = create_lesson(
    chapter=ch3, title="3.1 分支结构 (if-elif-else)", order=1, lesson_type='code',
    code_challenge_prompt="# 根据分数 score 打印等级：>=60 及格，<60 不及格\nscore = 55\nif score >= 60:\n    print('及格')\nelse:\n    print('不及格')",
    content="""# 3.1 分支结构

程序不再是“一条道走到黑”，而是可以根据条件选择不同的路。

## 1. 单分支 (if)
如果条件成立，就做某事。
```python
age = 18
if age >= 18:
    print("成年了")  # 注意前面的缩进（4个空格）
```
**重点**：`if` 语句后面要有**冒号** `:`，下一行必须**缩进**。

## 2. 双分支 (if-else)
如果条件成立做 A，否则做 B。
```python
score = 59
if score >= 60:
    print("及格")
else:
    print("不及格")
```

## 3. 多分支 (if-elif-else)
有多个条件判断。
```python
score = 85
if score >= 90:
    print("优秀")
elif score >= 80:
    print("良好")
elif score >= 60:
    print("及格")
else:
    print("不及格")
```
**注意**：程序会从上往下检查，一旦满足某个条件，执行完对应的代码块后，就会**跳出整个 if 结构**，不会再检查后面的条件。

## 4. 易错点
- 忘记冒号 `:`。
- 缩进不一致（Python 对缩进要求非常严格，通常使用 4 个空格）。
- `elif` 拼写错误（不是 `elseif`）。

## 5. 条件顺序很重要
多分支会从上到下检查，先满足谁就执行谁。

错误示例：

```python
score = 95
if score >= 60:
    print("及格")
elif score >= 90:
    print("优秀")
```

这会输出“及格”，不会输出“优秀”。因为 `score >= 60` 已经先成立。

正确写法：

```python
if score >= 90:
    print("优秀")
elif score >= 60:
    print("及格")
```

## 6. 嵌套 if
```python
age = 13
score = 90

if age >= 12:
    if score >= 80:
        print("可以参加进阶班")
```

嵌套 if 可以表达更复杂条件，但不要嵌套太深，太深会难读。

## 7. 小练习
根据分数输出等级：
- `>= 90`：优秀
- `>= 80`：良好
- `>= 60`：及格
- `< 60`：不及格

注意条件顺序。
"""
)

Quiz.objects.create(
    lesson=l3_1,
    question="在 Python 中，if 语句块的代码必须？",
    option_a="用大括号包围",
    option_b="缩进",
    option_c="写在同一行",
    option_d="加分号",
    correct_answer="B",
    explanation="Python 通过缩进来表示代码块的层级关系。"
)

Quiz.objects.create(
    lesson=l3_1,
    question="if x > 0: print('Positive') 的写法？",
    option_a="合法",
    option_b="不合法",
    option_c="必须换行",
    option_d="必须加括号",
    correct_answer="A",
    explanation="如果代码块只有一行，可以写在冒号后面（但不推荐）。"
)

Quiz.objects.create(
    lesson=l3_1,
    question="elif 必须配合什么使用？",
    option_a="else",
    option_b="if",
    option_c="for",
    option_d="while",
    correct_answer="B",
    explanation="elif 是 else if 的缩写，必须紧跟在 if 或另一个 elif 之后。"
)

Quiz.objects.create(
    lesson=l3_1,
    question="一个 if 结构中可以有多少个 elif？",
    option_a="0个",
    option_b="1个",
    option_c="任意个",
    option_d="最多3个",
    correct_answer="C",
    explanation="elif 可以有任意多个。"
)

Quiz.objects.create(
    lesson=l3_1,
    question="else 语句是必须的吗？",
    option_a="是",
    option_b="不是",
    option_c="看情况",
    option_d="在函数中是",
    correct_answer="B",
    explanation="else 是可选的。"
)

Quiz.objects.create(
    lesson=l3_1,
    question="if 条件后面忘记写冒号会怎样？",
    option_a="自动补全",
    option_b="SyntaxError",
    option_c="运行但不执行",
    option_d="输出 False",
    correct_answer="B",
    explanation="语法错误。"
)

Quiz.objects.create(
    lesson=l3_1,
    question="x = 10; if x: print('Yes') 会输出吗？",
    option_a="会",
    option_b="不会",
    option_c="报错",
    option_d="看运气",
    correct_answer="A",
    explanation="非零数字在布尔上下文中为 True。"
)

Quiz.objects.create(
    lesson=l3_1,
    question="嵌套 if 语句的缩进要求？",
    option_a="不需要缩进",
    option_b="增加一级缩进",
    option_c="减少一级缩进",
    option_d="随意缩进",
    correct_answer="B",
    explanation="每一层嵌套都需要增加缩进。"
)

Quiz.objects.create(
    lesson=l3_1,
    question="判断题：if 语句可以嵌套使用。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，if 里面可以再写 if。"
)

# --- 第4章：循环结构 ---
ch4, _ = Chapter.objects.get_or_create(course=c1, title="第4章：循环结构", defaults={'order': 4})

# 4.1 for 循环
l4_1 = create_lesson(
    chapter=ch4, title="4.1 For 循环与 range", order=1, lesson_type='text',
    code_challenge_prompt="# 打印 0 到 4\nfor i in range(5):\n    print(i)",
    content="""# 4.1 For 循环与 range

## 1. 什么是循环？
当我们需要重复做某件事时，就用循环。比如打印 100 次 "Hello"。

## 2. range() 函数
`range` 是 "范围" 的意思，用来生成一系列数字。
- `range(n)`: 生成 0 到 n-1。
    - `range(5)` -> 0, 1, 2, 3, 4 (共5个)
- `range(start, stop)`: 从 start 开始，到 stop-1 结束（**包头不包尾**）。
    - `range(1, 5)` -> 1, 2, 3, 4
- `range(start, stop, step)`: 每次加 step（步长）。
    - `range(1, 10, 2)` -> 1, 3, 5, 7, 9

## 3. for 循环基本结构
```python
for i in range(5):
    print(i)
```
- `i` 是循环变量，每次循环会自动变成 `range` 里的下一个数。
- 循环体（缩进部分）会被重复执行。

## 4. 累加求和案例
计算 1 + 2 + ... + 100 的和。
```python
total = 0           # 定义一个累加器
for i in range(1, 101): # 1 到 100
    total = total + i
print(total)        # 5050
```

## 5. 易错点
- `range(5)` 是从 0 开始，到 4 结束，不包含 5。
- 循环结束后，循环变量 `i` 会保留最后一次的值。

## 6. 遍历字符串和列表
`for` 不只能配合 `range`，还能遍历可迭代对象。

```python
for ch in "Python":
    print(ch)
```

```python
names = ["Tom", "Amy", "Jack"]
for name in names:
    print(name)
```

## 7. 倒序循环
```python
for i in range(5, 0, -1):
    print(i)
```

输出 `5, 4, 3, 2, 1`。

## 8. 嵌套循环
```python
for i in range(3):
    for j in range(2):
        print(i, j)
```

嵌套循环常用于表格、坐标、二维列表。它也常意味着更高的时间复杂度。

## 9. 小练习
1. 打印 1 到 10
2. 打印 10 到 1
3. 输出字符串 `"GESP"` 的每个字符
4. 求 1 到 100 中所有偶数的和
"""
)

Quiz.objects.create(
    lesson=l4_1,
    question="range(1, 5) 生成的序列是？",
    option_a="1, 2, 3, 4, 5",
    option_b="1, 2, 3, 4",
    option_c="0, 1, 2, 3, 4",
    option_d="1, 2, 3",
    correct_answer="B",
    explanation="range 包含起始值，不包含结束值（包头不包尾）。"
)

Quiz.objects.create(
    lesson=l4_1,
    question="range(5) 会循环几次？",
    option_a="4次",
    option_b="5次",
    option_c="6次",
    option_d="0次",
    correct_answer="B",
    explanation="0, 1, 2, 3, 4 共 5 个数。"
)

Quiz.objects.create(
    lesson=l4_1,
    question="for i in range(2, 5): print(i) 的输出是？",
    option_a="2 3 4 5",
    option_b="2 3 4",
    option_c="1 2 3 4",
    option_d="3 4 5",
    correct_answer="B",
    explanation="从 2 开始，到 5 结束（不含 5）。"
)

Quiz.objects.create(
    lesson=l4_1,
    question="range(0, 10, 2) 生成的数不包括？",
    option_a="0",
    option_b="8",
    option_c="10",
    option_d="6",
    correct_answer="C",
    explanation="10 是结束值，不包含。"
)

Quiz.objects.create(
    lesson=l4_1,
    question="for 循环可以遍历字符串吗？",
    option_a="可以",
    option_b="不可以",
    option_c="只能遍历数字",
    option_d="只能遍历列表",
    correct_answer="A",
    explanation="字符串也是可迭代对象，会逐个字符遍历。"
)

Quiz.objects.create(
    lesson=l4_1,
    question="如何让 range 倒序生成数字？",
    option_a="range(10, 0)",
    option_b="range(10, 0, -1)",
    option_c="range(0, 10, -1)",
    option_d="reverse(range(10))",
    correct_answer="B",
    explanation="步长设为负数。"
)

Quiz.objects.create(
    lesson=l4_1,
    question="for i in range(3): print('Hi') 会打印几次 Hi？",
    option_a="2",
    option_b="3",
    option_c="4",
    option_d="0",
    correct_answer="B",
    explanation="0, 1, 2 共 3 次。"
)

Quiz.objects.create(
    lesson=l4_1,
    question="循环变量 i 在循环结束后还能访问吗？",
    option_a="不能",
    option_b="能，保留最后一次的值",
    option_c="能，值重置为 0",
    option_d="报错",
    correct_answer="B",
    explanation="Python 循环变量作用域泄露到外部。"
)

Quiz.objects.create(
    lesson=l4_1,
    question="判断题：range() 函数生成的对象是一个列表。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，Python 3 中 range 返回的是一个 range 对象（生成器），不是列表。"
)

# 4.2 while 循环
l4_2 = create_lesson(
    chapter=ch4, title="4.2 While 循环", order=2, lesson_type='code',
    code_challenge_prompt="# 使用 while 循环打印 5 到 1\nn = 5\nwhile n > 0:\n    print(n)\n    n -= 1",
    content="""# 4.2 While 循环

## 1. 什么是 while 循环？
`for` 循环适合“已知次数”的循环，而 `while` 循环适合“当满足条件时”一直执行，直到条件不满足。

## 2. 基本结构
```python
while 条件:
    代码块
```
只要条件为 `True`，代码块就会一直执行。

## 3. 示例：倒计时
```python
n = 5
while n > 0:
    print(n)
    n = n - 1  # 重要！必须改变 n 的值，否则会变成死循环
print("发射！")
```

## 4. 死循环 (Dead Loop)
如果条件永远为真，循环永远停不下来，程序就卡死了。
```python
# ❌ 危险代码
while True:
    print("停不下来了")
```
如果不小心写了死循环，按 `Ctrl + C` 强制停止。

## 5. 什么时候用 while？
- 不知道具体要循环多少次。
- 比如：一直输入密码，直到输对为止。

## 6. 输入直到正确
```python
password = ""
while password != "123456":
    password = input("请输入密码：")
print("登录成功")
```

这种场景不知道用户会输错几次，所以 `while` 更自然。

## 7. while 和 for 怎么选
- 已知循环次数：优先 `for`
- 不知道次数，只知道停止条件：优先 `while`

例如：
- 打印 10 次：`for`
- 一直猜数字直到猜对：`while`

## 8. while + else
Python 的 `while` 也可以配合 `else`：

```python
n = 3
while n > 0:
    print(n)
    n -= 1
else:
    print("循环正常结束")
```

如果循环不是被 `break` 打断，`else` 会执行。

## 9. 小练习
写一个猜数字程序：
1. 答案固定为 `7`
2. 用户反复输入数字
3. 猜对后输出“猜对了”
"""
)

Quiz.objects.create(
    lesson=l4_2,
    question="while 循环结束的条件是？",
    option_a="循环次数达到上限",
    option_b="条件变为 False",
    option_c="遇到 print 语句",
    option_d="条件变为 True",
    correct_answer="B",
    explanation="当 while 后面的条件判断为 False 时，循环终止。"
)

Quiz.objects.create(
    lesson=l4_2,
    question="n = 3; while n > 0: n -= 1; print(n) 最后输出？",
    option_a="3",
    option_b="0",
    option_c="1",
    option_d="2",
    correct_answer="B",
    explanation="循环执行 3 次，n 依次变为 2, 1, 0。"
)

Quiz.objects.create(
    lesson=l4_2,
    question="如何避免 while 循环变成死循环？",
    option_a="不写条件",
    option_b="在循环体内改变条件变量",
    option_c="使用 for 循环代替",
    option_d="使用 break",
    correct_answer="B",
    explanation="必须确保条件最终会变为 False。"
)

Quiz.objects.create(
    lesson=l4_2,
    question="while True: 表示什么？",
    option_a="无限循环",
    option_b="循环一次",
    option_c="不循环",
    option_d="报错",
    correct_answer="A",
    explanation="条件永远为真。"
)

Quiz.objects.create(
    lesson=l4_2,
    question="Ctrl + C 的作用是？",
    option_a="复制",
    option_b="粘贴",
    option_c="强制中断程序",
    option_d="清屏",
    correct_answer="C",
    explanation="在终端中用于中断运行中的程序（如死循环）。"
)

Quiz.objects.create(
    lesson=l4_2,
    question="while 循环适合什么场景？",
    option_a="已知循环次数",
    option_b="未知循环次数，只知停止条件",
    option_c="遍历列表",
    option_d="遍历字典",
    correct_answer="B",
    explanation="条件控制循环。"
)

Quiz.objects.create(
    lesson=l4_2,
    question="i = 0; while i < 3: print(i); i += 1 输出？",
    option_a="0 1 2",
    option_b="1 2 3",
    option_c="0 1 2 3",
    option_d="1 2",
    correct_answer="A",
    explanation="0, 1, 2。"
)

Quiz.objects.create(
    lesson=l4_2,
    question="while 0: print('Hi') 会执行吗？",
    option_a="会",
    option_b="不会",
    option_c="报错",
    option_d="无限执行",
    correct_answer="B",
    explanation="0 是 False，循环体不会执行。"
)

Quiz.objects.create(
    lesson=l4_2,
    question="判断题：while 循环可以完全替代 for 循环。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，虽然有时候不如 for 方便，但功能上是覆盖的。"
)

# 4.3 循环控制
l4_3 = create_lesson(
    chapter=ch4, title="4.3 break 与 continue", order=3, lesson_type='text',
    code_challenge_prompt="# 寻找第一个能被 7 整除的数（大于 100）\nfor i in range(100, 200):\n    if i % 7 == 0:\n        print(f'找到了: {i}')\n        break",
    content="""# 4.3 循环控制：break 与 continue

有时候我们需要中途控制循环的行为。

## 1. break (中断)
**立即结束整个循环**，跳出循环体，执行后面的代码。

**案例**：在 1 到 100 中找第一个能被 17 整除的数。
```python
for i in range(1, 101):
    if i % 17 == 0:
        print(i)
        break  # 找到了就停止，不用再往后找了
```

## 2. continue (继续/跳过)
**跳过本次循环剩余的代码**，直接开始下一次循环。

**案例**：逢 7 过（打印 1-10，遇到 7 跳过）。
```python
for i in range(1, 11):
    if i == 7:
        continue  # 跳过 7，不执行下面的 print
    print(i)
```

## 3. 对比总结
- `break`：彻底罢工，不干了。
- `continue`：这一轮先休息，下一轮继续干。

## 4. 循环中的 else (进阶)
Python 的循环可以带 `else`，当循环**正常结束**（没有被 `break` 打断）时执行。
```python
# 判断素数
n = 13
for i in range(2, n):
    if n % i == 0:
        print("不是素数")
        break
else:
    print("是素数") # 只有循环完整走完没发现因子，才执行这里
```

## 5. break 常见场景
- 找到目标后停止搜索
- 用户输入 `q` 后退出
- 检测到错误条件后提前结束

```python
while True:
    cmd = input("请输入命令：")
    if cmd == "q":
        break
```

## 6. continue 常见场景
- 跳过不合格数据
- 跳过空字符串
- 跳过某些特殊值

```python
scores = [90, -1, 80, -1, 70]
for score in scores:
    if score == -1:
        continue
    print(score)
```

## 7. 嵌套循环里的 break
`break` 只会跳出它所在的那一层循环。

```python
for i in range(3):
    for j in range(3):
        if j == 1:
            break
        print(i, j)
```

外层循环仍会继续。

## 8. 易错点
- `break` 是结束循环，不是结束整个程序
- `continue` 是跳过本轮，不是跳出循环
- 循环 `else` 只有未被 `break` 打断时才执行
- 嵌套循环里要分清控制的是哪一层

## 9. 小练习
遍历 1 到 50：
1. 遇到能被 3 整除的数跳过
2. 遇到第一个大于 30 且能被 7 整除的数就停止
"""
)

Quiz.objects.create(
    lesson=l4_3,
    question="在循环中执行 break 语句会发生什么？",
    option_a="跳过本次循环",
    option_b="终止整个循环",
    option_c="暂停程序",
    option_d="没有任何反应",
    correct_answer="B",
    explanation="break 用于立即终止当前所在的循环结构。"
)

Quiz.objects.create(
    lesson=l4_3,
    question="continue 语句的作用是？",
    option_a="终止循环",
    option_b="跳过本次循环剩余代码，进入下一次循环",
    option_c="退出程序",
    option_d="暂停循环",
    correct_answer="B",
    explanation="跳过本次，继续下次。"
)

Quiz.objects.create(
    lesson=l4_3,
    question="for i in range(5): if i == 2: break; print(i) 输出？",
    option_a="0 1 2 3 4",
    option_b="0 1",
    option_c="0 1 2",
    option_d="0 1 3 4",
    correct_answer="B",
    explanation="当 i 为 2 时 break，打印了 0 和 1。"
)

Quiz.objects.create(
    lesson=l4_3,
    question="for i in range(5): if i == 2: continue; print(i) 输出？",
    option_a="0 1 2 3 4",
    option_b="0 1 3 4",
    option_c="0 1",
    option_d="2 3 4",
    correct_answer="B",
    explanation="跳过了 2。"
)

Quiz.objects.create(
    lesson=l4_3,
    question="break 可以用在 if 语句中吗？",
    option_a="可以",
    option_b="不可以",
    option_c="只能在循环中的 if 里",
    option_d="只能在函数中的 if 里",
    correct_answer="C",
    explanation="break 必须在循环体内，通常配合 if 使用。"
)

Quiz.objects.create(
    lesson=l4_3,
    question="循环中的 else 块什么时候执行？",
    option_a="每次循环执行",
    option_b="break 执行时",
    option_c="循环正常结束（未被 break 中断）时",
    option_d="永远不执行",
    correct_answer="C",
    explanation="Python 循环特有语法。"
)

Quiz.objects.create(
    lesson=l4_3,
    question="嵌套循环中，break 会跳出几层循环？",
    option_a="所有层",
    option_b="当前这一层",
    option_c="最外层",
    option_d="2层",
    correct_answer="B",
    explanation="break 只影响最近的一层循环。"
)

Quiz.objects.create(
    lesson=l4_3,
    question="pass 语句的作用是？",
    option_a="终止循环",
    option_b="跳过循环",
    option_c="占位，什么都不做",
    option_d="报错",
    correct_answer="C",
    explanation="空语句，保持语法完整。"
)

Quiz.objects.create(
    lesson=l4_3,
    question="判断题：continue 语句后面的代码在当次循环中不会被执行。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，直接跳到下一次循环判断。"
)

# ==========================================
# Course 2: GESP 2级 - 逻辑进阶
# ==========================================
print("正在创建 GESP 2级 课程...")
c2, _ = Course.objects.get_or_create(
    title="GESP 2级：逻辑进阶",
    description="深入掌握 Python 数据容器。重点讲解列表（List）、字符串（String）、元组（Tuple）、字典（Dictionary）、集合（Set）以及常见容器选型思路，对应 GESP 二级考纲。",
    defaults={'order': 2}
)

ch2_1, _ = Chapter.objects.get_or_create(course=c2, title="第1章：列表 List", defaults={'order': 1})

# 1.1 列表基础
l2_1_1 = create_lesson(
    chapter=ch2_1, title="1.1 列表的定义与索引", order=1, lesson_type='text',
    code_challenge_prompt="# 创建一个包含 'Spring', 'Summer', 'Autumn', 'Winter' 的列表，并打印 Summer\nseasons = ['Spring', 'Summer', 'Autumn', 'Winter']\nprint(seasons[1])",
    content="""# 1.1 列表的定义与索引

## 1. 为什么需要列表？
如果我们要存储全班 50 个同学的名字，定义 50 个变量（`name1`, `name2`...）太麻烦了。
列表（List）就像一个**大书包**，可以一次装下很多数据。

## 2. 定义列表
使用方括号 `[]`，元素之间用逗号 `,` 隔开。
```python
names = ["Alice", "Bob", "Charlie"]
numbers = [1, 2, 3, 4, 5]
empty_list = []  # 空列表
```

## 3. 索引 (Index) - 访问元素
列表里的每个元素都有一个编号，叫**索引**。
**重点**：索引从 **0** 开始！

```python
fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple (第1个)
print(fruits[1])  # banana (第2个)
```

## 4. 负数索引
Python 允许倒着数：
- `-1` 表示最后一个。
- `-2` 表示倒数第二个。

```python
print(fruits[-1]) # cherry
```

## 5. 切片 (Slicing) - 获取一部分
语法：`列表[start:end]` (包头不包尾)
```python
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])  # [1, 2, 3]
print(nums[:3])   # [0, 1, 2] (从头开始)
print(nums[3:])   # [3, 4, 5] (直到最后)
```

## 6. 引用与拷贝
列表是可变对象，这意味着“变量名”和“列表本体”要分开理解。

```python
a = [1, 2, 3]
b = a
b[0] = 9
print(a)  # [9, 2, 3]
```

这里不是 `b` 复制出了一份新列表，而是 `a` 和 `b` 指向同一个列表。

如果想要复制一份，可以这样做：

```python
a = [1, 2, 3]
b = a[:]
b[0] = 9
print(a)  # [1, 2, 3]
print(b)  # [9, 2, 3]
```

## 7. 二维列表示意
列表里的元素还可以继续是列表。

```python
table = [
    [95, 88, 76],
    [90, 91, 92]
]
print(table[0][1])  # 88
```

这就像一个小表格：
- 第一层索引：第几行
- 第二层索引：第几列

## 8. 常见错误
### 错误 A：把第一个元素当成索引 1
Python 索引从 0 开始，这是最常见的初学者错误。

### 错误 B：取超出范围的索引
```python
lst = [10, 20, 30]
# print(lst[3])  # 会报错
```

合法索引只有 `0, 1, 2`。

## 9. 列表适合什么问题？
当你遇到这些需求时，列表通常是首选：
- 有一串按顺序保存的数据
- 需要根据位置访问元素
- 后面还可能继续增删改

## 10. 本节总结
这一节要真正掌握的是：
- 列表会按顺序保存多个数据
- 索引从 0 开始
- 可以用切片取出一部分
- 变量名复制不等于真正拷贝列表
"""
)

# 5 MCQs + 2 True/False
# MCQ 1
Quiz.objects.create(
    lesson=l2_1_1,
    question="a = [10, 20, 30, 40]，a[-1] 的值是？",
    option_a="10",
    option_b="40",
    option_c="30",
    option_d="报错",
    correct_answer="B",
    explanation="负数索引 -1 表示列表的最后一个元素。"
)
# MCQ 2
Quiz.objects.create(
    lesson=l2_1_1,
    question="fruits = ['apple', 'banana', 'orange']，fruits[1] 是？",
    option_a="apple",
    option_b="banana",
    option_c="orange",
    option_d="报错",
    correct_answer="B",
    explanation="索引从0开始，1代表第二个元素。"
)
# MCQ 3
Quiz.objects.create(
    lesson=l2_1_1,
    question="lst = [1, 2, 3, 4, 5]，lst[1:3] 的结果是？",
    option_a="[2, 3]",
    option_b="[1, 2, 3]",
    option_c="[2, 3, 4]",
    option_d="[1, 2]",
    correct_answer="A",
    explanation="切片是左闭右开区间，索引1和2的元素被取出。"
)
# MCQ 4
Quiz.objects.create(
    lesson=l2_1_1,
    question="空列表如何定义？",
    option_a="list()",
    option_b="[]",
    option_c="{}",
    option_d="A和B都可以",
    correct_answer="D",
    explanation="[] 和 list() 都可以创建空列表，{} 是空字典。"
)
# MCQ 5
Quiz.objects.create(
    lesson=l2_1_1,
    question="lst = [1, 2, 3]，len(lst) 的值是？",
    option_a="2",
    option_b="3",
    option_c="4",
    option_d="0",
    correct_answer="B",
    explanation="len() 函数返回列表的元素个数。"
)
# T/F 1
Quiz.objects.create(
    lesson=l2_1_1,
    question="判断题：Python 列表的索引可以是从 1 开始。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，Python 列表索引总是从 0 开始。"
)
# T/F 2
Quiz.objects.create(
    lesson=l2_1_1,
    question="判断题：列表可以包含不同类型的数据，例如 [1, 'hello', True]。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，Python 列表是异构的，可以存储不同类型的数据。"
)

Quiz.objects.create(
    lesson=l2_1_1,
    question="如何创建一个包含 1 到 5 的列表？",
    option_a="[1-5]",
    option_b="list(1, 5)",
    option_c="list(range(1, 6))",
    option_d="range(1, 5)",
    correct_answer="C",
    explanation="list() 可以将 range 对象转换为列表。"
)

Quiz.objects.create(
    lesson=l2_1_1,
    question="a = [1, 2, 3]; b = a; b[0] = 9; a[0] 的值是？",
    option_a="1",
    option_b="9",
    option_c="报错",
    option_d="3",
    correct_answer="B",
    explanation="列表是引用传递，a 和 b 指向同一个对象。"
)

Quiz.objects.create(
    lesson=l2_1_1,
    question="判断题：切片操作 a[:] 会创建列表的一个浅拷贝。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，a[:] 返回一个新的列表对象。"
)


# 1.2 列表操作
l2_1_2 = create_lesson(
    chapter=ch2_1, title="1.2 列表的增删改查", order=2, lesson_type='code',
    code_challenge_prompt="# 列表操作挑战\nnums = [1, 2, 3]\nnums.append(4)\nnums[0] = 100\nprint(nums)",
    content="""# 1.2 列表的增删改查

列表是**可变**的（Mutable），我们可以随意修改它。

## 1. 增加 (Add)
- `append(x)`: 在末尾追加一个元素。
- `insert(index, x)`: 在指定位置插入。

```python
lst = ["a", "b"]
lst.append("c")      # ["a", "b", "c"]
lst.insert(0, "start") # ["start", "a", "b", "c"]
```

## 2. 删除 (Delete)
- `pop(index)`: 弹出指定位置的元素（默认最后一个），并**返回**它。
- `remove(x)`: 删除第一个出现的 `x`（如果不存会报错）。
- `del lst[index]`: 关键字删除。

```python
lst = ["a", "b", "c", "b"]
lst.pop()        # 删除 "b"
lst.remove("b")  # 删除第一个 "b"
```

## 3. 修改 (Update)
直接通过索引赋值。
```python
lst = [1, 2, 3]
lst[0] = 99      # [99, 2, 3]
```

## 4. 查询与统计
- `len(lst)`: 列表长度（元素个数）。
- `x in lst`: 判断 x 是否在列表中（返回 True/False）。
- `lst.count(x)`: 统计 x 出现的次数。
- `lst.index(x)`: 查找 x 第一次出现的位置。

```python
nums = [1, 2, 3, 1]
print(len(nums))     # 4
print(1 in nums)     # True
print(nums.count(1)) # 2
```

## 5. remove、pop、del 的区别
这三个删除方式很容易混淆。

### `remove(x)`
- 按“值”删除
- 删除第一个匹配项

### `pop(index)`
- 按“位置”删除
- 会返回被删除的元素

### `del lst[index]`
- 也是按位置删除
- 但不返回元素

如果你需要“删掉并顺手拿到这个值”，优先想到 `pop()`。

## 6. append vs extend
初学者经常把它们搞混。

```python
lst = [1, 2]
lst.append([3, 4])
print(lst)  # [1, 2, [3, 4]]
```

`append()` 是把整个对象当成一个元素塞进去。

```python
lst = [1, 2]
lst.extend([3, 4])
print(lst)  # [1, 2, 3, 4]
```

`extend()` 则是把另一个可迭代对象里的元素逐个加入。

## 7. 修改与插入的区别
- 修改：原位置有内容，直接替换
- 插入：保留原内容，把新元素塞进去

```python
lst = [10, 20, 30]
lst[1] = 99         # [10, 99, 30]
lst.insert(1, 77)   # [10, 77, 99, 30]
```

## 8. 一个真实场景
比如你在做一个待办清单程序：

```python
todos = ["做作业", "背单词"]
todos.append("练钢琴")
todos.remove("背单词")
print(todos)
```

列表最强的地方，就在于它很适合表示“会变化的一串数据”。

## 9. 本节总结
列表操作最核心的思路是：
- 想加内容：`append / insert`
- 想删内容：`remove / pop / del`
- 想改内容：索引赋值
- 想查内容：`in / count / index / len`
"""
)

# 5 MCQs + 2 T/F
# MCQ 1
Quiz.objects.create(
    lesson=l2_1_2,
    question="列表 list = [1, 2, 3]，执行 list.append(4) 后，list 是？",
    option_a="[4, 1, 2, 3]",
    option_b="[1, 2, 3, 4]",
    option_c="[1, 2, 3]",
    option_d="报错",
    correct_answer="B",
    explanation="append() 方法会将元素添加到列表的末尾。"
)
# MCQ 2
Quiz.objects.create(
    lesson=l2_1_2,
    question="lst = [10, 20, 30]，执行 lst.pop() 后，lst 是？",
    option_a="[20, 30]",
    option_b="[10, 20]",
    option_c="[10]",
    option_d="[]",
    correct_answer="B",
    explanation="pop() 默认删除并返回最后一个元素。"
)
# MCQ 3
Quiz.objects.create(
    lesson=l2_1_2,
    question="lst = [1, 2, 3]，执行 lst.insert(1, 9) 后，lst 是？",
    option_a="[1, 9, 2, 3]",
    option_b="[9, 1, 2, 3]",
    option_c="[1, 2, 9, 3]",
    option_d="报错",
    correct_answer="A",
    explanation="insert(1, 9) 在索引 1 的位置插入 9。"
)
# MCQ 4
Quiz.objects.create(
    lesson=l2_1_2,
    question="lst = ['a', 'b', 'c', 'b']，执行 lst.remove('b') 后，lst 是？",
    option_a="['a', 'c', 'b']",
    option_b="['a', 'b', 'c']",
    option_c="['a', 'c']",
    option_d="报错",
    correct_answer="A",
    explanation="remove() 只删除第一个匹配的元素。"
)
# MCQ 5
Quiz.objects.create(
    lesson=l2_1_2,
    question="如何判断 5 是否在列表 nums 中？",
    option_a="nums.has(5)",
    option_b="5 in nums",
    option_c="nums.contains(5)",
    option_d="exist(5, nums)",
    correct_answer="B",
    explanation="in 关键字用于判断元素是否存在。"
)
# T/F 1
Quiz.objects.create(
    lesson=l2_1_2,
    question="判断题：使用 remove(x) 删除元素时，如果 x 不在列表中，程序会报错。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，remove 不存在的元素会抛出 ValueError。"
)
# T/F 2
Quiz.objects.create(
    lesson=l2_1_2,
    question="判断题：列表是不可变的，一旦创建就不能修改。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，列表是可变的 (Mutable)。"
)

Quiz.objects.create(
    lesson=l2_1_2,
    question="如何清空列表 list？",
    option_a="list.clear()",
    option_b="list.empty()",
    option_c="list = []",
    option_d="del list",
    correct_answer="A",
    explanation="clear() 方法用于清空列表内容。"
)

Quiz.objects.create(
    lesson=l2_1_2,
    question="list.reverse() 的作用是？",
    option_a="排序",
    option_b="反转列表",
    option_c="复制列表",
    option_d="删除列表",
    correct_answer="B",
    explanation="原地反转列表元素顺序。"
)

Quiz.objects.create(
    lesson=l2_1_2,
    question="list.sort() 默认是？",
    option_a="升序",
    option_b="降序",
    option_c="不排序",
    option_d="随机排序",
    correct_answer="A",
    explanation="默认从小到大排序。"
)

ch2_2, _ = Chapter.objects.get_or_create(course=c2, title="第2章：字符串进阶", defaults={'order': 2})

# 2.1 字符串操作
l2_2_1 = create_lesson(
    chapter=ch2_2, title="2.1 字符串常用方法", order=1, lesson_type='text',
    code_challenge_prompt="# 将字符串 ' python ' 去掉首尾空格并转为大写\ns = ' python '\nprint(s.strip().upper())",
    content="""# 2.1 字符串常用方法

字符串和列表很像，也有索引和切片，但字符串是**不可变**的（不能直接修改某个字符）。

## 1. 为什么字符串方法这么重要？
在真实编程里，很多输入的数据本质上都是字符串：
- 用户输入的姓名
- 一行一行的文本
- 逗号分隔的数据
- 文件中的内容

所以学会字符串处理，等于学会“整理文字数据”的基础能力。

## 2. 大小写转换
- `s.upper()`：全大写
- `s.lower()`：全小写
- `s.capitalize()`：首字母大写
- `s.title()`：每个单词首字母大写

```python
s = "hello python"
print(s.upper())      # HELLO PYTHON
print(s.capitalize()) # Hello python
print(s.title())      # Hello Python
```

## 3. 查找与替换
- `s.find(sub)`：查找子串位置，找不到返回 `-1`
- `s.count(sub)`：统计某段内容出现了多少次
- `s.replace(old, new)`：把旧内容替换成新内容

```python
s = "I love Python, Python is fun"
print(s.find("Python"))       # 7
print(s.count("Python"))      # 2
print(s.replace("Python", "Coding"))
```

## 4. 分割与合并 (重点)
- `s.split(sep)`：把字符串切成列表
- `sep.join(list)`：把列表拼成字符串

```python
s = "apple,banana,orange"
lst = s.split(",")   # ['apple', 'banana', 'orange']
print("-".join(lst)) # apple-banana-orange
```

这种“拆开再重组”的过程，在整理数据时特别常见。

## 5. 去除空白
- `s.strip()`：去除首尾空格或换行
- `s.lstrip()`：只去左边
- `s.rstrip()`：只去右边

```python
s = "  hello  "
print(s.strip())   # hello
print(s.lstrip())  # hello  
print(s.rstrip())  #   hello
```

## 6. 判断字符串特征
- `s.isalpha()`：是否全是字母
- `s.isdigit()`：是否全是数字
- `s.isalnum()`：是否只由字母和数字组成
- `sub in s`：检查子串是否存在

```python
print("abc".isalpha())   # True
print("123".isdigit())   # True
print("a1b2".isalnum())  # True
print("py" in "python")  # True
```

## 7. 常见误区
### 误区 A：字符串可以像列表一样改字符
```python
s = "cat"
# s[0] = "b"  # 会报错
```

### 误区 B：find 找不到会报错
不会。它会返回 `-1`，所以很适合配合判断使用。

## 8. 一个实际例子
假设用户输入了：

```python
name = "  alice  "
```

我们可能会这样处理：

```python
name = name.strip().title()
print(name)  # Alice
```

这就是字符串方法在真实场景中的价值：把“脏数据”整理成整洁的数据。

## 9. 方法组合思维
字符串方法最重要的不只是“会一个个背下来”，而是学会把它们串起来用。

例如下面这段输入：

```python
raw = "  python,java,c++  "
```

如果我们想得到一个更整洁的列表，可以这样做：

```python
items = raw.strip().split(",")
print(items)  # ['python', 'java', 'c++']
```

这里其实连续做了两步：
- 先 `strip()` 清除首尾无用空格
- 再 `split()` 按逗号拆开

很多题目的关键，不是某一个方法很难，而是你能不能想到“先做什么、后做什么”。

## 10. 小练习思路
### 例 1：整理邮箱输入
```python
email = "  student@example.com  "
email = email.strip().lower()
print(email)
```

### 例 2：统计单词出现次数
```python
text = "python python java"
print(text.count("python"))  # 2
```

### 例 3：把名字列表变成一句话
```python
names = ["Tom", "Amy", "Lily"]
print("、".join(names))
```

## 11. 本节总结
这一节真正要掌握的不是“方法名字很多”，而是这三类能力：
- 知道该用哪个方法处理哪类问题
- 能把多个方法组合起来使用
- 能把原始字符串一步步整理成有用的信息
"""
)

# 5 MCQs + 2 T/F
# MCQ 1
Quiz.objects.create(
    lesson=l2_2_1,
    question="'1,2,3'.split(',') 的结果是？",
    option_a="[1, 2, 3]",
    option_b="['1', '2', '3']",
    option_c="'1 2 3'",
    option_d="['1,2,3']",
    correct_answer="B",
    explanation="split 返回一个列表，且元素都是字符串类型。"
)
# MCQ 2
Quiz.objects.create(
    lesson=l2_2_1,
    question="s = 'Hello World'，s.find('o') 返回？",
    option_a="4",
    option_b="5",
    option_c="7",
    option_d="4 和 7",
    correct_answer="A",
    explanation="find 返回第一个匹配项的索引，'o' 在索引 4。"
)
# MCQ 3
Quiz.objects.create(
    lesson=l2_2_1,
    question="'--'.join(['a', 'b', 'c']) 的结果是？",
    option_a="'abc'",
    option_b="'a-b-c'",
    option_c="'a--b--c'",
    option_d="['a--b--c']",
    correct_answer="C",
    explanation="join 使用指定的连接符连接列表元素。"
)
# MCQ 4
Quiz.objects.create(
    lesson=l2_2_1,
    question="' Hello '.strip() 的结果是？",
    option_a="'Hello '",
    option_b="' Hello'",
    option_c="'Hello'",
    option_d="报错",
    correct_answer="C",
    explanation="strip() 去除首尾的空白字符。"
)
# MCQ 5
Quiz.objects.create(
    lesson=l2_2_1,
    question="'abc'.upper() 的结果是？",
    option_a="'Abc'",
    option_b="'ABC'",
    option_c="'abc'",
    option_d="报错",
    correct_answer="B",
    explanation="upper() 将所有字符转换为大写。"
)
# T/F 1
Quiz.objects.create(
    lesson=l2_2_1,
    question="判断题：字符串是不可变的，不能通过 s[0] = 'a' 修改。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，字符串是不可变类型 (Immutable)。"
)
# T/F 2
Quiz.objects.create(
    lesson=l2_2_1,
    question="判断题：s.find('z') 如果找不到 'z' 会报错。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，find 找不到时返回 -1，不会报错。"
)

Quiz.objects.create(
    lesson=l2_2_1,
    question="'a' in 'apple' 的结果是？",
    option_a="True",
    option_b="False",
    option_c="1",
    option_d="0",
    correct_answer="A",
    explanation="in 运算符用于检查子串是否存在。"
)

Quiz.objects.create(
    lesson=l2_2_1,
    question="'abc'.isalpha() 的结果是？",
    option_a="True",
    option_b="False",
    option_c="Error",
    option_d="None",
    correct_answer="A",
    explanation="isalpha() 检查字符串是否只包含字母。"
)

Quiz.objects.create(
    lesson=l2_2_1,
    question="'123'.isdigit() 的结果是？",
    option_a="True",
    option_b="False",
    option_c="Error",
    option_d="None",
    correct_answer="A",
    explanation="isdigit() 检查字符串是否只包含数字。"
)


# 2.2 ASCII 码
l2_2_2 = create_lesson(
    chapter=ch2_2, title="2.2 字符与编码 (ASCII)", order=2, lesson_type='text',
    code_challenge_prompt="# 打印字符 'A' 的 ASCII 码\nprint(ord('A'))",
    content="""# 2.2 字符与编码 (ASCII)

## 1. 计算机只认识数字
在计算机内部，所有的字符（'a', 'A', '1', '!'）都存储为数字。这个对应的规则就是编码表，最常用的是 ASCII 码。

## 2. 两个重要函数 (GESP 考点)
- `ord(char)`: 字符 -> 数字 (Ordinal)
- `chr(number)`: 数字 -> 字符 (Character)

```python
print(ord('A'))  # 65
print(ord('a'))  # 97
print(ord('0'))  # 48

print(chr(66))   # 'B'
```

## 3. 常见 ASCII 码规律
- **数字**：'0' (48) ... '9' (57)
- **大写字母**：'A' (65) ... 'Z' (90)
- **小写字母**：'a' (97) ... 'z' (122)
- **大小写转换**：小写比大写大 32。
  `'a' - 'A' = 32`

## 4. 字符运算的直觉
为什么知道 ASCII 很有用？因为我们可以理解很多“看起来神奇”的比较结果。

例如：
- `'B'` 比 `'A'` 大，因为 66 > 65
- `'a'` 比 `'Z'` 大，因为 97 > 90
- `'0'` 到 `'9'` 是连续的一段数字字符

## 5. 字符串比较
字符串比较实际上是按字符一个一个比较 ASCII 码的大小。
```python
print('a' > 'A') # True (97 > 65)
print('apple' > 'banana') # False (比较第一个字母 'a' < 'b')
print('abc' < 'abd')      # True (比较到第三个字符 c < d)
```

## 6. 一个容易错的点
```python
print('10' > '2')  # False
```

这不是在比数字 10 和 2，而是在比字符串：
- 先比较 `'1'` 和 `'2'`
- 因为 `'1'` 更小，所以结果是 False

## 7. 大小写与编码
```python
print(ord('A'))  # 65
print(ord('a'))  # 97
```

这也是为什么：

```python
print('Apple' < 'apple')  # True
```

因为大写字母的 ASCII 码通常比小写字母小。

## 8. ASCII 和 Unicode 的关系
ASCII 只是最早、最基础的编码表，只包含英文字符、数字和常见符号。  
汉字、表情符号等更丰富的字符，一般使用更大的编码体系，比如 Unicode。

在 GESP 二级阶段，重点先掌握：
- `ord()`
- `chr()`
- 字符比较
- 大小写字母和数字字符的编码规律

## 9. 编码与排序的关系
为什么学了 ASCII 以后，很多排序结果 suddenly 就能看懂了？

因为字符串排序底层还是要比较字符编码。

例如：

```python
words = ["apple", "Banana", "cat"]
print(sorted(words))
```

结果中大写字母开头的单词，可能会排在小写字母前面。  
原因不是“英语规则”，而是：
- `'B'` 的 ASCII 更小
- 所以 `"Banana"` 会更靠前

## 10. 实战中的启发
如果你发现字符串排序结果“看起来怪怪的”，先别急着怀疑 Python，先想一想：
- 是不是大小写混在一起了？
- 是不是在按字符比较，而不是按数字比较？

比如：

```python
print(sorted(["2", "10", "1"]))  # ['1', '10', '2']
```

这不是数字从小到大的排序，而是字符串按字符比较的排序。

## 11. 本节总结
学 ASCII 的目标，不是死记硬背所有编号，而是建立这几个直觉：
- 字符本质上对应数字
- 字符比较本质上是数字比较
- 字符串比较是逐字符比较
- 数字字符串和真正的数字，不是一回事
"""
)

# 5 MCQs + 2 T/F
# MCQ 1
Quiz.objects.create(
    lesson=l2_2_2,
    question="ord('A') 的值是 65，那么 ord('C') 是多少？",
    option_a="66",
    option_b="67",
    option_c="68",
    option_d="97",
    correct_answer="B",
    explanation="ASCII 码是连续的，A=65, B=66, C=67。"
)
# MCQ 2
Quiz.objects.create(
    lesson=l2_2_2,
    question="chr(97) 返回的是？",
    option_a="'A'",
    option_b="'a'",
    option_c="'0'",
    option_d="97",
    correct_answer="B",
    explanation="97 是小写字母 'a' 的 ASCII 码。"
)
# MCQ 3
Quiz.objects.create(
    lesson=l2_2_2,
    question="'b' > 'a' 的结果是？",
    option_a="True",
    option_b="False",
    option_c="Error",
    option_d="None",
    correct_answer="A",
    explanation="字符比较是比较 ASCII 码，'b'(98) > 'a'(97)。"
)
# MCQ 4
Quiz.objects.create(
    lesson=l2_2_2,
    question="数字字符 '0' 的 ASCII 码是？",
    option_a="0",
    option_b="10",
    option_c="48",
    option_d="65",
    correct_answer="C",
    explanation="'0' 的 ASCII 码是 48。"
)
# MCQ 5
Quiz.objects.create(
    lesson=l2_2_2,
    question="小写字母 'a' 和大写字母 'A' 的 ASCII 码差值是多少？",
    option_a="26",
    option_b="32",
    option_c="48",
    option_d="10",
    correct_answer="B",
    explanation="97 - 65 = 32。"
)
# T/F 1
Quiz.objects.create(
    lesson=l2_2_2,
    question="判断题：'10' > '2' 的结果是 True。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，字符串比较是逐个字符比较，'1' < '2'，所以 '10' < '2'。"
)
# T/F 2
Quiz.objects.create(
    lesson=l2_2_2,
    question="判断题：ord() 函数可以将数字转换为对应的字符。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，ord() 是字符转数字，chr() 才是数字转字符。"
)

Quiz.objects.create(
    lesson=l2_2_2,
    question="'Apple' < 'apple' 的结果是？",
    option_a="True",
    option_b="False",
    option_c="Error",
    option_d="None",
    correct_answer="A",
    explanation="'A' (65) < 'a' (97)，所以结果为 True。"
)

Quiz.objects.create(
    lesson=l2_2_2,
    question="ord(' ') (空格) 的值是？",
    option_a="0",
    option_b="32",
    option_c="1",
    option_d="10",
    correct_answer="B",
    explanation="空格的 ASCII 码是 32。"
)

Quiz.objects.create(
    lesson=l2_2_2,
    question="判断题：ASCII 码表中包含了所有汉字。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，ASCII 只有 128 个字符，不包含汉字（汉字在 Unicode 中）。"
)

# 2.3 字符串切片与格式化
l2_2_3 = create_lesson(
    chapter=ch2_2, title="2.3 字符串切片与格式化输出", order=3, lesson_type='text',
    code_challenge_prompt="# 提取字符串 'Python' 的前 3 个字符，并格式化输出一条消息\ns = 'Python'\nprint(s[:3])\nname = 'Tom'\nscore = 95\nprint(f'{name} 的分数是 {score}')",
    content="""# 2.3 字符串切片与格式化输出

## 1. 字符串切片是什么？
切片就是“从一段字符串里取出一部分”。

```python
s = "Python"
print(s[0:2])  # Py
print(s[:3])   # Pyt
print(s[2:])   # thon
print(s[-3:])  # hon
```

## 2. 切片规则回顾
- `s[a:b]`：从索引 `a` 取到 `b` 之前
- 左闭右开：取到前面，不取后面
- 可以省略开头或结尾

## 3. 为什么切片很常用？
因为很多文本处理任务都需要：
- 取前缀
- 取后缀
- 截取中间一段
- 判断某种格式

例如：

```python
filename = "photo.jpg"
print(filename[-4:])  # .jpg
```

## 4. 字符串格式化输出
当我们要把变量嵌入文字中时，就需要格式化输出。

### 方法 A：f-string（推荐）
```python
name = "Tom"
score = 95
print(f"{name} 的分数是 {score}")
```

### 方法 B：字符串拼接
```python
print(name + " 的分数是 " + str(score))
```

## 5. 为什么推荐 f-string？
- 写法更清晰
- 不容易漏掉空格
- 不必手动频繁转换类型

## 6. 实际场景
比如你要生成一句学习反馈：

```python
student = "Amy"
lesson = "字符串进阶"
print(f"{student} 已完成《{lesson}》学习")
```

这就是程序生成自然语言信息的最基础方式。

## 7. 宽度与对齐
有时候我们不仅希望输出“对”，还希望输出“整齐”。

```python
name = "Tom"
score = 95
print(f"{name:>6}")
print(f"{score:0>4}")
```

可以理解为：
- `>6`：右对齐，总宽度 6
- `0>4`：右对齐，不够的地方用 0 补齐

在二级阶段不要求你掌握特别复杂的格式控制，但要知道：  
f-string 不只是“把变量放进去”，也可以控制输出样子。

## 8. 常见格式化错误
### 错误 A：忘记加 f
```python
name = "Tom"
print("{name}")   # 这里只会原样输出
print(f"{name}")  # 这样才会输出变量值
```

### 错误 B：数字和字符串直接拼接
```python
score = 95
# print("score=" + score)  # 报错
print("score=" + str(score))
print(f"score={score}")
```

## 9. 本节总结
这一节你要形成两个核心习惯：
- 看到一段字符串时，会想到能不能用切片提取出想要的部分
- 需要输出变量时，优先想到用 f-string 表达
"""
)
Quiz.objects.create(lesson=l2_2_3, question="'Python'[:2] 的结果是？", option_a="'Py'", option_b="'Pyt'", option_c="'yt'", option_d="'on'", correct_answer="A", explanation="切片左闭右开，取索引 0 和 1。")
Quiz.objects.create(lesson=l2_2_3, question="'Python'[2:] 的结果是？", option_a="'Py'", option_b="'thon'", option_c="'yth'", option_d="'on'", correct_answer="B", explanation="从索引 2 一直到结尾。")
Quiz.objects.create(lesson=l2_2_3, question="'Python'[-3:] 的结果是？", option_a="'Pyt'", option_b="'hon'", option_c="'tho'", option_d="'on'", correct_answer="B", explanation="负索引从后往前数，最后 3 个字符是 hon。")
Quiz.objects.create(lesson=l2_2_3, question="格式化输出最推荐的写法是？", option_a="注释", option_b="f-string", option_c="for 循环", option_d="input", correct_answer="B", explanation="现代 Python 中最常推荐的是 f-string。")
Quiz.objects.create(lesson=l2_2_3, question="f'{name} 的分数是 {score}' 中花括号的作用是？", option_a="写注释", option_b="插入变量值", option_c="定义列表", option_d="定义字典", correct_answer="B", explanation="花括号里可以放变量或表达式。")
Quiz.objects.create(lesson=l2_2_3, question="判断题：切片时右边界位置对应的字符会被取到。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，切片右边界不包含。")
Quiz.objects.create(lesson=l2_2_3, question="判断题：f-string 可以直接把数字变量放进字符串中输出。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，这也是它方便的地方。")
Quiz.objects.create(lesson=l2_2_3, question="'photo.jpg'[-4:] 的结果是？", option_a="'jpg'", option_b="'.jpg'", option_c="'photo'", option_d="'oto.'", correct_answer="B", explanation="最后四个字符是 .jpg。")
Quiz.objects.create(lesson=l2_2_3, question="下列哪项最适合描述切片用途？", option_a="从字符串中截取一部分", option_b="删除变量", option_c="创建循环", option_d="处理异常", correct_answer="A", explanation="切片本质上就是截取子串。")
Quiz.objects.create(lesson=l2_2_3, question="如果 name='Tom'，那么 f'Hello, {name}' 的结果是？", option_a="'Hello, {name}'", option_b="'Hello, Tom'", option_c="'TomHello'", option_d="报错", correct_answer="B", explanation="f-string 会把变量 name 的值替换进去。")

# 2.4 综合实战
l2_2_4 = create_lesson(
    chapter=ch2_2, title="2.4 综合实战：整理学生成绩字符串", order=4, lesson_type='code',
    code_challenge_prompt="""# 已知原始数据如下
raw = " Tom,89 ; Amy,95 ; Lily,100 "

# 目标：
# 1. 去掉首尾空格
# 2. 先按 ; 分割成每位学生的数据
# 3. 再按 , 分离姓名和分数
# 4. 打印格式化结果
print(raw)
""",
    content="""# 2.4 综合实战：整理学生成绩字符串

## 1. 题目背景
真实数据往往不是整整齐齐的。  
比如老师给你一行原始成绩数据：

```python
raw = " Tom,89 ; Amy,95 ; Lily,100 "
```

我们希望把它整理成更清晰的输出。

## 2. 第一步：去除首尾空白
```python
raw = raw.strip()
```

## 3. 第二步：按分号切分
```python
items = raw.split(";")
```

这时每一项还可能带空格，所以要继续处理。

## 4. 第三步：逐个整理
```python
for item in items:
    item = item.strip()
    name, score = item.split(",")
    print(f"{name} 同学的成绩是 {score}")
```

## 5. 这道题练到了什么？
- `strip()`：清理多余空格
- `split()`：拆分字符串
- 变量接收多个结果：`name, score = ...`
- `f-string`：格式化输出

## 6. 为什么这道题重要？
因为它已经非常接近真实的数据处理任务了。  
很多编程题看似复杂，本质上就是：
- 先把字符串拆开
- 再把数据整理好
- 最后按要求输出

## 7. 升级任务：生成成绩报告
如果我们不只是想打印每个人的成绩，还想统计人数与平均分，就可以继续往下做。

```python
raw = " Tom,89 ; Amy,95 ; Lily,100 "
items = raw.strip().split(";")

total = 0
count = 0

for item in items:
    item = item.strip()
    name, score = item.split(",")
    score = int(score)
    total += score
    count += 1
    print(f"{name} 同学的成绩是 {score}")

print(f"平均分是 {total / count}")
```

这一步已经从“字符串整理”进一步走向“基础数据处理”了。

## 8. 易错点总结
### 易错点 A：忘记先 strip
如果不先去掉多余空格，得到的数据就可能带着空格，影响后续处理。

### 易错点 B：split 后的结果还是字符串
```python
score = "89"
```

它虽然看起来像数字，但本质上还是字符串。  
如果要参与数学运算，需要：

```python
score = int(score)
```

### 易错点 C：分隔符写错
如果原始数据用的是 `;`，却写成 `split(",")`，得到的结果就会不对。

## 9. 本节总结
这一节是第 2 章最重要的综合应用课之一。  
它把前面学过的：
- `strip`
- `split`
- 切片与变量拆包
- f-string

放到了同一个真实任务里。  
能把这一题真正理解透，后面很多字符串处理题都会变得更容易。
"""
)
Quiz.objects.create(lesson=l2_2_4, question="处理原始成绩字符串时，第一步更适合先做什么？", option_a="排序", option_b="strip 去掉首尾空格", option_c="转字典", option_d="转集合", correct_answer="B", explanation="原始数据前后有多余空格，先清理最合理。")
Quiz.objects.create(lesson=l2_2_4, question="把 'Tom,89 ; Amy,95' 按 ';' 拆开应使用？", option_a="join", option_b="find", option_c="split", option_d="replace", correct_answer="C", explanation="split 用于按指定分隔符切分字符串。")
Quiz.objects.create(lesson=l2_2_4, question="name, score = item.split(',') 体现了什么写法？", option_a="异常处理", option_b="多变量接收拆分结果", option_c="递归", option_d="布尔判断", correct_answer="B", explanation="split 后得到两个元素，可以分别接收。")
Quiz.objects.create(lesson=l2_2_4, question="格式化输出“Tom 同学的成绩是 89”最推荐的方式是？", option_a="f-string", option_b="continue", option_c="pass", option_d="del", correct_answer="A", explanation="f-string 更直观清晰。")
Quiz.objects.create(lesson=l2_2_4, question="如果 item=' Amy,95 '，先调用哪个方法更适合？", option_a="upper()", option_b="strip()", option_c="isdigit()", option_d="count()", correct_answer="B", explanation="先去掉多余空格，再进一步拆分。")
Quiz.objects.create(lesson=l2_2_4, question="判断题：字符串整理题常常要连续使用多个字符串方法。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，真实题目经常需要组合使用多个方法。")
Quiz.objects.create(lesson=l2_2_4, question="判断题：'Tom,89'.split(',') 会得到一个列表。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，结果类似 ['Tom', '89']。")
Quiz.objects.create(lesson=l2_2_4, question="这类“整理字符串”题最核心的思路是？", option_a="先拆分，再清理，再输出", option_b="先递归，再排序", option_c="先建类，再继承", option_d="先建栈，再出栈", correct_answer="A", explanation="这是字符串数据整理的典型流程。")
Quiz.objects.create(lesson=l2_2_4, question="' Tom,89 '.strip() 的结果是？", option_a="' Tom,89 '", option_b="'Tom,89'", option_c="'Tom'", option_d="'89'", correct_answer="B", explanation="strip 会去掉首尾空格。")
Quiz.objects.create(lesson=l2_2_4, question="字符串综合题最常见的最终目标之一是？", option_a="把无序文本整理成结构化输出", option_b="只打印一个字符", option_c="把所有内容删掉", option_d="强制转元组", correct_answer="A", explanation="真正目的是把原始文本整理成可用数据。")

ch2_3, _ = Chapter.objects.get_or_create(course=c2, title="第3章：常见数据结构", defaults={'order': 3})

l2_3_1 = create_lesson(
    chapter=ch2_3, title="3.1 元组 Tuple：不能随意修改的序列", order=1, lesson_type='text',
    code_challenge_prompt="# 创建一个元组 point，保存平面坐标 (3, 5)\npoint = (3, 5)\nprint(point[0], point[1])",
    content="""# 3.1 元组 Tuple：不能随意修改的序列

## 1. 什么是元组？
元组（Tuple）和列表很像，都是**有序序列**，也都支持索引、切片、遍历。
最大的区别是：**元组创建后不能修改**，所以它适合存放“固定不变”的数据。

```python
point = (3, 5)
rgb = (255, 128, 0)
```

## 2. 为什么需要元组？
- 表示不会变化的数据，例如：坐标、年月日、颜色值。
- 防止程序中被误改。
- 在函数返回多个结果时非常常见。

## 3. 元组的基本操作
```python
point = (3, 5, 8)
print(point[0])   # 3
print(point[-1])  # 8
print(point[1:])  # (5, 8)
```

## 4. 单元素元组
只有一个元素时，后面要加逗号：

```python
a = (5,)      # 这是元组
b = (5)       # 这只是数字 5
```

## 5. 元组和列表的对比
- 列表：可变，适合频繁增删改
- 元组：不可变，适合固定数据

## 6. 易错点
```python
t = (1, 2, 3)
# t[0] = 9   # 会报错，元组不能修改
```

学会判断“数据是否需要变化”，是选择列表还是元组的关键。

## 7. 元组解包
元组非常常见的另一个用途，是“一次返回多个值”。

```python
point = (3, 5)
x, y = point
print(x)  # 3
print(y)  # 5
```

这叫做**解包**。

## 8. 元组适合的真实场景
- 地图上的坐标 `(x, y)`
- 日期 `(year, month, day)`
- 颜色 `(r, g, b)`
- 比赛结果 `(胜, 平, 负)`

这些数据的共同点是：
- 有顺序
- 各位置有固定含义
- 一般不希望随意更改

## 9. 本节总结
元组不是“不能改的列表”这么简单。  
它更像是在告诉别人：
- 这是一组固定结构的数据
- 里面每个位置都有明确意义
"""
)

Quiz.objects.create(lesson=l2_3_1, question="元组和列表最大的区别是什么？", option_a="元组更长", option_b="元组不能修改", option_c="列表不能遍历", option_d="列表不能切片", correct_answer="B", explanation="元组是不可变序列，列表是可变序列。")
Quiz.objects.create(lesson=l2_3_1, question="下列哪个是单元素元组？", option_a="(5)", option_b="[5]", option_c="(5,)", option_d="{5}", correct_answer="C", explanation="单元素元组必须写成 (5,)。")
Quiz.objects.create(lesson=l2_3_1, question="t = (10, 20, 30)，t[-1] 的值是？", option_a="10", option_b="20", option_c="30", option_d="报错", correct_answer="C", explanation="负索引 -1 表示最后一个元素。")
Quiz.objects.create(lesson=l2_3_1, question="元组最适合保存哪类数据？", option_a="每天会变化的购物车", option_b="需要不断插入的数据", option_c="固定不变的坐标信息", option_d="临时空列表", correct_answer="C", explanation="坐标等固定信息适合用元组保存。")
Quiz.objects.create(lesson=l2_3_1, question="判断题：元组支持索引访问。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，元组和列表一样支持索引。")
Quiz.objects.create(lesson=l2_3_1, question="判断题：元组中的元素一旦创建，通常不能直接修改。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，这正是元组的核心特点。")

l2_3_2 = create_lesson(
    chapter=ch2_3, title="3.2 字典 Dictionary：用名字找数据", order=2, lesson_type='code',
    code_challenge_prompt="# 创建一个字典 student，包含 name、age、score 三个键\nstudent = {\n    'name': 'Tom',\n    'age': 12,\n    'score': 95,\n}\nprint(student['name'])",
    content="""# 3.2 字典 Dictionary：用名字找数据

## 1. 为什么列表不够方便？
如果我们用列表保存学生信息：

```python
student = ["Tom", 12, 95]
```

过一会儿就可能忘记：
- 索引 0 是名字？
- 索引 1 是年龄？
- 索引 2 是成绩？

这时更适合使用**字典**。

## 2. 字典的结构
字典由很多组 **键: 值** 组成。

```python
student = {
    "name": "Tom",
    "age": 12,
    "score": 95
}
```

## 3. 访问与修改
```python
print(student["name"])   # Tom
student["score"] = 98
student["city"] = "深圳"
```

## 4. 常用方法
- `dict.keys()`：查看所有键
- `dict.values()`：查看所有值
- `dict.items()`：同时查看键和值
- `"name" in student`：判断键是否存在

## 5. 字典适合什么场景？
- 学生信息
- 商品信息
- 配置参数
- 联系人电话簿

## 6. 一个重要提醒
字典里的键通常应该是**唯一**的，重复键会覆盖旧值。

## 7. get 与 KeyError
如果直接访问一个不存在的键，会报错：

```python
student = {"name": "Tom"}
# print(student["age"])  # KeyError
```

更稳妥的方式是使用 `get()`：

```python
print(student.get("age"))       # None
print(student.get("age", 0))    # 0
```

## 8. 遍历字典的思路
很多时候我们不只是想查一个值，而是想把整张“表”都看一遍。

```python
student = {"name": "Tom", "age": 12, "score": 95}
for key, value in student.items():
    print(key, value)
```

这在打印信息、生成报告、批量检查字段时非常常见。

## 9. 字典最强的地方
字典最大的优势不是“语法好看”，而是：
- 查询快
- 读起来更清楚
- 适合表示“属性很多的一条记录”

## 10. 本节总结
看到这种问题时，应优先想到字典：
- 按名字取数据
- 一条记录有多个字段
- 想表达“键 -> 值”的对应关系
"""
)

Quiz.objects.create(lesson=l2_3_2, question="字典中用于查找数据的是？", option_a="索引位置", option_b="键（Key）", option_c="长度", option_d="切片", correct_answer="B", explanation="字典通过键来查找对应的值。")
Quiz.objects.create(lesson=l2_3_2, question="student = {'name': 'Amy', 'age': 11}，student['age'] 的值是？", option_a="Amy", option_b="11", option_c="'age'", option_d="报错", correct_answer="B", explanation="键 'age' 对应的值是 11。")
Quiz.objects.create(lesson=l2_3_2, question="向字典中新增键值对，下面哪种写法正确？", option_a="d.add('x', 1)", option_b="d['x'] = 1", option_c="d.append('x', 1)", option_d="d.insert('x', 1)", correct_answer="B", explanation="直接通过 d['x'] = 1 即可新增或修改。")
Quiz.objects.create(lesson=l2_3_2, question="遍历字典的键和值最常用的方法是？", option_a="keys()", option_b="values()", option_c="items()", option_d="pairs()", correct_answer="C", explanation="items() 会返回键值对。")
Quiz.objects.create(lesson=l2_3_2, question="判断题：字典中的键可以重复而不会有影响。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，重复键会覆盖原来的值。")
Quiz.objects.create(lesson=l2_3_2, question="判断题：'name' in student 可以判断键是否存在。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，in 可以判断键是否在字典中。")

l2_3_3 = create_lesson(
    chapter=ch2_3, title="3.3 集合 Set：自动去重的容器", order=3, lesson_type='code',
    code_challenge_prompt="# 使用集合对下面列表去重\nnums = [1, 2, 2, 3, 3, 3, 4]\nunique_nums = set(nums)\nprint(unique_nums)",
    content="""# 3.3 集合 Set：自动去重的容器

## 1. 什么是集合？
集合（Set）是一个**无序**、**元素不重复**的容器。

```python
nums = {1, 2, 3}
letters = set("banana")
print(letters)
```

输出中不会有重复元素。

## 2. 集合最常见的用途
- **去重**
- **快速判断元素是否存在**
- 进行交集、并集、差集等集合运算

## 3. 去重示例
```python
nums = [1, 2, 2, 3, 3, 4]
unique_nums = set(nums)
print(unique_nums)
```

## 4. 常用操作
```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)  # 并集 {1, 2, 3, 4, 5}
print(a & b)  # 交集 {3}
print(a - b)  # 差集 {1, 2}
```

## 5. 注意事项
- 集合没有固定顺序，所以不能像列表那样用索引访问。
- 集合中的元素必须是可哈希的，初学阶段可以简单理解为：通常放数字、字符串、元组，不放列表。

## 6. add/remove/discard
集合除了能直接创建，也可以在运行过程中不断变化。

```python
s = {1, 2, 3}
s.add(4)
s.remove(2)
print(s)
```

需要注意：
- `remove(x)`：元素不存在时会报错
- `discard(x)`：元素不存在也不会报错

```python
s.discard(100)  # 安全，不报错
```

## 7. 集合最适合什么问题？
看到下面这类任务时，集合通常很有优势：
- 名单去重
- 判断一个元素是否出现过
- 比较两个集合有哪些相同/不同

## 8. 一个实际例子
```python
submitted = ["Tom", "Amy", "Tom", "Lily"]
unique_students = set(submitted)
print(unique_students)
```

这就能快速算出“到底有多少位不同的同学提交过”。

## 9. 本节总结
集合的核心不是“存很多东西”，而是这两个字：
- 去重
- 判存在
"""
)

Quiz.objects.create(lesson=l2_3_3, question="集合最明显的特点是？", option_a="元素可重复", option_b="元素自动排序", option_c="元素不重复", option_d="只能保存数字", correct_answer="C", explanation="集合中的重复元素会被自动去掉。")
Quiz.objects.create(lesson=l2_3_3, question="set('banana') 中字母 'a' 最多会出现几次？", option_a="0 次", option_b="1 次", option_c="2 次", option_d="3 次", correct_answer="B", explanation="集合会自动去重，所以 'a' 只保留一次。")
Quiz.objects.create(lesson=l2_3_3, question="下列哪个运算表示交集？", option_a="|", option_b="&", option_c="-", option_d="*", correct_answer="B", explanation="& 表示两个集合共同拥有的元素。")
Quiz.objects.create(lesson=l2_3_3, question="为什么集合不适合按下标取值？", option_a="因为集合太大", option_b="因为集合只能存字符串", option_c="因为集合无序", option_d="因为集合必须先排序", correct_answer="C", explanation="集合无序，因此没有稳定的索引位置。")
Quiz.objects.create(lesson=l2_3_3, question="判断题：集合很适合做列表去重。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，set(list_data) 是常见去重方式。")
Quiz.objects.create(lesson=l2_3_3, question="判断题：集合可以直接使用 s[0] 访问第一个元素。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，集合没有索引。")

l2_3_4 = create_lesson(
    chapter=ch2_3, title="3.4 列表、元组、字典、集合怎么选？", order=4, lesson_type='code',
    code_challenge_prompt="# 请为下面 4 种数据选择合适的容器\n# 1. 学生姓名列表\n# 2. 固定坐标 (x, y)\n# 3. 学生信息（姓名、年龄、班级）\n# 4. 去重后的选课名单\nprint('思考：list / tuple / dict / set 分别适合什么场景？')",
    content="""# 3.4 列表、元组、字典、集合怎么选？

## 1. 四种容器回顾
- **列表 list**：有序、可修改，适合保存一串需要增删改的数据
- **元组 tuple**：有序、不可修改，适合固定信息
- **字典 dict**：键值对，适合“按名字找数据”
- **集合 set**：无序、不重复，适合去重和判存在

## 2. 典型场景
### 场景 A：班级成绩单
如果只想按顺序存一组分数，使用列表。

```python
scores = [95, 88, 76, 90]
```

### 场景 B：一个固定坐标
```python
point = (120, 45)
```

### 场景 C：一名学生的完整资料
```python
student = {
    "name": "Lily",
    "age": 12,
    "class": "三年级二班"
}
```

### 场景 D：报名名单去重
```python
signup = ["Tom", "Amy", "Tom", "Lucy"]
unique_signup = set(signup)
```

## 3. 选型口诀
- 要顺序又要修改：**列表**
- 要顺序但不修改：**元组**
- 要通过名称查数据：**字典**
- 要去重或快速查存在：**集合**

真正的编程能力，不只是会写语法，更是知道什么时候该用哪种数据结构。

## 4. 一个选型思考流程
以后遇到容器题时，可以按这个顺序问自己：

1. 这组数据有没有顺序？
2. 后面会不会修改？
3. 是按位置取，还是按名字取？
4. 有没有“去重”需求？

如果你能按这 4 个问题思考，通常就不会乱选。

## 5. 常见误选
### 误选 A：明明要按字段读取，却还在用列表
这会让代码越来越难看懂。

### 误选 B：明明只想去重，却还在手写很多判断
这时集合通常更直接。

### 误选 C：固定数据写成列表
虽然也能用，但表达力不如元组。

## 6. 本节总结
这一节不是单纯背结论，而是训练“数据结构选型意识”。  
真正的提升，是你看到题目时能主动判断：
- 为什么用它？
- 用别的为什么不合适？
"""
)

Quiz.objects.create(lesson=l2_3_4, question="保存每天可能新增的待办事项，更适合用哪种结构？", option_a="tuple", option_b="list", option_c="set", option_d="dict", correct_answer="B", explanation="待办事项会频繁增加和修改，列表更合适。")
Quiz.objects.create(lesson=l2_3_4, question="保存固定的平面坐标 (x, y)，更推荐使用？", option_a="list", option_b="tuple", option_c="dict", option_d="set", correct_answer="B", explanation="坐标通常固定不变，用元组更清晰。")
Quiz.objects.create(lesson=l2_3_4, question="已知学生姓名、年龄、班级，要按字段读取信息，更适合用？", option_a="dict", option_b="set", option_c="tuple", option_d="range", correct_answer="A", explanation="按字段名称读取最适合字典。")
Quiz.objects.create(lesson=l2_3_4, question="从一堆重复名单中保留唯一值，更适合用？", option_a="list", option_b="tuple", option_c="set", option_d="dict", correct_answer="C", explanation="集合天然去重。")
Quiz.objects.create(lesson=l2_3_4, question="判断题：如果要根据商品编号快速找到商品信息，字典通常比列表更直观。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，商品编号可以作为字典键。")
Quiz.objects.create(lesson=l2_3_4, question="判断题：集合中的元素顺序通常是稳定且可依赖的。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，集合是无序容器。")

l2_3_5 = create_lesson(
    chapter=ch2_3, title="3.5 综合实战：班级选课信息整理", order=5, lesson_type='code',
    code_challenge_prompt="""# 已知班级选课记录如下：
# 同一个学生可能出现多次，表示重复提交
records = [
    ("Tom", "Python"),
    ("Amy", "Scratch"),
    ("Tom", "Python"),
    ("Lily", "Python"),
    ("Amy", "C++"),
]

# 任务：
# 1. 用集合统计一共有多少位不同的学生
# 2. 用字典统计每门课程有多少位学生选择
# 3. 打印 students_count 和 course_counts

students_count = 0
course_counts = {}

# TODO: 在这里完成代码

print(students_count)
print(course_counts)
""",
    content="""# 3.5 综合实战：班级选课信息整理

这一节把前面学过的 **元组、字典、集合** 放在同一个任务里练习。

## 1. 题目背景
老师收到了下面这些选课记录：

```python
records = [
    ("Tom", "Python"),
    ("Amy", "Scratch"),
    ("Tom", "Python"),
    ("Lily", "Python"),
    ("Amy", "C++"),
]
```

每条记录都可以理解成一个**元组**：
- 第一个位置：学生姓名
- 第二个位置：课程名称

## 2. 我们要解决什么问题？
### 问题 A：一共有多少位不同的学生？
因为有重复提交，所以要去重。  
这时最适合用 **集合 set**。

### 问题 B：每门课程有多少位学生选择？
这时需要“课程名 -> 数量”的对应关系，最适合用 **字典 dict**。

## 3. 解题思路
```python
student_names = set()
course_counts = {}

for name, course in records:
    student_names.add(name)
    if course not in course_counts:
        course_counts[course] = 0
    course_counts[course] += 1
```

## 4. 这道题练到了什么？
- 元组解包：`for name, course in records`
- 集合去重：`student_names.add(name)`
- 字典计数：`course_counts[course] += 1`

## 5. 最终目标
你不只是会用某一种数据结构，而是能根据问题主动选择合适的数据结构。

## 6. 升级任务：最受欢迎课程
在统计每门课程选择人数之后，我们还可以继续问：

- 哪门课最受欢迎？

例如：

```python
most_popular = ""
max_count = 0

for course, count in course_counts.items():
    if count > max_count:
        max_count = count
        most_popular = course

print(most_popular, max_count)
```

这样，这道题就从“基础统计”进一步升级成了“小型分析题”。

## 7. 易错点
### 易错点 A：忘记初始化字典计数
如果还没有这门课，就必须先设为 0。

### 易错点 B：去重和计数混在一起没想清楚
- 去重：集合
- 计数：字典

### 易错点 C：没有意识到 records 中每项其实是元组
只要想通这一点，`for name, course in records` 就会很自然。

## 8. 本节总结
这一节是第3章最有代表性的综合题。  
它真正训练的是：
- 先读懂数据长什么样
- 再判断应该用哪些结构
- 最后把它们配合起来解决问题
"""
)

Quiz.objects.create(lesson=l2_3_5, question="records 中的每一项 ('Tom', 'Python') 最适合看成什么？", option_a="列表", option_b="元组", option_c="集合", option_d="字典", correct_answer="B", explanation="这类固定位置的数据更适合看成元组。")
Quiz.objects.create(lesson=l2_3_5, question="想统计有多少位不同的学生，最适合先把姓名放进哪种结构？", option_a="list", option_b="tuple", option_c="set", option_d="str", correct_answer="C", explanation="集合会自动去重，最适合统计不同姓名。")
Quiz.objects.create(lesson=l2_3_5, question="想保存“课程名 -> 选择人数”的对应关系，应使用哪种结构？", option_a="dict", option_b="set", option_c="tuple", option_d="range", correct_answer="A", explanation="键值对应关系最适合字典。")
Quiz.objects.create(lesson=l2_3_5, question="for name, course in records 这种写法用到了什么？", option_a="切片", option_b="元组解包", option_c="排序", option_d="递归", correct_answer="B", explanation="每条记录都有两个值，循环时可以直接拆成 name 和 course。")
Quiz.objects.create(lesson=l2_3_5, question="若 course_counts 中还没有某门课，正确的做法通常是？", option_a="直接删掉", option_b="先设为 0 再加 1", option_c="改成列表", option_d="转换成元组", correct_answer="B", explanation="计数问题通常先初始化为 0，再逐步累加。")
Quiz.objects.create(lesson=l2_3_5, question="判断题：集合和字典经常一起出现，一个负责去重，一个负责统计。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，这是非常常见的基础数据处理模式。")
Quiz.objects.create(lesson=l2_3_5, question="判断题：如果 Tom 重复提交两次，集合中会保留两个 Tom。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，集合中的重复元素只会保留一个。")


# ==========================================
# Course 3: GESP 3级 - 函数与模块
# ==========================================
print("正在创建 GESP 3级 课程...")
c3, _ = Course.objects.get_or_create(
    title="GESP 3级：函数与模块",
    description="掌握结构化编程。涵盖函数进阶、元组（Tuple）、异常处理（Try-Except）以及模块化编程。",
    defaults={'order': 3}
)

ch3_1, _ = Chapter.objects.get_or_create(course=c3, title="第1章：函数与作用域", defaults={'order': 1})

# 1.1 函数基础
l3_1_1 = create_lesson(
    chapter=ch3_1, title="1.1 函数定义与返回值", order=1, lesson_type='text',
    code_challenge_prompt="# 定义一个函数 add(a, b)，返回两个数的和\ndef add(a, b):\n    return a + b\n\nprint(add(3, 5))",
    content="""# 1.1 函数定义与返回值

## 1. 为什么需要函数？
避免重复代码，把特定的功能封装起来。

## 2. 定义函数
使用 `def` 关键字。
```python
def say_hello():
    print("Hello!")
```

## 3. 参数与返回值
- **参数**：函数接收的输入。
- **返回值**：函数处理后的输出，使用 `return`。

```python
def square(x):
    return x * x

result = square(5) # 25
```

## 4. return 与 print 的区别
这是函数学习里最容易混淆的点之一。

```python
def show_square(x):
    print(x * x)

def get_square(x):
    return x * x
```

- `print()`：只是把结果显示出来
- `return`：把结果“交还”给调用者，后面还能继续使用

```python
a = get_square(5)
print(a + 1)   # 26
```

## 5. 为什么函数能让代码更高级？
函数最大的价值，不只是“能重复调用”，而是让你给一段逻辑起名字。

例如：
- `calc_total()`
- `is_prime()`
- `format_name()`

当名字起得好时，程序可读性会明显提升。

## 6. 本节总结
学完这一节要真正掌握：
- 会用 `def` 定义函数
- 知道参数是输入，`return` 是输出
- 分得清 `print` 和 `return`

## 7. 函数执行顺序
定义函数不会立刻执行函数体：

```python
def say_hi():
    print("Hi")

print("before")
say_hi()
print("after")
```

只有调用 `say_hi()` 时，函数体才会运行。

## 8. return 会结束函数
```python
def check(score):
    if score >= 60:
        return "pass"
    return "fail"
```

一旦执行到 `return`，函数就结束，后面的代码不会继续执行。

## 9. 小练习
写函数 `max2(a, b)`，返回两个数中较大的一个。不要只 `print`，要用 `return`。
"""
)
Quiz.objects.create(lesson=l3_1_1, question="如果不写 return 语句，函数默认返回什么？", option_a="0", option_b="False", option_c="None", option_d="Error", correct_answer="C", explanation="默认返回 None。")
Quiz.objects.create(lesson=l3_1_1, question="定义函数使用哪个关键字？", option_a="function", option_b="def", option_c="func", option_d="define", correct_answer="B", explanation="使用 def。")
Quiz.objects.create(lesson=l3_1_1, question="def foo(): return 1\nprint(foo()) 输出？", option_a="foo", option_b="1", option_c="None", option_d="Error", correct_answer="B", explanation="输出 1。")
Quiz.objects.create(lesson=l3_1_1, question="函数可以没有参数吗？", option_a="可以", option_b="不可以", option_c="必须有", option_d="看情况", correct_answer="A", explanation="函数参数是可选的。")
Quiz.objects.create(lesson=l3_1_1, question="return 语句的作用？", option_a="打印", option_b="返回结果并结束函数", option_c="暂停", option_d="无作用", correct_answer="B", explanation="返回结果并结束。")
Quiz.objects.create(lesson=l3_1_1, question="判断题：一个函数可以有多个 return。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l3_1_1, question="判断题：函数必须有返回值。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，可以是 void 函数。")
Quiz.objects.create(lesson=l3_1_1, question="函数体内的代码必须？", option_a="缩进", option_b="加括号", option_c="写在一行", option_d="用 end 结束", correct_answer="A", explanation="Python 依靠缩进来定义代码块。")
Quiz.objects.create(lesson=l3_1_1, question="调用函数时，参数传递的顺序必须与定义时一致吗？", option_a="必须", option_b="不一定，可以使用关键字参数", option_c="完全随意", option_d="看函数名", correct_answer="B", explanation="使用关键字参数可以不按顺序传递。")
Quiz.objects.create(lesson=l3_1_1, question="def f(a, b=1): ... 其中 b=1 是什么？", option_a="默认参数", option_b="关键字参数", option_c="位置参数", option_d="错误写法", correct_answer="A", explanation="默认参数。")

# 1.2 变量作用域
l3_1_2 = create_lesson(
    chapter=ch3_1, title="1.2 局部变量与全局变量", order=2, lesson_type='text',
    code_challenge_prompt="# 观察局部变量\nx = 10\ndef change():\n    x = 20\n    print(f'内部: {x}')\nchange()\nprint(f'外部: {x}')",
    content="""# 1.2 局部变量与全局变量

## 1. 局部变量
在函数内部定义，只在函数内有效。

## 2. 全局变量
在函数外部定义，全程序有效。

## 3. global 关键字
在函数内修改全局变量需要声明。
```python
score = 0
def add():
    global score
    score += 1
```

## 4. 遮蔽现象
如果函数内部定义了和外部同名的变量，那么函数里会优先使用内部那一个。

```python
name = "Tom"

def show():
    name = "Amy"
    print(name)   # Amy

show()
print(name)       # Tom
```

这叫做“遮蔽”。

## 5. 什么时候需要 global？
只有在函数内部**重新赋值**全局变量时才需要 `global`。

如果只是读取，通常不需要。

## 6. LEGB 直觉理解
Python 找变量时，一般按下面顺序查找：
- Local：当前函数内部
- Enclosing：外层嵌套函数
- Global：当前文件全局
- Built-in：Python 内置名称

这就是 LEGB。

## 7. 本节总结
作用域这节最关键的不是背名词，而是理解：
- 同名变量可能不是同一个变量
- 局部变量通常不会影响全局变量
- 真要改全局值时要格外小心

## 8. 读取和修改不是一回事
读取全局变量通常可以直接读：

```python
score = 100

def show():
    print(score)
```

但在函数内重新赋值，就会创建局部变量，或需要 `global`：

```python
score = 0

def add():
    global score
    score += 1
```

## 9. 少用 global
`global` 能用，但不应该滥用。更好的做法通常是通过参数和返回值传递数据。

```python
def add(score):
    return score + 1

score = add(score)
```

## 10. 小练习
观察下面代码输出，并解释原因：

```python
x = 10
def f():
    x = 20
    return x

print(f())
print(x)
```
"""
)
Quiz.objects.create(lesson=l3_1_2, question="如何修改全局变量？", option_a="直接赋值", option_b="global 声明", option_c="extern", option_d="public", correct_answer="B", explanation="使用 global。")
Quiz.objects.create(lesson=l3_1_2, question="x=1; def f(): x=2; print(x); f(); print(x)", option_a="2 2", option_b="2 1", option_c="1 1", option_d="1 2", correct_answer="B", explanation="局部变量不影响全局。")
Quiz.objects.create(lesson=l3_1_2, question="局部变量作用域？", option_a="函数内", option_b="全局", option_c="类内", option_d="文件内", correct_answer="A", explanation="函数内部。")
Quiz.objects.create(lesson=l3_1_2, question="def f(): y=5; print(y) 外部访问 y？", option_a="5", option_b="None", option_c="报错", option_d="0", correct_answer="C", explanation="报错，NameError。")
Quiz.objects.create(lesson=l3_1_2, question="global 作用？", option_a="定义局部", option_b="声明全局", option_c="导入", option_d="类", correct_answer="B", explanation="声明全局变量。")
Quiz.objects.create(lesson=l3_1_2, question="判断题：函数内可直接读取全局变量。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l3_1_2, question="判断题：局部变量可与全局变量同名。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，会发生遮蔽。")
Quiz.objects.create(lesson=l3_1_2, question="在函数内部修改全局列表的内容（如 append）需要 global 吗？", option_a="需要", option_b="不需要", option_c="报错", option_d="看列表长度", correct_answer="B", explanation="修改可变对象的内容不需要 global，只有重新赋值才需要。")
Quiz.objects.create(lesson=l3_1_2, question="nonlocal 关键字用于？", option_a="全局变量", option_b="嵌套函数中的外层变量", option_c="局部变量", option_d="类变量", correct_answer="B", explanation="用于嵌套作用域。")
Quiz.objects.create(lesson=l3_1_2, question="Python 查找变量的顺序是？", option_a="LEGB (Local -> Enclosing -> Global -> Built-in)", option_b="LGBE", option_c="Global -> Local", option_d="随机", correct_answer="A", explanation="LEGB 原则。")

# 1.3 参数进阶
l3_1_3 = create_lesson(
    chapter=ch3_1, title="1.3 参数传递与函数调用", order=3, lesson_type='code',
    code_challenge_prompt="# 定义一个 greet 函数，支持默认参数 title='同学'\ndef greet(name, title='同学'):\n    return f'{title}，你好，{name}!'\n\nprint(greet('小明'))\nprint(greet('小红', title='老师'))",
    content="""# 1.3 参数传递与函数调用

## 1. 位置参数
函数调用时最常见的是按顺序传参。

```python
def add(a, b):
    return a + b

print(add(3, 5))
```

## 2. 默认参数
有些参数在大多数时候取同一个值，这时可以设置默认参数。

```python
def greet(name, title="同学"):
    return f"{title}，你好，{name}!"
```

如果调用时不传 `title`，就自动使用默认值。

## 3. 关键字参数
调用函数时也可以写出“参数名=值”，这样代码更清晰。

```python
print(greet(name="小明", title="班长"))
```

## 4. 返回多个结果
Python 函数可以一次返回多个值，本质上会打包成元组。

```python
def calc(a, b):
    return a + b, a - b

x, y = calc(8, 3)
```

## 5. 使用函数拆解问题
函数的意义不仅是“能调用”，更重要的是把复杂问题分成多个小步骤，让程序更清晰、便于复用和测试。

## 6. 参数设计习惯
写函数时可以先问自己：
- 这段功能需要哪些输入？
- 哪些参数最常变化？
- 哪些参数可以给默认值？

这样写出来的函数会更自然。

## 7. 返回多个值为什么有用？
有时一个函数处理后会得到不止一个结果。

```python
def calc(a, b):
    return a + b, a - b
```

这样可以一次把多个结果交出去，而不必写很多全局变量。

## 8. 本节总结
这一节真正要掌握的是：
- 按顺序传参：位置参数
- 给默认值：默认参数
- 写名字传参：关键字参数
- 一个函数可以返回多个结果
"""
)
Quiz.objects.create(lesson=l3_1_3, question="调用 add(3, 5) 时，3 和 5 属于哪类参数传递方式？", option_a="关键字参数", option_b="位置参数", option_c="默认参数", option_d="匿名参数", correct_answer="B", explanation="按顺序传入的参数叫位置参数。")
Quiz.objects.create(lesson=l3_1_3, question="def greet(name, title='同学') 中 title='同学' 属于？", option_a="局部变量", option_b="返回值", option_c="默认参数", option_d="全局变量", correct_answer="C", explanation="这是默认参数。")
Quiz.objects.create(lesson=l3_1_3, question="下面哪种调用方式属于关键字参数？", option_a="greet('小明', '老师')", option_b="greet(name='小明')", option_c="greet('小明')", option_d="greet()", correct_answer="B", explanation="写出参数名就是关键字参数。")
Quiz.objects.create(lesson=l3_1_3, question="函数 return a + b, a - b 返回的本质通常是？", option_a="列表", option_b="字符串", option_c="元组", option_d="字典", correct_answer="C", explanation="多个返回值会打包为元组。")
Quiz.objects.create(lesson=l3_1_3, question="函数最重要的作用之一是？", option_a="让代码更长", option_b="拆分问题、复用逻辑", option_c="减少缩进", option_d="替代变量", correct_answer="B", explanation="函数可以封装并复用逻辑。")
Quiz.objects.create(lesson=l3_1_3, question="判断题：默认参数只能放在参数列表最后。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="默认参数后面不能再跟普通位置参数。")
Quiz.objects.create(lesson=l3_1_3, question="判断题：关键字参数可以提高函数调用时的可读性。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，尤其是参数较多时。")
Quiz.objects.create(lesson=l3_1_3, question="x, y = calc(8, 3) 这种写法叫？", option_a="异常捕获", option_b="元组解包", option_c="切片", option_d="递归", correct_answer="B", explanation="返回的多个值可以直接解包到多个变量。")
Quiz.objects.create(lesson=l3_1_3, question="如果函数定义为 f(a, b=1)，调用 f(5) 时 b 的值是？", option_a="0", option_b="1", option_c="5", option_d="报错", correct_answer="B", explanation="未传入时使用默认值 1。")
Quiz.objects.create(lesson=l3_1_3, question="下列哪项最能体现“函数化思维”？", option_a="所有代码都写在 main 里", option_b="把重复逻辑提取成函数", option_c="少用 return", option_d="避免传参", correct_answer="B", explanation="复用和拆解是函数化思维的核心。")

ch3_2, _ = Chapter.objects.get_or_create(course=c3, title="第2章：元组与异常处理", defaults={'order': 2})

# 2.1 元组 Tuple
l3_2_1 = create_lesson(
    chapter=ch3_2, title="2.1 元组 Tuple", order=1, lesson_type='text',
    code_challenge_prompt="# 创建一个元组并尝试修改（会报错，请观察）\nt = (1, 2, 3)\nprint(t[0])\n# t[0] = 10",
    content="""# 2.1 元组 Tuple

## 1. 什么是元组？
元组就像是**不可变的列表**。一旦创建，就不能修改（不能增加、删除、修改元素）。
使用小括号 `()` 定义。

```python
t = (1, 2, 3)
print(t[0]) # 1
```

## 2. 为什么用元组？
- **安全**：数据不会被意外修改。
- **速度**：比列表稍微快一点。
- **作为键**：元组可以作为字典的键，列表不行。

## 3. 元组操作
- 支持索引和切片 `t[1:3]`。
- 支持 `len()`, `count()`, `index()`。
- **不支持** `append()`, `remove()`, `t[0]=x`。

## 4. 单元素元组
注意：`(1)` 是数字 1，`(1,)` 才是元组！

## 5. 元组为什么常和函数一起出现？
因为函数返回多个值时，Python 往往会把它们打包成元组。

```python
def info():
    return "Tom", 12

data = info()
print(data)   # ('Tom', 12)
```

## 6. 元组适合固定结构数据
比如：
- 坐标 `(x, y)`
- 日期 `(year, month, day)`
- 成绩记录 `(name, score)`

这些数据都有固定位置和固定意义。

## 7. 本节总结
元组最大的价值是：
- 结构固定
- 语义明确
- 不容易被误修改

## 8. 元组解包
```python
point = (3, 5)
x, y = point
print(x, y)
```

元组解包可以让代码更清楚。函数返回多个值时也常用它。

```python
def calc(a, b):
    return a + b, a - b

total, diff = calc(8, 3)
```

## 9. 元组里的可变对象
元组本身不可变，但如果元组里装的是列表，列表内容仍然可以变。

```python
t = (1, [2, 3])
t[1].append(4)
print(t)
```

这点容易考。

## 10. 小练习
用元组表示一个学生记录 `(name, age, score)`，再用解包输出三项信息。
"""
)
Quiz.objects.create(lesson=l3_2_1, question="t = (1, 2, 3)，t[0] = 10 会发生什么？", option_a="t变成(10,2,3)", option_b="报错", option_c="t不变", option_d="t变成[10,2,3]", correct_answer="B", explanation="元组是不可变的，不能修改。")
Quiz.objects.create(lesson=l3_2_1, question="如何定义包含一个元素 5 的元组？", option_a="(5)", option_b="(5,)", option_c="[5]", option_d="{5}", correct_answer="B", explanation="必须加逗号，否则被视为数学括号。")
Quiz.objects.create(lesson=l3_2_1, question="元组支持哪种操作？", option_a="append", option_b="remove", option_c="count", option_d="sort", correct_answer="C", explanation="支持查询类操作如 count。")
Quiz.objects.create(lesson=l3_2_1, question="t = (1, 2) + (3, 4) 的结果？", option_a="(1, 2, 3, 4)", option_b="(4, 6)", option_c="报错", option_d="((1,2),(3,4))", correct_answer="A", explanation="元组拼接。")
Quiz.objects.create(lesson=l3_2_1, question="列表和元组的主要区别？", option_a="列表用()", option_b="元组可变", option_c="元组不可变", option_d="列表不能存字符串", correct_answer="C", explanation="元组不可变。")
Quiz.objects.create(lesson=l3_2_1, question="判断题：元组可以包含列表作为元素。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，如 (1, [2, 3])。")
Quiz.objects.create(lesson=l3_2_1, question="判断题：空元组是 ()。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l3_2_1, question="tuple([1, 2]) 的结果是？", option_a="[1, 2]", option_b="(1, 2)", option_c="{1, 2}", option_d="报错", correct_answer="B", explanation="将列表转换为元组。")
Quiz.objects.create(lesson=l3_2_1, question="元组 (1, 2) * 2 的结果是？", option_a="(1, 2, 1, 2)", option_b="(2, 4)", option_c="(1, 1, 2, 2)", option_d="报错", correct_answer="A", explanation="重复拼接。")
Quiz.objects.create(lesson=l3_2_1, question="元组的遍历速度比列表？", option_a="快", option_b="慢", option_c="一样", option_d="无法比较", correct_answer="A", explanation="元组不可变，有些优化。")

# 2.2 异常处理
l3_2_2 = create_lesson(
    chapter=ch3_2, title="2.2 异常处理 try-except", order=2, lesson_type='code',
    code_challenge_prompt="# 捕获除以零的错误\ntry:\n    print(10 / 0)\nexcept ZeroDivisionError:\n    print('不能除以零')",
    content="""# 2.2 异常处理 try-except

## 1. 什么是异常？
程序运行过程中出现的错误，比如除以零、索引越界、文件找不到。如果不处理，程序会崩溃。

## 2. 基本结构
```python
try:
    # 可能出错的代码
    num = int(input("请输入数字: "))
    print(10 / num)
except ValueError:
    print("输入的不是数字！")
except ZeroDivisionError:
    print("不能除以零！")
except Exception as e:
    print(f"发生了其他错误: {e}")
```

## 3. else 和 finally
- `else`: 没有发生异常时执行。
- `finally`: 无论是否发生异常，**都会执行**（常用于关闭文件）。

## 4. 精准捕获 vs 一把抓
异常处理并不是“有 except 就行”，更重要的是尽量知道自己在处理什么错误。

```python
try:
    num = int("abc")
except ValueError:
    print("输入格式不对")
```

这就比直接写一个很宽泛的 `except Exception` 更清楚。

## 5. 为什么异常处理很重要？
如果程序一出错就直接中断，用户体验会很差。  
异常处理的意义是：
- 避免程序立刻崩掉
- 给出更友好的提示
- 让程序更稳健

## 6. raise 的直觉
`raise` 表示“我主动告诉程序这里出问题了”。

```python
age = -1
if age < 0:
    raise ValueError("年龄不能为负数")
```

## 7. 本节总结
异常处理的核心不是“把错误藏起来”，而是：
- 识别错误
- 合理处理
- 给出清楚反馈
"""
)
Quiz.objects.create(lesson=l3_2_2, question="处理异常使用哪个关键字？", option_a="catch", option_b="except", option_c="error", option_d="handle", correct_answer="B", explanation="try-except 结构。")
Quiz.objects.create(lesson=l3_2_2, question="finally 代码块什么时候执行？", option_a="出错时", option_b="不出错时", option_c="总是执行", option_d="不一定", correct_answer="C", explanation="总是执行。")
Quiz.objects.create(lesson=l3_2_2, question="捕获所有错误的基类是？", option_a="Error", option_b="Exception", option_c="Base", option_d="Object", correct_answer="B", explanation="Exception。")
Quiz.objects.create(lesson=l3_2_2, question="int('abc') 会抛出什么异常？", option_a="ValueError", option_b="TypeError", option_c="NameError", option_d="IndexError", correct_answer="A", explanation="值错误。")
Quiz.objects.create(lesson=l3_2_2, question="try 块中没有错误，会执行哪个块？", option_a="except", option_b="else", option_c="catch", option_d="error", correct_answer="B", explanation="else 块。")
Quiz.objects.create(lesson=l3_2_2, question="判断题：一个 try 可以对应多个 except。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l3_2_2, question="判断题：except 必须配合 try 使用。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l3_2_2, question="raise 关键字的作用是？", option_a="捕获异常", option_b="抛出异常", option_c="忽略异常", option_d="定义异常", correct_answer="B", explanation="手动抛出异常。")
Quiz.objects.create(lesson=l3_2_2, question="KeyError 通常发生在？", option_a="列表索引越界", option_b="字典键不存在", option_c="除以零", option_d="变量未定义", correct_answer="B", explanation="字典查找不存在的键。")
Quiz.objects.create(lesson=l3_2_2, question="IndexError 通常发生在？", option_a="访问不存在的列表索引", option_b="字典键错误", option_c="类型错误", option_d="文件错误", correct_answer="A", explanation="列表索引越界。")

ch3_3, _ = Chapter.objects.get_or_create(course=c3, title="第3章：模块与代码组织", defaults={'order': 3})

# 3.1 模块基础
l3_3_1 = create_lesson(
    chapter=ch3_3, title="3.1 什么是模块 import", order=1, lesson_type='text',
    code_challenge_prompt="# 导入 math 模块并计算 16 的平方根\nimport math\nprint(math.sqrt(16))",
    content="""# 3.1 什么是模块 import

## 1. 模块是什么？
Python 中，一个 `.py` 文件通常就可以看作一个**模块**。  
模块里可以放函数、变量、类，用来组织代码。

## 2. 为什么要用模块？
- 让代码更清晰
- 方便复用
- 避免把所有代码都写在一个文件里

## 3. 最基本的导入方式
```python
import math
print(math.sqrt(16))
```

这里 `math` 是 Python 自带的标准库模块。

## 4. 通过模块名调用函数
导入模块后，通常要写成：

```python
模块名.函数名()
```

例如：
```python
math.sqrt(25)
```

这种写法可以清楚地看出函数来自哪个模块。

## 5. 标准库和第三方库
模块不只有一种来源。

- 标准库：Python 自带，如 `math`、`random`
- 第三方库：需要额外安装，如 `numpy`、`pandas`
- 自定义模块：你自己写的 `.py` 文件

## 6. 为什么模块化很重要？
当程序只有十几行时，可能感觉不到模块的价值。  
但一旦代码变长，如果不拆模块，很快就会变得难找、难改、难复用。

## 7. 本节总结
学完这节要形成的意识是：
- `.py` 文件本身就可以是模块
- 模块让代码更清晰
- `import 模块名` 是最基础也最推荐先掌握的方式

## 8. 常见标准库模块
- `math`：数学函数
- `random`：随机数
- `datetime`：日期时间
- `os`：操作系统相关
- `sys`：解释器相关

```python
import random
print(random.randint(1, 6))
```

## 9. 模块名冲突
不要把自己的文件命名为 `random.py`、`math.py` 这类标准库名字。否则导入时可能导入到自己的文件，造成奇怪错误。

## 10. 小练习
导入 `random` 模块，模拟掷骰子，输出 1 到 6 的随机整数。
"""
)
Quiz.objects.create(lesson=l3_3_1, question="Python 中一个普通的 .py 文件通常可以看作什么？", option_a="变量", option_b="模块", option_c="异常", option_d="元组", correct_answer="B", explanation="一个 .py 文件通常就是一个模块。")
Quiz.objects.create(lesson=l3_3_1, question="使用 math 模块中的 sqrt 函数，正确写法是？", option_a="sqrt(16)", option_b="math->sqrt(16)", option_c="math.sqrt(16)", option_d="import.sqrt(16)", correct_answer="C", explanation="导入模块后要通过 模块名.函数名 调用。")
Quiz.objects.create(lesson=l3_3_1, question="模块的主要作用之一是？", option_a="删除变量", option_b="组织和复用代码", option_c="让程序变慢", option_d="替代 if", correct_answer="B", explanation="模块用于组织和复用代码。")
Quiz.objects.create(lesson=l3_3_1, question="import math 后，想求 9 的平方根应写作？", option_a="sqrt(9)", option_b="math.sqrt(9)", option_c="math(9)", option_d="import.sqrt(9)", correct_answer="B", explanation="函数属于 math 模块。")
Quiz.objects.create(lesson=l3_3_1, question="判断题：模块中只能写函数，不能写变量。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，模块中也可以定义变量和类。")
Quiz.objects.create(lesson=l3_3_1, question="判断题：使用模块可以减少代码混乱。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，模块有助于组织代码。")
Quiz.objects.create(lesson=l3_3_1, question="math 属于哪一类模块？", option_a="第三方模块", option_b="标准库模块", option_c="浏览器模块", option_d="数据库模块", correct_answer="B", explanation="math 是 Python 标准库模块。")
Quiz.objects.create(lesson=l3_3_1, question="模块导入后加模块名前缀的好处是？", option_a="代码更短", option_b="更清楚函数来源", option_c="速度更快", option_d="一定更省内存", correct_answer="B", explanation="写成 math.sqrt 更清楚函数来自哪里。")
Quiz.objects.create(lesson=l3_3_1, question="下列哪个关键字用于导入模块？", option_a="include", option_b="require", option_c="import", option_d="using", correct_answer="C", explanation="Python 使用 import 导入模块。")
Quiz.objects.create(lesson=l3_3_1, question="模块化编程最直接的好处不包括？", option_a="更易维护", option_b="更便于复用", option_c="完全不需要测试", option_d="结构更清晰", correct_answer="C", explanation="模块化不能替代测试。")

# 3.2 from import 与别名
l3_3_2 = create_lesson(
    chapter=ch3_3, title="3.2 from...import 与 as 别名", order=2, lesson_type='code',
    code_challenge_prompt="# 使用 from random import randint 生成 1~6 的随机整数\nfrom random import randint\nprint(randint(1, 6))",
    content="""# 3.2 from...import 与 as 别名

## 1. 直接导入模块中的内容
有时我们只想用模块里的某一个函数，可以写成：

```python
from math import sqrt
print(sqrt(36))
```

## 2. 使用别名
如果模块名太长，或者为了书写方便，可以使用 `as`。

```python
import random as rnd
print(rnd.randint(1, 10))
```

## 3. 两种导入方式对比
- `import math`：更清楚函数来自哪里
- `from math import sqrt`：调用更短

## 4. 一个习惯
初学时更推荐先理解 `import 模块名` 的方式，再学习 `from ... import ...` 和 `as`。

## 5. 什么时候适合用别名？
别名常见于两种情况：
- 模块名太长
- 领域里有约定俗成的缩写

例如：

```python
import numpy as np
import pandas as pd
```

## 6. from ... import ... 的优点和风险
优点：
- 写起来更短
- 某些场景更方便

风险：
- 看代码时不容易立刻知道函数来自哪个模块
- 容易和别的同名函数混淆

## 7. 本节总结
这节要学会的不是背语法，而是能根据场景选择：
- 想更清楚：`import 模块名`
- 想更简洁：`from ... import ...`
- 想更顺手：`as` 起别名

## 8. 不同写法对比
```python
import math
print(math.sqrt(16))
```

```python
from math import sqrt
print(sqrt(16))
```

两段代码结果一样，但第一种更清楚来源，第二种更简洁。

## 9. 多个导入
```python
from math import sqrt, pi
print(sqrt(16), pi)
```

可以从一个模块导入多个名字。

## 10. 小练习
用 `from random import randint` 写一个 1 到 100 的随机数生成器。
"""
)
Quiz.objects.create(lesson=l3_3_2, question="from math import sqrt 后，调用平方根函数应写作？", option_a="math.sqrt(9)", option_b="sqrt(9)", option_c="import.sqrt(9)", option_d="from.sqrt(9)", correct_answer="B", explanation="直接导入了 sqrt，因此可以直接写 sqrt(9)。")
Quiz.objects.create(lesson=l3_3_2, question="import random as rnd 中 rnd 是什么？", option_a="函数名", option_b="模块别名", option_c="异常对象", option_d="关键字参数", correct_answer="B", explanation="as 可以给模块起别名。")
Quiz.objects.create(lesson=l3_3_2, question="哪种写法表示“只导入模块中的一个函数”？", option_a="import math.sqrt", option_b="from math import sqrt", option_c="use math sqrt", option_d="math import sqrt", correct_answer="B", explanation="这是 Python 的标准写法。")
Quiz.objects.create(lesson=l3_3_2, question="as 关键字的主要用途是？", option_a="定义函数", option_b="设置默认参数", option_c="起别名", option_d="捕获异常", correct_answer="C", explanation="as 用于为模块或导入内容指定别名。")
Quiz.objects.create(lesson=l3_3_2, question="下列哪种导入方式更能清楚看出函数来源？", option_a="from math import sqrt", option_b="import math", option_c="都一样", option_d="都不行", correct_answer="B", explanation="写成 math.sqrt 更清楚来源。")
Quiz.objects.create(lesson=l3_3_2, question="判断题：from module import * 一般不推荐初学阶段大量使用。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="容易造成命名混乱。")
Quiz.objects.create(lesson=l3_3_2, question="判断题：import random as rnd 后，原来的模块功能依旧可以通过 rnd 使用。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="别名只是换了一个名字。")
Quiz.objects.create(lesson=l3_3_2, question="from random import randint 后，还必须写 random.randint(1, 6) 吗？", option_a="必须", option_b="不需要", option_c="只能在函数内写", option_d="会报错", correct_answer="B", explanation="已经直接导入了 randint。")
Quiz.objects.create(lesson=l3_3_2, question="下列哪个更适合表示“骰子随机点数”？", option_a="randint(1, 6)", option_b="sqrt(1, 6)", option_c="input(1, 6)", option_d="len(1, 6)", correct_answer="A", explanation="randint 可以生成指定范围内的随机整数。")
Quiz.objects.create(lesson=l3_3_2, question="关键字 as 的作用最接近下面哪句话？", option_a="给东西换个更方便的名字", option_b="把字符串变成数字", option_c="定义异常", option_d="创建循环", correct_answer="A", explanation="as 就是给导入对象设置别名。")

# 3.3 自定义模块
l3_3_3 = create_lesson(
    chapter=ch3_3, title="3.3 自定义模块与代码拆分", order=3, lesson_type='text',
    code_challenge_prompt="# 假设 helpers.py 中有 say_hi 函数\n# from helpers import say_hi\n# say_hi('Tom')\nprint('思考：为什么要把函数拆到 helpers.py 里？')",
    content="""# 3.3 自定义模块与代码拆分

## 1. 你自己写的 .py 文件也可以是模块
例如你写了一个 `helpers.py`：

```python
def say_hi(name):
    return f"你好，{name}"
```

然后在另一个文件中使用它：

```python
from helpers import say_hi
print(say_hi("Tom"))
```

## 2. 为什么要拆分文件？
- 主程序更简洁
- 常用函数可以复用
- 多个同学合作时更容易分工

## 3. 一个常见思路
- `main.py`：主程序入口
- `helpers.py`：辅助函数
- `utils.py`：工具函数

这就是最基础的代码组织方式。

## 4. 模块化思维
当程序越来越大时，把不同职责的代码放到不同模块中，是非常重要的编程习惯。

## 5. 为什么不要把所有函数都塞进 main.py
如果所有逻辑都写在一个文件里，通常会遇到这些问题：
- 文件越来越长
- 想找某个函数很麻烦
- 复用困难
- 多人协作容易冲突

所以，随着代码变大，把功能分到不同模块里是很自然的下一步。

## 6. 一种常见拆分方式
例如做一个小项目时，可以这样分：
- `main.py`：主流程
- `score_tools.py`：成绩计算
- `text_tools.py`：字符串处理

## 7. 本节总结
模块拆分不是为了“文件看起来高级”，而是为了：
- 结构清晰
- 更好维护
- 更易复用

## 8. __name__ 简介
自定义模块里常见这段代码：

```python
if __name__ == "__main__":
    print("直接运行这个文件")
```

它的意思是：只有当这个文件被直接运行时，才执行下面代码；如果它是被别的文件导入，就不执行。

## 9. 文件放在哪里
初学阶段，先把 `main.py` 和 `helpers.py` 放在同一个文件夹中，这样最容易导入。

## 10. 小练习
创建 `score_tools.py`，写入 `avg(scores)`；再在 `main.py` 中导入并调用。
"""
)
Quiz.objects.create(lesson=l3_3_3, question="自己写的 helpers.py 能不能作为模块导入？", option_a="能", option_b="不能", option_c="只有系统模块才行", option_d="必须联网才行", correct_answer="A", explanation="自己的 .py 文件也可以作为模块。")
Quiz.objects.create(lesson=l3_3_3, question="把常用函数放入 helpers.py 的主要好处是？", option_a="让代码更乱", option_b="便于复用和组织", option_c="自动加速程序", option_d="避免写函数", correct_answer="B", explanation="模块化的核心就是复用和清晰。")
Quiz.objects.create(lesson=l3_3_3, question="主程序入口通常更适合放在哪个文件？", option_a="main.py", option_b="random.py", option_c="except.py", option_d="tuple.py", correct_answer="A", explanation="main.py 常作为主程序入口。")
Quiz.objects.create(lesson=l3_3_3, question="from helpers import say_hi 说明要导入什么？", option_a="helpers 模块里的 say_hi", option_b="所有模块", option_c="异常处理", option_d="一个列表", correct_answer="A", explanation="导入的是 helpers 模块中的 say_hi 函数。")
Quiz.objects.create(lesson=l3_3_3, question="模块化编程更适合哪种场景？", option_a="代码越来越多时", option_b="只有一行代码时", option_c="不用函数时", option_d="只写输入输出时", correct_answer="A", explanation="程序变大后更需要模块化组织。")
Quiz.objects.create(lesson=l3_3_3, question="判断题：把所有代码永远写在一个文件里通常更利于维护。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，代码多时拆分模块更容易维护。")
Quiz.objects.create(lesson=l3_3_3, question="判断题：一个模块中可以包含多个函数。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，一个模块可以包含多个函数和变量。")
Quiz.objects.create(lesson=l3_3_3, question="helpers.py 最适合放什么内容？", option_a="辅助函数", option_b="浏览器设置", option_c="硬件驱动", option_d="数据库本体", correct_answer="A", explanation="名称就说明它适合放辅助函数。")
Quiz.objects.create(lesson=l3_3_3, question="模块拆分最能帮助哪一项？", option_a="代码分工与复用", option_b="减少所有缩进", option_c="自动修复 bug", option_d="取消参数", correct_answer="A", explanation="代码组织和复用是核心价值。")
Quiz.objects.create(lesson=l3_3_3, question="主程序调用模块函数，常见目的不包括？", option_a="复用逻辑", option_b="简化主程序", option_c="让所有文件都一样大", option_d="方便维护", correct_answer="C", explanation="模块化不是为了文件大小平均。")

# 3.4 综合实战
l3_3_4 = create_lesson(
    chapter=ch3_3, title="3.4 综合实战：制作成绩工具箱", order=4, lesson_type='code',
    code_challenge_prompt="""# 现在把“成绩统计”想象成来自 score_tools 模块
# 请定义下面两个函数：
# 1. avg(scores) 计算平均分
# 2. is_pass(score) 判断是否及格（>=60）
# 然后在主程序中调用它们

scores = [76, 88, 92, 61]

def avg(scores):
    pass

def is_pass(score):
    pass

print(avg(scores))
print(is_pass(scores[0]))
""",
    content="""# 3.4 综合实战：制作成绩工具箱

这一节把前面学过的内容串起来：
- 函数
- 返回值
- 模块化思维

## 1. 问题背景
如果我们经常要处理学生成绩，就可以把“求平均分”“判断是否及格”这些功能做成一个小工具箱。

## 2. 第一步：先写函数
```python
def avg(scores):
    return sum(scores) / len(scores)

def is_pass(score):
    return score >= 60
```

## 3. 第二步：主程序调用
```python
scores = [76, 88, 92, 61]
print(avg(scores))
print(is_pass(scores[0]))
```

## 4. 第三步：如果项目变大
就可以把这些函数放进 `score_tools.py`，主程序中再导入使用。

```python
from score_tools import avg, is_pass
```

## 5. 这节课的重点
真正的“函数与模块”不是分开记忆知识点，而是学会：
- 先封装函数
- 再组织到模块
- 最后在主程序里复用

## 6. 一个更完整的项目思维
以后遇到小项目时，可以这样想：
- 哪些功能值得单独写成函数？
- 哪些函数可以放进工具模块？
- 主程序是否只保留“流程控制”？

如果能形成这种思维，就已经进入了“代码组织”的层面。

## 7. 本节总结
综合题最重要的不是写出两个函数，而是理解：
- 重复逻辑应该抽出来
- 抽出来的函数可以继续组织成模块
- 主程序的职责应尽量简单明确

## 8. 加一个等级函数
```python
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 60:
        return "C"
    return "D"
```

这个函数可以和 `avg`、`is_pass` 一起放进成绩工具箱。

## 9. 工具箱升级方向
可以继续加入：
- `max_score(scores)`：最高分
- `min_score(scores)`：最低分
- `count_pass(scores)`：及格人数
- `format_report(scores)`：生成文字报告
"""
)
Quiz.objects.create(lesson=l3_3_4, question="把成绩计算函数放入 score_tools.py，最主要体现了什么思想？", option_a="递归", option_b="模块化", option_c="切片", option_d="排序", correct_answer="B", explanation="把功能拆到独立文件中是模块化思想。")
Quiz.objects.create(lesson=l3_3_4, question="avg(scores) 最可能返回什么？", option_a="一个平均分", option_b="一个文件", option_c="一个异常", option_d="一个模块名", correct_answer="A", explanation="avg 用于计算平均分。")
Quiz.objects.create(lesson=l3_3_4, question="is_pass(score) 最可能返回哪种值？", option_a="列表", option_b="布尔值", option_c="字典", option_d="元组", correct_answer="B", explanation="判断及格通常返回 True 或 False。")
Quiz.objects.create(lesson=l3_3_4, question="from score_tools import avg 表示？", option_a="导入模块中的 avg 函数", option_b="创建模块", option_c="删除模块", option_d="定义异常", correct_answer="A", explanation="这是从模块中导入函数。")
Quiz.objects.create(lesson=l3_3_4, question="综合实战里，主程序最主要负责什么？", option_a="重复写同样逻辑", option_b="调用已经封装好的函数", option_c="替代模块文件", option_d="删除返回值", correct_answer="B", explanation="主程序应以调用为主。")
Quiz.objects.create(lesson=l3_3_4, question="判断题：如果功能会重复使用，就值得写成函数。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，函数最适合封装重复逻辑。")
Quiz.objects.create(lesson=l3_3_4, question="判断题：模块化后，主程序通常会更短、更清晰。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，模块化可以让主程序更聚焦。")
Quiz.objects.create(lesson=l3_3_4, question="如果函数已经写好，再放到单独文件里，本质上是在做什么？", option_a="调试", option_b="代码组织", option_c="异常捕获", option_d="循环优化", correct_answer="B", explanation="这是代码组织与模块化。")
Quiz.objects.create(lesson=l3_3_4, question="下列哪项更像“工具箱函数”？", option_a="avg(scores)", option_b="while True", option_c="import", option_d="except", correct_answer="A", explanation="avg 是可复用的功能函数。")
Quiz.objects.create(lesson=l3_3_4, question="“先写函数，再拆成模块”最符合哪种学习路径？", option_a="从复用到组织", option_b="从异常到继承", option_c="从集合到排序", option_d="从元组到递归", correct_answer="A", explanation="这是函数与模块最自然的学习顺序。")


# ==========================================
# Course 4: GESP 4级 - 数据结构进阶
# ==========================================
print("正在创建 GESP 4级 课程...")
c4, _ = Course.objects.get_or_create(
    title="GESP 4级：数据结构进阶",
    description="深入学习字典、集合以及面向对象编程（OOP）基础。掌握更复杂的数据组织方式，为算法学习打下基础。",
    defaults={'order': 4}
)

ch4_1, _ = Chapter.objects.get_or_create(course=c4, title="第1章：字典与集合", defaults={'order': 1})

# 1.1 字典
l4_1_1 = create_lesson(
    chapter=ch4_1, title="1.1 字典 Dictionary", order=1, lesson_type='text',
    code_challenge_prompt="# 创建字典并访问\nd = {'name': 'Tom', 'age': 18}\nprint(d['name'])",
    content="""# 1.1 字典 Dictionary

## 1. 什么是字典？
字典（dict）是一种用**键值对**保存数据的容器。

```python
student = {
    "name": "Alice",
    "age": 12,
    "score": 95
}
```

每一项都由两部分组成：
- Key（键）：用来查找数据，例如 `"name"`
- Value（值）：真正保存的数据，例如 `"Alice"`

可以把字典理解成“带标签的数据柜”。列表靠位置找数据，字典靠名字找数据。

```python
scores = [95, 88, 76]
print(scores[0])

student = {"score": 95}
print(student["score"])
```

## 2. 键和值的规则
字典的键必须满足两个条件：
- 唯一：同一个字典里不能有两个相同的键
- 不可变：字符串、数字、元组可以做键；列表、字典不能做键

```python
d = {
    "name": "Tom",
    "name": "Jerry"
}
print(d)
```

输出：

```text
{'name': 'Jerry'}
```

后面的同名键会覆盖前面的值，所以写字典时要避免重复键。

值几乎可以是任意类型：

```python
student = {
    "name": "Alice",
    "scores": [90, 95, 88],
    "passed": True
}
```

## 3. 创建、访问、修改、删除
### 创建字典
```python
empty = {}
student = {"name": "Alice", "age": 12}
```

### 访问值
```python
print(student["name"])
```

### 修改已有键
```python
student["age"] = 13
```

### 新增键值对
```python
student["score"] = 95
```

### 删除键值对
```python
del student["age"]
```

也可以用 `pop()` 删除并拿到被删除的值：

```python
score = student.pop("score")
print(score)
```

## 4. 键是否存在时的处理
直接访问不存在的键会报错：

```python
d = {"name": "Tom"}
print(d["age"])  # KeyError
```

更稳妥的方式是使用 `get()`：

```python
print(d.get("age"))      # None
print(d.get("age", 0))   # 0
```

还可以先判断键是否存在：

```python
if "age" in d:
    print(d["age"])
else:
    print("没有 age")
```

GESP 常考点：
- `d["x"]`：键不存在会 `KeyError`
- `d.get("x")`：键不存在返回 `None`
- `d.get("x", 0)`：键不存在返回默认值 `0`
- `"x" in d`：判断键是否存在，不是判断值是否存在

## 5. 遍历字典
字典常见遍历有三种。

### 遍历所有键
```python
student = {"name": "Alice", "age": 12, "score": 95}

for key in student:
    print(key)
```

等价于：

```python
for key in student.keys():
    print(key)
```

### 遍历所有值
```python
for value in student.values():
    print(value)
```

### 同时遍历键和值
```python
for key, value in student.items():
    print(key, value)
```

`items()` 很重要，因为实际编程中经常需要同时知道字段名和字段值。

## 6. 字典为什么比列表更适合“记录型数据”
如果一名学生有姓名、年龄、班级、成绩等信息，用列表也能写：

```python
student = ["Alice", 12, "4班", 95]
```

但这样有问题：
- `student[0]` 到底是什么，需要记忆
- 顺序一改，代码容易错
- 字段多了以后很难维护

字典更清楚：

```python
student = {
    "name": "Alice",
    "age": 12,
    "class": "4班",
    "score": 95
}
```

读代码的人一眼知道每个数据的含义。

## 7. 嵌套字典和列表
字典经常和列表组合，用来表达更复杂的数据。

### 列表里放字典
```python
students = [
    {"name": "Alice", "score": 95},
    {"name": "Bob", "score": 80},
    {"name": "Cindy", "score": 58}
]

for student in students:
    if student["score"] >= 60:
        print(student["name"], "及格")
```

### 字典里放列表
```python
course = {
    "title": "Python",
    "students": ["Alice", "Bob", "Cindy"]
}

print(course["students"][0])
```

这类结构是后续 Web API、JSON 数据、真实业务系统的基础。

## 8. 计数问题：字典高频应用
字典最常见的算法用途之一是“统计次数”。

统计每个字符出现次数：

```python
text = "banana"
count = {}

for ch in text:
    count[ch] = count.get(ch, 0) + 1

print(count)
```

输出：

```text
{'b': 1, 'a': 3, 'n': 2}
```

核心思路：
1. 用字符当键
2. 用出现次数当值
3. 每遇到一次，就把对应值加 1

## 9. 合并与更新
`update()` 可以把一个字典的内容合并到另一个字典：

```python
info = {"name": "Alice", "age": 12}
score = {"score": 95, "rank": 1}

info.update(score)
print(info)
```

如果两个字典有相同的键，后面的值会覆盖前面的值。

```python
d = {"score": 80}
d.update({"score": 95})
print(d["score"])  # 95
```

## 10. 常见方法速查
| 方法 | 作用 |
| :--- | :--- |
| `keys()` | 获取所有键 |
| `values()` | 获取所有值 |
| `items()` | 获取所有键值对 |
| `get(key, default)` | 安全获取 |
| `pop(key)` | 删除并返回值 |
| `update(other)` | 合并/更新 |
| `clear()` | 清空字典 |

## 11. 易错点
### 错误 1：把列表当字典键
```python
d = {[1, 2]: "value"}  # TypeError
```

列表可变，不能做键。

### 错误 2：误以为 in 判断值
```python
d = {"name": "Alice"}
print("Alice" in d)  # False
```

`in` 默认判断键，不判断值。

### 错误 3：遍历时改字典大小
```python
for key in d:
    del d[key]  # 可能报错
```

更安全方式是先复制键列表：

```python
for key in list(d.keys()):
    del d[key]
```

## 12. 综合练习：成绩统计
给定多个学生成绩，统计每个分数段人数：

```python
scores = [95, 82, 59, 76, 88, 100, 45]
result = {"优秀": 0, "及格": 0, "不及格": 0}

for score in scores:
    if score >= 90:
        result["优秀"] += 1
    elif score >= 60:
        result["及格"] += 1
    else:
        result["不及格"] += 1

print(result)
```

再进一步：把每个学生姓名也保存进去，尝试输出所有不及格学生名单。

## 13. 本节总结
GESP 4级学字典，不只是记住 `{}` 和键值对，而是掌握一种组织复杂数据的方法。

必须掌握：
- 字典靠键访问值
- 键唯一且必须不可变
- `get()` 可避免 `KeyError`
- `items()` 常用于同时遍历键和值
- 字典适合记录型数据和计数问题
- 列表 + 字典可以表达真实项目中的复杂数据
"""
)
Quiz.objects.create(lesson=l4_1_1, question="d = {'a': 1}，d['b'] = 2 后 d 是？", option_a="{'a':1}", option_b="{'a':1, 'b':2}", option_c="报错", option_d="{'b':2}", correct_answer="B", explanation="新增键值对。")
Quiz.objects.create(lesson=l4_1_1, question="字典的键必须是？", option_a="可变的", option_b="不可变的", option_c="字符串", option_d="整数", correct_answer="B", explanation="不可变类型（Hashable）。")
Quiz.objects.create(lesson=l4_1_1, question="d.get('x', 0) 如果 x 不存在返回？", option_a="None", option_b="0", option_c="报错", option_d="False", correct_answer="B", explanation="返回默认值 0。")
Quiz.objects.create(lesson=l4_1_1, question="d.items() 返回什么？", option_a="键列表", option_b="值列表", option_c="键值对元组列表", option_d="字符串", correct_answer="C", explanation="键值对。")
Quiz.objects.create(lesson=l4_1_1, question="清空字典用什么方法？", option_a="delete()", option_b="clean()", option_c="clear()", option_d="empty()", correct_answer="C", explanation="clear()。")
Quiz.objects.create(lesson=l4_1_1, question="判断题：字典是有序的（Python 3.7+）。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l4_1_1, question="判断题：字典可以有重复的键。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，键唯一。")
Quiz.objects.create(lesson=l4_1_1, question="d = {'a': 1, 'b': 2}; len(d) 是？", option_a="1", option_b="2", option_c="3", option_d="0", correct_answer="B", explanation="两个键值对。")
Quiz.objects.create(lesson=l4_1_1, question="d.pop('a') 的作用是？", option_a="获取 'a' 的值", option_b="删除 'a' 并返回其值", option_c="删除 'a' 但不返回值", option_d="报错", correct_answer="B", explanation="删除并返回。")
Quiz.objects.create(lesson=l4_1_1, question="如何合并两个字典 d1 和 d2？", option_a="d1 + d2", option_b="d1.update(d2)", option_c="d1.append(d2)", option_d="d1.add(d2)", correct_answer="B", explanation="update 方法。")

# 1.2 集合 Set
l4_1_2 = create_lesson(
    chapter=ch4_1, title="1.2 集合 Set", order=2, lesson_type='code',
    code_challenge_prompt="# 集合去重\nlst = [1, 2, 2, 3, 3, 3]\ns = set(lst)\nprint(s)",
    content="""# 1.2 集合 Set

## 1. 什么是集合？
集合（set）是一种保存**不重复元素**的容器。

```python
s = {1, 2, 3}
```

集合有三个核心特点：
- 无重复：相同元素只保留一份
- 无序：不能靠下标访问
- 元素必须不可变：数字、字符串、元组可以；列表、字典不可以

注意：空集合不能写 `{}`，因为 `{}` 表示空字典。

```python
a = {}
b = set()

print(type(a))  # <class 'dict'>
print(type(b))  # <class 'set'>
```

## 2. 核心特性：去重
集合最直观的用途是去重。

```python
nums = [1, 2, 2, 3, 3, 3]
s = set(nums)
print(s)
```

输出可能是：

```text
{1, 2, 3}
```

如果需要重新变成列表：

```python
unique_nums = list(set(nums))
print(unique_nums)
```

重要提醒：集合无序，去重后元素顺序不一定和原列表一样。如果题目要求保持原顺序，需要用其他方法。

保持顺序去重：

```python
nums = [1, 2, 2, 3, 1]
seen = set()
result = []

for num in nums:
    if num not in seen:
        seen.add(num)
        result.append(num)

print(result)
```

## 3. 集合运算
集合很适合表达“共同拥有、全部拥有、只属于某一边”的问题。

```python
a = {"Alice", "Bob", "Cindy"}
b = {"Bob", "David", "Eric"}
```

### 交集：两边都有
```python
print(a & b)
```

结果：

```text
{'Bob'}
```

### 并集：合在一起
```python
print(a | b)
```

### 差集：只在 a，不在 b
```python
print(a - b)
```

### 对称差集：只在其中一边
```python
print(a ^ b)
```

记忆方法：
- `&`：共同部分
- `|`：全部合并
- `-`：减掉另一边
- `^`：两边不同部分

## 4. add、discard 与 remove
集合除了去重，还经常动态变化。

```python
s = {1, 2, 3}
s.add(4)
s.discard(2)
```

`add(x)` 添加元素：

```python
s.add(5)
```

如果元素已经存在，集合不会重复添加：

```python
s.add(5)
s.add(5)
print(s)
```

删除元素有两个常用方法：

```python
s.remove(3)
s.discard(10)
```

区别：
- `remove(x)`：如果元素不存在，会报 `KeyError`
- `discard(x)`：如果元素不存在，什么都不做

考试和实战中，如果不确定元素是否存在，优先用 `discard()`。

## 5. 成员判断：in
集合判断某个元素是否存在非常常用。

```python
visited = {"A", "B", "C"}

if "A" in visited:
    print("已经访问过")
```

集合的成员判断通常比列表更适合大量数据场景。直觉上：
- 列表：可能要从头找到尾
- 集合：更像直接查表

所以算法中常用集合保存：
- 已访问节点
- 已出现数字
- 已经处理过的用户名

## 6. 集合的典型业务场景
### 场景 1：报名名单去重
```python
names = ["Alice", "Bob", "Alice", "Cindy"]
unique_names = set(names)
print(unique_names)
```

### 场景 2：找两个班都报名的学生
```python
class_a = {"Alice", "Bob", "Cindy"}
class_b = {"Bob", "David"}

print(class_a & class_b)
```

### 场景 3：找还没完成任务的人
```python
all_students = {"Alice", "Bob", "Cindy"}
finished = {"Alice"}

not_finished = all_students - finished
print(not_finished)
```

## 7. 集合推导式
集合也支持推导式，写法类似列表推导式。

```python
nums = [1, 2, 2, 3, 4]
even_set = {x for x in nums if x % 2 == 0}
print(even_set)
```

结果：

```text
{2, 4}
```

集合推导式会自动去重。

## 8. frozenset 简介
普通集合是可变的，所以不能作为字典的键，也不能作为另一个集合的元素。

```python
s = {1, 2}
# d = {s: "value"}  # TypeError
```

`frozenset` 是不可变集合：

```python
fs = frozenset([1, 2, 3])
```

初学阶段只需知道：如果题目强调“不可变集合”，对应的是 `frozenset`。

## 9. 易错点
### 错误 1：用 `{}` 创建空集合
```python
s = {}
print(type(s))  # dict
```

正确：

```python
s = set()
```

### 错误 2：用索引访问集合
```python
s = {1, 2, 3}
print(s[0])  # TypeError
```

集合无序，不支持下标。

### 错误 3：集合里放列表
```python
s = {[1, 2], [3, 4]}  # TypeError
```

列表可变，不能作为集合元素。

### 错误 4：以为 set 去重一定保序
```python
nums = [3, 1, 2, 1]
print(list(set(nums)))
```

输出顺序不保证和原列表一致。

## 10. 综合练习：班级选课分析
有两个课程报名名单：

```python
python = {"Alice", "Bob", "Cindy", "David"}
robot = {"Bob", "David", "Eric"}
```

请输出：
1. 两门课都报名的人
2. 至少报名一门课的人
3. 只报名 Python 的人
4. 只报名一门课的人

参考：

```python
print(python & robot)
print(python | robot)
print(python - robot)
print(python ^ robot)
```

## 11. 本节总结
集合最强的地方不是“长得像大括号”，而是：
- 自动去重
- 快速判断元素是否存在
- 用交并差解决名单、标签、访问记录问题
- 不支持索引，元素必须不可变
- 空集合必须用 `set()`
"""
)
Quiz.objects.create(lesson=l4_1_2, question="创建空集合使用？", option_a="{}", option_b="[]", option_c="set()", option_d="()", correct_answer="C", explanation="{} 是空字典。")
Quiz.objects.create(lesson=l4_1_2, question="set([1, 2, 2]) 的结果？", option_a="{1, 2, 2}", option_b="{1, 2}", option_c="[1, 2]", option_d="报错", correct_answer="B", explanation="自动去重。")
Quiz.objects.create(lesson=l4_1_2, question="{1, 2} & {2, 3} 的结果？", option_a="{1, 2, 3}", option_b="{2}", option_c="{1, 3}", option_d="{}", correct_answer="B", explanation="交集。")
Quiz.objects.create(lesson=l4_1_2, question="集合中的元素必须是？", option_a="可变的", option_b="不可变的", option_c="有序的", option_d="无限制", correct_answer="B", explanation="不可变（Hashable）。")
Quiz.objects.create(lesson=l4_1_2, question="s.add(1) 的作用？", option_a="添加元素", option_b="删除元素", option_c="排序", option_d="求和", correct_answer="A", explanation="添加。")
Quiz.objects.create(lesson=l4_1_2, question="判断题：集合是有序的，可以通过索引访问。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，无序。")
Quiz.objects.create(lesson=l4_1_2, question="判断题：集合不能包含重复元素。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l4_1_2, question="s = {1, 2}; s.remove(3) 会？", option_a="什么都不做", option_b="报错 KeyError", option_c="自动添加 3", option_d="清空集合", correct_answer="B", explanation="remove 不存在的元素会报错，discard 不会。")
Quiz.objects.create(lesson=l4_1_2, question="集合支持索引吗？", option_a="支持", option_b="不支持", option_c="支持正数索引", option_d="支持负数索引", correct_answer="B", explanation="集合是无序的。")
Quiz.objects.create(lesson=l4_1_2, question="len({1, 1, 2}) 的结果是？", option_a="3", option_b="2", option_c="1", option_d="0", correct_answer="B", explanation="自动去重后只有 {1, 2}。")

ch4_2, _ = Chapter.objects.get_or_create(course=c4, title="第2章：面向对象编程 OOP", defaults={'order': 2})

# 2.1 类与对象
l4_2_1 = create_lesson(
    chapter=ch4_2, title="2.1 类与对象基础", order=1, lesson_type='text',
    code_challenge_prompt="# 定义一个 Dog 类，有一个 bark 方法\nclass Dog:\n    def bark(self):\n        print('Wang!')\n\nd = Dog()\nd.bark()",
    content="""# 2.1 类与对象基础

## 1. 为什么需要类？
前面学习列表、字典时，我们已经能保存一组数据。例如用字典表示一名学生：

```python
student = {
    "name": "Alice",
    "age": 12,
    "score": 95
}
```

如果只保存数据，字典很合适。但真实程序里，一个“学生”通常不只是数据，还会有行为：
- 查询是否及格
- 修改分数
- 打印自我介绍
- 统计等级

这时就会出现一个问题：**数据和函数分散在不同地方，程序越写越乱。**

面向对象编程（OOP）的核心思想是：把相关的数据和行为放在一起，组成一个“对象”。

## 2. 类与对象是什么？
类（Class）是创建对象的**蓝图**或**模板**。
对象（Object）是根据类创建出来的**具体实例**。

生活类比：

| 类 | 对象 |
| :--- | :--- |
| 狗 | 你家那只叫旺财的狗 |
| 学生 | 小明这名学生 |
| 游戏角色 | 当前屏幕上的某个角色 |
| 课程 | “GESP 4级：数据结构进阶”这门课 |

类描述“这一类东西有什么、能做什么”；对象是程序运行时真正存在的个体。

## 3. 定义一个最小的类
定义类使用 `class` 关键字，类名通常使用大驼峰命名法（每个单词首字母大写）。

```python
class Dog:
    def bark(self):
        print("Wang!")
```

这段代码定义了一个 `Dog` 类。类里面的函数叫**方法**。

注意缩进：
- `class Dog:` 后面的代码要缩进
- `def bark(self):` 在类里面
- `print("Wang!")` 在方法里面，所以还要再缩进

## 4. 创建对象：实例化
根据类创建对象的过程叫**实例化**。

```python
my_dog = Dog()
my_dog.bark()
```

执行过程可以这样理解：
1. `Dog` 是类
2. `Dog()` 创建一个新的 Dog 对象
3. `my_dog` 保存这个对象
4. `my_dog.bark()` 让这个对象执行 `bark` 方法

## 5. self 到底是什么？
`self` 代表“当前这个对象自己”。

```python
class Dog:
    def bark(self):
        print("Wang!")

d = Dog()
d.bark()
```

当你写：

```python
d.bark()
```

Python 会在背后理解成：

```python
Dog.bark(d)
```

也就是说，对象 `d` 会自动传给方法的第一个参数 `self`。

所以：
- 定义方法时，第一个参数通常写 `self`
- 调用方法时，不需要手动传 `self`
- `self` 不是关键字，但这是 Python 程序员共同遵守的命名习惯

## 6. 属性和方法
对象通常包含两类内容：
- **属性**：对象有什么，用变量表示
- **方法**：对象能做什么，用函数表示

例如一只狗：
- 属性：名字、年龄、品种
- 方法：叫、跑、吃东西

先看一个简单版本：

```python
class Dog:
    def set_name(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Wang!")

d = Dog()
d.set_name("Lucky")
d.bark()
```

`self.name` 是对象自己的属性。以后这个对象的其他方法也能访问它。

## 7. 多个对象互不干扰
同一个类可以创建很多个对象，每个对象都有自己的状态。

```python
class Dog:
    def set_name(self, name):
        self.name = name

    def bark(self):
        print(self.name, "says Wang!")

d1 = Dog()
d2 = Dog()

d1.set_name("Lucky")
d2.set_name("Coco")

d1.bark()
d2.bark()
```

输出：

```text
Lucky says Wang!
Coco says Wang!
```

`d1.name` 和 `d2.name` 是两个对象各自的属性，不会互相覆盖。

## 8. 类 vs 对象：考点辨析
下面这些写法意义不同：

```python
Dog       # 类本身
Dog()     # 创建一个 Dog 对象
d = Dog() # 变量 d 指向这个对象
d.bark()  # 对象调用方法
```

常见判断：
- `Dog` 是类
- `Dog()` 的结果是对象
- `type(d)` 可以查看对象属于哪个类
- 一个类可以创建多个对象

## 9. 易错点
### 错误 1：方法忘记写 self
```python
class Dog:
    def bark():
        print("Wang!")

d = Dog()
d.bark()  # TypeError
```

对象调用方法时，Python 会自动传入对象本身。如果方法没有 `self` 参数，就接不住这个对象。

### 错误 2：调用方法忘记括号
```python
d.bark    # 只是拿到方法本身，没有执行
d.bark()  # 执行方法
```

### 错误 3：先用属性，后设置属性
```python
class Dog:
    def bark(self):
        print(self.name)

d = Dog()
d.bark()  # AttributeError
```

对象还没有 `name` 属性，就不能直接访问。下一节会学习用 `__init__` 初始化属性。

## 10. 小练习：设计一个游戏角色
尝试补全下面的类：

```python
class Player:
    def set_info(self, name, hp):
        self.name = name
        self.hp = hp

    def show(self):
        print(self.name, "HP:", self.hp)

p = Player()
p.set_info("Hero", 100)
p.show()
```

思考：
- `Player` 是类还是对象？
- `p` 是类还是对象？
- `self.name` 保存在哪里？
- 如果再创建一个 `p2`，会不会影响 `p`？

## 11. 本节总结
这一节最关键的是建立面向对象直觉：
- 类是模板，对象是实例
- 方法是写在类里的函数
- 对象调用方法时会自动把自己传给 `self`
- 属性表示对象的数据，方法表示对象的行为
- 多个对象可以来自同一个类，但各自保存自己的状态
"""
)
Quiz.objects.create(lesson=l4_2_1, question="定义类使用哪个关键字？", option_a="def", option_b="class", option_c="object", option_d="struct", correct_answer="B", explanation="class。")
Quiz.objects.create(lesson=l4_2_1, question="类方法中第一个参数通常命名为？", option_a="this", option_b="me", option_c="self", option_d="obj", correct_answer="C", explanation="self。")
Quiz.objects.create(lesson=l4_2_1, question="根据类创建对象的过程叫？", option_a="初始化", option_b="实例化", option_c="抽象", option_d="继承", correct_answer="B", explanation="实例化。")
Quiz.objects.create(lesson=l4_2_1, question="Dog() 返回的是？", option_a="一个类", option_b="一个函数", option_c="一个对象", option_d="None", correct_answer="C", explanation="对象（实例）。")
Quiz.objects.create(lesson=l4_2_1, question="对象调用方法 d.bark() 等价于？", option_a="Dog.bark(d)", option_b="bark(d)", option_c="d.bark", option_d="Dog.bark()", correct_answer="A", explanation="类名.方法名(实例)。")
Quiz.objects.create(lesson=l4_2_1, question="判断题：一个类可以创建多个不同的对象。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l4_2_1, question="判断题：self 关键字是 Python 强制要求的语法，不能改名。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，约定俗成叫 self，改名也可以但强烈不推荐。")
Quiz.objects.create(lesson=l4_2_1, question="type(10) 返回的是？", option_a="<class 'int'>", option_b="int", option_c="10", option_d="Number", correct_answer="A", explanation="10 是 int 类的实例。")
Quiz.objects.create(lesson=l4_2_1, question="pass 关键字在定义空类时有用吗？", option_a="有用", option_b="没用", option_c="报错", option_d="必须用 return", correct_answer="A", explanation="占位符，保持语法完整。")
Quiz.objects.create(lesson=l4_2_1, question="面向对象的三大特征不包括？", option_a="封装", option_b="继承", option_c="多态", option_d="递归", correct_answer="D", explanation="递归是算法概念。")

# 2.2 构造函数
l4_2_2 = create_lesson(
    chapter=ch4_2, title="2.2 构造函数 __init__", order=2, lesson_type='code',
    code_challenge_prompt="# 定义 Student 类，初始化 name 和 age\nclass Student:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\ns = Student('Tom', 12)\nprint(s.name)",
    content="""# 2.2 构造函数 __init__

## 1. 上一节留下的问题
上一节我们用 `set_name()` 给对象设置属性：

```python
class Dog:
    def set_name(self, name):
        self.name = name

d = Dog()
d.set_name("Lucky")
```

这能运行，但有一个隐患：如果忘记调用 `set_name()`，对象就没有 `name` 属性。

更好的做法是：**对象一创建，就把必要属性准备好。**

## 2. __init__ 是什么？
`__init__` 是 Python 类里的特殊方法，会在创建对象时自动调用。
它通常用来初始化对象属性。

```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Alice", 12)
print(s1.name)
print(s1.age)
```

执行 `Student("Alice", 12)` 时，Python 会自动调用：

```python
Student.__init__(s1, "Alice", 12)
```

其中：
- `s1` 自动传给 `self`
- `"Alice"` 传给 `name`
- `12` 传给 `age`

## 3. 参数和属性不要混淆
看这两行：

```python
self.name = name
self.age = age
```

左边：
- `self.name`
- `self.age`

是对象属性，会长期保存在对象里。

右边：
- `name`
- `age`

是 `__init__` 的参数，只在方法执行时临时存在。

可以理解为：把外面传进来的值，存到对象自己身上。

## 4. 每个对象有独立属性
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s1 = Student("Alice", 95)
s2 = Student("Bob", 80)

print(s1.name, s1.score)
print(s2.name, s2.score)
```

`s1` 和 `s2` 都来自 `Student` 类，但它们保存的数据不同。

修改一个对象，不影响另一个对象：

```python
s1.score = 100
print(s1.score)  # 100
print(s2.score)  # 80
```

这就是实例属性的独立性。

## 5. 给类添加行为
类不只是保存数据，还应该提供和数据相关的方法。

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def is_passed(self):
        return self.score >= 60

    def introduce(self):
        return f"{self.name} 的成绩是 {self.score}"

s = Student("Alice", 95)
print(s.introduce())
print(s.is_passed())
```

这里：
- `name`、`score` 是属性
- `is_passed()`、`introduce()` 是方法
- 方法通过 `self.score` 读取对象自己的成绩

## 6. __init__ 不是“构造函数返回对象”
严格来说，`__init__` 负责初始化对象，不负责创建对象。
对象创建由 Python 自动完成，`__init__` 只是在对象创建后补充初始数据。

所以 `__init__` 不能返回其他值：

```python
class Student:
    def __init__(self, name):
        self.name = name
        return name  # 错误
```

`__init__` 应该返回 `None`。平时不要写 `return`。

## 7. __str__：让对象打印得更友好
如果直接打印对象，结果通常不够直观：

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

s = Student("Alice", 95)
print(s)
```

可能输出类似：

```text
<__main__.Student object at 0x...>
```

可以定义 `__str__`：

```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"Student(name={self.name}, score={self.score})"

s = Student("Alice", 95)
print(s)
```

输出：

```text
Student(name=Alice, score=95)
```

`__str__` 适合给对象提供人类可读的文本表示。

## 8. 类属性 vs 实例属性
初学阶段最重要的是实例属性，也就是写在 `self` 上的属性：

```python
self.name = name
```

它属于某一个具体对象。

还有一种写在类里面、方法外面的变量，叫类属性：

```python
class Student:
    school = "PyMaster"

    def __init__(self, name):
        self.name = name
```

`school` 属于类，通常表示所有对象共享的信息。
`name` 属于对象，每个对象可以不同。

本阶段先记住：
- 会变化、每个对象不同的数据，放到 `self.xxx`
- 所有对象共用的数据，才考虑类属性

## 9. 常见错误
### 错误 1：创建对象时参数数量不匹配
```python
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("Tom")  # 少传 age，TypeError
```

`__init__` 除了 `self` 之外需要几个参数，创建对象时就要传几个参数。

### 错误 2：把属性写成局部变量
```python
class Student:
    def __init__(self, name):
        name = name  # 错误：没有保存到对象上
```

应写成：

```python
self.name = name
```

### 错误 3：在类外访问属性时忘记对象名
```python
s = Student("Tom", 12)
print(name)    # 错误
print(s.name)  # 正确
```

属性属于对象，要通过 `对象.属性` 访问。

## 10. 综合练习：BankAccount
写一个银行账户类：

```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("余额不足")

    def show(self):
        print(self.owner, "余额:", self.balance)

account = BankAccount("Alice", 100)
account.deposit(50)
account.withdraw(30)
account.show()
```

思考：
- 哪些是属性？
- 哪些是方法？
- `deposit` 为什么要修改 `self.balance`？
- 如果再创建一个账户，对当前账户余额有没有影响？

## 11. 本节总结
`__init__` 的核心不是背语法，而是让对象一创建就处于可用状态。

必须掌握：
- `__init__` 创建对象时自动调用
- `self.xxx` 是实例属性
- 不同对象的实例属性互不干扰
- 方法通过 `self` 访问和修改对象自己的数据
- `__str__` 可以控制对象被打印时的显示内容
"""
)
Quiz.objects.create(lesson=l4_2_2, question="构造函数的名字是？", option_a="init", option_b="__init__", option_c="start", option_d="create", correct_answer="B", explanation="__init__。")
Quiz.objects.create(lesson=l4_2_2, question="__init__ 什么时候被调用？", option_a="类定义时", option_b="创建对象时", option_c="手动调用时", option_d="程序结束时", correct_answer="B", explanation="创建对象时自动调用。")
Quiz.objects.create(lesson=l4_2_2, question="self.age = age 的作用是？", option_a="定义局部变量", option_b="定义全局变量", option_c="定义对象属性", option_d="无作用", correct_answer="C", explanation="给对象绑定属性。")
Quiz.objects.create(lesson=l4_2_2, question="s = Student('Tom') 会调用？", option_a="Student.Tom()", option_b="__init__('Tom')", option_c="__init__(s, 'Tom')", option_d="start()", correct_answer="C", explanation="自动传入 self。")
Quiz.objects.create(lesson=l4_2_2, question="在类外部访问属性使用？", option_a=".", option_b="->", option_c="::", option_d="[]", correct_answer="A", explanation="点号。")
Quiz.objects.create(lesson=l4_2_2, question="判断题：__init__ 方法必须有返回值。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，不能有返回值（只能返回 None）。")
Quiz.objects.create(lesson=l4_2_2, question="判断题：不同对象的同名属性互不干扰。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l4_2_2, question="析构函数的名字是？", option_a="__del__", option_b="__init__", option_c="__end__", option_d="__destruct__", correct_answer="A", explanation="__del__。")
Quiz.objects.create(lesson=l4_2_2, question="s.age = 13 是修改谁的属性？", option_a="类", option_b="对象 s", option_c="所有对象", option_d="全局变量", correct_answer="B", explanation="实例属性。")
Quiz.objects.create(lesson=l4_2_2, question="__str__ 方法的作用是？", option_a="字符串转对象", option_b="对象转字符串（打印时显示）", option_c="构造函数", option_d="析构函数", correct_answer="B", explanation="定义对象的字符串表示。")


# ==========================================
# Course 5: Python 应用进阶 - 数据分析与可视化
# ==========================================
print("正在创建 Python 应用进阶 课程...")
c4a, _ = Course.objects.get_or_create(
    title="Python 应用进阶：数据分析与可视化",
    description="在进入算法学习之前，先掌握 NumPy、Pandas 与 Matplotlib 三大常用库，建立数组计算、表格处理和数据可视化的应用能力。",
    defaults={'order': 5}
)
c4a.order = 5
c4a.save(update_fields=['order'])

ch4a_1, _ = Chapter.objects.get_or_create(course=c4a, title="第1章：NumPy 数组计算", defaults={'order': 1})

l4a_1_1 = create_lesson(
    chapter=ch4a_1, title="1.1 NumPy 与 ndarray 入门", order=1, lesson_type='text',
    code_challenge_prompt="# 观察 NumPy 数组的基本写法\n# import numpy as np\n# arr = np.array([1, 2, 3, 4])\n# print(arr)\nprint('理解 ndarray 与 list 的区别')",
    content="""# 1.1 NumPy 与 ndarray 入门

## 1. 为什么需要 NumPy？
普通列表适合基础学习，但如果要处理大量数值数据，NumPy 会更高效、更方便。

## 2. ndarray 是什么？
NumPy 的核心对象叫 `ndarray`，可以理解为“多维数组”。

```python
import numpy as np
arr = np.array([1, 2, 3, 4])
```

## 3. 和列表有什么区别？
- list：更通用，元素类型可以不同
- ndarray：更适合数值计算，通常元素类型统一

## 4. 常见应用
- 成绩统计
- 图像像素处理
- 科学计算
- 算法数据预处理

## 5. 创建数组的常见方式
```python
import numpy as np

a = np.array([1, 2, 3])
b = np.zeros(5)
c = np.ones(3)
d = np.arange(0, 10, 2)
```

常见含义：
- `array()`：把列表转换成数组
- `zeros()`：创建全 0 数组
- `ones()`：创建全 1 数组
- `arange()`：生成等差数字序列，类似 `range`

## 6. dtype：数组元素类型
NumPy 数组通常要求元素类型统一。

```python
arr = np.array([1, 2, 3])
print(arr.dtype)
```

如果数组中混入浮点数，NumPy 可能自动提升类型：

```python
arr = np.array([1, 2, 3.5])
print(arr.dtype)
```

这和普通列表不同。列表可以同时放字符串、数字、布尔值，但数值计算时，统一类型更高效。

## 7. 向量化思维
NumPy 最重要的思维是：对整组数据一起运算，而不是手写循环。

```python
scores = np.array([80, 90, 100])
print(scores + 5)
```

输出：

```text
[ 85  95 105]
```

如果用列表，需要写循环；NumPy 可以直接表达“每个元素都加 5”。

## 8. 易错点
- `np.array([1, 2, 3])` 不是普通列表
- `arr + 10` 是逐元素加法，不是拼接
- NumPy 常用别名是 `np`
- 真实运行 NumPy 代码前，需要先安装 `numpy`

## 9. 小练习
创建一个成绩数组 `[70, 85, 90, 100]`，输出：
1. 每个成绩加 5 分后的结果
2. 数组的平均分
3. 数组的数据类型
"""
)
Quiz.objects.create(lesson=l4a_1_1, question="NumPy 中最核心的数据对象通常是？", option_a="dict", option_b="tuple", option_c="ndarray", option_d="set", correct_answer="C", explanation="NumPy 的核心对象是 ndarray。")
Quiz.objects.create(lesson=l4a_1_1, question="NumPy 最适合处理哪类数据？", option_a="大量数值数据", option_b="网页标签", option_c="图片文字排版", option_d="系统服务", correct_answer="A", explanation="NumPy 最擅长数值计算。")
Quiz.objects.create(lesson=l4a_1_1, question="import numpy as np 中 np 是什么？", option_a="函数", option_b="异常", option_c="别名", option_d="类名", correct_answer="C", explanation="通常使用 np 作为 numpy 的别名。")
Quiz.objects.create(lesson=l4a_1_1, question="列表和 ndarray 的一个重要区别是？", option_a="列表不能存数字", option_b="ndarray 更适合统一类型的数值运算", option_c="列表不能遍历", option_d="ndarray 不能切片", correct_answer="B", explanation="ndarray 更适合做统一数值运算。")
Quiz.objects.create(lesson=l4a_1_1, question="判断题：NumPy 经常用于科学计算与数据处理。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l4a_1_1, question="判断题：普通 Python 列表已经完全覆盖了 NumPy 的所有优势。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，NumPy 在数值处理方面更强。")

l4a_1_2 = create_lesson(
    chapter=ch4a_1, title="1.2 数组形状、索引与运算", order=2, lesson_type='text',
    code_challenge_prompt="# 观察二维数组和形状\n# import numpy as np\n# arr = np.array([[1, 2], [3, 4]])\n# print(arr.shape)\nprint('理解 shape、索引和逐元素运算')",
    content="""# 1.2 数组形状、索引与运算

## 1. shape 表示什么？
数组的形状代表“有几行几列”。

```python
arr = np.array([[1, 2], [3, 4]])
print(arr.shape)   # (2, 2)
```

## 2. 索引访问
```python
print(arr[0, 1])   # 第一行第二列
```

## 3. NumPy 的强项：逐元素运算
```python
arr = np.array([1, 2, 3])
print(arr + 10)    # [11 12 13]
print(arr * 2)     # [2 4 6]
```

## 4. 为什么这很重要？
因为数据处理中经常要对一整列数据一起加减乘除，而不是一个个写循环。

## 5. 一维数组和二维数组
一维数组像一排数据：

```python
arr = np.array([10, 20, 30])
```

二维数组像表格：

```python
table = np.array([
    [80, 90],
    [70, 85],
    [95, 100]
])
```

`shape` 能告诉我们结构：

```python
print(arr.shape)    # (3,)
print(table.shape)  # (3, 2)
```

`(3, 2)` 表示 3 行 2 列。

## 6. 切片
NumPy 支持类似列表的切片：

```python
arr = np.array([10, 20, 30, 40])
print(arr[1:3])
```

二维数组可以按行列切片：

```python
print(table[0])      # 第 1 行
print(table[:, 0])   # 第 1 列
```

`:` 表示“这一维全选”。

## 7. 常见统计
```python
scores = np.array([80, 90, 100])

print(scores.mean())
print(scores.max())
print(scores.min())
print(scores.sum())
```

这些方法常用于成绩、销量、温度等数值数据分析。

## 8. 易错点
- `arr[0, 1]` 用于二维数组，表示第 0 行第 1 列
- Python 索引仍然从 0 开始
- `shape` 是属性，不是方法，不写 `shape()`
- 数组维度越高，越要先看 `shape`

## 9. 小练习
给定二维数组：

```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
```

请输出：
1. 数组形状
2. 第一行
3. 第二列
4. 所有元素乘以 10 后的结果
"""
)
Quiz.objects.create(lesson=l4a_1_2, question="shape=(2, 3) 通常表示？", option_a="2 行 3 列", option_b="3 行 2 列", option_c="2 个元素", option_d="3 个维度", correct_answer="A", explanation="二维数组中通常表示 2 行 3 列。")
Quiz.objects.create(lesson=l4a_1_2, question="arr[0, 1] 表示？", option_a="第 0 行第 1 列", option_b="第 1 行第 0 列", option_c="第 0 列第 1 行", option_d="切片", correct_answer="A", explanation="二维数组按 行、列 访问。")
Quiz.objects.create(lesson=l4a_1_2, question="NumPy 中 arr + 10 常表示？", option_a="给数组每个元素都加 10", option_b="只给第一个元素加 10", option_c="报错", option_d="把 10 拼接到数组后面", correct_answer="A", explanation="这是逐元素运算。")
Quiz.objects.create(lesson=l4a_1_2, question="NumPy 在批量数值处理中的优势主要来自？", option_a="逐元素运算方便", option_b="不能做切片", option_c="必须手写循环", option_d="不支持二维数组", correct_answer="A", explanation="逐元素运算是它的重要优势。")
Quiz.objects.create(lesson=l4a_1_2, question="判断题：二维数组可以看成表格。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，很像一个表格。")
Quiz.objects.create(lesson=l4a_1_2, question="判断题：NumPy 不支持多维数组。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，NumPy 非常擅长多维数组。")

ch4a_2, _ = Chapter.objects.get_or_create(course=c4a, title="第2章：Pandas 表格处理", defaults={'order': 2})

l4a_2_1 = create_lesson(
    chapter=ch4a_2, title="2.1 Series 与 DataFrame", order=1, lesson_type='text',
    code_challenge_prompt="# 认识 DataFrame 的基本结构\n# import pandas as pd\n# df = pd.DataFrame({'name': ['Tom', 'Amy'], 'score': [90, 95]})\n# print(df)\nprint('理解 DataFrame 像一张表')",
    content="""# 2.1 Series 与 DataFrame

## 1. Pandas 是做什么的？
Pandas 专门用于处理“表格型数据”。

## 2. 两个核心对象
- `Series`：一列数据
- `DataFrame`：多列组成的一张表

```python
import pandas as pd
df = pd.DataFrame({
    "name": ["Tom", "Amy"],
    "score": [90, 95]
})
```

## 3. 为什么 DataFrame 很重要？
它和 Excel 表格很像，非常适合：
- 成绩表
- 销售表
- 考勤表
- 统计结果表

## 4. Series 更像“一列”
```python
scores = pd.Series([90, 85, 100])
print(scores)
```

`Series` 可以理解成带索引的一列数据。

## 5. DataFrame 更像“一张表”
```python
df = pd.DataFrame({
    "name": ["Tom", "Amy", "Jack"],
    "score": [90, 95, 82],
    "passed": [True, True, True]
})
```

每一列可以有自己的含义。你可以把它理解成 Python 里的迷你 Excel。

## 6. 查看数据
```python
print(df.head())
print(df.shape)
print(df.columns)
```

常见含义：
- `head()`：查看前几行
- `shape`：查看行数和列数
- `columns`：查看列名

## 7. 为什么不用普通字典就够了？
字典能表达表格，但 Pandas 提供更多表格操作：
- 选列
- 筛选行
- 分组统计
- 读取 CSV
- 处理缺失值
- 画图前整理数据

## 8. 易错点
- DataFrame 的每列长度要一致
- 选列用 `df["列名"]`
- `shape` 是属性，不是函数
- Pandas 常用别名是 `pd`

## 9. 小练习
创建一张包含 `name`、`age`、`score` 三列的 DataFrame，输出：
1. 前 5 行
2. 所有列名
3. 表格形状
"""
)
Quiz.objects.create(lesson=l4a_2_1, question="Pandas 中最像“整张表”的对象是？", option_a="Series", option_b="DataFrame", option_c="tuple", option_d="set", correct_answer="B", explanation="DataFrame 就像一张表。")
Quiz.objects.create(lesson=l4a_2_1, question="Series 更像什么？", option_a="一列数据", option_b="一整个项目", option_c="一幅图像", option_d="一个模块", correct_answer="A", explanation="Series 可以理解为一列数据。")
Quiz.objects.create(lesson=l4a_2_1, question="Pandas 最适合处理哪类数据？", option_a="表格数据", option_b="声音数据", option_c="操作系统内核", option_d="网页动画", correct_answer="A", explanation="Pandas 擅长表格型数据。")
Quiz.objects.create(lesson=l4a_2_1, question="DataFrame 和什么最像？", option_a="游戏地图", option_b="Excel 表格", option_c="栈结构", option_d="递归树", correct_answer="B", explanation="DataFrame 很像 Excel 表格。")
Quiz.objects.create(lesson=l4a_2_1, question="判断题：Pandas 常用于成绩表、销售表等数据处理。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l4a_2_1, question="判断题：DataFrame 只能有一列。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，DataFrame 可以有多列。")

l4a_2_2 = create_lesson(
    chapter=ch4a_2, title="2.2 选列、筛选与基础统计", order=2, lesson_type='text',
    code_challenge_prompt="# 观察常见 Pandas 操作\n# df['score']\n# df[df['score'] >= 60]\n# df['score'].mean()\nprint('理解选列、筛选和平均值统计')",
    content="""# 2.2 选列、筛选与基础统计

## 1. 选列
```python
df["score"]
```

## 2. 条件筛选
```python
df[df["score"] >= 60]
```

## 3. 基础统计
```python
df["score"].mean()
df["score"].max()
df["score"].min()
```

## 4. 为什么这很重要？
这些操作就是最基础的数据分析流程：
- 看某一列
- 找满足条件的数据
- 算平均值、最大值、最小值

## 5. 选多列
选择一列时使用一个列名：

```python
df["score"]
```

选择多列时，里面要再放一个列表：

```python
df[["name", "score"]]
```

注意这里是两层方括号。

## 6. 条件筛选的过程
```python
df["score"] >= 60
```

这一步会得到一列布尔值：

```text
True
False
True
```

再把它放回 `df[...]`，就能筛选出满足条件的行：

```python
passed = df[df["score"] >= 60]
```

## 7. 多条件筛选
Pandas 中多个条件要加括号：

```python
good = df[(df["score"] >= 80) & (df["age"] <= 15)]
```

常用符号：
- `&` 表示并且
- `|` 表示或者
- 每个条件外面都要加括号

## 8. 基础统计速查
```python
df["score"].mean()
df["score"].max()
df["score"].min()
df["score"].sum()
df["score"].count()
```

## 9. 易错点
- Pandas 多条件筛选不能直接用 `and` / `or`
- 多条件必须加括号
- `df["score"]` 返回一列，不是单个数字
- `mean()` 会忽略空值，但初学阶段先保证数据完整

## 10. 小练习
给定成绩表，完成：
1. 输出 `name` 和 `score` 两列
2. 筛选出及格学生
3. 计算平均分
4. 找出最高分
"""
)
Quiz.objects.create(lesson=l4a_2_2, question="df['score'] 通常表示？", option_a="选择 score 这一列", option_b="删除 score 列", option_c="给 score 赋值", option_d="创建新表", correct_answer="A", explanation="这是最常见的选列方式。")
Quiz.objects.create(lesson=l4a_2_2, question="df[df['score'] >= 60] 的作用是？", option_a="筛选及格的数据", option_b="删除所有数据", option_c="统计总人数", option_d="排序", correct_answer="A", explanation="这是条件筛选。")
Quiz.objects.create(lesson=l4a_2_2, question="mean() 常用来做什么？", option_a="求平均值", option_b="求最大值", option_c="求行数", option_d="转成字符串", correct_answer="A", explanation="mean 就是平均值。")
Quiz.objects.create(lesson=l4a_2_2, question="基础数据分析流程通常不包括？", option_a="选列", option_b="筛选", option_c="统计", option_d="编译内核", correct_answer="D", explanation="这不属于基础数据分析。")
Quiz.objects.create(lesson=l4a_2_2, question="判断题：Pandas 可以方便地统计成绩平均分。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l4a_2_2, question="判断题：条件筛选只在 NumPy 中存在，Pandas 不能用。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，Pandas 非常常用条件筛选。")

ch4a_3, _ = Chapter.objects.get_or_create(course=c4a, title="第3章：Matplotlib 数据可视化", defaults={'order': 3})

l4a_3_1 = create_lesson(
    chapter=ch4a_3, title="3.1 折线图与柱状图", order=1, lesson_type='text',
    code_challenge_prompt="# 认识最常见的图表类型\n# import matplotlib.pyplot as plt\n# plt.plot([1, 2, 3], [80, 85, 90])\n# plt.bar(['Tom', 'Amy'], [90, 95])\nprint('理解 plot 和 bar 的区别')",
    content="""# 3.1 折线图与柱状图

## 1. Matplotlib 是什么？
Matplotlib 是 Python 最常见的绘图库之一。

## 2. 折线图
适合展示趋势变化，例如每天温度、每次考试成绩变化。

```python
plt.plot([1, 2, 3], [80, 85, 90])
```

## 3. 柱状图
适合比较不同类别，例如不同同学的成绩。

```python
plt.bar(["Tom", "Amy"], [90, 95])
```

## 4. 什么时候用哪种图？
- 看趋势：折线图
- 看比较：柱状图

## 5. 折线图完整示例
```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temps = [20, 22, 21, 25, 24]

plt.plot(days, temps)
plt.show()
```

折线图重点表达“变化”，横轴通常是时间、次数、阶段。

## 6. 柱状图完整示例
```python
names = ["Tom", "Amy", "Jack"]
scores = [90, 95, 82]

plt.bar(names, scores)
plt.show()
```

柱状图重点表达“比较”，横轴通常是类别。

## 7. plt.show() 的作用
`plt.show()` 用来显示图表。很多环境中，如果不写它，图可能不会弹出来。

## 8. 易错点
- `plot(x, y)` 中 x 和 y 的长度要一致
- `bar(names, scores)` 中类别和数值要一一对应
- 画图前通常要先导入 `matplotlib.pyplot as plt`
- 图表不是越复杂越好，能说明问题最重要

## 9. 小练习
用折线图展示 5 次考试成绩变化；再用柱状图比较 3 名同学的成绩。
"""
)
Quiz.objects.create(lesson=l4a_3_1, question="想观察成绩随时间的变化趋势，通常用哪种图？", option_a="折线图", option_b="柱状图", option_c="饼图", option_d="散点图", correct_answer="A", explanation="趋势最适合折线图。")
Quiz.objects.create(lesson=l4a_3_1, question="想比较不同同学的分数高低，通常用哪种图？", option_a="折线图", option_b="柱状图", option_c="流程图", option_d="树图", correct_answer="B", explanation="柱状图适合做类别比较。")
Quiz.objects.create(lesson=l4a_3_1, question="Matplotlib 最主要的作用是？", option_a="数据可视化", option_b="数据库管理", option_c="网络通信", option_d="异常处理", correct_answer="A", explanation="Matplotlib 用来画图。")
Quiz.objects.create(lesson=l4a_3_1, question="plot 常用于？", option_a="趋势图", option_b="删除数据", option_c="创建字典", option_d="导入模块", correct_answer="A", explanation="plot 常用于绘制折线图。")
Quiz.objects.create(lesson=l4a_3_1, question="判断题：柱状图适合比较不同类别的数值。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l4a_3_1, question="判断题：折线图特别适合展示连续变化趋势。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")

l4a_3_2 = create_lesson(
    chapter=ch4a_3, title="3.2 标题、坐标轴与图例", order=2, lesson_type='text',
    code_challenge_prompt="# 观察图表的常见美化设置\n# plt.title('成绩变化')\n# plt.xlabel('次数')\n# plt.ylabel('分数')\n# plt.legend()\nprint('理解标题、坐标轴和图例的作用')",
    content="""# 3.2 标题、坐标轴与图例

## 1. 图表不仅要画出来，还要看得懂
如果没有标题和坐标轴说明，别人可能不知道这张图在表达什么。

## 2. 常见设置
```python
plt.title("成绩变化")
plt.xlabel("次数")
plt.ylabel("分数")
plt.legend()
```

## 3. 这些元素的作用
- `title`：告诉读者这张图讲什么
- `xlabel / ylabel`：说明横纵坐标的含义
- `legend`：区分不同数据系列

## 4. 好图表的标准
不仅要“能画”，更要“表达清楚”。

## 5. 图例 legend 怎么用
当一张图里有多条线时，需要给每条线设置 `label`：

```python
plt.plot([1, 2, 3], [80, 85, 90], label="Tom")
plt.plot([1, 2, 3], [70, 88, 92], label="Amy")
plt.legend()
```

`legend()` 会显示图例，让读者知道每条线代表谁。

## 6. 设置颜色和标记
```python
plt.plot([1, 2, 3], [80, 85, 90], color="red", marker="o")
```

初学阶段不必追求花哨，但可以知道：
- `color` 控制颜色
- `marker` 控制点的样式

## 7. 保存图片
```python
plt.savefig("score.png")
```

如果要把分析结果发给别人，保存图片很有用。

## 8. 易错点
- 标题和坐标轴不是装饰，是帮助读者理解
- 图例必须配合 `label` 才有意义
- 保存图片通常要在 `show()` 前调用
- 中文显示可能需要额外字体设置，本课先关注图表结构

## 9. 小练习
画出两名同学三次考试成绩变化图，要求包含：
1. 标题
2. 横轴名称
3. 纵轴名称
4. 图例
"""
)
Quiz.objects.create(lesson=l4a_3_2, question="title() 主要用来？", option_a="设置图表标题", option_b="删除图像", option_c="保存文件", option_d="创建数组", correct_answer="A", explanation="title 用来设置图表标题。")
Quiz.objects.create(lesson=l4a_3_2, question="xlabel() 和 ylabel() 的作用是？", option_a="删除坐标轴", option_b="说明横纵坐标含义", option_c="旋转图像", option_d="生成数据", correct_answer="B", explanation="它们负责标注坐标轴。")
Quiz.objects.create(lesson=l4a_3_2, question="legend() 常用于？", option_a="显示图例", option_b="关闭图表", option_c="创建柱状图", option_d="异常处理", correct_answer="A", explanation="legend 用于图例说明。")
Quiz.objects.create(lesson=l4a_3_2, question="好图表最重要的一点是？", option_a="颜色越多越好", option_b="表达清楚", option_c="越复杂越好", option_d="越大越好", correct_answer="B", explanation="图表的核心是清晰表达信息。")
Quiz.objects.create(lesson=l4a_3_2, question="判断题：没有坐标轴说明，图表的可读性通常会下降。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l4a_3_2, question="判断题：图例可以帮助读者区分不同数据系列。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")

ch4a_4, _ = Chapter.objects.get_or_create(course=c4a, title="第4章：综合实战", defaults={'order': 4})

l4a_4_1 = create_lesson(
    chapter=ch4a_4, title="4.1 用 Pandas + Matplotlib 分析成绩表", order=1, lesson_type='text',
    code_challenge_prompt="# 思考综合流程：读表 -> 统计 -> 画图\n# import pandas as pd\n# import matplotlib.pyplot as plt\n# df = pd.DataFrame({'name': ['Tom', 'Amy'], 'score': [90, 95]})\n# print(df['score'].mean())\nprint('理解完整的数据分析流程')",
    content="""# 4.1 用 Pandas + Matplotlib 分析成绩表

## 1. 一个完整的小流程
这门课的最终目标不是记住几个库名，而是知道如何把它们连起来用。

## 2. 常见流程
1. 用 Pandas 读入或构造成绩表  
2. 选出需要分析的列  
3. 统计平均分、最高分、最低分  
4. 用 Matplotlib 画出柱状图或折线图

## 3. 示例思路
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "name": ["Tom", "Amy", "Lily"],
    "score": [90, 95, 88]
})

print(df["score"].mean())
plt.bar(df["name"], df["score"])
```

## 4. 为什么放在算法前？
因为你会先看到“Python 解决真实问题”的样子，再进入更抽象的算法学习，会更有动力。

## 5. 从原始数据到结论
真实数据分析不只是写代码，而是按步骤得到结论：
1. 准备数据
2. 检查数据
3. 筛选或清洗
4. 统计指标
5. 用图表表达
6. 写出结论

例如：平均分是多少？谁最高？有多少人不及格？图表是否显示某种趋势？

## 6. 完整示例
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "name": ["Tom", "Amy", "Lily", "Jack"],
    "score": [90, 95, 58, 76]
})

passed = df[df["score"] >= 60]
print("平均分:", df["score"].mean())
print("及格人数:", len(passed))

plt.bar(df["name"], df["score"])
plt.title("Score Report")
plt.xlabel("Name")
plt.ylabel("Score")
plt.show()
```

## 7. 可以继续升级什么？
- 从 CSV 文件读取成绩表
- 增加是否及格列
- 按分数排序
- 输出最高分学生
- 保存图表到图片

## 8. 易错点
- 先处理数据，再画图
- 图表必须对应真实数据列
- 不要只输出数字，还要说明数字代表什么
- 变量名要表达含义，例如 `passed` 比 `x` 更清楚

## 9. 综合练习
用 DataFrame 保存 5 名同学成绩，完成：
1. 输出平均分
2. 筛选不及格学生
3. 按成绩画柱状图
4. 给图表加标题和坐标轴
"""
)
Quiz.objects.create(lesson=l4a_4_1, question="完整的数据分析流程中，通常先做什么？", option_a="先画图", option_b="先读取或准备数据", option_c="先删除数据", option_d="先写递归", correct_answer="B", explanation="分析之前要先有数据。")
Quiz.objects.create(lesson=l4a_4_1, question="想统计成绩平均分，最常用的库更偏向？", option_a="Pandas", option_b="Matplotlib", option_c="random", option_d="sys", correct_answer="A", explanation="Pandas 更适合做表格统计。")
Quiz.objects.create(lesson=l4a_4_1, question="想把成绩画成图，最常用的库更偏向？", option_a="NumPy", option_b="Matplotlib", option_c="collections", option_d="time", correct_answer="B", explanation="Matplotlib 负责可视化。")
Quiz.objects.create(lesson=l4a_4_1, question="为什么把这门课放在算法前？", option_a="因为这些库比算法更难", option_b="先建立真实应用场景，再进入算法", option_c="为了减少章节数", option_d="为了替代 GESP", correct_answer="B", explanation="这是更自然的学习路径。")
Quiz.objects.create(lesson=l4a_4_1, question="判断题：Pandas 和 Matplotlib 可以配合使用。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，常常一起用。")
Quiz.objects.create(lesson=l4a_4_1, question="判断题：这门课的目标之一是让学生看到 Python 的实际应用价值。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")


# ==========================================
# Course 6: GESP 5级 - 算法基础
# ==========================================
print("正在创建 GESP 5级 课程...")
c5, _ = Course.objects.get_or_create(
    title="GESP 5级：算法基础",
    description="进入算法的世界。学习算法复杂度分析、基础排序算法（冒泡、选择、插入）和查找算法（二分查找），培养计算思维。",
    defaults={'order': 5}
)
c5.order = 6
c5.save(update_fields=['order'])

ch5_1, _ = Chapter.objects.get_or_create(course=c5, title="第1章：算法复杂度", defaults={'order': 1})
l5_1_1 = create_lesson(
    chapter=ch5_1, title="1.1 时间复杂度 Big O", order=1, lesson_type='text',
    code_challenge_prompt="# 写一个 O(n) 的循环\nn = 10\nfor i in range(n):\n    print(i)",
    content="""# 1.1 时间复杂度 Big O

## 1. 怎么衡量算法快慢？
不是看运行了多少秒，而是看**操作次数随数据量 n 的增长趋势**。

## 2. 常见复杂度
- **O(1)**: 常数级。一次搞定。 `a = lst[0]`
- **O(n)**: 线性级。循环一遍。 `for i in range(n)`
- **O(n^2)**: 平方级。双重循环。 `for i... for j...`
- **O(log n)**: 对数级。二分查找。

## 3. 空间复杂度
算法运行需要占用的额外内存空间。

## 4. 为什么不看“跑了几秒”
同一个算法在不同电脑上运行，秒数可能不同；  
但如果数据量从 `n` 变成 `10n`，算法增长得快不快，这才是更稳定、更重要的判断标准。

所以复杂度分析关注的是：
- 数据规模变大时会怎样
- 循环层数会不会变多
- 操作次数是线性增长还是平方增长

## 5. 常数、系数和低阶项为什么常被忽略
例如：
- `O(2n)` 记作 `O(n)`
- `O(n + 100)` 也常记作 `O(n)`

因为当 `n` 很大时，真正决定趋势的是“最高增长项”。

## 6. 一个直觉对比
如果 `n = 10000`：
- `O(n)` 大约处理一万次
- `O(n^2)` 大约处理一亿次

这就是为什么算法复杂度在数据量大时特别关键。

## 7. 本节总结
这一节真正要建立的不是死记符号，而是复杂度直觉：
- 单层循环常常是 `O(n)`
- 双层嵌套循环常常是 `O(n^2)`
- 每次减半的问题常常会出现 `O(log n)`

## 8. 如何快速估算
看代码时先找最主要的重复结构：

```python
for i in range(n):
    print(i)
```

一层循环，约执行 `n` 次，是 `O(n)`。

```python
for i in range(n):
    for j in range(n):
        print(i, j)
```

两层嵌套，各执行 `n` 次，总体约 `n * n`，是 `O(n^2)`。

## 9. 小练习
判断下面代码复杂度：

```python
for i in range(n):
    print(i)

for j in range(n):
    print(j)
```

答案是 `O(n)`，不是 `O(2n)`，因为常数系数会被忽略。
"""
)
Quiz.objects.create(lesson=l5_1_1, question="访问列表索引 a[i] 的时间复杂度？", option_a="O(1)", option_b="O(n)", option_c="O(log n)", option_d="O(n^2)", correct_answer="A", explanation="数组索引访问是常数时间。")
Quiz.objects.create(lesson=l5_1_1, question="单层 for 循环遍历 n 个元素的时间复杂度？", option_a="O(1)", option_b="O(n)", option_c="O(n^2)", option_d="O(log n)", correct_answer="B", explanation="线性时间。")
Quiz.objects.create(lesson=l5_1_1, question="双层嵌套循环通常是？", option_a="O(n)", option_b="O(n^2)", option_c="O(log n)", option_d="O(1)", correct_answer="B", explanation="平方级。")
Quiz.objects.create(lesson=l5_1_1, question="二分查找的复杂度？", option_a="O(n)", option_b="O(log n)", option_c="O(1)", option_d="O(n^2)", correct_answer="B", explanation="对数级。")
Quiz.objects.create(lesson=l5_1_1, question="Big O 表示的是算法的？", option_a="最好情况", option_b="最坏情况", option_c="平均情况", option_d="具体秒数", correct_answer="B", explanation="通常指最坏情况的上界。")
Quiz.objects.create(lesson=l5_1_1, question="判断题：O(1) 的算法一定比 O(n) 快。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，n 很小时不一定，但在 n 很大时 O(1) 更优。")
Quiz.objects.create(lesson=l5_1_1, question="判断题：空间复杂度是指代码文件的字节大小。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，是指运行时占用的内存。")
Quiz.objects.create(lesson=l5_1_1, question="O(1) 叫做？", option_a="常数复杂度", option_b="线性复杂度", option_c="对数复杂度", option_d="指数复杂度", correct_answer="A", explanation="常数级。")
Quiz.objects.create(lesson=l5_1_1, question="归并排序的时间复杂度是？", option_a="O(n^2)", option_b="O(n log n)", option_c="O(n)", option_d="O(1)", correct_answer="B", explanation="线性对数级。")
Quiz.objects.create(lesson=l5_1_1, question="O(2n) 和 O(n) 在复杂度分析中一样吗？", option_a="一样", option_b="不一样", option_c="O(2n) 更慢", option_d="O(n) 更慢", correct_answer="A", explanation="常数系数忽略。")

l5_1_2 = create_lesson(
    chapter=ch5_1, title="1.2 空间复杂度与复杂度估算", order=2, lesson_type='text',
    code_challenge_prompt="# 观察下面代码额外申请了多少空间\nnums = [1, 2, 3, 4]\ncopy_nums = nums[:]\nprint(len(copy_nums))",
    content="""# 1.2 空间复杂度与复杂度估算

## 1. 什么是空间复杂度？
空间复杂度关注的是：算法运行时，**额外**需要多少内存。

注意，不是代码文件有多大，也不是电脑内存总大小，而是程序执行过程中多申请了多少辅助空间。

## 2. 常见空间复杂度直觉
- `O(1)`：只用了少量额外变量
- `O(n)`：额外开了一个和输入规模差不多的数组/列表
- `O(log n)`：常见于递归调用栈比较浅的情况

## 3. 例子
### 例 1：原地交换
```python
a, b = b, a
```

通常认为额外空间很少，接近 `O(1)`。

### 例 2：复制列表
```python
copy_nums = nums[:]
```

如果 `nums` 有 `n` 个元素，新列表也有 `n` 个元素，因此额外空间通常看作 `O(n)`。

## 4. 常见空间复杂度直觉
以后做题时，可以这样想：
- 有没有新建和原数组差不多大的容器？
- 有没有使用递归？
- 是否只是用了几个辅助变量？

## 5. 时间复杂度和空间复杂度的权衡
有些算法更快，但更占内存；  
有些算法更省内存，但运行更慢。

算法设计常常是在“时间”和“空间”之间找平衡。

## 6. 本节总结
这节的目标不是让你算得特别严谨，而是能形成判断：
- 新建大容器，空间通常会增大
- 只用少数变量，空间通常较小
- 复杂度分析不只有时间，也有空间

## 7. 原地算法
如果算法直接在原列表上修改，不额外创建同规模列表，通常叫原地算法。

```python
arr = [3, 1, 2]
arr[0], arr[1] = arr[1], arr[0]
```

这种操作只用了少量额外变量，空间复杂度通常看作 `O(1)`。

## 8. 递归调用栈
递归即使没有创建列表，也会占用调用栈空间。

```python
def f(n):
    if n == 0:
        return
    f(n - 1)
```

调用深度是 `n`，所以空间复杂度可能是 `O(n)`。

## 9. 小练习
判断下面哪段代码额外空间更大：
1. 只用变量 `total` 累加
2. 新建列表保存每个中间结果
"""
)
Quiz.objects.create(lesson=l5_1_2, question="空间复杂度主要关注什么？", option_a="代码有多少行", option_b="程序运行时额外占用多少内存", option_c="电脑内存总大小", option_d="文件体积", correct_answer="B", explanation="空间复杂度看的是运行时额外空间。")
Quiz.objects.create(lesson=l5_1_2, question="复制一个长度为 n 的列表，额外空间通常是？", option_a="O(1)", option_b="O(log n)", option_c="O(n)", option_d="O(n^2)", correct_answer="C", explanation="复制出一个同规模列表，额外空间通常是 O(n)。")
Quiz.objects.create(lesson=l5_1_2, question="只使用少量辅助变量的算法，空间复杂度通常更接近？", option_a="O(1)", option_b="O(n)", option_c="O(n^2)", option_d="O(2^n)", correct_answer="A", explanation="额外变量很少时通常是常数空间。")
Quiz.objects.create(lesson=l5_1_2, question="判断题：空间复杂度分析只在递归题里有意义。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，任何算法都可以分析空间复杂度。")
Quiz.objects.create(lesson=l5_1_2, question="判断题：算法越快，空间复杂度一定越小。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，时间和空间常常需要权衡。")
Quiz.objects.create(lesson=l5_1_2, question="下面哪种情况更可能增加空间复杂度？", option_a="只交换两个变量", option_b="创建一个和输入同样大的新列表", option_c="访问一次 arr[0]", option_d="打印一个数字", correct_answer="B", explanation="新建同规模容器通常意味着更高的额外空间。")

ch5_2, _ = Chapter.objects.get_or_create(course=c5, title="第2章：排序与查找", defaults={'order': 2})
l5_2_1 = create_lesson(
    chapter=ch5_2, title="2.1 冒泡排序 Bubble Sort", order=1, lesson_type='code',
    code_challenge_prompt="# 实现冒泡排序\narr = [3, 1, 4, 2]\n# 请补全代码",
    content="""# 2.1 冒泡排序 Bubble Sort

## 1. 原理
两两比较相邻元素，如果反序就交换。一轮下来，最大的元素会“冒泡”到最后。

## 2. 代码实现
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```

## 3. 复杂度
- 时间：O(n^2)
- 空间：O(1)

## 4. 一轮一轮发生了什么
冒泡排序最适合理解“局部比较，逐步逼近整体有序”。

第一轮：
- 最大值被推到最后

第二轮：
- 次大值被推到倒数第二位

所以每完成一轮，后面就多一个“已经排好”的位置。

## 5. 为什么它适合入门？
虽然效率不高，但它的逻辑非常直观：
- 比较相邻元素
- 发现顺序错了就交换
- 一轮结束后，最大值到末尾

## 6. 常见优化
如果某一轮下来**一次交换都没有发生**，说明数组已经有序，可以提前结束。

这也是为什么最好情况可以接近 `O(n)`。

## 7. 本节总结
冒泡排序最重要的学习价值不是“以后常用”，而是让你第一次真正理解：
- 排序是怎么通过重复比较逐步完成的
- 双重循环为什么常常对应 `O(n^2)`

## 8. 手动跟踪一轮
以 `[3, 1, 4, 2]` 为例：

```text
[3, 1, 4, 2]
比较 3 和 1，交换 -> [1, 3, 4, 2]
比较 3 和 4，不换 -> [1, 3, 4, 2]
比较 4 和 2，交换 -> [1, 3, 2, 4]
```

第一轮结束后，最大值 `4` 已经到最后。

## 9. 优化版本
```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr
```

`swapped` 用来记录这一轮有没有发生交换。如果完全没有交换，说明已经有序。

## 10. 易错点
- 内层循环上界是 `n - i - 1`，避免访问 `arr[j + 1]` 越界
- 交换要同时完成：`arr[j], arr[j + 1] = arr[j + 1], arr[j]`
- 冒泡排序默认是原地排序，会修改原列表

## 11. 小练习
给定 `[5, 1, 4, 2, 8]`，手写第一轮冒泡后的结果，再写代码验证。
"""
)
Quiz.objects.create(lesson=l5_2_1, question="冒泡排序的时间复杂度？", option_a="O(n)", option_b="O(n^2)", option_c="O(n log n)", option_d="O(1)", correct_answer="B", explanation="双重循环。")
Quiz.objects.create(lesson=l5_2_1, question="冒泡排序是稳定的吗？", option_a="是", option_b="否", option_c="不确定", option_d="看情况", correct_answer="A", explanation="相等元素不交换，相对位置不变，所以稳定。")
Quiz.objects.create(lesson=l5_2_1, question="第一轮冒泡后，哪个位置的元素确定了？", option_a="第一个", option_b="最后一个", option_c="中间", option_d="无", correct_answer="B", explanation="最大的元素冒泡到最后。")
Quiz.objects.create(lesson=l5_2_1, question="最好情况（已经有序）的复杂度？", option_a="O(n)", option_b="O(n^2)", option_c="O(1)", option_d="O(log n)", correct_answer="A", explanation="如果加了优化标志位，可以是 O(n)。")
Quiz.objects.create(lesson=l5_2_1, question="交换两个变量 a, b 的 Python 写法？", option_a="a, b = b, a", option_b="swap(a, b)", option_c="a = b", option_d="b = a", correct_answer="A", explanation="元组解包。")
Quiz.objects.create(lesson=l5_2_1, question="判断题：冒泡排序是效率最高的排序算法。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，通常较慢。")
Quiz.objects.create(lesson=l5_2_1, question="判断题：冒泡排序需要额外的 O(n) 空间。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，原地排序 O(1)。")
Quiz.objects.create(lesson=l5_2_1, question="冒泡排序的名字由来？", option_a="像气泡一样往上冒", option_b="像开水一样沸腾", option_c="像泡沫一样消失", option_d="无意义", correct_answer="A", explanation="大元素像气泡一样浮到顶端。")
Quiz.objects.create(lesson=l5_2_1, question="对 [5, 4, 3, 2, 1] 进行冒泡排序，第一轮交换几次？", option_a="1", option_b="2", option_c="3", option_d="4", correct_answer="D", explanation="4 次：5和4, 5和3, 5和2, 5和1。")
Quiz.objects.create(lesson=l5_2_1, question="Python 内置的 sort 算法是？", option_a="冒泡排序", option_b="快速排序", option_c="Timsort", option_d="插入排序", correct_answer="C", explanation="Timsort (归并+插入)。")

l5_2_2 = create_lesson(
    chapter=ch5_2, title="2.2 二分查找 Binary Search", order=2, lesson_type='code',
    code_challenge_prompt="# 在有序数组中查找 5\narr = [1, 3, 5, 7, 9]\n# 请实现二分查找",
    content="""# 2.2 二分查找 Binary Search

## 1. 原理
在**有序数组**中，每次取中间元素比较。如果中间值比目标大，则找左半边；否则找右半边。

## 2. 条件
必须是**有序**的！

## 3. 代码
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

## 4. 为什么必须有序
二分查找之所以快，是因为每次比较后都能放心地丢掉一半数据。

但如果数组无序：
- 你看到中间值比目标大
- 并不能说明目标一定在左边

所以“有序”不是可有可无，而是二分查找成立的前提。

## 5. 指针移动的本质
- `arr[mid] < target`：说明目标只可能在右半边，移动 `left`
- `arr[mid] > target`：说明目标只可能在左半边，移动 `right`

这其实就是“不断缩小搜索区间”。

## 6. 本节总结
二分查找真正要掌握的是：
- 只能在有序数据上用
- 每次排除一半范围
- 速度快的原因来自“减半”

## 7. 手动跟踪
在 `[1, 3, 5, 7, 9]` 中查找 `7`：

```text
left=0, right=4, mid=2, arr[mid]=5
5 < 7，所以去右边，left=3

left=3, right=4, mid=3, arr[mid]=7
找到，返回 3
```

## 8. 循环条件为什么是 left <= right
当 `left == right` 时，搜索区间里还有一个元素，仍然需要检查。

如果写成：

```python
while left < right:
```

可能漏掉最后一个元素。

## 9. 找不到时发生什么
当目标不存在，左右指针最终会交错：

```text
left > right
```

这说明搜索区间已经空了，因此返回 `-1`。

## 10. 易错点
- 忘记数组必须有序
- `mid` 要用整除 `//`
- 更新边界时要写 `mid + 1` 或 `mid - 1`
- 如果只写 `left = mid`，可能陷入死循环

## 11. 小练习
改造二分查找：如果找到了目标，返回下标；如果没找到，返回 `"not found"`。
"""
)
Quiz.objects.create(lesson=l5_2_2, question="二分查找的前提条件？", option_a="数组无序", option_b="数组有序", option_c="数组必须全正数", option_d="数组长度为偶数", correct_answer="B", explanation="必须有序。")
Quiz.objects.create(lesson=l5_2_2, question="二分查找的时间复杂度？", option_a="O(n)", option_b="O(n^2)", option_c="O(log n)", option_d="O(1)", correct_answer="C", explanation="每次减半，对数级。")
Quiz.objects.create(lesson=l5_2_2, question="在 100 个有序数字中找，最多找几次？", option_a="100", option_b="50", option_c="7", option_d="10", correct_answer="C", explanation="log2(100) 约等于 6.6，向上取整 7。")
Quiz.objects.create(lesson=l5_2_2, question="mid 的计算公式？", option_a="(left+right)/2", option_b="(left+right)//2", option_c="left+right", option_d="right-left", correct_answer="B", explanation="整除。")
Quiz.objects.create(lesson=l5_2_2, question="如果 arr[mid] < target，说明？", option_a="在左边", option_b="在右边", option_c="找到了", option_d="不存在", correct_answer="B", explanation="目标比中间大，在右边。")
Quiz.objects.create(lesson=l5_2_2, question="判断题：二分查找可以用于链表。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，链表不支持随机访问，效率低。")
Quiz.objects.create(lesson=l5_2_2, question="判断题：线性查找比二分查找慢。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确（在数据量大时）。")
Quiz.objects.create(lesson=l5_2_2, question="二分查找能用于链表吗？", option_a="能，效率很高", option_b="能，但效率不如数组", option_c="不能", option_d="会报错", correct_answer="B", explanation="链表不支持随机访问，定位中间节点需要 O(n)，导致整体效率下降。")
Quiz.objects.create(lesson=l5_2_2, question="target 不在数组中时，二分查找通常返回？", option_a="0", option_b="-1", option_c="None", option_d="False", correct_answer="B", explanation="约定俗成返回 -1。")
Quiz.objects.create(lesson=l5_2_2, question="二分查找属于哪种算法策略？", option_a="贪心", option_b="分治", option_c="动态规划", option_d="回溯", correct_answer="B", explanation="分而治之。")

l5_2_3 = create_lesson(
    chapter=ch5_2, title="2.3 选择排序 Selection Sort", order=3, lesson_type='code',
    code_challenge_prompt="# 实现选择排序\narr = [64, 25, 12, 22, 11]\n# 请补全代码",
    content="""# 2.3 选择排序 Selection Sort

## 1. 原理
每一轮从“未排序部分”中找出最小值，放到当前应在的位置。

## 2. 代码实现
```python
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
```

## 3. 复杂度
- 时间：O(n^2)
- 空间：O(1)

## 4. 和冒泡排序有什么区别
两者复杂度都常是 `O(n^2)`，但思路不同：
- 冒泡排序：不断比较相邻元素，把大元素往后推
- 选择排序：每轮直接找最小值，放到前面

## 5. 本节总结
选择排序的关键在于：
- 当前轮要确定“当前位置应该放谁”
- 找最小值是核心动作

## 6. 手动跟踪
以 `[64, 25, 12, 22, 11]` 为例：

第一轮在整个数组中找最小值 `11`，放到第 0 位：

```text
[11, 25, 12, 22, 64]
```

第二轮只在剩余部分 `[25, 12, 22, 64]` 中找最小值 `12`，放到第 1 位：

```text
[11, 12, 25, 22, 64]
```

每轮结束，前面就多一个确定位置。

## 7. 为什么交换次数少
选择排序每一轮最多交换一次。冒泡排序可能一轮交换很多次。

所以虽然二者时间复杂度常同为 `O(n^2)`，但在交换成本很高的场景，选择排序的思路仍有学习价值。

## 8. 稳定性提示
普通选择排序通常不是稳定排序。因为一次交换可能改变相等元素的相对顺序。

初学阶段先记住：
- 冒泡排序稳定
- 插入排序稳定
- 选择排序通常不稳定

## 9. 易错点
- `min_index` 每轮开始要设为 `i`
- 内层循环从 `i + 1` 开始
- 交换要在内层循环结束后做，不是每发现更小就立即交换

## 10. 小练习
给定 `[3, 1, 2]`，写出每一轮选择排序后的数组。
"""
)
Quiz.objects.create(lesson=l5_2_3, question="选择排序每一轮主要做什么？", option_a="把最大值冒到最后", option_b="从未排序部分选出最小值", option_c="随机交换", option_d="二分查找", correct_answer="B", explanation="选择排序每轮找出最小值放到当前位。")
Quiz.objects.create(lesson=l5_2_3, question="选择排序的时间复杂度通常是？", option_a="O(1)", option_b="O(log n)", option_c="O(n)", option_d="O(n^2)", correct_answer="D", explanation="两层循环，通常是 O(n^2)。")
Quiz.objects.create(lesson=l5_2_3, question="选择排序和冒泡排序的共同点之一是？", option_a="都基于分治", option_b="都常见于 O(n^2)", option_c="都要求有序数组", option_d="都使用递归", correct_answer="B", explanation="二者都是经典 O(n^2) 排序算法。")
Quiz.objects.create(lesson=l5_2_3, question="判断题：选择排序每一轮结束后，前面会多一个已经确定的位置。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，每轮会确定当前最小元素的位置。")
Quiz.objects.create(lesson=l5_2_3, question="判断题：选择排序依赖相邻交换不断冒泡。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，这是冒泡排序的特点。")
Quiz.objects.create(lesson=l5_2_3, question="如果第 i 轮找到了更小元素，通常会做什么？", option_a="删除元素", option_b="交换到第 i 位", option_c="直接返回", option_d="反转数组", correct_answer="B", explanation="会把最小值交换到当前位置。")

l5_2_4 = create_lesson(
    chapter=ch5_2, title="2.4 插入排序 Insertion Sort", order=4, lesson_type='code',
    code_challenge_prompt="# 实现插入排序\narr = [5, 2, 4, 6, 1, 3]\n# 请补全代码",
    content="""# 2.4 插入排序 Insertion Sort

## 1. 原理
把数组想成“左边已经排好，右边还没排好”。  
每次从右边拿一个元素，插入到左边合适的位置。

## 2. 代码实现
```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
```

## 3. 复杂度
- 最坏情况：O(n^2)
- 最好情况：接近 O(n)
- 空间：O(1)

## 4. 为什么叫“插入”
因为每次都是把当前元素插入到前面已经有序的那一段里。

## 5. 和前两种排序的区别
- 冒泡：通过交换把大元素往后推
- 选择：每轮找最小值放前面
- 插入：维护前缀有序，把新元素插入进去

## 6. 本节总结
插入排序适合理解“局部有序逐步扩张”的思路。  
在数据本来就接近有序时，它往往比冒泡、选择更自然。

## 7. 手动跟踪
以 `[5, 2, 4, 6]` 为例：

先认为第一个元素 `[5]` 已经有序。

处理 `2`：

```text
[5, 2, 4, 6] -> [2, 5, 4, 6]
```

处理 `4`：

```text
[2, 5, 4, 6] -> [2, 4, 5, 6]
```

处理 `6`：

```text
[2, 4, 5, 6]
```

## 8. 为什么接近有序时表现好
如果数组本来就接近有序，`while arr[j] > key` 很快就会停止，需要移动的元素少。

例如 `[1, 2, 3, 5, 4]` 只需要把 `4` 插入到正确位置。

## 9. 稳定性
插入排序通常是稳定的。只要判断条件使用 `arr[j] > key`，相等元素不会越过彼此。

## 10. 易错点
- `key` 要先保存当前元素，否则移动元素时会丢失
- `while` 中要同时判断 `j >= 0`
- 最后插入位置是 `j + 1`

## 11. 小练习
给定 `[4, 3, 2, 1]`，手动写出插入排序每轮结果。
"""
)
Quiz.objects.create(lesson=l5_2_4, question="插入排序的核心思路是？", option_a="每轮找最小值", option_b="把当前元素插入到前面有序部分", option_c="每次减半", option_d="随机交换", correct_answer="B", explanation="插入排序维护前缀有序。")
Quiz.objects.create(lesson=l5_2_4, question="插入排序中 key 通常表示什么？", option_a="当前准备插入的元素", option_b="数组长度", option_c="最小值", option_d="目标下标", correct_answer="A", explanation="key 常用来保存当前待插入元素。")
Quiz.objects.create(lesson=l5_2_4, question="插入排序最好情况常接近？", option_a="O(1)", option_b="O(log n)", option_c="O(n)", option_d="O(n^2)", correct_answer="C", explanation="数组接近有序时插入排序最好情况可接近 O(n)。")
Quiz.objects.create(lesson=l5_2_4, question="判断题：插入排序每次都从未排序部分拿一个元素处理。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l5_2_4, question="判断题：插入排序必须额外开一个和原数组一样大的新数组。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，插入排序通常是原地排序。")
Quiz.objects.create(lesson=l5_2_4, question="下列哪个最能描述插入排序？", option_a="不断减半", option_b="相邻冒泡", option_c="维护前面有序，再插入新元素", option_d="先建树再遍历", correct_answer="C", explanation="这正是插入排序的核心过程。")


# ==========================================
# Course 6: GESP 6级 - 进阶数据结构与递归
# ==========================================
print("正在创建 GESP 6级 课程...")
c6, _ = Course.objects.get_or_create(
    title="GESP 6级：进阶数据结构与递归",
    description="挑战高阶编程概念。深入理解递归思想，掌握栈（Stack）和队列（Queue）的原理与实现，解决复杂逻辑问题。",
    defaults={'order': 6}
)
c6.order = 7
c6.save(update_fields=['order'])

ch6_1, _ = Chapter.objects.get_or_create(course=c6, title="第1章：递归", defaults={'order': 1})
l6_1_1 = create_lesson(
    chapter=ch6_1, title="1.1 递归基础 Recursion", order=1, lesson_type='code',
    code_challenge_prompt="# 递归计算阶乘 5!\ndef factorial(n):\n    if n == 1: return 1\n    return n * factorial(n-1)\nprint(factorial(5))",
    content="""# 1.1 递归基础

## 1. 什么是递归？
函数**自己调用自己**。
必须有两个部分：
1.  **基准情况 (Base Case)**：停止递归的条件。
2.  **递归步骤 (Recursive Step)**：调用自身，向基准靠近。

## 2. 经典案例：阶乘
n! = n * (n-1)!
```python
def fact(n):
    if n == 1: return 1  # 基准
    return n * fact(n-1) # 递归
```

## 3. 调用过程展开
计算 `fact(4)` 时：

```text
fact(4)
= 4 * fact(3)
= 4 * 3 * fact(2)
= 4 * 3 * 2 * fact(1)
= 4 * 3 * 2 * 1
= 24
```

递归不是魔法，本质是函数一层一层调用，直到遇到基准情况，再一层一层返回结果。

## 4. 递归必须向基准靠近
下面代码有问题：

```python
def count_down(n):
    print(n)
    count_down(n)
```

它永远没有变小，也没有停止条件，会导致 `RecursionError`。

正确写法：

```python
def count_down(n):
    if n == 0:
        return
    print(n)
    count_down(n - 1)
```

## 5. 递归和栈
每一次函数调用都会压入调用栈。

```text
fact(4)
  fact(3)
    fact(2)
      fact(1)
```

所以递归代码虽然短，但会占用额外栈空间。递归太深时，Python 会报递归深度错误。

## 6. 什么时候适合递归？
适合递归的问题通常有“自己包含自己”的结构：
- 阶乘
- 斐波那契
- 汉诺塔
- 树形结构遍历
- 嵌套列表展开

不适合递归的情况：
- 只是普通重复次数，用循环更清楚
- 数据量极大，递归层数可能太深

## 7. 递归 vs 循环
```python
def sum_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_rec(n):
    if n == 1:
        return 1
    return n + sum_rec(n - 1)
```

两者都能求和。循环更节省栈空间；递归更贴近某些问题的数学定义。

## 8. 易错点
- 忘记基准情况
- 递归参数没有变化
- 基准情况写错，例如 `n == 0` 和 `n == 1` 混淆
- 以为递归一定比循环快

## 9. 小练习
写递归函数 `sum_to(n)`，返回 `1 + 2 + ... + n`。

提示：
- `sum_to(1)` 返回 1
- `sum_to(n)` 返回 `n + sum_to(n - 1)`
"""
)
Quiz.objects.create(lesson=l6_1_1, question="递归函数必须包含？", option_a="循环", option_b="基准情况", option_c="全局变量", option_d="数组", correct_answer="B", explanation="否则会死循环（栈溢出）。")
Quiz.objects.create(lesson=l6_1_1, question="如果没有基准情况会怎样？", option_a="正常运行", option_b="返回 0", option_c="栈溢出 (RecursionError)", option_d="死机", correct_answer="C", explanation="无限递归导致栈溢出。")
Quiz.objects.create(lesson=l6_1_1, question="递归计算 3! 的调用顺序？", option_a="f(3)->f(2)->f(1)", option_b="f(1)->f(2)->f(3)", option_c="f(3)->f(3)", option_d="f(3)->f(1)", correct_answer="A", explanation="层层向下调用。")
Quiz.objects.create(lesson=l6_1_1, question="斐波那契数列适合用递归吗？", option_a="适合且高效", option_b="适合但低效", option_c="完全不适合", option_d="不能用", correct_answer="B", explanation="简单递归会有大量重复计算。")
Quiz.objects.create(lesson=l6_1_1, question="Python 默认递归深度限制？", option_a="100", option_b="1000", option_c="无限", option_d="10", correct_answer="B", explanation="通常是 1000。")
Quiz.objects.create(lesson=l6_1_1, question="判断题：所有递归都可以转化为循环。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确（理论上）。")
Quiz.objects.create(lesson=l6_1_1, question="判断题：递归通常比循环更节省内存。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，递归需要栈空间。")
Quiz.objects.create(lesson=l6_1_1, question="递归函数的两个要素是？", option_a="循环和判断", option_b="基准情况和递归步骤", option_c="输入和输出", option_d="加和减", correct_answer="B", explanation="Base case and Recursive step.")
Quiz.objects.create(lesson=l6_1_1, question="尾递归是指？", option_a="递归调用在函数最开始", option_b="递归调用在函数最后一步", option_c="递归调用在中间", option_d="没有递归", correct_answer="B", explanation="Last step recursion.")
Quiz.objects.create(lesson=l6_1_1, question="汉诺塔问题最适合用什么解法？", option_a="循环", option_b="递归", option_c="穷举", option_d="贪心", correct_answer="B", explanation="经典的递归问题。")

ch6_2, _ = Chapter.objects.get_or_create(course=c6, title="第2章：栈与队列", defaults={'order': 2})
l6_2_1 = create_lesson(
    chapter=ch6_2, title="2.1 栈 Stack", order=1, lesson_type='code',
    code_challenge_prompt="# 用列表模拟栈\nstack = []\nstack.append(1)\nstack.append(2)\nprint(stack.pop())",
    content="""# 2.1 栈 Stack

## 1. 概念
**后进先出 (LIFO - Last In First Out)**。
就像洗盘子，最后放上去的盘子最先被拿走。

## 2. Python 实现
使用 `list` 即可。
- 进栈 (Push): `append()`
- 出栈 (Pop): `pop()`

```python
stack = []
stack.append("A")
stack.append("B")
print(stack.pop()) # "B"
```

## 3. 栈顶是什么？
栈顶就是最后进入、最先出去的位置。

```python
stack = []
stack.append("A")
stack.append("B")
stack.append("C")

print(stack[-1])   # 查看栈顶 C
print(stack.pop()) # 弹出 C
```

## 4. 空栈不能 pop
```python
stack = []
stack.pop()  # IndexError
```

更稳妥：

```python
if stack:
    item = stack.pop()
else:
    print("栈为空")
```

## 5. 栈的常见应用
- 浏览器后退
- 撤销操作
- 函数调用栈
- 括号匹配
- 深度优先搜索 DFS

## 6. 括号匹配示例
```python
def is_valid(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack or stack.pop() != pairs[ch]:
                return False

    return len(stack) == 0
```

思路：
1. 左括号入栈
2. 右括号出现时，弹出栈顶检查是否匹配
3. 最后栈为空才说明全部匹配

## 7. 栈和递归的关系
递归调用本质上依赖调用栈。每深入一层递归，就像把一个任务压入栈；每返回一次，就像弹出栈顶任务。

## 8. 易错点
- `pop()` 会删除并返回元素
- 空栈 `pop()` 会报错
- 栈只关心栈顶，不关心中间元素
- 用列表模拟栈时，推荐在末尾 `append/pop`

## 9. 小练习
用栈反转字符串：

```python
text = "python"
stack = []

for ch in text:
    stack.append(ch)

result = ""
while stack:
    result += stack.pop()

print(result)
```
"""
)
Quiz.objects.create(lesson=l6_2_1, question="栈的特点是？", option_a="先进先出", option_b="后进先出", option_c="随机进出", option_d="先进后出", correct_answer="B", explanation="LIFO。")
Quiz.objects.create(lesson=l6_2_1, question="进栈操作对应 Python 列表的？", option_a="insert", option_b="push", option_c="append", option_d="add", correct_answer="C", explanation="append。")
Quiz.objects.create(lesson=l6_2_1, question="出栈操作对应 Python 列表的？", option_a="delete", option_b="remove", option_c="pop", option_d="get", correct_answer="C", explanation="pop。")
Quiz.objects.create(lesson=l6_2_1, question="Stack: 进 1, 进 2, 出, 进 3, 出。剩下？", option_a="[1]", option_b="[2]", option_c="[3]", option_d="[]", correct_answer="A", explanation="进1,2->[1,2]; 出2->[1]; 进3->[1,3]; 出3->[1]。")
Quiz.objects.create(lesson=l6_2_1, question="函数调用栈使用的是哪种数据结构？", option_a="队列", option_b="栈", option_c="树", option_d="图", correct_answer="B", explanation="栈。")
Quiz.objects.create(lesson=l6_2_1, question="判断题：栈可以访问中间的元素。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，只能访问栈顶。")
Quiz.objects.create(lesson=l6_2_1, question="判断题：栈是线性结构。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l6_2_1, question="栈溢出 (Stack Overflow) 通常是因为？", option_a="栈空了还 pop", option_b="递归深度过深或无限递归", option_c="栈满了还 push", option_d="B和C", correct_answer="D", explanation="空间耗尽。")
Quiz.objects.create(lesson=l6_2_1, question="浏览器的“后退”功能通常使用什么实现？", option_a="队列", option_b="栈", option_c="堆", option_d="树", correct_answer="B", explanation="后访问的页面先退回。")
Quiz.objects.create(lesson=l6_2_1, question="检查括号匹配 ([]) 使用什么数据结构？", option_a="栈", option_b="队列", option_c="链表", option_d="哈希表", correct_answer="A", explanation="左括号入栈，右括号出栈匹配。")

l6_2_2 = create_lesson(
    chapter=ch6_2, title="2.2 队列 Queue", order=2, lesson_type='code',
    code_challenge_prompt="# 用 deque 模拟队列\nfrom collections import deque\nq = deque()\nq.append(1)\nq.append(2)\nprint(q.popleft())",
    content="""# 2.2 队列 Queue

## 1. 概念
**先进先出 (FIFO - First In First Out)**。
就像排队买票，先来的先服务。

## 2. Python 实现
列表的 `pop(0)` 很慢（O(n)），建议用 `collections.deque`。

```python
from collections import deque
q = deque()
q.append("A") # 入队
q.append("B")
print(q.popleft()) # "A" - 出队
```

## 3. 为什么不用 list.pop(0)
列表头部删除需要移动后面所有元素：

```python
lst = [1, 2, 3, 4]
lst.pop(0)
```

当列表很长时，这会比较慢。`deque.popleft()` 更适合队列。

## 4. 入队和出队
```python
from collections import deque

q = deque()
q.append("task1")
q.append("task2")
q.append("task3")

print(q.popleft())  # task1
print(q.popleft())  # task2
```

先进入的 `task1` 先出去，这就是 FIFO。

## 5. 队列常见应用
- 排队叫号
- 打印任务
- 消息处理
- 广度优先搜索 BFS
- 游戏事件队列

## 6. BFS 直觉
队列适合一层一层处理问题。

```python
from collections import deque

q = deque(["A"])
visited = set()

while q:
    node = q.popleft()
    if node in visited:
        continue
    visited.add(node)
    print(node)
```

先进入队列的节点会先被处理，因此 BFS 可以按距离从近到远探索。

## 7. deque 是双端队列
`deque` 不只可以当普通队列，也支持两端操作：

```python
q.append("right")
q.appendleft("left")
q.pop()
q.popleft()
```

普通队列只强调一端进、一端出；双端队列更灵活。

## 8. 易错点
- 队列是 FIFO，栈是 LIFO
- `popleft()` 来自 `deque`，普通 list 没有这个方法
- `list.pop(0)` 能用但不适合大量数据
- 空队列 `popleft()` 会报错

## 9. 小练习
模拟排队叫号：

```python
from collections import deque

line = deque(["Alice", "Bob", "Cindy"])
while line:
    person = line.popleft()
    print("请", person, "办理业务")
```
"""
)
Quiz.objects.create(lesson=l6_2_2, question="队列的特点是？", option_a="先进先出", option_b="后进先出", option_c="随机访问", option_d="无序", correct_answer="A", explanation="FIFO。")
Quiz.objects.create(lesson=l6_2_2, question="Python 中推荐用什么实现队列？", option_a="list", option_b="dict", option_c="deque", option_d="set", correct_answer="C", explanation="collections.deque。")
Quiz.objects.create(lesson=l6_2_2, question="deque 出队的方法是？", option_a="pop()", option_b="popleft()", option_c="remove()", option_d="delete()", correct_answer="B", explanation="popleft()。")
Quiz.objects.create(lesson=l6_2_2, question="Queue: 进 1, 进 2, 出, 进 3, 出。剩下？", option_a="[3]", option_b="[1]", option_c="[2]", option_d="[]", correct_answer="A", explanation="进1,2->[1,2]; 出1->[2]; 进3->[2,3]; 出2->[3]。")
Quiz.objects.create(lesson=l6_2_2, question="BFS（广度优先搜索）使用什么数据结构？", option_a="栈", option_b="队列", option_c="堆", option_d="树", correct_answer="B", explanation="队列。")
Quiz.objects.create(lesson=l6_2_2, question="判断题：列表的 pop(0) 操作是 O(1) 的。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，是 O(n)，因为要移动后续元素。")
Quiz.objects.create(lesson=l6_2_2, question="判断题：队列允许在两端插入和删除。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，那是双端队列（Deque），普通队列只能一端进一端出。")
Quiz.objects.create(lesson=l6_2_2, question="打印机的任务队列是？", option_a="LIFO", option_b="FIFO", option_c="随机", option_d="优先权", correct_answer="B", explanation="先提交的任务先打印。")
Quiz.objects.create(lesson=l6_2_2, question="双端队列 (Deque) 允许？", option_a="只能两端进", option_b="只能两端出", option_c="两端都可以进出", option_d="只能一端进一端出", correct_answer="C", explanation="Double-ended queue。")
Quiz.objects.create(lesson=l6_2_2, question="Python 的 collections.deque 是基于什么实现的？", option_a="数组", option_b="双向链表", option_c="单向链表", option_d="栈", correct_answer="B", explanation="双向链表，头尾操作 O(1)。")


# ==========================================
# Course 7: Head First Python (Structured)
# ==========================================
print("正在创建 Head First Python 课程 (Structured)...")
c7, _ = Course.objects.get_or_create(
    title="Head First Python",
    description="《Head First Python》经典教材改编。通过生动有趣的项目驱动学习，涵盖列表、模块、文件处理、异常处理等实用技能。",
    defaults={'order': 7}
)
c7.order = 8
c7.save(update_fields=['order'])

# Chapter 1: The Basics
ch7_1, _ = Chapter.objects.get_or_create(course=c7, title="第1章：基础知识 (The Basics)", defaults={'order': 1})

# 1.1 Getting Started
l7_1_1 = create_lesson(
    chapter=ch7_1, title="1.1 快速入门与 IDLE", order=1, lesson_type='text',
    code_challenge_prompt="print('Hello Head First Python')",
    content="""# 1.1 快速入门与 IDLE

## 1. 打破传统
大多数书籍从 "Hello World" 开始，但 Head First 系列不同。我们直接从一个更有趣的例子开始。

## 2. IDLE 开发环境
Python 自带了一个轻量级的 IDE 叫 IDLE。它有两个窗口：
- **Python Shell**: 用于运行单行代码片段 (REPL)。
- **Edit Window**: 用于编写完整的程序文件。

## 3. 你的第一个挑战
在 IDLE 中输入代码并运行。确保你安装了 Python 3。

## 4. Shell 和文件运行的区别
Shell 适合快速试验：

```python
>>> 2 + 3
5
```

但完整程序应该写进 `.py` 文件：

```python
print("Hello Head First Python")
```

Shell 像草稿纸，文件像正式作业。

## 5. 出错不可怕
初学时最常见的是语法错误：

```python
print("Hello"
```

这会报 `SyntaxError`，意思是 Python 看不懂这行代码结构。

读错误信息时先看：
- 错误类型
- 出错行号
- 箭头指向哪里

## 6. 内置函数 BIF
BIF 是 Built-in Function，表示 Python 自带函数。例如：

```python
print("Hello")
len("Python")
type(123)
```

这些函数不需要导入模块，可以直接使用。

## 7. 小练习
在 Shell 中分别运行：
1. `print("Python")`
2. `len("Python")`
3. `type(3.14)`

观察每条输出。

## 8. 从 Shell 走向脚本
Shell 适合立即看到结果，但脚本文件更适合保存和复用。

建议学习节奏：
1. 在 Shell 里试一行
2. 确认能运行
3. 放进 `.py` 文件
4. 保存并运行完整程序

## 9. 学习习惯
每次写完代码后问自己：
- 这行代码输入是什么？
- 输出是什么？
- 如果写错一个符号，会报什么错？
"""
)
Quiz.objects.create(lesson=l7_1_1, question="IDLE 的 Python Shell 主要用于？", option_a="编写大型项目", option_b="测试代码片段 (REPL)", option_c="浏览网页", option_d="画图", correct_answer="B", explanation="Shell 是 Read-Eval-Print-Loop 环境。")
Quiz.objects.create(lesson=l7_1_1, question="在 IDLE 中，>>> 提示符表示什么？", option_a="等待输入命令", option_b="程序正在运行", option_c="出现错误", option_d="注释", correct_answer="A", explanation="这是 Shell 等待用户输入的标志。")
Quiz.objects.create(lesson=l7_1_1, question="Head First 系列提倡的学习方式是？", option_a="死记硬背", option_b="大量阅读文字", option_c="图像化与实践驱动", option_d="只看视频", correct_answer="C", explanation="强调大脑友好的学习方式。")
Quiz.objects.create(lesson=l7_1_1, question="Python 源代码文件的扩展名通常是？", option_a=".python", option_b=".exe", option_c=".py", option_d=".txt", correct_answer="C", explanation="标准后缀是 .py。")
Quiz.objects.create(lesson=l7_1_1, question="如果 print('Hello') 漏掉了右括号，Python 会？", option_a="自动补全", option_b="报错 SyntaxError", option_c="忽略错误", option_d="打印 Hello", correct_answer="B", explanation="语法错误会导致程序无法运行。")
Quiz.objects.create(lesson=l7_1_1, question="判断题：IDLE 是 Python 官方自带的编辑器。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，随 Python 安装包一起提供。")
Quiz.objects.create(lesson=l7_1_1, question="判断题：print 是 Python 2 和 Python 3 中的关键字，用法完全一样。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，Python 3 中 print 是函数，必须加括号。")
Quiz.objects.create(lesson=l7_1_1, question="Python 中单行注释使用什么符号？", option_a="//", option_b="#", option_c="/*", option_d="--", correct_answer="B", explanation="# 用于单行注释。")
Quiz.objects.create(lesson=l7_1_1, question="IDLE 的全称是什么？", option_a="Integrated Development and Learning Environment", option_b="Ideal Development Logic Engine", option_c="International Developers Local Environment", option_d="Internal Debugging Loop Executor", correct_answer="A", explanation="集成开发与学习环境。")
Quiz.objects.create(lesson=l7_1_1, question="BIF 是什么意思？", option_a="Binary Input File", option_b="Built-in Function", option_c="Basic Interface Format", option_d="Big Integer Format", correct_answer="B", explanation="Built-in Function (内置函数)。")

# 1.2 A Meatier Example (odd.py)
l7_1_2 = create_lesson(
    chapter=ch7_1, title="1.2 实战：奇数分钟检测 (odd.py)", order=2, lesson_type='code',
    code_challenge_prompt="""# 编写一个程序，检测当前分钟数。
# 如果是奇数，打印 "This minute is a little odd"
# 如果是偶数，打印 "Not an odd minute"
from datetime import datetime
import time
import random

odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
right_this_minute = datetime.today().minute

if right_this_minute in odds:
    print("This minute is a little odd")
else:
    print("Not an odd minute")
""",
    content="""# 1.2 实战：奇数分钟检测

## 1. 任务描述
我们需要编写一个程序 `odd.py`，它能根据当前时间的分钟数，打印不同的消息。

## 2. 关键模块
- `datetime`: 获取系统时间。
- `time`: 控制程序暂停 (`sleep`)。
- `random`: 生成随机数。

## 3. 代码解析
```python
from datetime import datetime
right_this_minute = datetime.today().minute

if right_this_minute % 2 != 0:
    print("This minute is a little odd")
```

## 4. 判断奇偶的两种方式
书中常用列表保存奇数分钟：

```python
odds = [1, 3, 5, 7, 9]
if right_this_minute in odds:
    print("odd")
```

也可以用取模：

```python
if right_this_minute % 2 != 0:
    print("odd")
```

取模 `%` 表示求余数。一个数除以 2 余数不为 0，就是奇数。

## 5. import 的意义
```python
from datetime import datetime
```

意思是从 `datetime` 模块中导入 `datetime` 类。导入后才能调用：

```python
datetime.today()
```

## 6. 随机暂停
如果配合 `time.sleep()` 和 `random.randint()`，程序可以隔一段随机时间检查一次分钟数。

```python
import time
import random

time.sleep(random.randint(1, 5))
```

## 7. 易错点
- `=` 是赋值，`==` 是比较
- `if` 后面要写冒号
- `if` 代码块必须缩进
- `datetime` 是标准库，不需要额外安装

## 8. 小练习
改写程序：如果当前分钟是偶数，输出 `"Even minute"`；如果是奇数，输出 `"Odd minute"`。
"""
)
Quiz.objects.create(lesson=l7_1_2, question="如何获取当前时间的分钟数？", option_a="datetime.minute()", option_b="datetime.today().minute", option_c="time.minute", option_d="clock.minute", correct_answer="B", explanation="使用 datetime.today() 获取当前时间对象。")
Quiz.objects.create(lesson=l7_1_2, question="time.sleep(5) 的作用是？", option_a="让程序加速运行", option_b="让程序暂停 5 秒", option_c="让程序暂停 5 分钟", option_d="关闭程序", correct_answer="B", explanation="暂停执行指定的秒数。")
Quiz.objects.create(lesson=l7_1_2, question="random.randint(1, 60) 可能生成的数包括？", option_a="1", option_b="60", option_c="1 和 60 都包括", option_d="都不包括", correct_answer="C", explanation="randint 是闭区间，包含两端的值。")
Quiz.objects.create(lesson=l7_1_2, question="range(5) 生成的序列是？", option_a="1, 2, 3, 4, 5", option_b="0, 1, 2, 3, 4", option_c="0, 1, 2, 3, 4, 5", option_d="1, 2, 3, 4", correct_answer="B", explanation="从 0 开始，包头不包尾。")
Quiz.objects.create(lesson=l7_1_2, question="在 if 语句中，判断相等应该使用？", option_a="=", option_b="==", option_c="is", option_d="equals", correct_answer="B", explanation="== 是比较运算符，= 是赋值。")
Quiz.objects.create(lesson=l7_1_2, question="判断题：datetime 模块需要 pip install 才能使用。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，它是 Python 标准库的一部分。")
Quiz.objects.create(lesson=l7_1_2, question="判断题：if 语句后面的代码块必须缩进。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，Python 依靠缩进来组织代码块。")
Quiz.objects.create(lesson=l7_1_2, question="datetime.today() 返回的是什么类型？", option_a="str", option_b="int", option_c="datetime 对象", option_d="float", correct_answer="C", explanation="返回一个包含日期和时间的 datetime 对象。")
Quiz.objects.create(lesson=l7_1_2, question="time.sleep() 的参数单位是？", option_a="毫秒", option_b="秒", option_c="分钟", option_d="小时", correct_answer="B", explanation="参数是秒 (seconds)。")
Quiz.objects.create(lesson=l7_1_2, question="range(1, 10, 2) 生成的最后一个数是？", option_a="10", option_b="9", option_c="8", option_d="11", correct_answer="B", explanation="生成 1, 3, 5, 7, 9。")

# Chapter 2: List Data
ch7_2, _ = Chapter.objects.get_or_create(course=c7, title="第2章：列表数据 (List Data)", defaults={'order': 2})

# 2.1 Creating Lists
l7_2_1 = create_lesson(
    chapter=ch7_2, title="2.1 列表初探：电影列表", order=1, lesson_type='code',
    code_challenge_prompt="""# 创建一个列表 movies，包含以下电影：
# "The Holy Grail", "The Life of Brian", "The Meaning of Life"
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
print(movies[1])
""",
    content="""# 2.1 列表初探

## 1. 一切皆对象
在 Python 中，变量不需要声明类型。你可以把任何东西赋值给变量。

## 2. 列表 (List)
列表是一个有序的、可变的集合。就像一个数组，但更灵活。

```python
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
```

## 3. 访问列表
使用索引（从 0 开始）来访问列表中的元素。
`movies[1]` 会返回 "The Life of Brian"。

## 4. 修改列表元素
列表是可变的，可以直接修改某个位置：

```python
movies[0] = "New Movie"
```

字符串不可变，列表可变，这是 Python 中很重要的区别。

## 5. 负数索引
```python
movies[-1]
```

表示最后一个元素。负数索引从右往左数：
- `-1`：最后一个
- `-2`：倒数第二个

## 6. 混合类型列表
```python
movie = ["The Holy Grail", 1975, "Comedy"]
```

Python 列表可以放不同类型的数据。但如果数据有明确字段，后面会学习用字典表达得更清楚。

## 7. 易错点
- 索引从 0 开始
- `len(movies)` 返回元素个数，不是最后一个索引
- 最后一个索引是 `len(movies) - 1`
- 访问不存在的索引会 `IndexError`

## 8. 小练习
创建一个电影列表，完成：
1. 打印第一部电影
2. 打印最后一部电影
3. 修改第二部电影名
4. 输出列表长度

## 9. 列表和字符串的相似点
列表和字符串都支持索引：

```python
name = "Python"
movies = ["A", "B", "C"]

print(name[0])
print(movies[0])
```

不同点是：字符串不可变，列表可变。

## 10. 小项目思维
电影列表可以继续扩展：
- 添加上映年份
- 添加导演
- 按顺序打印
- 搜索某部电影是否存在
"""
)
Quiz.objects.create(lesson=l7_2_1, question="列表的索引是从几开始的？", option_a="1", option_b="0", option_c="-1", option_d="任意", correct_answer="B", explanation="Python 索引从 0 开始。")
Quiz.objects.create(lesson=l7_2_1, question="定义一个列表使用什么符号？", option_a="()", option_b="[]", option_c="{}", option_d="<>", correct_answer="B", explanation="方括号 []。")
Quiz.objects.create(lesson=l7_2_1, question="Python 变量在使用前需要声明类型吗？", option_a="需要", option_b="不需要", option_c="看情况", option_d="只能声明整数", correct_answer="B", explanation="Python 是动态类型语言，不需要声明类型。")
Quiz.objects.create(lesson=l7_2_1, question="movies = ['A', 'B', 'C']，movies[2] 是？", option_a="A", option_b="B", option_c="C", option_d="报错", correct_answer="C", explanation="索引 2 是第三个元素。")
Quiz.objects.create(lesson=l7_2_1, question="len(movies) 返回的是？", option_a="列表占用的内存", option_b="列表的元素个数", option_c="列表的最大索引", option_d="列表的名称", correct_answer="B", explanation="len() 返回长度。")
Quiz.objects.create(lesson=l7_2_1, question="判断题：列表中的元素必须是相同类型的。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，Python 列表可以包含混合类型的数据。")
Quiz.objects.create(lesson=l7_2_1, question="判断题：列表创建后，其大小不能改变。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，列表是动态的，可以随时增加或删除元素。")
Quiz.objects.create(lesson=l7_2_1, question="列表是可变的吗？", option_a="是", option_b="否", option_c="有时候是", option_d="不知道", correct_answer="A", explanation="列表 (List) 是可变数据类型。")
Quiz.objects.create(lesson=l7_2_1, question="如何获取列表的长度？", option_a="length()", option_b="size()", option_c="count()", option_d="len()", correct_answer="D", explanation="使用内置函数 len()。")
Quiz.objects.create(lesson=l7_2_1, question="空列表 [] 的布尔值是？", option_a="True", option_b="False", option_c="None", option_d="Error", correct_answer="B", explanation="空列表在布尔上下文中为 False。")

# 2.2 List Methods
l7_2_2 = create_lesson(
    chapter=ch7_2, title="2.2 列表操作：增删改", order=2, lesson_type='code',
    code_challenge_prompt="""# 1. 创建 movies 列表
# 2. 使用 append 添加 "Terry Jones"
# 3. 使用 pop 删除最后一个元素
movies = ["The Holy Grail", "The Life of Brian"]
movies.append("Terry Jones")
print(movies)
movies.pop()
print(movies)
""",
    content="""# 2.2 列表操作

## 1. 常用方法
列表自带了很多好用的方法（Method）：
- `append(x)`: 在末尾添加 x。
- `pop()`: 删除并返回末尾的元素。
- `extend(list)`: 将另一个列表拼接到末尾。
- `remove(x)`: 删除第一个出现的 x。
- `insert(i, x)`: 在索引 i 处插入 x。

## 2. 混合类型
Python 的列表可以装任何东西！数字、字符串，甚至是另一个列表。

## 3. append 和 extend 的区别
```python
movies = ["A", "B"]
movies.append(["C", "D"])
print(movies)
```

结果是把整个列表作为一个元素加入：

```text
['A', 'B', ['C', 'D']]
```

`extend()` 会把另一个列表里的元素逐个加入：

```python
movies = ["A", "B"]
movies.extend(["C", "D"])
print(movies)
```

结果：

```text
['A', 'B', 'C', 'D']
```

## 4. pop 和 remove 的区别
```python
movies.pop()
movies.remove("A")
```

- `pop()` 按位置删除，默认删除最后一个，并返回被删元素
- `remove(x)` 按值删除，删除第一个等于 `x` 的元素

## 5. del 语句
```python
del movies[0]
```

`del` 可以按索引删除，也可以删除切片。

## 6. 易错点
- `append()` 会把参数当成一个整体
- `remove()` 找不到元素会 `ValueError`
- `insert(0, x)` 会移动后续元素
- 很多列表方法会原地修改列表，返回值可能是 `None`

## 7. 小练习
用列表保存 3 个电影名，完成：
1. 末尾添加 1 个电影
2. 开头插入 1 个电影
3. 删除最后一个电影
4. 删除指定电影名
"""
)
Quiz.objects.create(lesson=l7_2_2, question="pop() 方法默认删除哪个元素？", option_a="第一个", option_b="最后一个", option_c="随机一个", option_d="指定的一个", correct_answer="B", explanation="默认删除末尾元素。")
Quiz.objects.create(lesson=l7_2_2, question="在列表末尾添加一个元素，使用？", option_a="add", option_b="push", option_c="append", option_d="insert", correct_answer="C", explanation="append 方法。")
Quiz.objects.create(lesson=l7_2_2, question="remove('A') 的作用是？", option_a="删除索引为 A 的元素", option_b="删除所有值为 A 的元素", option_c="删除第一个值为 A 的元素", option_d="报错", correct_answer="C", explanation="只删除第一个匹配项。")
Quiz.objects.create(lesson=l7_2_2, question="extend 方法接收的参数通常是？", option_a="一个数字", option_b="一个字符串", option_c="另一个列表", option_d="无参数", correct_answer="C", explanation="用于合并两个列表。")
Quiz.objects.create(lesson=l7_2_2, question="insert(0, 'Start') 会将元素插入到？", option_a="列表末尾", option_b="列表开头", option_c="列表中间", option_d="替换第一个元素", correct_answer="B", explanation="索引 0 是开头。")
Quiz.objects.create(lesson=l7_2_2, question="判断题：pop() 方法不仅删除元素，还会返回被删除的元素。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，可以用来获取被弹出的值。")
Quiz.objects.create(lesson=l7_2_2, question="判断题：remove() 如果找不到元素会静默失败（什么都不做）。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，会抛出 ValueError。")
Quiz.objects.create(lesson=l7_2_2, question="list.remove(x) 如果 x 不存在会怎样？", option_a="返回 None", option_b="返回 -1", option_c="抛出 ValueError", option_d="什么都不发生", correct_answer="C", explanation="remove 不存在的元素会报错。")
Quiz.objects.create(lesson=l7_2_2, question="list.insert(0, x) 的效率比 append(x) 高还是低？", option_a="高", option_b="低", option_c="一样", option_d="取决于 x", correct_answer="B", explanation="低，因为插入头部需要移动后续所有元素。")
Quiz.objects.create(lesson=l7_2_2, question="del list[0] 的作用是？", option_a="清空列表", option_b="删除第一个元素", option_c="删除最后一个元素", option_d="删除索引为 0 的变量", correct_answer="B", explanation="删除索引为 0 的元素。")

# 2.3 Nested Lists
l7_2_3 = create_lesson(
    chapter=ch7_2, title="2.3 嵌套列表与循环", order=3, lesson_type='code',
    code_challenge_prompt="""# 遍历嵌套列表
movies = ["The Holy Grail", 1975, ["Terry Jones", 91]]
for item in movies:
    if isinstance(item, list):
        for nested_item in item:
            print(nested_item)
    else:
        print(item)
""",
    content="""# 2.3 嵌套列表与循环

## 1. 列表里的列表
列表可以包含其他列表。
```python
movies = ["The Holy Grail", 1975, ["Terry Jones", 91]]
```

## 2. 处理嵌套数据
当我们遍历列表时，如果遇到子列表，直接 `print` 会打印出整个方括号。
我们需要判断：**如果**它是一个列表，**那么**深入一层继续处理。

## 3. isinstance()
`isinstance(item, list)` 用来检查一个变量是否是列表类型。

## 4. 为什么需要类型判断
嵌套列表中，普通元素和子列表需要不同处理：

```python
for item in movies:
    if isinstance(item, list):
        for nested_item in item:
            print(nested_item)
    else:
        print(item)
```

如果不判断类型，程序只能把内部列表整体打印出来。

## 5. 任意深度怎么办
如果嵌套层级不固定，手写多层 `for` 会很难维护。更自然的方式是递归。

```python
def print_items(items):
    for item in items:
        if isinstance(item, list):
            print_items(item)
        else:
            print(item)
```

这为后面的 `print_lol` 函数做铺垫。

## 6. 易错点
- `isinstance(item, list)` 返回布尔值
- `for` 默认只遍历最外层
- `len(["A", ["B", "C"]])` 是 2，不是 3
- 多层索引用多个方括号：`data[0][1]`

## 7. 小练习
给定：

```python
items = ["A", ["B", "C"], ["D", ["E"]]]
```

尝试写代码打印每个字符串。先用嵌套循环，再思考为什么递归更合适。
"""
)
Quiz.objects.create(lesson=l7_2_3, question="isinstance(x, list) 的作用是？", option_a="将 x 转为列表", option_b="判断 x 是否为列表", option_c="创建新列表", option_d="删除列表", correct_answer="B", explanation="类型检查。")
Quiz.objects.create(lesson=l7_2_3, question="对于嵌套列表 lst = [1, [2, 3]]，lst[1][0] 是？", option_a="1", option_b="2", option_c="3", option_d="[2, 3]", correct_answer="B", explanation="先取第二个元素 [2,3]，再取其第一个元素 2。")
Quiz.objects.create(lesson=l7_2_3, question="遍历列表通常使用哪种循环？", option_a="for", option_b="while", option_c="do-while", option_d="until", correct_answer="A", explanation="for loop 是遍历集合的首选。")
Quiz.objects.create(lesson=l7_2_3, question="如果列表层级很深（比如 10 层），手动写 for 循环嵌套会？", option_a="非常高效", option_b="非常痛苦且代码难看", option_c="自动优化", option_d="报错", correct_answer="B", explanation="深层嵌套难以维护，需要递归。")
Quiz.objects.create(lesson=l7_2_3, question="movies = ['A', ['B', 'C']]，len(movies) 是？", option_a="2", option_b="3", option_c="4", option_d="1", correct_answer="A", explanation="只有两个元素：字符串 'A' 和内部列表 ['B', 'C']。")
Quiz.objects.create(lesson=l7_2_3, question="判断题：Python 的列表可以嵌套任意层级。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，受限于内存，但逻辑上无限。")
Quiz.objects.create(lesson=l7_2_3, question="判断题：isinstance(3, list) 返回 True。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，3 是 int，不是 list。")
Quiz.objects.create(lesson=l7_2_3, question="嵌套列表可以有多深？", option_a="2层", option_b="10层", option_c="任意深度（受内存限制）", option_d="100层", correct_answer="C", explanation="Python 对嵌套深度没有硬性限制，只受递归深度和内存限制。")
Quiz.objects.create(lesson=l7_2_3, question="如何访问三层嵌套列表 list[0][0][0]？", option_a="list[0,0,0]", option_b="list(0)(0)(0)", option_c="list[0][0][0]", option_d="list.get(0,0,0)", correct_answer="C", explanation="使用多个方括号逐层访问。")
Quiz.objects.create(lesson=l7_2_3, question="for 循环可以遍历嵌套列表吗？", option_a="不可以", option_b="可以，但只能遍历最外层", option_c="可以自动遍历所有层", option_d="会报错", correct_answer="B", explanation="for 循环默认只遍历第一层，处理内部列表需要递归或嵌套循环。")


# Chapter 3: Structured Data
ch7_3, _ = Chapter.objects.get_or_create(course=c7, title="第3章：结构化数据 (Structured Data)", defaults={'order': 3})

# 3.1 Dictionaries
l7_3_1 = create_lesson(
    chapter=ch7_3, title="3.1 字典：更好的数据结构", order=1, lesson_type='code',
    code_challenge_prompt="""# 创建一个字典表示电影信息
movie = {
    "title": "The Holy Grail",
    "year": 1975,
    "director": "Terry Jones"
}
print(movie["year"])
""",
    content="""# 3.1 字典：更好的数据结构

## 1. 列表的问题
用列表存储数据时，我们必须记住索引的含义（索引 0 是标题？索引 1 是年份？）。这很麻烦。

## 2. 字典 (Dictionary)
字典允许我们要**名字**（Key）来访问数据，而不是索引。
```python
movie = {
    "title": "The Holy Grail",
    "year": 1975
}
```

## 3. 键值对
字典由 Key: Value 对组成。Key 必须是唯一的。

## 4. 修改和新增
```python
movie["year"] = 1979
movie["rating"] = 9.0
```

如果键已存在，就是修改；如果键不存在，就是新增。

## 5. 遍历字典
```python
for key, value in movie.items():
    print(key, value)
```

`items()` 会同时给出键和值。

## 6. get 安全访问
```python
print(movie.get("director", "unknown"))
```

如果键不存在，返回默认值，不会报 `KeyError`。

## 7. 嵌套结构
```python
movie = {
    "title": "The Holy Grail",
    "actors": ["Graham Chapman", "John Cleese"]
}
```

字典的值可以是列表，这让它适合表达更真实的数据。

## 8. 易错点
- 空 `{}` 是字典，不是集合
- 键必须不可变
- `in` 默认判断键，不判断值
- 重复键会被后面的值覆盖

## 9. 小练习
创建一个电影字典，包含 `title`、`year`、`actors`。输出电影名和演员数量。
"""
)
Quiz.objects.create(lesson=l7_3_1, question="字典使用什么符号定义？", option_a="[]", option_b="()", option_c="{}", option_d="<>", correct_answer="C", explanation="大括号 {}。")
Quiz.objects.create(lesson=l7_3_1, question="字典中访问数据使用的是？", option_a="索引 (0, 1...)", option_b="键 (Key)", option_c="值 (Value)", option_d="随机访问", correct_answer="B", explanation="通过 Key 查找 Value。")
Quiz.objects.create(lesson=l7_3_1, question="d = {'name': 'Tom'}，如何获取 'Tom'？", option_a="d[0]", option_b="d.Tom", option_c="d['name']", option_d="d('name')", correct_answer="C", explanation="使用方括号加键名。")
Quiz.objects.create(lesson=l7_3_1, question="字典的 Key 必须是？", option_a="唯一的", option_b="整数", option_c="字符串", option_d="可变的", correct_answer="A", explanation="键必须唯一且不可变（Hashable）。")
Quiz.objects.create(lesson=l7_3_1, question="列表和字典的主要区别是？", option_a="列表有序，字典无序（逻辑上）", option_b="列表用 {}，字典用 []", option_c="字典不能存数字", option_d="列表比字典慢", correct_answer="A", explanation="列表是序列，字典是映射。")
Quiz.objects.create(lesson=l7_3_1, question="判断题：字典中的 Value 可以是列表。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，Value 可以是任何对象。")
Quiz.objects.create(lesson=l7_3_1, question="判断题：两个不同的 Key 可以对应同一个 Value。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，如 {'a': 1, 'b': 1}。")
Quiz.objects.create(lesson=l7_3_1, question="字典的键可以是列表吗？", option_a="可以", option_b="不可以", option_c="看情况", option_d="可以，如果列表为空", correct_answer="B", explanation="列表是可变类型，不可哈希，不能作为字典的键。")
Quiz.objects.create(lesson=l7_3_1, question="字典的键可以是元组吗？", option_a="可以", option_b="不可以", option_c="必须是元组", option_d="只有空元组可以", correct_answer="A", explanation="元组是不可变的（如果其内容也都是不可变的），可以作为键。")
Quiz.objects.create(lesson=l7_3_1, question="{} 代表什么？", option_a="空列表", option_b="空元组", option_c="空字典", option_d="空集合", correct_answer="C", explanation="{} 默认表示空字典，空集合需要用 set()。")

# Chapter 4: Code Reuse
ch7_4, _ = Chapter.objects.get_or_create(course=c7, title="第4章：代码复用 (Code Reuse)", defaults={'order': 4})

# 4.1 Functions
l7_4_1 = create_lesson(
    chapter=ch7_4, title="4.1 函数：print_lol", order=1, lesson_type='code',
    code_challenge_prompt="""# 定义一个递归函数 print_lol 打印嵌套列表
def print_lol(the_list):
    for item in the_list:
        if isinstance(item, list):
            print_lol(item)
        else:
            print(item)

movies = ["The Holy Grail", 1975, ["Terry Jones", 91]]
print_lol(movies)
""",
    content="""# 4.1 函数：print_lol

## 1. 不要重复代码 (DRY)
如果你发现自己在复制粘贴代码，你就应该写一个函数。

## 2. 定义函数
使用 `def` 关键字。
```python
def print_lol(the_list):
    # 代码逻辑
```

## 3. 递归 (Recursion)
函数调用自身。这对于处理**任意深度**的嵌套列表非常有用。
我们在 `print_lol` 中调用 `print_lol` 来处理子列表。

## 4. print_lol 的完整版本
```python
def print_lol(the_list):
    for item in the_list:
        if isinstance(item, list):
            print_lol(item)
        else:
            print(item)
```

函数名来自 “print list of lists”，也就是打印列表里的列表。

## 5. 为什么函数让代码更好
函数的价值：
- 给一段逻辑起名字
- 避免重复代码
- 让主程序更清楚
- 方便测试和复用

## 6. 参数和调用
```python
print_lol(movies)
```

`movies` 是实参，传入函数；`the_list` 是形参，在函数内部接收它。

## 7. 基准情况在哪里
`print_lol` 的基准情况不是单独写的 `if n == 1`，而是遇到普通元素时直接打印，不再递归。

## 8. 易错点
- 函数定义后不会自动运行，必须调用
- 递归必须让问题越来越小或越来越接近普通元素
- 忘记缩进会改变函数体范围
- 没写 `return` 的函数默认返回 `None`

## 9. 小练习
改造 `print_lol`：增加一个参数 `level`，打印嵌套层级缩进。
"""
)
Quiz.objects.create(lesson=l7_4_1, question="DRY 原则的意思是？", option_a="Do Repeat Yourself", option_b="Don't Repeat Yourself", option_c="Do Right Yesterday", option_d="Data Ready Yet", correct_answer="B", explanation="不要重复造轮子。")
Quiz.objects.create(lesson=l7_4_1, question="Python 中定义函数使用哪个关键字？", option_a="function", option_b="def", option_c="func", option_d="define", correct_answer="B", explanation="def 是 define 的缩写。")
Quiz.objects.create(lesson=l7_4_1, question="递归函数是指？", option_a="调用其他函数的函数", option_b="调用自己的函数", option_c="没有返回值的函数", option_d="无限循环的函数", correct_answer="B", explanation="Self-calling function。")
Quiz.objects.create(lesson=l7_4_1, question="处理任意层级的嵌套列表，最适合的算法是？", option_a="多层 for 循环", option_b="递归", option_c="随机抽样", option_d="二分查找", correct_answer="B", explanation="递归可以自然适应任意深度。")
Quiz.objects.create(lesson=l7_4_1, question="函数参数 (Argument) 的作用是？", option_a="定义返回值", option_b="向函数传递数据", option_c="停止函数", option_d="定义函数名", correct_answer="B", explanation="传递输入数据。")
Quiz.objects.create(lesson=l7_4_1, question="判断题：Python 函数必须有 return 语句。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，没有 return 默认返回 None。")
Quiz.objects.create(lesson=l7_4_1, question="判断题：缩进在 Python 函数定义中非常重要。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，决定了函数体的范围。")
Quiz.objects.create(lesson=l7_4_1, question="函数内部定义的变量在外部可见吗？", option_a="可见", option_b="不可见", option_c="看情况", option_d="只有全局变量可见", correct_answer="B", explanation="函数内部定义的变量是局部变量，作用域仅限于函数内部。")
Quiz.objects.create(lesson=l7_4_1, question="递归深度太深会怎样？", option_a="程序变慢", option_b="栈溢出 (RecursionError)", option_c="自动优化为循环", option_d="无影响", correct_answer="B", explanation="Python 默认递归深度限制通常为 1000，超过会报错。")
Quiz.objects.create(lesson=l7_4_1, question="定义函数时参数列表里的变量叫什么？", option_a="实参", option_b="形参", option_c="全局变量", option_d="常量", correct_answer="B", explanation="定义时叫形式参数 (Parameter)，调用时传入的叫实际参数 (Argument)。")

# 4.2 Modules
l7_4_2 = create_lesson(
    chapter=ch7_4, title="4.2 模块：nester.py", order=2, lesson_type='text',
    code_challenge_prompt="# 假设我们将 print_lol 保存到了 nester.py\n# import nester\n# nester.print_lol(movies)",
    content="""# 4.2 模块：nester.py

## 1. 什么是模块？
模块就是一个包含 Python 代码的文件（.py）。
通过模块，我们可以在不同的程序之间共享代码。

## 2. 创建模块
只需将 `print_lol` 函数保存到一个名为 `nester.py` 的文件中。

## 3. 导入模块
使用 `import nester`。
调用函数时需要加上命名空间：`nester.print_lol(movies)`。

## 4. 模块的好处
如果所有代码都写在一个文件里，很快会变乱。

模块可以帮助我们：
- 按功能拆分代码
- 在多个程序中复用函数
- 降低主程序复杂度
- 更容易维护和测试

## 5. import 的几种写法
```python
import nester
nester.print_lol(movies)
```

```python
from nester import print_lol
print_lol(movies)
```

```python
import nester as ns
ns.print_lol(movies)
```

## 6. 命名空间
`nester.print_lol` 中的 `nester` 就是命名空间。它能避免不同模块里同名函数互相冲突。

## 7. 不推荐 import *
```python
from nester import *
```

这种写法会把模块里的名字都导入当前文件，容易造成变量名冲突。学习阶段可以见过，但实战中少用。

## 8. 易错点
- 模块文件名不要和标准库同名，例如不要叫 `random.py`
- 导入自己写的模块时，文件通常要在同一目录或 Python 能找到的路径中
- 修改模块后，有些交互环境需要重启才能重新加载

## 9. 小练习
把 `print_lol` 保存到 `nester.py`，再写一个 `main.py` 导入并调用它。
"""
)
Quiz.objects.create(lesson=l7_4_2, question="导入模块的关键字是？", option_a="load", option_b="include", option_c="import", option_d="use", correct_answer="C", explanation="import。")
Quiz.objects.create(lesson=l7_4_2, question="如果模块名为 my_module，调用其中的 func 函数应该是？", option_a="func()", option_b="my_module.func()", option_c="call func from my_module", option_d="import func", correct_answer="B", explanation="需要使用模块名作为命名空间前缀。")
Quiz.objects.create(lesson=l7_4_2, question="Python 模块文件的后缀名必须是？", option_a=".txt", option_b=".java", option_c=".py", option_d=".exe", correct_answer="C", explanation="Python 源码文件。")
Quiz.objects.create(lesson=l7_4_2, question="PyPI 是什么？", option_a="Python 解释器", option_b="Python 包索引 (Package Index)", option_c="Python 编辑器", option_d="Python 教程", correct_answer="B", explanation="第三方库的仓库。")
Quiz.objects.create(lesson=l7_4_2, question="使用 from module import function 的好处是？", option_a="代码运行更快", option_b="可以直接使用函数名，不用加前缀", option_c="可以导入私有函数", option_d="没有区别", correct_answer="B", explanation="引入当前命名空间。")
Quiz.objects.create(lesson=l7_4_2, question="判断题：你自己写的 .py 文件也可以作为模块被导入。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，只要在 Python 路径下。")
Quiz.objects.create(lesson=l7_4_2, question="判断题：一个模块只能包含一个函数。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，可以包含任意数量的函数、类和变量。")
Quiz.objects.create(lesson=l7_4_2, question="import module as alias 的作用？", option_a="导入模块所有内容", option_b="给模块起别名", option_c="只导入部分内容", option_d="重新加载模块", correct_answer="B", explanation="as 关键字用于给导入的模块指定一个别名。")
Quiz.objects.create(lesson=l7_4_2, question="from module import * 推荐吗？", option_a="强烈推荐", option_b="不推荐", option_c="无所谓", option_d="必须使用", correct_answer="B", explanation="不推荐，容易导致命名空间污染（变量名冲突）。")
Quiz.objects.create(lesson=l7_4_2, question="一个 .py 文件就是一个模块吗？", option_a="是", option_b="不是", option_c="只有含类的才是", option_d="只有含函数的才是", correct_answer="A", explanation="Python 中任何 .py 文件都可以被视为一个模块。")

# Chapter 5: File Processing
ch7_5, _ = Chapter.objects.get_or_create(course=c7, title="第5章：文件处理 (File Processing)", defaults={'order': 5})

# 5.1 Reading Files
l7_5_1 = create_lesson(
    chapter=ch7_5, title="5.1 读取文本文件：open 与 read", order=1, lesson_type='code',
    code_challenge_prompt="""# 假设 notes.txt 文件中有几行文字
# 请用 open + read 读取它的内容

with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()

print(content)
""",
    content="""# 5.1 读取文本文件：open 与 read

## 1. 为什么要学文件操作？
前面的数据很多都直接写在代码里，但真实程序往往需要**从文件读取数据**。
比如：
- 读取成绩表
- 读取配置文件
- 读取用户保存的文本内容

## 2. 打开文件
Python 最常用的方式是 `open()`：

```python
f = open("notes.txt", "r", encoding="utf-8")
content = f.read()
f.close()
```

其中：
- `"r"` 表示读取模式（read）
- `encoding="utf-8"` 表示按 UTF-8 编码读取中文文本

## 3. 更推荐的写法：with open
```python
with open("notes.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)
```

`with` 的好处是：**文件用完后会自动关闭**。

## 4. 常见读取方式
- `read()`：一次读完整个文件
- `readline()`：读一行
- `readlines()`：读成多行列表

## 5. 逐行遍历文件
大文件不适合一次性读入内存，可以逐行处理：

```python
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
```

`strip()` 可以去掉行尾换行符和多余空白。

## 6. 文件路径
```python
open("notes.txt")
```

表示在当前工作目录下找文件。若文件不在当前目录，需要写相对路径或绝对路径。

## 7. 异常处理
读取不存在的文件会报错：

```python
FileNotFoundError
```

可以用 `try-except` 处理：

```python
try:
    with open("notes.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("文件不存在")
```

## 8. 易错点
- 读取文件前要确认路径正确
- 中文文本建议指定 `encoding="utf-8"`
- `read()` 读完整文件，文件很大时要谨慎
- `with open` 比手动 `close()` 更安全

## 9. 小练习
读取一个文本文件，统计：
1. 一共有多少行
2. 一共有多少个字符
3. 哪些行包含关键词 `"Python"`
"""
)
Quiz.objects.create(lesson=l7_5_1, question="open('a.txt', 'r') 中 'r' 表示？", option_a="写入", option_b="读取", option_c="追加", option_d="删除", correct_answer="B", explanation="'r' 是 read，表示读取模式。")
Quiz.objects.create(lesson=l7_5_1, question="读取整个文件内容最常用的方法是？", option_a="write()", option_b="append()", option_c="read()", option_d="close()", correct_answer="C", explanation="read() 用于读取文件内容。")
Quiz.objects.create(lesson=l7_5_1, question="with open(...) as f 的主要好处是？", option_a="自动关闭文件", option_b="自动删除文件", option_c="自动压缩文件", option_d="自动创建图表", correct_answer="A", explanation="with 会在结束后自动关闭文件。")
Quiz.objects.create(lesson=l7_5_1, question="readline() 的作用是？", option_a="读取一整列", option_b="读取一行", option_c="写入一行", option_d="删除一行", correct_answer="B", explanation="readline() 一次读取一行。")
Quiz.objects.create(lesson=l7_5_1, question="读取中文文本时，常见编码参数写作？", option_a="encoding='gbk-only'", option_b="encoding='utf-8'", option_c="encoding='python'", option_d="encoding='ascii-all'", correct_answer="B", explanation="UTF-8 是最常见的文本编码。")
Quiz.objects.create(lesson=l7_5_1, question="判断题：文件读取完成后，最好及时关闭文件。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，避免资源占用。")
Quiz.objects.create(lesson=l7_5_1, question="判断题：with open 是为了让代码更安全、更易维护。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，尤其体现在自动关闭文件。")
Quiz.objects.create(lesson=l7_5_1, question="readlines() 一般返回什么？", option_a="一个整数", option_b="一个字符串", option_c="一个行列表", option_d="一个字典", correct_answer="C", explanation="readlines() 会把每一行组成列表。")
Quiz.objects.create(lesson=l7_5_1, question="如果文件不存在，open('x.txt', 'r') 常会抛出？", option_a="IndexError", option_b="FileNotFoundError", option_c="TypeError", option_d="SyntaxError", correct_answer="B", explanation="读取不存在的文件通常抛出 FileNotFoundError。")
Quiz.objects.create(lesson=l7_5_1, question="文件操作最适合保存哪类数据？", option_a="需要长期保留的文本或记录", option_b="只能保存图片", option_c="只能保存数字", option_d="只能保存列表", correct_answer="A", explanation="文件常用于长期保存文本和程序数据。")

# 5.2 Writing Files
l7_5_2 = create_lesson(
    chapter=ch7_5, title="5.2 写入与追加：write、w 模式、a 模式", order=2, lesson_type='code',
    code_challenge_prompt="""# 将一条学习记录写入 study_log.txt
with open("study_log.txt", "a", encoding="utf-8") as f:
    f.write("今天完成了文件操作练习\\n")

print("记录已写入")
""",
    content="""# 5.2 写入与追加：write、w 模式、a 模式

## 1. 写文件的两种常见模式
- `"w"`：写入模式，如果文件已存在会**覆盖原内容**
- `"a"`：追加模式，在文件末尾继续写

## 2. 写入示例
```python
with open("hello.txt", "w", encoding="utf-8") as f:
    f.write("你好，Python！")
```

## 3. 追加示例
```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("新增一条记录\\n")
```

## 4. 为什么追加很有用？
像学习日志、运行记录、签到信息，这些内容通常不是覆盖，而是**一条一条接着写**。

## 5. 一个习惯
写文件时要想清楚：
- 是要覆盖旧内容？
- 还是保留旧内容继续追加？

## 6. write 不会自动换行
```python
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("第一行")
    f.write("第二行")
```

结果可能会连在一起：

```text
第一行第二行
```

如果需要换行，要自己加 `\n`：

```python
f.write("第一行\n")
```

## 7. writelines
```python
lines = ["A\n", "B\n", "C\n"]
with open("out.txt", "w", encoding="utf-8") as f:
    f.writelines(lines)
```

`writelines()` 不会自动给每个元素加换行符。

## 8. 覆盖风险
`"w"` 模式会清空旧文件内容。写日志、历史记录、打卡记录时，一般用 `"a"` 更安全。

## 9. 易错点
- `write()` 只能写字符串，写数字前要 `str()`
- `"w"` 会覆盖，`"a"` 会追加
- 换行要自己写 `\n`
- 文件夹不存在时，写文件也会报错

## 10. 小练习
写一个程序，把三条学习记录逐行追加到 `study_log.txt`。
"""
)
Quiz.objects.create(lesson=l7_5_2, question="open('a.txt', 'w') 中 'w' 模式表示？", option_a="读取", option_b="写入并可能覆盖原内容", option_c="追加", option_d="只读", correct_answer="B", explanation="'w' 会写入文件，旧内容可能被覆盖。")
Quiz.objects.create(lesson=l7_5_2, question="想在文件末尾继续添加内容，应该使用？", option_a="'r'", option_b="'w'", option_c="'a'", option_d="'x'", correct_answer="C", explanation="'a' 是追加模式。")
Quiz.objects.create(lesson=l7_5_2, question="把字符串写入文件最常用的方法是？", option_a="read()", option_b="write()", option_c="append()", option_d="insert()", correct_answer="B", explanation="write() 用来写入字符串。")
Quiz.objects.create(lesson=l7_5_2, question="学习日志更适合使用哪种模式？", option_a="'w'", option_b="'a'", option_c="'r'", option_d="'rb'", correct_answer="B", explanation="日志通常是一条条追加。")
Quiz.objects.create(lesson=l7_5_2, question="使用 'w' 模式操作已存在文件时，最需要注意什么？", option_a="会自动加密", option_b="内容可能被覆盖", option_c="只能写一行", option_d="不能写中文", correct_answer="B", explanation="'w' 模式会清空旧内容后重写。")
Quiz.objects.create(lesson=l7_5_2, question="判断题：write() 写入换行时，通常需要自己写 '\\n'。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，write 不会自动换行。")
Quiz.objects.create(lesson=l7_5_2, question="判断题：追加模式适合记录多次运行结果。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，追加模式不会覆盖旧记录。")
Quiz.objects.create(lesson=l7_5_2, question="写文件时使用 with open 的主要原因之一是？", option_a="自动保存图片", option_b="自动关闭文件", option_c="自动生成目录", option_d="自动排序文本", correct_answer="B", explanation="with 可以自动关闭文件。")
Quiz.objects.create(lesson=l7_5_2, question="如果想生成一个新的文本报告，通常更适合先用哪种模式？", option_a="'w'", option_b="'a'", option_c="'r'", option_d="'None'", correct_answer="A", explanation="生成全新报告常用 w 模式。")
Quiz.objects.create(lesson=l7_5_2, question="文件写入和追加最核心的区别是？", option_a="是否支持中文", option_b="是否会保留原内容", option_c="是否需要 import", option_d="是否可以打印", correct_answer="B", explanation="w 可能覆盖，a 会保留原内容并继续写。")

# 5.3 Practical File Project
l7_5_3 = create_lesson(
    chapter=ch7_5, title="5.3 综合实战：学习日志文件", order=3, lesson_type='code',
    code_challenge_prompt="""# 用文件记录今天完成的任务
task = "完成 NumPy 课程"

with open("study_log.txt", "a", encoding="utf-8") as f:
    f.write(task + "\\n")

with open("study_log.txt", "r", encoding="utf-8") as f:
    print(f.read())
""",
    content="""# 5.3 综合实战：学习日志文件

## 1. 实战目标
把“写入”和“读取”连起来，做一个最基础的学习日志。

## 2. 第一步：把今天完成的任务写入文件
```python
task = "完成 NumPy 课程"
with open("study_log.txt", "a", encoding="utf-8") as f:
    f.write(task + "\\n")
```

## 3. 第二步：把日志再读出来
```python
with open("study_log.txt", "r", encoding="utf-8") as f:
    print(f.read())
```

## 4. 这节课练到了什么？
- 追加写入
- 读取文本
- `with open`
- 日志型小项目思维

## 5. 为什么它适合初学者？
因为这是非常真实的编程任务：把程序结果保存下来，而不是只打印在屏幕上。

## 6. 加上时间戳
日志最好记录时间：

```python
from datetime import datetime

task = "完成文件操作练习"
now = datetime.now().strftime("%Y-%m-%d %H:%M")

with open("study_log.txt", "a", encoding="utf-8") as f:
    f.write(f"{now} - {task}\n")
```

## 7. 读取并编号显示
```python
with open("study_log.txt", "r", encoding="utf-8") as f:
    for index, line in enumerate(f, start=1):
        print(index, line.strip())
```

`enumerate()` 可以在遍历时同时得到编号。

## 8. 统计日志数量
```python
with open("study_log.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()

print("记录条数:", len(lines))
```

## 9. 易错点
- 追加日志用 `"a"`，不要误用 `"w"`
- 写入时记得加换行
- 读取前确认文件已经存在
- 日志内容如果来自用户输入，要先检查是否为空

## 10. 综合升级
把学习日志程序升级成菜单：
1. 输入 `1` 添加日志
2. 输入 `2` 查看日志
3. 输入 `3` 统计日志条数
4. 输入 `0` 退出程序
"""
)
Quiz.objects.create(lesson=l7_5_3, question="学习日志项目中，先把任务保存下来更适合用哪种操作？", option_a="读取", option_b="追加写入", option_c="删除", option_d="排序", correct_answer="B", explanation="日志通常使用追加写入。")
Quiz.objects.create(lesson=l7_5_3, question="想把保存后的日志再次显示出来，下一步应做什么？", option_a="再 append 一次", option_b="打开文件读取", option_c="删除文件", option_d="创建字典", correct_answer="B", explanation="读取文件才能看到保存内容。")
Quiz.objects.create(lesson=l7_5_3, question="学习日志最适合说明文件操作的哪种价值？", option_a="让代码更短", option_b="把结果长期保存下来", option_c="替代列表", option_d="替代函数", correct_answer="B", explanation="文件操作的重要价值之一是持久保存数据。")
Quiz.objects.create(lesson=l7_5_3, question="下面哪种场景最像学习日志项目？", option_a="记录签到信息", option_b="只打印 Hello", option_c="画流程图", option_d="定义空元组", correct_answer="A", explanation="签到、打卡、日志都属于记录型文件应用。")
Quiz.objects.create(lesson=l7_5_3, question="判断题：文件操作让程序结果不只停留在屏幕输出上。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，文件可以保存结果。")
Quiz.objects.create(lesson=l7_5_3, question="判断题：日志型小项目适合帮助初学者理解文件读写。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，这种场景直观且实用。")

print("所有课程创建完成！")
