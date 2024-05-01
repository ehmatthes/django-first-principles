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

INSTALLED_APPS=["blogs"]

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(__file__).parent / 'db.sqlite3',
    }
}
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"