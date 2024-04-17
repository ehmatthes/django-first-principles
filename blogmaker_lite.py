from django.conf import settings
from django.http import HttpResponse
from django.urls import path
from django.core.handlers.wsgi import WSGIHandler
from django.core.management import \
    execute_from_command_line

settings.configure(
    ROOT_URLCONF=__name__,
    DEBUG=True,
    SECRET_KEY="my-secret-key",
)

def index(request):
    title = "BlogMaker Lite"
    description = "Start a blog!"

    page_text = f"<h1>{title}</h1>"
    page_text += f"<p>{description}</p>"

    return HttpResponse(page_text)

urlpatterns = [
    path("", index)
]

application = WSGIHandler()

if __name__ == "__main__":
    execute_from_command_line()