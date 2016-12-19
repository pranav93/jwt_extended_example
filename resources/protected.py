from flask_jwt_extended import get_jwt_claims
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from utils.resource_exceptions import handle_exceptions


class GetAllPermissions(Resource):
    decorators = [jwt_required, handle_exceptions()]

    def get(self):
        user_claims = get_jwt_claims()
        return {'permissions': user_claims['foo']}
