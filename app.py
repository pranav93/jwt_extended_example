from flask import Flask
from flask_jwt_extended import JWTManager
from models import session, User

from resources import create_restful_api
from utils.helpers import config


def create_app():

    app = Flask(config.FLASK_APP_NAME)
    app.secret_key = config.secret_key
    jwt = JWTManager(app=app)

    @jwt.user_claims_loader
    def add_claims_to_access_token(identity):
        user_obj = session.query(User).filter(User.id == identity).first()
        return {
            'id': identity,
            'first_name': user_obj.first_name,
            'superpowers': ['super_speed', 'fly', 'be_a_batman']
        }

    create_restful_api(app)
    return app
