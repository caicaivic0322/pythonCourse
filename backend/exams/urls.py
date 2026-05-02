from django.urls import path
from . import views

urlpatterns = [
    path('', views.ExamListView.as_view(), name='exam-list'),
    path('<int:pk>/', views.ExamDetailView.as_view(), name='exam-detail'),
    path('<int:pk>/start/', views.ExamStartView.as_view(), name='exam-start'),
    path('<int:pk>/submit/', views.ExamSubmitView.as_view(), name='exam-submit'),
    path('results/<int:pk>/', views.ExamResultView.as_view(), name='exam-result'),
    path('history/', views.ExamHistoryView.as_view(), name='exam-history'),
]
