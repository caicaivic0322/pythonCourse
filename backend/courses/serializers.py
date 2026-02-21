from rest_framework import serializers
from .models import Course, Chapter, Lesson, Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = '__all__'

class LessonSerializer(serializers.ModelSerializer):
    next_lesson_id = serializers.SerializerMethodField()
    prev_lesson_id = serializers.SerializerMethodField()
    course_id = serializers.IntegerField(source='chapter.course.id', read_only=True)
    quizzes = QuizSerializer(many=True, read_only=True)

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_next_lesson_id(self, obj):
        # 1. Next in same chapter
        next_in_chapter = Lesson.objects.filter(chapter=obj.chapter, order__gt=obj.order).order_by('order').first()
        if next_in_chapter:
            return next_in_chapter.id
        
        # 2. First in next chapter
        next_chapter = Chapter.objects.filter(course=obj.chapter.course, order__gt=obj.chapter.order).order_by('order').first()
        if next_chapter:
            next_lesson = next_chapter.lessons.order_by('order').first()
            if next_lesson:
                return next_lesson.id
        
        # 3. First lesson of next Course (跨课程跳转)
        current_course = obj.chapter.course
        next_course = Course.objects.filter(order__gt=current_course.order).order_by('order').first()
        if next_course:
            first_chapter = next_course.chapters.order_by('order').first()
            if first_chapter:
                first_lesson = first_chapter.lessons.order_by('order').first()
                if first_lesson:
                    return first_lesson.id
        
        return None

    def get_prev_lesson_id(self, obj):
        # 1. Previous in same chapter
        prev_in_chapter = Lesson.objects.filter(chapter=obj.chapter, order__lt=obj.order).order_by('-order').first()
        if prev_in_chapter:
            return prev_in_chapter.id
        
        # 2. Last in previous chapter
        prev_chapter = Chapter.objects.filter(course=obj.chapter.course, order__lt=obj.chapter.order).order_by('-order').first()
        if prev_chapter:
            prev_lesson = prev_chapter.lessons.order_by('-order').first()
            if prev_lesson:
                return prev_lesson.id
        
        # 3. Last lesson of previous Course (跨课程跳转)
        current_course = obj.chapter.course
        prev_course = Course.objects.filter(order__lt=current_course.order).order_by('-order').first()
        if prev_course:
            last_chapter = prev_course.chapters.order_by('-order').first()
            if last_chapter:
                last_lesson = last_chapter.lessons.order_by('-order').first()
                if last_lesson:
                    return last_lesson.id
        
        return None

class ChapterSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)
    class Meta:
        model = Chapter
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    chapters = ChapterSerializer(many=True, read_only=True)
    class Meta:
        model = Course
        fields = '__all__'
