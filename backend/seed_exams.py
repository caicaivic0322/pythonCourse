"""
考试模块种子数据
用法: python manage.py seed_exams
"""
import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from exams.models import Exam, Question


EXAMS = [
    {
        'title': 'GESP 一级模拟考试',
        'description': '覆盖 Python 基础语法、变量、数据类型和输入输出的综合测试。',
        'duration_minutes': 30,
        'passing_score': 60,
        'questions': [
            {
                'question_type': 'single_choice',
                'content': '在 Python 中，以下哪个是正确的变量命名？',
                'option_a': '2name',
                'option_b': 'my_name',
                'option_c': 'my-name',
                'option_d': 'class',
                'correct_answer': 'B',
                'explanation': 'Python 变量名只能以字母或下划线开头，不能以数字开头、不能包含连字符、不能使用关键字。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '运行 print(type(3.14)) 会输出什么？',
                'option_a': "<class 'int'>",
                'option_b': "<class 'float'>",
                'option_c': "<class 'str'>",
                'option_d': "<class 'bool'>",
                'correct_answer': 'B',
                'explanation': '3.14 是小数，Python 中属于 float（浮点数）类型。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '以下代码的运行结果是？\n\nx = 5\ny = 2\nprint(x // y)',
                'option_a': '2.5',
                'option_b': '2',
                'option_c': '10',
                'option_d': '3',
                'correct_answer': 'B',
                'explanation': '// 是整除运算符，5 // 2 = 2（向下取整）。',
                'score': 10,
            },
            {
                'question_type': 'true_false',
                'content': '在 Python 中，input() 函数返回的数据类型始终是字符串。',
                'option_a': '正确',
                'option_b': '错误',
                'option_c': '',
                'option_d': '',
                'correct_answer': 'A',
                'explanation': 'input() 读取用户输入后总是返回 str 类型，需要时要用 int() 或 float() 转换。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': 'print("Hello" + " " + "World") 的输出是什么？',
                'option_a': 'Hello World',
                'option_b': 'HelloWorld',
                'option_c': 'Hello + World',
                'option_d': '报错',
                'correct_answer': 'A',
                'explanation': '字符串可以用 + 拼接，中间空格 " " 也被拼接进去。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '以下哪个语句可以用来输出 "Python 很有趣"？',
                'option_a': 'input("Python 很有趣")',
                'option_b': 'print("Python 很有趣")',
                'option_c': 'echo "Python 很有趣"',
                'option_d': 'output("Python 很有趣")',
                'correct_answer': 'B',
                'explanation': 'Python 中使用 print() 函数输出内容到控制台。',
                'score': 10,
            },
            {
                'question_type': 'true_false',
                'content': '在 Python 中，单行注释使用 # 符号。',
                'option_a': '正确',
                'option_b': '错误',
                'option_c': '',
                'option_d': '',
                'correct_answer': 'A',
                'explanation': '# 开头的行是注释，Python 解释器会忽略这些内容。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '以下哪个是正确的赋值语句？',
                'option_a': 'x = 10',
                'option_b': '10 = x',
                'option_c': 'x == 10',
                'option_d': 'x := 10',
                'correct_answer': 'A',
                'explanation': 'Python 中赋值使用 =，变量名在左边，值在右边。== 是比较运算符。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': 'len("Python") 的返回值是多少？',
                'option_a': '5',
                'option_b': '6',
                'option_c': '7',
                'option_d': '0',
                'correct_answer': 'B',
                'explanation': "'Python' 这个字符串共 6 个字符。",
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '运行以下代码的结果是？\n\na = 3\nb = 4\nprint(a * b)',
                'option_a': '7',
                'option_b': '12',
                'option_c': '34',
                'option_d': '1',
                'correct_answer': 'B',
                'explanation': '* 是乘法运算符，3 * 4 = 12。',
                'score': 10,
            },
        ],
    },
    {
        'title': 'GESP 二级模拟考试',
        'description': '覆盖条件判断、循环结构和逻辑运算的综合测试。',
        'duration_minutes': 45,
        'passing_score': 60,
        'questions': [
            {
                'question_type': 'single_choice',
                'content': '运行以下代码的结果是？\n\nx = 10\nif x > 5:\n    print("大")\nelse:\n    print("小")',
                'option_a': '大',
                'option_b': '小',
                'option_c': '大小',
                'option_d': '报错',
                'correct_answer': 'A',
                'explanation': '10 > 5 为 True，所以执行 if 分支，输出"大"。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': 'for i in range(3): print(i) 会依次输出什么？',
                'option_a': '1 2 3',
                'option_b': '0 1 2',
                'option_c': '0 1 2 3',
                'option_d': '1 2',
                'correct_answer': 'B',
                'explanation': 'range(3) 从 0 开始，生成 0, 1, 2 三个数。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '以下哪个运算符表示"逻辑与"？',
                'option_a': 'and',
                'option_b': 'or',
                'option_c': 'not',
                'option_d': '&',
                'correct_answer': 'A',
                'explanation': 'Python 中逻辑与用 and，逻辑或用 or，逻辑非用 not。& 是位运算符。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': 'while 循环的条件为 False 时会怎样？',
                'option_a': '循环执行一次后退出',
                'option_b': '直接跳过，不执行循环体',
                'option_c': '无限循环',
                'option_d': '报错',
                'correct_answer': 'B',
                'explanation': 'while 循环在条件为 True 时执行，条件为 False 时直接跳过循环体。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '运行以下代码，最终 x 的值是多少？\n\nx = 0\nfor i in range(1, 4):\n    x += i\nprint(x)',
                'option_a': '4',
                'option_b': '5',
                'option_c': '6',
                'option_d': '10',
                'correct_answer': 'C',
                'explanation': '循环 3 次：x = 0 + 1 = 1, x = 1 + 2 = 3, x = 3 + 3 = 6。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '以下代码输出什么？\n\nfor c in "AB":\n    print(c, end="")',
                'option_a': 'AB',
                'option_b': 'A B',
                'option_c': "A\\nB",
                'option_d': '报错',
                'correct_answer': 'A',
                'explanation': '遍历字符串"AB"逐个输出字符，end="" 取消换行，结果是 AB 连在一起。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': 'True and False 的结果是什么？',
                'option_a': 'True',
                'option_b': 'False',
                'option_c': 'None',
                'option_d': '0',
                'correct_answer': 'B',
                'explanation': 'and 运算要求两边都为 True 才返回 True，有一边为 False 就返回 False。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': 'if x > 0 and x < 10 表示什么条件？',
                'option_a': 'x 大于 0 或小于 10',
                'option_b': 'x 大于 0 且小于 10',
                'option_c': 'x 等于 0 或等于 10',
                'option_d': 'x 在 0 到 10 之外',
                'correct_answer': 'B',
                'explanation': 'and 连接两个条件，要求两个都满足，即 x 在 (0, 10) 之间。',
                'score': 10,
            },
            {
                'question_type': 'true_false',
                'content': 'break 语句可以用来提前终止循环。',
                'option_a': '正确',
                'option_b': '错误',
                'option_c': '',
                'option_d': '',
                'correct_answer': 'A',
                'explanation': 'break 立即退出循环；continue 跳过当前迭代进入下一轮。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '以下代码输出什么？\n\nfor i in range(1, 6):\n    if i == 3:\n        continue\n    print(i, end=" ")',
                'option_a': '1 2 3 4 5',
                'option_b': '1 2 4 5',
                'option_c': '3',
                'option_d': '1 2',
                'correct_answer': 'B',
                'explanation': 'continue 跳过 i==3 时的输出，其余数字正常打印。',
                'score': 10,
            },
        ],
    },
    {
        'title': 'GESP 三级模拟考试',
        'description': '覆盖列表、元组、字符串操作和数据结构的综合测试。',
        'duration_minutes': 45,
        'passing_score': 60,
        'questions': [
            {
                'question_type': 'single_choice',
                'content': '以下哪个是创建列表的正确语法？',
                'option_a': 'list = {1, 2, 3}',
                'option_b': 'list = [1, 2, 3]',
                'option_c': 'list = (1, 2, 3)',
                'option_d': 'list = <1, 2, 3>',
                'correct_answer': 'B',
                'explanation': '列表用方括号 [] 创建。{} 是字典或集合，() 是元组。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': 'nums = [1, 2, 3]\nnums.append(4)\nprint(nums) 输出什么？',
                'option_a': '[1, 2, 3]',
                'option_b': '[1, 2, 3, 4]',
                'option_c': '[4, 1, 2, 3]',
                'option_d': '报错',
                'correct_answer': 'B',
                'explanation': 'append() 将元素添加到列表末尾。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '以下代码输出什么？\n\nt = (1, 2, 3)\nt[0] = 10\nprint(t)',
                'option_a': '(10, 2, 3)',
                'option_b': '(1, 2, 3)',
                'option_c': '报错',
                'option_d': '[10, 2, 3]',
                'correct_answer': 'C',
                'explanation': '元组是不可变的，不能修改其中的元素，尝试修改会报 TypeError。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': 's = "hello world"\nprint(s[0:5]) 输出什么？',
                'option_a': 'hello',
                'option_b': 'world',
                'option_c': 'hell',
                'option_d': 'ello',
                'correct_answer': 'A',
                'explanation': '切片 [0:5] 取索引 0 到 4 的字符，即 "hello"。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '以下哪个方法可以从列表中移除指定元素？',
                'option_a': 'add()',
                'option_b': 'delete()',
                'option_c': 'remove()',
                'option_d': 'discard()',
                'correct_answer': 'C',
                'explanation': 'remove(x) 删除列表中第一个值为 x 的元素。add() 和 discard() 是集合方法。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '运行以下代码，结果是什么？\n\nlst = [1, 2, 3]\nprint(lst[-1])',
                'option_a': '1',
                'option_b': '2',
                'option_c': '3',
                'option_d': '报错',
                'correct_answer': 'C',
                'explanation': '负索引从列表末尾开始，-1 表示最后一个元素。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '字符串 "abc def".split() 的结果是什么？',
                'option_a': "['a', 'b', 'c', ' ', 'd', 'e', 'f']",
                'option_b': "['abc', 'def']",
                'option_c': "['abc def']",
                'option_d': "'abcdef'",
                'correct_answer': 'B',
                'explanation': 'split() 默认按空白字符分割字符串，返回列表。',
                'score': 10,
            },
            {
                'question_type': 'true_false',
                'content': '列表的索引是从 1 开始的。',
                'option_a': '正确',
                'option_b': '错误',
                'option_c': '',
                'option_d': '',
                'correct_answer': 'B',
                'explanation': 'Python 列表索引从 0 开始，第一个元素的索引是 0。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': 'len([1, 2, 3, 4, 5]) 返回什么？',
                'option_a': '5',
                'option_b': '4',
                'option_c': '6',
                'option_d': '0',
                'correct_answer': 'A',
                'explanation': 'len() 返回列表中的元素个数，这里有 5 个元素。',
                'score': 10,
            },
            {
                'question_type': 'single_choice',
                'content': '以下代码输出什么？\n\ncolors = ["红", "蓝", "绿"]\ncolors.insert(1, "黄")\nprint(colors)',
                'option_a': "['黄', '红', '蓝', '绿']",
                'option_b': "['红', '黄', '蓝', '绿']",
                'option_c': "['红', '蓝', '绿', '黄']",
                'option_d': '报错',
                'correct_answer': 'B',
                'explanation': 'insert(1, "黄") 在索引 1 处插入"黄"，原有元素后移。',
                'score': 10,
            },
        ],
    },
]


def seed():
    created = 0
    updated = 0

    for exam_data in EXAMS:
        questions_data = exam_data.pop('questions')
        exam, is_new = Exam.objects.update_or_create(
            title=exam_data['title'],
            defaults={**exam_data, 'is_published': True},
        )
        if is_new:
            created += 1
        else:
            updated += 1

        total_score = 0
        for i, q_data in enumerate(questions_data, start=1):
            q_data['question_number'] = i
            Question.objects.update_or_create(
                exam=exam,
                question_number=i,
                defaults=q_data,
            )
            total_score += q_data['score']

        # 更新总分
        exam.total_score = total_score
        exam.save()

        # 删除多余的旧题目
        Question.objects.filter(exam=exam, question_number__gt=len(questions_data)).delete()

    print(f'考试种子数据完成: 新建 {created}, 更新 {updated}')


if __name__ == '__main__':
    seed()
