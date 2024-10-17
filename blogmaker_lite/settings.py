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


# Fly.io settings.
import os

if os.environ.get("ON_FLYIO_SETUP") or os.environ.get("ON_FLYIO"):
    # Static file configuration needs to take effect during the build process,
    #   and when deployed.
    # from https://whitenoise.evans.io/en/stable/#quickstart-for-django-apps
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATIC_URL = "/static/"
    try:
        STATICFILES_DIRS.append(os.path.join(BASE_DIR, "static"))
    except NameError:
        STATICFILES_DIRS = [os.path.join(BASE_DIR, "static"),]

    i = MIDDLEWARE.index("django.middleware.security.SecurityMiddleware")
    MIDDLEWARE.insert(i + 1, "whitenoise.middleware.WhiteNoiseMiddleware")

if os.environ.get("ON_FLYIO"):
    # These settings need to be in place during deployment, but not during
    #   the setup process.
    # The `dj_database_url.parse()` call causes the build to fail; other settings
    #   here may not.
    import dj_database_url

    # Use secret, if set, to update DEBUG value.
    if os.environ.get("DEBUG") == "FALSE":
        DEBUG = False
    elif os.environ.get("DEBUG") == "TRUE":
        DEBUG = True

    # Set a Fly.io-specific allowed host.
    ALLOWED_HOSTS.append("black-wildflower-2652.fly.dev")

    # Use the Fly.io Postgres database.
    db_url = os.environ.get("DATABASE_URL")
    DATABASES["default"] = dj_database_url.parse(db_url)

    # Prevent CSRF "Origin checking failed" issue.
    CSRF_TRUSTED_ORIGINS = ["https://black-wildflower-2652.fly.dev"]
