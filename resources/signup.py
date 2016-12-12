# from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_restful import reqparse
from flask_restful import Resource

from models.configure import session
from services.profile import signup
from utils.validations import non_empty_str
from utils.helpers import get_logger

signup_request_format = reqparse.RequestParser()
signup_request_format.add_argument('username', type=non_empty_str, required=True)
signup_request_format.add_argument('password', type=non_empty_str, required=True)
signup_request_format.add_argument('first_name', type=non_empty_str, required=True)
signup_request_format.add_argument('last_name', type=non_empty_str, required=True)
signup_request_format.add_argument('designation', type=non_empty_str, required=True)

api_logger = get_logger('api')
crash_logger = get_logger('crash')


class Signup(Resource):
    def post(self):
        signup_kwargs = signup_request_format.parse_args()
        user_object = signup(**signup_kwargs)
        session.commit()
        return {
            'username': user_object.username,
            'first_name': user_object.first_name,
            'last_name': user_object.last_name,
            'designation': user_object.designation,
        }
