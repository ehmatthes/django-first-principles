from pathlib import Path

from django.conf import settings
from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import \
    execute_from_command_line
from django.shortcuts import render

settings.configure(
    ROOT_URLCONF=__name__,
    DEBUG=True,
    SECRET_KEY="my-secret-key",
    TEMPLATES=[
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [Path(__file__).parent / "templates"],
        }
    ],
)

def index(request):
    return render(request, "index.html")

urlpatterns = [
    path("", index)
]

application = WSGIHandler()

if __name__ == "__main__":
    execute_from_command_line()