import os
from pathlib import Path

# from django.db.backends.postgresql.psycopg_any import IsolationLevel
from dotenv import load_dotenv

# call the load_dotenv() function
load_dotenv(".env", override=True)

ENV_PREFIX = "DJANGO_"
DATABASE_PREFIX = "POSTGRES_"

# define the BASE_DIR for PYTHONPATH
BASE_DIR = Path(__file__).resolve().parent.parent.parent
print("BASEDIR = ", BASE_DIR)


# load from the environment variables
SECRET_KEY = os.getenv(f"{ENV_PREFIX}SECRET_KEY")

# load from the environment variables
try:
    DEBUG = bool(os.getenv(f"{ENV_PREFIX}IS_DEBUG"))


except ValueError:
    DEBUG = False


if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True
    CORS_ALLOW_CREDENTIALS = True
else:
    CORS_ALLOWED_ORIGINS = [...]


# no domain-name, only local development
ALLOWED_HOSTS = [".localhost", "127.0.0.1", "[::1]", "nginx", "0.0.0.0", "*"]


INTERNAL_IPS = ["127.0.0.1", "*"]


# Application definition
INSTALLED_APPS = [
    "channels",
    "daphne",
    "api.user",
    "api.chat",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework_swagger",
    # security
    "corsheaders",
    # debugging
    "debug_toolbar",
    # rest
    "rest_framework",
    "drf_yasg",
    # custom created apps
]

MIDDLEWARE = [
    "api.chat.middlewares.custom.ApplyKafkaProducerMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # additional middlewares
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

# signed cookies enabled
SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
SESSION_COOKIE_HTTPONLY = True

# root url conf module
ROOT_URLCONF = "core.routers.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
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

WSGI_APPLICATION = "core.infrastructure.wsgi.application"


# Database config
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv(f"{DATABASE_PREFIX}DB"),
        "USER": os.getenv(f"{DATABASE_PREFIX}USER"),
        "PASSWORD": os.getenv(f"{DATABASE_PREFIX}PASSWORD"),
        "HOST": os.getenv(f"DB_HOST"),
        "PORT": "5432",
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
STATIC_URL = "src/chatty/static/"

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# config pagination rules


SPECTACULAR_SETTINGS = {
    "TITLE": "Remofirst API",
    "DESCRIPTION": "",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}

# configure logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "standard": {"format": "[%(asctime)s] {%(module)s} [%(levelname)s] - %(message)s", "datefmt": "%d-%m-%Y %H:%M:%S"},
    },
    "handlers": {
        "console": {"level": "DEBUG", "class": "logging.StreamHandler", "formatter": "standard"},
        "file": {"class": "logging.FileHandler", "filename": BASE_DIR / "log/debug.log", "formatter": "standard"},
    },
    "loggers": {
        "core": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": True,
        },
        "api.user": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": True,
        },
        "api.chat": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": True,
        },
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": True,
        },
        "django.request": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "django.server": {
            "handlers": ["console", "file"],
            "level": "ERROR",
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["console", "file"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 30,
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    "EXCEPTION_HANDLER": "api.chat.exceptions.generic.custom_exception_handler",
}


PASSWORD_HASHERS = ["django.contrib.auth.hashers.BCryptSHA256PasswordHasher"]

AUTH_USER_MODEL = "user.User"

STATIC_ROOT = os.path.join(BASE_DIR, "static")

ASGI_APPLICATION = "core.infrastructure.asgi.application"
