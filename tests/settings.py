from pathlib import Path
from dotenv import load_dotenv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.

#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/


load_dotenv()
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'viewflow.frontend', 
    'viewflow',   
    'material',
    'material.frontend',
    'material.admin',

#    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    'datahub.pipeline',
    'tests'
)

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = 'tests.urls'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR,"db.sqlite3"),
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

MIGRATION_MODULES = {
    'frontend': None,
    'material': None,
    'admin': None,
    'auth': None,
    'contenttypes': None,
    'sessions': None,
    'messages': None,
    'staticfiles': None,
    'viewflow_frontend': None,
    'viewflow': None,
    'tests': None,
    'pipeline': None
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
            'debug': True,
        },
    },
]

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'viewflow/locale'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


# Celery

CELERYD_CONCURRENCY = 1
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_BROKER_URL = 'redis://localhost:6379/10'

CELERY_IMPORTS = [
    os.path.join(root, filename)[len(BASE_DIR)+1: -3].replace('/', '.')
    for root, dirs, files in os.walk(os.path.join(BASE_DIR, 'tests'))
    for filename in files
    if filename.startswith('test_') and filename.endswith('.py')]

DJKOMBU_POLLING_INTERVAL = 0.05
