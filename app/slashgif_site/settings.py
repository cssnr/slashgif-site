from decouple import config, Csv
from django.contrib.messages import constants as message_constants
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config('DJANGO_SECRET_KEY')
DEBUG = config('DJANGO_DEBUG', 'False', bool)
ALLOWED_HOSTS = config('DJANGO_ALLOWED', '*', Csv())
SESSION_COOKIE_AGE = config('DJANGO_SESSION', 3600 * 24 * 14, int)

WSGI_APPLICATION = 'slashgif_site.wsgi.application'
ROOT_URLCONF = 'slashgif_site.urls'

LOGIN_URL = '/oauth/'
STATIC_URL = '/static/'
STATIC_ROOT = config('DJANGO_STATIC_DIR')
STATICFILES_DIRS = [BASE_DIR / 'static']
TEMPLATES_DIRS = [BASE_DIR / 'templates']

LANGUAGE_CODE = config('DJANGO_LANGUAGE_CODE', 'en-us')
USE_TZ = config('USE_TZ', 'True', bool)
TIME_ZONE = config('TZ', 'UTC')
USE_I18N = True
USE_L10N = True

STATSD_PREFIX = config('STATSD_PREFIX', 'slashgif.site.dev')
STATSD_PORT = config('STATSD_PORT', 8125, int)
STATSD_HOST = config('STATSD_HOST', 'localhost')
STATSD_CLIENT = 'django_statsd.clients.toolbar'

SLACK_OAUTH_URL = config('SLACK_OAUTH_URL')
SLACK_ACCESS_URL = config('SLACK_ACCESS_URL')
SLACK_CLIENT_ID = config('SLACK_CLIENT_ID')
SLACK_CLIENT_SECRET = config('SLACK_CLIENT_SECRET')
SLACK_REDIRECT_URI = config('SLACK_REDIRECT_URI')
SLACK_OAUTH_SCOPES = config('SLACK_OAUTH_SCOPES')
SLACK_APP_URL = config('SLACK_APP_URL')

STATUS_SITE = config('STATUS_SITE')
DISCORD_HOOK_URL = config('DISCORD_HOOK_URL')

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

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': ('%(asctime)s - '
                       '%(levelname)s - '
                       '%(filename)s '
                       '%(module)s.%(funcName)s:%(lineno)d - '
                       '%(message)s'),
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
            'level': config('DJANGO_LOG_LEVEL', 'INFO'),
            'propagate': True,
        },
        'app': {
            'handlers': ['console'],
            'level': config('APP_LOG_LEVEL', 'DEBUG'),
            'propagate': True,
        },
    },
}
