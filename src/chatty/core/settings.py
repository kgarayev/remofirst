from pathlib import Path
import os
from dotenv import load_dotenv

# call the load_dotenv() function
load_dotenv('../../.env')

ENV_PREFIX = "DJANGO_"
DATABASE_PREFIX = "POSTGRES_"

# define the BASE_DIR for PYTHONPATH
BASE_DIR = Path(__file__).resolve().parent.parent
print("PYTHONPATH = ", BASE_DIR)


# load from the environment variables
SECRET_KEY = os.getenv(f"{ENV_PREFIX}SECRET_KEY")
print(SECRET_KEY)

# load from the environment variables
try:
    DEBUG = bool(os.getenv(f"{ENV_PREFIX}IS_DEBUG"))


except ValueError:
    DEBUG = False
    

if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOW_CREDENTIALS = True
else:
    CORS_ALLOWED_ORIGINS = [
        ...
]


# no domain-name, only local development
ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]', 'nginx']



INTERNAL_IPS = [
    '127.0.0.1'
]


# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    # security 
    "corsheaders",

    # debugging
    "debug_toolbar",

    # rest
    "rest_framework"


]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",

    # additional middlewares
    "corsheaders.middleware.CorsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# signed cookies enabled
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_HTTPONLY = True

# root url conf module
ROOT_URLCONF = "core.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database config
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv(f"{DATABASE_PREFIX}DB"),
        "USER": os.getenv(f"{DATABASE_PREFIX}USER"),
        "PASSWORD": os.getenv(f"{DATABASE_PREFIX}PASSWORD"),
        "HOST": os.getenv(f"127.0.0.1"),
        "PORT": os.getenv(f"5432")
    }
}


# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Baku"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = "static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# config pagination rules
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 30
}