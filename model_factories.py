from random import randint, choice

import factory
from faker import Faker

from django.contrib.auth.models import User

from blogs.models import Blog, BlogPost

fake = Faker()

def get_username():
    return fake.email().split("@")[0]

def get_title():
    return " ".join(fake.words()).title()

def get_description():
    return fake.sentence(nb_words=10)

def get_body():
    paragraphs = [
        fake.paragraph(randint(5,10))
        for _ in range(randint(3,25))
    ]
    return "\n\n".join(paragraphs)

def get_blog_owner():
    users = User.objects.all()
    return choice(users)

def get_blog():
    blogs = Blog.objects.all()
    return choice(blogs)

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.LazyFunction(get_username)
    password = "fake_pw"

class BlogFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Blog

    title = factory.LazyFunction(get_title)
    description = factory.LazyFunction(get_description)
    owner = factory.LazyFunction(get_blog_owner)

class BlogPostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = BlogPost

    title = factory.LazyFunction(get_title)
    body = factory.LazyFunction(get_body)
    blog = factory.LazyFunction(get_blog)
