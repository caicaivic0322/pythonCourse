import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from courses.models import Course, Chapter, Lesson

# 1. Update or Create Course (Chinese) - Safe operation
print("正在更新课程数据...")

# 2. Create Course (Chinese)
course, created = Course.objects.update_or_create(
    title="Head First Python: 基础入门",
    defaults={
        'description': "基于《Head First Python》经典教材，带你轻松入门 Python 编程。从基础语法到数据结构，再到函数与模块，一步步掌握 Python 核心技能。",
        'order': 1
    }
)
print(f"更新课程: {course.title}")

# ==========================================
# Chapter 1: The Basics
# ==========================================
ch1, _ = Chapter.objects.update_or_create(
    course=course, 
    title="第一章：基础知识 - 快速入门", 
    defaults={'order': 1}
)

# Lesson 1.1: Mission Briefing
Lesson.objects.update_or_create(
    chapter=ch1, 
    title="任务简报：初识 Python", 
    defaults={
        'content': """
## 什么是 Python？

Python 是一种**强大且易于学习**的编程语言。它就像是编程界的“瑞士军刀”，无所不能！

### 为什么选择 Python？
- **简单易读**：代码像英语一样直观，非常适合初学者。
- **应用广泛**：从网站开发（YouTube, Instagram）到人工智能（ChatGPT），再到数据分析，Python 无处不在。
- **社区强大**：拥有庞大的开发者社区，遇到问题很容易找到答案。

### 我们的任务
在本课程中，你将扮演一名“代码学员”，通过完成一个个任务，掌握 Python 的核心技能，最终获得“Python 大师”勋章！
    """,
        'lesson_type': 'text',
        'order': 1
    }
)

