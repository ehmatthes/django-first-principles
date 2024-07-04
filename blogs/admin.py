from django.contrib import admin

from .models import Blog, BlogPost

admin.site.register((Blog, BlogPost))