"""
❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤
Django settings for sonora project.
❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤❤
"""
import sys
import os


def env_to_bool(env, default):
    str_val = os.environ.get(env)
    return default if str_val is None else str_val == 'True'


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env_to_bool('DJANGO_DEBUG', True)

TESTING = os.environ.get('DJANGO_TESTING')

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*', '127.0.0.1', 'sonora.com']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'mdeditor',
    'blog',
    'accounts',
    'comments',
    'oauth',
    'servermanager',
    'owntracks'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'blog.middleware.OnlineMiddleware'
]

ROOT_URLCONF = 'sonora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'blog.context_processors.seo_processor'
            ],
        },
    },
]

WSGI_APPLICATION = 'sonora.wsgi.application'

# Database
DATABASES = {
    'default': {'ENGINE': os.environ.get('DJANGO_ENGINE'),
                'NAME': os.environ.get('DJANGO_MYSQL_DATABASE'),
                'USER': os.environ.get('DJANGO_MYSQL_USER'),
                'PASSWORD': os.environ.get('DJANGO_MYSQL_PASSWORD'),
                'HOST': os.environ.get('DJANGO_MYSQL_HOST'),
                'PORT': int(os.environ.get('DJANGO_MYSQL_PORT'),
                'OPTIONS': {'charset': 'utf8mb4'}}
            }

TIME_FORMAT = '%Y-%m-%d %H:%M:%S'
DATE_TIME_FORMAT = '%Y-%m-%d'

MEDIA_ROOT = os.path.join(BASE_DIR, 'uploads')
MEDIA_URL = '/media/'
