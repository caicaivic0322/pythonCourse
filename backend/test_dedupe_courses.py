from django.test import TestCase

from courses.models import Course
from dedupe_courses import choose_keep_course


class DedupeCoursesTests(TestCase):
    def test_choose_keep_course_supports_explicit_keep_order(self):
        course2 = Course.objects.create(title='GESP 2级：逻辑进阶', description='old', order=2)
        course3 = Course.objects.create(title='GESP 2级：逻辑进阶', description='new', order=3)

        keep_course = choose_keep_course([course2, course3], keep_order=3)

        self.assertEqual(keep_course.id, course3.id)
