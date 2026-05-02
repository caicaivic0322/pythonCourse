from datetime import timezone

from django.shortcuts import get_object_or_404
from django.utils import timezone as django_timezone
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.throttling import ScopedRateThrottle

from .models import Exam, Question, UserExamAttempt, UserAnswer
from .serializers import (
    ExamListSerializer,
    ExamDetailSerializer,
    ExamSubmitSerializer,
    ExamResultSerializer,
)


class ExamListView(generics.ListAPIView):
    """已发布考试列表"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExamListSerializer

    def get_queryset(self):
        return Exam.objects.filter(is_published=True)


class ExamDetailView(generics.RetrieveAPIView):
    """考试详情（包含题目，不含答案）"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExamDetailSerializer

    def get_queryset(self):
        return Exam.objects.filter(is_published=True)


class ExamStartView(APIView):
    """开始考试——创建一次考试记录"""
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk, is_published=True)

        # 检查是否已有未提交的考试（可以续考）
        existing = UserExamAttempt.objects.filter(
            user=request.user,
            exam=exam,
            submitted_at__isnull=True,
        ).first()

        if existing:
            return Response({
                'attempt_id': existing.id,
                'started_at': existing.started_at,
                'message': '继续之前的考试',
            })

        attempt = UserExamAttempt.objects.create(
            user=request.user,
            exam=exam,
            total_questions=exam.questions.count(),
        )

        return Response({
            'attempt_id': attempt.id,
            'started_at': attempt.started_at,
            'message': '考试开始',
        }, status=status.HTTP_201_CREATED)


class ExamSubmitView(APIView):
    """提交考试答案并自动评分"""
    permission_classes = [permissions.IsAuthenticated]
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'exam_submit'

    def post(self, request, pk):
        exam = get_object_or_404(Exam, pk=pk, is_published=True)
        serializer = ExamSubmitSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        answers_data = serializer.validated_data['answers']  # {"1": "A", "2": "B", ...}

        # 查找或创建考试记录
        attempt = UserExamAttempt.objects.filter(
            user=request.user,
            exam=exam,
            submitted_at__isnull=True,
        ).first()

        if not attempt:
            attempt = UserExamAttempt.objects.create(
                user=request.user,
                exam=exam,
                total_questions=exam.questions.count(),
            )

        # 检查是否超时
        questions = exam.questions.all().order_by('question_number')
        total_score = 0
        correct_count = 0

        for question in questions:
            q_num = str(question.question_number)
            selected = answers_data.get(q_num, '').strip().upper()
            # 标准化答案比较：多选题排序后比较，单选/判断直接比较
            correct = self._check_answer(question, selected)

            if correct:
                correct_count += 1
                total_score += question.score

            UserAnswer.objects.update_or_create(
                attempt=attempt,
                question=question,
                defaults={
                    'selected_answer': selected or '',
                    'is_correct': correct,
                },
            )

        # 更新考试记录
        passing_threshold = exam.total_score * exam.passing_score / 100
        attempt.score = total_score
        attempt.correct_count = correct_count
        attempt.is_passed = total_score >= passing_threshold
        attempt.submitted_at = django_timezone.now()
        attempt.save()

        # 返回结果
        result_serializer = ExamResultSerializer(attempt, context={'request': request})
        return Response(result_serializer.data)

    def _check_answer(self, question, selected):
        """比较用户答案和正确答案"""
        if not selected:
            return False

        correct = question.correct_answer.strip().upper()

        if question.question_type == 'multiple_choice':
            # 多选题：排序后逐字符比较
            return ''.join(sorted(selected)) == ''.join(sorted(correct))

        # 单选题、判断题：直接比较
        return selected == correct


class ExamResultView(generics.RetrieveAPIView):
    """查看考试结果"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExamResultSerializer

    def get_queryset(self):
        return UserExamAttempt.objects.filter(
            user=self.request.user,
            submitted_at__isnull=False,
        )


class ExamHistoryView(generics.ListAPIView):
    """用户的考试历史"""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ExamResultSerializer

    def get_queryset(self):
        return UserExamAttempt.objects.filter(
            user=self.request.user,
            submitted_at__isnull=False,
        ).order_by('-submitted_at')
