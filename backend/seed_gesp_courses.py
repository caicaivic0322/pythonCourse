import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from courses.models import Course, Chapter, Lesson, Quiz

# 1. 清理旧数据
print("正在清理旧数据...")
Course.objects.all().delete()

# ==========================================
# Course 1: GESP 1级 - 编程启蒙
# ==========================================
c1, _ = Course.objects.get_or_create(
    title="GESP 1级：编程启蒙",
    description="Python 编程基础：变量、运算符与基本逻辑。",
    defaults={'order': 1}
)
print(f"创建课程: {c1.title}")

# Ch1: 初识 Python
ch1_1, _ = Chapter.objects.get_or_create(course=c1, title="第1章：初识 Python", defaults={'order': 1})
l1_1 = Lesson.objects.create(
    chapter=ch1_1, title="1.1 什么是 Python？", order=1, lesson_type='text',
    code_challenge_prompt="""# 1.1 什么是 Python - 代码验证题
# 题目：请使用 print() 函数输出 "Hello, GESP!"

# 你的代码:

# 验证提示：运行后，终端输出应为 Hello, GESP!
""",
    content="""
## 什么是 Python？
Python 是一种广泛使用的高级编程语言，以简洁、易读著称。

### 核心特性
1. **解释型**：代码逐行执行，无需像 C++ 那样先编译成机器码。
2. **动态类型**：变量在运行时确定类型，无需显式声明（如 `int a`）。
3. **强类型**：虽然不需要声明，但类型之间不会随意隐式转换（例如字符串和数字不能直接相加）。

### Python vs C++
| 特性 | C++ | Python |
| :--- | :--- | :--- |
| **运行方式** | 编译执行 (Compile) | 解释执行 (Interpret) |
| **代码块** | 大括号 `{}` | **缩进 (Indentation)** |
| **语句结尾** | 分号 `;` | 换行符 |
| **变量声明** | 必须声明类型 | 直接赋值 |

### 第一个程序
```python
print("Hello, World!")
```
"""
)
Quiz.objects.create(
    lesson=l1_1,
    question="Python 是一种什么类型的语言？",
    option_a="编译型语言",
    option_b="解释型语言",
    option_c="汇编语言",
    option_d="机器语言",
    correct_answer="B",
    explanation="Python 是解释型语言，代码逐行执行，不需要预先编译成机器码。"
)
Quiz.objects.create(
    lesson=l1_1,
    question="在 Python 中，如何表示代码块？",
    option_a="大括号 {}",
    option_b="begin 和 end",
    option_c="缩进 (Indentation)",
    option_d="分号 ;",
    correct_answer="C",
    explanation="Python 使用缩进（通常是4个空格）来划分代码块，这是 Python 的核心特色。"
)

l1_2 = Lesson.objects.create(
    chapter=ch1_1, title="1.2 变量与命名规则", order=2, lesson_type='text',
    code_challenge_prompt="""# 1.2 变量与命名规则 - 代码验证题
# 题目：定义一个变量 my_score 并赋值为 100，然后打印它。

# 你的代码:

# 验证提示：终端应输出 100
""",
    content="""
## 变量 (Variable)
变量是存储数据的容器。在 Python 中，变量更像是一个**标签**，贴在数据上。

### 命名规则 (标识符)
1. **组成**：只能包含**字母** (a-z, A-Z)、**数字** (0-9) 和**下划线** (_)。
2. **开头**：**不能以数字开头**。
   - ✅ `name1`, `_score`, `student_id`
   - ❌ `1name` (数字开头), `my-name` (包含连字符), `class` (关键字)
3. **大小写敏感**：`Score` 和 `score` 是两个不同的变量。
4. **关键字**：不能使用 Python 的保留字（如 `if`, `for`, `while`, `True` 等）。

### 命名习惯
- **蛇形命名法 (Snake Case)**：单词之间用下划线连接，全小写。这是 Python 推荐的变量和函数命名方式。
  - 例如：`student_score`, `max_value`
- **驼峰命名法 (Camel Case)**：第二个单词首字母大写。Python 中通常用于类名。
  - 例如：`StudentScore`

### 赋值
使用 `=` 进行赋值。
```python
x = 10
x = x + 5  # 现在 x 是 15
```
"""
)
Quiz.objects.create(
    lesson=l1_2,
    question="以下哪个是合法的 Python 变量名？",
    option_a="1st_place",
    option_b="my-name",
    option_c="_score",
    option_d="if",
    correct_answer="C",
    explanation="变量名不能以数字开头（排除A），不能包含连字符（排除B），不能是关键字（排除D）。_score 符合规则。"
)
Quiz.objects.create(
    lesson=l1_2,
    question="Python 中推荐使用什么命名风格来命名变量？",
    option_a="驼峰命名法 (myScore)",
    option_b="蛇形命名法 (my_score)",
    option_c="匈牙利命名法 (iScore)",
    option_d="帕斯卡命名法 (MyScore)",
    correct_answer="B",
    explanation="Python 官方 PEP 8 规范推荐使用蛇形命名法（全小写，下划线分隔）来命名变量和函数。"
)

