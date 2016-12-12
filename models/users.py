from sqlalchemy import Column
from sqlalchemy import String

from models.configure import Model, UNIQUE_ID, CREATED_ON, MODIFIED_ON, DELETED_ON
from utils.data import md5_encrypt


class User(Model):
    __tablename__ = 'user'

    id = UNIQUE_ID.copy()

    username = Column(String(255), unique=True)
    password = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    designation = Column(String(255))

    created_on = CREATED_ON.copy()
    modified_on = MODIFIED_ON.copy()
    deleted_on = DELETED_ON.copy()

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        if kwargs.get('password'):
            self.password = md5_encrypt(kwargs['password'])
