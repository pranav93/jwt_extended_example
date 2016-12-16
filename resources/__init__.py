from resources.protected import GetAllPermissions
from resources.refresh import Refresh
from resources.signup import Signup
from resources.login import Login

from flask_restful import Api
from flask_cors import CORS


def create_restful_api(app):
    api = Api(app)

    CORS(app, resources={r"*": {"origins": "*"}})

    api.add_resource(Signup, '/signup')
    api.add_resource(Login, '/login')
    api.add_resource(Refresh, '/refresh')
    api.add_resource(GetAllPermissions, '/permissions')