l1_3 = Lesson.objects.create(
    chapter=ch1_1, title="1.3 基本数据类型", order=3, lesson_type='text',
    code_challenge_prompt="""# 1.3 基本数据类型 - 代码验证题
# 题目：将字符串 "123" 转换为整数，并加上 10，然后打印结果。

# 你的代码:

# 验证提示：终端应输出 133
""",
    content="""
## 基本数据类型详解
Python 中的变量可以存储不同类型的数据。

### 1. 整数 (int)
- **定义**：没有小数点的数字。
- **特性**：
    - **无大小限制**：只要内存允许，可以存储任意大的整数（如 `10**100`）。这是 Python 的一大优势。
    - **进制表示**：
        - 二进制：`0b` 开头，如 `0b1010` (10)
        - 八进制：`0o` 开头，如 `0o12` (10)
        - 十六进制：`0x` 开头，如 `0xA` (10)

### 2. 浮点数 (float)
- **定义**：带有小数点的数字。
- **特性**：
    - **科学计数法**：`1.23e9` 表示 $1.23 \\times 10^9$，`1.5e-3` 表示 $0.0015$。
    - **精度误差**：基于 IEEE 754 标准，存在浮点数精度问题。
    ```python
    print(0.1 + 0.2)  # 输出 0.30000000000000004
    ```

### 3. 字符串 (str)
- **定义**：文本数据。
- **引号**：单引号 `'` 和双引号 `"` 完全等价。三引号 `'''` 用于多行字符串。
- **不可变性**：字符串创建后不能修改。
- **转义字符**：
    - `\\n`: 换行
    - `\\t`: 制表符 (Tab)
    - `\\\\`: 反斜杠本身
    - `\\' / \\"`: 引号

### 4. 布尔值 (bool)
- **定义**：逻辑真假。
- **值**：`True` 和 `False` (**首字母大写**)。
- **本质**：是 `int` 的子类，`True == 1`, `False == 0`。

### 类型查询与转换
- `type(x)`: 查看 x 的类型。
- `int(x)`: 转为整数（截断小数部分）。
- `float(x)`: 转为浮点数。
- `str(x)`: 转为字符串。
"""
)
Quiz.objects.create(
    lesson=l1_3,
    question="type(10 / 2) 的结果是？",
    option_a="<class 'int'>",
    option_b="<class 'float'>",
    option_c="<class 'str'>",
    option_d="5",
    correct_answer="B",
    explanation="在 Python 3 中，除法运算符 / 总是返回浮点数 (float)，即使能整除。"
)
Quiz.objects.create(
    lesson=l1_3,
    question="以下哪个字符串表示包含一个双引号？",
    option_a="'\"'",
    option_b="\"\"\"",
    option_c="'",
    option_d="\"'\"",
    correct_answer="A",
    explanation="可以使用单引号包裹双引号 '\"'，或者使用转义字符 \"\\\"\"。"
)

# 1.4 输入与输出 (IO)
l1_4 = Lesson.objects.create(
    chapter=ch1_1, title="1.4 输入与输出 (IO)", order=4, lesson_type='code',
    content="""
## 输入与输出详解

### 输出：print()
函数原型：`print(*objects, sep=' ', end='\\n')`
1. **多个参数**：可以用逗号隔开，默认用空格连接。
   ```python
   print("Hello", "World")  # 输出: Hello World
   ```
2. **sep 参数**：指定分隔符。
   ```python
   print("2023", "10", "01", sep="-")  # 输出: 2023-10-01
   ```
3. **end 参数**：指定结尾符号，默认为换行符 `\\n`。
   ```python
   print("Hello", end=" ")
   print("World")
   # 输出: Hello World (在同一行)
   ```
4. **格式化输出 (f-string)**：推荐使用。
   ```python
   name = "Alice"
   age = 12
   print(f"我是 {name}，今年 {age} 岁")
   ```

### 输入：input()
函数原型：`input(prompt)`
1. **返回值**：永远是 **字符串 (str)** 类型。
2. **转换**：如果需要数字，必须手动转换。

```python
# 错误写法
# age = input("年龄: ")
# print(age + 1)  # 报错！字符串不能和数字相加

# 正确写法
age = int(input("年龄: "))
print(age + 1)
```

### 任务
输入两个整数，输出它们的乘积。
"""
)
Quiz.objects.create(
    lesson=l1_4,
    question="执行代码 `print(1, 2, 3, sep='-')` 的输出结果是？",
    option_a="1 2 3",
    option_b="1-2-3",
    option_c="1,2,3",
    option_d="123",
    correct_answer="B",
    explanation="sep 参数指定了多个打印对象之间的分隔符，这里是短横线 '-'。"
)
Quiz.objects.create(
    lesson=l1_4,
    question="关于 input() 函数，以下说法正确的是？",
    option_a="它可以直接读取整数类型",
    option_b="它总是返回字符串类型",
    option_c="它不能接受提示信息作为参数",
    option_d="它只能在 Windows 系统下使用",
    correct_answer="B",
    explanation="input() 函数读取用户输入的内容，并始终将其作为字符串返回。如果需要数字，必须使用 int() 或 float() 转换。"
)

