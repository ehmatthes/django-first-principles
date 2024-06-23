import factory
from faker import Faker

from blogs.models import Blog, BlogPost

fake = Faker()

class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = " ".join(fake.words()).title()
    description = "This is a great sample blog!"