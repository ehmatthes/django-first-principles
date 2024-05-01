from pathlib import Path

from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from django.shortcuts import render


def index(request):
    return render(request, "index.html")

urlpatterns = [
    path("", index)
]

application = WSGIHandler()
