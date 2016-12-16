from __future__ import absolute_import
from os import path

FLASK_APP_NAME = 'jwt_extended'
secret_key = 'super-secret'

pwd = path.dirname(path.realpath('__file__'))

SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/jwt_extended'
SQLALCHEMY_CONVERT_UNICODE = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_POOL_CYCLE = 3600

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
            'slacker': {
                'class': 'utils.slacker.SlackHandler',
                'url': 'https://hooks.slack.com/services/xyz',
                'channel': 'pranavdev',
                'username': 'crash_jabber',
                'icon_emoji': ':ghost:'
            },
            'cron': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'formatter': 'verbose',
                'level': 'DEBUG',
                'filename': '%s/%s' % (pwd, 'logs/cron/cron.log'),
                'interval': 1,
                'when': 'midnight',
                'encoding': 'utf8'
            },
            'api': {
                'class': 'logging.handlers.TimedRotatingFileHandler',
                'formatter': 'verbose',
                'level': 'DEBUG',
                'filename': '%s/%s' % (pwd, 'logs/api/api.log'),
                'interval': 1,
                'when': 'midnight',
                'encoding': 'utf8'
            },
            'critical_err': {
                'class': 'logging.handlers.SMTPHandler',
                'formatter': 'err_report',
                'mailhost': ("localhost", 25),
                'fromaddr': 'no-reply@onehop.co',
                'toaddrs': [
                        'some@some.com'
                ],
                'subject': '[Dev] Onehop : Something bad happened'
            },
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
                'handlers': ['cron'],
                'level': 'DEBUG',
                'propagate': False
            },
            'api': {
                'handlers': ['api'],
                'level': 'DEBUG',
                'propagate': False
            },
            'crash': {
                'handlers': ['critical_err', 'api', 'slacker'],
                'level': 'ERROR',
                'propagate': False
            }
        }
    )
