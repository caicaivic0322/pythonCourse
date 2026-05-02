from django.db import models
from django.conf import settings


class Exam(models.Model):
    title = models.CharField(max_length=200, verbose_name="考试标题")
    description = models.TextField(blank=True, verbose_name="考试描述")
    duration_minutes = models.PositiveIntegerField(default=60, verbose_name="考试时长（分钟）")
    total_score = models.PositiveIntegerField(default=100, verbose_name="满分")
    passing_score = models.PositiveIntegerField(default=60, help_text="及格百分比，例如 60 表示 60%", verbose_name="及格线")
    is_published = models.BooleanField(default=False, verbose_name="已发布")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "考试"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

    @property
    def question_count(self):
        return self.questions.count()


class Question(models.Model):
    QUESTION_TYPES = (
        ('single_choice', '单选题'),
        ('multiple_choice', '多选题'),
        ('true_false', '判断题'),
    )

    exam = models.ForeignKey(Exam, related_name='questions', on_delete=models.CASCADE, verbose_name="所属考试")
    question_number = models.PositiveIntegerField(verbose_name="题号")
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='single_choice', verbose_name="题目类型")
    content = models.TextField(verbose_name="题目内容")
    option_a = models.CharField(max_length=500, blank=True, verbose_name="选项 A")
    option_b = models.CharField(max_length=500, blank=True, verbose_name="选项 B")
    option_c = models.CharField(max_length=500, blank=True, verbose_name="选项 C")
    option_d = models.CharField(max_length=500, blank=True, verbose_name="选项 D")
    correct_answer = models.CharField(max_length=10, verbose_name="正确答案")
    explanation = models.TextField(blank=True, verbose_name="答案解析")
    score = models.PositiveIntegerField(default=5, verbose_name="分值")

    class Meta:
        ordering = ['question_number']
        unique_together = ('exam', 'question_number')
        verbose_name = "试题"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"第{self.question_number}题 - {self.exam.title[:20]}"


class UserExamAttempt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='exam_attempts', verbose_name="用户")
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='attempts', verbose_name="考试")
    started_at = models.DateTimeField(auto_now_add=True, verbose_name="开始时间")
    submitted_at = models.DateTimeField(null=True, blank=True, verbose_name="提交时间")
    score = models.IntegerField(default=0, verbose_name="得分")
    total_questions = models.IntegerField(default=0, verbose_name="总题数")
    correct_count = models.IntegerField(default=0, verbose_name="答对题数")
    is_passed = models.BooleanField(default=False, verbose_name="是否及格")

    class Meta:
        ordering = ['-started_at']
        verbose_name = "用户考试记录"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.user.username} - {self.exam.title}"


class UserAnswer(models.Model):
    attempt = models.ForeignKey(UserExamAttempt, on_delete=models.CASCADE, related_name='answers', verbose_name="考试记录")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="试题")
    selected_answer = models.CharField(max_length=10, verbose_name="用户答案")
    is_correct = models.BooleanField(default=False, verbose_name="是否正确")

    class Meta:
        unique_together = ('attempt', 'question')
        verbose_name = "用户答案"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.attempt.user.username} - 第{self.question.question_number}题"
