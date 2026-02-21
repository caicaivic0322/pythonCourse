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
    description="掌握结构化编程。学习函数的定义、参数传递（位置/关键字/默认参数）、作用域（局部/全局变量），以及 Python 模块的导入与使用。",
    defaults={'order': 3}
)

ch3_1, _ = Chapter.objects.get_or_create(course=c3, title="第1章：函数 Functions", defaults={'order': 1})

# 1.1 函数基础
l3_1_1 = Lesson.objects.create(
    chapter=ch3_1, title="1.1 函数定义与返回值", order=1, lesson_type='text',
    code_challenge_prompt="# 定义一个函数 add(a, b)，返回两个数的和\ndef add(a, b):\n    return a + b\n\nprint(add(3, 5))",
    content="""# 1.1 函数定义与返回值

## 1. 为什么需要函数？
避免重复代码，把特定的功能封装起来。就像我们用 `print()` 一样，我们也可以造自己的工具。

## 2. 定义函数
使用 `def` 关键字。
```python
def say_hello():
    print("Hello!")

# 调用函数
say_hello()
```

## 3. 参数 (Parameters)
函数可以接收数据。
```python
def greet(name):
    print(f"Hello, {name}")

greet("Alice") # 实参
```

## 4. 返回值 (Return)
函数不仅可以打印，还可以**把结果还给调用者**。这是函数最强大的地方。
```python
def square(x):
    return x * x

result = square(5) # result 变成了 25
print(result + 10) # 35
```
**注意**：函数执行到 `return` 会立刻结束。如果没写 `return`，默认返回 `None`。
"""
)

# 5 MCQs + 2 T/F
# MCQ 1
Quiz.objects.create(
    lesson=l3_1_1,
    question="如果不写 return 语句，函数默认返回什么？",
    option_a="0",
    option_b="False",
    option_c="None",
    option_d="空字符串",
    correct_answer="C",
    explanation="Python 函数默认返回 None。"
)
# MCQ 2
Quiz.objects.create(
    lesson=l3_1_1,
    question="定义函数使用哪个关键字？",
    option_a="function",
    option_b="def",
    option_c="func",
    option_d="define",
    correct_answer="B",
    explanation="Python 使用 def 关键字定义函数。"
)
# MCQ 3
Quiz.objects.create(
    lesson=l3_1_1,
    question="def foo(): return 1\nprint(foo()) 输出什么？",
    option_a="foo",
    option_b="1",
    option_c="None",
    option_d="报错",
    correct_answer="B",
    explanation="函数返回 1，print 打印返回值。"
)
# MCQ 4
Quiz.objects.create(
    lesson=l3_1_1,
    question="下列关于函数参数说法正确的是？",
    option_a="函数必须有参数",
    option_b="函数可以没有参数",
    option_c="参数必须是整数",
    option_d="参数数量有限制",
    correct_answer="B",
    explanation="函数可以定义为不需要任何参数。"
)
# MCQ 5
Quiz.objects.create(
    lesson=l3_1_1,
    question="return 语句的作用是？",
    option_a="打印结果",
    option_b="结束函数并返回值",
    option_c="暂停函数",
    option_d="定义变量",
    correct_answer="B",
    explanation="return 用于结束函数执行并将结果返回给调用者。"
)
# T/F 1
Quiz.objects.create(
    lesson=l3_1_1,
    question="判断题：一个函数可以写多个 return 语句。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，函数可以有多个 return，但只会执行其中一个。"
)
# T/F 2
Quiz.objects.create(
    lesson=l3_1_1,
    question="判断题：函数必须有返回值，否则会报错。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，没有 return 的函数也是合法的，默认返回 None。"
)


# 1.2 变量作用域
l3_1_2 = Lesson.objects.create(
    chapter=ch3_1, title="1.2 局部变量与全局变量", order=2, lesson_type='text',
    code_challenge_prompt="# 观察局部变量\nx = 10\ndef change():\n    x = 20\n    print(f'内部: {x}')\nchange()\nprint(f'外部: {x}')",
    content="""# 1.2 局部变量与全局变量

## 1. 局部变量 (Local)
在函数**内部**定义的变量。
- **作用范围**：只在函数内部有效。
- 函数运行完，局部变量就会被销毁。

```python
def func():
    a = 10  # 局部变量
    print(a)

func()
# print(a)  # ❌ 报错！外面看不到 a
```

## 2. 全局变量 (Global)
在函数**外部**定义的变量。
- **作用范围**：整个程序都可以读取。

```python
x = 100 # 全局变量

def func():
    print(x) # ✅ 可以读取

func()
```

## 3. global 关键字
如果要在函数内部**修改**全局变量，必须先声明 `global`。
```python
score = 0

def add_score():
    global score  # 声明我要修改外面的 score
    score += 10

add_score()
print(score) # 10
```
如果不加 `global`，Python 会认为你是在创建一个新的同名局部变量，不会影响外面的。
"""
)

