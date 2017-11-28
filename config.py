from __future__ import absolute_import
from os import path

FLASK_APP_NAME = 'jwt_extended'
secret_key = 'super-secret'

pwd = path.dirname(path.realpath('__file__'))

SQLALCHEMY_DATABASE_URI = 'mysql://root:p@localhost/jwt_extended'
SQLALCHEMY_CONVERT_UNICODE = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_CYCLE = 3600
DEFAULT_LOGGER_NAME = 'api'

LOGGING_CONFIG = dict(
        version=1,
        formatters={
            'compact': {
                'format': '%(asctime)s [%(levelname)-8.8s] %(name)-10.10s : %(message)s'
            },
            'verbose': {
                'format': '%(asctime)s [%(levelname)-8.8s] %(name)-8.8s [%(filename)-15.15s:%(lineno)-3.3s]: %(message)s'
            },
            'err_report': {
                'format': '%(asctime)s\n%(message)s'
            }
        },
        handlers={
            'default': {
                'class': 'logging.StreamHandler',
                'formatter': 'verbose'
            },
        },
        loggers={
            '': {
                'handlers': ['default'],
                'level': 'DEBUG'
            },
            'cron': {
                'handlers': ['default'],
                'level': 'DEBUG',
                'propagate': False
            },
            'api': {
                'handlers': ['default'],
                'level': 'DEBUG',
                'propagate': False
            },
            'crash': {
                'handlers': ['default'],
                'level': 'ERROR',
                'propagate': False
            }
        }
    )
