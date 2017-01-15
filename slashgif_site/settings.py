import configparser
import logging
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_FILE = os.path.join(BASE_DIR, 'settings.ini')

config = configparser.ConfigParser()
config.read(CONFIG_FILE)

logging.basicConfig(
    filename=config.get('App', 'log_file'),
    level=logging.getLevelName(config.get('App', 'log_level')),
    format='%(asctime)s - '
           '%(levelname)s %(module)s.%(funcName)s %(lineno)d - '
           '%(message)s',
)

allowed_hosts = config.get('App', 'allowed_hosts')
ALLOWED_HOSTS = allowed_hosts.split(' ')

SECRET_KEY = config.get('App', 'secret')
DEBUG = config.getboolean('App', 'debug')

TEMPLATES_DIRS = [os.path.join(BASE_DIR, 'templates')]
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = config.get('App', 'static_root')
STATIC_URL = '/static/'

WSGI_APPLICATION = 'slashgif_site.wsgi.application'
ROOT_URLCONF = 'slashgif_site.urls'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TEMPLATES_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'slashgif_site.processors.global_variables',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.' +
             'UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.' +
             'MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.' +
             'CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.' +
             'NumericPasswordValidator'},
]
