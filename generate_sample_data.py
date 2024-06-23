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

# Create a superuser.
os.environ["DJANGO_SUPERUSER_PASSWORD"] = "fake_pw"

cmd = "createsuperuser --username fake_admin"
cmd += " --email fake_email@example.com"
cmd += " --noinput"

cmd_parts = cmd.split()
call_command(*cmd_parts)