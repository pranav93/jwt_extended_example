from flask_restful import Resource, abort

from services.profile import get_profile, get_profile_pic
from utils.helpers import get_logger

api_logger = get_logger('api')
slacker = get_logger('crash')


class Profile(Resource):

    def get(self):
        try:
            profile_info = get_profile_pic()
            api_logger.info(profile_info)
            return profile_info
        except KeyError as v:
            slacker.exception(v)
            return abort(400, message=v.message)
