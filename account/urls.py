from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import UserListAPIView, Login


urlpatterns = [
    path('api/token/', Login.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('users/', UserListAPIView.as_view()),
]