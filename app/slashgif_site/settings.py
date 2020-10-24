import os
from distutils.util import strtobool

ROOT_URLCONF = 'home.urls'
WSGI_APPLICATION = 'slashgif_site.wsgi.application'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.environ['DJANGO_DATA_DIR']

LOGIN_URL = '/oauth/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
TEMPLATES_DIRS = [os.path.join(BASE_DIR, 'templates')]

SESSION_COOKIE_AGE = int(os.getenv('DJANGO_SESSION', 1209600))
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED', '*').strip('"').split(' ')
DEBUG = strtobool(os.getenv('DJANGO_DEBUG', 'True'))
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY')
STATIC_ROOT = os.getenv('DJANGO_STATIC_DIR')

DATETIME_FORMAT = os.getenv('DATETIME_FORMAT', 'N j, Y, f A').strip('"')
TIME_ZONE = os.getenv('TZ', 'America/Los_Angeles')
LANGUAGE_CODE = os.getenv('DJANGO_LANGUAGE_CODE', 'en-us')

STATSD_PREFIX = os.getenv('STATSD_PREFIX', 'smwcweb.dev')
STATSD_PORT = int(os.getenv('STATSD_PORT', 8125))
STATSD_HOST = os.getenv('STATSD_HOST', 'localhost')
STATSD_CLIENT = 'django_statsd.clients.toolbar'

SLACK_OAUTH_URL = os.getenv('SLACK_OAUTH_URL')
SLACK_ACCESS_URL = os.getenv('SLACK_ACCESS_URL')
SLACK_CLIENT_ID = os.getenv('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = os.getenv('SLACK_CLIENT_SECRET')
SLACK_REDIRECT_URI = os.getenv('SLACK_REDIRECT_URI')
SLACK_OAUTH_SCOPES = os.getenv('SLACK_OAUTH_SCOPES')
SLACK_APP_URL = os.getenv('SLACK_APP_URL')

STATUS_SITE = os.getenv('STATUS_SITE')
DISCORD_HOOK_URL = os.getenv('DISCORD_HOOK_URL')

USE_I18N = True
USE_L10N = True
USE_TZ = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s - %(levelname)s - %(filename)s %(module)s.%(funcName)s:%(lineno)d - %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
        'app': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_APP_LOG_LEVEL', 'DEBUG'),
            'propagate': True,
        },
    },
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django_extensions',
    'django_statsd',
    'home',
]

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
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
                'django.template.context_processors.static',
            ],
        },
    },
]
