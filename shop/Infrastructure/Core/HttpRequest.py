import tornado.web
from Infrastructure.Session.SessionFacotry import SessionFactory
import Config


class BaseRequestHandler(tornado.web.RequestHandler):
    """docstring for BaseRequestHandler"""

    def initialize(self):
        self.session = SessionFactory.get_session()
        self.session.initialize(self, Config.SESSION_EXPIRES)