# Ch2: 运算符与表达式
ch1_2, _ = Chapter.objects.get_or_create(course=c1, title="第2章：运算符与表达式", defaults={'order': 2})
l2_1 = Lesson.objects.create(
    chapter=ch1_2, title="2.1 算术运算符", order=1, lesson_type='text',
    content="""
## 算术运算符
| 符号 | 描述 | 示例 | 结果 | 注意 |
| :--- | :--- | :--- | :--- | :--- |
| `+` | 加法 | `3 + 5` | `8` | |
| `-` | 减法 | `5 - 3` | `2` | |
| `*` | 乘法 | `3 * 5` | `15` | |
| `/` | **真除法** | `5 / 2` | `2.5` | 结果总是 float |
| `//` | **整除** | `5 // 2` | `2` | 向下取整 |
| `%` | 取模 (余数) | `5 % 2` | `1` | |
| `**` | 幂运算 | `2 ** 3` | `8` | $2^3$ |

### 重点：整除与取模
- **整除 `//`**：向下取整（往小了取）。
  - `5 // 2` -> `2`
  - `-5 // 2` -> `-3` (注意！C++ 可能是 -2)
- **取模 `%`**：
  - `5 % 2` -> `1`
  - `-5 % 2` -> `1` (Python 中余数的符号与除数一致)

### 复合赋值
`+=`, `-=`, `*=`, `/=`, `//=`, `%=`
- `a += 1` 等价于 `a = a + 1`
- **注意**：Python 没有 `++` 或 `--` 运算符！
"""
)
Quiz.objects.create(
    lesson=l2_1,
    question="表达式 `5 // 2` 的结果是？",
    option_a="2.5",
    option_b="2",
    option_c="3",
    option_d="2.0",
    correct_answer="B",
    explanation="// 是整除运算符，向下取整，5 除以 2 等于 2.5，向下取整为 2。"
)
Quiz.objects.create(
    lesson=l2_1,
    question="表达式 `2 ** 3` 的结果是？",
    option_a="5",
    option_b="6",
    option_c="8",
    option_d="9",
    correct_answer="C",
    explanation="** 是幂运算符，表示 2 的 3 次方，即 2 * 2 * 2 = 8。"
)

l2_2 = Lesson.objects.create(
    chapter=ch1_2, title="2.2 比较与逻辑运算符", order=2, lesson_type='code',
    content="""
## 比较运算符
结果为 `True` 或 `False`。
- `==`, `!=`, `>`, `<`, `>=`, `<=`
- **链式比较**：Python 支持数学写法！
  ```python
  x = 5
  if 1 < x < 10:  # 等价于 1 < x and x < 10
      print("在范围内")
  ```

## 逻辑运算符
| 符号 | 描述 | C++ 对应 | 特性 |
| :--- | :--- | :--- | :--- |
| `and` | 与 | `&&` | 全真才真 |
| `or` | 或 | `||` | 一真即真 |
| `not` | 非 | `!` | 真变假，假变真 |

### 短路求值 (Short-circuit)
- `a and b`：如果 a 为假，直接返回 a，不计算 b。
- `a or b`：如果 a 为真，直接返回 a，不计算 b。

```python
# 安全的除法检查
b = 0
if b != 0 and (10 / b) > 1:  # 如果 b 是 0，前半部分为假，后半部分不会执行，避免报错
    print("Result")
```

### 任务
判断一个年份是否为闰年：(能被4整除 且 不能被100整除) 或 (能被400整除)。
"""
)
Quiz.objects.create(
    lesson=l2_2,
    question="以下哪个表达式的结果为 True？",
    option_a="True and False",
    option_b="not True",
    option_c="False or True",
    option_d="3 > 5",
    correct_answer="C",
    explanation="False or True 的结果是 True，因为 or 运算符只要有一个为真，结果就为真。"
)
Quiz.objects.create(
    lesson=l2_2,
    question="在 Python 中，逻辑运算符 '与' 是？",
    option_a="&",
    option_b="&&",
    option_c="and",
    option_d="with",
    correct_answer="C",
    explanation="Python 使用单词 'and' 作为逻辑与运算符，而不是符号 &&。"
)

l2_3 = Lesson.objects.create(
    chapter=ch1_2, title="2.3 运算符优先级", order=3, lesson_type='text',
    content="""
## 运算符优先级 (从高到低)
了解优先级可以避免逻辑错误。如果不确定，**加括号 ()** 是最好的习惯。

1. `**` (幂运算，最高)
2. `+`, `-` (正负号)
3. `*`, `/`, `//`, `%`
4. `+`, `-` (加减)
5. `==`, `!=`, `>`, `<`, ... (比较)
6. `not`
7. `and`
8. `or` (最低)

```python
print(2 + 3 * 4)    # 14 (先乘)
print((2 + 3) * 4)  # 20 (先加)
print(not True or True) # True (先 not 得到 False，再 or)
```
"""
)
Quiz.objects.create(
    lesson=l2_3,
    question="表达式 `2 + 3 * 4` 的计算结果是？",
    option_a="20",
    option_b="14",
    option_c="24",
    option_d="10",
    correct_answer="B",
    explanation="乘法优先级高于加法，先算 3*4=12，再算 2+12=14。"
)

# Ch3: 决策与分支
ch1_3, _ = Chapter.objects.get_or_create(course=c1, title="第3章：决策与分支", defaults={'order': 3})
l3_1 = Lesson.objects.create(
    chapter=ch1_3, title="3.1 分支结构详解", order=1, lesson_type='code',
    content="""
## 分支结构
控制程序根据条件执行不同的代码块。

### 语法结构
```python
if 条件1:
    代码块1
elif 条件2:
    代码块2
else:
    代码块3
```

### 关键点
1. **冒号**：每个条件行末尾必须有 `:`。
2. **缩进**：代码块必须缩进（推荐 4 空格）。Python 依靠缩进来区分代码块。
3. **pass 语句**：如果代码块为空（还没想好写什么），必须写 `pass` 占位，否则报错。

```python
if score > 60:
    pass  # 待办
```

### 任务
编写一个程序，输入一个整数：
- 如果是正数，输出 "Positive"
- 如果是负数，输出 "Negative"
- 如果是零，输出 "Zero"
"""
)
Quiz.objects.create(
    lesson=l3_1,
    question="Python 中 if 语句的代码块是如何划分的？",
    option_a="使用大括号 {}",
    option_b="使用缩进",
    option_c="使用 begin 和 end",
    option_d="使用圆括号 ()",
    correct_answer="B",
    explanation="Python 强制使用缩进来表示代码块的层级关系。"
)
Quiz.objects.create(
    lesson=l3_1,
    question="如果 if 语句后面没有代码需要执行，应该使用什么关键字占位？",
    option_a="null",
    option_b="void",
    option_c="pass",
    option_d="empty",
    correct_answer="C",
    explanation="pass 是 Python 的空语句，用于占位，防止语法错误。"
)


