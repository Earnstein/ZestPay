from . import views
from django.urls import path

app_name = "auths"


urlpatterns = [
    path("register/", views.httpRegisterUser, name="index")
]
