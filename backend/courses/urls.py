from django.urls import path
from .views import CourseListView, CourseDetailView, LessonDetailView, MarkLessonCompleteView

urlpatterns = [
    path('', CourseListView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('lessons/<int:pk>/complete/', MarkLessonCompleteView.as_view(), name='lesson-complete'),
]
