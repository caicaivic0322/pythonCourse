from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model
from django.db.models import Sum, Count
from .serializers import UserSerializer, RegisterSerializer
from courses.models import UserLessonProgress, UserCourseProgress

User = get_user_model()

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'username': user.username,
            # 'is_approved': user.is_approved
        })

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

class UserStatsView(generics.GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        user = request.user
        
        # 1. 经验值 (XP): 所有 completed lessons 的分数总和 + 额外奖励 (e.g. 50 XP per lesson)
        # 这里简单点：score 是百分制，直接作为 XP
        lesson_progress = UserLessonProgress.objects.filter(user=user, is_completed=True)
        total_xp = lesson_progress.aggregate(total_score=Sum('score'))['total_score'] or 0
        
        # 2. 勋章 (Badges): 完成的课程数量
        badges_count = UserCourseProgress.objects.filter(user=user, is_completed=True).count()
        
        # 3. 学习课程 (Enrolled Courses): 正在进行的课程 + 完成的课程
        courses_count = UserCourseProgress.objects.filter(user=user).count()
        
        # 4. 学习时长 (Study Time): 完成的小节数 * 20分钟 (0.33小时)
        completed_lessons_count = lesson_progress.count()
        study_hours = round(completed_lessons_count * 0.33, 1) # 保留一位小数
        
        # 如果是 admin，给点初始数据好看点
        if user.is_superuser and total_xp == 0:
            total_xp = 1250
            badges_count = 3
            courses_count = 4
            study_hours = 12.5

        return Response({
            'xp': total_xp,
            'badges': badges_count,
            'courses_learned': courses_count,
            'study_hours': study_hours
        })
