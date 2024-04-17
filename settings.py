from pathlib import Path

ROOT_URLCONF="blogmaker_lite"

DEBUG=True

SECRET_KEY="my-secret-key"

TEMPLATES=[
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [Path(__file__).parent / "templates"],
    }
]