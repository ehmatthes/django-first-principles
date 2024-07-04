from django.urls import path

from . import views

app_name = "blogs"
urlpatterns = [
    path("blogs/", views.blogs, name="blogs"),
    path("blogs/<int:blog_id>/", views.blog, name="blog"),
    path("posts/<int:post_id>/", views.post, name="post"),
    path("", views.index, name="index"),
]