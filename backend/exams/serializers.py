from rest_framework import serializers
from .models import Exam, Question, UserExamAttempt, UserAnswer


class ExamListSerializer(serializers.ModelSerializer):
    """考试列表（不含题目详情）"""
    question_count = serializers.IntegerField(read_only=True)
    has_attempted = serializers.SerializerMethodField()
    best_score = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = [
            'id', 'title', 'description', 'duration_minutes',
            'total_score', 'passing_score', 'question_count',
            'has_attempted', 'best_score', 'created_at',
        ]

    def get_has_attempted(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.attempts.filter(user=user).exists()
        return False

    def get_best_score(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            best = obj.attempts.filter(user=user).order_by('-score').first()
            return best.score if best else None
        return None


class QuestionSerializer(serializers.ModelSerializer):
    """试题（不含正确答案，用于考试进行中）"""
    question = serializers.CharField(source='content')

    class Meta:
        model = Question
        fields = ['id', 'question_number', 'question_type', 'question',
                  'option_a', 'option_b', 'option_c', 'option_d']


class ExamDetailSerializer(serializers.ModelSerializer):
    """考试详情（含题目，不含答案）"""
    questions = QuestionSerializer(many=True, read_only=True)
    question_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Exam
        fields = [
            'id', 'title', 'description', 'duration_minutes',
            'total_score', 'passing_score', 'question_count',
            'questions', 'created_at',
        ]


class ExamSubmitSerializer(serializers.Serializer):
    """提交答案的请求格式"""
    answers = serializers.DictField(
        child=serializers.CharField(),
        help_text="key 为题号（字符串），value 为用户选择的答案"
    )


class ExamResultSerializer(serializers.ModelSerializer):
    """考试结果"""
    questions = serializers.SerializerMethodField()
    totalQuestions = serializers.IntegerField(source='total_questions')
    correctCount = serializers.IntegerField(source='correct_count')

    class Meta:
        model = UserExamAttempt
        fields = [
            'id', 'exam', 'score', 'totalQuestions', 'correctCount',
            'is_passed', 'started_at', 'submitted_at', 'questions',
        ]

    def get_questions(self, obj):
        """返回题目及答案解析"""
        result = []
        for answer in obj.answers.select_related('question').all():
            q = answer.question
            options = []
            for key in ['A', 'B', 'C', 'D']:
                opt_text = getattr(q, f'option_{key.lower()}', '')
                if opt_text:
                    options.append({'key': key, 'text': opt_text})
            result.append({
                'question': q.content,
                'options': options,
                'answer': q.correct_answer,
                'userAnswer': answer.selected_answer,
                'isCorrect': answer.is_correct,
                'explanation': q.explanation,
            })
        return result
