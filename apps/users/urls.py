from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import UserAPIView, UserRegisterAPI

urlpatterns = [
    path('', UserAPIView.as_view(), name='api_users'),
    path('register/', UserRegisterAPI.as_view(), name='api-register'),
    
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]