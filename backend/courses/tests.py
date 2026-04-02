from django.contrib.auth import get_user_model
from django.urls import reverse
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
