from rest_framework.routers import DefaultRouter
from django.urls import include, path
from api.user.routers.views import RegisterUser, LoginUser, LogoutUser


urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register-user'),
    path('login/', LoginUser.as_view(), name='login-user'),
    path('logout/', LogoutUser.as_view(), name='logout-user')
]
