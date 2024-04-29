from api.user.routers.views import GetCookies, LoginUser, LogoutUser, RegisterUser
from django.urls import path

urlpatterns = [
    path("register/", RegisterUser.as_view(), name="register-user"),
    path("login/", LoginUser.as_view(), name="login-user"),
    path("logout/", LogoutUser.as_view(), name="logout-user"),
    path("get-cookies", GetCookies.as_view(), name="get-cookies"),
]

