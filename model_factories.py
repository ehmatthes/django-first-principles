import factory
from faker import Faker

from blogs.models import Blog, BlogPost

class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = "My Sample Blog"
    description = "This is a great sample blog!"