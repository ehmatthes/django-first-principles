from pathlib import Path

from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from django.shortcuts import render
from django.contrib import admin

from blogs.models import Blog, BlogPost


admin.site.register((Blog, BlogPost))

def index(request):
    return render(request, "index.html")

def blogs(request):
    all_blogs = Blog.objects.all()
    context = {"blogs": all_blogs}
    return render(request, "blogs.html", context)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blogs/", blogs),
    path("", index),
]

application = WSGIHandler()
