from flask import Flask

from resources import create_restful_api
from utils.helpers import config


def create_app():

    app = Flask(config.FLASK_APP_NAME)

    app.config.from_object(config)

    create_restful_api(app)

    return app