# ==========================================
# Course 2: GESP 2级 - 逻辑进阶
# ==========================================
c2, _ = Course.objects.get_or_create(
    title="GESP 2级：逻辑进阶",
    description="循环结构、列表数组与字符串操作。",
    defaults={'order': 2}
)
print(f"创建课程: {c2.title}")

# Ch1: 循环结构
ch2_1, _ = Chapter.objects.get_or_create(course=c2, title="第1章：循环结构", defaults={'order': 1})
Lesson.objects.create(
    chapter=ch2_1, title="1.1 range() 与 For 循环", order=1, lesson_type='text',
    content="""
## range() 函数详解
`range` 生成一个整数序列，左闭右开 `[start, stop)`。

1. `range(stop)`: 从 0 开始，到 stop-1。
   - `range(5)` -> 0, 1, 2, 3, 4
2. `range(start, stop)`: 从 start 开始，到 stop-1。
   - `range(2, 5)` -> 2, 3, 4
3. `range(start, stop, step)`: 步长为 step。
   - `range(1, 10, 2)` -> 1, 3, 5, 7, 9
   - **倒序**：step 为负数。
   - `range(5, 0, -1)` -> 5, 4, 3, 2, 1

## For 循环
遍历序列中的每个元素。
```python
for i in range(1, 11):
    print(i, end=" ")
```
"""
)

Lesson.objects.create(
    chapter=ch2_1, title="1.2 While 循环与死循环", order=2, lesson_type='code',
    content="""
## While 循环
当条件为真时，重复执行。

```python
n = 1
while n <= 5:
    print(n)
    n += 1  # 别忘了更新条件！
```

### 死循环 (Infinite Loop)
如果条件永远为真，循环将无法停止。
```python
while True:
    print("停不下来了！")
    break  # 除非有 break
```

### 任务
使用 while 循环，计算从 1 加到 100 的和。
"""
)

Lesson.objects.create(
    chapter=ch2_1, title="1.3 循环控制 (Break/Continue/Else)", order=3, lesson_type='text',
    content="""
## 循环控制语句

### break
立即**终止**当前循环，跳出循环体。
```python
for i in range(10):
    if i == 5:
        break  # 到 5 就结束了
    print(i)
```

### continue
**跳过**本次循环的剩余部分，直接进入下一次循环（条件判断）。
```python
for i in range(5):
    if i == 2:
        continue  # 跳过 2
    print(i)
```

### else 子句 (特有)
当循环**正常结束**（没有被 break 打断）时执行。
```python
for i in range(5):
    if i == 10:
        break
else:
    print("没有找到 10，循环正常结束")
```
"""
)

Lesson.objects.create(
    chapter=ch2_1, title="1.4 循环嵌套实战", order=4, lesson_type='code',
    content="""
## 循环嵌套
外层循环每执行一次，内层循环就执行一整轮。
常用于处理二维数组、打印图形等。

### 打印九九乘法表
```python
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j}", end="\\t")
    print()  # 换行
```

### 任务
打印倒直角三角形：
*****
****
***
**
*
"""
)

# Ch2: 列表 (List)
ch2_2, _ = Chapter.objects.get_or_create(course=c2, title="第2章：列表 (List)", defaults={'order': 2})
Lesson.objects.create(
    chapter=ch2_2, title="2.1 列表基础与索引", order=1, lesson_type='text',
    content="""
## 列表 (List)
Python 的列表是一个有序、可变、异构（可存不同类型）的序列。

### 创建
```python
a = [1, 2, 3]
b = list(range(5))  # [0, 1, 2, 3, 4]
```

### 索引 (Indexing)
- **正向索引**：从 0 开始。
- **负向索引**：从 -1 开始（表示最后一个）。
```python
lst = [10, 20, 30, 40]
print(lst[0])   # 10
print(lst[-1])  # 40
print(lst[-2])  # 30
```
"""
)

Lesson.objects.create(
    chapter=ch2_2, title="2.2 列表切片 (Slicing)", order=2, lesson_type='text',
    content="""
## 列表切片
一次性获取列表的一部分。
语法：`list[start:stop:step]`
- **特性**：切片操作会返回一个新的列表（浅拷贝）。

### 常见用法
```python
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(nums[2:5])   # [2, 3, 4] (不含 5)
print(nums[:3])    # [0, 1, 2] (从头开始)
print(nums[5:])    # [5, 6, 7, 8, 9] (直到末尾)
print(nums[::2])   # [0, 2, 4, 6, 8] (每隔一个)
print(nums[::-1])  # [9, 8, ..., 0] (列表反转)
```
"""
)

