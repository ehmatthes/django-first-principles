from django.urls import path, include
from django.core.handlers.wsgi import WSGIHandler
from django.contrib import admin


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("", include("blogs.urls")),
]

application = WSGIHandler()
