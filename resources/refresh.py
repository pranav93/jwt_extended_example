from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_refresh_token_required
from flask_restful import Resource

from utils.resource_exceptions import handle_exceptions


class Refresh(Resource):
    decorators = [jwt_refresh_token_required, handle_exceptions()]

    def post(self):
        current_user_id = get_jwt_identity()
        return {'access_token': create_access_token(identity=current_user_id)}
