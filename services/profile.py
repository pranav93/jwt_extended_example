from __future__ import absolute_import

from flask_jwt_extended import create_access_token

from models import User
from models.configure import session
from utils.data import md5_encrypt
from utils.errors import AuthenticationError


def signup(**kwargs):
    user_object = User(**kwargs)
    session.add(user_object)
    return user_object


def login(**kwargs):
    username = kwargs.get('username', None)
    password = kwargs.get('password', None)
    user_obj = session.query(User).filter(User.username == username).first()

    if not user_obj:
        raise AuthenticationError('No such user')

    if user_obj.password == md5_encrypt(password):
        return user_obj
    else:
        raise AuthenticationError('Wrong Password')
