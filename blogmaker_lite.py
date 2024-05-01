from pathlib import Path

from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from django.shortcuts import render
from django.contrib import admin

from blogs.models import Blog


admin.site.register(Blog)

def index(request):
    return render(request, "index.html")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", index)
]

application = WSGIHandler()
