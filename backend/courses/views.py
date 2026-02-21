from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Course, Chapter, Lesson, UserCourseProgress, UserLessonProgress, Quiz
from .serializers import CourseSerializer, ChapterSerializer, LessonSerializer

class CourseListView(generics.ListAPIView):
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Course.objects.all().order_by('order')

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        user = request.user
        
        # 获取用户的所有课程进度
        progresses = UserCourseProgress.objects.filter(user=user)
        progress_map = {p.course.id: p for p in progresses}
        
        # 默认解锁第一个课程
        first_course = Course.objects.order_by('order').first()
        
        # 增强返回数据，添加 is_locked 状态
        for course_data in response.data:
            course_id = course_data['id']
            
            # 添加 is_completed 状态
            current_progress = progress_map.get(course_id)
            if current_progress and current_progress.is_completed:
                course_data['is_completed'] = True
            else:
                course_data['is_completed'] = False

            # Superuser always unlocked
            if request.user.is_superuser:
                course_data['is_locked'] = False
                continue

            # Check if user is approved
            if not request.user.is_approved:
                course_data['is_locked'] = True
                continue

            # 1. 第一个课程永远解锁
            if first_course and course_id == first_course.id:
                course_data['is_locked'] = False
                continue
            
            # 2. 检查前一个课程是否完成
            # 找到前一个课程对象
            current_course_order = course_data['order']
            
            prev_course = Course.objects.filter(order__lt=current_course_order).order_by('-order').first()
            
            if prev_course:
                prev_progress = progress_map.get(prev_course.id)
                # 如果前一个课程有进度且已完成，则当前课程解锁
                if prev_progress and prev_progress.is_completed:
                    course_data['is_locked'] = False
                else:
                    course_data['is_locked'] = True
            else:
                # 理论上不会走到这里，因为前面已经处理了第一个课程
                course_data['is_locked'] = False
                
        return response

class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        user = request.user

        # 获取该用户在该课程下的所有 Lesson 进度
        lesson_progresses = UserLessonProgress.objects.filter(user=user, lesson__chapter__course=instance)
        progress_map = {p.lesson.id: p.is_completed for p in lesson_progresses}

        # 遍历章节和课程，计算解锁状态
        # 逻辑：第一个课程永远解锁。后续课程依赖前一个课程完成。
        # 在课程内部：第一个 Lesson 永远解锁。后续 Lesson 依赖前一个 Lesson 完成。
        
        is_first_lesson = True
        previous_completed = True # 第一个 Lesson 默认解锁（因为只要能进这个页面，说明课程已解锁）

        # Superuser always unlocked
        if request.user.is_superuser:
            previous_completed = True
        
        # Check if user is approved
        elif not request.user.is_approved:
            previous_completed = False
            is_first_lesson = False # Force lock everything
        
        for chapter in data['chapters']:
            for lesson in chapter['lessons']:
                lesson_id = lesson['id']
                is_completed = progress_map.get(lesson_id, False)
                lesson['is_completed'] = is_completed
                
                if request.user.is_superuser:
                    lesson['is_locked'] = False
                elif not request.user.is_approved:
                    lesson['is_locked'] = True
                elif is_first_lesson:
                    lesson['is_locked'] = False
                    is_first_lesson = False
                else:
                    lesson['is_locked'] = not previous_completed
                
                # 更新 previous_completed 为当前 lesson 的状态，供下一个 lesson 使用
                previous_completed = is_completed

        return Response(data)

class LessonDetailView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        # 1. Check if user is approved
        if not request.user.is_superuser and not request.user.is_approved:
            return Response(
                {"detail": "You must be approved by an administrator to view lesson content."},
                status=status.HTTP_403_FORBIDDEN
            )

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        
        # 注入用户当前课程的完成状态
        try:
            progress = UserLessonProgress.objects.get(user=request.user, lesson=instance)
            data['user_progress'] = {
                'is_completed': progress.is_completed,
                'score': progress.score
            }
        except UserLessonProgress.DoesNotExist:
            data['user_progress'] = {
                'is_completed': False,
                'score': 0
            }
            
        return Response(data)

class MarkLessonCompleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        lesson = get_object_or_404(Lesson, pk=pk)
        user = request.user
        data = request.data
        
        # 1. 计算 Quiz 得分 (如果有提交 quiz_answers)
        quiz_answers = data.get('quiz_answers') # { quiz_id: selected_option }
        score = 0
        passed = True # 默认通过，除非有测验没过
        
        if quiz_answers:
            quizzes = Quiz.objects.filter(lesson=lesson)
            total_quizzes = quizzes.count()
            if total_quizzes > 0:
                correct_count = 0
                for quiz in quizzes:
                    # 确保 quiz_answers key 是字符串，需要转 int 比较? 前端一般传 string key
                    # 假设 quiz_answers 是 { "1": "A", "2": "B" }
                    user_answer = quiz_answers.get(str(quiz.id))
                    if user_answer == quiz.correct_answer:
                        correct_count += 1
                
                score = int((correct_count / total_quizzes) * 100)
                if score < 50:
                    passed = False
            else:
                score = 100 # 没有测验，默认满分
        else:
            # 如果没有提交答案，检查该课程是否有测验
            # 如果有测验但没提交答案，且之前也没过，则不能通过
            if lesson.quizzes.exists():
                 # 检查是否已经通过
                 try:
                     prev_progress = UserLessonProgress.objects.get(user=user, lesson=lesson)
                     if prev_progress.is_completed:
                         passed = True
                         score = prev_progress.score
                     else:
                         passed = False # 必须做题
                         score = 0
                 except UserLessonProgress.DoesNotExist:
                     passed = False
                     score = 0
            else:
                score = 100 # 无测验直接通过

        # 2. 记录/更新 UserLessonProgress
        lesson_progress, _ = UserLessonProgress.objects.get_or_create(user=user, lesson=lesson)
        
        # 只有当分数更高时才更新分数，或者第一次
        if score > lesson_progress.score:
            lesson_progress.score = score
        
        if passed:
            lesson_progress.is_completed = True
            lesson_progress.save()
            
            # 3. 更新 UserCourseProgress (仅当通过时)
            course = lesson.chapter.course
            course_progress, _ = UserCourseProgress.objects.get_or_create(user=user, course=course)
            course_progress.current_lesson = lesson
            
            # 检查是否完成整个课程
            last_chapter = course.chapters.order_by('-order').first()
            if last_chapter:
                last_lesson = last_chapter.lessons.order_by('-order').first()
                if last_lesson and last_lesson.id == lesson.id:
                    course_progress.is_completed = True
                    course_progress.completed_at = timezone.now()
            
            course_progress.save()
            
            return Response({
                'status': 'success', 
                'passed': True, 
                'score': score,
                'course_completed': course_progress.is_completed
            })
        else:
            lesson_progress.save() # 保存分数即使没过
            return Response({
                'status': 'failed', 
                'passed': False, 
                'score': score,
                'message': f'得分 {score}% 低于 50%，请重试！'
            })
