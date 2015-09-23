"""
Django settings for beratung_erfurt project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: join(BASE_DIR, ...)

from .local import *
from .files import *

from os.path import join


# TODO: create secret_key.txt in the same folder as manage.py
with open(join(BASE_DIR, 'secret_key.txt')) as f:
    SECRET_KEY = f.read().strip()

FIXTURE_DIRS = (join(BASE_DIR, 'fixtures'),)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost']

TEMPLATE_DIRS = (
    join(BASE_DIR, "templates"),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

)

__loaders = (
    'utils.template_loader.Loader',
    'django.template.loaders.app_directories.Loader'
  )
if DEBUG is False:
  TEMPLATE_LOADERS = [(
    'django.template.loaders.cached.Loader',
    __loaders
    )
  ]
else:
  TEMPLATE_LOADERS = __loaders


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django_extensions',
    'beratung_erfurt',
    'dbbackup',
    'utils',
)

# import sys
# if "test" not in sys.argv:
#   INSTALLED_APPS += (
#     "south",
#   )

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'beratung_erfurt.urls'

WSGI_APPLICATION = 'beratung_erfurt.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

STATIC_URL = '/media/'
MEDIA_URL = 'media/'

STATIC_ROOT = "/opt/beratung-erfurt-django/web/media/"
MEDIA_ROOT = join(BASE_DIR, MEDIA_URL)

STATICFILES_DIRS = [
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.

    MEDIA_ROOT,
]
LANGUAGE_CODE = 'de-DE'

TIME_ZONE = 'Europe/Berlin'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

from .db_backup import *
