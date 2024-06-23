"""Script to generate sample data."""

import os

import django
from django.core.management import call_command

# Load settings.
os.environ["DJANGO_SETTINGS_MODULE"] = "settings"
django.setup()

# Flush current data.
call_command("flush", "--noinput")
print("Flushed existing db.")