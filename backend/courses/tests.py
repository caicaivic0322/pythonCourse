from django.contrib.auth import get_user_model
from django.urls import reverse
from pathlib import Path
import runpy
from rest_framework.test import APITestCase

from .models import Chapter, Course, Lesson, UserCourseProgress, UserLessonProgress


User = get_user_model()


class CourseUnlockLogicTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='student',
            password='pass12345',
            is_approved=True,
        )
        self.client.force_authenticate(self.user)

    def test_course_list_keeps_access_to_started_course_and_newly_inserted_previous_course(self):
        course1 = Course.objects.create(title='Course 1', description='d1', order=1)
        course2 = Course.objects.create(title='Course 2', description='d2', order=2)
        course3 = Course.objects.create(title='Course 3', description='d3', order=3)

        chapter1 = Chapter.objects.create(course=course1, title='Chapter 1', order=1)
        chapter3 = Chapter.objects.create(course=course3, title='Chapter 1', order=1)
        lesson1 = Lesson.objects.create(chapter=chapter1, title='Lesson 1', order=1)
        lesson3 = Lesson.objects.create(chapter=chapter3, title='Lesson 1', order=1)

        UserCourseProgress.objects.create(
            user=self.user,
            course=course1,
            is_completed=True,
            current_lesson=lesson1,
        )
        UserCourseProgress.objects.create(
            user=self.user,
            course=course3,
            is_completed=False,
            current_lesson=lesson3,
        )

        response = self.client.get('/api/courses/')

        self.assertEqual(response.status_code, 200)
        payload = {item['id']: item for item in response.data}
        self.assertFalse(payload[course2.id]['is_locked'])
        self.assertFalse(payload[course3.id]['is_locked'])

    def test_course_detail_keeps_access_to_started_lesson_and_newly_inserted_previous_lesson(self):
        course = Course.objects.create(title='Course', description='desc', order=1)
        chapter = Chapter.objects.create(course=course, title='Chapter 1', order=1)
        lesson1 = Lesson.objects.create(chapter=chapter, title='Lesson 1', order=1)
        lesson2 = Lesson.objects.create(chapter=chapter, title='Lesson 2', order=2)
        lesson3 = Lesson.objects.create(chapter=chapter, title='Lesson 3', order=3)

        UserLessonProgress.objects.create(user=self.user, lesson=lesson1, is_completed=True, score=100)
        UserLessonProgress.objects.create(user=self.user, lesson=lesson3, is_completed=False, score=0)

        response = self.client.get(f'/api/courses/{course.id}/')

        self.assertEqual(response.status_code, 200)
        lessons = response.data['chapters'][0]['lessons']
        lessons_by_id = {lesson['id']: lesson for lesson in lessons}
        self.assertFalse(lessons_by_id[lesson2.id]['is_locked'])
        self.assertFalse(lessons_by_id[lesson3.id]['is_locked'])


