from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token

from .models import Exam, Question, UserExamAttempt

User = get_user_model()


class ExamModelTests(TestCase):
    """考试模型基础测试"""

    def setUp(self):
        self.exam = Exam.objects.create(
            title='测试考试',
            duration_minutes=30,
            total_score=100,
            passing_score=60,
            is_published=True,
        )
        self.q1 = Question.objects.create(
            exam=self.exam, question_number=1,
            question_type='single_choice',
            content='1+1等于几？',
            option_a='1', option_b='2', option_c='3', option_d='4',
            correct_answer='B', score=10,
        )
        self.q2 = Question.objects.create(
            exam=self.exam, question_number=2,
            question_type='true_false',
            content='Python是编译型语言。',
            option_a='正确', option_b='错误',
            correct_answer='B', score=10,
        )
        self.q3 = Question.objects.create(
            exam=self.exam, question_number=3,
            question_type='multiple_choice',
            content='以下哪些是Python关键字？',
            option_a='if', option_b='for', option_c='then', option_d='while',
            correct_answer='ABD', score=10,
        )

    def test_exam_creation(self):
        self.assertEqual(self.exam.title, '测试考试')
        self.assertEqual(self.exam.question_count, 3)

    def test_question_ordering(self):
        questions = list(self.exam.questions.all())
        self.assertEqual(questions[0].question_number, 1)
        self.assertEqual(questions[1].question_number, 2)
        self.assertEqual(questions[2].question_number, 3)

    def test_unpublished_exam_hidden(self):
        hidden = Exam.objects.create(title='隐藏考试', is_published=False)
        published = Exam.objects.filter(is_published=True)
        self.assertIn(self.exam, published)
        self.assertNotIn(hidden, published)


class ExamAPITests(TestCase):
    """考试 API 测试"""

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='teststudent', password='testpass123', is_approved=True,
        )
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

        self.exam = Exam.objects.create(
            title='API测试考试', duration_minutes=30, total_score=100,
            passing_score=60, is_published=True,
        )
        for i, (q_type, answer, score) in enumerate([
            ('single_choice', 'B', 10),
            ('true_false', 'A', 20),
            ('single_choice', 'C', 10),
        ], start=1):
            Question.objects.create(
                exam=self.exam, question_number=i,
                question_type=q_type,
                content=f'题目{i}',
                option_a='A选项', option_b='B选项', option_c='C选项', option_d='D选项',
                correct_answer=answer, score=score,
            )

    def test_list_published_exams(self):
        # 确保未发布的不会出现
        Exam.objects.create(title='隐藏', is_published=False)
        resp = self.client.get('/api/exams/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(len(resp.data), 1)

    def test_exam_detail_with_questions(self):
        resp = self.client.get(f'/api/exams/{self.exam.pk}/')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['title'], 'API测试考试')
        self.assertEqual(len(resp.data['questions']), 3)
        # 不应泄露答案
        self.assertNotIn('correct_answer', resp.data['questions'][0])

    def test_exam_requires_auth(self):
        anon = APIClient()
        resp = anon.get('/api/exams/')
        self.assertEqual(resp.status_code, 401)

    def test_start_exam(self):
        resp = self.client.post(f'/api/exams/{self.exam.pk}/start/')
        self.assertEqual(resp.status_code, 201)
        self.assertIn('attempt_id', resp.data)

    def test_start_exam_resume(self):
        # 第一次开始
        first = self.client.post(f'/api/exams/{self.exam.pk}/start/')
        # 第二次应该续考
        second = self.client.post(f'/api/exams/{self.exam.pk}/start/')
        self.assertEqual(first.data['attempt_id'], second.data['attempt_id'])

    def test_submit_exam_scoring(self):
        self.client.post(f'/api/exams/{self.exam.pk}/start/')
        resp = self.client.post(f'/api/exams/{self.exam.pk}/submit/', {
            'answers': {'1': 'B', '2': 'A', '3': 'C'},
        }, format='json')
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.data['score'], 40)  # 10+20+10
        self.assertEqual(resp.data['correctCount'], 3)
        self.assertEqual(resp.data['is_passed'], False)  # 40% < 60%

    def test_submit_partial_answers(self):
        self.client.post(f'/api/exams/{self.exam.pk}/start/')
        resp = self.client.post(f'/api/exams/{self.exam.pk}/submit/', {
            'answers': {'1': 'B', '2': 'X', '3': 'D'},
        }, format='json')
        self.assertEqual(resp.data['score'], 10)  # only Q1 correct
        self.assertEqual(resp.data['correctCount'], 1)

    def test_result_includes_explanations(self):
        self.client.post(f'/api/exams/{self.exam.pk}/start/')
        resp = self.client.post(f'/api/exams/{self.exam.pk}/submit/', {
            'answers': {'1': 'B', '2': 'A', '3': 'C'},
        }, format='json')
        self.assertEqual(len(resp.data['questions']), 3)
        # 结果应包含正确答案和用户答案
        self.assertIn('answer', resp.data['questions'][0])
        self.assertIn('userAnswer', resp.data['questions'][0])
        self.assertIn('isCorrect', resp.data['questions'][0])
