"""Script to generate sample data."""

import argparse
import os

import django
from django.core.management import call_command

# Parse CLI args.
parser = argparse.ArgumentParser()
parser.add_argument("--num-blogs", type=int, default=10)
parser.add_argument("--num-posts", type=int, default=100)
args = parser.parse_args()

# Load settings.
os.environ["DJANGO_SETTINGS_MODULE"] = "blogmaker_lite.settings"
django.setup()

# Flush current data.
call_command("flush", "--noinput")
print("Flushed existing db.")

# Create a superuser.
os.environ["DJANGO_SUPERUSER_PASSWORD"] = "fake_pw"

cmd = "createsuperuser --username fake_admin"
cmd += " --email fake_email@example.com"
cmd += " --noinput"

cmd_parts = cmd.split()
call_command(*cmd_parts)

# Create sample users.
from model_factories import UserFactory

num_users = int(args.num_blogs / 3)
for _ in range(num_users):
    UserFactory.create()
print(f"Generated {num_users} sample users.")

# Create sample blogs.
from model_factories import BlogFactory, BlogPostFactory

for _ in range(args.num_blogs):
    BlogFactory.create() 
print(f"Generated {args.num_blogs} sample blogs.")

for _ in range(args.num_posts):
    BlogPostFactory.create()
print(f"Generaged {args.num_posts} sample posts.")
