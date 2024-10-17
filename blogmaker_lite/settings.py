from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
ALLOWED_HOSTS = []

ROOT_URLCONF="blogmaker_lite.urls"

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
    "accounts",
    "simple_deploy",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    'django.contrib.sessions',
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DATABASES={
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': Path(__file__).parents[1] / 'db.sqlite3',
    }
}
DEFAULT_AUTO_FIELD="django.db.models.BigAutoField"

STATIC_URL="static/"
STATICFILES_DIRS = [
    "css",
]

STATIC_ROOT = "staticfiles/"

LOGIN_REDIRECT_URL = "blogs:index"
LOGOUT_REDIRECT_URL = "blogs:index"
