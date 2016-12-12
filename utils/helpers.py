from __future__ import absolute_import

import logging
import logging.config
from utils.basic_config import get_config

__logging_configured = False
config = get_config('/home/pranav/presentation/jwt_extended/config.py')


def get_logger(logger_name=None):
    global __logging_configured
    if not __logging_configured:
        logging.config.dictConfig(config.LOGGING_CONFIG)
        __logging_configured = True
    logger = logging.getLogger(logger_name or config.DEFAULT_LOGGER_NAME)
    return logger
