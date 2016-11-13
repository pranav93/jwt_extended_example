from profile import Profile

from flask_restful import Api
from flask_cors import CORS


def create_restful_api(app):
    api = Api(app)

    CORS(app, resources={r"*": {"origins": "*"}})

    api.add_resource(Profile, '/profile')