# 5 MCQs + 2 T/F
# MCQ 1
Quiz.objects.create(
    lesson=l3_1_2,
    question="如何在函数内部修改全局变量 x？",
    option_a="直接 x = 10",
    option_b="global x; x = 10",
    option_c="extern x; x = 10",
    option_d="public x; x = 10",
    correct_answer="B",
    explanation="使用 global 关键字声明全局变量。"
)
# MCQ 2
Quiz.objects.create(
    lesson=l3_1_2,
    question="x = 1\ndef func():\n    x = 2\n    print(x)\nfunc()\nprint(x)\n输出什么？",
    option_a="2 2",
    option_b="2 1",
    option_c="1 1",
    option_d="1 2",
    correct_answer="B",
    explanation="函数内部的 x 是局部变量，不会影响全局 x。函数内打印 2，函数外打印 1。"
)
# MCQ 3
Quiz.objects.create(
    lesson=l3_1_2,
    question="局部变量的作用域是？",
    option_a="整个程序",
    option_b="函数内部",
    option_c="类内部",
    option_d="文件内部",
    correct_answer="B",
    explanation="局部变量只在定义它的函数内部有效。"
)
# MCQ 4
Quiz.objects.create(
    lesson=l3_1_2,
    question="def func():\n    y = 5\nprint(y) 会发生什么？",
    option_a="输出 5",
    option_b="输出 None",
    option_c="报错",
    option_d="输出 0",
    correct_answer="C",
    explanation="y 是局部变量，在函数外部无法访问，会报 NameError。"
)
# MCQ 5
Quiz.objects.create(
    lesson=l3_1_2,
    question="关于 global 关键字，说法正确的是？",
    option_a="用于定义局部变量",
    option_b="用于在函数内部声明全局变量",
    option_c="用于导入模块",
    option_d="用于定义类",
    correct_answer="B",
    explanation="global 用于在函数内部指示变量引用的是全局变量。"
)
# T/F 1
Quiz.objects.create(
    lesson=l3_1_2,
    question="判断题：在函数内部可以直接读取全局变量的值。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，读取全局变量不需要 global 关键字。"
)
# T/F 2
Quiz.objects.create(
    lesson=l3_1_2,
    question="判断题：局部变量和全局变量不能重名。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，可以重名，此时函数内部会优先使用局部变量（遮蔽）。"
)


# ==========================================
# Course 4: GESP 4级 - 数据结构
# ==========================================
print("正在创建 GESP 4级 课程...")
c4, _ = Course.objects.get_or_create(
    title="GESP 4级：数据结构",
    description="学习更复杂的数据结构。重点掌握字典（Dictionary）的键值对操作、集合（Set）的去重特性、元组（Tuple）的不可变性，以及面向对象（Class）的初步概念。",
    defaults={'order': 4}
)

ch4_1, _ = Chapter.objects.get_or_create(course=c4, title="第1章：字典与集合", defaults={'order': 1})

# 1.1 字典
l4_1_1 = Lesson.objects.create(
    chapter=ch4_1, title="1.1 字典 Dictionary", order=1, lesson_type='text',
    code_challenge_prompt="# 创建字典并访问\nd = {'name': 'Tom', 'age': 18}\nprint(d['name'])",
    content="""# 1.1 字典 Dictionary

## 1. 什么是字典？
列表用数字索引（0, 1, 2...），字典用**键 (Key)** 来索引。
它像一本真的字典，通过“单词”（键）找到“解释”（值）。
结构：`{key: value, key: value}`

```python
student = {
    "name": "Alice",
    "age": 12,
    "score": 98
}
```

## 2. 操作字典
- **访问**：`d[key]`
  ```python
  print(student["name"]) # Alice
  ```
- **添加/修改**：`d[key] = new_value`
  ```python
  student["age"] = 13    # 修改
  student["city"] = "Beijing" # 新增
  ```
- **删除**：`d.pop(key)`
  ```python
  student.pop("score")
  ```

## 3. 遍历字典
```python
# 遍历键
for k in student.keys():
    print(k)

# 遍历值
for v in student.values():
    print(v)

# 遍历键值对
for k, v in student.items():
    print(k, v)
```

## 4. 特性
- 键必须是**不可变**的（通常是字符串或数字，列表不能做键）。
- 键是唯一的，不能重复。
"""
)

