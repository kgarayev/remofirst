from rest_framework.routers import DefaultRouter
from django.urls import include, path
from src.chatty.api.user.routers.views import RegisterUser, LoginUser


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register-user'),
    path('login/', LoginUser.as_view(), name='login-user'),
]
