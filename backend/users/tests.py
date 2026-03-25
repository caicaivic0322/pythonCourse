from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from courses.models import Chapter, Course, Lesson, UserCourseProgress, UserLessonProgress


User = get_user_model()


class AdminUserProgressTests(TestCase):
    def setUp(self):
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpass123',
        )
        self.student = User.objects.create_user(
            username='student_one',
            email='student@example.com',
            password='studentpass123',
            is_approved=True,
        )
        self.student_two = User.objects.create_user(
            username='student_two',
            email='student_two@example.com',
            password='studentpass123',
            is_approved=True,
        )
        self.student_three = User.objects.create_user(
            username='student_three',
            email='student_three@example.com',
            password='studentpass123',
            is_approved=True,
        )
        self.student_four = User.objects.create_user(
            username='student_four',
            email='student_four@example.com',
            password='studentpass123',
            is_approved=True,
        )

        course = Course.objects.create(
            title='Admin Test Course',
            description='Course used for admin progress tests.',
            order=1,
        )
        chapter = Chapter.objects.create(
            course=course,
            title='Chapter 1',
            order=1,
        )

        scores = [100, 95, 88, 72, 60, 55, 40]
        lessons = []
        for index, score in enumerate(scores, start=1):
            lesson = Lesson.objects.create(
                chapter=chapter,
                title=f'Lesson {index}',
                order=index,
                lesson_type='text',
                content='test',
            )
            lessons.append(lesson)
            UserLessonProgress.objects.create(
                user=self.student,
                lesson=lesson,
                is_completed=True,
                score=score,
            )

        UserCourseProgress.objects.create(
            user=self.student,
            course=course,
            current_lesson=lessons[-1],
            is_completed=False,
        )

        self.matrix_lessons = []
        for index in range(1, 5):
            self.matrix_lessons.append(
                Lesson.objects.create(
                    chapter=chapter,
                    title=f'Matrix Lesson {index}',
                    order=100 + index,
                    lesson_type='quiz',
                    content='matrix',
                )
            )

        matrix_data = {
            self.student: [90, 80, 70, 60],
            self.student_two: [85, 75, 65, None],
            self.student_three: [95, 88, 55, None],
            self.student_four: [78, None, 40, None],
        }

        for user, values in matrix_data.items():
            for lesson, score in zip(self.matrix_lessons, values):
                if score is None:
                    continue
                UserLessonProgress.objects.create(
                    user=user,
                    lesson=lesson,
                    is_completed=True,
                    score=score,
                )

    def test_admin_user_change_page_shows_ranked_lesson_scores(self):
        self.client.force_login(self.admin_user)

        response = self.client.get(reverse('admin:users_user_change', args=[self.student.pk]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '学习进度')
        self.assertContains(response, 'Lesson 1')
        self.assertContains(response, 'Lesson 7')
        self.assertContains(response, 'score-pill score-top', count=3, html=False)
        self.assertContains(response, 'score-pill score-bottom', count=3, html=False)
        self.assertContains(response, 'score-pill score-neutral', count=5, html=False)

    def test_admin_user_list_page_shows_progress_snapshot(self):
        self.client.force_login(self.admin_user)

        response = self.client.get(reverse('admin:users_user_changelist'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '课程 1')
        self.assertContains(response, '小节 11')

    def test_admin_score_matrix_only_shows_lessons_with_75_percent_participation(self):
        self.client.force_login(self.admin_user)

        response = self.client.get(reverse('admin:users_user_score_matrix'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '成绩总表')
        self.assertContains(response, 'Matrix Lesson 1')
        self.assertContains(response, 'Matrix Lesson 2')
        self.assertContains(response, 'Matrix Lesson 3')
        self.assertNotContains(response, 'Matrix Lesson 4')
        self.assertContains(response, 'student_one')
        self.assertContains(response, 'student_four')
        self.assertContains(response, 'matrix-score score-top', count=9, html=False)
        self.assertContains(response, 'matrix-score score-bottom', count=2, html=False)


class CustomAuthTokenTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='student_login',
            email='student_login@example.com',
            password='studentpass123',
            is_approved=True,
        )

    def test_login_accepts_email_address(self):
        response = self.client.post(
            '/api/users/login/',
            {
                'username': 'student_login@example.com',
                'password': 'studentpass123',
            },
            format='json',
        )

        self.assertEqual(response.status_code, 200)
        self.assertIn('token', response.data)
        self.assertEqual(response.data['username'], 'student_login')


class UserStatsViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='stats_user',
            email='stats@example.com',
            password='studentpass123',
            is_approved=True,
        )
        self.course = Course.objects.create(
            title='Stats Course',
            description='Course used for stats tests.',
            order=1,
        )
        self.chapter = Chapter.objects.create(
            course=self.course,
            title='Stats Chapter',
            order=1,
        )
        self.lesson_one = Lesson.objects.create(
            chapter=self.chapter,
            title='Lesson 1',
            order=1,
            lesson_type='text',
            content='content',
        )
        self.lesson_two = Lesson.objects.create(
            chapter=self.chapter,
            title='Lesson 2',
            order=2,
            lesson_type='quiz',
            content='content',
        )

        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson_one,
            is_completed=True,
            score=100,
        )
        UserLessonProgress.objects.create(
            user=self.user,
            lesson=self.lesson_two,
            is_completed=True,
            score=80,
        )
        UserCourseProgress.objects.create(
            user=self.user,
            course=self.course,
            current_lesson=self.lesson_two,
            is_completed=False,
        )

        self.client.force_authenticate(user=self.user)

    def test_stats_endpoint_returns_aggregated_learning_metrics(self):
        response = self.client.get('/api/users/stats/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['xp'], 180)
        self.assertEqual(response.data['badges'], 0)
        self.assertEqual(response.data['courses_learned'], 1)
        self.assertEqual(response.data['study_hours'], 0.7)