class CourseSeedContentTests(APITestCase):
    def test_gesp2_string_chapter_has_richer_lesson_count(self):
        seed_path = Path(__file__).resolve().parents[1] / 'seed_gesp_courses.py'
        runpy.run_path(str(seed_path), run_name='__main__')

        course = Course.objects.get(title='GESP 2级：逻辑进阶')
        chapter1 = Chapter.objects.get(course=course, title='第1章：列表 List')
        chapter = Chapter.objects.get(course=course, title='第2章：字符串进阶')
        chapter3 = Chapter.objects.get(course=course, title='第3章：常见数据结构')

        self.assertGreaterEqual(chapter.lessons.count(), 4)

        # Chapter 1
        lesson_11 = Lesson.objects.get(chapter=chapter1, title='1.1 列表的定义与索引')
        lesson_12 = Lesson.objects.get(chapter=chapter1, title='1.2 列表的增删改查')
        self.assertIn('## 6. 引用与拷贝', lesson_11.content)
        self.assertIn('## 6. append vs extend', lesson_12.content)

        lesson_21 = Lesson.objects.get(chapter=chapter, title='2.1 字符串常用方法')
        lesson_22 = Lesson.objects.get(chapter=chapter, title='2.2 字符与编码 (ASCII)')
        lesson_23 = Lesson.objects.get(chapter=chapter, title='2.3 字符串切片与格式化输出')
        lesson_24 = Lesson.objects.get(chapter=chapter, title='2.4 综合实战：整理学生成绩字符串')

        self.assertIn('## 9. 方法组合思维', lesson_21.content)
        self.assertIn('## 9. 编码与排序的关系', lesson_22.content)
        self.assertIn('## 7. 宽度与对齐', lesson_23.content)
        self.assertIn('## 7. 升级任务：生成成绩报告', lesson_24.content)

        # Chapter 3
        lesson_31 = Lesson.objects.get(chapter=chapter3, title='3.1 元组 Tuple：不能随意修改的序列')
        lesson_32 = Lesson.objects.get(chapter=chapter3, title='3.2 字典 Dictionary：用名字找数据')
        lesson_33 = Lesson.objects.get(chapter=chapter3, title='3.3 集合 Set：自动去重的容器')
        lesson_35 = Lesson.objects.get(chapter=chapter3, title='3.5 综合实战：班级选课信息整理')
        self.assertIn('## 7. 元组解包', lesson_31.content)
        self.assertIn('## 7. get 与 KeyError', lesson_32.content)
        self.assertIn('## 6. add/remove/discard', lesson_33.content)
        self.assertIn('## 6. 升级任务：最受欢迎课程', lesson_35.content)

        course3 = Course.objects.get(title='GESP 3级：函数与模块')
        lesson_311 = Lesson.objects.get(chapter__course=course3, title='1.1 函数定义与返回值')
        lesson_321 = Lesson.objects.get(chapter__course=course3, title='2.1 元组进阶：解包、返回值与不可变数据')
        lesson_322 = Lesson.objects.get(chapter__course=course3, title='2.2 异常处理 try-except')
        lesson_333 = Lesson.objects.get(chapter__course=course3, title='3.3 自定义模块与代码拆分')
        self.assertIn('## 4. return 与 print 的区别', lesson_311.content)
        self.assertIn('## 0. 和 GESP 2级有什么不同？', lesson_321.content)
        self.assertIn('## 4. 精准捕获 vs 一把抓', lesson_322.content)
        self.assertIn('## 5. 为什么不要把所有函数都塞进 main.py', lesson_333.content)

        course4 = Course.objects.get(title='GESP 4级：数据结构进阶')
        lesson_411 = Lesson.objects.get(chapter__course=course4, title='1.1 字典进阶：嵌套、计数与数据建模')
        lesson_412 = Lesson.objects.get(chapter__course=course4, title='1.2 集合进阶：关系运算与去重策略')
        lesson_421 = Lesson.objects.get(chapter__course=course4, title='2.1 类与对象基础')
        lesson_422 = Lesson.objects.get(chapter__course=course4, title='2.2 构造函数 __init__')
        self.assertIn('## 0. 和 GESP 2级有什么不同？', lesson_411.content)
        self.assertIn('## 8. 计数问题：字典高频应用', lesson_411.content)
        self.assertIn('## 0. 和 GESP 2级有什么不同？', lesson_412.content)
        self.assertIn('## 10. 综合练习：班级选课分析', lesson_412.content)
        self.assertIn('## 5. self 到底是什么？', lesson_421.content)
        self.assertIn('## 9. 易错点', lesson_421.content)
        self.assertIn('## 3. 参数和属性不要混淆', lesson_422.content)
        self.assertIn('## 10. 综合练习：BankAccount', lesson_422.content)

        head_first = Course.objects.get(title='Head First Python')
        hf_list = Lesson.objects.get(chapter__course=head_first, title='2.1 项目实践：电影列表建模')
        hf_dict = Lesson.objects.get(chapter__course=head_first, title='3.1 项目实践：电影信息字典')
        hf_fn = Lesson.objects.get(chapter__course=head_first, title='4.1 项目实践：print_lol 递归函数')
        hf_module = Lesson.objects.get(chapter__course=head_first, title='4.2 项目实践：封装 nester.py 模块')
        self.assertIn('## 0. 和 GESP 2级列表有什么不同？', hf_list.content)
        self.assertIn('## 0. 和前面字典课程有什么不同？', hf_dict.content)
        self.assertIn('## 0. 和 GESP 函数课程有什么不同？', hf_fn.content)
        self.assertIn('## 0. 和 GESP 模块课程有什么不同？', hf_module.content)

        course5 = Course.objects.get(title='GESP 5级：算法基础')
        chapter51 = Chapter.objects.get(course=course5, title='第1章：算法复杂度')
        chapter52 = Chapter.objects.get(course=course5, title='第2章：排序与查找')
        self.assertGreaterEqual(chapter52.lessons.count(), 4)

        lesson_511 = Lesson.objects.get(chapter=chapter51, title='1.1 时间复杂度 Big O')
        lesson_512 = Lesson.objects.get(chapter=chapter51, title='1.2 空间复杂度与复杂度估算')
        lesson_521 = Lesson.objects.get(chapter=chapter52, title='2.1 冒泡排序 Bubble Sort')
        lesson_522 = Lesson.objects.get(chapter=chapter52, title='2.2 二分查找 Binary Search')
        lesson_523 = Lesson.objects.get(chapter=chapter52, title='2.3 选择排序 Selection Sort')
        lesson_524 = Lesson.objects.get(chapter=chapter52, title='2.4 插入排序 Insertion Sort')

        self.assertIn('## 4. 为什么不看“跑了几秒”', lesson_511.content)
        self.assertIn('## 4. 常见空间复杂度直觉', lesson_512.content)
        self.assertIn('## 4. 一轮一轮发生了什么', lesson_521.content)
        self.assertIn('## 4. 为什么必须有序', lesson_522.content)
        self.assertIn('## 4. 和冒泡排序有什么区别', lesson_523.content)
        self.assertIn('## 4. 为什么叫“插入”', lesson_524.content)
