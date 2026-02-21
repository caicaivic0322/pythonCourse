from django.urls import path
from .views import RegisterView, CustomAuthToken, UserDetailView, UserStatsView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('me/', UserDetailView.as_view(), name='user-detail'),
    path('stats/', UserStatsView.as_view(), name='user-stats'),
]
