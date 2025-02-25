import os
from pathlib import Path

from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "SECRET_KEY", default="1bpsyzvo+3z4nx1=75ug-ey3upt4cx-fd7=uso-8o71e*y#a86"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True, cast=bool)

ALLOWED_HOSTS = ["*"]


# Application definition

INSTALLED_PLUGINS = [
    "admin_interface",
    "colorfield",
    "compressor",
    "crispy_bootstrap5",
    "crispy_forms",
    "django_extensions",
    "django_filters",
    "django_tables2",
    "import_export",
    "registration",
    "tinymce",
    "easy_thumbnails",
    'simple_history',
    'mptt',
    "rosetta",
    "modeltranslation",
    "versatileimagefield",
]

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.humanize",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "user_sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
MODULES = ["web", "exams", "employees", "core", "accounts",  "accounting", "branches", "courses", "admission", ]

INSTALLED_APPS = INSTALLED_PLUGINS + DJANGO_APPS + MODULES



CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

X_FRAME_OPTIONS = "SAMEORIGIN"
SILENCED_SYSTEM_CHECKS = ["security.W019"]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.locale.LocaleMiddleware",
]

ROOT_URLCONF = "oxdu.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "web.context_processors.main_context",
            ]
        },
    }
]

WSGI_APPLICATION = "oxdu.wsgi.application"

LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config("DB_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": config("DB_NAME", default=BASE_DIR / "db.sqlite3"),
        "USER": config("DB_USER", default=""),
        "PASSWORD": config("DB_PASSWORD", default=""),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": "",
    }
}

VERSATILEIMAGEFIELD_SETTINGS = {
    "cache_length": 2592000,
    "cache_name": "versatileimagefield_cache",
    "jpeg_resize_quality": 70,
    "sized_directory_name": "__sized__",
    "filtered_directory_name": "__filtered__",
    "placeholder_directory_name": "__placeholder__",
    "create_images_on_demand": True,
    "image_key_post_processor": None,
    "progressive_jpeg": False,
}

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/


LANGUAGE_CODE = "en-us"
LANGUAGES = [("en", "English"), ("ml", "Malayalam")]
IS_MONOLINGUAL = False
MODELTRANSLATION_DEFAULT_LANGUAGE = "en"
LOCALE_PATHS = [os.path.join(BASE_DIR, "locale")]
ROSETTA_SHOW_AT_ADMIN_PANEL = True

TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True

USE_L10N = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
STATIC_URL = "/static/"
STATIC_FILE_ROOT = BASE_DIR / "static"
STATICFILES_DIRS = ((BASE_DIR / "static"),)
STATIC_ROOT = BASE_DIR / "assets"


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


ACCOUNT_ACTIVATION_DAYS = 7
REGISTRATION_AUTO_LOGIN = True
SEND_ACTIVATION_EMAIL = False
REGISTRATION_EMAIL_SUBJECT_PREFIX = ""

REGISTRATION_OPEN = True
LOGIN_URL = "/accounts/login/"
LOGOUT_URL = "/accounts/logout/"
LOGIN_REDIRECT_URL = "/core/"

SITE_ID = 1
if DEBUG is False:
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
    CSRF_COOKIE_SECURE = True
    COMPRESS_ENABLED = False
    X_FRAME_OPTIONS = "DENY"
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    HTML_MINIFY = True
    KEEP_COMMENTS_ON_MINIFYING = False
    
EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.smtp.EmailBackend"
)
EMAIL_HOST = config("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = config("EMAIL_PORT", default=587)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = config("DEFAULT_FROM_EMAIL", default=EMAIL_HOST_USER)
DEFAULT_BCC_EMAIL = config("DEFAULT_BCC_EMAIL", default=EMAIL_HOST_USER)
DEFAULT_REPLY_TO_EMAIL = config("DEFAULT_REPLY_TO_EMAIL", default=EMAIL_HOST_USER)
SERVER_EMAIL = config("SERVER_EMAIL", default=EMAIL_HOST_USER)
ADMIN_EMAIL = config("ADMIN_EMAIL", default=EMAIL_HOST_USER)


CSRF_TRUSTED_ORIGINS = ["https://8000-gedexomainse-production-cete37r1o1j.ws-us110.gitpod.io"]

THUMBNAIL_ALIASES = {'': {'avatar': {'size': (50, 50), 'crop': True}}}

GRAPH_MODELS = {'all_applications': True, 'group_models': True}

AUTH_USER_MODEL = "accounts.User"