Lesson.objects.create(
    chapter=ch2_2, title="2.3 列表的增删改查", order=3, lesson_type='code',
    content="""
## 列表常用方法

### 增加
- `append(x)`: 末尾追加。
- `insert(i, x)`: 指定位置插入。
- `extend(iterable)`: 拼接另一个列表。

### 删除
- `pop(i)`: 删除并返回索引 i 处的元素（默认最后一个）。
- `remove(x)`: 删除第一个值为 x 的元素（找不到报错）。
- `clear()`: 清空列表。
- `del lst[i]`: 删除指定位置。

### 查找与统计
- `index(x)`: 查找 x 的索引。
- `count(x)`: 统计 x 出现的次数。
- `x in lst`: 判断 x 是否在列表中 (True/False)。

### 排序
- `sort()`: 原地排序（修改原列表）。
- `reverse()`: 原地反转。

### 任务
创建一个列表 `[3, 1, 4, 1, 5, 9]`，删除所有的 `1`，然后降序排列。
"""
)

# Ch3: 字符串操作
ch2_3, _ = Chapter.objects.get_or_create(course=c2, title="第3章：字符串操作", defaults={'order': 3})
Lesson.objects.create(
    chapter=ch2_3, title="3.1 字符串与编码", order=1, lesson_type='text',
    content="""
## 字符串基础
字符串是**不可变**序列。支持索引和切片操作。

### ASCII 码 (GESP 考点)
计算机内部使用数字存储字符。
- `ord(char)`: 字符 -> ASCII 码。
- `chr(code)`: ASCII 码 -> 字符。

```python
print(ord('A'))  # 65
print(ord('a'))  # 97
print(chr(66))   # 'B'
```
记住：`'a'` 比 `'A'` 大 32。
"""
)

Lesson.objects.create(
    chapter=ch2_3, title="3.2 字符串常用方法", order=2, lesson_type='code',
    content="""
## 常用方法
由于字符串不可变，这些方法都会**返回新字符串**，不会修改原字符串。

### 大小写
- `upper()`: 全大写。
- `lower()`: 全小写。
- `capitalize()`: 首字母大写。

### 查找与替换
- `find(sub)`: 返回子串第一次出现的索引，找不到返回 -1。
- `replace(old, new)`: 替换。
- `count(sub)`: 统计次数。

### 清理与分割
- `strip()`: 去除首尾空白字符（空格、换行）。
- `split(sep)`: 按分隔符切割成**列表**。
- `join(iterable)`: 将列表元素连接成字符串。

```python
s = "  Python,C++,Java  "
clean = s.strip()
langs = clean.split(",")  # ['Python', 'C++', 'Java']
res = "-".join(langs)     # "Python-C++-Java"
```

### 任务
输入一行英文句子，统计其中单词的个数（假设单词间用空格分隔）。
"""
)


# ==========================================
# Course 3: GESP 3级 - 算法初探
# ==========================================
c3, _ = Course.objects.get_or_create(
    title="GESP 3级：算法初探",
    description="函数、元组字典与基础算法。",
    defaults={'order': 3}
)
print(f"创建课程: {c3.title}")

# Ch1: 函数
ch3_1, _ = Chapter.objects.get_or_create(course=c3, title="第1章：函数", defaults={'order': 1})
Lesson.objects.create(
    chapter=ch3_1, title="1.1 函数基础", order=1, lesson_type='text',
    content="""
## 函数 (Function)
函数是组织好的、可重复使用的代码块。

### 定义与调用
```python
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")
```

### 返回值
使用 `return` 语句。如果没有 return，默认返回 `None`。
可以返回多个值（本质是返回一个元组）。
```python
def get_point():
    return 10, 20

x, y = get_point()  # 解包
```
"""
)

Lesson.objects.create(
    chapter=ch3_1, title="1.2 参数传递详解", order=2, lesson_type='text',
    content="""
## 参数类型

1. **位置参数**：按顺序传。
2. **关键字参数**：指定参数名，顺序无关。
   ```python
   func(a=1, b=2)
   ```
3. **默认参数**：定义时给参数默认值。
   ```python
   def power(x, n=2):  # n 默认为 2
       return x ** n
   ```
   **警告**：默认参数必须放在非默认参数后面。且默认参数最好指向**不可变对象**（不要用列表做默认参数）。

### 可变参数 (选学)
- `*args`: 接收任意个位置参数（元组）。
- `**kwargs`: 接收任意个关键字参数（字典）。
"""
)

Lesson.objects.create(
    chapter=ch3_1, title="1.3 变量作用域 (Scope)", order=3, lesson_type='text',
    content="""
## 作用域 (LEGB 规则)
变量查找顺序：Local(局部) -> Enclosing -> Global(全局) -> Built-in(内置)。

### Global 关键字
在函数内部修改全局变量。
```python
cnt = 0
def add():
    global cnt
    cnt += 1
```

如果不加 `global`，函数内对 `cnt = 1` 只是创建了一个新的局部变量，不会影响外部。
"""
)

# Ch2: 高级数据结构
ch3_2, _ = Chapter.objects.get_or_create(course=c3, title="第2章：高级数据结构", defaults={'order': 2})
Lesson.objects.create(
    chapter=ch3_2, title="2.1 元组 (Tuple)", order=1, lesson_type='text',
    content="""
## 元组
不可变的列表。使用 `()`。
如果元组只有一个元素，必须加逗号：`(1,)`。

### 打包与解包
```python
t = 1, 2, 3  # 打包
a, b, c = t  # 解包
```

### 交换变量
Python 特有的语法糖：
```python
a, b = b, a
```
"""
)

