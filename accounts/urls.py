from django.urls import path, include
from django.contrib.auth import urls as auth_urls

from . import views

app_name = "accounts"
urlpatterns = [
    path("", include(auth_urls)),
    path("register/", views.register, name="register"),
]
