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

# 1.1 什么是 Python？
l1_1 = Lesson.objects.create(
    chapter=ch1_1, title="1.1 什么是 Python？", order=1, lesson_type='text',
    code_challenge_prompt="""# 1.1 什么是 Python - 代码验证题
# 题目：请使用 print() 函数输出 "Hello, GESP!"

# 你的代码:

# 验证提示：运行后，终端输出应为 Hello, GESP!
""",
    content='''
## 什么是 Python？
Python 是一种广泛使用的高级编程语言，以**简洁、易读**著称。它的创造者是荷兰程序员 Guido van Rossum，名字来源于喜剧团体 Monty Python。

### 🎯 学习目标
- 了解 Python 的核心特性
- 理解解释型语言 vs 编译型语言的区别
- 掌握 Python 的基本语法特点

### 1️⃣ Python 的核心特性

#### 🔹 解释型语言
代码**逐行执行**，不需要像 C++ 那样先编译成机器码。
```python
# Python 代码（人类可读）
print("Hello")

# 机器码（010101...）
# 0010101010101010101010...
```

#### 🔹 动态类型
变量在**运行时**确定类型，无需显式声明。
```python
# Python：直接赋值，类型自动推断
x = 10          # 自动识别为 int
name = "Alice"   # 自动识别为 str
```

#### 🔹 强类型
虽然不需要声明，但类型之间**不会随意隐式转换**。
```python
# ❌ 错误示例
# "Hello" + 5  # TypeError: can only concatenate str

# ✅ 正确做法
"Hello" + str(5)  # "Hello5"
int("5") + 5      # 10
```

### 2️⃣ Python vs 其他语言对比

| 特性 | C++ | Java | Python |
| :--- | :--- | :--- | :--- |
| **运行方式** | 编译执行 | 编译+解释 | 解释执行 |
| **代码块** | 大括号 `{}` | 大括号 `{}` | **缩进** |
| **语句结尾** | 分号 `;` | 分号 `;` | 换行符 |
| **变量声明** | 必须声明类型 | 必须声明类型 | 直接赋值 |

### 3️⃣ 第一个 Python 程序
```python
print("Hello, World!")
```
**代码解析：**
- `print()` 是 Python 的内置函数
- `"Hello, World!"` 是字符串（用引号包裹）
- 括号 `()` 表示调用函数

### 4️⃣ 动手试一试
尝试修改下面的代码，输出你想要的文字：
```python
print("你好，世界！")
print("我在学习 Python")
```

### 📝 本节小结
- Python 是一种**解释型**高级语言
- 使用**缩进**划分代码块（这是 Python 的标志特色！）
- 代码简洁易读，适合初学者入门
'''
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
Quiz.objects.create(
    lesson=l1_1,
    question="以下哪个不是 Python 的特性？",
    option_a="动态类型",
    option_b="强类型",
    option_c="必须使用大括号",
    option_d="解释执行",
    correct_answer="C",
    explanation="Python 使用缩进而非大括号来划分代码块，这是它区别于 C++ 和 Java 的重要特点。"
)

# 1.2 变量与命名规则
l1_2 = Lesson.objects.create(
    chapter=ch1_1, title="1.2 变量与命名规则", order=2, lesson_type='text',
    code_challenge_prompt="""# 1.2 变量与命名规则 - 代码验证题
# 题目：定义一个变量 my_score 并赋值为 100，然后打印它。

# 你的代码:

# 验证提示：终端应输出 100
""",
    content='''
## 🎯 本节目标
- 理解变量的概念
- 掌握 Python 标识符的命名规则
- 养成良好的命名习惯

## 1️⃣ 什么是变量？

变量是存储数据的**容器**。在 Python 中，变量更像是一个**标签**，贴在数据上。

### 📦 直观理解
```python
# 创建一个名为 "score" 的盒子，放入数字 100
score = 100

# 创建一个名为 "name" 的盒子，放入文字 "Alice"
name = "Alice"

# 变量可以重新赋值（盒子里的东西可以换）
score = 200  # 原来的 100 被替换掉了
```

### 🔍 查看变量
```python
x = 10
print(x)       # 输出: 10
print(type(x)) # 输出: <class 'int'>
```

## 2️⃣ 标识符命名规则

**标识符**：变量、函数、类等的名字

### ✅ 合法的标识符
1. **字符组成**：只能包含：
   - 字母 (a-z, A-Z)
   - 数字 (0-9)
   - 下划线 (_)

2. **开头限制**：**不能以数字开头**
   ```python
   ✅ 合法:  name1, _score, student_id, total123
   ❌ 非法:  1name, 2fast, 3D
   ```

3. **大小写敏感**
   ```python
   score = 100
   Score = 200
   SCORE = 300
   # 这三个是完全不同的变量！
   ```

4. **不能使用关键字**
   ```python
   # ❌ 以下是 Python 保留的关键字，不能用作变量名
   if, else, for, while, class, def, return, 
   True, False, None, import, from, as, try, except
   ```

### ⚠️ 常见错误
```python
# ❌ 错误示例
my-name = "Alice"   # 原因：包含连字符 "-"
class = "Python"    # 原因：class 是关键字
1st = 100          # 原因：数字开头
```

## 3️⃣ 命名习惯（重要！）

### 🐍 蛇形命名法 (Snake Case) - 推荐用于变量和函数
```python
# 变量
student_name = "Alice"
max_score = 100
is_active = True

# 函数
def get_user_name():
    return "Alice"

def calculate_total_price():
    return 100
```

### 🐫 驼峰命名法 (Camel Case) - 推荐用于类名
```python
class StudentName:  # 类名首字母大写
    pass

class ShoppingCart:
    pass
```

### 📝 帕斯卡命名法 (Pascal Case)
```python
# 每个单词首字母都大写
FirstName = "Alice"
LastName = "Smith"
```

## 4️⃣ 变量赋值详解

### 🔄 基本赋值
```python
x = 10          # 整型
y = 3.14        # 浮点型
name = "Python"  # 字符串
is_learn = True  # 布尔值
```

### 🔄 链式赋值
```python
# 多个变量同时赋同一个值
a = b = c = 0

# 多个变量同时赋不同值
x, y, z = 1, 2, 3
```

### 🔄 交换变量
```python
a = 1
b = 2

# Python 特有的写法，无需临时变量
a, b = b, a

print(a, b)  # 输出: 2 1
```

## 5️⃣ 进阶：变量本质

在 Python 中，一切皆对象。变量实际上是指向对象的引用。
```python
a = [1, 2, 3]  # 创建列表对象，[1,2,3]
b = a           # b 也指向同一个列表对象

b.append(4)     # 通过 b 修改
print(a)        # a 也变了！输出: [1, 2, 3, 4]
print(b)        # 输出: [1, 2, 3, 4]
```

### 📋 验证变量 ID
```python
a = "hello"
b = "hello"
print(id(a) == id(b))  # 可能 True（Python 会优化字符串）

a = [1, 2]
b = [1, 2]
print(id(a) == id(b))  # False（列表是新对象）
```

## 6️⃣ 动手练习
```python
# 练习1：创建变量并打印
name = "你的名字"
age = 18
print(f"我叫{name}，今年{age}岁")

# 练习2：交换变量
x = 5
y = 10
# 尝试交换 x 和 y 的值
```
'''
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
Quiz.objects.create(
    lesson=l1_2,
    question="执行 a, b = 1, 2 后，a 和 b 的值分别是？",
    option_a="a=1, b=1",
    option_b="a=1, b=2",
    option_c="a=2, b=1",
    option_d="a=2, b=2",
    correct_answer="B",
    explanation="Python 支持多元赋值，a, b = 1, 2 会将 1 赋给 a，2 赋给 b。"
)

# 1.3 基本数据类型
# l1_3 = Lesson.objects.create(
#     chapter=ch1_1, title="1.3 基本数据类型", order=3, lesson_type='text',
#     code_challenge_prompt="""# 1.3 基本数据类型 - 代码验证题
# # 题目：将字符串 '123' 转换为整数，并加上 10，然后打印结果。
# 
# # 你的代码:
# 
# # 验证提示：终端应输出 133
# """,
#     content='''
# ## 🎯 本节目标
# - 掌握 Python 的四种基本数据类型
# - 学会类型之间的相互转换
# - 理解不同数据类型的特性和适用场景
# 
# ---
# 
# ## 1️⃣ 整数 (int) - Integer
# 
# **定义**：没有小数点的数字
# 
# ### 🔹 特性
# 1. **无大小限制**（只要内存允许）
# ```python
# very_big = 10 ** 100  # 10 的 100 次方
# print(very_big)        # 仍然是精确的大整数
# ```
# 
# 2. **支持多种进制表示**
# ```python
# # 十进制（默认）
# a = 42
# 
# # 二进制（0b 开头）
# b = 0b101010  # 对应十进制 42
# 
# # 八进制（0o 开头）
# c = 0o52      # 对应十进制 42
# 
# # 十六进制（0x 开头）
# d = 0x2a      # 对应十进制 42
# 
# print(a, b, c, d)  # 42 42 42 42
# ```
# 
# ### 🔹 进制转换
# ```python
# n = 42
# print(bin(n))   # 二进制: 0b101010
# print(oct(n))   # 八进制: 0o52
# print(hex(n))   # 十六进制: 0x2a
# ```
# 
# ---
# 
# ## 2️⃣ 浮点数 (float) - Floating Point
# 
# **定义**：带有小数点的数字
# 
# ### 🔹 特性
# 1. **科学计数法**
# ```python
# 1.23e9   # 1.23 × 10^9 = 1230000000
# 1.5e-3   # 1.5 × 10^-3 = 0.0015
# ```
# 
# 2. **精度问题（重要！）**
# ```python
# # 由于 IEEE 754 浮点数标准，会有精度误差
# print(0.1 + 0.2)   # 0.30000000000000004
# 
# # 解决方案：使用 decimal 模块
# from decimal import Decimal
# print(Decimal('0.1') + Decimal('0.2'))  # 0.3
# ```
# 
# ### 🔹 特殊浮点数
# ```python
# print(float('inf'))    # 正无穷: inf
# print(float('-inf'))   # 负无穷: -inf
# print(float('nan'))    # 非数字: nan
# ```
# 
# ---
# 
# ## 3️⃣ 字符串 (str) - String
# 
# **定义**：文本数据，用引号包裹
# 
# ### 🔹 引号的使用
# ```python
# # 单引号、双引号完全等价
# 'Hello' == "Hello"  # True
# 
# # 三引号：多行字符串
# text = '''这是
# 多行
# 字符串'''
# 
# # 也可以用三双引号
# text = ''''这也是
# 多行字符串'''
# ```
# 
# ### 🔹 字符串不可变
# ```python
# s = "hello"
# # s[0] = 'H'  # ❌ 错误：字符串不可修改
# 
# # 正确做法：创建新字符串
# s = "Hello"  # 重新赋值
# s = "H" + s[1:]  # 通过拼接创建新字符串
# ```
# 
# ### 🔹 转义字符
# | 转义字符 | 说明 |
# | :--- | :--- |
# | `\\n` | 换行 |
# | `\\t` | 制表符 (Tab) |
# | `\\\\` | 反斜杠 |
# | `\\'` | 单引号 |
# | `\\"` | 双引号 |
# 
# ```python
# print("Hello\\nWorld")  # Hello(换行)World
# print("Tab:\\there")    # Tab:	here
# print("\\\\")           # \\
# ```
# 
# ### 🔹 字符串常用操作
# ```python
# s = "Python"
# 
# # 长度
# len(s)           # 6
# 
# # 索引
# s[0]             # 'P'
# s[-1]            # 'n'
# 
# # 切片
# s[0:3]           # 'Pyt'
# s[::2]           # 'Pto' (每隔一个)
# s[::-1]          # 'nohtyP' (反转)
# ```
# 
# ---
# 
# ## 4️⃣ 布尔值 (bool) - Boolean
# 
# **定义**：表示真/假的逻辑值
# 
# ### 🔹 只有两个值
# ```python
# is_active = True
# is_deleted = False
# ```
# 
# ### 🔹 重要特性
# 在 Python 中，`True` 等于整数 `1`，`False` 等于整数 `0`：
# ```python
# print(True + True)    # 2
# print(True * 10)      # 10
# print(False == 0)     # True
# ```
# 
# ### 🔹 布尔转换
# ```python
# # 下列值会被判定为 False（称为"假值"）
# bool(0)        # False
# bool(0.0)      # False
# bool("")       # False (空字符串)
# bool([])       # False (空列表)
# bool(None)     # False
# 
# # 其余大多为 True
# bool(1)        # True
# bool("False")   # True (非空字符串)
# bool([0])       # True (非空列表)
# ```
# 
# ---
# 
# ## 5️⃣ 类型转换
# 
# ### 🔹 常用转换函数
# ```python
# # 字符串 -> 整数
# int("123")           # 123
# int("1010", 2)       # 10 (二进制转十进制)
# 
# # 字符串 -> 浮点数
# float("3.14")        # 3.14
# int("3.14")          # 3 (截断小数)
# 
# # 整数/浮点数 -> 字符串
# str(123)             # "123"
# str(3.14)            # "3.14"
# 
# # 整数 -> 浮点数
# float(10)            # 10.0
# ```
# 
# ### 🔹 四舍五入
# ```python
# round(3.7)          # 4
# round(3.14159, 2)    # 3.14 (保留2位小数)
# ```
# 
# ---
# 
# ## 6️⃣ type() 函数
# 
# ```python
# x = 10
# y = "hello"
# z = True
# 
# print(type(x))   # <class 'int'>
# print(type(y))   # <class 'str'>
# print(type(z))   # <class 'bool'>
# 
# # 在判断时使用
# if type(x) == int:
#     print("x 是整数")
# ```
# 
# ---
# 
# ## 📝 动手练习
# ```python
# # 练习1：类型转换
# num_str = "123"
# # 将 num_str 转换为整数并加 10
# 
# # 练习2：进制转换
# # 将十进制数 255 转换为二进制和十六进制
# 
# # 练习3：布尔运算
# # 验证 True + True + True 的结果
# ```
# '''
# )
# Quiz.objects.create(
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
    option_a="'\\\"'",
    option_b="''''''",
    option_c="'",
    option_d="'\\\"'",
    correct_answer="A",
    explanation="可以使用单引号包裹双引号 '\\\"'，或者使用转义字符。"
)
Quiz.objects.create(
    lesson=l1_3,
    question="在 Python 中，True + 1 的结果是？",
    option_a="2",
    option_b="True",
    option_c="报错",
    option_d="1",
    correct_answer="A",
    explanation="在 Python 中，True 等价于整数 1，所以 True + 1 = 2。"
)

# 1.4 输入与输出
l1_4 = Lesson.objects.create(
    chapter=ch1_1, title="1.4 输入与输出 (IO)", order=4, lesson_type='code',
    code_challenge_prompt="""# 1.4 输入与输出 - 代码验证题
# 题目：输入两个整数，输出它们的乘积。

# 提示：使用 input() 获取输入，int() 转换类型

# 你的代码:

""",
    content="""
## 🎯 本节目标
- 掌握 print() 输出函数的各种用法
- 掌握 input() 输入函数的使用
- 学会字符串格式化的多种方式

---

## 1️⃣ 输出：print() 函数

### 🔹 基本用法
```python
print("Hello, World!")  # 输出字符串
print(123)              # 输出数字
print(True)              # 输出布尔值
```

### 🔹 多个参数
```python
# 用逗号分隔，自动加空格
print("Hello", "World")     # Hello World
print(1, 2, 3)             # 1 2 3

# 不同类型混用
print("年龄:", 18)          # 年龄: 18
```

### 🔹 sep 参数 - 分隔符
```python
# 默认用空格分隔
print(1, 2, 3)             # 1 2 3

# 自定义分隔符
print(1, 2, 3, sep="-")     # 1-2-3
print("2023", "10", "01", sep="-")  # 2023-10-01
```

### 🔹 end 参数 - 结尾符
```python
# 默认换行
print("第一行")
print("第二行")

# 不换行
print("第一行", end=" ")
print("第二行")              # 第一行 第二行

# 用分隔符连接
for i in range(5):
    print(i, end=" ")        # 0 1 2 3 4 
```

### 🔹 f-string 格式化（推荐！）
```python
name = "Alice"
age = 18
score = 95.5

# 基本用法
print(f"我叫{name}，今年{age}岁")

# 数字格式化
print(f"分数: {score:.1f}")   # 分数: 95.5 (保留1位小数)
print(f"分数: {score:.2f}")   # 分数: 95.50 (保留2位小数)

# 宽度对齐
print(f"{name:>10}")    #      Alice (右对齐，宽度10)
print(f"{name:<10}")    # Alice      (左对齐，宽度10)
print(f"{name:^10}")    #   Alice   (居中，宽度10)

# 数字补零
print(f"{42:05d}")      # 00042 (宽度5，不足补零)
```

### 🔹 其他格式化方式
```python
# % 格式化（旧式）
name = "Alice"
print("Hello, %s" % name)

# .format() 方法
print("Hello, {}".format(name))
print("Hello, {name}".format(name="Bob"))
```

---

## 2️⃣ 输入：input() 函数

### 🔹 基本用法
```python
# input() 会暂停程序，等待用户输入
name = input()
print("你输入的是:", name)

# 带提示信息的 input()
name = input("请输入你的名字: ")
print("你好,", name)
```

### 🔹 重要：input() 返回的是字符串！
```python
# ❌ 常见错误
age = input("请输入年龄: ")
print(age + 1)  # 报错！字符串不能和数字相加
# input 返回的是字符串 "18"，不是数字 18

# ✅ 正确做法
age = int(input("请输入年龄: "))
print(age + 1)  # 正确：整数相加
```

### 🔹 读取多种类型
```python
# 读取整数
num = int(input())

# 读取浮点数
price = float(input())

# 读取多个值（空格分隔）
a, b = input().split()  # 输入: 1 2
a = int(a)
b = int(b)

# 或者更简洁
a, b = map(int, input().split())
```

---

## 3️⃣ 实战练习

### 练习1：简单计算器
```python
# 输入两个数字，输出它们的和、差、积、商
num1 = float(input("请输入第一个数: "))
num2 = float(input("请输入第二个数: "))

print(f"和: {num1 + num2}")
print(f"差: {num1 - num2}")
print(f"积: {num1 * num2}")
print(f"商: {num1 / num2}")
```

### 练习2：个人信息录入
```python
name = input("姓名: ")
age = int(input("年龄: "))
height = float(input("身高(cm): "))

print(f"\\n{'='*20}")
print(f"姓名: {name}")
print(f"年龄: {age}岁")
print(f"身高: {height}cm")
print(f"{'='*20}")
```

---

## 📝 本节小结
- `print()` 用于输出， 支持 `sep` 和 `end` 参数
- `input()` 用于输入，**返回值是字符串**
- 使用 `f-string` 进行字符串格式化（推荐）
- 需要数字时要使用 `int()` 或 `float()` 转换
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
Quiz.objects.create(
    lesson=l1_4,
    question="以下哪个是 f-string 正确的格式化方式？",
    option_a="print('Score: %.2f' % score)",
    option_b="print('Score: {}'.format(score))",
    option_c="print(f'Score: {score}')",
    option_d="print('Score: ' + score)",
    correct_answer="C",
    explanation="f-string 使用 f 或 F 开头，在字符串中用 {} 包裹变量，是 Python 3.6+ 推荐的格式化方式。"
)

# ==========================================
# Ch2: 运算符与表达式
# ==========================================
ch1_2, _ = Chapter.objects.get_or_create(course=c1, title="第2章：运算符与表达式", defaults={'order': 2})

# 2.1 算术运算符
l2_1 = Lesson.objects.create(
    chapter=ch1_2, title="2.1 算术运算符", order=1, lesson_type='text',
    content="""
## 🎯 本节目标
- 掌握 Python 的算术运算符
- 理解整除和取模的特殊行为
- 学会使用复合赋值运算符

---

## 1️⃣ 算术运算符一览

| 运算符 | 描述 | 示例 | 结果 | 备注 |
| :--- | :--- | :--- | :--- | :--- |
| `+` | 加法 | `3 + 5` | `8` | |
| `-` | 减法 | `5 - 3` | `2` | |
| `*` | 乘法 | `3 * 5` | `15` | |
| `/` | **真除法** | `5 / 2` | `2.5` | 结果总是 float |
| `//` | **整除** | `5 // 2` | `2` | 向下取整 |
| `%` | 取模 (余数) | `5 % 2` | `1` | |
| `**` | 幂运算 | `2 ** 3` | `8` | $2^3$ |

---

## 2️⃣ 重点：整除 // 与取模 %

### 🔹 整除 // 
向下取整（往**小**的方向取整）
```python
# 正数：直接取整
5 // 2       # 2
7 // 3       # 2

# 负数：注意！
-5 // 2      # -3 (向下取整，不是 -2！)

# 负数整除的规律
-7 // 3      # -3
7 // -3       # -3
```

### 🔹 取模 %
余数的符号与**除数**一致
```python
# 正数取模
7 % 3        # 1
10 % 4       # 2

# 负数取模
-7 % 3       # 2  (余数符号与除数 3 一致)
7 % -3        # -2 (余数符号与除数 -3 一致)
-7 % -3       # -1
```

### 🔹 经典应用

**判断奇偶**
```python
n = 7
if n % 2 == 0:
    print("偶数")
else:
    print("奇数")
```

**获取各位数字**
```python
n = 123
ge = n % 10        # 3 (个位)
shi = (n // 10) % 10  # 2 (十位)
bai = n // 100     # 1 (百位)
```

**循环遍历**
```python
# 遍历 0-9，每次走 2 步
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

---

## 3️⃣ 幂运算 **

### 🔹 基本用法
```python
2 ** 3        # 8 (2 的 3 次方)
5 ** 2        # 25 (5 的平方)
9 ** 0.5      # 3.0 (平方根)
```

### 🔹 负数指数
```python
2 ** -1       # 0.5 (2 的 -1 次方 = 1/2)
4 ** -2       # 0.0625 (1/16)
```

---

## 4️⃣ 复合赋值运算符

| 运算符 | 等价于 | 示例 |
| :--- | :--- | :--- |
| `+=` | a = a + b | x += 3 |
| `-=` | a = a - b | x -= 3 |
| `*=` | a = a * b | x *= 3 |
| `/=` | a = a / b | x /= 3 |
| `//=` | a = a // b | x //= 3 |
| `%=` | a = a % b | x %= 3 |
| `**=` | a = a ** b | x **= 3 |

### 🔹 示例
```python
x = 10
x += 5        # x = 15
x -= 3        # x = 12
x *= 2        # x = 24

# 字符串也可以用 +=
s = "Hello"
s += " World"
print(s)     # "Hello World"

# 列表也可以
lst = [1, 2]
lst += [3, 4]
print(lst)   # [1, 2, 3, 4]
```

### ⚠️ 注意：Python 没有 ++ 或 -- ！
```python
# ❌ 错误
i++

# ✅ 正确
i += 1
i -= 1
```

---

## 📝 动手练习
```python
# 练习1：计算
# 计算 123 的各位数字之和 (1+2+3=6)

# 练习2：整除应用
# 输入一个秒数，转换为 XX 分 XX 秒
# 例如：130秒 = 2分10秒
```

"""
)
Quiz.objects.create(
    lesson=l2_1,
    question="表达式 5 // 2 的结果是？",
    option_a="2.5",
    option_b="2",
    option_c="3",
    option_d="2.0",
    correct_answer="B",
    explanation="// 是整除运算符，向下取整，5 除以 2 等于 2.5，向下取整为 2。"
)
Quiz.objects.create(
    lesson=l2_1,
    question="表达式 2 ** 3 的结果是？",
    option_a="5",
    option_b="6",
    option_c="8",
    option_d="9",
    correct_answer="C",
    explanation="** 是幂运算符，表示 2 的 3 次方，即 2 * 2 * 2 = 8。"
)
Quiz.objects.create(
    lesson=l2_1,
    question="-7 % 3 的结果是？",
    option_a="-1",
    option_b="1",
    option_c="2",
    option_d="-2",
    correct_answer="C",
    explanation="Python 中取模运算的结果符号与除数一致，除数是 3（正数），所以结果是 2。"
)

# 2.2 比较与逻辑运算符
l2_2 = Lesson.objects.create(
    chapter=ch1_2, title="2.2 比较与逻辑运算符", order=2, lesson_type='code',
    code_challenge_prompt="""# 2.2 比较与逻辑运算符 - 代码验证题
# 题目：输入一个年份，判断是否为闰年
# 闰年条件：能被4整除 且 不能被100整除，或者能被400整除

year = int(input("请输入年份: "))

# 在这里写下你的判断代码:

""",
    content="""
## 🎯 本节目标
- 掌握比较运算符
- 掌握逻辑运算符
- 理解短路求值机制

---

## 1️⃣ 比较运算符

比较结果为 `True` 或 `False`

| 运算符 | 描述 | 示例 |
| :--- | :--- | :--- |
| `==` | 等于 | 5 == 5 → True |
| `!=` | 不等于 | 5 != 3 → True |
| `>` | 大于 | 5 > 3 → True |
| `<` | 小于 | 5 < 3 → False |
| `>=` | 大于等于 | 5 >= 5 → True |
| `<=` | 小于等于 | 5 <= 3 → False |

### 🔹 链式比较（Python 特有！）
```python
x = 5

# 传统写法
if x >= 1 and x <= 10:
    print("在 1-10 范围内")

# Pythonic 写法（更简洁）
if 1 <= x <= 10:
    print("在 1-10 范围内")

# 多重比较
if 1 < 2 < 3 < 4:
    print("链式比较成功")
```

---

## 2️⃣ 逻辑运算符

| 运算符 | 描述 | C++ 对应 | 说明 |
| :--- | :--- | :--- | :--- |
| `and` | 与 | `&&` | 全真才真 |
| `or` | 或 | `\|\|` | 一真即真 |
| `not` | 非 | `!` | 真变假，假变真 |

### 🔹 真值表
```python
# and: 两边都为 True 才为 True
True and True    # True
True and False   # False
False and True   # False
False and False  # False

# or: 至少一边为 True 就为 True
True or True     # True
True or False    # True
False or True    # True
False or False   # False

# not: 取反
not True         # False
not False        # True
```

---

## 3️⃣ 短路求值 (Short-circuit Evaluation)

Python 会**尽可能少地**计算表达式

### 🔹 and 的短路
```python
# a and b: 如果 a 为假，直接返回 a，不计算 b
result = 0 and (10 / 0)  # 不会报错！返回 0
# 因为 0 是假，Python 直接返回 0，不会计算 (10/0)
```

### 🔹 or 的短路
```python
# a or b: 如果 a 为真，直接返回 a，不计算 b
result = 1 or (10 / 0)   # 不会报错！返回 1
# 因为 1 是真，Python 直接返回 1
```

### 🔹 实际应用

**安全的默认值**
```python
# 传统写法
name = ""
if user_name:
    name = user_name
else:
    name = "Guest"

# Pythonic 写法
name = user_name or "Guest"
```

**安全的除法检查**
```python
def safe_divide(a, b):
    # 如果 b 为 0，直接返回 None，不会执行除法
    return b != 0 and a / b

print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # False
```

---

## 4️⃣ 运算符优先级

从**高到低**：

1. `**` (幂运算，最高)
2. `+`, `-` (正负号)
3. `*`, `/`, `//`, `%`
4. `+`, `-` (加减)
5. `==`, `!=`, `>`, `<`, `>=`, `<=`
6. `not`
7. `and`
8. `or` (最低)

### 🔹 建议
**如果不确定，就加括号！**

```python
# 优先级容易混淆
print(2 + 3 * 4)      # 14 (先乘后加)

# 加括号更清晰
print((2 + 3) * 4)    # 20

# 复杂表达式
print(not True or True)    # True
print(not (True or True))  # False
```

---

## 📝 实战：闰年判断

```python
year = int(input("请输入年份: "))

# 闰年条件：
# 1. 能被4整除 且 不能被100整除
# 2. 或者能被400整除

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year}年是闰年")
else:
    print(f"{year}年不是闰年")
```

### 🔹 测试数据
- 2000 年：闰年（能被400整除）
- 2024 年：闰年（能被4整除且不能被100整除）
- 1900 年：不是闰年（能被100整除但不能被400整除）
- 2023 年：不是闰年
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
Quiz.objects.create(
    lesson=l2_2,
    question="表达式 0 and 10 / 0 的结果是？",
    option_a="报错",
    option_b="0",
    option_c="10",
    option_d="False",
    correct_answer="B",
    explanation="由于短路求值，0 为假，直接返回 0，不会计算 10/0，所以不会报错。"
)

# 2.3 运算符优先级
l2_3 = Lesson.objects.create(
    chapter=ch1_2, title="2.3 运算符优先级", order=3, lesson_type='text',
    content="""
## 🎯 本节目标
- 记住运算符优先级
- 学会使用括号明确计算顺序

---

## 1️⃣ 运算符优先级表

从**高到低**排序：

| 优先级 | 运算符 | 说明 |
| :--- | :--- | :--- |
| 1 (最高) | `**` | 幂运算 |
| 2 | `+`, `-` | 正负号 |
| 3 | `*`, `/`, `//`, `%` | 乘除取模 |
| 4 | `+`, `-` | 加减 |
| 5 | `==`, `!=`, `>`, `<`, `>=`, `<=` | 比较 |
| 6 | `not` | 逻辑非 |
| 7 | `and` | 逻辑与 |
| 8 (最低) | `or` | 逻辑或 |

---

## 2️⃣ 记忆口诀

**"先算幂，再算符，乘除取模后加减，比较非与或"**

- **幂** - `**`
- **符** - `+ -` (正负号)
- **乘除** - `* / // %`
- **加减** - `+ -`
- **比较** - `== != > < >= <=`
- **非** - `not`
- **与** - `and`
- **或** - `or`

---

## 3️⃣ 示例演示

```python
# 例1：先乘后加
print(2 + 3 * 4)      # 14
print((2 + 3) * 4)    # 20

# 例2：幂运算最高
print(-3 ** 2)         # -9 (相当于 -(3**2))
print((-3) ** 2)       # 9

# 例3：比较 + 逻辑
print(1 < 2 and 3 < 4)   # True
print(1 > 2 or 3 < 4)    # True
print(not 1 > 2)          # True

# 例4：复杂表达式
print(2 + 3 * 4 ** 2)           # 50 (4**2=16, 16*3=48, 48+2=50)
print((2 + 3) * 4 ** 2)         # 80 ((2+3)=5, 4**2=16, 16*5=80)
```

---

## ⚠️ 最佳实践

**当你不确定优先级时，永远使用括号！**

```python
# ❌ 不好：依赖记忆
result = a and b or c and d

# ✅ 好：清晰明确
result = (a and b) or (c and d)

# ✅ 非常好：加注释
# 逻辑：先判断是否是VIP，再判断是否超过限额
is_valid = (is_vip and amount > 1000) or (is_admin)
```

---

## 📝 练习

```python
# 计算下列表达式的结果
print(2 + 3 * 4 ** 2)
print((2 + 3) * 4 ** 2)
print(not True or False and True)
print(1 < 2 < 3 < 4)
```
"""
)
Quiz.objects.create(
    lesson=l2_3,
    question="表达式 2 + 3 * 4 的计算结果是？",
    option_a="20",
    option_b="14",
    option_c="24",
    option_d="10",
    correct_answer="B",
    explanation="乘法优先级高于加法，先算 3*4=12，再算 2+12=14。"
)
Quiz.objects.create(
    lesson=l2_3,
    question="-3 ** 2 的结果是？",
    option_a="-9",
    option_b="9",
    option_c="-6",
    option_d="6",
    correct_answer="A",
    explanation="幂运算优先级高于负号，所以是 -(3**2) = -9。如果想要 (-3)**2 = 9，需要加括号。"
)

# ==========================================
# Ch3: 决策与分支
# ==========================================
ch1_3, _ = Chapter.objects.get_or_create(course=c1, title="第3章：决策与分支", defaults={'order': 3})

# 3.1 分支结构
l3_1 = Lesson.objects.create(
    chapter=ch1_3, title="3.1 分支结构详解", order=1, lesson_type='code',
    code_challenge_prompt="""# 3.1 分支结构 - 代码验证题
# 题目：输入一个整数，判断是正数、负数还是零

num = int(input("请输入一个整数: "))

# 在这里写下你的判断代码:

""",
    content="""
## 🎯 本节目标
- 掌握 if-elif-else 语法
- 理解缩进的重要性
- 学会使用 pass 语句

---

## 1️⃣ if 语句基础

### 🔹 语法结构
```python
if 条件:
    代码块
```

### 🔹 完整结构
```python
if 条件1:
    代码块1
elif 条件2:
    代码块2
else:
    代码块3
```

---

## 2️⃣ 关键语法点

### 🔹 冒号 :
每个条件行末尾**必须有冒号**
```python
# ✅ 正确
if age >= 18:
    print("成年")

# ❌ 错误
if age >= 18
    print("成年")
```

### 🔹 缩进 (Indentation)
Python 使用**缩进**（通常是4个空格）来划分代码块

```python
# ✅ 正确缩进
if True:
    print("这是 if 内的代码")
    print("这也是")

print("这是 if 外的代码")

# ❌ 缩进错误会导致语法错误
if True:
print("错误！没有缩进")
```

### 🔹 pass 语句
如果代码块暂时为空，必须用 `pass` 占位
```python
if score > 60:
    pass  # TODO: 等下再写
else:
    print("需要补考")
```

---

## 3️⃣ 多条件判断

### 🔹 if-elif-else
```python
score = 85

if score >= 90:
    print("A - 优秀")
elif score >= 80:
    print("B - 良好")
elif score >= 70:
    print("C - 中等")
elif score >= 60:
    print("D - 及格")
else:
    print("F - 不及格")
```

### 🔹 嵌套 if
```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("可以开车")
    else:
        print("需要考驾照")
else:
    print("年龄不够，不能开车")
```

---

## 4️⃣ 条件表达式

### 🔹 三元运算符
Python 也有三元运算符，但写法不同：
```python
# 传统写法
if age >= 18:
    status = "成人"
else:
    status = "未成年"

# Pythonic 写法（一行）
status = "成人" if age >= 18 else "未成年"
```

---

## 5️⃣ 实战练习

### 练习1：成绩分级
```python
score = int(input("请输入成绩: "))

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
elif score >= 60:
    print("D")
else:
    print("F")
```

### 练习2：大小比较
```python
a = int(input("a = "))
b = int(input("b = "))

if a > b:
    print(f"{a} > {b}")
elif a < b:
    print(f"{a} < {b}")
else:
    print(f"{a} = {b}")
```

### 练习3：判断是否闰年
```python
year = int(input("年份: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("闰年")
else:
    print("平年")
```

---

## 📝 常见错误

1. **忘记冒号**
   ```python
   # ❌
   if x > 0
       print(x)
   
   # ✅
   if x > 0:
       print(x)
   ```

2. **缩进不一致**
   ```python
   # ❌ 混用空格和 tab
   if True:
       print(1)
   print(2)
   
   # ✅ 统一使用 4 个空格
   ```
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
Quiz.objects.create(
    lesson=l3_1,
    question="以下哪个条件会返回 True？",
    option_a="bool(0)",
    option_b="bool('' )",
    option_c="bool('0')",
    option_d="bool([])",
    correct_answer="C",
    explanation="空字符串 ''、数字 0、空列表 [] 都是假值，但非空字符串 '0' 是真值。"
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

# 循环结构
ch2_1, _ = Chapter.objects.get_or_create(course=c2, title="第1章：循环结构", defaults={'order': 1})

l_r1 = Lesson.objects.create(
    chapter=ch2_1, title="1.1 range() 与 For 循环", order=1, lesson_type='text',
    content="""
## 🎯 本节目标
- 掌握 range() 函数的使用
- 学会使用 for 循环遍历序列

---

## 1️⃣ range() 函数详解

`range()` 生成一个**整数序列**，左闭右开 `[start, stop)`

### 🔹 三种用法

```python
# range(stop) - 从 0 开始
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# range(start, stop) - 自定义起点
for i in range(2, 6):
    print(i)  # 2, 3, 4, 5

# range(start, stop, step) - 自定义步长
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# 负数步长（倒序）
for i in range(5, 0, -1):
    print(i)  # 5, 4, 3, 2, 1
```

### 🔹 步长为负
```python
# 倒序遍历
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, ..., 1
```

---

## 2️⃣ for 循环

### 🔹 遍历序列
```python
# 遍历列表
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 遍历字符串
for char in "Python":
    print(char)

# 遍历字典（默认遍历键）
d = {"a": 1, "b": 2}
for key in d:
    print(key, d[key])
```

### 🔹 使用 range() 控制循环次数
```python
# 循环 5 次
for i in range(5):
    print(f"第 {i+1} 次循环")

# 遍历带索引
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")

# 或者用 enumerate
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")
```

---

## 📝 练习

```python
# 练习1：打印 1-10
for i in range(1, 11):
    print(i)

# 练习2：打印偶数
for i in range(0, 11, 2):
    print(i)

# 练习3：打印九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}*{i}={i*j}", end="\\t")
    print()
```
"""
)

l_r2 = Lesson.objects.create(
    chapter=ch2_1, title="1.2 While 循环与死循环", order=2, lesson_type='code',
    code_challenge_prompt="""# While 循环练习
# 题目：计算 1+2+3+...+100 的和

sum = 0
i = 1

# 在这里写下 while 循环代码:

print(f"1到100的和是: {sum}")
""",
    content="""
## 🎯 本节目标
- 掌握 while 循环的使用
- 理解死循环的危害和避免方法

---

## 1️⃣ While 循环

当条件为 True 时，重复执行代码块

### 🔹 语法
```python
while 条件:
    代码块
```

### 🔹 示例
```python
# 打印 1-5
n = 1
while n <= 5:
    print(n)
    n += 1  # 重要：更新条件！
```

### 🔹 计算 1+2+...+100
```python
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1

print(sum)  # 5050
```

---

## 2️⃣ 死循环

如果条件永远为 True，循环不会停止！

### 🔹 常见死循环
```python
# ❌ 死循环：忘记更新条件
while True:
    print("停不下来了！")

# ❌ 死循环：条件永远为真
n = 1
while n > 0:
    print(n)
    n += 1  # n 会越来越大，永远大于 0
```

### 🔹 安全的 while True
```python
# 使用 break 退出
while True:
    answer = input("继续吗？(y/n): ")
    if answer == 'n':
        break  # 退出循环
    print("继续运行...")
```

---

## 3️⃣ 练习

```python
# 练习1：计算阶乘
# 5! = 5*4*3*2*1 = 120

n = 5
factorial = 1
while n > 0:
    factorial *= n
    n -= 1
print(factorial)

# 练习2：猜数字游戏
import random
target = random.randint(1, 100)
while True:
    guess = int(input("猜一个1-100的数字: "))
    if guess == target:
        print("恭喜猜对了！")
        break
    elif guess < target:
        print("太小了！")
    else:
        print("太大了！")
```
"""
)

l_r3 = Lesson.objects.create(
    chapter=ch2_1, title="1.3 循环控制 (Break/Continue/Else)", order=3, lesson_type='text',
    content="""
## 🎯 本节目标
- 掌握 break、continue 的使用
- 理解 else 与循环的配合

---

## 1️⃣ break - 立即终止循环

```python
# 找到第一个平方大于 50 的数
for i in range(1, 100):
    if i ** 2 > 50:
        print(f"第一个平方大于50的数是: {i}")
        break  # 找到后立即退出循环
    print(i, i**2)
```

---

## 2️⃣ continue - 跳过本次循环

```python
# 打印 1-10，跳过 5
for i in range(1, 11):
    if i == 5:
        continue  # 跳过 5，继续下一次
    print(i)
# 输出: 1,2,3,4,6,7,8,9,10
```

---

## 3️⃣ else - 循环正常结束后执行

**这是 Python 特有的语法！**

```python
# 找到则退出，找不到则执行 else
for i in range(2, 10):
    if i == 100:  # 永远找不到
        print("找到了！")
        break
else:
    print("循环正常结束，没有找到")

# 配合 while
n = 5
while n > 0:
    n -= 1
    if n == 100:
        break
else:
    print("循环正常结束")
```

---

## 4️⃣ 实战：判断质数

```python
n = 17
is_prime = True

for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{n} 是质数")
else:
    print(f"{n} 不是质数")
```
"""
)

# 更多课程内容...
print("课程数据填充完成！")