# 5 MCQs + 2 T/F
# MCQ 1
Quiz.objects.create(
    lesson=l4_1_1,
    question="d = {'a': 1, 'b': 2}，执行 d['c'] = 3 后，d 是？",
    option_a="{'a': 1, 'b': 2}",
    option_b="{'a': 1, 'b': 2, 'c': 3}",
    option_c="报错",
    option_d="{'c': 3}",
    correct_answer="B",
    explanation="给不存在的键赋值会自动添加该键值对。"
)
# MCQ 2
Quiz.objects.create(
    lesson=l4_1_1,
    question="d = {'a': 1, 'b': 2}，执行 d['a'] = 10 后，d 是？",
    option_a="{'a': 1, 'b': 2, 'a': 10}",
    option_b="{'a': 10, 'b': 2}",
    option_c="报错",
    option_d="{'b': 2}",
    correct_answer="B",
    explanation="键是唯一的，赋值给已存在的键会更新对应的值。"
)
# MCQ 3
Quiz.objects.create(
    lesson=l4_1_1,
    question="如何安全地获取字典的值，如果键不存在不报错？",
    option_a="d[key]",
    option_b="d.get(key)",
    option_c="d.value(key)",
    option_d="d.find(key)",
    correct_answer="B",
    explanation="get() 方法在键不存在时返回 None，而不会报错。"
)
# MCQ 4
Quiz.objects.create(
    lesson=l4_1_1,
    question="下列哪个可以作为字典的键？",
    option_a="[1, 2]",
    option_b="{'a': 1}",
    option_c="'name'",
    option_d="[1]",
    correct_answer="C",
    explanation="字典的键必须是不可变类型，字符串是不可变的，列表是可变的。"
)
# MCQ 5
Quiz.objects.create(
    lesson=l4_1_1,
    question="d.keys() 返回的是什么？",
    option_a="所有值",
    option_b="所有键",
    option_c="键值对",
    option_d="字典长度",
    correct_answer="B",
    explanation="keys() 返回字典中所有的键。"
)
# T/F 1
Quiz.objects.create(
    lesson=l4_1_1,
    question="判断题：字典中的键值对是有序的（Python 3.7+）。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="A",
    explanation="正确，Python 3.7+ 字典保持插入顺序。"
)
# T/F 2
Quiz.objects.create(
    lesson=l4_1_1,
    question="判断题：同一个字典中可以有两个相同的键。",
    option_a="正确",
    option_b="错误",
    option_c="",
    option_d="",
    correct_answer="B",
    explanation="错误，字典的键必须唯一。"
)


# ==========================================
# Course 5: Head First Python
# ==========================================
print("正在创建 Head First Python 课程...")
c5, _ = Course.objects.get_or_create(
    title="Head First Python",
    description="《Head First Python》经典教材改编。通过生动有趣的项目驱动学习，涵盖列表、模块、文件处理、异常处理等实用技能。",
    defaults={'order': 5}
)

ch5_1, _ = Chapter.objects.get_or_create(course=c5, title="第1章：初识 Python", defaults={'order': 1})
hf1 = Lesson.objects.create(
    chapter=ch5_1, title="1.1 Python 的不同之处", order=1, lesson_type='text',
    code_challenge_prompt="print('Hello Head First Python')",
    content="""# 1.1 Python 的不同之处

## 1. 为什么叫 Head First？
Head First 系列图书主张“通过图像、故事和练习”来激活你的大脑，而不是枯燥的列出语法规则。

## 2. 列表 - 你的第一个数据结构
Python 的列表极其强大，它不只是数组。
```python
movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
```

## 3. 嵌套列表
列表里面还可以放列表！
```python
list_in_list = ["Item 1", ["Sub Item 1", "Sub Item 2"]]
print(list_in_list[1][0]) # 输出 "Sub Item 1"
```
这种结构可以用来处理复杂的树形数据。
"""
)
Quiz.objects.create(
    lesson=hf1,
    question="访问嵌套列表 nums = [1, [2, 3]] 中的 3，应该用？",
    option_a="nums[1]",
    option_b="nums[1][1]",
    option_c="nums[2][2]",
    option_d="nums[0][1]",
    correct_answer="B",
    explanation="先取 nums[1] 得到 [2, 3]，再取 [1] 得到 3。"
)

ch5_2, _ = Chapter.objects.get_or_create(course=c5, title="第2章：模块与函数", defaults={'order': 2})
hf2 = Lesson.objects.create(
    chapter=ch5_2, title="2.1 模块化编程", order=1, lesson_type='text',
    code_challenge_prompt="import math\nprint(math.sqrt(16))",
    content="""# 2.1 模块化编程

## 1. 什么是模块？
当代码越来越多，我们需要把它拆分到不同的文件里。每个 `.py` 文件就是一个模块。

## 2. 导入模块
Python 标准库提供了“电池内置”的功能。
```python
import random
print(random.randint(1, 10)) # 生成 1-10 随机数
```

## 3. PyPI (Python Package Index)
Python 的强大之处在于第三方库。你可以通过 `pip install` 安装成千上万的库。
"""
)
Quiz.objects.create(
    lesson=hf2,
    question="使用哪个关键字导入模块？",
    option_a="include",
    option_b="using",
    option_c="import",
    option_d="require",
    correct_answer="C",
    explanation="import 是 Python 的导入关键字。"
)

print("所有课程创建完成！")
