import factory
from faker import Faker

from blogs.models import Blog, BlogPost

fake = Faker()

def get_title():
    return " ".join(fake.words()).title()

class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.LazyFunction(get_title)
    description = "This is a great sample blog!"