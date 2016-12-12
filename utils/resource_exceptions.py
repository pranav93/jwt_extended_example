# from functools import wraps
#
# from flask_restful import abort
# from utils.helpers import get_logger
# # from onehop.models import session
# # from sqlalchemy.exc import SQLAlchemyError, IntegrityError
# from zoho.subscription.api import ZohoAPIError
#
# log = get_logger()
# crash_log = get_logger('crash')
#
#
# def handle_exceptions():
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args, **kwargs):
#             try:
#                 return fn(*args, **kwargs)
#             except ValueError as val_err:
#                 log.error(repr(val_err))
#                 session.rollback()
#                 abort(400, message=val_err.message)
#             except KeyError as key_err:
#                 log.error(repr(key_err))
#                 session.rollback()
#                 abort(400, message=key_err.message)
#             except IOError as io_err:
#                 crash_log.exception(io_err)
#                 session.rollback()
#                 abort(500, message="API-ERR-IO")
#             except AuthorizationFailedError as auth_err:
#                 log.error(repr(auth_err))
#                 session.rollback()
#                 abort(403, message="FORBIDDEN")
#             except SMSApiError as sms_err:
#                 crash_log.exception(sms_err)
#                 session.rollback()
#                 abort(500, message=sms_err.message)
#             except NotFoundError as nf_err:
#                 log.exception(repr(nf_err))
#                 session.rollback()
#                 abort(404, message=nf_err.message)
#             except ZohoAPIError as za_err:
#                 crash_log.exception(za_err)
#                 log.debug(za_err.api_response)
#                 session.rollback()
#                 abort(500, message=za_err.message)
#             except AuthorizationTargetError as auth_target_err:
#                 log.error(repr(auth_target_err))
#                 session.rollback()
#                 abort(401, message=auth_target_err.message)
#             except IntegrityError as err:
#                 crash_log.exception(err)
#                 session.rollback()
#                 # pattern = "\'[a-z]+(?:_[a-z]*)*\'"
#                 # matches = re.findall(pattern, err.orig[1])
#                 abort(400, message=err.message)
#             except SQLAlchemyError as sa_err:
#                 crash_log.exception(sa_err)
#                 session.rollback()
#                 abort(500, message="API-ERR-DB")
#             except Exception as exc:
#                 session.rollback()
#                 crash_log.exception(exc)
#                 raise
#
#         return decorator
#
#     return wrapper
