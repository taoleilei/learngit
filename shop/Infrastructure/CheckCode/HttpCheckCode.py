# from UIAdmin.Core.HttpRequest import AdminRequestHandler
from Infrastructure.Core.HttpRequest import BaseRequestHandler
from Infrastructure.CheckCode import check_code
# import check_code
import io


class CheckCodeHandler(BaseRequestHandler):
    """docstring for CheckCodeHandler"""

    def get(self):
        mstream = io.BytesIO()
        img, code = check_code.create_validate_code()
        img.save(mstream, 'GIF')        
        self.session['CheckCode'] = code
        self.write(mstream.getvalue())
