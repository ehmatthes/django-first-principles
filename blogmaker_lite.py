from django.urls import path, include
from django.core.handlers.wsgi import WSGIHandler
from django.contrib import admin

from blogs import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blogs.urls")),
]

application = WSGIHandler()
