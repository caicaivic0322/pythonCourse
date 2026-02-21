from django.contrib import admin
from .models import Course, Chapter, Lesson, Quiz, UserCourseProgress, UserLessonProgress

class QuizInline(admin.StackedInline):
    model = Quiz
    extra = 1

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 1

class ChapterInline(admin.StackedInline):
    model = Chapter
    extra = 1

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'created_at')
    inlines = [ChapterInline]

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    inlines = [LessonInline]
    list_filter = ('course',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'lesson_type', 'order')
    list_filter = ('lesson_type', 'chapter__course')
    inlines = [QuizInline]

@admin.register(UserCourseProgress)
class UserCourseProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'is_completed', 'completed_at')
    list_filter = ('is_completed', 'course')

@admin.register(UserLessonProgress)
class UserLessonProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'is_completed', 'score', 'completed_at')
    list_filter = ('is_completed', 'score')
