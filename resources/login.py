from flask_jwt_extended import create_access_token, create_refresh_token
from flask_restful import Resource
from flask_restful import reqparse

from utils.validations import non_empty_str

from services.profile import login

login_request_format = reqparse.RequestParser()
login_request_format.add_argument('username', type=non_empty_str, required=True)
login_request_format.add_argument('password', type=non_empty_str, required=True)


class Login(Resource):
    def post(self):
        login_kwargs = login_request_format.parse_args()
        user_object = login(**login_kwargs)
        return {
            'access_token': create_access_token(user_object.id),
            'refresh_token': create_refresh_token(user_object.id),
        }
