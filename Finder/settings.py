
"""
Django settings for Finder project.

Generated by 'django-admin startproject' using Django 3.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import dj_database_url
from decouple import config

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-#pp^l_$1%k6(^3eas$z*yn@7ga$=^8j9gonyeoh@y=5wn9q6fa'
# SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['finder-app-api.herokuapp.com', '192.168.56.1']
# '192.168.56.1'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'Account',
    'SearchApp',
    'FounderApp',
    'SelectChoice',
    'django_filters',
    'corsheaders',
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:19002",
    # "http://127.0.0.1:9000",
    'https://192.168.56.1',
]

REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS':
['django_filters.rest_framework.DjangoFilterBackend'],

'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Finder.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'Finder.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dbrh0ln8m5oe87',
        'HOST': 'ec2-52-45-183-77.compute-1.amazonaws.com',
        'PORT': 5432,
        'USER': 'aamzhqfukevquo',
        'PASSWORD': '45e71397f5ca44fe793ef13a8cb9f9d55408c747aa5265755a4994395915c67b'
    }
}
# postgres://aamzhqfukevquo:45e71397f5ca44fe793ef13a8cb9f9d55408c747aa5265755a4994395915c67b@ec2-52-45-183-77.compute-1.amazonaws.com:5432/dbrh0ln8m5oe87

# DATABASES = {
#     'default': dj_database_url.config(
#         default=config('DATABASE_URL')
#     )
# }


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'Account.UserProfile'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

















# """
# Django settings for Finder project.
#
# Generated by 'django-admin startproject' using Django 3.2.2.
#
# For more information on this file, see
# https://docs.djangoproject.com/en/3.2/topics/settings/
#
# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/3.2/ref/settings/
# """
# import dj_database_url       # Place this line preferably at the top
# from decouple import config  # Place this line preferably at the top
#
# from pathlib import Path
# import os
#
# # Build paths inside the project like this: BASE_DIR / 'subdir'.
# PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
#
# BASE_DIR = Path(__file__).resolve().parent.parent
#
#
# # Quick-start development settings - unsuitable for production
# # See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/
#
# # SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-#pp^l_$1%k6(^3eas$z*yn@7ga$=^8j9gonyeoh@y=5wn9q6fa'
# # SECRET_KEY = config('SECRET_KEY')
#
# # SECURITY WARNING: don't run with debug turned on in production!
# # DEBUG = True
# DEBUG = config('DEBUG', default=False, cast=bool)
#
# ALLOWED_HOSTS = ['finder-api-app.herokuapp.com','192.168.56.1']
#
#
# # Application definition
#
# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#
#     'rest_framework',
#     'rest_framework.authtoken',
#     'Account',
#     'SearchApp',
#     'FounderApp',
#     'SelectChoice',
#     'django_filters',
#     'corsheaders',
# ]
#
#
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:19002",
#     # "http://127.0.0.1:9000",
#     'https://192.168.56.1',
# ]
# #
#
#
# REST_FRAMEWORK = {
#     'DEFAULT_FILTER_BACKENDS':
#         ['django_filters.rest_framework.DjangoFilterBackend'],
#
#     'DEFAULT_AUTHENTICATION_CLASSES': (
#         'rest_framework.authentication.TokenAuthentication',
#         'rest_framework.authentication.SessionAuthentication',
#     ),
#
#     # 'DEFAULT_PARSER_CLASSES': (
#     #     'rest_framework.parsers.JSONParser',
#     #     'rest_framework.parsers.FormParser',
#     #     'rest_framework.parsers.MultiPartParser',
#     # )
#
# }
#
# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'corsheaders.middleware.CorsMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
# ]
#
# ROOT_URLCONF = 'Finder.urls'
#
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]
#
# WSGI_APPLICATION = 'Finder.wsgi.application'
#
#
# # Database
# # https://docs.djangoproject.com/en/3.2/ref/settings/#databases
#
# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.sqlite3',
# #         'NAME': BASE_DIR / 'db.sqlite3',
# #     }
# # }
#
# DATABASES = {
#     'default': dj_database_url.config(
#         default=config('DATABASE_URL')
#     )
# }
#
#
# # Password validation
# # https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators
#
# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]
#
#
# # Internationalization
# # https://docs.djangoproject.com/en/3.2/topics/i18n/
#
# LANGUAGE_CODE = 'en-us'
#
# TIME_ZONE = 'UTC'
#
# USE_I18N = True
#
# USE_L10N = True
#
# USE_TZ = True
#
#
# # Static files (CSS, JavaScript, Images)
# # https://docs.djangoproject.com/en/3.2/howto/static-files/
#
# STATIC_URL = '/static/'
# STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, 'static'),)
# STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
# MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'media')
# MEDIA_URL = '/media/'
#
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
#
# # Default primary key field type
# # https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field
#
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
#
# AUTH_USER_MODEL = 'Account.UserProfile'
#
# # Here am writting codes for hosting the api on heroku
