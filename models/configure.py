from utils.helpers import config
from utils.data import generate_unique_business_id, get_date_time
from sqlalchemy import (
    orm, create_engine, Column, String, DateTime, TIMESTAMP, text
)
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base()
engine = create_engine(config.SQLALCHEMY_DATABASE_URI,
                       convert_unicode=config.SQLALCHEMY_CONVERT_UNICODE,
                       pool_recycle=config.SQLALCHEMY_POOL_CYCLE,
                       echo=config.SQLALCHEMY_ECHO)
# Why pool_recycle : http://docs.sqlalchemy.org/en/rel_0_9/dialects/mysql.html#connection-timeouts
_Session = orm.sessionmaker(autocommit=False, autoflush=True, bind=engine)
session = orm.scoped_session(_Session)
Model.metadata.bind = engine
Model.query = session.query_property()

UNIQUE_ID = Column(String(36), primary_key=True, default=generate_unique_business_id)

CREATED_ON = Column(DateTime, default=get_date_time)
MODIFIED_ON = Column(TIMESTAMP, nullable=False, default=get_date_time,
                     server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
DELETED_ON = Column(DateTime)

# NOTE Not using Mixin because the order of columns is important for us
