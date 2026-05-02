from django.contrib import admin
from .models import Exam, Question, UserExamAttempt, UserAnswer


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    fields = ['question_number', 'question_type', 'content', 'correct_answer', 'score']


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ['title', 'duration_minutes', 'total_score', 'passing_score', 'is_published', 'question_count', 'created_at']
    list_filter = ['is_published']
    search_fields = ['title', 'description']
    inlines = [QuestionInline]


class UserAnswerInline(admin.TabularInline):
    model = UserAnswer
    extra = 0
    readonly_fields = ['question', 'selected_answer', 'is_correct']
    can_delete = False


@admin.register(UserExamAttempt)
class UserExamAttemptAdmin(admin.ModelAdmin):
    list_display = ['user', 'exam', 'score', 'correct_count', 'total_questions', 'is_passed', 'started_at', 'submitted_at']
    list_filter = ['is_passed', 'exam']
    search_fields = ['user__username', 'user__email', 'exam__title']
    readonly_fields = ['started_at', 'submitted_at']
    inlines = [UserAnswerInline]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['exam', 'question_number', 'question_type', 'content_preview', 'correct_answer', 'score']
    list_filter = ['exam', 'question_type']
    search_fields = ['content']

    def content_preview(self, obj):
        return obj.content[:50]
    content_preview.short_description = '题目预览'
