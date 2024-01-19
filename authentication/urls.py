from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = "auths"


urlpatterns = [
    path("register/", views.httpRegisterUser, name="index"),
    path("login/", views.httpLogin, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
