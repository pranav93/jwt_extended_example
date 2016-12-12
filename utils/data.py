from __future__ import absolute_import

import hashlib
import uuid

from datetime import datetime


def generate_unique_business_id():
    return str(uuid.uuid4())


def get_date_time():
    return datetime.now()


def md5_encrypt(val):
    return hashlib.md5(val).hexdigest()