Lesson.objects.create(
    chapter=ch3_2, title="2.2 字典 (Dict)", order=2, lesson_type='code',
    content="""
## 字典
键值对 (Key-Value) 映射。
- **Key**：必须是**不可变**类型（int, str, tuple）。不能是列表！
- **Value**：任意类型。

### 增删改查
```python
d = {"a": 1, "b": 2}
val = d.get("a", 0)  # 安全获取，不存在返回 0
d["c"] = 3           # 新增/修改
d.pop("a")           # 删除
```

### 遍历
```python
for k in d:          # 遍历键
for v in d.values(): # 遍历值
for k, v in d.items(): # 遍历键值对
```

### 任务
统计字符串中每个字符出现的次数，存入字典。
"""
)

Lesson.objects.create(
    chapter=ch3_2, title="2.3 集合 (Set)", order=3, lesson_type='text',
    content="""
## 集合 (Set)
无序、不重复的元素集合。使用 `{}`。

### 特性
1. **自动去重**：`set([1, 2, 2, 3])` -> `{1, 2, 3}`。
2. **成员检测**：`x in s` 速度极快（哈希查找）。

### 集合运算
- `&`: 交集
- `|`: 并集
- `-`: 差集
"""
)

# Ch3: 基础算法
ch3_3, _ = Chapter.objects.get_or_create(course=c3, title="第3章：基础算法", defaults={'order': 3})
Lesson.objects.create(
    chapter=ch3_3, title="3.1 枚举算法", order=1, lesson_type='code',
    content="""
## 枚举 (Brute Force)
暴力穷举所有可能性。

### 经典案例：百钱百鸡
公鸡 5 文，母鸡 3 文，小鸡 3 只 1 文。用 100 文买 100 只鸡。
```python
# x:公鸡, y:母鸡, z:小鸡
for x in range(21):
    for y in range(34):
        z = 100 - x - y
        if z % 3 == 0 and 5*x + 3*y + z//3 == 100:
            print(x, y, z)
```
"""
)

Lesson.objects.create(
    chapter=ch3_3, title="3.2 排序算法", order=2, lesson_type='code',
    content="""
## 排序
Python 内置了强大的排序功能。

### list.sort()
原地排序。
```python
a = [3, 1, 2]
a.sort(reverse=True)  # 降序
```

### sorted()
返回新列表，原列表不变。
```python
b = sorted(a)
```

### 自定义排序 (Key)
按绝对值排序：
```python
a = [-5, 1, -2]
a.sort(key=abs)  # [1, -2, -5]
```

### 任务
有一组学生信息 `[("Alice", 80), ("Bob", 90), ("Charlie", 70)]`，请按成绩从高到低排序。
"""
)


# ==========================================
# Course 4: GESP 4级 - 系统构建
# ==========================================
c4, _ = Course.objects.get_or_create(
    title="GESP 4级：系统构建",
    description="面向对象编程、异常处理与文件操作。",
    defaults={'order': 4}
)
print(f"创建课程: {c4.title}")

# Ch1: 面向对象
ch4_1, _ = Chapter.objects.get_or_create(course=c4, title="第1章：面向对象 (OOP)", defaults={'order': 1})
Lesson.objects.create(
    chapter=ch4_1, title="1.1 类与对象", order=1, lesson_type='text',
    content="""
## 类与对象
Python 一切皆对象。

### 定义
```python
class Cat:
    # 类属性
    species = "Mammal"

    # 构造函数
    def __init__(self, name):
        self.name = name  # 实例属性

    # 方法
    def meow(self):
        print(f"{self.name} says Meow!")
```

### self 是什么？
`self` 代表**实例本身**。在调用方法时 `c.meow()`，Python 会自动把 `c` 传给 `self`。
"""
)

Lesson.objects.create(
    chapter=ch4_1, title="1.2 继承与多态", order=2, lesson_type='code',
    content="""
## 继承
子类继承父类的属性和方法。
```python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):  # 重写 (Override)
        print("Woof!")

d = Dog()
d.speak()  # Woof!
```

### super()
调用父类的方法。
```python
class SuperDog(Dog):
    def speak(self):
        super().speak()
        print("And I can fly!")
```
"""
)

# Ch2: 异常处理
ch4_2, _ = Chapter.objects.get_or_create(course=c4, title="第2章：异常处理", defaults={'order': 2})
Lesson.objects.create(
    chapter=ch4_2, title="2.1 异常捕获机制", order=1, lesson_type='code',
    content="""
## 完整结构
```python
try:
    # 可能出错的代码
    f = open("file.txt")
    val = int(f.read())
except FileNotFoundError:
    print("文件没找到")
except ValueError:
    print("内容不是数字")
except Exception as e:
    print(f"未知错误: {e}")
else:
    print("一切正常执行这里")
finally:
    f.close()
    print("无论如何都会执行（用于清理资源）")
```

### 任务
编写一个除法计算器，处理除零异常和输入非数字异常。
"""
)

# Ch3: 文件操作
ch4_3, _ = Chapter.objects.get_or_create(course=c4, title="第3章：文件操作", defaults={'order': 3})
Lesson.objects.create(
    chapter=ch4_3, title="3.1 文件读写详解", order=1, lesson_type='text',
    content="""
## 文件操作

### 打开模式
- `'r'`: 只读（默认）。文件不存在报错。
- `'w'`: 写入。文件存在则**清空**，不存在则创建。
- `'a'`: 追加。
- `'b'`: 二进制模式（如 `'rb'`, `'wb'`），用于图片、音频。

### with 语句 (上下文管理器)
自动关闭文件，防止资源泄露。
```python
with open("data.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()  # 读取所有行到列表
```
"""
)

