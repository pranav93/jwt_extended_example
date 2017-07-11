from functools import wraps

from flask_restful import abort
from utils.helpers import get_logger
from models import session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

log = get_logger()
crash_log = get_logger('crash')


def handle_exceptions():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except ValueError as val_err:
                log.exception(repr(val_err))
                session.rollback()
                abort(400, message=val_err.message)
            except KeyError as key_err:
                log.exception(repr(key_err))
                session.rollback()
                abort(400, message=key_err.message)
            except IOError as io_err:
                crash_log.exception(io_err)
                session.rollback()
                abort(500, message="API-ERR-IO")
            except IntegrityError as err:
                crash_log.exception(err)
                session.rollback()
                # pattern = "\'[a-z]+(?:_[a-z]*)*\'"
                # matches = re.findall(pattern, err.orig[1])
                abort(400, message=err.message)
            except SQLAlchemyError as sa_err:
                crash_log.exception(sa_err)
                session.rollback()
                abort(500, message="API-ERR-DB")
            except Exception as exc:
                session.rollback()
                crash_log.exception(exc)
                raise

        return decorator

    return wrapper
