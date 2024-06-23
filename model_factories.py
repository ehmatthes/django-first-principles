import factory
from faker import Faker

from blogs.models import Blog, BlogPost

fake = Faker()

def get_title():
    return " ".join(fake.words()).title()

def get_description():
    return fake.sentence(nb_words=10)

class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.LazyFunction(get_title)
    description = factory.LazyFunction(get_description)