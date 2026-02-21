import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from courses.models import Course, Chapter, Lesson, Quiz

print("正在清理旧数据...")
Course.objects.all().delete()

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
l1_1 = Lesson.objects.create(
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

# 1.2 变量与命名
l1_2 = Lesson.objects.create(
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

# 1.3 基本数据类型
l1_3 = Lesson.objects.create(
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

# 1.4 输入与输出
l1_4 = Lesson.objects.create(
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

# --- 第2章：运算符与表达式 ---
ch2, _ = Chapter.objects.get_or_create(course=c1, title="第2章：运算符与表达式", defaults={'order': 2})

# 2.1 算术运算符
l2_1 = Lesson.objects.create(
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

# 2.2 比较与逻辑运算符
l2_2 = Lesson.objects.create(
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

# 2.3 运算符优先级
l2_3 = Lesson.objects.create(
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

# --- 第3章：决策与分支 ---
ch3, _ = Chapter.objects.get_or_create(course=c1, title="第3章：决策与分支", defaults={'order': 3})

# 3.1 if 结构
l3_1 = Lesson.objects.create(
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

# --- 第4章：循环结构 ---
ch4, _ = Chapter.objects.get_or_create(course=c1, title="第4章：循环结构", defaults={'order': 4})

# 4.1 for 循环
l4_1 = Lesson.objects.create(
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

# 4.2 while 循环
l4_2 = Lesson.objects.create(
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

# 4.3 循环控制
l4_3 = Lesson.objects.create(
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

# ==========================================
# Course 2: GESP 2级 - 逻辑进阶
# ==========================================
print("正在创建 GESP 2级 课程...")
c2, _ = Course.objects.get_or_create(
    title="GESP 2级：逻辑进阶",
    description="深入掌握 Python 数据容器。重点讲解列表（List）的增删改查、字符串操作、多层循环嵌套以及 ASCII 码等进阶概念。对应 GESP 二级考纲。",
    defaults={'order': 2}
)

ch2_1, _ = Chapter.objects.get_or_create(course=c2, title="第1章：列表 List", defaults={'order': 1})

# 1.1 列表基础
l2_1_1 = Lesson.objects.create(
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


# 1.2 列表操作
l2_1_2 = Lesson.objects.create(
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

ch2_2, _ = Chapter.objects.get_or_create(course=c2, title="第2章：字符串进阶", defaults={'order': 2})

# 2.1 字符串操作
l2_2_1 = Lesson.objects.create(
    chapter=ch2_2, title="2.1 字符串常用方法", order=1, lesson_type='text',
    code_challenge_prompt="# 将字符串 ' python ' 去掉首尾空格并转为大写\ns = ' python '\nprint(s.strip().upper())",
    content="""# 2.1 字符串常用方法

字符串和列表很像，也有索引和切片，但字符串是**不可变**的（不能直接修改某个字符）。

## 1. 大小写转换
- `s.upper()`: 全大写
- `s.lower()`: 全小写
- `s.capitalize()`: 首字母大写

```python
s = "Hello"
print(s.upper()) # "HELLO"
```

## 2. 查找与替换
- `s.find(sub)`: 查找子串的位置，找不到返回 -1。
- `s.replace(old, new)`: 替换。

```python
s = "I love Python"
print(s.replace("Python", "Coding")) # "I love Coding"
```

## 3. 分割与合并 (重点)
- `s.split(sep)`: 把字符串切成列表。
- `sep.join(list)`: 把列表拼成字符串。

```python
s = "apple,banana,orange"
lst = s.split(",")   # ['apple', 'banana', 'orange']

print("-".join(lst)) # "apple-banana-orange"
```

## 4. 去除空白
- `s.strip()`: 去除首尾空格（或换行符）。

```python
s = "  hello  "
print(s.strip()) # "hello"
```
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


# 2.2 ASCII 码
l2_2_2 = Lesson.objects.create(
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

## 4. 字符串比较
字符串比较实际上是比较 ASCII 码的大小。
```python
print('a' > 'A') # True (97 > 65)
print('apple' > 'banana') # False (比较第一个字母 'a' < 'b')
```
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
l3_1_1 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l3_1_1, question="如果不写 return 语句，函数默认返回什么？", option_a="0", option_b="False", option_c="None", option_d="Error", correct_answer="C", explanation="默认返回 None。")
Quiz.objects.create(lesson=l3_1_1, question="定义函数使用哪个关键字？", option_a="function", option_b="def", option_c="func", option_d="define", correct_answer="B", explanation="使用 def。")
Quiz.objects.create(lesson=l3_1_1, question="def foo(): return 1\nprint(foo()) 输出？", option_a="foo", option_b="1", option_c="None", option_d="Error", correct_answer="B", explanation="输出 1。")
Quiz.objects.create(lesson=l3_1_1, question="函数可以没有参数吗？", option_a="可以", option_b="不可以", option_c="必须有", option_d="看情况", correct_answer="A", explanation="函数参数是可选的。")
Quiz.objects.create(lesson=l3_1_1, question="return 语句的作用？", option_a="打印", option_b="返回结果并结束函数", option_c="暂停", option_d="无作用", correct_answer="B", explanation="返回结果并结束。")
Quiz.objects.create(lesson=l3_1_1, question="判断题：一个函数可以有多个 return。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l3_1_1, question="判断题：函数必须有返回值。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，可以是 void 函数。")

# 1.2 变量作用域
l3_1_2 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l3_1_2, question="如何修改全局变量？", option_a="直接赋值", option_b="global 声明", option_c="extern", option_d="public", correct_answer="B", explanation="使用 global。")
Quiz.objects.create(lesson=l3_1_2, question="x=1; def f(): x=2; print(x); f(); print(x)", option_a="2 2", option_b="2 1", option_c="1 1", option_d="1 2", correct_answer="B", explanation="局部变量不影响全局。")
Quiz.objects.create(lesson=l3_1_2, question="局部变量作用域？", option_a="函数内", option_b="全局", option_c="类内", option_d="文件内", correct_answer="A", explanation="函数内部。")
Quiz.objects.create(lesson=l3_1_2, question="def f(): y=5; print(y) 外部访问 y？", option_a="5", option_b="None", option_c="报错", option_d="0", correct_answer="C", explanation="报错，NameError。")
Quiz.objects.create(lesson=l3_1_2, question="global 作用？", option_a="定义局部", option_b="声明全局", option_c="导入", option_d="类", correct_answer="B", explanation="声明全局变量。")
Quiz.objects.create(lesson=l3_1_2, question="判断题：函数内可直接读取全局变量。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l3_1_2, question="判断题：局部变量可与全局变量同名。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，会发生遮蔽。")

ch3_2, _ = Chapter.objects.get_or_create(course=c3, title="第2章：元组与异常处理", defaults={'order': 2})

# 2.1 元组 Tuple
l3_2_1 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l3_2_1, question="t = (1, 2, 3)，t[0] = 10 会发生什么？", option_a="t变成(10,2,3)", option_b="报错", option_c="t不变", option_d="t变成[10,2,3]", correct_answer="B", explanation="元组是不可变的，不能修改。")
Quiz.objects.create(lesson=l3_2_1, question="如何定义包含一个元素 5 的元组？", option_a="(5)", option_b="(5,)", option_c="[5]", option_d="{5}", correct_answer="B", explanation="必须加逗号，否则被视为数学括号。")
Quiz.objects.create(lesson=l3_2_1, question="元组支持哪种操作？", option_a="append", option_b="remove", option_c="count", option_d="sort", correct_answer="C", explanation="支持查询类操作如 count。")
Quiz.objects.create(lesson=l3_2_1, question="t = (1, 2) + (3, 4) 的结果？", option_a="(1, 2, 3, 4)", option_b="(4, 6)", option_c="报错", option_d="((1,2),(3,4))", correct_answer="A", explanation="元组拼接。")
Quiz.objects.create(lesson=l3_2_1, question="列表和元组的主要区别？", option_a="列表用()", option_b="元组可变", option_c="元组不可变", option_d="列表不能存字符串", correct_answer="C", explanation="元组不可变。")
Quiz.objects.create(lesson=l3_2_1, question="判断题：元组可以包含列表作为元素。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，如 (1, [2, 3])。")
Quiz.objects.create(lesson=l3_2_1, question="判断题：空元组是 ()。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")

# 2.2 异常处理
l3_2_2 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l3_2_2, question="处理异常使用哪个关键字？", option_a="catch", option_b="except", option_c="error", option_d="handle", correct_answer="B", explanation="try-except 结构。")
Quiz.objects.create(lesson=l3_2_2, question="finally 代码块什么时候执行？", option_a="出错时", option_b="不出错时", option_c="总是执行", option_d="不一定", correct_answer="C", explanation="总是执行。")
Quiz.objects.create(lesson=l3_2_2, question="捕获所有错误的基类是？", option_a="Error", option_b="Exception", option_c="Base", option_d="Object", correct_answer="B", explanation="Exception。")
Quiz.objects.create(lesson=l3_2_2, question="int('abc') 会抛出什么异常？", option_a="ValueError", option_b="TypeError", option_c="NameError", option_d="IndexError", correct_answer="A", explanation="值错误。")
Quiz.objects.create(lesson=l3_2_2, question="try 块中没有错误，会执行哪个块？", option_a="except", option_b="else", option_c="catch", option_d="error", correct_answer="B", explanation="else 块。")
Quiz.objects.create(lesson=l3_2_2, question="判断题：一个 try 可以对应多个 except。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l3_2_2, question="判断题：except 必须配合 try 使用。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")


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
l4_1_1 = Lesson.objects.create(
    chapter=ch4_1, title="1.1 字典 Dictionary", order=1, lesson_type='text',
    code_challenge_prompt="# 创建字典并访问\nd = {'name': 'Tom', 'age': 18}\nprint(d['name'])",
    content="""# 1.1 字典 Dictionary

## 1. 什么是字典？
键值对（Key-Value）的集合。键必须唯一且不可变。

```python
d = {"name": "Alice", "age": 12}
```

## 2. 常用操作
- `d[key]`: 获取值。
- `d[key] = value`: 修改或新增。
- `del d[key]`: 删除。
- `d.get(key, default)`: 安全获取。

## 3. 遍历
- `d.keys()`, `d.values()`, `d.items()`
"""
)
Quiz.objects.create(lesson=l4_1_1, question="d = {'a': 1}，d['b'] = 2 后 d 是？", option_a="{'a':1}", option_b="{'a':1, 'b':2}", option_c="报错", option_d="{'b':2}", correct_answer="B", explanation="新增键值对。")
Quiz.objects.create(lesson=l4_1_1, question="字典的键必须是？", option_a="可变的", option_b="不可变的", option_c="字符串", option_d="整数", correct_answer="B", explanation="不可变类型（Hashable）。")
Quiz.objects.create(lesson=l4_1_1, question="d.get('x', 0) 如果 x 不存在返回？", option_a="None", option_b="0", option_c="报错", option_d="False", correct_answer="B", explanation="返回默认值 0。")
Quiz.objects.create(lesson=l4_1_1, question="d.items() 返回什么？", option_a="键列表", option_b="值列表", option_c="键值对元组列表", option_d="字符串", correct_answer="C", explanation="键值对。")
Quiz.objects.create(lesson=l4_1_1, question="清空字典用什么方法？", option_a="delete()", option_b="clean()", option_c="clear()", option_d="empty()", correct_answer="C", explanation="clear()。")
Quiz.objects.create(lesson=l4_1_1, question="判断题：字典是有序的（Python 3.7+）。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l4_1_1, question="判断题：字典可以有重复的键。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，键唯一。")

# 1.2 集合 Set
l4_1_2 = Lesson.objects.create(
    chapter=ch4_1, title="1.2 集合 Set", order=2, lesson_type='code',
    code_challenge_prompt="# 集合去重\nlst = [1, 2, 2, 3, 3, 3]\ns = set(lst)\nprint(s)",
    content="""# 1.2 集合 Set

## 1. 什么是集合？
无序、不重复的元素集合。就像没有值的字典。
用 `{}` 定义，但空集合必须用 `set()`。

```python
s = {1, 2, 3}
```

## 2. 核心特性：去重
```python
lst = [1, 2, 2, 3]
print(list(set(lst))) # [1, 2, 3]
```

## 3. 集合运算
- `&` 交集
- `|` 并集
- `-` 差集
"""
)
Quiz.objects.create(lesson=l4_1_2, question="创建空集合使用？", option_a="{}", option_b="[]", option_c="set()", option_d="()", correct_answer="C", explanation="{} 是空字典。")
Quiz.objects.create(lesson=l4_1_2, question="set([1, 2, 2]) 的结果？", option_a="{1, 2, 2}", option_b="{1, 2}", option_c="[1, 2]", option_d="报错", correct_answer="B", explanation="自动去重。")
Quiz.objects.create(lesson=l4_1_2, question="{1, 2} & {2, 3} 的结果？", option_a="{1, 2, 3}", option_b="{2}", option_c="{1, 3}", option_d="{}", correct_answer="B", explanation="交集。")
Quiz.objects.create(lesson=l4_1_2, question="集合中的元素必须是？", option_a="可变的", option_b="不可变的", option_c="有序的", option_d="无限制", correct_answer="B", explanation="不可变（Hashable）。")
Quiz.objects.create(lesson=l4_1_2, question="s.add(1) 的作用？", option_a="添加元素", option_b="删除元素", option_c="排序", option_d="求和", correct_answer="A", explanation="添加。")
Quiz.objects.create(lesson=l4_1_2, question="判断题：集合是有序的，可以通过索引访问。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，无序。")
Quiz.objects.create(lesson=l4_1_2, question="判断题：集合不能包含重复元素。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")

ch4_2, _ = Chapter.objects.get_or_create(course=c4, title="第2章：面向对象编程 OOP", defaults={'order': 2})

# 2.1 类与对象
l4_2_1 = Lesson.objects.create(
    chapter=ch4_2, title="2.1 类与对象基础", order=1, lesson_type='text',
    code_challenge_prompt="# 定义一个 Dog 类，有一个 bark 方法\nclass Dog:\n    def bark(self):\n        print('Wang!')\n\nd = Dog()\nd.bark()",
    content="""# 2.1 类与对象基础

## 1. 什么是类 (Class)？
类是创建对象的**蓝图**或**模板**。对象是类的**实例**。
比如：“狗”是一个类，“你家那只叫旺财的狗”是一个对象。

## 2. 定义类
```python
class Dog:
    def bark(self):
        print("Wang!")
```

## 3. 创建对象
```python
my_dog = Dog()
my_dog.bark() # 调用方法
```

## 4. self 是什么？
`self` 代表对象自己。在类的方法中，第一个参数必须是 `self`。
"""
)
Quiz.objects.create(lesson=l4_2_1, question="定义类使用哪个关键字？", option_a="def", option_b="class", option_c="object", option_d="struct", correct_answer="B", explanation="class。")
Quiz.objects.create(lesson=l4_2_1, question="类方法中第一个参数通常命名为？", option_a="this", option_b="me", option_c="self", option_d="obj", correct_answer="C", explanation="self。")
Quiz.objects.create(lesson=l4_2_1, question="根据类创建对象的过程叫？", option_a="初始化", option_b="实例化", option_c="抽象", option_d="继承", correct_answer="B", explanation="实例化。")
Quiz.objects.create(lesson=l4_2_1, question="Dog() 返回的是？", option_a="一个类", option_b="一个函数", option_c="一个对象", option_d="None", correct_answer="C", explanation="对象（实例）。")
Quiz.objects.create(lesson=l4_2_1, question="对象调用方法 d.bark() 等价于？", option_a="Dog.bark(d)", option_b="bark(d)", option_c="d.bark", option_d="Dog.bark()", correct_answer="A", explanation="类名.方法名(实例)。")
Quiz.objects.create(lesson=l4_2_1, question="判断题：一个类可以创建多个不同的对象。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")
Quiz.objects.create(lesson=l4_2_1, question="判断题：self 关键字是 Python 强制要求的语法，不能改名。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，约定俗成叫 self，改名也可以但强烈不推荐。")

# 2.2 构造函数
l4_2_2 = Lesson.objects.create(
    chapter=ch4_2, title="2.2 构造函数 __init__", order=2, lesson_type='code',
    code_challenge_prompt="# 定义 Student 类，初始化 name 和 age\nclass Student:\n    def __init__(self, name, age):\n        self.name = name\n        self.age = age\n\ns = Student('Tom', 12)\nprint(s.name)",
    content="""# 2.2 构造函数 __init__

## 1. 初始化对象
`__init__` 是一个特殊方法，在创建对象时**自动调用**。通常用来初始化属性。

```python
class Student:
    def __init__(self, name, age):
        self.name = name  # 属性
        self.age = age

s1 = Student("Alice", 12)
print(s1.name)
```

## 2. 属性
`self.name` 是对象的属性，每个对象都有自己独立的一份。
"""
)
Quiz.objects.create(lesson=l4_2_2, question="构造函数的名字是？", option_a="init", option_b="__init__", option_c="start", option_d="create", correct_answer="B", explanation="__init__。")
Quiz.objects.create(lesson=l4_2_2, question="__init__ 什么时候被调用？", option_a="类定义时", option_b="创建对象时", option_c="手动调用时", option_d="程序结束时", correct_answer="B", explanation="创建对象时自动调用。")
Quiz.objects.create(lesson=l4_2_2, question="self.age = age 的作用是？", option_a="定义局部变量", option_b="定义全局变量", option_c="定义对象属性", option_d="无作用", correct_answer="C", explanation="给对象绑定属性。")
Quiz.objects.create(lesson=l4_2_2, question="s = Student('Tom') 会调用？", option_a="Student.Tom()", option_b="__init__('Tom')", option_c="__init__(s, 'Tom')", option_d="start()", correct_answer="C", explanation="自动传入 self。")
Quiz.objects.create(lesson=l4_2_2, question="在类外部访问属性使用？", option_a=".", option_b="->", option_c="::", option_d="[]", correct_answer="A", explanation="点号。")
Quiz.objects.create(lesson=l4_2_2, question="判断题：__init__ 方法必须有返回值。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，不能有返回值（只能返回 None）。")
Quiz.objects.create(lesson=l4_2_2, question="判断题：不同对象的同名属性互不干扰。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")


# ==========================================
# Course 5: GESP 5级 - 算法基础
# ==========================================
print("正在创建 GESP 5级 课程...")
c5, _ = Course.objects.get_or_create(
    title="GESP 5级：算法基础",
    description="进入算法的世界。学习算法复杂度分析、基础排序算法（冒泡、选择、插入）和查找算法（二分查找），培养计算思维。",
    defaults={'order': 5}
)

ch5_1, _ = Chapter.objects.get_or_create(course=c5, title="第1章：算法复杂度", defaults={'order': 1})
l5_1_1 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l5_1_1, question="访问列表索引 a[i] 的时间复杂度？", option_a="O(1)", option_b="O(n)", option_c="O(log n)", option_d="O(n^2)", correct_answer="A", explanation="数组索引访问是常数时间。")
Quiz.objects.create(lesson=l5_1_1, question="单层 for 循环遍历 n 个元素的时间复杂度？", option_a="O(1)", option_b="O(n)", option_c="O(n^2)", option_d="O(log n)", correct_answer="B", explanation="线性时间。")
Quiz.objects.create(lesson=l5_1_1, question="双层嵌套循环通常是？", option_a="O(n)", option_b="O(n^2)", option_c="O(log n)", option_d="O(1)", correct_answer="B", explanation="平方级。")
Quiz.objects.create(lesson=l5_1_1, question="二分查找的复杂度？", option_a="O(n)", option_b="O(log n)", option_c="O(1)", option_d="O(n^2)", correct_answer="B", explanation="对数级。")
Quiz.objects.create(lesson=l5_1_1, question="Big O 表示的是算法的？", option_a="最好情况", option_b="最坏情况", option_c="平均情况", option_d="具体秒数", correct_answer="B", explanation="通常指最坏情况的上界。")
Quiz.objects.create(lesson=l5_1_1, question="判断题：O(1) 的算法一定比 O(n) 快。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，n 很小时不一定，但在 n 很大时 O(1) 更优。")
Quiz.objects.create(lesson=l5_1_1, question="判断题：空间复杂度是指代码文件的字节大小。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，是指运行时占用的内存。")

ch5_2, _ = Chapter.objects.get_or_create(course=c5, title="第2章：排序与查找", defaults={'order': 2})
l5_2_1 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l5_2_1, question="冒泡排序的时间复杂度？", option_a="O(n)", option_b="O(n^2)", option_c="O(n log n)", option_d="O(1)", correct_answer="B", explanation="双重循环。")
Quiz.objects.create(lesson=l5_2_1, question="冒泡排序是稳定的吗？", option_a="是", option_b="否", option_c="不确定", option_d="看情况", correct_answer="A", explanation="相等元素不交换，相对位置不变，所以稳定。")
Quiz.objects.create(lesson=l5_2_1, question="第一轮冒泡后，哪个位置的元素确定了？", option_a="第一个", option_b="最后一个", option_c="中间", option_d="无", correct_answer="B", explanation="最大的元素冒泡到最后。")
Quiz.objects.create(lesson=l5_2_1, question="最好情况（已经有序）的复杂度？", option_a="O(n)", option_b="O(n^2)", option_c="O(1)", option_d="O(log n)", correct_answer="A", explanation="如果加了优化标志位，可以是 O(n)。")
Quiz.objects.create(lesson=l5_2_1, question="交换两个变量 a, b 的 Python 写法？", option_a="a, b = b, a", option_b="swap(a, b)", option_c="a = b", option_d="b = a", correct_answer="A", explanation="元组解包。")
Quiz.objects.create(lesson=l5_2_1, question="判断题：冒泡排序是效率最高的排序算法。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，通常较慢。")
Quiz.objects.create(lesson=l5_2_1, question="判断题：冒泡排序需要额外的 O(n) 空间。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，原地排序 O(1)。")

l5_2_2 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l5_2_2, question="二分查找的前提条件？", option_a="数组无序", option_b="数组有序", option_c="数组必须全正数", option_d="数组长度为偶数", correct_answer="B", explanation="必须有序。")
Quiz.objects.create(lesson=l5_2_2, question="二分查找的时间复杂度？", option_a="O(n)", option_b="O(n^2)", option_c="O(log n)", option_d="O(1)", correct_answer="C", explanation="每次减半，对数级。")
Quiz.objects.create(lesson=l5_2_2, question="在 100 个有序数字中找，最多找几次？", option_a="100", option_b="50", option_c="7", option_d="10", correct_answer="C", explanation="log2(100) 约等于 6.6，向上取整 7。")
Quiz.objects.create(lesson=l5_2_2, question="mid 的计算公式？", option_a="(left+right)/2", option_b="(left+right)//2", option_c="left+right", option_d="right-left", correct_answer="B", explanation="整除。")
Quiz.objects.create(lesson=l5_2_2, question="如果 arr[mid] < target，说明？", option_a="在左边", option_b="在右边", option_c="找到了", option_d="不存在", correct_answer="B", explanation="目标比中间大，在右边。")
Quiz.objects.create(lesson=l5_2_2, question="判断题：二分查找可以用于链表。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，链表不支持随机访问，效率低。")
Quiz.objects.create(lesson=l5_2_2, question="判断题：线性查找比二分查找慢。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确（在数据量大时）。")


# ==========================================
# Course 6: GESP 6级 - 进阶数据结构与递归
# ==========================================
print("正在创建 GESP 6级 课程...")
c6, _ = Course.objects.get_or_create(
    title="GESP 6级：进阶数据结构与递归",
    description="挑战高阶编程概念。深入理解递归思想，掌握栈（Stack）和队列（Queue）的原理与实现，解决复杂逻辑问题。",
    defaults={'order': 6}
)

ch6_1, _ = Chapter.objects.get_or_create(course=c6, title="第1章：递归", defaults={'order': 1})
l6_1_1 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l6_1_1, question="递归函数必须包含？", option_a="循环", option_b="基准情况", option_c="全局变量", option_d="数组", correct_answer="B", explanation="否则会死循环（栈溢出）。")
Quiz.objects.create(lesson=l6_1_1, question="如果没有基准情况会怎样？", option_a="正常运行", option_b="返回 0", option_c="栈溢出 (RecursionError)", option_d="死机", correct_answer="C", explanation="无限递归导致栈溢出。")
Quiz.objects.create(lesson=l6_1_1, question="递归计算 3! 的调用顺序？", option_a="f(3)->f(2)->f(1)", option_b="f(1)->f(2)->f(3)", option_c="f(3)->f(3)", option_d="f(3)->f(1)", correct_answer="A", explanation="层层向下调用。")
Quiz.objects.create(lesson=l6_1_1, question="斐波那契数列适合用递归吗？", option_a="适合且高效", option_b="适合但低效", option_c="完全不适合", option_d="不能用", correct_answer="B", explanation="简单递归会有大量重复计算。")
Quiz.objects.create(lesson=l6_1_1, question="Python 默认递归深度限制？", option_a="100", option_b="1000", option_c="无限", option_d="10", correct_answer="B", explanation="通常是 1000。")
Quiz.objects.create(lesson=l6_1_1, question="判断题：所有递归都可以转化为循环。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确（理论上）。")
Quiz.objects.create(lesson=l6_1_1, question="判断题：递归通常比循环更节省内存。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，递归需要栈空间。")

ch6_2, _ = Chapter.objects.get_or_create(course=c6, title="第2章：栈与队列", defaults={'order': 2})
l6_2_1 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l6_2_1, question="栈的特点是？", option_a="先进先出", option_b="后进先出", option_c="随机进出", option_d="先进后出", correct_answer="B", explanation="LIFO。")
Quiz.objects.create(lesson=l6_2_1, question="进栈操作对应 Python 列表的？", option_a="insert", option_b="push", option_c="append", option_d="add", correct_answer="C", explanation="append。")
Quiz.objects.create(lesson=l6_2_1, question="出栈操作对应 Python 列表的？", option_a="delete", option_b="remove", option_c="pop", option_d="get", correct_answer="C", explanation="pop。")
Quiz.objects.create(lesson=l6_2_1, question="Stack: 进 1, 进 2, 出, 进 3, 出。剩下？", option_a="[1]", option_b="[2]", option_c="[3]", option_d="[]", correct_answer="A", explanation="进1,2->[1,2]; 出2->[1]; 进3->[1,3]; 出3->[1]。")
Quiz.objects.create(lesson=l6_2_1, question="函数调用栈使用的是哪种数据结构？", option_a="队列", option_b="栈", option_c="树", option_d="图", correct_answer="B", explanation="栈。")
Quiz.objects.create(lesson=l6_2_1, question="判断题：栈可以访问中间的元素。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，只能访问栈顶。")
Quiz.objects.create(lesson=l6_2_1, question="判断题：栈是线性结构。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确。")

l6_2_2 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l6_2_2, question="队列的特点是？", option_a="先进先出", option_b="后进先出", option_c="随机访问", option_d="无序", correct_answer="A", explanation="FIFO。")
Quiz.objects.create(lesson=l6_2_2, question="Python 中推荐用什么实现队列？", option_a="list", option_b="dict", option_c="deque", option_d="set", correct_answer="C", explanation="collections.deque。")
Quiz.objects.create(lesson=l6_2_2, question="deque 出队的方法是？", option_a="pop()", option_b="popleft()", option_c="remove()", option_d="delete()", correct_answer="B", explanation="popleft()。")
Quiz.objects.create(lesson=l6_2_2, question="Queue: 进 1, 进 2, 出, 进 3, 出。剩下？", option_a="[3]", option_b="[1]", option_c="[2]", option_d="[]", correct_answer="A", explanation="进1,2->[1,2]; 出1->[2]; 进3->[2,3]; 出2->[3]。")
Quiz.objects.create(lesson=l6_2_2, question="BFS（广度优先搜索）使用什么数据结构？", option_a="栈", option_b="队列", option_c="堆", option_d="树", correct_answer="B", explanation="队列。")
Quiz.objects.create(lesson=l6_2_2, question="判断题：列表的 pop(0) 操作是 O(1) 的。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，是 O(n)，因为要移动后续元素。")
Quiz.objects.create(lesson=l6_2_2, question="判断题：队列允许在两端插入和删除。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，那是双端队列（Deque），普通队列只能一端进一端出。")


# ==========================================
# Course 7: Head First Python (Structured)
# ==========================================
print("正在创建 Head First Python 课程 (Structured)...")
c7, _ = Course.objects.get_or_create(
    title="Head First Python",
    description="《Head First Python》经典教材改编。通过生动有趣的项目驱动学习，涵盖列表、模块、文件处理、异常处理等实用技能。",
    defaults={'order': 7}
)

# Chapter 1: The Basics
ch7_1, _ = Chapter.objects.get_or_create(course=c7, title="第1章：基础知识 (The Basics)", defaults={'order': 1})

# 1.1 Getting Started
l7_1_1 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l7_1_1, question="IDLE 的 Python Shell 主要用于？", option_a="编写大型项目", option_b="测试代码片段 (REPL)", option_c="浏览网页", option_d="画图", correct_answer="B", explanation="Shell 是 Read-Eval-Print-Loop 环境。")
Quiz.objects.create(lesson=l7_1_1, question="在 IDLE 中，>>> 提示符表示什么？", option_a="等待输入命令", option_b="程序正在运行", option_c="出现错误", option_d="注释", correct_answer="A", explanation="这是 Shell 等待用户输入的标志。")
Quiz.objects.create(lesson=l7_1_1, question="Head First 系列提倡的学习方式是？", option_a="死记硬背", option_b="大量阅读文字", option_c="图像化与实践驱动", option_d="只看视频", correct_answer="C", explanation="强调大脑友好的学习方式。")
Quiz.objects.create(lesson=l7_1_1, question="Python 源代码文件的扩展名通常是？", option_a=".python", option_b=".exe", option_c=".py", option_d=".txt", correct_answer="C", explanation="标准后缀是 .py。")
Quiz.objects.create(lesson=l7_1_1, question="如果 print('Hello') 漏掉了右括号，Python 会？", option_a="自动补全", option_b="报错 SyntaxError", option_c="忽略错误", option_d="打印 Hello", correct_answer="B", explanation="语法错误会导致程序无法运行。")
Quiz.objects.create(lesson=l7_1_1, question="判断题：IDLE 是 Python 官方自带的编辑器。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，随 Python 安装包一起提供。")
Quiz.objects.create(lesson=l7_1_1, question="判断题：print 是 Python 2 和 Python 3 中的关键字，用法完全一样。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，Python 3 中 print 是函数，必须加括号。")

# 1.2 A Meatier Example (odd.py)
l7_1_2 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l7_1_2, question="如何获取当前时间的分钟数？", option_a="datetime.minute()", option_b="datetime.today().minute", option_c="time.minute", option_d="clock.minute", correct_answer="B", explanation="使用 datetime.today() 获取当前时间对象。")
Quiz.objects.create(lesson=l7_1_2, question="time.sleep(5) 的作用是？", option_a="让程序加速运行", option_b="让程序暂停 5 秒", option_c="让程序暂停 5 分钟", option_d="关闭程序", correct_answer="B", explanation="暂停执行指定的秒数。")
Quiz.objects.create(lesson=l7_1_2, question="random.randint(1, 60) 可能生成的数包括？", option_a="1", option_b="60", option_c="1 和 60 都包括", option_d="都不包括", correct_answer="C", explanation="randint 是闭区间，包含两端的值。")
Quiz.objects.create(lesson=l7_1_2, question="range(5) 生成的序列是？", option_a="1, 2, 3, 4, 5", option_b="0, 1, 2, 3, 4", option_c="0, 1, 2, 3, 4, 5", option_d="1, 2, 3, 4", correct_answer="B", explanation="从 0 开始，包头不包尾。")
Quiz.objects.create(lesson=l7_1_2, question="在 if 语句中，判断相等应该使用？", option_a="=", option_b="==", option_c="is", option_d="equals", correct_answer="B", explanation="== 是比较运算符，= 是赋值。")
Quiz.objects.create(lesson=l7_1_2, question="判断题：datetime 模块需要 pip install 才能使用。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，它是 Python 标准库的一部分。")
Quiz.objects.create(lesson=l7_1_2, question="判断题：if 语句后面的代码块必须缩进。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，Python 依靠缩进来组织代码块。")

# Chapter 2: List Data
ch7_2, _ = Chapter.objects.get_or_create(course=c7, title="第2章：列表数据 (List Data)", defaults={'order': 2})

# 2.1 Creating Lists
l7_2_1 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l7_2_1, question="列表的索引是从几开始的？", option_a="1", option_b="0", option_c="-1", option_d="任意", correct_answer="B", explanation="Python 索引从 0 开始。")
Quiz.objects.create(lesson=l7_2_1, question="定义一个列表使用什么符号？", option_a="()", option_b="[]", option_c="{}", option_d="<>", correct_answer="B", explanation="方括号 []。")
Quiz.objects.create(lesson=l7_2_1, question="Python 变量在使用前需要声明类型吗？", option_a="需要", option_b="不需要", option_c="看情况", option_d="只能声明整数", correct_answer="B", explanation="Python 是动态类型语言，不需要声明类型。")
Quiz.objects.create(lesson=l7_2_1, question="movies = ['A', 'B', 'C']，movies[2] 是？", option_a="A", option_b="B", option_c="C", option_d="报错", correct_answer="C", explanation="索引 2 是第三个元素。")
Quiz.objects.create(lesson=l7_2_1, question="len(movies) 返回的是？", option_a="列表占用的内存", option_b="列表的元素个数", option_c="列表的最大索引", option_d="列表的名称", correct_answer="B", explanation="len() 返回长度。")
Quiz.objects.create(lesson=l7_2_1, question="判断题：列表中的元素必须是相同类型的。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，Python 列表可以包含混合类型的数据。")
Quiz.objects.create(lesson=l7_2_1, question="判断题：列表创建后，其大小不能改变。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，列表是动态的，可以随时增加或删除元素。")

# 2.2 List Methods
l7_2_2 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l7_2_2, question="pop() 方法默认删除哪个元素？", option_a="第一个", option_b="最后一个", option_c="随机一个", option_d="指定的一个", correct_answer="B", explanation="默认删除末尾元素。")
Quiz.objects.create(lesson=l7_2_2, question="在列表末尾添加一个元素，使用？", option_a="add", option_b="push", option_c="append", option_d="insert", correct_answer="C", explanation="append 方法。")
Quiz.objects.create(lesson=l7_2_2, question="remove('A') 的作用是？", option_a="删除索引为 A 的元素", option_b="删除所有值为 A 的元素", option_c="删除第一个值为 A 的元素", option_d="报错", correct_answer="C", explanation="只删除第一个匹配项。")
Quiz.objects.create(lesson=l7_2_2, question="extend 方法接收的参数通常是？", option_a="一个数字", option_b="一个字符串", option_c="另一个列表", option_d="无参数", correct_answer="C", explanation="用于合并两个列表。")
Quiz.objects.create(lesson=l7_2_2, question="insert(0, 'Start') 会将元素插入到？", option_a="列表末尾", option_b="列表开头", option_c="列表中间", option_d="替换第一个元素", correct_answer="B", explanation="索引 0 是开头。")
Quiz.objects.create(lesson=l7_2_2, question="判断题：pop() 方法不仅删除元素，还会返回被删除的元素。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，可以用来获取被弹出的值。")
Quiz.objects.create(lesson=l7_2_2, question="判断题：remove() 如果找不到元素会静默失败（什么都不做）。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，会抛出 ValueError。")

# 2.3 Nested Lists
l7_2_3 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l7_2_3, question="isinstance(x, list) 的作用是？", option_a="将 x 转为列表", option_b="判断 x 是否为列表", option_c="创建新列表", option_d="删除列表", correct_answer="B", explanation="类型检查。")
Quiz.objects.create(lesson=l7_2_3, question="对于嵌套列表 lst = [1, [2, 3]]，lst[1][0] 是？", option_a="1", option_b="2", option_c="3", option_d="[2, 3]", correct_answer="B", explanation="先取第二个元素 [2,3]，再取其第一个元素 2。")
Quiz.objects.create(lesson=l7_2_3, question="遍历列表通常使用哪种循环？", option_a="for", option_b="while", option_c="do-while", option_d="until", correct_answer="A", explanation="for loop 是遍历集合的首选。")
Quiz.objects.create(lesson=l7_2_3, question="如果列表层级很深（比如 10 层），手动写 for 循环嵌套会？", option_a="非常高效", option_b="非常痛苦且代码难看", option_c="自动优化", option_d="报错", correct_answer="B", explanation="深层嵌套难以维护，需要递归。")
Quiz.objects.create(lesson=l7_2_3, question="movies = ['A', ['B', 'C']]，len(movies) 是？", option_a="2", option_b="3", option_c="4", option_d="1", correct_answer="A", explanation="只有两个元素：字符串 'A' 和内部列表 ['B', 'C']。")
Quiz.objects.create(lesson=l7_2_3, question="判断题：Python 的列表可以嵌套任意层级。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，受限于内存，但逻辑上无限。")
Quiz.objects.create(lesson=l7_2_3, question="判断题：isinstance(3, list) 返回 True。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，3 是 int，不是 list。")


# Chapter 3: Structured Data
ch7_3, _ = Chapter.objects.get_or_create(course=c7, title="第3章：结构化数据 (Structured Data)", defaults={'order': 3})

# 3.1 Dictionaries
l7_3_1 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l7_3_1, question="字典使用什么符号定义？", option_a="[]", option_b="()", option_c="{}", option_d="<>", correct_answer="C", explanation="大括号 {}。")
Quiz.objects.create(lesson=l7_3_1, question="字典中访问数据使用的是？", option_a="索引 (0, 1...)", option_b="键 (Key)", option_c="值 (Value)", option_d="随机访问", correct_answer="B", explanation="通过 Key 查找 Value。")
Quiz.objects.create(lesson=l7_3_1, question="d = {'name': 'Tom'}，如何获取 'Tom'？", option_a="d[0]", option_b="d.Tom", option_c="d['name']", option_d="d('name')", correct_answer="C", explanation="使用方括号加键名。")
Quiz.objects.create(lesson=l7_3_1, question="字典的 Key 必须是？", option_a="唯一的", option_b="整数", option_c="字符串", option_d="可变的", correct_answer="A", explanation="键必须唯一且不可变（Hashable）。")
Quiz.objects.create(lesson=l7_3_1, question="列表和字典的主要区别是？", option_a="列表有序，字典无序（逻辑上）", option_b="列表用 {}，字典用 []", option_c="字典不能存数字", option_d="列表比字典慢", correct_answer="A", explanation="列表是序列，字典是映射。")
Quiz.objects.create(lesson=l7_3_1, question="判断题：字典中的 Value 可以是列表。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，Value 可以是任何对象。")
Quiz.objects.create(lesson=l7_3_1, question="判断题：两个不同的 Key 可以对应同一个 Value。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，如 {'a': 1, 'b': 1}。")

# Chapter 4: Code Reuse
ch7_4, _ = Chapter.objects.get_or_create(course=c7, title="第4章：代码复用 (Code Reuse)", defaults={'order': 4})

# 4.1 Functions
l7_4_1 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l7_4_1, question="DRY 原则的意思是？", option_a="Do Repeat Yourself", option_b="Don't Repeat Yourself", option_c="Do Right Yesterday", option_d="Data Ready Yet", correct_answer="B", explanation="不要重复造轮子。")
Quiz.objects.create(lesson=l7_4_1, question="Python 中定义函数使用哪个关键字？", option_a="function", option_b="def", option_c="func", option_d="define", correct_answer="B", explanation="def 是 define 的缩写。")
Quiz.objects.create(lesson=l7_4_1, question="递归函数是指？", option_a="调用其他函数的函数", option_b="调用自己的函数", option_c="没有返回值的函数", option_d="无限循环的函数", correct_answer="B", explanation="Self-calling function。")
Quiz.objects.create(lesson=l7_4_1, question="处理任意层级的嵌套列表，最适合的算法是？", option_a="多层 for 循环", option_b="递归", option_c="随机抽样", option_d="二分查找", correct_answer="B", explanation="递归可以自然适应任意深度。")
Quiz.objects.create(lesson=l7_4_1, question="函数参数 (Argument) 的作用是？", option_a="定义返回值", option_b="向函数传递数据", option_c="停止函数", option_d="定义函数名", correct_answer="B", explanation="传递输入数据。")
Quiz.objects.create(lesson=l7_4_1, question="判断题：Python 函数必须有 return 语句。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，没有 return 默认返回 None。")
Quiz.objects.create(lesson=l7_4_1, question="判断题：缩进在 Python 函数定义中非常重要。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，决定了函数体的范围。")

# 4.2 Modules
l7_4_2 = Lesson.objects.create(
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
"""
)
Quiz.objects.create(lesson=l7_4_2, question="导入模块的关键字是？", option_a="load", option_b="include", option_c="import", option_d="use", correct_answer="C", explanation="import。")
Quiz.objects.create(lesson=l7_4_2, question="如果模块名为 my_module，调用其中的 func 函数应该是？", option_a="func()", option_b="my_module.func()", option_c="call func from my_module", option_d="import func", correct_answer="B", explanation="需要使用模块名作为命名空间前缀。")
Quiz.objects.create(lesson=l7_4_2, question="Python 模块文件的后缀名必须是？", option_a=".txt", option_b=".java", option_c=".py", option_d=".exe", correct_answer="C", explanation="Python 源码文件。")
Quiz.objects.create(lesson=l7_4_2, question="PyPI 是什么？", option_a="Python 解释器", option_b="Python 包索引 (Package Index)", option_c="Python 编辑器", option_d="Python 教程", correct_answer="B", explanation="第三方库的仓库。")
Quiz.objects.create(lesson=l7_4_2, question="使用 from module import function 的好处是？", option_a="代码运行更快", option_b="可以直接使用函数名，不用加前缀", option_c="可以导入私有函数", option_d="没有区别", correct_answer="B", explanation="引入当前命名空间。")
Quiz.objects.create(lesson=l7_4_2, question="判断题：你自己写的 .py 文件也可以作为模块被导入。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="A", explanation="正确，只要在 Python 路径下。")
Quiz.objects.create(lesson=l7_4_2, question="判断题：一个模块只能包含一个函数。", option_a="正确", option_b="错误", option_c="", option_d="", correct_answer="B", explanation="错误，可以包含任意数量的函数、类和变量。")

print("所有课程创建完成！")
