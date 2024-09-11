import os
from django.core.management import execute_from_command_line

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "blogmaker_lite.settings")
    execute_from_command_line()
