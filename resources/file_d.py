import StringIO

from flask import send_file
from flask_restful import Resource

from utils.resource_exceptions import handle_exceptions


class FileDownload(Resource):
    decorators = [handle_exceptions()]

    def get(self):
        str_IO = StringIO.StringIO()
        str_IO.write('Hello from Dan Jacob and Stephane Wirtel !')
        str_IO.seek(0)
        return send_file(str_IO,
                         attachment_filename="testing.txt",
                         as_attachment=True)