Lesson.objects.create(
    chapter=ch4_3, title="3.2 CSV 与 JSON", order=2, lesson_type='code',
    content="""
## CSV 处理
```python
import csv
with open('scores.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Math'])
    writer.writerow(['Alice', 100])
```

## JSON 处理 (常用)
```python
import json
data = {"name": "Bob", "age": 15}
json_str = json.dumps(data)  # 转为字符串
obj = json.loads(json_str)   # 转回对象
```

### 任务
读取一个 CSV 文件，计算某列的平均值。
"""
)

print("GESP 1-4 级课程数据填充完成！")

# ==========================================
# Course 5: Head First Python 实战
# ==========================================
c5, _ = Course.objects.get_or_create(
    title="Python 实战：Web 开发入门",
    description="基于《Head First Python》经典案例，从零开始构建一个完整的 Web 应用程序。Learning by Doing！",
    defaults={'order': 5}
)
print(f"创建课程: {c5.title}")

# Ch1: 核心逻辑与数据结构
ch5_1, _ = Chapter.objects.get_or_create(course=c5, title="第1章：构建核心业务逻辑", defaults={'order': 1})
l5_1_1 = Lesson.objects.create(
    chapter=ch5_1, title="1.1 列表与复杂数据处理", order=1, lesson_type='code',
    code_challenge_prompt="""# 1.1 列表处理 - 代码验证题
# 题目：给定一个包含混合数据的列表 vowels = ['a', 'e', 'i', 'o', 'u']
# 请编写代码，接收用户输入的一个单词，统计该单词中出现了哪些元音字母，并打印出来（去重）。

word = input("Provide a word to search for vowels: ")
found = []
# 你的代码:

""",
    content="""
## 从列表开始 (The Basics)
我们的目标是构建一个 Web 应用，但首先需要有“业务逻辑”。
假设我们要为一个“元音字母搜索服务”编写核心代码。

### 任务
1. 接收用户输入。
2. 检查输入中有哪些元音字母 ('a', 'e', 'i', 'o', 'u')。
3. 输出结果。

### 知识点回顾
- `input()`: 获取输入。
- `in` 操作符: 检查元素是否存在。
- `append()`: 添加到列表。
"""
)
Quiz.objects.create(
    lesson=l5_1_1,
    question="如果列表 a = [1, 2]，执行 a.append(3) 后，a 的值是？",
    option_a="[1, 2]",
    option_b="[1, 2, 3]",
    option_c="[3, 1, 2]",
    option_d="报错",
    correct_answer="B",
    explanation="append() 方法会将元素添加到列表的末尾。"
)

l5_1_2 = Lesson.objects.create(
    chapter=ch5_1, title="1.2 字典与高效查找", order=2, lesson_type='code',
    code_challenge_prompt="""# 1.2 字典优化 - 代码验证题
# 题目：这次不仅要找出元音，还要统计每个元音出现的次数。
# 请使用字典 (dict) 来存储结果。

word = input("Provide a word to search for vowels: ")
found = {}
# 你的代码:

""",
    content="""
## 使用结构化数据 (Structured Data)
列表虽然好用，但如果我们想知道“每个元音出现了几次”，列表就显得笨拙了。
这时候，**字典 (Dictionary)** 登场了。

### 字典的优势
- **键值对**：`{'a': 3, 'e': 1}` 直观地表示数据。
- **查找快**：哈希表实现，速度飞快。
- **setdefault()**: 一个非常有用的方法，避免 Key Error。

```python
found = {}
if 'a' in found:
    found['a'] += 1
else:
    found['a'] = 1
# 等价于
found.setdefault('a', 0)
found['a'] += 1
```
"""
)
Quiz.objects.create(
    lesson=l5_1_2,
    question="对于字典 d = {'a': 1}，执行 d['b'] 会发生什么？",
    option_a="返回 None",
    option_b="返回 0",
    option_c="抛出 KeyError",
    option_d="自动创建 'b': None",
    correct_answer="C",
    explanation="访问不存在的键会抛出 KeyError。应使用 d.get('b') 或 d.setdefault('b', 0) 来安全访问。"
)

# Ch2: 模块化与复用
ch5_2, _ = Chapter.objects.get_or_create(course=c5, title="第2章：模块化与代码复用", defaults={'order': 2})
l5_2_1 = Lesson.objects.create(
    chapter=ch5_2, title="2.1 编写函数", order=1, lesson_type='code',
    code_challenge_prompt="""# 2.1 函数封装 - 代码验证题
# 题目：将之前的逻辑封装成一个函数 search4vowels(phrase: str) -> dict
# 并调用它测试 "hitch-hiker"。

def search4vowels(phrase: str) -> dict:
    # 你的代码:
    return {}

# 测试调用
print(search4vowels("hitch-hiker"))
""",
    content="""
## 代码复用 (Code Reuse)
我们已经写好了逻辑，但如果想在另一个程序里用它怎么办？复制粘贴吗？
No！我们需要**函数 (Functions)**。

### 函数三要素
1. **函数名**：见名知意 (`search4vowels`)。
2. **参数**：输入数据 (`phrase`)。
3. **返回值**：输出结果 (`dict`)。

### 类型注解 (Type Hints)
Python 3.5+ 支持类型注解，让代码更易读。
```python
def search4vowels(phrase: str) -> dict:
    ...
```
"""
)

