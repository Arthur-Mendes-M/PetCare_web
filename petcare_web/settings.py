"""
Django settings for petcare_web project.

Generated by 'django-admin startproject' using Django 5.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-o#=bkunj**wffhqnf9*hi92c7dgmfl*$(h7z67geq+^8n=bz=w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app']


# Application definition

# CHANGED TO NOT USE A DEPENDENCIES WITH DB
INSTALLED_APPS = [
    'django.contrib.sessions',
    'django.contrib.staticfiles',
    'access',
    'home',
    'sales',
    'analytics',
    'user_profile',
    'reports'
]

# CHANGED TO NOT USE A DEPENDENCIES WITH DB
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'petcare_web.middlewares.AuthenticateRoutes',
    'petcare_web.middlewares.ErrorHandler'
]

ROOT_URLCONF = 'petcare_web.urls'

# CHANGED TO NOT USE A DEPENDENCIES WITH DB
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request'
            ],
        },
    },
]

WSGI_APPLICATION = 'petcare_web.wsgi.app'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# CHANGED TO USE A FAKE DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.dummy'
    }
}

# ADDED FOR CHANGE SESSION STORAGE LOGIC TO NOT USE DB
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

# REMOVED BECAUSE DB IS NOT USED

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'pt-BR'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'templates/static')]

STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'