from django.db import models
from django.conf import settings

class Course(models.Model):
    title = models.CharField(max_length=200, verbose_name="课程标题")
    description = models.TextField(verbose_name="课程描述")
    order = models.PositiveIntegerField(default=0, verbose_name="排序")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        ordering = ['order']
        verbose_name = "课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Chapter(models.Model):
    course = models.ForeignKey(Course, related_name='chapters', on_delete=models.CASCADE, verbose_name="所属课程")
    title = models.CharField(max_length=200, verbose_name="章节标题")
    order = models.PositiveIntegerField(default=0, verbose_name="排序")

    class Meta:
        ordering = ['order']
        verbose_name = "章节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.course.title} - {self.title}"

class Lesson(models.Model):
    LESSON_TYPES = (
        ('text', '图文课程'),
        ('quiz', '测验'),
        ('code', '代码挑战'),
    )
    chapter = models.ForeignKey(Chapter, related_name='lessons', on_delete=models.CASCADE, verbose_name="所属章节")
    title = models.CharField(max_length=200, verbose_name="小节标题")
    content = models.TextField(blank=True, help_text="课程内容的 Markdown 文本", verbose_name="内容")
    code_challenge_prompt = models.TextField(blank=True, help_text="代码挑战的初始代码或提示", verbose_name="代码挑战提示")
    lesson_type = models.CharField(max_length=10, choices=LESSON_TYPES, default='text', verbose_name="课程类型")
    order = models.PositiveIntegerField(default=0, verbose_name="排序")

    class Meta:
        ordering = ['order']
        verbose_name = "小节"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Quiz(models.Model):
    lesson = models.ForeignKey(Lesson, related_name='quizzes', on_delete=models.CASCADE, verbose_name="所属小节")
    question = models.TextField(verbose_name="问题")
    option_a = models.CharField(max_length=200, verbose_name="选项 A")
    option_b = models.CharField(max_length=200, verbose_name="选项 B")
    option_c = models.CharField(max_length=200, verbose_name="选项 C")
    option_d = models.CharField(max_length=200, verbose_name="选项 D")
    correct_answer = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], verbose_name="正确答案")
    explanation = models.TextField(blank=True, help_text="正确答案的解析", verbose_name="解析")

    class Meta:
        verbose_name = "测验"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.lesson.title} 的测验"

class UserCourseProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='course_progress', verbose_name="用户")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="课程")
    is_completed = models.BooleanField(default=False, verbose_name="是否完成")
    completed_at = models.DateTimeField(null=True, blank=True, verbose_name="完成时间")
    
    # 记录学到了哪一课
    current_lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="当前学习小节")

    class Meta:
        unique_together = ('user', 'course')
        verbose_name = "用户课程进度"
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.user.username} - {self.course.title}"

class UserLessonProgress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='lesson_progress', verbose_name="用户")
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name="小节")
    is_completed = models.BooleanField(default=False, verbose_name="是否完成")
    score = models.IntegerField(default=0, help_text="本节测验得分", verbose_name="得分")
    completed_at = models.DateTimeField(auto_now_add=True, verbose_name="完成时间")

    class Meta:
        unique_together = ('user', 'lesson')
        verbose_name = "用户小节进度"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return f"{self.user.username} - {self.lesson.title}"