l5_2_2 = Lesson.objects.create(
    chapter=ch5_2, title="2.2 创建模块", order=2, lesson_type='text',
    content="""
## 模块 (Modules)
函数多了，文件会变得很长。我们可以把函数放到单独的文件中，这就是**模块**。

### 怎么做？
1. 创建一个 `vsearch.py` 文件。
2. 把 `search4vowels` 函数剪切进去。
3. 在主程序中 `import vsearch`。

### 命名空间
使用模块名作为前缀，避免命名冲突。
```python
import vsearch
vsearch.search4vowels("test")
```
"""
)
Quiz.objects.create(
    lesson=l5_2_2,
    question="如果在模块 mymod.py 中定义了函数 func，导入后如何调用？",
    option_a="func()",
    option_b="mymod.func()",
    option_c="call func from mymod",
    option_d="mymod->func()",
    correct_answer="B",
    explanation="默认 import 导入模块对象，需要通过 模块名.函数名 的方式调用。"
)

# Ch3: 构建 Web 应用
ch5_3, _ = Chapter.objects.get_or_create(course=c5, title="第3章：构建 Web 应用 (Flask)", defaults={'order': 3})
l5_3_1 = Lesson.objects.create(
    chapter=ch5_3, title="3.1 Hello Flask", order=1, lesson_type='text',
    content="""
## 构建 Web 应用 (Building a Webapp)
现在我们有了核心逻辑模块 `vsearch`，是时候把它放到互联网上了！
我们将使用 **Flask** —— 一个轻量级、Pythonic 的 Web 框架。

### 最小的 Flask 应用
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

app.run()
```

### 装饰器 (Decorators)
`@app.route('/')` 是一个装饰器。它告诉 Flask：当用户访问根网址 `/` 时，执行下面的 `hello` 函数，并把返回值显示在浏览器上。
"""
)
Quiz.objects.create(
    lesson=l5_3_1,
    question="在 Flask 中，@app.route('/') 的作用是？",
    option_a="定义一个类",
    option_b="导入路由模块",
    option_c="将 URL 路径映射到 Python 函数",
    option_d="启动服务器",
    correct_answer="C",
    explanation="装饰器 @app.route 将特定的 URL 规则绑定到视图函数上。"
)

l5_3_2 = Lesson.objects.create(
    chapter=ch5_3, title="3.2 处理 Web 请求", order=2, lesson_type='code',
    code_challenge_prompt="""# 3.2 模拟 Web 请求处理 - 代码验证题
# 题目：编写一个函数 do_search(request_data)，模拟 Flask 的视图函数。
# request_data 是一个字典，包含用户提交的 'phrase' 和 'letters'。
# 函数应调用之前的 search4letters 逻辑（假设已存在），返回结果字符串。

def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    return set(letters).intersection(set(phrase))

def do_search(request_data: dict) -> str:
    # 你的代码: 从 request_data 获取 phrase 和 letters
    # 调用 search4letters
    # 返回格式化字符串，例如 "Results: {'a', 'e'}"
    return ""
    
# 测试
print(do_search({'phrase': 'life is short', 'letters': 'aeiou'}))
""",
    content="""
## 接入真实逻辑
Web 应用的核心是：**接收请求 -> 处理数据 -> 返回响应**。

### 在 Flask 中
通常使用 `request` 对象来获取表单数据。
```python
from flask import request

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = str(search4letters(phrase, letters))
    return render_template('results.html', the_results=results)
```

由于我们在浏览器中无法运行完整的 Flask 服务，上方的代码挑战通过模拟 `request_data` 字典来练习这一逻辑。
"""
)

# Ch4: 数据持久化
ch5_4, _ = Chapter.objects.get_or_create(course=c5, title="第4章：数据持久化", defaults={'order': 4})
l5_4_1 = Lesson.objects.create(
    chapter=ch5_4, title="4.1 文件读写与日志", order=1, lesson_type='code',
    code_challenge_prompt="""# 4.1 写入日志 - 代码验证题
# 题目：编写 log_request(req: dict, res: str) 函数。
# 将请求和结果写入到 'vsearch.log' 文件中，格式自定义（例如一行一条）。

def log_request(req: dict, res: str):
    # 你的代码: 打开文件，写入内容，关闭文件
    pass

# 测试
log_request({'phrase': 'test'}, "{'e'}")
with open('vsearch.log') as f:
    print(f.read())
""",
    content="""
## 存储数据 (Storing Data)
Web 应用运行起来了，但我们想知道谁用了它，搜了什么。我们需要**日志 (Log)**。

### 简单文件操作
```python
log = open('vsearch.log', 'a')  # 'a' for append
print("Someone searched something!", file=log)
log.close()
```

### 更好的方式：with 语句
自动处理文件关闭，即使发生错误。
```python
with open('vsearch.log', 'a') as log:
    print("Log message", file=log)
```
"""
)
Quiz.objects.create(
    lesson=l5_4_1,
    question="使用 open(filename, 'a') 打开文件的作用是？",
    option_a="读取文件",
    option_b="覆盖写入文件",
    option_c="在文件末尾追加内容",
    option_d="以二进制模式打开",
    correct_answer="C",
    explanation="'a' 代表 append（追加）模式，新写入的内容会添加到文件末尾，而不会清空原有内容。"
)

print("Course 5 (Head First Python) 填充完成！")