# Lesson 1.2: First Script
Lesson.objects.update_or_create(
    chapter=ch1, 
    title="你的第一个脚本", 
    defaults={
        'content': """
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
        'lesson_type': 'code',
        'code_challenge_prompt': "print('Hello, Python!')",
        'order': 2
    }
)

# Lesson 1.3: Variables & Assignment
Lesson.objects.update_or_create(
    chapter=ch1, 
    title="变量与赋值", 
    defaults={
        'content': """
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

### 动态类型
Python 是**动态类型**语言。这意味着你不需要声明变量类型，Python 会自动根据你赋的值来决定类型。
```python
x = 10      # x 是整数
x = "Hello" # 现在 x 变成了字符串！
```
    """,
        'lesson_type': 'text',
        'order': 3
    }
)

# Lesson 1.4: Control Flow
Lesson.objects.update_or_create(
    chapter=ch1, 
    title="流程控制：做出决定", 
    defaults={
        'content': """
## if, else, elif

程序不仅仅是按顺序执行代码，还需要根据情况做出决定。

### if 语句
```python
if score > 90:
    print("优秀！")
```
注意：Python 使用**缩进**（Indentation）来划分代码块，而不是大括号 `{}`。

### else 语句
```python
if score >= 60:
    print("及格")
else:
    print("不及格")
```

### elif 语句 (else if)
```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
```

### 实战挑战
定义一个变量 `temperature`，如果它大于 30，打印 "热"；否则打印 "舒适"。
    """,
        'lesson_type': 'code',
        'code_challenge_prompt': """temperature = 35
# 在这里写下你的 if-else 代码
""",
        'order': 4
    }
)

# Lesson 1.5: Iteration
Lesson.objects.update_or_create(
    chapter=ch1, 
    title="循环迭代", 
    defaults={
        'content': """
## for 循环

当你需要重复做某件事，或者遍历一组数据时，`for` 循环是你的好帮手。

### 遍历列表
```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

### 使用 range()
`range()` 函数可以生成一个数字序列。
```python
for i in range(5):
    print(i)
# 输出: 0, 1, 2, 3, 4
```

### 啤酒之歌 (Beer Song) 挑战
利用循环，打印出 "99 bottles of beer on the wall..." 的歌词片段。
    """,
        'lesson_type': 'code',
        'code_challenge_prompt': """for i in range(5, 0, -1):
    print(f"{i} bottles of beer on the wall...")
print("No more bottles of beer on the wall.")
""",
        'order': 5
    }
)

# ==========================================
# Chapter 2: List Data
# ==========================================
ch2, _ = Chapter.objects.update_or_create(
    course=course, 
    title="第二章：列表数据 - 处理有序数据", 
    defaults={'order': 2}
)

# Lesson 2.1: Intro to Lists
Lesson.objects.update_or_create(
    chapter=ch2, 
    title="列表初探", 
    defaults={
        'content': """
## 什么是列表 (List)？

列表是 Python 中最常用的数据结构之一，它就像一个**有序的容器**，可以存放任何东西。

### 创建列表
使用方括号 `[]` 来创建列表，元素之间用逗号 `,` 分隔。

```python
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]
mixed = [1, "Alice", True, 3.14] # 列表可以包含不同类型的数据！
```

### 访问元素
列表是有序的，你可以通过**索引** (Index) 来访问其中的元素。索引从 `0` 开始。

```python
names = ["Alice", "Bob", "Charlie"]
print(names[0]) # 输出: Alice
print(names[1]) # 输出: Bob
```
    """,
        'lesson_type': 'text',
        'order': 1
    }
)

# Lesson 2.2: List Methods
Lesson.objects.update_or_create(
    chapter=ch2, 
    title="列表方法", 
    defaults={
        'content': """
## 列表的常用方法

Python 的列表对象自带了许多强大的方法（函数）。

### 1. append() - 追加
在列表末尾添加一个元素。
```python
cart = ["apple"]
cart.append("banana")
# cart 变为 ["apple", "banana"]
```

### 2. remove() - 移除
移除列表中第一个匹配的元素。
```python
cart.remove("apple")
# cart 变为 ["banana"]
```

### 3. pop() - 弹出
移除并返回指定位置的元素（默认是最后一个）。
```python
last_item = cart.pop()
# last_item 是 "banana", cart 变为空列表 []
```

### 4. extend() - 扩展
将另一个列表的所有元素添加到当前列表中。
```python
list1 = [1, 2]
list2 = [3, 4]
list1.extend(list2)
# list1 变为 [1, 2, 3, 4]
```

### 5. insert() - 插入
在指定索引位置插入一个元素。
```python
nums = [1, 3]
nums.insert(1, 2) # 在索引 1 的位置插入 2
# nums 变为 [1, 2, 3]
```
    """,
        'lesson_type': 'code',
        'code_challenge_prompt': """my_list = [1, 2, 3]
# 尝试使用 append, pop, insert 等方法操作这个列表
print(my_list)
""",
        'order': 2
    }
)

# Lesson 2.3: Challenge: Don't Panic
Lesson.objects.update_or_create(
    chapter=ch2, 
    title="实战：Don't Panic", 
    defaults={
        'content': """
## 挑战任务

将字符串 "Don't panic!" 转换为 "on tap"。
你需要使用列表切片和列表方法来完成这个变换。

原始代码：
```python
phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# 在这里写下你的代码，操作 plist
# 目标：让 plist 最终包含 ['o', 'n', ' ', 't', 'a', 'p']

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
```

提示：
1. 你可以使用 `pop()` 移除不需要的字符。
2. 你可以使用 `remove()` 移除特定字符。
3. 你可以使用 `extend()` 或 `insert()` 调整顺序。
    """,
        'lesson_type': 'code',
        'code_challenge_prompt': """phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)

# TODO: 修改 plist，使其变为 ['o', 'n', ' ', 't', 'a', 'p']
# 提示：观察 "Don't panic!" 和 "on tap" 的字符关系

new_phrase = ''.join(plist)
print(plist)
print(new_phrase)
""",
        'order': 3
    }
)

# ==========================================
# Chapter 3: Structured Data
# ==========================================
ch3, _ = Chapter.objects.update_or_create(
    course=course, 
    title="第三章：结构化数据 - 字典与集合", 
    defaults={'order': 3}
)

# Lesson 3.1: Dictionary Basics
Lesson.objects.update_or_create(
    chapter=ch3, 
    title="字典基础", 
    defaults={
        'content': """
## 什么是字典 (Dictionary)？

如果说列表是**有序**的数组，那么字典就是**键值对** (Key-Value Pair) 的集合。它就像一本真正的字典，你通过“单词”（键）来查找“定义”（值）。

### 创建字典
使用大括号 `{}` 创建字典，键和值之间用冒号 `:` 分隔。

```python
person = {
    'name': 'Ford Prefect',
    'gender': 'Male',
    'occupation': 'Researcher',
    'home_planet': 'Betelgeuse Seven'
}
```

### 访问值
使用方括号 `[]` 和键名来访问对应的值。

```python
print(person['name']) # 输出: Ford Prefect
```

### 添加/修改
```python
person['age'] = 42        # 添加新键值对
person['name'] = 'Arthur' # 修改已有键的值
```
    """,
        'lesson_type': 'code',
        'code_challenge_prompt': """student = {'name': 'Alice', 'score': 90}
# 尝试修改 score，并添加一个新的键 'grade'
print(student)
""",
        'order': 1
    }
)

# Lesson 3.2: Iterating Dictionaries
Lesson.objects.update_or_create(
    chapter=ch3, 
    title="迭代字典", 
    defaults={
        'content': """
## 遍历字典

我们可以使用 `for` 循环来遍历字典。

### 1. 遍历键 (Keys)
默认情况下，遍历字典会得到键。
```python
data = {'a': 1, 'b': 2}
for key in data:
    print(key)
# 输出: a, b (顺序不一定)
```

### 2. 遍历值 (Values)
```python
for value in data.values():
    print(value)
```

### 3. 遍历键值对 (Items)
使用 `.items()` 方法同时获取键和值，这是最常用的方式。
```python
for key, value in data.items():
    print(f"Key: {key}, Value: {value}")
```
    """,
        'lesson_type': 'code',
        'code_challenge_prompt': """scores = {'Math': 95, 'English': 88, 'History': 92}
# 使用 for 循环打印每门课的成绩
""",
        'order': 2
    }
)

# Lesson 3.3: Sets and Tuples
Lesson.objects.update_or_create(
    chapter=ch3, 
    title="集合与元组", 
    defaults={
        'content': """
## 集合 (Set)
集合是一个**无序**且**不重复**的元素集。它非常适合用来**去重**。

```python
vowels = {'a', 'e', 'i', 'o', 'u'}
letters = set('hello world')
print(letters) 
# 输出类似: {'d', 'e', 'h', 'l', 'o', 'r', 'w'} (无序，且 'l' 和 'o' 只出现一次)
```

## 元组 (Tuple)
元组就像列表，但是它是**不可变** (Immutable) 的。一旦创建，就不能修改（不能添加、删除或更改元素）。使用小括号 `()`。

```python
coordinates = (10.0, 20.0)
# coordinates[0] = 15.0  <-- 这会报错！
```
元组通常用于存储不应该被改变的数据，比如坐标、配置项等。
    """,
        'lesson_type': 'text',
        'order': 3
    }
)

# Lesson 3.4: Challenge: Vowels Frequency
Lesson.objects.update_or_create(
    chapter=ch3, 
    title="实战：元音统计", 
    defaults={
        'content': """
## 挑战任务

编写一个程序，统计一个单词中每个元音字母 ('a', 'e', 'i', 'o', 'u') 出现的次数。

示例输入："hitch-hiker"
示例输出：
a was found 0 time(s).
e was found 1 time(s).
i was found 2 time(s).
o was found 0 time(s).
u was found 0 time(s).

提示：
1. 创建一个字典来存储计数，初始值都为 0。
2. 遍历单词中的每个字符。
3. 检查字符是否是元音。
4. 如果是，更新字典中的计数。
    """,
        'lesson_type': 'code',
        'code_challenge_prompt': """word = "hitch-hiker"
vowels = ['a', 'e', 'i', 'o', 'u']
found = {}

# 初始化字典
for v in vowels:
    found[v] = 0

# TODO: 遍历 word，统计元音出现次数

# 打印结果
for k, v in sorted(found.items()):
    print(f"{k} was found {v} time(s).")
""",
        'order': 4
    }
)

# ==========================================
# Chapter 4: Functions & Modules
# ==========================================
ch4, _ = Chapter.objects.update_or_create(
    course=course, 
    title="第四章：代码复用 - 函数与模块", 
    defaults={'order': 4}
)

# Lesson 4.1: Defining Functions
Lesson.objects.update_or_create(
    chapter=ch4, 
    title="定义函数", 
    defaults={
        'content': """
## 为什么需要函数？

当你的代码越来越长，你会发现自己在使用复制粘贴。这通常是一个坏信号。
函数允许你将一段代码**封装**起来，给它起个名字，然后在需要的地方**重复调用**。

### 定义函数
使用 `def` 关键字定义函数。

```python
def say_hello():
    print("Hello, Python!")
```

### 调用函数
```python
say_hello()
say_hello()
say_hello()
```
    """,
        'lesson_type': 'code',
        'code_challenge_prompt': """def say_hello():
    print("Hello, Python!")

# 调用三次这个函数
""",
        'order': 1
    }
)

# Lesson 4.2: Arguments & Return Values
Lesson.objects.update_or_create(
    chapter=ch4, 
    title="参数与返回值", 
    defaults={
        'content': """
## 函数参数 (Arguments)
函数可以接收数据作为输入，这些数据称为参数。

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
```

## 返回值 (Return Values)
函数不仅可以打印东西，还可以**返回**数据给调用者，使用 `return` 关键字。

```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result) # 输出: 8
```
一旦执行到 `return`，函数就会立即结束。
    """,
        'lesson_type': 'code',
        'code_challenge_prompt': """def calculate_area(width, height):
    # TODO: 返回矩形的面积
    pass

area = calculate_area(5, 10)
print(f"Area is: {area}")
""",
        'order': 2
    }
)

# Lesson 4.3: Modules & Imports
Lesson.objects.update_or_create(
    chapter=ch4, 
    title="模块与导入", 
    defaults={
        'content': """
## 什么是模块 (Module)？

一个 `.py` 文件就是一个模块。模块可以包含函数、变量和类。
你可以将代码组织到不同的模块中，然后在其他地方**导入** (import) 使用。

### 导入模块
假设你有一个 `vsearch.py` 文件，里面定义了 `search4vowels` 函数。

```python
import vsearch

vsearch.search4vowels("hello")
```

或者你可以直接导入函数：

```python
from vsearch import search4vowels

search4vowels("hello")
```

### 标准库 (Standard Library)
Python 自带了大量的标准库模块，例如 `random` (随机数), `math` (数学), `datetime` (日期时间) 等。

```python
import random
print(random.randint(1, 10))
```
    """,
        'lesson_type': 'text',
        'order': 3
    }
)

print("完整课程数据（第1-4章）填充/更新完成！")
