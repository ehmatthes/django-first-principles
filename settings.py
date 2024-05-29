from pathlib import Path

ROOT_URLCONF="blogmaker_lite"

DEBUG=True

SECRET_KEY="my-secret-key"

TEMPLATES=[
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [Path(__file__).parent / "templates"],
        "APP_DIRS": True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }
]

INSTALLED_APPS=[
    "blogs",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    'django.contrib.sessions',
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
]

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(__file__).parent / 'db.sqlite3',
    }
}
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"

STATIC_URL="static/"
STATICFILES_DIRS = [
    "css",
]