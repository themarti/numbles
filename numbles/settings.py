"""
Global settings for Numbles.

Global settings that apply regardless of installation are contained
in this file. Installation-specific settings are stored in local_settings.py.
"""

# Determine the directory this file resides in so that an absolute
# path can be specified for the static files and templates
import os.path
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)

USE_TZ = True
TIME_ZONE = 'UTC'

ROOT_URLCONF = 'numbles.urls'
WSGI_APPLICATION = 'numbles.wsgi.application'

# After login, go to the home page
LOGIN_REDIRECT_URL = 'home'

INSTALLED_APPS = (
    # Core Django applications
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Django helper applications
    'widget_tweaks',
    # Numbles applications
    'numbles.accounts',
    'numbles.ledger',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'numbles.middleware.TimezoneMiddleware',
)

# Import all local settings
from local_settings import *
