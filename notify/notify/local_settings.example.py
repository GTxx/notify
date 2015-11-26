# change secret_key in production env
SECRET_KEY = '1234567898'

DEBUG = False

# allow all hosts can visit
ALLOWED_HOSTS = ['*']

# log
import os


HOME_PATH = os.path.expanduser('~')


LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'logerrortofile': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'formatter': 'verbose',
            'filename': os.path.join(HOME_PATH, 'django-error.log')
        },
        'loginfotofile': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'simple',
            'filename': os.path.join(HOME_PATH, 'django-info.log')
        },
    },
    'loggers': {
        'django': {
            'handlers': ['loginfotofile'],
            'propagate': True,
            'level': 'INFO',
        },
        'django.request': {
            'handlers': ['logerrortofile'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}
