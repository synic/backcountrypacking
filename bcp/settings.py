# Django settings for dc project.

import os
from os.path import dirname

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.join(dirname(os.path.abspath(__file__)))
PATHOF = lambda *x: os.path.join(BASE_DIR, *x)  # noqa

DEBUG = os.getenv('BCP_DEV', False) in ('t', 'T', '1', True)
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

ALLOWED_HOSTS = [
    "backcountrypacking.com",
    "www.backcountrypacking.com",
    "hollowrockoutfitters.com",
    "www.hollowrockoutfitters.com",
]

if os.getenv('BCP_DEV', '') == '1':
    ALLOWED_HOSTS.append('localhost')

MANAGERS = ADMINS

DATABASE_URI = os.getenv(
    'DATABASE_URI',
    'postgres://postgres:bcp@bcp-db/postgres',
)
DATABASES = {
    'default': dj_database_url.config(default=DATABASE_URI),
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Phoenix'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'storage', 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'aayjjd6(jq#)58w2d^7k&)9)z&7foooqti!nk_o*k^0w(pf@ah'

STATICFILES_DIRS = (
    PATHOF('staticfiles'),
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bcp.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['/var/www/backcountrypacking/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'bcp.dropcamp.context_processors.link',
            ],
        },
    },
]


INSTALLED_APPS = (
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_markup',

    # third party
    'sorl.thumbnail',

    # ours
    'bcp.aolib',
    'bcp.chunks',
    'bcp.dropcamp',
)

STATIC_ROOT = os.path.join(BASE_DIR, '..', 'storage', 'static')
STATIC_URL = '/static/'

CONTACT_EMAIL = 'arolsen@gmail.com'

COMMIT_SHA = os.getenv('COMMIT_SHA', 'unknown')
COMMIT_BRANCH = os.getenv('COMMIT_BRANCH', 'unknown')
BUILD_DATE = os.getenv('BUILD_DATE', 'unknown')
BUILD_INFO = f'{COMMIT_BRANCH}:{COMMIT_SHA}@{BUILD_DATE}'

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
