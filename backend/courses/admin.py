from django.contrib import admin
from .models import Course, Chapter, Lesson, Quiz, UserCourseProgress, UserLessonProgress

class QuizInline(admin.StackedInline):
    model = Quiz
    extra = 0

class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0
    show_change_link = True

class ChapterInline(admin.TabularInline):
    model = Chapter
    extra = 0
    show_change_link = True

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'chapter_count', 'created_at')
    search_fields = ('title', 'description')
    ordering = ('order', 'id')
    inlines = [ChapterInline]

    def chapter_count(self, obj):
        return obj.chapters.count()

    chapter_count.short_description = '章节数'

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    search_fields = ('title', 'course__title')
    ordering = ('course__order', 'order', 'id')
    list_select_related = ('course',)
    inlines = [LessonInline]
    list_filter = ('course',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'chapter', 'course_title', 'lesson_type', 'order', 'quiz_count')
    list_filter = ('lesson_type', 'chapter__course')
    search_fields = ('title', 'chapter__title', 'chapter__course__title')
    ordering = ('chapter__course__order', 'chapter__order', 'order', 'id')
    list_select_related = ('chapter', 'chapter__course')
    inlines = [QuizInline]

    def course_title(self, obj):
        return obj.chapter.course.title

    course_title.short_description = '课程'

    def quiz_count(self, obj):
        return obj.quizzes.count()

    quiz_count.short_description = '测验数'

@admin.register(UserCourseProgress)
class UserCourseProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'current_lesson', 'is_completed', 'completed_at')
    list_filter = ('is_completed', 'course')
    search_fields = ('user__username', 'user__email', 'course__title')
    list_select_related = ('user', 'course', 'current_lesson')
    autocomplete_fields = ('user', 'course', 'current_lesson')

@admin.register(UserLessonProgress)
class UserLessonProgressAdmin(admin.ModelAdmin):
    list_display = ('user', 'lesson', 'is_completed', 'score', 'completed_at')
    list_filter = ('is_completed', 'score')
    search_fields = ('user__username', 'user__email', 'lesson__title', 'lesson__chapter__title')
    list_select_related = ('user', 'lesson', 'lesson__chapter', 'lesson__chapter__course')
    autocomplete_fields = ('user', 'lesson')
